#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Публичная выгрузка для репозитория SKB-BY/cbr-news-materials (t50u, 12.11.2026).

Собирает в каталог --out:
  АКТУАЛЬНЫЙ_ОТЧЁТ.md          — подтверждённые новости по темам (утверждения — где без них картина неполна),
                                 программы DARPA; у каждого материала коды ОИ 5×5 (Первоначальная ОИ,
                                 ОИ со временем) цветным знаком. Без статистики.
  data/mention_gap.md|.csv     — разрыв упоминаний (scripts/mention_gap.py по живой базе).
  data/oi5x5/news_oi_<год>.csv — коды ОИ 5×5 и метаданные новостей (без текста и без перевода текста).
  data/oi5x5/links_news.csv    — связи новость–новость (тот_же_факт, подтверждение, перепечатка, ссылка).
  data/oi5x5/README.md         — описание колонок и дата прохода ОИ (без статистики).
  manifest.json                — служебный: sha256 файлов и качество сопоставления (в репозиторий не идёт).

Источник кодов — компактная выгрузка ОИ (oi_compact.csv.gz, oi_links.csv.gz, oi_meta.json), подготовленная
на машине, где идёт проход ОИ 5×5. На сервере ОИ и перевод не считаются. Материалы живой базы, которых нет
в выгрузке, остаются без кода до следующего прохода ОИ — код не выдумывается.

