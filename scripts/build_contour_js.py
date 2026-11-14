# t62u: news-map/contour.js — сущности, связи, сфера и окрас для фильтров Новостной карты.
import csv, json, sys
from pathlib import Path
PUB = Path(sys.argv[1]); NM = Path(sys.argv[2]); REG = Path(sys.argv[3])   # pub dir, news-map dir, repo root (companies.csv, map/locations.csv)
ents = json.loads((PUB / "entities.json").read_text(encoding="utf-8"))
rels = json.loads((PUB / "relations.json").read_text(encoding="utf-8"))
items = json.loads((PUB / "items.json").read_text(encoding="utf-8"))
areas = json.loads((NM / "areas.geojson").read_text(encoding="utf-8"))["features"]
anames = [f["properties"]["name"] for f in areas]
part = {}
for n in anames:
    for p in [n] + [x.strip() for x in n.replace("(", "/").replace(")", "/").split("/")]:
        if p and p not in part: part[p.lower()] = n
KYIV = (50.4501, 30.5234)
pts = {}
for r in csv.DictReader(open(REG / "map" / "locations.csv", encoding="utf-8")):
    try: lat, lon = float(r["lat"]), float(r["lon"])
    except Exception: continue
    if r["precision"] != "street": continue            # город без адреса — не точка (UNLOCATED)
    if abs(lat - KYIV[0]) < 1e-3 and abs(lon - KYIV[1]) < 1e-3: continue   # центроид Киева не используется
    pts[r["name"].strip().lower()] = [round(lat, 6), round(lon, 6), r["address_text"], r["source_url"]]
E, unloc = [], []
eidx = {}
for e in ents:
    place = None
    names = [e["name"]] + (e.get("aliases") or [])
    if e["type"] == "локация":
        for n in names:
            if n.lower() in part: place = {"a": part[n.lower()]}; break
    elif e["type"] in ("компания", "организация"):
        for n in names:
            if n.strip().lower() in pts: place = {"p": pts[n.strip().lower()]}; break
    if not place: unloc.append(e)
    eidx[e["id"]] = len(E)
    E.append([e["id"], e["type"], e["name"], (e.get("aliases") or [])[:8], e.get("country") or "", e["items"], place])
R = []
for r in rels:
    s = r.get("sentiment") or {}
    R.append([eidx[r["from"]], eidx[r["to"]], r["type"], r["evidence_count"], s.get("score_pm2"), s.get("score_pm1"),
              [[x["url"], x["published_at"], x["quote"]] for x in r["evidence"]], r.get("event_date") or ""])
I = {}
for it in items:
    s = it["sentiment"] or {}
    I[it["dedupe_hash"][:16]] = [[[x["sphere"], x["subfilter"]] for x in it["spheres"]], s.get("score_pm1"), s.get("score_pm2"),
                                  s.get("subjectivity"), s.get("risk_tags") or [], [eidx[x] for x in it.get("entities", []) if x in eidx], it["url"]]
data = {"entities": E, "relations": R, "items": I, "unlocated": len(unloc)}
(NM / "contour.js").write_text("window.NEWS_CONTOUR=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
for n in ("entities.json", "relations.json", "items.json"):
    (NM / n).write_text((PUB / n).read_text(encoding="utf-8"), encoding="utf-8")
with open(NM / "entities_unlocated.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["id", "type", "name", "country", "items", "reason"])
    for e in unloc:
        why = {"локация": "нет области в словаре мест", "компания": "нет адреса с официальной или реестровой страницы",
               "организация": "нет адреса с официальной или реестровой страницы"}.get(e["type"], "тип не является местом")
        w.writerow([e["id"], e["type"], e["name"], e.get("country") or "", e["items"], why])
from collections import Counter
print(json.dumps({"entities": len(E), "relations": len(R), "items": len(I), "unlocated": len(unloc),
                  "areas": sum(1 for e in E if e[6] and "a" in e[6]), "points": sum(1 for e in E if e[6] and "p" in e[6]),
                  "types": Counter(e[1] for e in E), "bytes": (NM / "contour.js").stat().st_size}, ensure_ascii=False))
