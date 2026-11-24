#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2026 GREEN-CBR. Все права защищены. Разработчик — GREEN-CBR. Лицензия: LICENSE в корне репозитория.
"""t171u: публичный таймлайн эволюции сюжетов (iid/timeline/) — только из уже публичных файлов среза.

Решения GREEN t169s969: серверная история изменений (history/oi_history.sqlite) наружу НЕ выкладывается;
публичный таймлайн строится только из публичных данных: начальный и текущий код ОИ 5×5 (oi0, oi1, oi1at),
кластеры дедупликации, связи подтверждения, Окрас и Субъективность материалов, сюжеты ИИД-100.
Связь сюжета ИИД с новостями: (1) тот же материал или его кластер; (2) подтверждение / перепечатка / ссылка
(data/oi5x5/links_news.csv); (3) ключи мест и организаций сюжета — только реальное совпадение названия
(словоформы публичного словаря iid/iid_lex.json в заголовке новости) или узла реестра (map/node_index.js, t167u).
Ключи чисел и дат (N:, D:) для связи не используются. Сюжеты «только для расчёта ИИД-100» — метка со спойлером
(io_name, t157u/t158u), без URL; в выгрузки не идут (iid_only).

Вход: каталоги-источники по порядку (первый, где файл есть): ROOT1 [ROOT2 ...]; выход: OUT (iid/timeline).
Только стандартная библиотека.
"""
import csv, json, re, sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

VERSION = "t197u-timeline-2"
COPY = "© 2026 GREEN-CBR. Все права защищены. Разработчик — GREEN-CBR"
MINSK = timezone(timedelta(hours=3))
WINDOW_DAYS = 7          # новости по ключам — в пределах ±7 суток от начала сюжета
MAX_KEY_LINKS = 25       # не более 25 новостей по ключам на сюжет (больше общих ключей — выше)
csv.field_size_limit(10 ** 8)


def find(roots, rel):
    for r in roots:
        p = Path(r) / rel
        if p.exists():
            return p
    raise FileNotFoundError(rel)


def js_obj(p):
    t = Path(p).read_text(encoding="utf-8")
    t = t[t.index("=") + 1:].strip()
    return json.loads(t[:-1] if t.endswith(";") else t)


def parse_t(s):
    if not s:
        return None
    s = s.strip().replace(" ", "T")
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    if len(s) == 10:
        s += "T00:00+03:00"
    if re.match(r".*T\d\d:\d\d$", s):
        s += "+03:00"     # время карт — Europe/Minsk
    try:
        d = datetime.fromisoformat(s)
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=MINSK)


def iso(d):
    return d.astimezone(MINSK).isoformat(timespec="minutes") if d else ""


def form_rx(lex, forms, lang="ru"):
    L = lex["langs"][lang]
    ends = sorted(L.get("endings") or [], key=len, reverse=True)
    prefix = L.get("form_mode") == "prefix"
    parts = []
    for f in forms:
        words = f.lower().split()
        last = words[-1]
        if prefix and len(last) >= 5:
            lt = re.escape(last) + r"\w*"
        else:
            e = "|".join(re.escape(x) for x in ends)
            lt = re.escape(last) + (f"(?:{e})?" if e else "") + r"(?!\w)"
        toks = [re.escape(w) + r"\w*" for w in words[:-1]] + [lt]
        parts.append((r"(?<![\w-])" if prefix else r"(?<!\w)") + r"[\s,]+".join(toks))
    return re.compile("|".join(parts)) if parts else None


