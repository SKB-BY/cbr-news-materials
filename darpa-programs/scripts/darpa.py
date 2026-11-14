# -*- coding: utf-8 -*-
"""DARPA working register: программы, организации, листинг, персоналии + разметка новостей.

Рабочий реестр, не перепись всех программ DARPA. Данные — darpa_data.py (каждая строка с URL
источника). Разметка новостей пишет только в таблицу darpa_item_tags (ключ — dedupe_hash), поэтому
перенос строк items в архив (archive/news_archive.sqlite) разметку не теряет. Архив читается
только на чтение. Транзакции записи короткие (пакеты по 200 строк).

  python3 darpa.py seed            # таблицы darpa_programs / darpa_orgs / darpa_program_orgs / darpa_personnel
  python3 darpa.py tag             # разметка live + archive (если есть)
  python3 darpa.py export --csv-dir export/darpa
  python3 darpa.py repo --out /tmp/darpa-programs   # дерево для GitLab-проекта darpa-programs
  python3 darpa.py block --since 2026-11-11T03:00:00Z --until 2026-11-11T15:00:00Z  # блок для сводки
"""
from __future__ import annotations

import argparse, csv, json, os, re, sqlite3, sys
from calendar import monthrange
from datetime import datetime, timedelta, timezone
from pathlib import Path

import darpa_data as DD
from store import DB_PATH, connect

ARCHIVE = Path(os.environ.get("CBR_NEWS_ARCHIVE", str(Path(DB_PATH).parent / "archive" / "news_archive.sqlite")))
DARPA_CTX = re.compile(r"DARPA|ДАРПА|Defense Advanced Research Projects|Агентств\w* перспективных (оборонных )?исследовательских", re.I)

DDL = """
CREATE TABLE IF NOT EXISTS darpa_programs (
  id TEXT PRIMARY KEY, short TEXT, official_name TEXT, kind TEXT, darpa_url TEXT, office TEXT,
  status TEXT, period TEXT, purpose TEXT, purpose_src TEXT, patterns TEXT, as_of TEXT,
  news_count INTEGER DEFAULT 0, news_examples TEXT);
CREATE TABLE IF NOT EXISTS darpa_orgs (
  id TEXT PRIMARY KEY, name TEXT, listing_status TEXT, ticker TEXT, exchange TEXT, parent TEXT,
  invest_source TEXT, note TEXT, as_of TEXT, news_count INTEGER DEFAULT 0);
CREATE TABLE IF NOT EXISTS darpa_program_orgs (
  program_id TEXT, org_id TEXT, role TEXT, evidence_url TEXT, evidence_date TEXT, note TEXT,
  PRIMARY KEY (program_id, org_id, role, evidence_url));
CREATE TABLE IF NOT EXISTS darpa_personnel (
  name TEXT, role TEXT, org_id TEXT, program_id TEXT, evidence_url TEXT, note TEXT,
  PRIMARY KEY (name, role, program_id, org_id));
CREATE TABLE IF NOT EXISTS darpa_lead_check (
  claim TEXT PRIMARY KEY, verdict TEXT, detail TEXT, source TEXT, as_of TEXT);
CREATE TABLE IF NOT EXISTS darpa_item_tags (
  dedupe_hash TEXT PRIMARY KEY, item_id INTEGER, db TEXT, url TEXT, title TEXT, published_at TEXT,
  program_ids TEXT, org_ids TEXT, matched TEXT, tagged_at TEXT);
CREATE INDEX IF NOT EXISTS idx_darpa_tags_pub ON darpa_item_tags(published_at);
"""

# t25u columns (added by migrate(); empty = no opened source)
NEW_COLS = {
    "darpa_orgs": ["successor_entity", "successor_source", "acquisition_date", "acquisition_source", "acquisition_note",
                   "entity_type", "entity_type_source"],
    "darpa_program_orgs": ["entity_type"],
    "darpa_programs": ["adversarial_mirror", "mirror_country", "mirror_source"],
    "darpa_personnel": ["red_flag", "red_flag_source"],
}


def migrate(conn):
    conn.executescript(DDL)
    for t, cols in NEW_COLS.items():
        have = {r[1] for r in conn.execute(f"pragma table_info({t})")}
        for c in cols:
            if c not in have:
                conn.execute(f"alter table {t} add column {c} TEXT")
    conn.commit()

