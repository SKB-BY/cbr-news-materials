#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Субподряды по исполнителям DARPA-реестра — рабочий список, не перепись.

Источник: открытый API USAspending.gov (Минфин США; данные FFATA о субподрядах, которые
головные исполнители отчитывают в SAM.gov / FSRS). Ключ API не нужен.
  POST https://api.usaspending.gov/api/v2/search/spending_by_award/   (subawards=true)

Для каждой организации из data/darpa_orgs.csv: (1) крупнейшие головные контракты и гранты, где
**заказчик — DARPA** (awarding subtier «Defense Advanced Research Projects Agency») и получатель
совпадает с названием организации; (2) субподряды, отчитанные по этим award id. Результат:
  data/sam_subawards.csv  — строки субподрядов (с URL карточки головного контракта на usaspending.gov)
  data/sam_subawards.md   — субподрядчики, которых НЕТ в darpa_orgs.csv (рабочий список для проверки)
В darpa_orgs.csv ничего не вносится автоматически. Место (город/штат) — адрес исполнения по
отчёту, а не штат регистрации юрлица; «прокладкой» строку делает только проверка человеком.

Ограничения: OTA (Other Transaction) DARPA попадают в USAspending не всегда, а субподряды
по OTA, как правило, не отчитываются по FFATA — их отсутствие в списке не означает отсутствия.

  python3 scripts/sam_subawards.py                    # все организации, до 3 страниц по 100 строк
  python3 scripts/sam_subawards.py --ids lockheed,dynetics --pages 1
  python3 scripts/sam_subawards.py --dry-run          # показать запросы, без сети
