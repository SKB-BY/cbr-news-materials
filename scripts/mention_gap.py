#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mention gap: «Упомянуто в новостях, но отсутствует в реестре».

Pure Python (stdlib only). Builds a WORKING gap list, not a verified census:
candidates are extracted with regular expressions (organisation suffixes,
quoted Russian names after «компания / концерн / АО / ООО …»), then compared
with the register (names, aliases in parentheses, short names before «—», and —
when companies_data.py is importable — the same tight MENTION_RE patterns the
aggregator uses). Nothing is inserted into the register automatically; every
candidate must be checked by a person (official site, source) before it is added.

Inputs
  --csv companies.csv           register (required); mention_examples titles are scanned
  --db news.sqlite              optional: also scan titles + leads (first 3000 chars) of items
Outputs
  --out-csv mention_gap.csv     candidate, hits, items, example_urls, example_titles
  --out-md  mention_gap.md      the same as a Markdown table

Usage
  python3 scripts/mention_gap.py --csv companies.csv --out-csv data/mention_gap.csv --out-md data/mention_gap.md
  python3 scripts/mention_gap.py --csv companies.csv --db /path/news.sqlite --min-items 2 ...
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

ORG_SUFFIX = (
    r"Inc|Corp|Corporation|Co|Ltd|LLC|GmbH|AG|SA|S\.A\.|SAS|SpA|S\.p\.A\.|BV|AB|ASA|Oy|plc|PLC|"
    r"Systems|Technologies|Technology|Defense|Defence|Aerospace|Aeronautics|Aviation|Robotics|"
    r"Dynamics|Industries|Industry|Group|Labs|Laboratories|Electronics|Engineering|Solutions|Drones|"
    r"Unmanned|Autonomy|Holdings|Holding|Tech|AI"
)
CAP = r"[A-Z][A-Za-z0-9&'’\-\.]*"
EN_ORG = re.compile(rf"\b((?:{CAP}\s+){{0,3}}{CAP}\s+(?:{ORG_SUFFIX}))\b")
RU_ORG = re.compile(
    r"(?:компани[яиюей]|концерн[аеу]?|фирм[аыуе]|производител[ья]|предприяти[ея]|завод[аеу]?|"
    r"корпораци[яиюей]|холдинг[аеу]?|стартап[аеу]?|КБ|НПО|АО|ООО|ПАО|ГК)\s+"
    r"[«\"“]([^»\"”]{2,60})[»\"”]"
)
EN_COMPANY = re.compile(r"\b(?:company|firm|startup|manufacturer|maker|contractor)\s+([A-Z][A-Za-z0-9\-]+(?:\s+[A-Z][A-Za-z0-9\-]+){0,2})")

# Generic phrases that match the patterns but are not organisations of interest.
STOP = {
    "unmanned", "defense", "defence", "systems", "technology", "technologies", "group", "aviation",
    "the", "a", "an", "us", "uk", "eu", "nato", "new", "air", "army", "navy", "space",
    "ministry of defence", "ministry of defense", "department of defense", "armed forces",
    "air force", "space force", "joint", "national", "global", "european", "american", "russian",
    "chinese", "ukrainian", "israeli", "turkish", "british", "french", "german",
}
# Candidates made only of these generic words are dropped (e.g. «Federal Aviation», «Physical AI»).
GENERIC = STOP | {
    "federal", "civil", "drone", "drones", "counter", "counter-uas", "counter-unmanned", "aircraft", "autonomous",
    "embedded", "physical", "industry", "industries", "airspace", "navigation", "satellite", "engineering",
    "solutions", "robotics", "dynamics", "aerospace", "ai", "uas", "uav", "c-uas", "systems", "system",
    "unmanned", "combat", "proven", "combat-proven", "danish", "advanced", "military", "commercial", "tech",
    "labs", "electronics", "holdings", "holding", "small", "large", "future", "smart", "integrated", "mission",
}
LEAD_STOP = re.compile(r"^(?:The|A|An|And|Of|For|With|By|From|In|On|At|To|As|Its|Their|Our|This|That|How|Why|What|When|"
                       r"US|U\.S\.|UK|EU|NATO|New|Latest|Breaking|Exclusive|Watch|Video|Photo)\s+")


