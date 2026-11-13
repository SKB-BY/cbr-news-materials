#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""t86u: публичный каталог darpa-programs для GitHub Pages (все офисы DARPA, сферы, руководители, исполнители, новости).

  python3 darpa_site.py --out <dir> [--base <старый каталог darpa-programs>]
1) копирует из --base файлы, которые этот скрипт не создаёт (data/sam_subawards.*, revolving_door.md и т. п.);
2) darpa.repo(conn) — карточки, таблицы, LEAD_CHECK, UNASSIGNED (только чтение базы);
3) дополняет карточки и README сведениями darpa_ext.json (офис, сфера, руководитель, контракты USAspending, материалы darpa.mil).
Базу не пишет. Публикуются только имена и связи из опубликованных источников; телефонов и e-mail нет.
"""
import argparse, csv, json, re, shutil, sqlite3, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import darpa
import darpa_data as DD
from store import DB_PATH

OFF_RU = {"TTO": "Tactical Technology Office (TTO) — тактические технологии",
          "STO": "Strategic Technology Office (STO) — стратегические технологии",
          "BTO": "Biological Technologies Office (BTO) — биологические технологии",
          "DSO": "Defense Sciences Office (DSO) — оборонные науки",
          "IPTO": "Information Processing Techniques Office (IPTO) — обработка информации",
          "MXO": "Multi X Office (MXO; расширение Microsystems Technology Office, MTO)",
          "SBPO": "Small Business Programs Office (SBPO) — программы малого бизнеса",
          "DO": "Director's Office (DO) — офис директора",
          "": "Офис не указан на странице darpa.mil"}
ORDER = ["TTO", "STO", "IPTO", "MXO", "DSO", "BTO", "SBPO", "DO", ""]
SPHERES = ["вооружение", "бронетехника", "армейские джипы", "артиллерийские системы", "системы ПВО и РВСН", "авиация",
           "средства связи и коммуникаций", "программное обеспечение специального назначения", "тактика и стратегия", "БПЛА"]
ST = {"active": "действует", "completed": "завершена", "unknown": "статус не установлен"}


def cell(s):
    return str(s or "").replace("|", "/").replace("\n", " ")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); ap.add_argument("--base")
    a = ap.parse_args()
    out = Path(a.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    if a.base and Path(a.base).is_dir():
        for p in Path(a.base).rglob("*"):
            rel = p.relative_to(a.base)
            if p.is_file() and rel.parts[0] != "programs" and rel.name not in ("README.md",) and "__pycache__" not in rel.parts:
                (out / rel).parent.mkdir(parents=True, exist_ok=True); shutil.copy2(p, out / rel)
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True, timeout=30)
    darpa.repo(conn, out)
    ext = json.loads((HERE / "darpa_ext.json").read_text(encoding="utf-8"))
    E = {p["id"]: p for p in ext["programs"]}
    C = defaultdict(list)
    for c in ext["contracts"]:
        C[c["program_id"]].append(c)
    progs = conn.execute("select id, short, official_name, office, status, news_count from darpa_programs where kind != 'support'").fetchall()
    po = Counter(r[0] for r in conn.execute("select program_id from darpa_program_orgs"))
    tags = conn.execute("select program_ids from darpa_item_tags").fetchall()
    news = Counter(pid for (t,) in tags for pid in json.loads(t or "[]"))
    orgname = {r[0]: r[1] for r in conn.execute("select id, name from darpa_orgs")}
    # program cards
    for pid, short, name, office, status, _n in progs:
        f = out / "programs" / pid / "README.md"
        if not f.exists():
            continue
        e = E.get(pid, {})
        L = ["", "## Категория и сфера (t86u, проверка " + ext["as_of"] + ")", "",
             f"- Офис DARPA (категория): {OFF_RU.get(e.get('office_abbr', ''), office or 'не указан')}" if e else f"- Офис DARPA: {office or 'не указан'}",
             f"- Статус по darpa.mil: {'пометка «This program is now complete»' if e.get('status') == 'completed' else ('пометки о завершении нет' if e else ST.get(status, status))}",
             f"- Сфера (ось сайта, словарь sphere.py по названию и цитате назначения): {', '.join(e.get('spheres') or []) or 'не назначена (признаков нет)'}", ""]
        if e.get("pm"):
            L += ["## Руководитель программы (darpa.mil)", ""] + [f"- {x['name']} — [страница DARPA]({x['bio']})" for x in e["pm"]] + [""]
        cs = sorted(C.get(pid, []), key=lambda c: c.get("start") or "")
        if cs:
            L += [f"## Исполнители: контракты и гранты DARPA по USAspending.gov ({len(cs)})", "",
                  "Только записи, где описание контракта называет программу (правило совпадения — в последней колонке). Сумма — обязательства по записи USAspending, не цена программы.", "",
                  "| Дата начала | Получатель | Награда | Сумма, $ | Описание (USAspending) | Совпадение |", "|---|---|---|---|---|---|"]
            for c in cs:
                amt = f"{float(c['amount']):,.0f}".replace(",", " ") if c.get("amount") is not None else ""
                L.append(f"| {c.get('start','')} | {cell(orgname.get(c['org_id'], c['recipient']))} | [{c['award_id']}]({c['url']}) | {amt} | {cell(c['description'])[:220]} | {c['match']} |")
            L.append("")
        if e.get("related"):
            L += ["## Связанные материалы darpa.mil", ""] + [f"- [{cell(x['title'])}]({x['url']})" for x in e["related"]] + [""]
        f.write_text(f.read_text(encoding="utf-8").rstrip("\n") + "\n" + "\n".join(L), encoding="utf-8")
    # index
    by = defaultdict(list)
    for pid, short, name, office, status, _n in progs:
        e = E.get(pid, {})
        by[e.get("office_abbr", "") if e else ("" if not office else next((k for k, v in OFF_RU.items() if office and office.split(" (")[0] in v), ""))].append((pid, short, name, status, e))
    total = len(progs)
    sph = Counter(s for e in E.values() for s in (e.get("spheres") or []))
    R = ["# Программы DARPA — реестр по всем офисам", "",
         f"Проверка {ext['as_of']} (Europe/Minsk). В реестре {total} программ: все страницы программ из карты сайта darpa.mil "
         f"(https://www.darpa.mil/sitemap.xml, раздел /research/programs/) и программы, найденные в новостях агрегатора без страницы darpa.mil.", "",
         "Источники: страница программы на darpa.mil (название, офис, назначение — цитата, руководитель, пометка «This program is now complete»); "
         "исполнители — открытый API USAspending.gov (агентство-заказчик DARPA; в реестр попадают только записи, где описание контракта называет программу); "
         "новости — совпадение названия программы в хранилище агрегатора (live и архив). Пустое поле — в источнике нет. "
         "Непроверенные совпадения на публичные страницы не выносятся.", "",
         "Офис I2O на darpa.mil на дату проверки не значится; программы информационной тематики там указаны с офисом IPTO. "
         "MTO расширен в Multi X Office (MXO) — по странице https://www.darpa.mil/about/offices/mxo.", "",
         "## Сводка по офисам (категориям)", "", "| Офис | Программ | Действуют | Завершены | С исполнителями | С новостями |", "|---|---|---|---|---|---|"]
    for k in ORDER:
        rows = by.get(k, [])
        if not rows:
            continue
        R.append(f"| [{OFF_RU[k]}](#{('office-' + (k or 'none')).lower()}) | {len(rows)} | {sum(1 for r in rows if r[3]=='active')} | {sum(1 for r in rows if r[3]=='completed')} | {sum(1 for r in rows if po.get(r[0]))} | {sum(1 for r in rows if news.get(r[0]))} |")
    R += ["", "## Сферы (ось сайта)", "", "| Сфера | Программ |", "|---|---|"] + [f"| {s} | {sph.get(s, 0)} |" for s in SPHERES] + [
          "", "Сфера назначается словарём sphere.py (термин в названии или цитате назначения; иначе ≥2 разных термина в описании). У остальных программ признаков нет — сфера не назначается.", ""]
    for k in ORDER:
        rows = sorted(by.get(k, []), key=lambda r: r[1].lower())
        if not rows:
            continue
        R += [f'<a id="{("office-" + (k or "none")).lower()}"></a>', "", f"## {OFF_RU[k]} — {len(rows)}", "",
              "| Программа | Полное название | Статус | Сфера | Руководитель (darpa.mil) | Исполнителей | Новостей |", "|---|---|---|---|---|---|---|"]
        for pid, short, name, status, e in rows:
            R.append(f"| [{cell(short)}](programs/{pid}/README.md) | {cell(name)} | {ST.get(status, status)} | {cell(', '.join(e.get('spheres') or [])) if e else ''} | "
                     f"{cell(', '.join(x['name'] for x in (e.get('pm') or []))) if e else ''} | {po.get(pid, 0)} | {news.get(pid, 0)} |")
        R.append("")
    R += ["## Таблицы", "", "- `data/darpa_programs.csv`, `data/darpa_orgs.csv`, `data/darpa_program_orgs.csv`, `data/darpa_personnel.csv` — реестр;",
          "- `data/darpa_contracts_usaspending.csv` — контракты и гранты по программам (USAspending.gov);",
          "- `data/darpa_item_tags.json` — разметка новостей; `LEAD_CHECK.md` — проверка вводного списка; `UNASSIGNED.md` — материалы с DARPA без названной программы.", ""]
    old = (out / "README.md").read_text(encoding="utf-8")
    tail = old[old.find("## Листинг организаций"):] if "## Листинг организаций" in old else ""
    (out / "README.md").write_text("\n".join(R) + "\n" + tail, encoding="utf-8")
    with open(out / "data" / "darpa_contracts_usaspending.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["program_id", "org_id", "recipient", "award_id", "award_group", "start", "amount_usd", "description", "url", "match"])
        for c in ext["contracts"]:
            w.writerow([c["program_id"], c["org_id"], c["recipient"], c["award_id"], c["award_group"], c.get("start", ""), c.get("amount", ""), c["description"], c["url"], c["match"]])
    (out / "scripts").mkdir(exist_ok=True)
    for fn in ("darpa.py", "darpa_data.py", "darpa_t86u.py", "darpa_site.py"):
        if (HERE / fn).exists():
            shutil.copy2(HERE / fn, out / "scripts" / fn)
    shutil.copy2(HERE / "darpa_ext.json", out / "data" / "darpa_ext.json")
    # t86u: связи «новость → программа DARPA» для Новостной карты (ключ — первые 16 символов dedupe_hash)
    pn = {r[0]: (r[1] or r[0]) for r in conn.execute("select id, short from darpa_programs")}
    tags = {}
    for h, pids in conn.execute("select dedupe_hash, program_ids from darpa_item_tags where program_ids not in ('', '[]')"):
        lst = [[x, pn[x]] for x in json.loads(pids or "[]") if x in pn]
        if lst and h:
            tags[h[:16]] = lst
    (out / "data" / "news_tags.js").write_text("window.DARPA_NEWS_TAGS=" + json.dumps(tags, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print(json.dumps({"programs": total, "offices": {k or "—": len(v) for k, v in by.items()}, "contracts": len(ext["contracts"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
