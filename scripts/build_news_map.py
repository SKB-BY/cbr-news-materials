#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""«Новостная» карта: news-map/data.js, news-map/news_points.csv, news-map/UNLOCATED.md, news-map/news_unlocated.csv
(t57u, 12.11.2026, Europe/Minsk).

Читает рабочую базу новостей (SQLite, только чтение; в репозиторий не входит) и news-map/areas.geojson.

Отбор:
  * новости с датой публикации с 01.01.2026 (Europe/Minsk) по последний материал базы, у которых есть код ОИ 5×5;
  * «поднятые» записи — более ранние материалы базы, на которые новость 2026 г. ссылается как на тот же факт,
    подтверждение или ссылку: они наносятся вместе с новой записью в одном сюжете (принцип актуальности);
  * актуальность: если более поздняя новость прямо связана с более ранней («тот_же_факт», «подтверждение», «ссылка»,
    «перепечатка»), ранняя считается дополненной и показывается под актуальной записью (вместе с ней на карте, по месту
    актуальной записи); актуальная запись — новость 2026 г., которую ещё никто не дополнил. Связи берутся только прямые
    (без цепочек), чтобы не склеивать разные факты. Дополненная запись, чей «дополнитель» сам уже дополнен,
    показывается отдельно с пометкой «дополнена позже» и ссылками на более поздние записи.
