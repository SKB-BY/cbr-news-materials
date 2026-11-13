# -*- coding: utf-8 -*-
"""t86u (13.11.2026): расширение рабочего реестра DARPA по всем офисам darpa.mil.

Данные — darpa_ext.json рядом с этим файлом (собраны с darpa.mil/sitemap.xml: страницы /research/programs/<slug>,
офис, пометка «This program is now complete», руководитель программы, связанные материалы; контракты — открытый API
USAspending.gov, агентство-заказчик DARPA, только записи, где описание контракта называет программу).
Ничего не выдумывается: пустое поле = в источнике нет. Ошибка чтения файла не ломает сводку: списки остаются пустыми.
"""
import json
from pathlib import Path

AS_OF = "2026-11-13"
EXT = {}
PROGRAMS_T86U, ORGS_T86U, PROGRAM_ORGS_T86U, PERSONNEL_T86U = [], [], [], []
EXISTING_UPDATE = {}   # id -> {"office", "status"} для программ, уже бывших в реестре (только если там пусто)

try:
    EXT = json.loads((Path(__file__).with_name("darpa_ext.json")).read_text(encoding="utf-8"))
except Exception:
    EXT = {}

for p in EXT.get("programs", []):
    if p.get("existing"):
        EXISTING_UPDATE[p["id"]] = {"office": p.get("office") or "", "status": p.get("status") or "", "darpa_url": p.get("darpa_url") or ""}
    else:
        PROGRAMS_T86U.append((p["id"], p["short"], p["official_name"], p["kind"], p["darpa_url"], p.get("office") or "",
                              p.get("status") or "unknown", "", p.get("purpose") or "", p.get("purpose_src") or "",
                              p.get("strong") or [], p.get("weak") or []))
    for pm in p.get("pm") or []:
        PERSONNEL_T86U.append((pm["name"], "DARPA program manager", "", p["id"], p["darpa_url"],
                               "руководитель программы по странице darpa.mil (проверка " + AS_OF + ")"))

_names = EXT.get("orgs_new", {})
for oid, name in sorted(_names.items()):
    src = next((c["url"] for c in EXT.get("contracts", []) if c.get("org_id") == oid), "")
    ORGS_T86U.append((oid, name, "unknown", "", "", "", src,
                      "получатель контракта / гранта DARPA по USAspending.gov; листинг не проверялся (" + AS_OF + ")"))

_agg = {}
for c in EXT.get("contracts", []):
    k = (c["program_id"], c["org_id"])
    a = _agg.setdefault(k, {"urls": [], "ids": [], "start": [], "amount": 0.0, "grp": set(), "how": set()})
    a["urls"].append(c["url"]); a["ids"].append(c["award_id"]); a["start"].append(c.get("start") or "")
    a["amount"] += float(c.get("amount") or 0); a["grp"].add(c["award_group"]); a["how"].add(c["match"])
for (pid, oid), a in sorted(_agg.items()):
    starts = sorted(s for s in a["start"] if s)
    ids = sorted(set(a["ids"]))
    note = ("USAspending: " + ", ".join(ids[:6]) + (f" и ещё {len(ids) - 6}" if len(ids) > 6 else "")
            + f"; сумма обязательств по записям USAspending ${a['amount']:,.0f}".replace(",", " ")
            + "; " + "; ".join(sorted(a["how"])))
    PROGRAM_ORGS_T86U.append((pid, oid, "performer" if "contract" in a["grp"] else "performer (grant)",
                              a["urls"][0], starts[0] if starts else "", note))

# Быстрый предфильтр разметки (darpa.py match_text): программа проверяется регулярными выражениями, только если
# в тексте есть самое длинное слово её полного названия или аббревиатуры. Шаблон без этого слова совпасть не может.
import re as _re
_TOK = _re.compile(r"[a-z0-9]+")
KEYS = {}
for p in EXT.get("programs", []):
    if p.get("existing"):
        continue
    ks = set()
    for s in (p.get("official_name") or "", p.get("short") or ""):
        t = _TOK.findall((s or "").lower())
        if t:
            ks.add(max(t, key=len))
    KEYS[p["id"]] = ks