Только стандартная библиотека Python 3.8+. Живая база открывается только на чтение; тексты новостей
целиком не загружаются (выборка по SQL, выгрузка ОИ читается потоком).
"""
from __future__ import annotations

import argparse, csv, gzip, hashlib, html, json, os, re, sqlite3, subprocess, sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

MINSK = timezone(timedelta(hours=3), "Europe/Minsk")  # без перехода на летнее время с 2011 г.

# Цвет — представление уже присвоенного кода ОИ 5×5; на расчёт кода не влияет.
# Основной цвет — по сведениям (1–5), оттенок — по источнику (А темнее/насыщеннее, Д светлее/глуше).
PALETTE = {
    "А1": ("#0B5D2A", "#fff"), "Б1": ("#1B7A3D", "#fff"), "В1": ("#2E9A4F", "#fff"), "Г1": ("#5BB86A", "#000"), "Д1": ("#A8D5B0", "#000"),
    "А2": ("#0D47A1", "#fff"), "Б2": ("#1565C0", "#fff"), "В2": ("#1E88E5", "#fff"), "Г2": ("#64B5F6", "#000"), "Д2": ("#BBDEFB", "#000"),
    "А3": ("#F9A825", "#000"), "Б3": ("#FBC02D", "#000"), "В3": ("#FDD835", "#000"), "Г3": ("#FFEE58", "#000"), "Д3": ("#FFF59D", "#000"),
    "А4": ("#EF6C00", "#fff"), "Б4": ("#FB8C00", "#000"), "В4": ("#FFA726", "#000"), "Г4": ("#FFCC80", "#000"), "Д4": ("#BDBDBD", "#000"),
    "А5": ("#B71C1C", "#fff"), "Б5": ("#C62828", "#fff"), "В5": ("#E53935", "#fff"), "Г5": ("#EF5350", "#000"), "Д5": ("#4A0000", "#fff"),
}
SOURCES = "АБВГД"
INFOS = "12345"

TOPIC_LABEL = {"drones": "Дроны", "countermeasures": "Противодействие", "navigation": "Навигация"}
CLAIM_LABEL = {"news": "✅ новость", "claim": "утверждение", "rumor": "слух"}
OI_COLS = ["id", "published_at", "event_date", "source", "url", "title", "title_ru", "language",
           "topic", "section", "category", "vehicle", "status_initial", "oi_initial",
           "status_evolved", "oi_evolved", "oi_evolved_at", "method_version", "as_of"]
PAGES = "https://skb-by.github.io/cbr-news-materials"


EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(?<![\w/])(?:\+\d{1,3}[\s(.-]*\d{2,4}[\s).-]*\d{2,4}[\s.-]*\d{2,4}(?:[\s.-]*\d{2,4})?"
                      r"|8[\s(-]*\d{3}[\s)-]*\d{3}[\s-]*\d{2}[\s-]*\d{2})(?![\w/])")


def redact(s: str) -> str:
    """Адреса e-mail и телефоны из заголовков в публичные файлы не попадают."""
    if not s:
        return s or ""
    return PHONE_RE.sub("[телефон скрыт]", EMAIL_RE.sub("[e-mail скрыт]", s))


def status_of(code: str) -> str:
    """Статус по коду ОИ 5×5 — как в расчёте t46u-oi5x5-2 (OI_5x5.md §5)."""
    if not code or len(code) != 2:
        return ""
    src, info = code[0], code[1]
    if info == "1":
        return "новость"
    if info == "2" and src in "АБВ":
        return "утверждение"
    return "слух"


def badge(code: str) -> str:
    if code not in PALETTE:
        return html.escape(code or "")
    bg, fg = PALETTE[code]
    return (f'<span style="background:{bg};color:{fg};padding:0 .35em;border-radius:3px;'
            f'font-weight:600;white-space:nowrap" title="ОИ 5×5: {code}">{code}</span>')


def md_text(s: str) -> str:
    s = html.escape((s or "").strip(), quote=False)
    return s.replace("[", "(").replace("]", ")").replace("|", "/").replace("\n", " ")


def short(s: str, n: int = 180) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 3] + "…"


def fmt_pub(s) -> str:
    if not s:
        return "—"
    day = str(s)[:10]
    if len(day) == 10 and day[4] == "-":
        y, m, d = day.split("-")
        return f"{d}.{m}.{y}"
    return str(s)


def fmt_minsk(iso: str) -> str:
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return dt.astimezone(MINSK).strftime("%d.%m.%Y %H:%M Europe/Minsk")
    except Exception:
        return iso


def has_table(conn, name):
    return conn.execute("select 1 from sqlite_master where type='table' and name=?", (name,)).fetchone() is not None


def has_col(conn, table, col):
    return any(r[1] == col for r in conn.execute(f"pragma table_info({table})"))


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


# ---------- выборка для отчёта (те же правила, что у «Актуального отчёта» бота) ----------

def list_items(conn, where, args, limit):
    sql = ("select id, dedupe_hash, published_at, source, title, url, claim_status from items "
           f"where ({where}) order by published_at desc, id desc limit ?")
    return [dict(r) for r in conn.execute(sql, (*args, limit))]


def select_report(conn):
    topics = []
    claim = has_col(conn, "items", "claim_status")
    for topic, label in TOPIC_LABEL.items():
        if claim:
            news = list_items(conn, "topic_domain=? and claim_status='news'", (topic,), 8)
            claims = list_items(conn, "topic_domain=? and claim_status='claim'", (topic,), 6)
        else:
            news, claims = list_items(conn, "topic_domain=?", (topic,), 8), []
        # утверждения — если новостей нет или тема навигации тонкая (как в боте)
        if not (claims and (not news or topic == "navigation")):
            claims = []
        topics.append((topic, label, news, claims))
    darpa = []
    if has_table(conn, "darpa_item_tags") and has_table(conn, "darpa_programs"):
        names = {r[0]: r[1] for r in conn.execute("select id, short from darpa_programs")}
        by = {}
        for r in conn.execute("select dedupe_hash, url, title, published_at, program_ids from darpa_item_tags "
                              "where program_ids is not null and program_ids != '[]' order by published_at desc"):
            try:
                pids = json.loads(r[4] or "[]")
            except Exception:
                pids = []
            for pid in pids:
                by.setdefault(pid, []).append({"dedupe_hash": r[0], "url": r[1], "title": r[2],
                                               "published_at": r[3], "claim_status": None, "source": None})
        for pid, items in sorted(by.items(), key=lambda kv: kv[0]):
            darpa.append((names.get(pid, pid), items[:6]))
    return topics, darpa


# ---------- выгрузка ОИ: потоковое чтение, таблицы по годам, сопоставление для отчёта ----------

def process_oi(oi_dir: Path, out: Path, want_hash: set, want_url: set):
    meta = json.loads((oi_dir / "oi_meta.json").read_text(encoding="utf-8"))
    ddir = out / "data" / "oi5x5"
    ddir.mkdir(parents=True, exist_ok=True)
    for old in ddir.glob("news_oi_*.csv"):
        old.unlink()
    writers, handles = {}, []
    by_hash, by_url = {}, {}
    with gzip.open(oi_dir / "oi_compact.csv.gz", "rt", encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        for r in rd:
            year = (r.get("published_at") or "")[:4]
            if not (len(year) == 4 and year.isdigit()):
                year = "без_даты"
            w = writers.get(year)
            if w is None:
                h = open(ddir / f"news_oi_{year}.csv", "w", encoding="utf-8", newline="")
                handles.append(h)
                w = csv.writer(h)
                w.writerow(OI_COLS)
                writers[year] = w
            r["title_ru"] = redact(clean_ru(r.get("title_ru", "")))
            r["title"] = redact(r.get("title", ""))
            w.writerow([r.get(k, "") for k in OI_COLS])
            if r["id"] in want_hash:
                by_hash[r["id"]] = r
            elif r.get("url") in want_url:
                by_url[r["url"]] = r
    for h in handles:
        h.close()
    links = oi_dir / "oi_links.csv.gz"
    if links.exists():
        with gzip.open(links, "rt", encoding="utf-8", newline="") as src, \
                open(ddir / "links_news.csv", "w", encoding="utf-8", newline="") as dst:
            for line in src:
                dst.write(line)
    return meta, sorted(writers), by_hash, by_url


def oi_readme(meta, years) -> str:
    as_of = fmt_minsk(meta.get("as_of", ""))
    files = "\n".join(f"- [news_oi_{y}.csv](news_oi_{y}.csv) — новости с датой публикации в {y} г." if y.isdigit()
                      else f"- [news_oi_{y}.csv](news_oi_{y}.csv) — новости без даты публикации" for y in years)
    return f"""# Данные ОИ 5×5

