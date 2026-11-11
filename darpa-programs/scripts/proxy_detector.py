#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Детектор «дочек вне реестра» (potential shells) — рабочий список, не обвинение.

1. Читает data/darpa_orgs.csv.
2. Для компаний с листингом (listing_status=listed и CIK в SEC) берёт из SEC EDGAR последний
   годовой отчёт 10-K (для иностранных эмитентов — 20-F / 40-F) и его приложение Exhibit 21
   «Subsidiaries of the Registrant» (официальный перечень дочерних структур).
   API: https://data.sec.gov/submissions/CIK##########.json, индекс подачи
   https://www.sec.gov/Archives/edgar/data/<cik>/<accession>/<accession>-index.htm
3. Сравнивает дочерние структуры с названиями в разметке новостей data/darpa_item_tags.json
   (заголовки; при --db — также текст материалов из news.sqlite) и с darpa_orgs.csv.
4. Пишет data/potential_shells.md и .csv: дочерняя структура известного игрока, названная в
   материале с контекстом DARPA, но отсутствующая в основном реестре. Плюс полный перечень
   найденных Exhibit 21 по компаниям (data/sec_subsidiaries.csv).
В darpa_orgs.csv ничего не вносится автоматически.

SEC требует описательный User-Agent с контактом: переменная SEC_EDGAR_USER_AGENT.
Без неё скрипт не делает сетевых запросов (режим --dry-run). Пауза между запросами — 0,3 с
(лимит SEC — 10 запросов в секунду).

  SEC_EDGAR_USER_AGENT="Org contact" python3 scripts/proxy_detector.py [--db news.sqlite]
  python3 scripts/proxy_detector.py --dry-run
