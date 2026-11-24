#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""t86u: публичный каталог darpa-programs для GitHub Pages (все офисы DARPA, сферы, руководители, исполнители, новости).

  python3 darpa_site.py --out <dir> [--base <старый каталог darpa-programs>]
1) копирует из --base файлы, которые этот скрипт не создаёт (data/sam_subawards.*, revolving_door.md и т. п.);
2) darpa.repo(conn) — карточки, таблицы, LEAD_CHECK, UNASSIGNED (только чтение базы);
3) дополняет карточки и README сведениями darpa_ext.json (офис, сфера, руководитель, контракты USAspending, материалы darpa.mil).
Базу не пишет. Публикуются только имена и связи из опубликованных источников; телефонов и e-mail нет.
"""
import argparse, csv, json, re, shutil, sqlite3, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import darpa
import darpa_data as DD
from store import DB_PATH

OFF_RU = {"TTO": "Tactical Technology Office (TTO) — тактические технологии",
          "STO": "Strategic Technology Office (STO) — стратегические технологии",
          "BTO": "Biological Technologies Office (BTO) — биологические технологии",
          "DSO": "Defense Sciences Office (DSO) — оборонные науки",
          "IPTO": "Information Processing Techniques Office (IPTO) — обработка информации",
          "MXO": "Multi X Office (MXO; расширение Microsystems Technology Office, MTO)",
          "SBPO": "Small Business Programs Office (SBPO) — программы малого бизнеса",
          "DO": "Director's Office (DO) — офис директора",
          "": "Офис не указан на странице darpa.mil"}
ORDER = ["TTO", "STO", "IPTO", "MXO", "DSO", "BTO", "SBPO", "DO", ""]
SPHERES = ["вооружение", "бронетехника", "армейские джипы", "артиллерийские системы", "системы ПВО и РВСН", "авиация",
           "средства связи и коммуникаций", "программное обеспечение специального назначения", "тактика и стратегия", "БПЛА"]
ST = {"active": "действует", "completed": "завершена", "unknown": "статус не установлен"}
# t197u-w2 (аудит 6.1г): теги базовых технологий — по ключевым словам в кратком и полном названии и цитате назначения
TECH = [("ИИ/автономность", r"\b(AI|A\.I\.|artificial intelligence|machine learning|autonom\w*|neural|deep learning|reasoning)\b"),
        ("кибербезопасность", r"\b(cyber\w*|malware|vulnerabilit\w*|formal methods|secure software|software security)\b"),
        ("сенсоры/фотоника", r"\b(sensor\w*|sensing|photonic\w*|optic\w*|laser\w*|lidar|radar|infrared|imag(?:ing|er))\b"),
        ("квантовые технологии", r"\bquantum\b"),
        ("микроэлектроника", r"\b(microelectronic\w*|semiconductor\w*|chips?|circuits?|transistor\w*|foundr\w*)\b"),
        ("биотехнологии", r"\b(bio\w*|genetic\w*|genom\w*|vaccin\w*|pathogen\w*|protein\w*)\b"),
        ("космос", r"\b(space|orbit\w*|satellite\w*|lunar|cislunar)\b"),
        ("гиперзвук", r"\bhypersonic\w*\b"),
        ("энергетика", r"\b(energy|batter(?:y|ies)|nuclear|fuel)\b")]
TECH_RE = [(t, re.compile(p, re.I)) for t, p in TECH]


def tech_tags(*texts):
    t = " ".join(x or "" for x in texts)
    return [n for n, rx in TECH_RE if rx.search(t)]


def money_m(x):
    return f"{x / 1e6:,.1f}".replace(",", " ").replace(".", ",") if x else ""


FILTER_HTML = """<div class="dp-filt" id="dp-filt"><b>Фильтр по всем офисам:</b>
<input type="search" id="dp-q" placeholder="Программа, руководитель, исполнитель…">
<select id="dp-st"><option value="">статус: любой</option><option>действует</option><option>завершена</option><option>статус не установлен</option></select>
<select id="dp-tag"><option value="">сфера или технология: любая</option>__OPTS__</select>
<label><input type="checkbox" id="dp-news"> с новостями</label>
<label><input type="checkbox" id="dp-exec"> с исполнителями</label>
<label><input type="checkbox" id="dp-fund"> с суммой USAspending</label>
<label><input type="checkbox" id="dp-dup"> только пометки о совпадении</label>
<span id="dp-n"></span></div>

