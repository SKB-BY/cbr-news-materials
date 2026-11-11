#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""«Вращающаяся дверь»: персоналии реестра DARPA × официальные документы SEC EDGAR — рабочий список.

LinkedIn и другие соцсети НЕ используются. Источник — полнотекстовый поиск SEC EDGAR
(https://efts.sec.gov/LATEST/search-index, официальный API SEC) по точному имени из
data/darpa_personnel.csv в формах 3/4/5 (инсайдеры), 8-K (назначения), DEF 14A (директора и
руководители), 10-K. Совпадение засчитывается, только если документ подан компанией из
data/darpa_orgs.csv (CIK по https://www.sec.gov/files/company_tickers_exchange.json и CIK из
invest_source). Совпадение имени — НЕ доказательство: это кандидат для ручной проверки
(тёзки, упоминание человека в чужом контексте). В darpa_personnel.red_flag ничего не пишется
автоматически.

Частные компании (Anduril, Shield AI и др.) в SEC не отчитываются — по ним проверка этим
скриптом невозможна; это отмечается в отчёте.

  SEC_EDGAR_USER_AGENT="Org name contact" python3 scripts/revolving_door.py
  python3 scripts/revolving_door.py --dry-run
"""
from __future__ import annotations

import argparse, csv, json, os, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EFTS = "https://efts.sec.gov/LATEST/search-index"
TICKERS = "https://www.sec.gov/files/company_tickers_exchange.json"
FORMS = "3,4,5,8-K,DEF 14A,10-K"


def get(url, ua):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def org_ciks(orgs, ua):
    """org_id -> CIK (int) for orgs with a US SEC listing / submissions URL."""
    out = {}
    for o in orgs:
        m = re.search(r"CIK0*(\d+)", o.get("invest_source", ""))
        if m:
            out[o["id"]] = int(m.group(1))
    data = get(TICKERS, ua)
    by_ticker = {row[2]: row[0] for row in data["data"]}
    for o in orgs:
        t = (o.get("ticker") or "").split()[0] if o.get("ticker") else ""
        if t and t in by_ticker and o["id"] not in out:
            out[o["id"]] = by_ticker[t]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=str(ROOT / "data"))
    ap.add_argument("--out-md", default=str(ROOT / "data" / "revolving_door.md"))
    ap.add_argument("--sleep", type=float, default=0.3, help="pause between SEC requests (SEC limit: 10/s)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    d = Path(a.data)
    orgs = list(csv.DictReader(open(d / "darpa_orgs.csv", encoding="utf-8")))
    pers = list(csv.DictReader(open(d / "darpa_personnel.csv", encoding="utf-8")))
    po = list(csv.DictReader(open(d / "darpa_program_orgs.csv", encoding="utf-8")))
    names = {o["id"]: o["name"] for o in orgs}
    people = {}
    for p in pers:
        people.setdefault(p["name"], []).append(p)
    ua = os.environ.get("SEC_EDGAR_USER_AGENT", "")
    if a.dry_run or not ua:
        print("dry-run: SEC_EDGAR_USER_AGENT не задан или указан --dry-run; запросы не выполняются", file=sys.stderr)
        for n in people:
            print(f"{EFTS}?{urllib.parse.urlencode({'q': json.dumps(n), 'forms': FORMS})}")
        return
    ciks = org_ciks(orgs, ua)
    cik2org = {v: k for k, v in ciks.items()}
    rows, errors, totals = [], [], {}
    for name, recs in people.items():
        url = f"{EFTS}?{urllib.parse.urlencode({'q': json.dumps(name), 'forms': FORMS})}"
        try:
            res = get(url, ua)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{name}: {e}"); continue
        hits = res.get("hits", {}).get("hits", [])
        totals[name] = res.get("hits", {}).get("total", {}).get("value", 0)
        progs = {r["program_id"] for r in recs if r["program_id"]}
        same_prog_orgs = {x["org_id"] for x in po if x["program_id"] in progs}
        for h in hits:
            s = h["_source"]
            for c in s.get("ciks", []):
                oid = cik2org.get(int(c))
                if not oid:
                    continue
                adsh, fname = h["_id"].split(":", 1)
                doc = f"https://www.sec.gov/Archives/edgar/data/{int(c)}/{adsh.replace('-', '')}/{fname}"
                rows.append({"name": name, "darpa_roles": "; ".join(f"{r['role']} ({r['program_id'] or '—'})" for r in recs),
                             "org_id": oid, "org": names.get(oid, oid), "form": s.get("form"), "date": s.get("file_date"),
                             "same_program": oid in same_prog_orgs, "url": doc})
        time.sleep(a.sleep)
    private = [o["name"] for o in orgs if o["id"] not in ciks and o["listing_status"] in ("private", "acquired", "unknown")]
    with open(a.out_md, "w", encoding="utf-8") as fh:
        fh.write("# «Вращающаяся дверь» — рабочий список возможных связей (SEC EDGAR)\n\n")
        fh.write("**Рабочий список, не факты реестра.** Каждая строка — документ SEC компании из `darpa_orgs.csv`, в тексте которого "
                 "встречается точное имя человека из `darpa_personnel.csv`. Это может быть тёзка или упоминание в ином контексте; "
                 "связь считается установленной только после чтения документа человеком. LinkedIn не используется. "
                 "В `darpa_personnel.red_flag` ничего не переносится автоматически.\n\n")
        fh.write(f"Источник: полнотекстовый поиск SEC EDGAR, формы {FORMS}. Проверено имён: {len(people)}; "
                 f"компаний с CIK: {len(ciks)}; ошибок запросов: {len(errors)}.\n\n")
        same = [r for r in rows if r["same_program"]]
        fh.write("## Совпадения в документах компании — исполнителя той же программы\n\n")
        if same:
            fh.write("| Имя | Роль в реестре | Компания | Форма | Дата | Документ |\n|---|---|---|---|---|---|\n")
            for r in sorted(same, key=lambda r: (r["name"], r["date"] or "")):
                fh.write(f"| {r['name']} | {r['darpa_roles']} | {r['org']} | {r['form']} | {r['date']} | [SEC]({r['url']}) |\n")
        else:
            fh.write("Нет.\n")
        other = [r for r in rows if not r["same_program"]]
        fh.write("\n## Совпадения в документах других компаний реестра\n\n")
        if other:
            fh.write("| Имя | Роль в реестре | Компания | Форма | Дата | Документ |\n|---|---|---|---|---|---|\n")
            for r in sorted(other, key=lambda r: (r["name"], r["date"] or "")):
                fh.write(f"| {r['name']} | {r['darpa_roles']} | {r['org']} | {r['form']} | {r['date']} | [SEC]({r['url']}) |\n")
        else:
            fh.write("Нет.\n")
        fh.write("\n## Не проверяется этим скриптом\n\n")
        fh.write("Компании без отчётности в SEC (частные, поглощённые, иностранные без CIK) — по ним сведения о должностях "
                 "в SEC отсутствуют; проверка возможна только по официальным страницам самих компаний (руководство, совет директоров):\n\n")
        fh.write(", ".join(sorted(private)) + "\n")
        if errors:
            fh.write("\n## Ошибки запросов\n\n" + "\n".join(f"- {e}" for e in errors) + "\n")
    print(json.dumps({"people": len(people), "ciks": len(ciks), "rows": len(rows), "same_program": len(same), "errors": len(errors)}))


if __name__ == "__main__":
    main()