# company mention patterns (latin + russian). Mention of a company does NOT imply a program.
ORG_RX = {
 "lockheed": r"Lockheed|Локхид", "boeing": r"\bBoeing\b|Боинг", "northrop": r"Northrop|Нортроп",
 "rtx": r"\bRTX\b|Raytheon|Рейтеон|Рэйтеон", "bbn": r"\bBBN\b", "moderna": r"Moderna|Модерн[аы]",
 "irobot": r"iRobot", "boston-dynamics": r"Boston Dynamics|Бостон Дайнемикс", "siri": r"\bSiri\b",
 "sri": r"SRI International", "spacex": r"SpaceX", "blue-origin": r"Blue Origin|Блю Ориджин",
 "anduril": r"Anduril|Андурил", "shield-ai": r"Shield AI|Hivemind", "ionq": r"\bIonQ\b",
 "rigetti": r"Rigetti", "atom-computing": r"Atom Computing", "diraq": r"\bDiraq\b",
 "quantinuum": r"Quantinuum", "psiquantum": r"PsiQuantum", "quera": r"QuEra", "xanadu": r"Xanadu",
 "firefly": r"Firefly Aerospace", "redwire": r"Redwire", "sierra-space": r"Sierra Space", "gitai": r"\bGITAI\b",
 "strategic-analysis": r"Strategic Analysis,? Inc", "guidehouse": r"Guidehouse", "spa": r"Systems Planning and Analysis",
 "amentum": r"Amentum", "booz-allen": r"Booz Allen", "bae": r"BAE Systems|\bBAE\b", "palantir": r"Palantir|Палантир",
 "charles-river": r"Charles River Analytics", "soartech": r"SoarTech|Accelint", "parallax": r"Parallax Advanced Research",
 "leidos": r"Leidos|Лейдос", "dynetics": r"Dynetics", "calspan": r"Calspan", "aerovironment": r"AeroVironment|АэроВайронмент",
 "skydio": r"Skydio|Скайдио", "waymo": r"Waymo", "aurora": r"Aurora Innovation", "argo-ai": r"Argo AI", "nuro": r"\bNuro\b",
 "qinetiq-na": r"QinetiQ|Foster-Miller", "palladyne": r"Palladyne|Sarcos", "l3harris": r"L3Harris",
 "field-ai": r"Field AI", "overland-ai": r"Overland AI", "carnegie-robotics": r"Carnegie Robotics",
 "avidrone": r"AVIDrone", "portal-aircraft": r"Portal Aircraft",
}


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# t89u: в бот (сводка, «Актуальный отчёт») программа DARPA попадает только при наличии
# связанной новости за последние BOT_RECENT_DAYS суток от момента отчёта, Europe/Minsk.
# Дата события (item_analysis.event_date), если указана; иначе дата публикации. Страница сайта не затронута.
MINSK = timezone(timedelta(hours=3))
BOT_RECENT_DAYS = 7


def now_minsk(ts=None):
    if ts is None:
        return datetime.now(MINSK)
    if ts.tzinfo is None:
        return ts.replace(tzinfo=MINSK)
    return ts.astimezone(MINSK)


def bot_cutoff(as_of=None, days=BOT_RECENT_DAYS):
    return now_minsk(as_of) - timedelta(days=days)


def parse_published(s):
    """published_at → datetime Europe/Minsk, иначе None."""
    if not s:
        return None
    raw = str(s).strip()
    if not raw:
        return None
    try:
        if raw.endswith("Z"):
            dt = datetime.fromisoformat(raw[:-1] + "+00:00")
        else:
            dt = datetime.fromisoformat(raw)
    except ValueError:
        try:
            dt = datetime.strptime(raw[:19], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=MINSK)
    return dt.astimezone(MINSK)


def parse_event_date(s):
    """event_date (YYYY-MM-DD / YYYY-MM / YYYY) → date. Для неполной даты — последний день периода."""
    raw = (s or "").strip()
    if not raw:
        return None
    if len(raw) >= 10 and raw[4] == "-" and raw[7] == "-":
        try:
            return datetime.strptime(raw[:10], "%Y-%m-%d").date()
        except ValueError:
            pass
    if len(raw) >= 7 and raw[4] == "-" and raw[:7].replace("-", "").isdigit():
        try:
            y, m = int(raw[:4]), int(raw[5:7])
            return datetime(y, m, monthrange(y, m)[1]).date()
        except ValueError:
            pass
    if len(raw) >= 4 and raw[:4].isdigit():
        try:
            return datetime(int(raw[:4]), 12, 31).date()
        except ValueError:
            pass
    return None


