#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fill lat/lon in map/locations.csv with OpenStreetMap Nominatim (stdlib only).

Only the published locality in `geocode_query` is geocoded (street > city > region > state, see
`precision`). Rows with precision=none are never placed on the map.

Nominatim usage policy: max 1 request/second, an identifying User-Agent. The User-Agent is taken
from env NOMINATIM_USER_AGENT; if it is not set the script runs in dry-run mode and only prints the
queries. Example (project contact URL, no personal e-mail):
  NOMINATIM_USER_AGENT="CBRNewsAggregator/1.0 (+https://gitlab.com/cbr-uav-group/n8n-news-aggregator)" \
    python3 scripts/geocode_locations.py
Options: --force  re-geocode rows that already have lat/lon.
"""
import csv, json, os, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "map" / "locations.csv"
ZOOM = {"street": 18, "city": 10, "region": 8, "state": 5}


def main():
    ua = os.environ.get("NOMINATIM_USER_AGENT", "").strip()
    force = "--force" in sys.argv
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    cols = list(rows[0].keys())
    cache, last = {}, 0.0
    todo = [r for r in rows if r["precision"] != "none" and (force or not r["lat"])]
    if not ua:
        print("DRY RUN: NOMINATIM_USER_AGENT is not set; queries that would be sent:")
        for r in todo:
            print(" ", r["id"], "|", r["precision"], "|", r["geocode_query"])
        return
    for r in todo:
        q = r["geocode_query"]
        if q not in cache:
            time.sleep(max(0.0, 1.1 - (time.time() - last)))
            url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
                {"q": q, "format": "jsonv2", "limit": 1, "accept-language": "en"})
            req = urllib.request.Request(url, headers={"User-Agent": ua})
            try:
                cache[q] = json.load(urllib.request.urlopen(req, timeout=30))
            except Exception as e:  # noqa
                cache[q] = []
                print("ERR", r["id"], e)
            last = time.time()
        res = cache[q]
        if res:
            r["lat"], r["lon"] = "%.6f" % float(res[0]["lat"]), "%.6f" % float(res[0]["lon"])
            r["geocoder"] = "nominatim: " + res[0].get("display_name", "")[:160]
            print("OK ", r["id"], r["lat"], r["lon"], "|", r["geocoder"][:90])
        else:
            print("MISS", r["id"], "|", q)
    if "geocoder" not in cols:
        cols.append("geocoder")
    with open(CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, cols)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})


if __name__ == "__main__":
    main()