<script>(function(){function T(){return [].slice.call(document.querySelectorAll('table')).filter(function(t){var h=t.rows[0];return h&&/Технологии/.test(h.textContent);});}
function col(t,n){var c=[].slice.call(t.rows[0].cells);for(var i=0;i<c.length;i++)if(c[i].textContent.indexOf(n)===0)return i;return -1;}
function run(){var q=(document.getElementById('dp-q').value||'').trim().toLowerCase(),st=document.getElementById('dp-st').value,tg=document.getElementById('dp-tag').value,
nw=document.getElementById('dp-news').checked,ex=document.getElementById('dp-exec').checked,fd=document.getElementById('dp-fund').checked,dp=document.getElementById('dp-dup').checked,shown=0,all=0;
T().forEach(function(t){var iS=col(t,'Статус'),iSp=col(t,'Сфера'),iT=col(t,'Технологии'),iN=col(t,'Новостей'),iE=col(t,'Исполнител'),iF=col(t,'Объём'),iP=col(t,'Программа'),v=0;
for(var r=1;r<t.rows.length;r++){var c=t.rows[r].cells,ok=true;all++;
if(q&&t.rows[r].textContent.toLowerCase().indexOf(q)<0)ok=false;
if(ok&&st&&c[iS].textContent.trim()!==st)ok=false;
if(ok&&tg&&(c[iSp].textContent+', '+c[iT].textContent).indexOf(tg)<0)ok=false;
if(ok&&nw&&!(parseInt(c[iN].textContent,10)>0))ok=false;
if(ok&&ex&&!(parseInt(c[iE].textContent,10)>0))ok=false;
if(ok&&fd&&!c[iF].textContent.trim())ok=false;
if(ok&&dp&&c[iP].textContent.indexOf('⚠')<0)ok=false;
t.rows[r].style.display=ok?'':'none';if(ok){v++;shown++;}}
t.style.display=v?'':'none';var h=t.previousElementSibling;if(h&&/^H/.test(h.tagName))h.style.opacity=v?'':'.35';});
document.getElementById('dp-n').textContent='показано программ: '+shown+' из '+all;}
function init(){['dp-q','dp-st','dp-tag','dp-news','dp-exec','dp-fund','dp-dup'].forEach(function(id){var e=document.getElementById(id);if(e)e.addEventListener(e.tagName==='INPUT'&&e.type==='search'?'input':'change',run);});run();}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();})();</script>

