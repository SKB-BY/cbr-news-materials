#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Границы мест для «Новостной» карты: news-map/areas.geojson (t57u, 12.11.2026).

Место берётся только из «ключевых мест» новости (словарь мест анализатора). Каждое место рисуется
областью — границей страны, региона, города или акватории, — а не точкой: в новости названо место
целиком, адреса или координат события в ней нет. Центроиды городов как точки не используются.

Источники границ:
  - Natural Earth 1:50m admin-0 map units (страны) и 1:10m admin-1 (регионы, города со статусом региона),
    1:10m geography_marine_polys (моря) — public domain, https://www.naturalearthdata.com
  - OpenStreetMap / Nominatim — административные границы городов, которых нет в admin-1 Natural Earth
    (relation id записан в свойстве `src`), © участники OpenStreetMap, ODbL.

usage: build_news_areas.py <каталог с распакованными NE и nom_*.json> scripts/news_places.json news-map/areas.geojson
Нужны пакеты shapely и pyshp.
"""
import json, sys
from pathlib import Path
import shapefile
from shapely.geometry import shape, mapping
from shapely.ops import unary_union

GEO, GAZ, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
gaz = json.loads(GAZ.read_text(encoding="utf-8"))
TOL = {"country": 0.03, "region": 0.01, "city": 0.002, "sea": 0.03}


def load(path, keyf):
    r = shapefile.Reader(str(path))
    out = {}
    for sr in r.iterShapeRecords():
        k = keyf(sr.record)
        if k:
            out.setdefault(k, []).append(shape(sr.shape.__geo_interface__))
    return out


a0 = load(GEO / "ne_50m_admin_0_map_units/ne_50m_admin_0_map_units", lambda r: r["ADM0_A3"])
gu = load(GEO / "ne_50m_admin_0_map_units/ne_50m_admin_0_map_units", lambda r: r["GU_A3"])
a1 = load(GEO / "ne_10m_admin_1_states_provinces/ne_10m_admin_1_states_provinces", lambda r: r["adm1_code"])
london = load(GEO / "ne_10m_admin_1_states_provinces/ne_10m_admin_1_states_provinces",
              lambda r: "london" if r["admin"] == "United Kingdom" and (r["region"] or "").startswith("Greater London") else None)
sea = load(GEO / "ne_10m_geography_marine_polys/ne_10m_geography_marine_polys", lambda r: r["name"])

feats = []
for name, (prec, parts) in gaz.items():
    geoms, srcs = [], []
    for p in parts:
        typ, _, key = p.partition(":")
        if typ == "a0":
            geoms += a0[key]; srcs.append(f"Natural Earth admin-0 {key}")
        elif typ == "gu":
            geoms += gu[key]; srcs.append(f"Natural Earth admin-0 map unit {key}")
        elif typ == "a1":
            geoms += a1[key]; srcs.append(f"Natural Earth admin-1 {key}")
        elif typ == "london":
            geoms += london["london"]; srcs.append("Natural Earth admin-1 Greater London (33 боро + City)")
        elif typ == "sea":
            geoms += sea[key]; srcs.append(f"Natural Earth marine {key}")
        elif typ == "osm":
            d = json.loads((GEO / f"nom_{key}.json").read_text(encoding="utf-8"))[0]
            geoms.append(shape(d["geojson"])); srcs.append(f"OpenStreetMap {d['osm_type']} {d['osm_id']}")
        else:
            raise SystemExit(f"unknown part {p}")
    g = unary_union(geoms).simplify(TOL[prec], preserve_topology=True)
    gj = mapping(g)

    def rnd(c):
        return [rnd(x) for x in c] if isinstance(c[0], (list, tuple)) else [round(c[0], 4), round(c[1], 4)]
    gj = {"type": gj["type"], "coordinates": rnd(gj["coordinates"])}
    feats.append({"type": "Feature", "properties": {"name": name, "precision": prec, "src": "; ".join(srcs)}, "geometry": gj})

OUT.write_text(json.dumps({"type": "FeatureCollection", "features": feats}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(len(feats), OUT.stat().st_size)