def effective_dt(published_at, event_date=None):
    """Дата события (конец дня, Europe/Minsk), если указана и разобрана; иначе дата публикации."""
    ev = parse_event_date(event_date)
    if ev is not None:
        return datetime(ev.year, ev.month, ev.day, 23, 59, 59, tzinfo=MINSK)
    return parse_published(published_at)


def item_is_recent(published_at, event_date=None, as_of=None, days=BOT_RECENT_DAYS):
    dt = effective_dt(published_at, event_date)
    if dt is None:
        return False
    return dt >= bot_cutoff(as_of, days)


def _tag_rows_with_event(conn):
    has_ia = conn.execute(
        "select 1 from sqlite_master where type='table' and name='item_analysis'"
    ).fetchone()
    if has_ia:
        return conn.execute(
            "select t.program_ids, t.published_at, a.event_date "
            "from darpa_item_tags t "
            "left join item_analysis a on a.dedupe_hash=t.dedupe_hash "
            "where t.program_ids is not null and t.program_ids != '[]'"
        ).fetchall()
    return conn.execute(
        "select program_ids, published_at, null from darpa_item_tags "
        "where program_ids is not null and program_ids != '[]'"
    ).fetchall()


def recent_program_hits(conn, as_of=None, days=BOT_RECENT_DAYS):
    """program_id → {short, latest (datetime Minsk), count} за скользящие days суток."""
    try:
        names = {r[0]: r[1] for r in conn.execute("select id, short from darpa_programs")}
        rows = _tag_rows_with_event(conn)
    except Exception:
        return {}
    cutoff = bot_cutoff(as_of, days)
    out = {}
    for r in rows:
        try:
            pids = json.loads(r[0] or "[]") or []
        except Exception:
            pids = []
        dt = effective_dt(r[1], r[2])
        if not pids or dt is None or dt < cutoff:
            continue
        for pid in pids:
            rec = out.setdefault(pid, {"short": names.get(pid, pid), "latest": dt, "count": 0})
            rec["count"] += 1
            if dt > rec["latest"]:
                rec["latest"] = dt
    return out


def program_latest_dates(conn):
    """program_id → {short, latest} по всем размеченным новостям (для отчёта «снято»)."""
    try:
        names = {r[0]: r[1] for r in conn.execute("select id, short from darpa_programs")}
        rows = _tag_rows_with_event(conn)
    except Exception:
        return {}
    out = {}
    for r in rows:
        try:
            pids = json.loads(r[0] or "[]") or []
        except Exception:
            pids = []
        dt = effective_dt(r[1], r[2])
        for pid in pids:
            rec = out.setdefault(pid, {"short": names.get(pid, pid), "latest": dt})
            if dt is not None and (rec["latest"] is None or dt > rec["latest"]):
                rec["latest"] = dt
    return out


def format_bot_recent_audit(conn, as_of=None, days=BOT_RECENT_DAYS):
    """Текст проверки t89u: какие программы остаются в боте и какие сняты."""
    as_of_dt = now_minsk(as_of)
    cutoff = bot_cutoff(as_of_dt, days)
    kept = recent_program_hits(conn, as_of_dt, days)
    allp = program_latest_dates(conn)
    dropped = {pid: rec for pid, rec in allp.items() if pid not in kept}
    lines = [
        f"darpa t89u as_of={as_of_dt.strftime('%Y-%m-%d %H:%M:%S %Z')} "
        f"cutoff={cutoff.strftime('%Y-%m-%d %H:%M:%S %Z')} days={days}",
        f"kept={len(kept)} dropped={len(dropped)} tagged_programs={len(allp)}",
    ]
    if kept:
        lines.append("kept:")
        for pid, rec in sorted(kept.items(), key=lambda kv: kv[1]["latest"], reverse=True):
            last = rec["latest"].strftime("%Y-%m-%d %H:%M Europe/Minsk")
            lines.append(f"  {rec['short']} ({pid}) last={last} n={rec['count']}")
    else:
        lines.append("kept: (none)")
    if dropped:
        lines.append("dropped:")
        def _key(kv):
            return kv[1]["latest"] or datetime(1, 1, 1, tzinfo=MINSK)
        for pid, rec in sorted(dropped.items(), key=_key, reverse=True):
            last = rec["latest"].strftime("%Y-%m-%d %H:%M Europe/Minsk") if rec["latest"] else "—"
            lines.append(f"  {rec['short']} ({pid}) last={last}")
    else:
        lines.append("dropped: (none)")
    return "\n".join(lines)