Место — только из «ключевых мест» новости (словарь мест); на карте — областью (страна / регион / город / акватория).
Органы и программы (FAA, Пентагон и т.п.) местом не считаются. Коды ОИ не выдумываются; дата публикации
не подставляется вместо даты события. Текст новости и тезисы не публикуются — только метаданные, заголовок и коды.
"""
import csv, json, re, sqlite3, sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from public_export import PALETTE, redact, clean_ru, status_of  # noqa: E402

DB = sys.argv[1]
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE.parent / "news-map"
START = "2026-01-01"
MSK = timezone(timedelta(hours=3))  # Europe/Minsk, без перехода на летнее время
LIFT_TYPES = {"тот_же_факт", "подтверждение", "ссылка"}
CLUSTER_TYPES = LIFT_TYPES | {"перепечатка"}
TOPIC = {"drones": "Дроны", "countermeasures": "Противодействие", "navigation": "Навигация"}
CATEGORY = {"military": "военные", "FPV": "FPV", "commercial": "коммерческие", "industrial": "промышленные"}
VEHICLE = {"air": "воздух", "ground": "земля", "water": "вода"}


def minsk(iso):
    if not iso:
        return ""
    d = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(MSK).strftime("%Y-%m-%d %H:%M")


def cut(s, n=220):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
areas = json.loads((OUT / "areas.geojson").read_text(encoding="utf-8"))
AREA = {f["properties"]["name"]: f for f in areas["features"]}

rows = {}
Q = """select i.dedupe_hash, i.published_at, i.source, i.url, i.title, coalesce(nullif(t.lang_original,''), i.language), i.topic_domain, i.category, i.section,
       i.vehicle_domain, t.title_ru, a.event_date, a.event_date_precision, a.places,
       o.initial_code, o.evolved_code, o.evolved_at, i.collected_at
       from items i left join item_translation t using(dedupe_hash) left join item_analysis a using(dedupe_hash)
       join item_oi o using(dedupe_hash) where o.initial_code is not null and i.published_at >= ?"""
# 2025-12-31 21:00Z = 01.01.2026 00:00 Europe/Minsk
for r in con.execute(Q, ("2025-12-31T21:00:00Z",)):
    if minsk(r[1])[:10] >= START:
        rows[r[0]] = r
base = set(rows)

links = []
for a, b, t in con.execute("select dedupe_hash_a, dedupe_hash_b, link_type from fact_links where from_kind='новость' and to_kind='новость'"):
    if t in CLUSTER_TYPES:
        links.append((a, b, t))

# поднятые записи: более ранние материалы, с которыми новость 2026 г. связана как тот же факт / подтверждение / ссылка
lift = set()
for a, b, t in links:
    if t in LIFT_TYPES:
        if b in base and a not in base:
            lift.add(a)
        elif a in base and b not in base:
            lift.add(b)
QL = Q.replace("and i.published_at >= ?", "and i.dedupe_hash = ?")
for h in sorted(lift):
    r = con.execute(QL, (h,)).fetchone()
    if r and minsk(r[1])[:10] < START:
        rows[h] = r
lift = {h for h in lift if h in rows}

# сюжеты по принципу актуальности: более поздняя связанная новость дополняет более раннюю;
# актуальная запись — та, которую ещё никто не дополнил; ранние записи поднимаются в её историю
newer = defaultdict(set)   # h -> более поздние связанные
older = defaultdict(set)   # h -> более ранние связанные
rel = defaultdict(set)
for a, b, t in links:
    if a in rows and b in rows and a != b:
        x, y = sorted((a, b), key=lambda h: (rows[h][1] or "", h))  # по дате публикации
        newer[x].add(y); older[y].add(x)
        rel[a].add(t); rel[b].add(t)
HIST_CAP = 40

LT = {"тот_же_факт": "тот же факт", "подтверждение": "подтверждение", "ссылка": "ссылка", "перепечатка": "перепечатка"}
items, places_of = {}, {}
for h, r in rows.items():
    (_, pub, src, url, title, lang, topic, cat, sec, veh, tr, ev, evp, places, oi0, oi1, oi1at, _coll) = r
    lang = lang or ""
    if lang.startswith("ru") or lang == "und":
        ttl, tflag = redact(cut(title)), 0
    else:
        t_ru = redact(clean_ru(tr or ""))
        ttl, tflag = (cut(t_ru), 1) if t_ru else (redact(cut(title)), 2)
    pl = []
    for p in json.loads(places or "[]"):
        if p.get("name") in AREA and p["name"] not in pl:
            pl.append(p["name"])
    other = sorted({p["name"] for p in json.loads(places or "[]") if p.get("name") not in AREA})
    assert oi0 in PALETTE and (not oi1 or oi1 in PALETTE), (h, oi0, oi1)
    items[h] = {
        "id": h, "pub": minsk(pub), "ev": ev or "", "evp": evp or "", "src": src or "", "url": url or "",
        "t": ttl, "tf": tflag, "lang": lang, "topic": TOPIC.get(topic, ""), "cat": CATEGORY.get(cat, ""),
        "sec": sec if sec and sec != "Иные" else ("иные" if sec else ""), "veh": VEHICLE.get(veh, ""),
        "oi0": oi0, "oi1": oi1 or "", "oi1at": minsk(oi1at)[:10] if oi1at else "",
        "lift": 1 if h in lift else 0, "rel": sorted(LT[x] for x in rel.get(h, ())), "nonplace": other,
    }
    places_of[h] = pl


def chron(it):  # дата для хронологии: дата события, если названа; иначе дата публикации
    return (it["ev"] or it["pub"][:10], it["pub"])


clusters, unplaced = [], []
heads = [h for h in rows if h in base and not newer.get(h)]
shown = set(heads)
for h in heads:
    shown |= older.get(h, set())
# дополненные записи, чей более поздний «дополнитель» сам уже дополнен: показываются отдельной записью
# с пометкой «дополнена позже», чтобы ни одна поднятая или ранняя запись не пропала с карты
orphans = [h for h in rows if h not in shown]


def mk(h, current):
    hist = sorted(older.get(h, ()), key=lambda x: chron(items[x]), reverse=True)
    pl = list(places_of[h])
    if not pl:  # место ранней записи, если в самой новости места нет
        for m in hist + (sorted(newer.get(h, ()), key=lambda x: chron(items[x])) if not current else []):
            for p in places_of[m]:
                if p not in pl:
                    pl.append(p)
    return {"head": h, "items": [h] + hist[:HIST_CAP], "places": pl, "more": max(0, len(hist) - HIST_CAP),
            "current": current, "later": sorted(newer.get(h, ()), key=lambda x: chron(items[x]), reverse=True)[:5]}


for h in heads:
    c = mk(h, True)
    (clusters if c["places"] else unplaced).append(c)
for h in orphans:
    c = mk(h, False)
    (clusters if c["places"] else unplaced).append(c)

clusters.sort(key=lambda c: chron(items[c["head"]]), reverse=True)
used = {h for c in clusters for h in c["items"]}
idx = {h: i for i, h in enumerate(sorted(used, key=lambda h: chron(items[h]), reverse=True))}
FIELDS = ["id", "pub", "ev", "evp", "src", "url", "t", "tf", "lang", "topic", "cat", "sec", "veh", "oi0", "oi1", "oi1at", "lift", "rel", "nonplace"]
item_arr = [None] * len(idx)
for h, i in idx.items():
    it = dict(items[h]); it["id"] = h[:16]
    item_arr[i] = [it[k] for k in FIELDS]
assert len({x[0] for x in item_arr}) == len(item_arr)
area_names = [n for n in AREA if any(n in c["places"] for c in clusters)]
aidx = {n: i for i, n in enumerate(area_names)}
cl_arr = [[[idx[h] for h in c["items"]], [aidx[p] for p in c["places"]], c["more"], int(c["current"]),
           [idx[h] for h in c["later"] if h in idx]] for c in clusters]

as_of = minsk(max(rows[h][17] or "" for h in base))  # по времени сбора: у части сайтов время публикации без пояса
oi_as_of = con.execute("select max(updated_at) from job_checkpoint where job like 'oi5x5%'").fetchone()[0] or ""
data = {
    "title": "Новостная карта", "as_of": as_of, "oi_as_of": minsk(oi_as_of) if oi_as_of else "",
    "from": START, "fields": FIELDS, "palette": PALETTE,
    "areas": {"type": "FeatureCollection", "features": [AREA[n] for n in area_names]},
    "items": item_arr, "clusters": cl_arr,
}
(OUT / "data.js").write_text("window.NEWS_MAP_DATA=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")

# news_points.csv: одна строка на пару «новость — место»
PRECR = {"country": "страна", "region": "регион", "city": "город", "sea": "акватория"}
with open(OUT / "news_points.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["id", "story", "is_current", "lifted", "published_at_minsk", "event_date", "event_date_precision", "source", "url",
                "title_ru", "oi_initial", "oi_evolved", "status", "place", "place_precision", "area_source"])
    for k, c in enumerate(clusters):
        for h in c["items"]:
            it = items[h]; code = it["oi1"] or it["oi0"]
            for p in c["places"]:
                w.writerow([h, k + 1, int(h == c["head"] and c["current"]), it["lift"], it["pub"], it["ev"], it["evp"], it["src"], it["url"],
                            it["t"], it["oi0"], it["oi1"], status_of(code), p,
                            PRECR[AREA[p]["properties"]["precision"]], AREA[p]["properties"]["src"]])
with open(OUT / "news_unlocated.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["id", "lifted", "published_at_minsk", "event_date", "source", "url", "title_ru", "oi_initial", "oi_evolved", "status", "named_not_a_place"])
    for c in sorted(unplaced, key=lambda c: chron(items[c["head"]]), reverse=True):
        for h in c["items"]:
            it = items[h]; code = it["oi1"] or it["oi0"]
            w.writerow([h, it["lift"], it["pub"], it["ev"], it["src"], it["url"], it["t"], it["oi0"], it["oi1"], status_of(code),
                        "; ".join(it["nonplace"])])
nonplace = sorted({n for h in items for n in items[h]["nonplace"]})
(OUT / "UNLOCATED.md").write_text(f"""# Новостная карта — что не нанесено