def norm(s: str) -> str:
    s = s.lower().replace("ё", "е")
    s = re.sub(r"[«»\"“”'’().,\-]", " ", s)
    s = re.sub(r"\b(inc|corp|corporation|co|ltd|llc|gmbh|ag|sa|sas|spa|bv|ab|asa|oy|plc|ао|ооо|пао)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def register_terms(rows):
    """Names, short names (before «—»), aliases in parentheses."""
    terms = set()
    for r in rows:
        name = r.get("name") or ""
        parts = [name] + re.split(r"\s+[—-]\s+", name) + re.findall(r"\(([^)]+)\)", name)
        parts += [re.sub(r"\([^)]*\)", "", name)]
        for p in parts:
            for q in re.split(r"[;/]", p):
                n = norm(q)
                if len(n) >= 3:
                    terms.add(n)
    return terms


def load_patterns():
    """Tight MENTION_RE from the aggregator if it is importable (not shipped in the public pack)."""
    for d in (Path(__file__).resolve().parent.parent, Path.cwd()):
        if (d / "companies_data.py").exists():
            sys.path.insert(0, str(d))
            try:
                from companies_data import MENTION_RE  # type: ignore
                return [re.compile(p, re.I) for p in MENTION_RE.values()]
            except Exception:
                return []
    return []


def in_register(cand: str, terms, patterns) -> bool:
    n = norm(cand)
    if not n or n in STOP:
        return True
    for t in terms:
        if n == t or (len(t) >= 4 and re.search(rf"(?<!\w){re.escape(t)}(?!\w)", n)) or \
           (len(n) >= 4 and re.search(rf"(?<!\w){re.escape(n)}(?!\w)", t)):
            return True
    return any(p.search(cand) for p in patterns)


def candidates(text: str):
    out = []
    for m in EN_ORG.finditer(text):
        c = LEAD_STOP.sub("", m.group(1)).strip(" .-")
        if len(c.split()) >= 2 or re.search(ORG_SUFFIX, c):
            out.append(c)
    for m in RU_ORG.finditer(text):
        out.append(m.group(1).strip())
    for m in EN_COMPANY.finditer(text):
        out.append(m.group(1).strip())
    clean = []
    for c in out:
        n = norm(c)
        if len(n) < 3 or n in STOP or all(w in GENERIC for w in n.split()):
            continue
        clean.append(c)
    return clean


def texts_from_csv(rows):
    seen = set()
    for r in rows:
        try:
            ex = json.loads(r.get("mention_examples") or "[]")
        except ValueError:
            ex = []
        for e in ex:
            key = e.get("url") or e.get("title")
            if key in seen:
                continue
            seen.add(key)
            yield key, e.get("url") or "", e.get("title") or "", e.get("title") or ""


def texts_from_db(path):
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    for i, url, title, body in conn.execute("select id, url, title, body from items"):
        yield i, url or "", title or "", f"{title or ''} {(body or '')[:3000]}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", required=True)
    ap.add_argument("--db", default="")
    ap.add_argument("--out-csv", default="mention_gap.csv")
    ap.add_argument("--out-md", default="")
    ap.add_argument("--min-items", type=int, default=2, help="keep candidates seen in at least N items")
    ap.add_argument("--limit", type=int, default=200)
    a = ap.parse_args()

    rows = list(csv.DictReader(open(a.csv, encoding="utf-8")))
    terms = register_terms(rows)
    patterns = load_patterns()

    hits = defaultdict(lambda: {"hits": 0, "items": set(), "ex": [], "forms": defaultdict(int)})
    sources = list(texts_from_csv(rows))
    if a.db:
        sources += list(texts_from_db(a.db))
    for key, url, title, text in sources:
        for c in candidates(text):
            if in_register(c, terms, patterns):
                continue
            k = norm(c)
            h = hits[k]
            h["hits"] += 1
            h["forms"][c] += 1
            if key not in h["items"]:
                h["items"].add(key)
                if len(h["ex"]) < 3 and url:
                    h["ex"].append((url, title[:140]))

    out = [(max(h["forms"], key=h["forms"].get), h) for k, h in hits.items() if len(h["items"]) >= a.min_items]
    out.sort(key=lambda x: (-len(x[1]["items"]), -x[1]["hits"], x[0].lower()))
    out = out[:a.limit]

    Path(a.out_csv).parent.mkdir(parents=True, exist_ok=True)
    with open(a.out_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["candidate", "hits", "items", "example_urls", "example_titles"])
        for c, h in out:
            w.writerow([c, h["hits"], len(h["items"]), " ".join(u for u, _ in h["ex"]), " | ".join(t for _, t in h["ex"])])
    if a.out_md:
        with open(a.out_md, "w", encoding="utf-8") as fh:
            fh.write("# Упомянуто в новостях, но отсутствует в реестре — рабочий список\n\n")
            fh.write("Рабочий список кандидатов, **не проверенная перепись**. Названия извлечены регулярными выражениями "
                     "из заголовков и вводных абзацев новостей и сравнены с реестром `companies.csv` "
                     "(названия, псевдонимы, шаблоны упоминаний). Среди кандидатов есть ложные срабатывания "
                     "(продукты, ведомства, общие слова). В реестр ничего автоматически не добавляется: "
                     "строка вносится только после открытия официального сайта и источника.\n\n")
            fh.write("Российские компании в реестр не вносятся (решение 11.11.2026: «Удали все российские компании»); "
                     "российские названия в этом списке — только упоминания в ленте, не кандидаты в реестр.\n\n")
            fh.write(f"Порог: кандидат встретился минимум в {a.min_items} материалах. Кандидатов: {len(out)}.\n\n")
            fh.write("| Кандидат | Материалов | Примеры (ссылки) |\n|---|---:|---|\n")
            for c, h in out:
                links = "; ".join(f"[{t.replace('|', '/').replace(']', ')').replace('[', '(') or 'ссылка'}]({u})" for u, t in h["ex"])
                fh.write(f"| {c.replace('|', '/')} | {len(h['items'])} | {links} |\n")
    print(json.dumps({"register_rows": len(rows), "texts": len(sources), "candidates": len(out),
                      "mention_patterns": len(patterns)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