def seed(conn):
    migrate(conn)
    progs = DD.PROGRAMS + [DD.SETA]
    with conn:
        for p in progs:
            i, short, name, kind, url, office, status, period, purpose, psrc, strong, weak = p
            conn.execute("""INSERT INTO darpa_programs (id,short,official_name,kind,darpa_url,office,status,period,purpose,purpose_src,patterns,as_of)
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET short=excluded.short, official_name=excluded.official_name,
              kind=excluded.kind, darpa_url=excluded.darpa_url, office=excluded.office, status=excluded.status, period=excluded.period,
              purpose=excluded.purpose, purpose_src=excluded.purpose_src, patterns=excluded.patterns, as_of=excluded.as_of""",
              (i, short, name, kind, url, office, status, period, purpose, psrc, json.dumps({"strong": strong, "weak": weak}), DD.AS_OF))
        for o in DD.ORGS:
            conn.execute("""INSERT INTO darpa_orgs (id,name,listing_status,ticker,exchange,parent,invest_source,note,as_of)
              VALUES (?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET name=excluded.name, listing_status=excluded.listing_status,
              ticker=excluded.ticker, exchange=excluded.exchange, parent=excluded.parent, invest_source=excluded.invest_source,
              note=excluded.note, as_of=excluded.as_of""", (*o, DD.AS_OF))
        for o in DD.ORGS:
            acq = DD.ACQUISITION.get(o[0], ("", "", "", "", ""))
            et = DD.ENTITY_TYPE.get(o[0], ("", ""))
            conn.execute("""update darpa_orgs set successor_entity=?, successor_source=?, acquisition_date=?, acquisition_source=?,
              acquisition_note=?, entity_type=?, entity_type_source=? where id=?""", (*acq, *et, o[0]))
        for p in progs:
            conn.execute("update darpa_programs set adversarial_mirror=?, mirror_country=?, mirror_source=? where id=?",
                         (*DD.MIRROR.get(p[0], ("", "", "")), p[0]))
        conn.execute("DELETE FROM darpa_program_orgs")
        conn.executemany("INSERT OR REPLACE INTO darpa_program_orgs (program_id,org_id,role,evidence_url,evidence_date,note,entity_type) VALUES (?,?,?,?,?,?,?)",
                         [(*x, DD.ENTITY_TYPE.get(x[1], ("", ""))[0]) for x in DD.PROGRAM_ORGS])
        conn.execute("DELETE FROM darpa_personnel")
        conn.executemany("INSERT OR REPLACE INTO darpa_personnel (name,role,org_id,program_id,evidence_url,note,red_flag,red_flag_source) VALUES (?,?,?,?,?,?,?,?)",
                         [(*x, *DD.PERSONNEL_RED_FLAG.get((x[0], x[3]), ("", ""))) for x in DD.PERSONNEL])
        conn.execute("DELETE FROM darpa_lead_check")
        conn.executemany("INSERT OR REPLACE INTO darpa_lead_check VALUES (?,?,?,?,?)", [(*c, DD.AS_OF) for c in DD.LEAD_CHECK])


def compile_programs():
    out = []
    for p in DD.PROGRAMS:
        i, strong, weak = p[0], p[10], p[11]
        out.append((i, [re.compile(x, re.I if re.search(r"[a-zа-я]", x.replace("\\b", "")) else 0) for x in strong],
                    [re.compile(x) for x in weak]))
    return out


NOISE = re.compile(r"DARPA ?& ?CIA|darpaandcia", re.I)  # подпись/ссылка канала «DARPA&CIA» — не упоминание агентства


def successor_watch(progs):
    """[(old_org_id, successor_rx, [program strong rx])] for acquired orgs with a filled successor and program links."""
    strong = {pid: st for pid, st, _w in progs}
    out = []
    for oid, (succ, *_rest) in DD.ACQUISITION.items():
        rx = DD.SUCCESSOR_RX.get(oid)
        pids = sorted({x[0] for x in DD.PROGRAM_ORGS if x[1] == oid and x[0] in strong})
        if succ and rx and pids:
            out.append((oid, re.compile(rx), [r for pid in pids for r in strong[pid]]))
    return out


try:  # t86u: предфильтр по ключевым словам для программ из darpa_ext.json (ускорение разметки архива)
    from darpa_t86u import KEYS as T86U_KEYS
except Exception:  # noqa: BLE001
    T86U_KEYS = {}
_TOKEN = re.compile(r"[a-z0-9]+")