Срез: новости с датой публикации с 01.01.2026 по {as_of[:10][8:10]}.{as_of[5:7]}.{as_of[:4]} {as_of[11:]} Europe/Minsk.

На карту не наносятся сюжеты, в ключевых местах которых нет ни одного места из словаря мест (страна, регион, город, акватория).
Точку для таких новостей не выдумываем: по заголовку или источнику место не подставляется. Перечень — [news_unlocated.csv](news_unlocated.csv)
(те же метаданные и коды ОИ 5×5, что и на карте; в колонке `named_not_a_place` — названные органы и программы).

Органы и программы из словаря ключевых мест местом не считаются — у них нет точки события. Если в той же новости есть
место, новость стоит на карте по этому месту; если нет — в news_unlocated.csv:

{chr(10).join('- ' + n for n in nonplace)}

Места рисуются областью (граница страны, региона, города, акватории), а не точкой: в новости названо место целиком,
адреса события нет. Центроид города как координаты события не используется.

Новые материалы, поступившие после прохода ОИ, на карту не попадают до следующего прохода: код ОИ 5×5 не выдумывается.
""", encoding="utf-8")

print(json.dumps({"base_2026": len(base), "lifted": len(lift), "clusters_on_map": len(clusters), "items_on_map": len(used),
                  "lifted_on_map": sum(1 for h in used if items[h]["lift"]), "unplaced_clusters": len(unplaced),
                  "unplaced_items": sum(len(c["items"]) for c in unplaced), "areas": len(area_names), "as_of": as_of,
                  "oi_as_of": data["oi_as_of"], "orphans": len(orphans), "orphans_on_map": sum(1 for c in clusters if not c["current"]), "max_cluster": max(len(c["items"]) for c in clusters), "capped": sum(1 for c in clusters if c["more"]), "with_history": sum(1 for c in clusters if len(c["items"])>1),
                  "no_translation": sum(1 for h in used if items[h]["tf"] == 2),
                  "data_js": (OUT / "data.js").stat().st_size}, ensure_ascii=False, indent=1))