<style>.dp-filt{border:1px solid var(--line-2,#2a3340);border-left:3px solid var(--accent,#3fa7ff);padding:6px 10px;margin:8px 0;font-size:13px;position:sticky;top:0;background:var(--bg,#0b0d10);z-index:5}
.dp-filt input[type=search]{min-width:260px}.dp-filt label{margin-right:10px;white-space:nowrap}#dp-n{color:var(--muted,#8a96a3)}</style>
"""


def cell(s):
    return str(s or "").replace("|", "/").replace("\n", " ")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); ap.add_argument("--base")
    a = ap.parse_args()
    out = Path(a.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    if a.base and Path(a.base).is_dir():
        for p in Path(a.base).rglob("*"):
            rel = p.relative_to(a.base)
            if p.is_file() and rel.parts[0] != "programs" and rel.name not in ("README.md",) and "__pycache__" not in rel.parts:
                (out / rel).parent.mkdir(parents=True, exist_ok=True); shutil.copy2(p, out / rel)
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True, timeout=30)
    darpa.repo(conn, out)
    ext = json.loads((HERE / "darpa_ext.json").read_text(encoding="utf-8"))
    E = {p["id"]: p for p in ext["programs"]}
    C = defaultdict(list)
    for c in ext["contracts"]:
        C[c["program_id"]].append(c)
    progs = conn.execute("select id, short, official_name, office, status, news_count from darpa_programs where kind != 'support'").fetchall()
    po = Counter(r[0] for r in conn.execute("select program_id from darpa_program_orgs"))
    tags = conn.execute("select program_ids from darpa_item_tags").fetchall()
    news = Counter(pid for (t,) in tags for pid in json.loads(t or "[]"))
    orgname = {r[0]: r[1] for r in conn.execute("select id, name from darpa_orgs")}
    # t197u-w2 (аудит 6.1б–д): объём USAspending, исполнители со ссылками, теги технологий, пометки одноимённых программ
    fund = defaultdict(float)
    for c in ext["contracts"]:
        try:
            fund[c["program_id"]] += float(c.get("amount") or 0)
        except Exception:
            pass
    porgs = defaultdict(list)
    for p_, o_ in conn.execute("select program_id, org_id from darpa_program_orgs"):
        if o_ not in porgs[p_]:
            porgs[p_].append(o_)
    gids = set()
    try:
        g = json.loads((Path(a.base).parent / "graph" / "graph.json").read_text(encoding="utf-8")) if a.base else {}
        gids = {n["id"] for n in g.get("nodes", [])}
    except Exception:
        gids = set()
    abbr = defaultdict(list)
    for pid, short, name, office, status, _n in progs:
        abbr[re.sub(r"[^A-Z0-9]", "", (short or "").upper())].append((pid, short, name, office))

    offc = {r_[0]: r_[3] for r_ in progs}

    def dup_mark(pid, short, name):
        office = offc.get(pid)
        k = re.sub(r"[^A-Z0-9]", "", (short or "").upper())
        others = [x for x in abbr.get(k, []) if x[0] != pid] if k else []
        if not others:
            return ""
        same = any((x[3] or "") == (office or "") and ((x[2] or "").strip().upper() in ((name or "").upper(), k) or (name or "").strip().upper() == k)
                   for x in others)
        where = "; ".join(f"[{cell(x[2] or x[1])}](programs/{x[0]}/README.md)" for x in others)
        return (" ⚠ возможный дубль (две страницы darpa.mil с одной аббревиатурой): " if same else " ⚠ одноимённая аббревиатура, другая программа: ") + where

    def execs(pid):
        L_ = porgs.get(pid, [])
        out_ = []
        for o_ in L_[:3]:
            nm = cell(orgname.get(o_, o_))
            out_.append(f"[{nm}](../graph/#node={o_})" if o_ in gids else nm)
        return (f"{len(L_)}: " + ", ".join(out_) + (f" и ещё {len(L_) - 3}" if len(L_) > 3 else "")) if L_ else "0"
    # program cards
    for pid, short, name, office, status, _n in progs:
        f = out / "programs" / pid / "README.md"
        if not f.exists():
            continue
        e = E.get(pid, {})
        L = ["", "## Категория и сфера (t86u, проверка " + ext["as_of"] + ")", "",
             f"- Офис DARPA (категория): {OFF_RU.get(e.get('office_abbr', ''), office or 'не указан')}" if e else f"- Офис DARPA: {office or 'не указан'}",
             f"- Статус по darpa.mil: {'пометка «This program is now complete»' if e.get('status') == 'completed' else ('пометки о завершении нет' if e else ST.get(status, status))}",
             f"- Сфера (ось сайта, словарь sphere.py по названию и цитате назначения): {', '.join(e.get('spheres') or []) or 'не назначена (признаков нет)'}", ""]
        if e.get("pm"):
            L += ["## Руководитель программы (darpa.mil)", ""] + [f"- {x['name']} — [страница DARPA]({x['bio']})" for x in e["pm"]] + [""]
        cs = sorted(C.get(pid, []), key=lambda c: c.get("start") or "")
        if cs:
            L += [f"## Исполнители: контракты и гранты DARPA по USAspending.gov ({len(cs)})", "",
                  "Только записи, где описание контракта называет программу (правило совпадения — в последней колонке). Сумма — обязательства по записи USAspending, не цена программы.", "",
                  "| Дата начала | Получатель | Награда | Сумма, $ | Описание (USAspending) | Совпадение |", "|---|---|---|---|---|---|"]
            for c in cs:
                amt = f"{float(c['amount']):,.0f}".replace(",", " ") if c.get("amount") is not None else ""
                L.append(f"| {c.get('start','')} | {cell(orgname.get(c['org_id'], c['recipient']))} | [{c['award_id']}]({c['url']}) | {amt} | {cell(c['description'])[:220]} | {c['match']} |")
            L.append("")
        if e.get("related"):
            L += ["## Связанные материалы darpa.mil", ""] + [f"- [{cell(x['title'])}]({x['url']})" for x in e["related"]] + [""]
        f.write_text(f.read_text(encoding="utf-8").rstrip("\n") + "\n" + "\n".join(L), encoding="utf-8")
    # index
    by = defaultdict(list)
    for pid, short, name, office, status, _n in progs:
        e = E.get(pid, {})
        by[e.get("office_abbr", "") if e else ("" if not office else next((k for k, v in OFF_RU.items() if office and office.split(" (")[0] in v), ""))].append((pid, short, name, status, e))
    total = len(progs)
    sph = Counter(s for e in E.values() for s in (e.get("spheres") or []))
    R = ["# Программы DARPA — реестр по всем офисам", "",
         f"Проверка {ext['as_of']} (Europe/Minsk). В реестре {total} программ: все страницы программ из карты сайта darpa.mil "
         f"(https://www.darpa.mil/sitemap.xml, раздел /research/programs/) и программы, найденные в новостях агрегатора без страницы darpa.mil.", "",
         "Источники: страница программы на darpa.mil (название, офис, назначение — цитата, руководитель, пометка «This program is now complete»); "
         "исполнители — открытый API USAspending.gov (агентство-заказчик DARPA; в реестр попадают только записи, где описание контракта называет программу); "
         "новости — совпадение названия программы в хранилище агрегатора (live и архив). Пустое поле — в источнике нет. "
         "Непроверенные совпадения на публичные страницы не выносятся.", "",
         "Офис I2O на darpa.mil на дату проверки не значится; программы информационной тематики там указаны с офисом IPTO. "
         "MTO расширен в Multi X Office (MXO) — по странице https://www.darpa.mil/about/offices/mxo.", "",
         "Колонки «Объём USAspending» — сумма обязательств по записям USAspending.gov, где описание контракта называет программу "
         "(не цена программы); «Исполнители» — реестр связей программа → организация (первые три, ссылка — узел в Графе связей, если он есть); "
         "«Технологии» — теги по ключевым словам в названии и цитате назначения darpa.mil (правило — scripts/darpa_site.py, TECH); "
         "⚠ — пометка об одноимённых программах: «возможный дубль» — две страницы darpa.mil с одной аббревиатурой и совпадающим названием, "
         "«одноимённая аббревиатура» — разные программы. Строки не удаляются.", "",
         "## Сводка по офисам (категориям)", "", "| Офис | Программ | Действуют | Завершены | С исполнителями | С новостями |", "|---|---|---|---|---|---|"]
    for k in ORDER:
        rows = by.get(k, [])
        if not rows:
            continue
        R.append(f"| [{OFF_RU[k]}](#{('office-' + (k or 'none')).lower()}) | {len(rows)} | {sum(1 for r in rows if r[3]=='active')} | {sum(1 for r in rows if r[3]=='completed')} | {sum(1 for r in rows if po.get(r[0]))} | {sum(1 for r in rows if news.get(r[0]))} |")
    R += ["", FILTER_HTML.replace("__OPTS__", "".join(f"<option>{x}</option>" for x in SPHERES + [t for t, _ in TECH])), ""]
    R += ["", "## Сферы (ось сайта)", "", "| Сфера | Программ |", "|---|---|"] + [f"| {s} | {sph.get(s, 0)} |" for s in SPHERES] + [
          "", "Сфера назначается словарём sphere.py (термин в названии или цитате назначения; иначе ≥2 разных термина в описании). У остальных программ признаков нет — сфера не назначается.", ""]
    for k in ORDER:
        rows = sorted(by.get(k, []), key=lambda r: r[1].lower())
        if not rows:
            continue
        R += [f'<a id="{("office-" + (k or "none")).lower()}"></a>', "", f"## {OFF_RU[k]} — {len(rows)}", "",
              "| Программа | Полное название | Статус | Сфера | Технологии | Руководитель (darpa.mil) | Исполнители | Объём USAspending, $ млн | Новостей |",
              "|---|---|---|---|---|---|---|---|---|"]
        for pid, short, name, status, e in rows:
            R.append(f"| [{cell(short)}](programs/{pid}/README.md){dup_mark(pid, short, name)} | {cell(name)} | {ST.get(status, status)} | {cell(', '.join(e.get('spheres') or [])) if e else ''} | "
                     f"{cell(', '.join(tech_tags(short, name, (e or {}).get('purpose'))))} | "
                     f"{cell(', '.join(x['name'] for x in (e.get('pm') or []))) if e else ''} | {execs(pid)} | {money_m(fund.get(pid, 0))} | {news.get(pid, 0)} |")
        R.append("")
    R += ["## Таблицы", "", "- `data/darpa_programs.csv`, `data/darpa_orgs.csv`, `data/darpa_program_orgs.csv`, `data/darpa_personnel.csv` — реестр;",
          "- `data/darpa_contracts_usaspending.csv` — контракты и гранты по программам (USAspending.gov);",
          "- `data/darpa_item_tags.json` — разметка новостей; `LEAD_CHECK.md` — проверка вводного списка; `UNASSIGNED.md` — материалы с DARPA без названной программы.", ""]
    old = (out / "README.md").read_text(encoding="utf-8")
    tail = old[old.find("## Листинг организаций"):] if "## Листинг организаций" in old else ""
    (out / "README.md").write_text("\n".join(R) + "\n" + tail, encoding="utf-8")
    with open(out / "data" / "darpa_contracts_usaspending.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["program_id", "org_id", "recipient", "award_id", "award_group", "start", "amount_usd", "description", "url", "match"])
        for c in ext["contracts"]:
            w.writerow([c["program_id"], c["org_id"], c["recipient"], c["award_id"], c["award_group"], c.get("start", ""), c.get("amount", ""), c["description"], c["url"], c["match"]])
    (out / "scripts").mkdir(exist_ok=True)
    for fn in ("darpa.py", "darpa_data.py", "darpa_t86u.py", "darpa_site.py"):
        if (HERE / fn).exists():
            shutil.copy2(HERE / fn, out / "scripts" / fn)
    shutil.copy2(HERE / "darpa_ext.json", out / "data" / "darpa_ext.json")
    # t86u: связи «новость → программа DARPA» для Новостной карты (ключ — первые 16 символов dedupe_hash)
    pn = {r[0]: (r[1] or r[0]) for r in conn.execute("select id, short from darpa_programs")}
    tags = {}
    for h, pids in conn.execute("select dedupe_hash, program_ids from darpa_item_tags where program_ids not in ('', '[]')"):
        lst = [[x, pn[x]] for x in json.loads(pids or "[]") if x in pn]
        if lst and h:
            tags[h[:16]] = lst
    (out / "data" / "news_tags.js").write_text("window.DARPA_NEWS_TAGS=" + json.dumps(tags, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print(json.dumps({"programs": total, "offices": {k or "—": len(v) for k, v in by.items()}, "contracts": len(ext["contracts"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