def match_text(text, progs, orgs, watch=()):
    pids, matched = [], []
    text = NOISE.sub(" ", text)
    ctx = bool(DARPA_CTX.search(text))
    toks = None
    for pid, strong, weak in progs:
        keys = T86U_KEYS.get(pid)
        if keys is not None:
            if toks is None:
                toks = set(_TOKEN.findall(text.lower()))
            if not (keys & toks):
                continue
        hit = next((m.group(0) for rx in strong if (m := rx.search(text))), None)
        if not hit and ctx:
            hit = next((m.group(0) for rx in weak if (m := rx.search(text))), None)
        if hit:
            pids.append(pid); matched.append(f"{pid}:{hit}")
    oids = [oid for oid, rx in orgs if rx.search(text)]
    # successor hook: old org is still tagged when the successor AND an old-program term are named together
    for oid, srx, terms in watch:
        if oid not in oids and srx.search(text) and any(t.search(text) for t in terms):
            oids.append(oid); matched.append(f"successor:{oid}")
    return pids, oids, ctx, matched


def tag_db(live, path, label, progs, orgs, watch=()):
    src = sqlite3.connect(f"file:{path}?mode=ro", uri=True) if label == "archive" else live
    rows = src.execute("select id, dedupe_hash, url, title, body, published_at from items").fetchall()
    out = []
    for r in rows:
        text = f"{r[3] or ''}\n{(r[4] or '')[:6000]}"
        pids, oids, ctx, matched = match_text(text, progs, orgs, watch)
        # keep item if a program matched, or DARPA is named, or a DARPA-linked org is named together with DARPA
        if pids or ctx:
            out.append((r[1], r[0], label, r[2], (r[3] or "")[:300], r[5], json.dumps(pids), json.dumps(oids),
                        json.dumps(matched + (["DARPA"] if ctx else []), ensure_ascii=False), now()))
    for k in range(0, len(out), 200):
        with live:
            live.executemany("""INSERT INTO darpa_item_tags VALUES (?,?,?,?,?,?,?,?,?,?) ON CONFLICT(dedupe_hash) DO UPDATE SET
              item_id=excluded.item_id, db=excluded.db, url=excluded.url, title=excluded.title, published_at=excluded.published_at,
              program_ids=excluded.program_ids, org_ids=excluded.org_ids, matched=excluded.matched, tagged_at=excluded.tagged_at""",
              out[k:k + 200])
    if label == "archive":
        src.close()
    return len(rows), len(out)


def tag(conn):
    migrate(conn)
    progs = compile_programs()
    orgs = [(k, re.compile(v)) for k, v in ORG_RX.items()]
    watch = successor_watch(progs)
    stats = {"live": tag_db(conn, None, "live", progs, orgs, watch)}
    if ARCHIVE.is_file():
        stats["archive"] = tag_db(conn, ARCHIVE, "archive", progs, orgs, watch)
    # counts per program / org
    tags = conn.execute("select program_ids, org_ids, url, title, published_at from darpa_item_tags").fetchall()
    with conn:
        for (pid,) in conn.execute("select id from darpa_programs").fetchall():
            hits = sorted([t for t in tags if pid in json.loads(t[0])], key=lambda t: t[4] or "", reverse=True)
            ex = [{"url": t[2], "title": t[3][:160], "published_at": t[4]} for t in hits[:5]]
            conn.execute("update darpa_programs set news_count=?, news_examples=? where id=?", (len(hits), json.dumps(ex, ensure_ascii=False), pid))
        for (oid,) in conn.execute("select id from darpa_orgs").fetchall():
            n = sum(1 for t in tags if oid in json.loads(t[1]))
            conn.execute("update darpa_orgs set news_count=? where id=?", (n, oid))
    return stats


def window_tags(conn, since, until):
    """Tagged items in a time window (for the digest)."""
    try:
        return conn.execute("""select dedupe_hash, url, title, published_at, program_ids, org_ids from darpa_item_tags
                               where published_at >= ? and published_at < ? order by published_at desc""", (since, until)).fetchall()
    except sqlite3.OperationalError:
        return []


