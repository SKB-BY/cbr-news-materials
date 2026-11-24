#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2026 GREEN-CBR. Все права защищены. Разработчик — GREEN-CBR. Лицензия: LICENSE в корне репозитория.
"""t171u: граф связей «Контура» (graph/) — только из уже публичных файлов среза.

Вход: каталоги ROOT1 [ROOT2 …] по порядку (первый, где файл есть; staging → templates → repo):
  map/data.js (MAP_DATA: узлы реестра, внешние узлы, аналитические связи с URL источника)
  map/contour.js (REG_CONTOUR: узлы node_links t167u-links-2, их материалы, связи контура между узлами)
  darpa-programs/data/darpa_programs.csv, darpa_orgs.csv, darpa_program_orgs.csv
  news-map/entities.json, news-map/relations.json (персоны и их связи с узлами)
Выход OUT: graph_data.js (window.CBR_GRAPH), graph.json, graph.graphml (весь граф), registry.graphml (весь реестр).

Правила:
  * t167u: связь — только реальная (основание с URL: реестр, DARPA, цитаты контура). «Названы в одном материале»
    (совместное упоминание) НЕ включается: заготовка ниже выключена (COMENTION_ENABLED = False, решение GREEN t169s969).
  * DARPA: все программы каталога — узлы; связь программа→организация только при evidence_url; программа→DARPA — по darpa_url.
  * Персоны: только из публичных материалов контура (entities.json), без контактов; узел — если есть связь
    с узлом графа (сопоставление по имени или алиасу, точное после нормализации).
Только стандартная библиотека.
"""
import csv, json, re, sys, unicodedata
from datetime import datetime, timezone, timedelta
from pathlib import Path
from xml.sax.saxutils import escape as xesc, quoteattr

VERSION = "t171u-graph-1"
COPY = "© 2026 GREEN-CBR. Все права защищены. Разработчик — GREEN-CBR"
COMENTION_ENABLED = False   # GREEN t169s969: тип «названы в одном материале» не включать
MINSK = timezone(timedelta(hours=3))
csv.field_size_limit(10 ** 8)

LINK_TYPES = {"contract": "контракт (реестр)", "partner": "партнёрство (реестр)", "structure": "структура (реестр)",
              "ubo": "бенефициар (реестр)", "customer": "заказчик (реестр)"}
DARPA_ROLES = {"performer": "исполнитель программы DARPA", "performer (grant)": "исполнитель по гранту DARPA",
               "prime": "головной исполнитель DARPA", "SETA": "SETA-поддержка DARPA", "grew-from": "выросла из программы DARPA"}


def js_obj(p):
    t = Path(p).read_text(encoding="utf-8")
    t = t[t.index("=") + 1:].strip()
    if t.endswith(";"):
        t = t[:-1]
    return json.loads(t)