"""
from __future__ import annotations

import argparse, csv, html, json, os, re, sqlite3, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TICKERS = "https://www.sec.gov/files/company_tickers_exchange.json"
ANNUAL = ("10-K", "20-F", "40-F")
SUFFIX = re.compile(r"\b(inc|incorporated|corp|corporation|co|company|llc|l\.l\.c|ltd|limited|plc|lp|l\.p|gmbh|ag|sa|s\.a|bv|b\.v|"
                    r"pty|pte|sarl|s\.r\.l|srl|spa|s\.p\.a|kk|k\.k|ulc|holdings?|the)\b\.?", re.I)
GENERIC = {"international", "services", "systems", "technologies", "technology", "holdings", "group", "solutions",
           "global", "america", "americas", "usa", "us", "uk", "europe", "defense", "defence", "operations", "company"}


def norm(s):
    s = SUFFIX.sub(" ", html.unescape(s or "").lower())
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


class Sec:
    def __init__(self, ua, pause):
        self.ua, self.pause = ua, pause

    def get(self, url, as_json=False):
        time.sleep(self.pause)
        req = urllib.request.Request(url, headers={"User-Agent": self.ua, "Accept-Encoding": "identity"})
        with urllib.request.urlopen(req, timeout=60) as r:
            b = r.read()
        return json.loads(b) if as_json else b.decode("utf-8", "replace")


def latest_annual(sec, cik):
    sub = sec.get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", True)
    rec = sub["filings"]["recent"]
    for form, acc, date in zip(rec["form"], rec["accessionNumber"], rec["filingDate"]):
        if form in ANNUAL:
            return form, acc, date, sub.get("name")
    return None, None, None, sub.get("name")


def ex21(sec, cik, acc):
    idx_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{acc}-index.htm"
    page = sec.get(idx_url)
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", page, re.S | re.I):
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S | re.I)
        if len(cells) >= 4 and re.match(r"\s*EX-21", re.sub(r"<[^>]+>", "", cells[3]), re.I):
            m = re.search(r'href="([^"]+)"', cells[2], re.I)
            if m:
                href = m.group(1).replace("/ix?doc=", "")
                return idx_url, "https://www.sec.gov" + href if href.startswith("/") else href
    return idx_url, None


def subsidiaries(doc):
    """Subsidiary names from an Exhibit 21 document: first cell of table rows, else non-empty lines."""
    names = []
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", doc, re.S | re.I)
    for row in rows:
        cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c))).strip()
                 for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S | re.I)]
        cells = [c for c in cells if c]
        if cells:
            names.append(cells[0])
    if len(names) < 3:
        text = html.unescape(re.sub(r"<[^>]+>", "\n", doc))
        names = [re.sub(r"\s+", " ", l).strip() for l in text.splitlines()]
    out = []
    for n in names:
        n = re.sub(r"\s*[\(\[].*?[\)\]]\s*$", "", n).strip(" .,*")
        if 3 <= len(n) <= 120 and re.search(r"[A-Za-z]", n) and not re.search(
                r"subsidiar|jurisdiction|name of|state or|organized|percent|exhibit|registrant|^\d+$", n, re.I):
            out.append(n)
    return list(dict.fromkeys(out))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=str(ROOT / "data"))
    ap.add_argument("--db", default="", help="optional news.sqlite: also scan item text for tagged URLs")
    ap.add_argument("--pause", type=float, default=0.3)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    d = Path(a.data)
    orgs = list(csv.DictReader(open(d / "darpa_orgs.csv", encoding="utf-8")))
    listed = [o for o in orgs if o["listing_status"] == "listed"]
    ua = os.environ.get("SEC_EDGAR_USER_AGENT", "")
    if a.dry_run or not ua:
        print("dry-run: SEC_EDGAR_USER_AGENT не задан или указан --dry-run; запросы к SEC не выполняются", file=sys.stderr)
        for o in listed:
            print(o["id"], o["ticker"], "->", "https://data.sec.gov/submissions/CIK<cik>.json -> 10-K -> EX-21")
        return
    sec = Sec(ua, a.pause)
    by_ticker = {row[2]: row[0] for row in sec.get(TICKERS, True)["data"]}
    tags = json.load(open(d / "darpa_item_tags.json", encoding="utf-8"))
    texts = {t["url"]: f"{t.get('title') or ''}" for t in tags}
    if a.db:
        conn = sqlite3.connect(f"file:{a.db}?mode=ro", uri=True)
        for url, title, body in conn.execute("select url, title, body from items"):
            if url in texts:
                texts[url] = f"{title or ''} {(body or '')[:6000]}"
    ntexts = {u: f" {norm(t)} " for u, t in texts.items()}
    known = {norm(re.sub(r"\(.*?\)", "", o["name"])) for o in orgs} | {norm(o["name"]) for o in orgs}
    known.discard("")
    allsubs, shells, report = [], [], []
    for o in listed:
        m = re.search(r"CIK0*(\d+)", o.get("invest_source", ""))
        tk = (o.get("ticker") or "").split()[0]
        cik = int(m.group(1)) if m else by_ticker.get(tk)
        if not cik:
            report.append((o["name"], "", "", "", "CIK не найден в SEC (листинг вне США / ADR без отчётности)")); continue
        try:
            form, acc, date, sec_name = latest_annual(sec, cik)
            if not acc:
                report.append((o["name"], cik, "", "", "годового отчёта 10-K/20-F/40-F в последних подачах нет")); continue
            idx_url, ex_url = ex21(sec, cik, acc)
            if not ex_url:
                report.append((o["name"], cik, f"{form} {date}", idx_url, "Exhibit 21 в подаче не найден")); continue
            subs = subsidiaries(sec.get(ex_url))
        except Exception as e:  # noqa: BLE001
            report.append((o["name"], cik, "", "", f"ошибка: {e}")); continue
        report.append((o["name"], cik, f"{form} {date}", ex_url, f"дочерних структур: {len(subs)}"))
        for s in subs:
            n = norm(s)
            allsubs.append({"org_id": o["id"], "parent": o["name"], "subsidiary": s, "form": form, "filing_date": date, "exhibit_url": ex_url})
            words = [w for w in n.split() if w not in GENERIC]
            if len(n) < 6 or not words or n in known:
                continue
            hits = [u for u, t in ntexts.items() if f" {n} " in t]
            if hits:
                shells.append({"subsidiary": s, "parent": o["name"], "parent_id": o["id"], "form": form, "filing_date": date,
                               "exhibit_url": ex_url, "items": len(hits), "example_urls": " ".join(hits[:3])})
    with open(d / "sec_subsidiaries.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["org_id", "parent", "subsidiary", "form", "filing_date", "exhibit_url"]); w.writeheader(); w.writerows(allsubs)
    with open(d / "potential_shells.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["subsidiary", "parent", "parent_id", "form", "filing_date", "exhibit_url", "items", "example_urls"])
        w.writeheader(); w.writerows(shells)
    with open(d / "potential_shells.md", "w", encoding="utf-8") as fh:
        fh.write("# Дочерние структуры вне реестра (potential shells) — рабочий список\n\n")
        fh.write("**Рабочий список, не обвинение и не факты реестра.** Строка = юридическая дочерняя структура компании из "
                 "`darpa_orgs.csv` (по Exhibit 21 последнего годового отчёта в SEC EDGAR), которая названа в материале с контекстом "
                 "DARPA (`darpa_item_tags.json`), но отсутствует в `darpa_orgs.csv`. В реестр ничего не вносится автоматически.\n\n")
        fh.write(f"Компаний с листингом: {len(listed)}; дочерних структур в Exhibit 21: {len(allsubs)} (`sec_subsidiaries.csv`); "
                 f"материалов в разметке: {len(texts)}{' (с текстом из news.sqlite)' if a.db else ' (только заголовки)'}.\n\n")
        fh.write("## Кандидаты\n\n")
        if shells:
            fh.write("| Дочерняя структура | Материнская компания | Отчёт | Exhibit 21 | Материалов | Примеры |\n|---|---|---|---|---:|---|\n")
            for s in shells:
                ex = " ".join(f"[ссылка]({u})" for u in s["example_urls"].split())
                fh.write(f"| {s['subsidiary']} | {s['parent']} | {s['form']} {s['filing_date']} | [SEC]({s['exhibit_url']}) | {s['items']} | {ex} |\n")
        else:
            fh.write("Совпадений нет: ни одна дочерняя структура из Exhibit 21 не названа в размеченных материалах с контекстом DARPA.\n")
        fh.write("\n## Проверенные отчёты\n\n| Компания | CIK | Отчёт | Источник | Результат |\n|---|---|---|---|---|\n")
        for r in report:
            fh.write(f"| {r[0]} | {r[1]} | {r[2]} | {('[SEC](' + r[3] + ')') if r[3] else '—'} | {r[4]} |\n")
    print(json.dumps({"listed": len(listed), "subsidiaries": len(allsubs), "shell_candidates": len(shells),
                      "texts": len(texts)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