Коды ОИ 5×5 по новостям живой базы и архива. Проход ОИ: **{as_of}**, версия расчёта `{meta.get('method_version','')}`.
Пояснение кодов и цветов — [ОИ 5×5](../../OI_5x5.md), цветная матрица — [{PAGES}/oi-5x5/]({PAGES}/oi-5x5/).

В таблицах только метаданные и коды: текст новости, анонс и перевод текста не публикуются; живая база и архив (SQLite) в репозиторий не входят. Статистика по базе не публикуется.

Новые материалы живой базы, поступившие после прохода ОИ, остаются без кода до следующего прохода ОИ. Код для них не выдумывается.

## Файлы

{files}
- [links_news.csv](links_news.csv) — связи новость–новость: `тот_же_факт`, `подтверждение`, `перепечатка`, `ссылка` (совместные упоминания сущностей не публикуются).

## Колонки news_oi_*.csv

| Колонка | Что содержит |
|---|---|
| `id` | постоянный идентификатор новости (sha256 от URL, заголовка и даты публикации — `dedupe_hash` агрегатора) |
| `published_at` | дата публикации (UTC, как в источнике) |
| `event_date` | дата события, если названа в тексте; пусто, если не названа |
| `source` | источник (сайт или канал `tg:<имя>`), как в оригинале |
| `url` | ссылка на новость |
| `title` | заголовок в оригинале (у постов Telegram — начало поста, как в живой базе); адреса e-mail и телефоны заменены пометкой «скрыт» |
| `title_ru` | заголовок по-русски (машинный перевод без правки); пусто, если оригинал русский, текста нет или в переводе служебные артефакты модели |
| `language` | язык оригинала |
| `topic`, `section`, `category`, `vehicle` | тема, раздел, категория, носитель — по классификации агрегатора |
| `status_initial`, `oi_initial` | статус (новость / утверждение / слух) и код **Первоначальной ОИ** — на дату публикации |
| `status_evolved`, `oi_evolved`, `oi_evolved_at` | статус и код **ОИ со временем** и дата публикации первого подтверждения; пусто — пересмотра не было |
| `method_version` | версия расчёта ОИ 5×5 |
| `as_of` | дата и время прохода ОИ |