def norm(s):
    s = unicodedata.normalize("NFKC", s or "").lower().replace("ё", "е")
    s = re.sub(r"[«»\"'“”„()\[\],.]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def find(roots, rel):
    for r in roots:
        p = Path(r) / rel
        if p.exists():
            return p
    raise FileNotFoundError(rel)


def build(roots):
    md = js_obj(find(roots, "map/data.js"))
    rc = js_obj(find(roots, "map/contour.js"))
    nodes, edges = {}, []

    def add_node(nid, **kw):
        if nid not in nodes:
            nodes[nid] = dict(id=nid, **kw)
        return nodes[nid]

    # 1) узлы реестра и node_links (map/contour.js — тот же набор, что на «Карте реестра»)
    regd = {n["id"]: n for n in md["nodes"]}
    for nid, v in rc["nodes"].items():
        r = regd.get(nid, {})
        add_node(nid, label=v.get("name") or nid, kind=v.get("kind") or "", country=v.get("country") or "",
                 src=v.get("src") or "", n=len(v.get("it") or []), url=r.get("url") or "",
                 role=r.get("role_focus") or "", reg=bool(r))
    for x in md.get("external") or []:
        add_node(x["id"], label=x.get("name") or x["id"], kind="external", country=x.get("country") or "",
                 src="реестр (внешний узел)", n=0, url="", role=x.get("note") or "", reg=False)
    byname = {}
    for nid, n in nodes.items():
        byname.setdefault(norm(n["label"]), nid)

    # 2) аналитические связи реестра (map/data.js links: basis + URL источника)
    for i, l in enumerate(md.get("links") or []):
        if l["from"] in nodes and l["to"] in nodes and l.get("source"):
            edges.append(dict(id="reg:%d" % i, s=l["from"], t=l["to"], type=LINK_TYPES.get(l["type"], l["type"]),
                              g="реестр", basis=l.get("basis") or "", url=l["source"], date="", n=1))

    # 3) связи контура между узлами (REG_CONTOUR.rels, оба конца — узлы), с Окрасом связи
    # t197u волна 3: у связи — коды ОИ 5×5 (текущие), сферы, число разных доменов-источников и даты по материалам-основаниям
    rcu = {}
    for v in (rc.get("items") or {}).values():
        if isinstance(v, list) and len(v) > 7 and v[2]:
            rcu[v[2]] = v

    def ev_meta(ev):
        oi, sp, dom, ds = set(), set(), set(), []
        for x in ev:
            it = rcu.get(x[0])
            if it:
                c = it[6] or it[5]
                if c:
                    oi.add(c)
                for q in it[7] or []:
                    if q and q[0]:
                        sp.add(q[0])
            m = re.match(r"https?://(?:www\.)?([^/]+)", x[0] or "")
            if m:
                dom.add(m.group(1).lower())
            if x[1]:
                ds.append(str(x[1])[:10])
        return dict(oi=sorted(oi), sp=sorted(sp), nd=len(dom), d0=min(ds) if ds else "", d1=max(ds) if ds else "")
    for i, r in enumerate(rc.get("rels") or []):
        if r.get("a") in nodes and r.get("b") in nodes:
            ev = [[e[0], e[1], e[2]] for e in (r.get("ev") or [])[:5]]
            if not ev:
                continue
            edges.append(dict(id="ctr:%d" % i, s=r["a"], t=r["b"], type=r.get("t") or "", g="контур",
                              basis="цитаты из материалов (контур)", url=ev[0][0], date=r.get("d") or "",
                              n=r.get("n") or len(ev), s2=r.get("s2"), s1=r.get("s1"), ev=ev, **ev_meta(r.get("ev") or [])))

    # 4) DARPA: все программы — узлы; программа→DARPA по darpa_url; программа→организация по evidence_url
    progs = list(csv.DictReader(open(find(roots, "darpa-programs/data/darpa_programs.csv"), encoding="utf-8")))
    orgs = {o["id"]: o for o in csv.DictReader(open(find(roots, "darpa-programs/data/darpa_orgs.csv"), encoding="utf-8"))}
    darpa = "darpa" if "darpa" in nodes else None
    for p in progs:
        pid = "darpa-prog:" + p["id"]
        add_node(pid, label=(p.get("short") or p["id"]) + ((" — " + p["official_name"]) if p.get("official_name") and p.get("official_name") != p.get("short") else ""),
                 kind="darpa-program", country="США", src="DARPA", n=int(p.get("news_count") or 0),
                 url=p.get("darpa_url") or "", role=(p.get("office") or "") + ((" · " + p["status"]) if p.get("status") else ""),
                 reg=False, page="../darpa-programs/programs/%s/" % p["id"])
        if darpa and p.get("darpa_url"):
            edges.append(dict(id="dprog:" + p["id"], s=pid, t=darpa, type="программа DARPA", g="DARPA",
                              basis="страница программы на darpa.mil" + ((" · офис " + p["office"]) if p.get("office") else ""),
                              url=p["darpa_url"], date="", n=1))
    omap = {}
    for oid, o in orgs.items():
        if oid in nodes:
            omap[oid] = oid
        elif norm(o.get("name")) in byname:
            omap[oid] = byname[norm(o.get("name"))]
    for i, r in enumerate(csv.DictReader(open(find(roots, "darpa-programs/data/darpa_program_orgs.csv"), encoding="utf-8"))):
        if not r.get("evidence_url"):
            continue
        pid = "darpa-prog:" + r["program_id"]
        if pid not in nodes:
            continue
        oid = r["org_id"]
        nid = omap.get(oid)
        if not nid:
            o = orgs.get(oid, {})
            nid = "darpa-org:" + oid
            add_node(nid, label=o.get("name") or oid, kind="research" if "research" in (r.get("entity_type") or o.get("entity_type") or "") else "company",
                     country="", src="DARPA (организация)", n=int(o.get("news_count") or 0), url="",
                     role=(o.get("listing_status") or "") + ((" · " + o["parent"]) if o.get("parent") else ""), reg=False)
        edges.append(dict(id="dpo:%d" % i, s=pid, t=nid, type=DARPA_ROLES.get(r.get("role"), r.get("role") or ""), g="DARPA",
                          basis=r.get("note") or "", url=r["evidence_url"], date=r.get("evidence_date") or "", n=1))

    # 5) персоны: только публичные лица из публичных материалов; связь — из relations.json с цитатами
    ents = {e["id"]: e for e in json.loads(find(roots, "news-map/entities.json").read_text(encoding="utf-8"))}
    def ent_node(eid):
        if "c:" + eid in nodes:
            return "c:" + eid
        e = ents.get(eid) or {}
        for nm in [e.get("name")] + list(e.get("aliases") or []):
            if nm and norm(nm) in byname and nodes[byname[norm(nm)]]["kind"] != "person":
                return byname[norm(nm)]
        return None
    persons = 0
    for r in json.loads(find(roots, "news-map/relations.json").read_text(encoding="utf-8")):
        fa, fb = ents.get(r["from"], {}), ents.get(r["to"], {})
        pe, other = (fa, r["to"]) if fa.get("type") == "персона" else ((fb, r["from"]) if fb.get("type") == "персона" else (None, None))
        if not pe:
            continue
        if ents.get(other, {}).get("type") == "персона":
            on = "person:" + other if other in ents else None
        else:
            on = ent_node(other)
        ev = [[e.get("url") or "", (e.get("published_at") or "")[:16].replace("T", " "), e.get("quote") or ""] for e in (r.get("evidence") or [])[:5]]
        ev = [e for e in ev if e[0]]
        if not on or not ev:
            continue
        pid = "person:" + pe["id"]
        if pid not in nodes:
            add_node(pid, label=pe.get("name") or pe["id"], kind="person", country=pe.get("country") or "",
                     src="контур (персона)", n=int(pe.get("items") or 0), url="", role="", reg=False)
            persons += 1
        if on.startswith("person:") and on not in nodes:
            o = ents[other]
            add_node(on, label=o.get("name") or other, kind="person", country=o.get("country") or "",
                     src="контур (персона)", n=int(o.get("items") or 0), url="", role="", reg=False)
            persons += 1
        s = r.get("sentiment") or {}
        a, b = ("person:" + r["from"], on) if fa.get("type") == "персона" else (on, "person:" + r["to"])
        edges.append(dict(id="per:" + r["id"], s=a, t=b, type=r.get("type") or "", g="контур",
                          basis="цитаты из материалов (контур)", url=ev[0][0], date=r.get("event_date") or "",
                          n=r.get("evidence_count") or len(ev), s2=s.get("score_pm2"), s1=s.get("score_pm1"), ev=ev))

    # 6) заготовка «названы в одном материале» — выключена
    if COMENTION_ENABLED:  # pragma: no cover
        raise SystemExit("COMENTION_ENABLED: тип не утверждён GREEN")

    deg = {}
    for e in edges:
        deg[e["s"]] = deg.get(e["s"], 0) + 1
        deg[e["t"]] = deg.get(e["t"], 0) + 1
    for n in nodes.values():
        n["deg"] = deg.get(n["id"], 0)
    meta = {"version": VERSION, "links_version": rc.get("links_version"), "oi_as_of": rc.get("oi_as_of"),
            "built_at": datetime.now(MINSK).isoformat(timespec="seconds"), "copyright": COPY,
            "rule": "t167u: связь только при реальной связи (основание с URL); совместные упоминания не включены",
            "counts": {"nodes": len(nodes), "edges": len(edges), "persons": persons,
                       "darpa_programs": sum(1 for n in nodes.values() if n["kind"] == "darpa-program")}}
    return {"meta": meta, "nodes": list(nodes.values()), "edges": edges}, md


NODE_KEYS = ["label", "kind", "country", "src", "n", "deg", "url", "role"]
EDGE_KEYS = ["type", "g", "basis", "url", "date", "n", "s2", "s1"]


def graphml(nodes, edges, meta, title):
    o = ['<?xml version="1.0" encoding="UTF-8"?>', "<!-- %s. %s -->" % (xesc(title), xesc(COPY)),
         '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">']
    for k in NODE_KEYS:
        o.append('<key id="n_%s" for="node" attr.name="%s" attr.type="string"/>' % (k, k))
    for k in EDGE_KEYS:
        o.append('<key id="e_%s" for="edge" attr.name="%s" attr.type="string"/>' % (k, k))
    o.append('<key id="g_meta" for="graph" attr.name="meta" attr.type="string"/>')
    o.append('<graph id="kontur" edgedefault="directed"><data key="g_meta">%s</data>' % xesc(json.dumps(meta, ensure_ascii=False)))
    for n in nodes:
        o.append("<node id=%s>%s</node>" % (quoteattr(n["id"]), "".join(
            '<data key="n_%s">%s</data>' % (k, xesc(str(n.get(k)))) for k in NODE_KEYS if n.get(k) not in (None, ""))))
    for e in edges:
        o.append("<edge id=%s source=%s target=%s>%s</edge>" % (quoteattr(e["id"]), quoteattr(e["s"]), quoteattr(e["t"]), "".join(
            '<data key="e_%s">%s</data>' % (k, xesc(str(e.get(k)))) for k in EDGE_KEYS if e.get(k) not in (None, ""))))
    o.append("</graph></graphml>")
    return "\n".join(o) + "\n"


def main():
    *roots, out = sys.argv[1:]
    out = Path(out)
    g, md = build(roots)
    out.mkdir(parents=True, exist_ok=True)
    js = json.dumps(g, ensure_ascii=False, separators=(",", ":"))
    (out / "graph_data.js").write_text("/* %s. Граф связей «Контура» (%s). */\nwindow.CBR_GRAPH=%s;\n" % (COPY, VERSION, js), encoding="utf-8")
    (out / "graph.json").write_text(json.dumps(g, ensure_ascii=False, indent=0), encoding="utf-8")
    (out / "graph.graphml").write_text(graphml(g["nodes"], g["edges"], g["meta"], "КОНТУР — весь граф связей"), encoding="utf-8")
    regids = {n["id"] for n in md["nodes"]} | {x["id"] for x in md.get("external") or []}
    rn = [n for n in g["nodes"] if n["id"] in regids]
    re_ = [e for e in g["edges"] if e["s"] in regids and e["t"] in regids]
    rmeta = dict(g["meta"], counts={"nodes": len(rn), "edges": len(re_)}, scope="весь реестр (узлы map/data.js и связи между ними)")
    (out / "registry.graphml").write_text(graphml(rn, re_, rmeta, "КОНТУР — весь реестр"), encoding="utf-8")
    print(json.dumps(g["meta"]["counts"] | {"registry_nodes": len(rn), "registry_edges": len(re_)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