Переменные окружения: USASPENDING_API (по умолчанию https://api.usaspending.gov), HTTP_USER_AGENT.
"""
from __future__ import annotations

import argparse, csv, json, os, re, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = os.environ.get("USASPENDING_API", "https://api.usaspending.gov") + "/api/v2/search/spending_by_award/"
UA = os.environ.get("HTTP_USER_AGENT", "CBRNewsAggregator/1.0 (+https://gitlab.com/cbr-uav-group/n8n-news-aggregator; darpa-programs research)")
DARPA = "Defense Advanced Research Projects Agency"
FIELDS = ["Sub-Award ID", "Sub-Awardee Name", "Sub-Award Amount", "Sub-Award Date", "Prime Recipient Name",
          "Prime Award ID", "Sub-Award Description", "Sub-Recipient Location"]
# search text per org (USAspending matches prime OR sub name); default = name without the parenthesis
SEARCH = {"rtx": "Raytheon", "bbn": "BBN", "spacex": "Space Exploration Technologies", "qinetiq-na": "Foster-Miller",
          "spa": "Systems Planning and Analysis", "google-quantum": "Google", "bae": "BAE Systems",
          "palladyne": "Sarcos", "soartech": "Soar Technology", "boston-dynamics": "Boston Dynamics",
          "draper": "Charles Stark Draper", "siri": "Siri"}
SUFFIX = re.compile(r"\b(inc|incorporated|corp|corporation|co|company|llc|l\.l\.c|ltd|plc|lp|the|holdings?|group|technologies|technology|systems)\b\.?", re.I)


def norm(s: str) -> str:
    s = SUFFIX.sub(" ", (s or "").lower())
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def post(body: dict) -> dict:
    req = urllib.request.Request(API, data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)


GROUPS = {"contracts": ["A", "B", "C", "D"], "grants": ["02", "03", "04", "05"]}
PERIOD = [{"start_date": "2007-10-01", "end_date": "2026-09-30"}]
AG = [{"type": "awarding", "tier": "subtier", "name": DARPA}]


def primes_body(text: str, group: str, limit: int) -> dict:
    """Step 1: DARPA prime awards whose recipient matches the org (recipient_search_text = prime name here)."""
    return {"filters": {"agencies": AG, "award_type_codes": GROUPS[group], "recipient_search_text": [text], "time_period": PERIOD},
            "fields": ["Award ID", "Recipient Name", "Award Amount"], "limit": limit, "page": 1,
            "sort": "Award Amount", "order": "desc"}


def body_for(award_ids: list, group: str, page: int) -> dict:
    """Step 2: subawards reported under those prime award ids (with subawards=true, recipient_search_text
    would match the SUB-awardee, so the prime is selected by award id instead)."""
    return {"filters": {"agencies": AG, "award_type_codes": GROUPS[group], "award_ids": award_ids, "time_period": PERIOD},
            "fields": FIELDS, "subawards": True, "limit": 100, "page": page,
            "sort": "Sub-Award Amount", "order": "desc"}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--orgs", default=str(ROOT / "data" / "darpa_orgs.csv"))
    ap.add_argument("--out-csv", default=str(ROOT / "data" / "sam_subawards.csv"))
    ap.add_argument("--out-md", default=str(ROOT / "data" / "sam_subawards.md"))
    ap.add_argument("--ids", default="")
    ap.add_argument("--pages", type=int, default=3, help="subaward pages (100 rows) per org and award group")
    ap.add_argument("--primes", type=int, default=25, help="largest DARPA prime awards per org and group")
    ap.add_argument("--sleep", type=float, default=1.0)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    orgs = list(csv.DictReader(open(a.orgs, encoding="utf-8")))
    if a.ids:
        orgs = [o for o in orgs if o["id"] in a.ids.split(",")]
    known = {norm(o["name"]) for o in orgs} | {norm(re.sub(r"\(.*?\)", "", o["name"])) for o in orgs}
    known |= {norm(SEARCH[o["id"]]) for o in orgs if o["id"] in SEARCH}
    known.discard("")
    rows, errors = [], []
    for o in orgs:
        text = SEARCH.get(o["id"], re.sub(r"\s*\(.*?\)", "", o["name"]).strip())
        key = norm(text)
        if a.dry_run:
            print(o["id"], json.dumps(primes_body(text, "contracts", a.primes), ensure_ascii=False)); continue
        for group in GROUPS:
            try:
                pr = post(primes_body(text, group, a.primes)).get("results") or []
            except Exception as e:  # noqa: BLE001
                errors.append(f"{o['id']}/{group} primes: {e}"); continue
            ids = sorted({r["Award ID"] for r in pr if r.get("Award ID") and key in norm(r.get("Recipient Name"))})
            time.sleep(a.sleep)
            if not ids:
                continue
            for page in range(1, a.pages + 1):
                try:
                    res = post(body_for(ids, group, page))
                except Exception as e:  # noqa: BLE001
                    errors.append(f"{o['id']}/{group} subawards: {e}"); break
                for r in res.get("results") or []:
                    if key not in norm(r.get("Prime Recipient Name")):
                        continue
                    loc = r.get("Sub-Recipient Location") or {}
                    gid = r.get("prime_award_generated_internal_id") or ""
                    rows.append({"org_id": o["id"], "prime_recipient": r.get("Prime Recipient Name"), "prime_award_id": r.get("Prime Award ID"),
                                 "sub_awardee": r.get("Sub-Awardee Name"), "sub_amount": r.get("Sub-Award Amount"),
                                 "sub_date": r.get("Sub-Award Date"), "sub_city": loc.get("city_name") or "",
                                 "sub_state": loc.get("state_code") or "", "sub_country": loc.get("country_name") or "",
                                 "description": (r.get("Sub-Award Description") or "")[:200],
                                 "source_url": f"https://www.usaspending.gov/award/{gid}" if gid else ""})
                time.sleep(a.sleep)
                if not (res.get("page_metadata") or {}).get("hasNext"):
                    break
        time.sleep(a.sleep)
    if a.dry_run:
        return
    Path(a.out_csv).parent.mkdir(parents=True, exist_ok=True)
    cols = ["org_id", "prime_recipient", "prime_award_id", "sub_awardee", "sub_amount", "sub_date", "sub_city", "sub_state",
            "sub_country", "description", "source_url"]
    with open(a.out_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows)
    new = {}
    for r in rows:
        n = norm(r["sub_awardee"])
        if not n or n in known or any(k and (k == n or f" {k} " in f" {n} ") for k in known):
            continue
        d = new.setdefault(r["sub_awardee"], {"n": 0, "amt": 0.0, "primes": set(), "places": set(), "url": r["source_url"]})
        d["n"] += 1; d["amt"] += float(r["sub_amount"] or 0); d["primes"].add(r["prime_recipient"])
        d["places"].add(", ".join(x for x in (r["sub_city"].title(), r["sub_state"], r["sub_country"].title()) if x))
    with open(a.out_md, "w", encoding="utf-8") as fh:
        fh.write("# Субподрядчики исполнителей DARPA, которых нет в darpa_orgs.csv — рабочий список\n\n")
        fh.write("**Рабочий список, не перепись и не факты реестра.** Источник — открытый API USAspending.gov (отчёты FFATA "
                 "головных исполнителей о субподрядах по контрактам и грантам, где заказчик — DARPA). Место — место исполнения "
                 "по отчёту, не штат регистрации юрлица. Субподряды по OTA, как правило, не отчитываются, поэтому отсутствие "
                 "в списке ничего не доказывает. В `darpa_orgs.csv` ничего не вносится автоматически.\n\n")
        fh.write("«Сумма записей» — сумма всех отчётов по субподрядчику (отчёты о модификациях одного субподряда суммируются), а не стоимость контракта.\n\n")
        fh.write(f"Строк субподрядов: {len(rows)}; субподрядчиков вне реестра: {len(new)}. "
                 f"Ошибок запросов: {len(errors)}.\n\n")
        fh.write("| Субподрядчик | Записей | Сумма записей, $ | Головной исполнитель | Место (по отчёту) | Пример карточки |\n|---|---:|---:|---|---|---|\n")
        for name, d in sorted(new.items(), key=lambda kv: -kv[1]["amt"]):
            fh.write(f"| {name} | {d['n']} | {d['amt']:,.0f} | {'; '.join(sorted(d['primes']))} | {'; '.join(sorted(d['places']))[:120]} | [usaspending]({d['url']}) |\n")
        if errors:
            fh.write("\n## Ошибки запросов\n\n" + "\n".join(f"- {e}" for e in errors) + "\n")
    print(json.dumps({"orgs": len(orgs), "subaward_rows": len(rows), "new_subawardees": len(new), "errors": len(errors)}))


if __name__ == "__main__":
    main()