def build(roots):
    iid = json.loads(find(roots, "iid/iid.json").read_text(encoding="utf-8"))
    lex = json.loads(find(roots, "iid/iid_lex.json").read_text(encoding="utf-8"))
    nm = js_obj(find(roots, "news-map/data.js"))
    cx = js_obj(find(roots, "news-map/contour.js"))
    ni = js_obj(find(roots, "map/node_index.js"))
    F = nm["fields"]
    items = [dict(zip(F, a)) for a in nm["items"]]
    by_id = {x["id"]: i for i, x in enumerate(items)}
    by_url = {x["url"]: i for i, x in enumerate(items) if x.get("url")}
    for x in items:
        c = cx["items"].get(x["id"])
        x["okr"] = c[2] if c else None
        x["okr_score"] = c[1] if c else None
        x["subj"] = c[3] if c else None
        x["sp"] = sorted({q[0] for q in (c[0] or []) if q and q[0]}) if c else []   # t197u волна 3: сферы материала (фильтр таймлайна)
        x["_t"] = parse_t(x.get("pub"))
    clusters = [[k for k in c[0]] for c in nm["clusters"]]
    cl_of = {}
    for ci, c in enumerate(clusters):
        for k in c:
            cl_of[k] = ci
    # связи подтверждения/перепечатки/ссылки — только между материалами карты
    links = {}
    for r in csv.DictReader(open(find(roots, "data/oi5x5/links_news.csv"), encoding="utf-8")):
        a, b = by_id.get(r["id_a"][:16]), by_id.get(r["id_b"][:16])
        if a is None or b is None or r["link_type"] == "тот_же_факт":
            continue
        links.setdefault(a, []).append((b, r["link_type"]))
        links.setdefault(b, []).append((a, r["link_type"]))
    # словарь ключей мест и организаций (ru — заголовки карты по-русски)
    krx, kname = {}, {}
    for grp in ("places", "orgs", "mention"):
        for p in lex.get(grp) or []:
            fr = (p.get("forms") or {}).get("ru")
            if fr:
                rx = form_rx(lex, fr)
                if rx:
                    krx["P:" + p["code"] if grp == "places" else "O:" + p["code"]] = rx
                    kname["P:" + p["code"] if grp == "places" else "O:" + p["code"]] = p.get("name") or p["code"]
    node_items = ni.get("items") or {}
    node_names = {k: v[0] for k, v in (ni.get("nodes") or {}).items()}

    countries = {"O:" + p["code"] for p in lex.get("mention") or [] if p.get("kind") == "страна"}
    def is_country(k):
        return (k.startswith("P:") and "-" not in k[2:]) or k in countries

    def ev_item(i, via, kind="material"):
        x = items[i]
        return {"kind": kind, "t": iso(x["_t"]), "src": x["src"], "url": x["url"], "title": x["t"], "oi": x.get("oi1") or x["oi0"],
                "oi0": x["oi0"], "oi1": x.get("oi1") or "", "oi1at": x.get("oi1at") or "", "okr": x["okr"], "okr_score": x["okr_score"],
                "subj": x["subj"], "id": x["id"], "via": via}

    def key_match(i, key):
        x = items[i]
        if key.startswith("O:reg:"):
            return key[6:] in (node_items.get(x["id"]) or [])
        rx = krx.get(key)
        return bool(rx and rx.search((x.get("t") or "").lower()))

    stories = []
    for s in iid.get("stories") or []:
        t0 = parse_t(s.get("t0"))
        io = bool(s.get("io_name"))
        st = {"id": "iid:" + s["id"], "kind": "iid", "title": s.get("title") or "", "url": s.get("url") or "", "t0": iso(t0),
              "window_until": s.get("window_until") or "", "countries": s.get("countries") or [], "sphere": s.get("sphere") or "",
              "iid_before": (s.get("before") or {}).get("iid"), "iid_after": (s.get("after") or {}).get("iid"), "delta": s.get("delta"),
              "effect": s.get("effect"), "closed": bool(s.get("after_closed")), "n": s.get("n"), "nneg": s.get("nneg"),
              "keys": [k for k in s.get("keys") or [] if k[:2] in ("P:", "O:")], "iid_only": io}
        if io:
            st["io_name"] = s["io_name"]
        evs, seen = [], set()
        for m in s.get("materials") or []:
            e = {"kind": "material", "t": m.get("t") or "", "src": m.get("source") or "", "url": m.get("url") or "", "title": m.get("title") or "",
                 "oi": m.get("oi") or "", "okr": None, "okr_score": m.get("S"), "subj": m.get("subj"), "via": "материал сюжета ИИД-100"}
            if m.get("iid_only"):
                e.update(iid_only=True, url="", src="‹источник скрыт›")
            evs.append(e)
            i = by_url.get(m.get("url")) if m.get("url") else None
            if i is not None:
                seen.add(i)
                e.update({k: v for k, v in ev_item(i, e["via"]).items() if k in ("oi0", "oi1", "oi1at", "okr", "id")})
                ci = cl_of.get(i)
                for k in (clusters[ci] if ci is not None else []):
                    if k not in seen:
                        seen.add(k); evs.append(ev_item(k, "тот же сюжет (кластер дедупликации)", "linked"))
                for k, lt in links.get(i, []):
                    if k not in seen:
                        seen.add(k); evs.append(ev_item(k, lt.replace("_", " ") + " (связь ОИ 5×5)", "linked"))
        if s.get("response"):
            r = s["response"]
            evs.append({"kind": "response", "t": r.get("t") or "", "src": r.get("source") or "", "url": r.get("url") or "", "title": r.get("title") or "",
                        "oi": r.get("oi") or "", "okr": None, "okr_score": None, "subj": r.get("subj"), "via": "отклик (ИИД-100): " + (r.get("timely") or "")})
        if t0 and st["keys"]:
            need = min(2, len(st["keys"]))
            lo, hi = t0 - timedelta(days=WINDOW_DAYS), t0 + timedelta(days=WINDOW_DAYS)
            cand = []
            for i, x in enumerate(items):
                if i in seen or not x["_t"] or not (lo <= x["_t"] <= hi):
                    continue
                hit = [k for k in st["keys"] if key_match(i, k)]
                # страна сама по себе слишком широка: нужен хотя бы один ключ точнее страны (город, область, организация, узел реестра)
                if len(hit) >= need and any(not is_country(k) for k in hit):
                    cand.append((len(hit), -abs((x["_t"] - t0).total_seconds()), i, hit))
            cand.sort(reverse=True)
            for nh, _, i, hit in cand[:MAX_KEY_LINKS]:
                names = [kname.get(k) or node_names.get(k[6:], k[6:]) if k.startswith("O:reg:") else kname.get(k, k) for k in hit]
                evs.append(ev_item(i, "ключи: " + ", ".join(names), "linked"))
            st["key_links_total"] = len(cand)
        st["key_names"] = [node_names.get(k[6:], k[6:]) if k.startswith("O:reg:") else kname.get(k, k) for k in st["keys"]]
        evs.sort(key=lambda e: e["t"] or "")
        st["events"] = evs
        stories.append(st)

    # сюжеты Новостной карты: кластеры из ≥2 материалов или с эволюцией кода ОИ (oi1)
    nstories = []
    for ci, c in enumerate(clusters):
        if len(c) < 2 and not any(items[k].get("oi1") for k in c):
            continue
        evs = [ev_item(k, "материал сюжета (кластер дедупликации)") for k in c]
        inset = set(c)
        for k in c:
            for j, lt in links.get(k, []):
                if j not in inset:
                    inset.add(j); evs.append(ev_item(j, lt.replace("_", " ") + " (связь ОИ 5×5)", "linked"))
        for k in c:
            x = items[k]
            if x.get("oi1") and x.get("oi1at"):
                evs.append({"kind": "oi_change", "t": iso(parse_t(x["oi1at"])), "day": len(x["oi1at"]) == 10, "src": x["src"], "url": x["url"], "title": x["t"], "oi": x["oi1"],
                            "oi0": x["oi0"], "oi1": x["oi1"], "oi1at": x["oi1at"], "okr": x["okr"], "okr_score": x["okr_score"], "subj": x["subj"],
                            "id": x["id"], "via": "код ОИ 5×5 изменился: %s → %s" % (x["oi0"], x["oi1"])})
        evs.sort(key=lambda e: e["t"] or "")
        h = items[c[0]]
        okrs = [e["okr"] for e in evs if e.get("okr") is not None and e["kind"] != "oi_change"]
        nstories.append({"id": "news:" + h["id"], "kind": "news", "title": h["t"], "url": h["url"], "t0": evs[0]["t"] if evs else "",
                         "t1": evs[-1]["t"] if evs else "", "n": len(c), "changed": any(items[k].get("oi1") for k in c),
                         "okr_range": [min(okrs), max(okrs)] if okrs else None, "sp": sorted({q for k in c for q in items[k].get("sp") or []}), "events": evs})
    nstories.sort(key=lambda s: s["t1"], reverse=True)
    meta = {"version": VERSION, "built_at": datetime.now(MINSK).isoformat(timespec="seconds"), "copyright": COPY,
            "iid_computed_at": iid.get("computed_at"), "iid_method": iid.get("method_version"), "news_as_of": nm.get("as_of"), "oi_as_of": nm.get("oi_as_of"),
            "rules": {"window_days": WINDOW_DAYS, "max_key_links": MAX_KEY_LINKS, "keys": "P: места и O: организации (словарь iid_lex.json, заголовок по-русски) и O:reg: узлы реестра (node_index, t167u); нужно не меньше min(2, число ключей) совпадений и хотя бы один ключ точнее страны; N: и D: не используются"},
            "history_note": "Полная история изменений ОИ 5×5, Окраса и Субъективности хранится только на сервере (решение GREEN t169s969) и сюда не выкладывается. Здесь — только публичные данные: начальный и текущий код ОИ (с датой изменения), кластеры, связи подтверждения, Окрас и Субъективность материалов.",
            "counts": {"iid_stories": len(stories), "iid_only_stories": sum(1 for s in stories if s["iid_only"]), "news_stories": len(nstories),
                       "news_changed": sum(1 for s in nstories if s["changed"])}}
    return {"meta": meta, "iid": stories, "news": nstories}