def digest_block(conn, since, until, esc=lambda s: s, limit=8):
    """Text block «Программы DARPA» for the digest. Empty string when nothing is tagged in the window."""
    rows = window_tags(conn, since, until)
    if not rows:
        return ""
    names = {r[0]: r[1] for r in conn.execute("select id, short from darpa_programs")}
    by = {}
    for r in rows:
        for pid in json.loads(r[4]) or ["—"]:
            by.setdefault(pid, []).append(r)
    lines = ["<b>Программы DARPA</b>",
             "Материалы окна, где названы DARPA или программа из рабочего реестра darpa-programs. Связь — по совпадению названия в тексте."]
    # t89u: именованная программа — только если по ней есть новость за последние 7 дней (Europe/Minsk).
    recent = recent_program_hits(conn)
    by = {pid: items for pid, items in by.items() if pid == "—" or pid in recent}
    if not by:
        return ""
    for pid, items in sorted(by.items(), key=lambda kv: kv[0] or ""):
        label = names.get(pid, "DARPA без названной программы") if pid != "—" else "DARPA без названной программы"
        lines.append(f"• {esc(label)}")
        for r in items[:limit]:
            lines.append(f"  – <a href=\"{esc(r[1])}\">{esc((r[2] or '')[:120])}</a>")
    return "\n".join(lines)