## Колонки links_news.csv

| Колонка | Что содержит |
|---|---|
| `id_a`, `id_b` | идентификаторы новостей (`id` из news_oi_*.csv) |
| `link_type` | тип связи |
| `published_at_b` | дата публикации второй новости |
"""


# ---------- отчёт ----------

MT_ARTIFACT = re.compile(r"formula_|_BAR_|_[A-Z]{3,}_")


def clean_ru(tr: str) -> str:
    """Машинный перевод заголовка; пусто, если в нём служебные артефакты модели."""
    tr = (tr or "").strip()
    return "" if MT_ARTIFACT.search(tr) else tr


def item_line(r, oi, as_of_oi: str) -> str:
    title = redact((r.get("title") or "без заголовка").strip())
    tr = redact(clean_ru((oi or {}).get("title_ru") or ""))
    url = r.get("url") or ""
    d = fmt_pub(r.get("published_at"))
    head = f"- {d} — " + (f"[{md_text(short(title))}]({url})" if url else md_text(short(title)))
    meta = []
    if r.get("source"):
        meta.append(md_text(r["source"]))
    lab = CLAIM_LABEL.get(r.get("claim_status") or "")
    if lab:
        meta.append(lab)
    if meta:
        head += f" ({', '.join(meta)})"
    if oi and oi.get("oi_initial"):
        head += f" · Первоначальная ОИ {badge(oi['oi_initial'])}"
        if oi.get("oi_evolved"):
            head += f" · ОИ со временем {badge(oi['oi_evolved'])}"
    else:
        head += f" · ОИ 5×5: кода ещё нет (материала нет в проходе ОИ {as_of_oi})"
    if tr:
        head += f"  \n  по-русски (машинный перевод, {md_text((oi or {}).get('language') or '')}→ru): «{md_text(short(tr, 180))}»"
    return head


def build_report(topics, darpa, lookup, as_of_label, as_of_oi) -> str:
    L = [f"**Актуальный отчёт** на {as_of_label}", "",
         "Только проанализированная, выверенная и структурированная информация по живой базе (классификация и правило слухов). "
         "В отчёт включены подтверждённые новости; утверждения — отдельно, если без них картина темы неполна. "
         "Слухи сюда не входят — они в отдельном разделе меню.", "",
         "У каждого материала — коды ОИ 5×5: **Первоначальная ОИ** (на дату публикации) и, если был пересмотр, "
         "**ОИ со временем**. Буква — надёжность источника (А–Д), цифра — достоверность сведений (1–5); "
         f"цвет и правила — в разделе [ОИ 5×5](OI_5x5.md) ([цветная матрица]({PAGES}/oi-5x5/)). "
         f"Коды — по проходу ОИ {as_of_oi}. Материалы, поступившие после этого прохода, кода ещё не имеют: "
         "код не выдумывается и появится после следующего прохода ОИ. "
         "Отметка «новость» / «утверждение» в скобках — правило слухов живой базы на дату отчёта.", "",
         "Этот файл — актуальный отчёт. Таблицы и материалы проектов лежат в этом репозитории; "
         "коды ОИ 5×5 по всем новостям — [data/oi5x5/](data/oi5x5/README.md).", ""]
    for topic, label, news, claims in topics:
        L += [f"**{label}**", ""]
        if news:
            L += ["Подтверждённые новости:", ""]
            L += [item_line(r, lookup(r), as_of_oi) for r in news]
        else:
            L.append("Подтверждённых новостей по этой теме в текущей выборке нет.")
        if claims:
            L += ["", "Утверждения (один источник, без независимого подтверждения в базе):", ""]
            L += [item_line(r, lookup(r), as_of_oi) for r in claims]
        L.append("")
    if darpa:
        L += ["**Программы DARPA**", "В ленте названы программы из рабочего реестра. Связь — по совпадению названия в тексте.", ""]
        for name, items in darpa:
            L += [f"**{md_text(name)}**", ""]
            L += [item_line(r, lookup(r), as_of_oi) for r in items]
            L.append("")
    return "\n".join(L).rstrip() + "\n"


def main():
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", default=os.environ.get("CBR_NEWS_DB", str(here / "news.sqlite")))
    ap.add_argument("--oi-dir", default=str(here / "oi"))
    ap.add_argument("--companies", required=True, help="companies.csv публичного репозитория")
    ap.add_argument("--mention-gap", default=str(here / "mention_gap.py"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--skip-mention-gap", action="store_true")
    a = ap.parse_args()

    out = Path(a.out)
    (out / "data").mkdir(parents=True, exist_ok=True)
    now = datetime.now(MINSK)
    as_of_label = now.strftime("%d.%m.%Y %H:%M Europe/Minsk")

    conn = sqlite3.connect(f"file:{a.db}?mode=ro", uri=True, timeout=60)
    conn.row_factory = sqlite3.Row
    topics, darpa = select_report(conn)
    all_rows = [r for _, _, n, c in topics for r in n + c] + [r for _, items in darpa for r in items]
    want_hash = {r["dedupe_hash"] for r in all_rows if r.get("dedupe_hash")}
    want_url = {r["url"] for r in all_rows if r.get("url")}
    conn.close()

    meta, years, by_hash, by_url = process_oi(Path(a.oi_dir), out, want_hash, want_url)
    as_of_oi = fmt_minsk(meta.get("as_of", ""))

    stat = {"hash": 0, "url": 0, "none": 0, "unmatched": []}

    def lookup(r):
        oi = by_hash.get(r.get("dedupe_hash") or "")
        if oi:
            stat["hash"] += 1
            return oi
        oi = by_url.get(r.get("url") or "")
        if oi:
            stat["url"] += 1
            return oi
        stat["none"] += 1
        stat["unmatched"].append({"published_at": r.get("published_at"), "url": r.get("url")})
        return None

    report = build_report(topics, darpa, lookup, as_of_label, as_of_oi)
    (out / "АКТУАЛЬНЫЙ_ОТЧЁТ.md").write_text(report, encoding="utf-8")
    (out / "data" / "oi5x5" / "README.md").write_text(oi_readme(meta, years), encoding="utf-8")

    mg = {"skipped": True}
    if not a.skip_mention_gap:
        cmd = [sys.executable, a.mention_gap, "--csv", a.companies, "--db", a.db, "--min-items", "2",
               "--out-csv", str(out / "data" / "mention_gap.csv"), "--out-md", str(out / "data" / "mention_gap.md"),
               "--as-of", as_of_label]
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
        mg = {"rc": p.returncode, "stdout": p.stdout.strip()[-500:], "stderr": p.stderr.strip()[-500:]}
        if p.returncode != 0:
            print(json.dumps({"ok": False, "step": "mention_gap", **mg}, ensure_ascii=False))
            sys.exit(2)

    files = {}
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name != "manifest.json":
            files[str(p.relative_to(out))] = {"bytes": p.stat().st_size, "sha256": sha256(p)}
    man = {"ok": True, "as_of": now.isoformat(timespec="seconds"), "as_of_label": as_of_label,
           "oi_as_of": meta.get("as_of"), "method_version": meta.get("method_version"),
           "report_items": len(all_rows), "join": {k: stat[k] for k in ("hash", "url", "none")},
           "unmatched": stat["unmatched"], "mention_gap": mg, "files": files}
    (out / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: man[k] for k in ("ok", "as_of_label", "oi_as_of", "report_items", "join")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