def main():
    *roots, out = sys.argv[1:]
    out = Path(out)
    d = build(roots)
    out.mkdir(parents=True, exist_ok=True)
    (out / "timeline_data.js").write_text("/* %s. Таймлайн сюжетов (%s). */\nwindow.CBR_TIMELINE=%s;\n" % (
        COPY, VERSION, json.dumps(d, ensure_ascii=False, separators=(",", ":"))), encoding="utf-8")
    print(json.dumps(d["meta"]["counts"], ensure_ascii=False))
    # t197u: «Что нового с прошлого среза» в Актуальном отчёте: срез (staging) против опубликованного (repo).
    # Таймлайн — последний шаг сборки; ошибка блока на таймлайн не влияет (в отчёте остаётся «сравнение не выполнено»).
    try:
        import subprocess
        p = subprocess.run([sys.executable, str(Path(__file__).with_name("build_whatsnew.py")), roots[0], roots[-1]],
                           capture_output=True, text=True, timeout=300)
        print((p.stdout + p.stderr).strip()[-200:], file=sys.stderr)
    except Exception as e:
        print("t197u whatsnew: " + str(e)[:200], file=sys.stderr)
    # t197u волна 3: каталог «Источники сбора» (SOURCES.md: состояние сбора, КПД лент за 30 суток, архив); журнал — INGEST_LOG.md.
    # При ошибке в срез кладётся опубликованный SOURCES.md (каталог не откатывается к шаблону).
    try:
        import subprocess, shutil
        p = subprocess.run([sys.executable, str(Path(__file__).with_name("build_sources.py")), roots[0], roots[1] if len(roots) > 1 else roots[0]],
                           capture_output=True, text=True, timeout=300)
        print((p.stdout + p.stderr).strip()[-200:], file=sys.stderr)
        if p.returncode and not (Path(roots[0]) / "SOURCES.md").exists() and (Path(roots[-1]) / "SOURCES.md").exists():
            shutil.copy2(Path(roots[-1]) / "SOURCES.md", Path(roots[0]) / "SOURCES.md")
    except Exception as e:
        print("t197u sources: " + str(e)[:200], file=sys.stderr)


if __name__ == "__main__":
    main()