def export_csv(conn, d):
    migrate(conn)
    d = Path(d); d.mkdir(parents=True, exist_ok=True)
    for t in ["darpa_programs", "darpa_orgs", "darpa_program_orgs", "darpa_personnel", "darpa_lead_check"]:
        cur = conn.execute(f"select * from {t}")
        with open(d / f"{t}.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh); w.writerow([c[0] for c in cur.description]); w.writerows(cur.fetchall())


STATUS_RU = {"active": "действует", "completed": "завершена", "unknown": "статус не установлен"}
LIST_RU = {"listed": "торгуется на бирже", "private": "частная", "acquired": "поглощена / входит в группу", "closed": "закрыта", "unknown": "не установлено"}


def md_link(u):
    return f"[{u}]({u})" if u else "—"


README_T25U = [
 "## Слепые зоны реестра: поля и скрипты (11.11.2026)", "",
 "Это **рабочий** реестр. Пустая ячейка значит «открытого источника на дату проверки нет», а не «нет связи». "
 "Непроверенные утверждения и вводные списки остаются в `LEAD_CHECK.md` с вердиктом «не подтверждено» и в основные таблицы не вносятся. "
 "Рабочие списки скриптов (`data/*.md`) — кандидаты для ручной проверки, не перепись и не факты реестра; в `darpa_orgs.csv` из них ничего не вносится автоматически.", "",
 "### Новые колонки", "",
 "| Таблица | Колонка | Правило |", "|---|---|---|",
 "| `darpa_orgs.csv` | `successor_entity`, `successor_source` | правопреемник / материнская группа — только со страницей источника |",
 "| `darpa_orgs.csv` | `acquisition_date`, `acquisition_source`, `acquisition_note` | дата закрытия сделки — только если открытый источник её прямо называет; иначе пусто и причина в `acquisition_note` |",
 "| `darpa_orgs.csv`, `darpa_program_orgs.csv` | `entity_type` (+ `entity_type_source` в orgs) | словарь: `prime`, `company`, `corporate_division`, `FFRDC`, `UARC`, `university`, `university_spinout`, `nonprofit_research`, `other`; пусто — не классифицировано |",
 "| `darpa_programs.csv` | `adversarial_mirror`, `mirror_country`, `mirror_source` | заполняется только при источнике, прямо описывающем программу-аналог; предложения без источника — в `LEAD_CHECK.md` |",
 "| `darpa_personnel.csv` | `red_flag`, `red_flag_source` | только с источником; кандидаты из `revolving_door.py` сюда не переносятся автоматически |", "",
 "`entity_type`: `FFRDC` — только по Master Government List of FFRDCs (NSF NCSES, https://www.nsf.gov/statistics/ffrdclist/); "
 "`university_spinout` — только при прямой формулировке источника; `prime` — только организации, которые `companies.csv` относит к Tier 1.", "",
 "### Мониторинг правопреемника", "",
 "Агрегатор продолжает искать старое название организации (`ORG_RX` в `darpa.py`). Если у организации заполнен `successor_entity`, "
 "`darpa.py tag` дополнительно размечает материал старым `org_id`, когда в тексте одновременно названы правопреемник (`SUCCESSOR_RX` в `darpa_data.py`) "
 "и сильный шаблон программы, с которой старая организация связана в `darpa_program_orgs.csv` (в `matched` — `successor:<org_id>`). "
 "Для организаций без связи с программой связка не работает (нет проверенных терминов технологии).", "",
 "### Скрипты (`scripts/`, только стандартная библиотека Python)", "",
 "- `sam_subawards.py` — головные контракты и субподряды по исполнителям реестра из открытого API USAspending.gov (агентство DARPA) → `data/sam_subawards.csv`, `data/sam_subawards.md` (рабочий список субподрядчиков, которых нет в `darpa_orgs.csv`).",
 "- `revolving_door.py` — перекрёстная проверка `darpa_personnel.csv` с официальными данными SEC EDGAR (инсайдерские отчёты Forms 3/4/5 и списки должностных лиц компаний с листингом) → `data/revolving_door.md`. LinkedIn не используется.",
 "- `proxy_detector.py` — для компаний с листингом берёт Exhibit 21 («Subsidiaries of the Registrant») из последнего 10-K в SEC EDGAR и сравнивает дочерние структуры с названиями в `data/darpa_item_tags.json` → `data/potential_shells.md` / `.csv`.",
 "- Для запросов к SEC нужна переменная `SEC_EDGAR_USER_AGENT` (описательный User-Agent с контактом); без неё скрипты работают только в режиме `--dry-run`.", "",
]


def repo(conn, out):
    out = Path(out); (out / "programs").mkdir(parents=True, exist_ok=True)
    progs = conn.execute("select * from darpa_programs where kind != 'support' order by id").fetchall()
    cols = [c[0] for c in conn.execute("select * from darpa_programs limit 0").description]
    orgs = {r[0]: r for r in conn.execute("select * from darpa_orgs")}
    po = conn.execute("select * from darpa_program_orgs").fetchall()
    pers = conn.execute("select * from darpa_personnel").fetchall()
    tags = conn.execute("select url, title, published_at, program_ids, db, org_ids from darpa_item_tags order by published_at desc").fetchall()
    idx = []
    for row in progs:
        p = dict(zip(cols, row)); pid = p["id"]
        pd = out / "programs" / pid; pd.mkdir(exist_ok=True)
        L = [f"# {p['short']} — {p['official_name']}", "",
             "Единица сбора и анализа рабочего реестра darpa-programs. Только проверенные факты с URL источника.", "",
             "## Карточка", "", "| Поле | Значение |", "|---|---|",
             f"| Тип | {p['kind']} |", f"| Страница darpa.mil | {md_link(p['darpa_url']) if p['darpa_url'] else 'не найдена на darpa.mil (проверено ' + DD.AS_OF + ')'} |",
             f"| Офис DARPA | {p['office'] or 'не установлен'} |", f"| Статус | {STATUS_RU.get(p['status'], p['status'])} |",
             f"| Период | {p['period'] or 'не установлен'} |", f"| Дата проверки | {p['as_of']} |", ""]
        if p["purpose"]:
            L += ["## Назначение (цитата DARPA)", "", f"> {p['purpose']}", "", f"Источник: {md_link(p['purpose_src'])}", ""]
        else:
            L += ["## Назначение", "", f"Официального текста DARPA в проверке нет. Источник сведений о программе: {md_link(p['purpose_src'])}", ""]
        L += ["## Организации", "", "| Организация | Роль | Листинг | Доказательство | Дата | Примечание |", "|---|---|---|---|---|---|"]
        rows_o = [x for x in po if x[0] == pid]
        for x in rows_o:
            o = orgs.get(x[1]); lst = (LIST_RU.get(o[2], o[2]) + (f", {o[3]} ({o[4]})" if o[3] else "") + (f"; {o[5]}" if o[5] else "")) if o else ""
            L.append(f"| {o[1] if o else x[1]} | {x[2]} | {lst} | {md_link(x[3])} | {x[4] or ''} | {x[5] or ''} |")
        if not rows_o:
            L.append("| — | — | — | — | — | организации не подтверждены |")
        L += ["", "## Персоналии", "", "| Имя | Роль | Организация | Доказательство | Примечание |", "|---|---|---|---|---|"]
        rp = [x for x in pers if x[3] == pid]
        for x in rp:
            L.append(f"| {x[0]} | {x[1]} | {orgs[x[2]][1] if x[2] in orgs else ''} | {md_link(x[4])} | {x[5] or ''} |")
        if not rp:
            L.append("| — | — | — | — | не подтверждены |")
        news = [t for t in tags if pid in json.loads(t[3])]
        L += ["", f"## Новости из хранилища ({len(news)})", "",
              "Совпадение по названию программы в тексте (правило — `../../ADD_PROGRAM.md`). Машиночитаемо: `../../data/darpa_item_tags.json`. Хранилище: live — `news.sqlite`, archive — `archive/news_archive.sqlite`.", ""]
        for t in news:
            L.append(f"- {(t[2] or '')[:10]} [{(t[1] or '').replace('|', '/').replace('[', '(').replace(']', ')')[:140]}]({t[0]}) — {t[4]}")
        if not news:
            L.append("Совпадений нет.")
        (pd / "README.md").write_text("\n".join(L) + "\n", encoding="utf-8")
        idx.append(f"| [{p['short']}](programs/{pid}/README.md) | {p['official_name']} | {p['office'] or '—'} | {STATUS_RU.get(p['status'], p['status'])} | {len(rows_o)} | {len(news)} |")
    n_list = {}
    for o in orgs.values():
        n_list[o[2]] = n_list.get(o[2], 0) + 1
    R = ["# darpa-programs — рабочий реестр программ DARPA", "",
         "**Рабочий реестр, не перепись всех программ DARPA.** Реестр растёт по мере появления программ в новостях агрегатора cbr-srv-big.",
         "", f"Дата проверки: {DD.AS_OF}. Источник истины — `darpa_data.py` в проекте агрегатора (копия в `scripts/`, таблицы — `data/`).", "",
         "Правило: каждая строка имеет URL источника. Заявления из вводного списка, которые не подтверждены, записаны в `LEAD_CHECK.md` как «не подтверждено» и в таблицы не внесены.", "",
         "## Как устроен «отдельный проект на программу»", "",
         "Каждая программа — каталог `programs/<slug>/`: `README.md` (карточка, организации, листинг, персоналии, все совпадения из хранилища новостей). Добавление новой программы — `ADD_PROGRAM.md`.", "",
         f"## Программы ({len(progs)})", "", "| Программа | Полное название | Офис | Статус | Организаций | Новостей |", "|---|---|---|---|---|---|", *idx, "",
         "## Листинг организаций", "", *[f"- {LIST_RU.get(k, k)}: {v}" for k, v in sorted(n_list.items())], "",
         "Таблицы: `data/darpa_item_tags.json` (разметка новостей), `data/darpa_orgs.csv` (листинг, тикер, биржа, источник), `data/darpa_program_orgs.csv`, `data/darpa_personnel.csv`, `data/darpa_programs.csv`, `data/darpa_lead_check.csv`.", "",
         *README_T25U]
    (out / "README.md").write_text("\n".join(R), encoding="utf-8")
    un = [t for t in tags if not json.loads(t[3])]
    U = ["# Материалы с DARPA без названной программы", "",
         "Кандидаты на новую программу (правило — `ADD_PROGRAM.md`). Программа не назначается без названия в тексте.", ""]
    U += [f"- {(t[2] or '')[:10]} [{(t[1] or '').replace('|', '/')[:140]}]({t[0]}) — {t[4]}" for t in un]
    (out / "UNASSIGNED.md").write_text("\n".join(U) + "\n", encoding="utf-8")
    lc = conn.execute("select claim, verdict, detail, source from darpa_lead_check").fetchall()
    LC = ["# Проверка вводного списка (сообщение GREEN, 11.11.2026)", "", "Вводный список — перечень для проверки, не источник.", "",
          "| Утверждение | Вердикт | Что установлено | Источник |", "|---|---|---|---|"]
    LC += [f"| {c[0]} | {c[1]} | {c[2] or ''} | {md_link(c[3])} |" for c in lc]
    (out / "LEAD_CHECK.md").write_text("\n".join(LC) + "\n", encoding="utf-8")
    export_csv(conn, out / "data")
    (out / "data" / "darpa_item_tags.json").write_text(json.dumps(
        [{"url": t[0], "title": t[1], "published_at": t[2], "program_ids": json.loads(t[3]), "org_ids": json.loads(t[5] or "[]"), "db": t[4]} for t in tags],
        ensure_ascii=False, indent=1), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["seed", "tag", "export", "repo", "block", "all", "bot-recent"])
    ap.add_argument("--csv-dir", default="export/darpa")
    ap.add_argument("--out", default="/tmp/darpa-programs")
    ap.add_argument("--since"); ap.add_argument("--until")
    ap.add_argument("--at", help="moment for bot-recent, ISO Europe/Minsk")
    a = ap.parse_args()
    conn = connect()
    if a.cmd in ("seed", "all"):
        seed(conn)
    if a.cmd in ("tag", "all"):
        print(json.dumps(tag(conn)))
    if a.cmd in ("export", "all"):
        export_csv(conn, a.csv_dir)
    if a.cmd in ("repo", "all"):
        repo(conn, a.out)
    if a.cmd == "block":
        print(digest_block(conn, a.since, a.until))
    if a.cmd == "bot-recent":
        ts = datetime.fromisoformat(a.at) if a.at else None
        print(format_bot_recent_audit(conn, ts))


if __name__ == "__main__":
    main()
