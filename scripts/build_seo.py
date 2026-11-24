#!/usr/bin/env python3
"""t199u: генерация SEO-файлов среза (robots, sitemap, RSS/Atom, 404, поиск,
текстовые версии карт/графа, IndexNow-ключ, _data/seo.json).

Запуск из public-export:
  python3 templates/scripts/build_seo.py STAGING TEMPLATES REPO

Пишет в STAGING. Не меняет тексты новостей. Источники iid_only не читает.
Контакты, телефоны и почты в разметку не попадают.
Время — Europe/Minsk.
"""
from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote, urljoin
from xml.sax.saxutils import escape as xml_esc

# каталог рядом со скриптом, и на сервере тот же модуль кладётся в templates/scripts/
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from pages_meta import SITE, SITE_NAME, AUTHOR, DEFAULT_DESC, PAGES
except ImportError:
    SITE = "https://skb-by.github.io/cbr-news-materials"
    SITE_NAME = "КОНТУР - I-OSINT BY"
    AUTHOR = "GREEN-CBR"
    DEFAULT_DESC = "Открытые новости «Контура»."
    PAGES = {}

MINSK = timezone(timedelta(hours=3), "Europe/Minsk")
REPORT_MD = "АКТУАЛЬНЫЙ_ОТЧЁТ.md"
REPORT_HTML = "АКТУАЛЬНЫЙ_ОТЧЁТ.html"
# Стабильный публичный ключ IndexNow (это не секрет: файл лежит в корне сайта).
INDEXNOW_KEY = hashlib.sha256(b"cbr-kontur-iosint-by-indexnow-t199u").hexdigest()[:32]

NAV = [
    ("Главная", ""),
    ("Актуальный отчёт", REPORT_HTML),
    ("ИИД-100", "iid/"),
    ("Таймлайн сюжетов", "iid/timeline/"),
    ("Новостная карта", "news-map/"),
    ("Карта реестра", "map/"),
    ("Граф связей", "graph/"),
    ("ОИ 5×5", "OI_5x5.html"),
    ("Источники сбора", "SOURCES.html"),
    ("Программы DARPA", "darpa-programs/"),
    ("Поиск", "search.html"),
]


def log(msg: str) -> None:
    print("t199u-seo: " + msg, flush=True)


def abs_url(path: str) -> str:
    path = path.lstrip("/")
    return SITE + "/" + path if path else SITE + "/"


def load_asof(staging: Path, repo: Path) -> dict:
    for p in (staging / "_data" / "asof.json", repo / "_data" / "asof.json",
              staging / "manifest.json"):
        if p.exists():
            try:
                d = json.loads(p.read_text(encoding="utf-8"))
                if d.get("as_of") or d.get("as_of_label"):
                    if "as_of" not in d and "as_of_label" in d:
                        d["as_of"] = d["as_of_label"]
                    return d
            except Exception:
                continue
    return {"as_of": "", "oi_as_of": "", "tz": "Europe/Minsk"}


def parse_as_of(s: str) -> datetime | None:
    s = (s or "").strip()
    if not s:
        return None
    s = s.replace(" Europe/Minsk", "").replace(" - ", " ")
    for fmt in ("%d.%m.%Y %H:%M", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S"):
        try:
            d = datetime.strptime(s[:19] if "T" in fmt and "%z" not in fmt else s, fmt)
            return d.replace(tzinfo=MINSK) if d.tzinfo is None else d
        except Exception:
            continue
    return None


def lastmod_iso(as_of: str) -> str:
    d = parse_as_of(as_of) or datetime.now(MINSK)
    return d.astimezone(MINSK).strftime("%Y-%m-%dT%H:%M:%S+03:00")


def rfc822(as_of: str) -> str:
    d = parse_as_of(as_of) or datetime.now(MINSK)
    # RSS pubDate: RFC 822, с зоной +0300
    return d.astimezone(MINSK).strftime("%a, %d %b %Y %H:%M:%S +0300")


def desc_of(path: str, as_of: str) -> str:
    meta = PAGES.get(path, {})
    d = meta.get("desc") or DEFAULT_DESC
    return d.format(as_of=as_of or "—")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def robots_txt() -> str:
    return (
        "# Контур - I-OSINT BY. Разрешена индексация всех опубликованных страниц.\n"
        "# Поисковики читают robots.txt у корня хоста.\n"
        "# Сейчас сайт — проектный путь GitHub Pages, поэтому управляющий файл —\n"
        "# https://skb-by.github.io/robots.txt (репозиторий SKB-BY.github.io или свой домен).\n"
        "# Этот файл задаёт политику для своего домена и указывает sitemap уже сейчас.\n"
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {SITE}/sitemap.xml\n"
    )


def collect_sitemap_paths(staging: Path, repo: Path, as_of: str) -> list[tuple[str, str, str]]:
    """(loc_path, lastmod, changefreq) — только существующие публичные HTML-страницы."""
    roots = [staging, repo]
    lm = lastmod_iso(as_of)
    out: list[tuple[str, str, str]] = []

    def exists(rel: str) -> bool:
        for root in roots:
            p = root / rel
            if p.exists():
                return True
            # Jekyll: .md → .html
            if rel.endswith(".html"):
                md = root / (rel[:-5] + ".md")
                if md.exists():
                    return True
            if rel.endswith("/") and (root / rel / "index.html").exists():
                return True
        return False

    core = [
        ("", "daily"),
        (REPORT_HTML, "hourly"),
        ("iid/", "daily"),
        ("iid/timeline/", "daily"),
        ("iid/timeline/text.html", "daily"),
        ("news-map/", "daily"),
        ("news-map/text.html", "daily"),
        ("map/", "weekly"),
        ("map/text.html", "weekly"),
        ("graph/", "weekly"),
        ("graph/text.html", "weekly"),
        ("OI_5x5.html", "monthly"),
        ("oi-5x5/", "monthly"),
        ("data/oi5x5/", "daily"),
        ("data/mention_gap.html", "daily"),
        ("SOURCES.html", "weekly"),
        ("INGEST_LOG.html", "weekly"),
        ("darpa-programs/", "weekly"),
        ("search.html", "daily"),
        ("rss.xml", "hourly"),
    ]
    for path, freq in core:
        if path in ("", "search.html", "rss.xml") or exists(path) or path.endswith("text.html"):
            # text.html и search/rss мы сами пишем в staging
            out.append((path, lm, freq))

    # программы DARPA (HTML-страницы каталога)
    seen = {p for p, _, _ in out}
    for root in roots:
        prog = root / "darpa-programs" / "programs"
        if not prog.is_dir():
            continue
        for d in sorted(prog.iterdir()):
            if d.is_dir() and ((d / "index.html").exists() or (d / "README.md").exists() or True):
                # включаем каталог, если есть любая страница или это известный slug
                rel = f"darpa-programs/programs/{d.name}/"
                if rel not in seen and (d / "index.html").exists():
                    out.append((rel, lm, "monthly"))
                    seen.add(rel)
        break
    return out


def sitemap_xml(entries: list[tuple[str, str, str]]) -> str:
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, lm, freq in entries:
        loc = abs_url(path)
        # в sitemap допустим UTF-8, но пробелы/кириллицу надёжнее кодировать поэлементно
        loc = quote(loc, safe=":/")
        pri = "1.0" if path == "" else ("0.9" if path == REPORT_HTML else ("0.7" if freq in ("hourly", "daily") else "0.5"))
        parts += [
            "  <url>",
            f"    <loc>{xml_esc(loc)}</loc>",
            f"    <lastmod>{xml_esc(lm)}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{pri}</priority>",
            "  </url>",
        ]
    parts.append("</urlset>\n")
    return "\n".join(parts)


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def extract_day_items(md: str) -> list[str]:
    """Пункты «Главное за сутки» — и нумерованный список, и строки ленты."""
    m = re.search(
        r'id="b-glavnoe".*?</summary>\s*(.*?)(?:\n</details>|\n<details class="cbr-block")',
        md,
        flags=re.S,
    )
    if not m:
        return []
    body = m.group(1)
    items = []
    for raw in re.findall(r"<li>([\s\S]*?)</li>", body, flags=re.I):
        t = strip_tags(raw)
        if t:
            items.append(t)
    if not items:
        for raw in re.findall(r"^\s*(?:\d+\.|-|\*)\s+(.+)$", body, flags=re.M):
            t = strip_tags(raw)
            if t:
                items.append(t)
    # уникальные, порядок сохраняем
    seen, out = set(), []
    for t in items:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def extract_news_bullets(md: str, limit: int = 40) -> list[tuple[str, str]]:
    """Пары (дата, заголовок) из пунктов ленты отчёта."""
    out = []
    for m in re.finditer(r"^- (\d\d\.\d\d\.\d{4}) — (.+?)(?=\n- |\n\*\*|\n</details>|\n<details|\Z)", md, flags=re.S | re.M):
        title = strip_tags(m.group(2))
        # обрезаем на первой точке с кодом ОИ / длинным хвостом — оставляем разумный заголовок
        title = re.split(r"\s+[—–-]\s+«", title, maxsplit=1)[0].strip()
        title = re.sub(r"\s+", " ", title)
        if len(title) > 240:
            title = title[:237] + "…"
        if title:
            out.append((m.group(1), title))
        if len(out) >= limit:
            break
    return out


def rss_and_atom(as_of: str, day_items: list[str], bullets: list[tuple[str, str]]) -> tuple[str, str]:
    link_report = abs_url(REPORT_HTML)
    pub = rfc822(as_of)
    updated = lastmod_iso(as_of)
    items = []
    for i, t in enumerate(day_items):
        items.append(("Главное за сутки: " + t, t, f"{link_report}#b-glavnoe", f"day-{i}-{hashlib.sha1(t.encode()).hexdigest()[:12]}", pub, updated))
    if not items:
        for d, t in bullets[:15]:
            items.append((t, t, link_report, f"news-{d}-{hashlib.sha1(t.encode()).hexdigest()[:12]}", pub, updated))
    # RSS
    ch = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
        "<channel>",
        f"<title>{xml_esc(SITE_NAME)} — актуальный отчёт</title>",
        f"<link>{xml_esc(link_report)}</link>",
        f"<description>{xml_esc('Лента актуального отчёта «Контура»: главное за сутки и новые пункты. Срез ' + (as_of or '—') + ' Europe/Minsk.')}</description>",
        "<language>ru</language>",
        f"<lastBuildDate>{xml_esc(pub)}</lastBuildDate>",
        f"<copyright>{xml_esc('© 2026 ' + AUTHOR + '. Новости — собственность их источников.')}</copyright>",
        f'<atom:link href="{xml_esc(SITE + "/rss.xml")}" rel="self" type="application/rss+xml"/>',
        f"<managingEditor></managingEditor>".replace("<managingEditor></managingEditor>", ""),  # не оставляем пустой тег с почтой
    ]
    # убрать пустую строку от managingEditor
    ch = [x for x in ch if x != ""]
    for title, desc, link, guid, pubd, _ in items:
        ch += [
            "<item>",
            f"<title>{xml_esc(title)}</title>",
            f"<link>{xml_esc(link)}</link>",
            f"<guid isPermaLink=\"false\">{xml_esc(guid)}</guid>",
            f"<pubDate>{xml_esc(pubd)}</pubDate>",
            f"<description>{xml_esc(desc)}</description>",
            "</item>",
        ]
    ch += ["</channel>", "</rss>\n"]
    rss = "\n".join(ch)
    at = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<feed xmlns="http://www.w3.org/2005/Atom">',
        f"<title>{xml_esc(SITE_NAME)} — актуальный отчёт</title>",
        f'<link href="{xml_esc(link_report)}"/>',
        f'<link rel="self" href="{xml_esc(SITE + "/atom.xml")}"/>',
        f"<id>{xml_esc(link_report)}</id>",
        f"<updated>{xml_esc(updated)}</updated>",
        f"<author><name>{xml_esc(AUTHOR)}</name></author>",
        f"<subtitle>{xml_esc('Лента актуального отчёта «Контура». Срез ' + (as_of or '—') + ' Europe/Minsk.')}</subtitle>",
        f"<rights>{xml_esc('© 2026 ' + AUTHOR + '. Новости — собственность их источников.')}</rights>",
    ]
    for title, desc, link, guid, _pubd, upd in items:
        at += [
            "<entry>",
            f"<title>{xml_esc(title)}</title>",
            f'<link href="{xml_esc(link)}"/>',
            f"<id>tag:skb-by.github.io,2026:{xml_esc(guid)}</id>",
            f"<updated>{xml_esc(upd)}</updated>",
            f"<summary>{xml_esc(desc)}</summary>",
            "</entry>",
        ]
    at += ["</feed>\n"]
    return rss, "\n".join(at)


def chrome(title: str, desc: str, canonical: str, as_of: str, body: str, crumbs: str = "",
           robots: str = "index,follow", extra_head: str = "", depth: int = 0) -> str:
    prefix = "../" * depth
    if not prefix:
        prefix = "./"
        # для корня удобнее абсолютный baseurl-путь
        prefix = "/cbr-news-materials/"
        home = prefix
        css = prefix + "assets/cbr-ops.css"
        og = prefix + "assets/og.png"
        fav_svg = prefix + "assets/favicon.svg"
        fav_ico = prefix + "assets/favicon.ico"
        apple = prefix + "assets/apple-touch-icon.png"
        asof_js = prefix + "assets/asof.js"
        rss = prefix + "rss.xml"
        atom = prefix + "atom.xml"
    else:
        home = prefix
        css = prefix + "assets/cbr-ops.css"
        og = SITE + "/assets/og.png"
        fav_svg = prefix + "assets/favicon.svg"
        fav_ico = prefix + "assets/favicon.ico"
        apple = prefix + "assets/apple-touch-icon.png"
        asof_js = prefix + "assets/asof.js"
        rss = prefix + "rss.xml"
        atom = prefix + "atom.xml"
        if depth > 0:
            og = SITE + "/assets/og.png"
            rss = SITE + "/rss.xml"
            atom = SITE + "/atom.xml"

    nav = []
    for name, path in NAV:
        href = (prefix + path) if not path.startswith("http") else path
        if prefix == "/cbr-news-materials/":
            href = prefix + path
        nav.append(f'<a href="{html.escape(href)}">{html.escape(name)}</a>')
    ld = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canonical,
        "inLanguage": "ru",
        "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": SITE + "/"},
        "author": {"@type": "Organization", "name": AUTHOR, "alternateName": SITE_NAME},
    }
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="author" content="{html.escape(AUTHOR)}">
<meta name="copyright" content="© 2026 {html.escape(AUTHOR)}. Все права защищены.">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="{html.escape(robots)}">
<link rel="canonical" href="{html.escape(canonical)}">
<link rel="alternate" hreflang="ru" href="{html.escape(canonical)}">
<link rel="alternate" hreflang="x-default" href="{html.escape(canonical)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ru_RU">
<meta property="og:site_name" content="{html.escape(SITE_NAME)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{html.escape(canonical)}">
<meta property="og:image" content="{html.escape(SITE + '/assets/og.png')}">
<meta property="og:image:alt" content="{html.escape(SITE_NAME)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{html.escape(SITE + '/assets/og.png')}">
<link rel="icon" href="{html.escape(fav_svg)}" type="image/svg+xml">
<link rel="icon" href="{html.escape(fav_ico)}" sizes="any">
<link rel="apple-touch-icon" href="{html.escape(apple)}">
<link rel="alternate" type="application/rss+xml" title="{html.escape(SITE_NAME)} — лента актуального отчёта" href="{html.escape(SITE + '/rss.xml')}">
<link rel="alternate" type="application/atom+xml" title="{html.escape(SITE_NAME)} — лента Atom" href="{html.escape(SITE + '/atom.xml')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{html.escape(css)}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{extra_head}
</head>
<body>
<header class="cbr-bar">
  <a class="cbr-mark" href="{html.escape(home)}"><b class="cbr-logo" tabindex="0">CBR</b><span>{html.escape(SITE_NAME)}</span></a>
  <nav class="cbr-nav">
    {''.join(nav)}
  </nav>
  <span class="cbr-asof" id="cbr-asof"><span class="cbr-last">последнее обновление <b>{html.escape(as_of or '—')} Europe/Minsk</b></span></span>
</header>
<main class="cbr-doc">
{crumbs}
{body}
</main>
<footer class="cbr-foot">{html.escape(SITE_NAME)} · сведения на {html.escape(as_of or '—')} Europe/Minsk · <a href="https://github.com/SKB-BY/cbr-news-materials">репозиторий</a><br>© 2026 {html.escape(AUTHOR)}. Все права защищены. Разработчик — {html.escape(AUTHOR)}. · новости — собственность их источников</footer>
<script src="{html.escape(asof_js)}"></script>
</body>
</html>
"""


def page_404(as_of: str) -> str:
    body = f"""<h1>Страница не найдена</h1>
<p>Такой страницы в «Контуре» нет. Перейдите в один из разделов:</p>
<ul>
{chr(10).join(f'<li><a href="/cbr-news-materials/{html.escape(p)}">{html.escape(n)}</a></li>' for n,p in NAV)}
</ul>
<p>Либо откройте <a href="/cbr-news-materials/search.html">поиск</a> или <a href="/cbr-news-materials/sitemap.xml">карту сайта</a>.</p>
"""
    return chrome(PAGES["404.html"]["title"], PAGES["404.html"]["desc"], abs_url("404.html"),
                  as_of, body, robots="noindex,follow")


def page_search(as_of: str, index: list[dict]) -> str:
    # компактный индекс встраиваем, чтобы страница работала и без отдельного json
    payload = json.dumps(index, ensure_ascii=False)
    body = f"""<h1>Поиск по разделам «Контура»</h1>
<p>Ищется подстрока в названии страницы, заголовке материала, имени организации или программы. Данные — из этой выгрузки{(' на ' + html.escape(as_of) + ' Europe/Minsk') if as_of else ''}.</p>
<form id="f" method="get" action="search.html" role="search">
  <label for="q">Запрос (не короче 2 знаков)</label><br>
  <input type="search" id="q" name="q" minlength="2" required style="width:min(100%,36rem);padding:6px 8px;margin:8px 0">
  <button type="submit">Найти</button>
</form>
<p id="status"></p>
<ol id="res"></ol>
<noscript>
<p>Без JavaScript откройте <a href="АКТУАЛЬНЫЙ_ОТЧЁТ.html">актуальный отчёт</a>, <a href="sitemap.xml">карту сайта</a>
или текстовые версии <a href="news-map/text.html">новостной карты</a>, <a href="map/text.html">карты реестра</a>
и <a href="graph/text.html">графа связей</a>.</p>
</noscript>
<script>
var IDX = {payload};
(function(){{
  var q = new URLSearchParams(location.search).get("q") || "";
  var inp = document.getElementById("q");
  inp.value = q;
  var st = document.getElementById("status");
  var box = document.getElementById("res");
  if (q.trim().length < 2) {{ st.textContent = "Введите не меньше двух знаков."; return; }}
  var nq = q.trim().toLowerCase();
  var hits = [];
  for (var i=0;i<IDX.length;i++){{
    var it = IDX[i];
    var hay = ((it.t||"")+" "+(it.s||"")+" "+(it.g||"")).toLowerCase();
    if (hay.indexOf(nq) >= 0) hits.push(it);
    if (hits.length >= 200) break;
  }}
  st.textContent = "Найдено: " + hits.length + (hits.length>=200 ? " (показаны первые 200)" : "") + " по запросу «" + q.replace(/[<>]/g,"") + "».";
  box.innerHTML = hits.map(function(it){{
    var g = it.g ? '<span class="muted"> — ' + it.g.replace(/[<>]/g,"") + '</span>' : "";
    return '<li><a href="'+it.u+'">'+ (it.t||it.u).replace(/[<>]/g,"") +'</a>'+g+'</li>';
  }}).join("");
}})();
</script>
"""
    extra = """<script type="application/ld+json">%s</script>""" % json.dumps({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "url": SITE + "/",
        "inLanguage": "ru",
        "publisher": {"@type": "Organization", "name": AUTHOR, "alternateName": SITE_NAME},
        "potentialAction": {
            "@type": "SearchAction",
            "target": SITE + "/search.html?q={search_term_string}",
            "query-input": "required name=search_term_string",
        },
    }, ensure_ascii=False)
    return chrome(PAGES["search.html"]["title"], PAGES["search.html"]["desc"],
                  abs_url("search.html"), as_of, body, extra_head=extra)


def first_existing(*paths: Path) -> Path | None:
    for p in paths:
        if p and p.exists():
            return p
    return None


def text_news_map(staging: Path, repo: Path, as_of: str) -> tuple[str, int]:
    p = first_existing(staging / "news-map" / "news_points.csv", repo / "news-map" / "news_points.csv")
    rows = []
    if p:
        with p.open(encoding="utf-8", errors="replace", newline="") as f:
            r = csv.DictReader(f)
            seen = set()
            for row in r:
                uid = (row.get("id") or row.get("url") or "").strip()
                title = (row.get("title_ru") or "").strip()
                if not title or uid in seen:
                    continue
                seen.add(uid)
                rows.append(row)
    # группировка по месту
    by: dict[str, list] = {}
    for row in rows:
        place = (row.get("place") or "Без места").strip() or "Без места"
        by.setdefault(place, []).append(row)
    parts = [
        "<h1>Новостная карта — текстовая версия</h1>",
        "<p>Тот же состав сведений, что на <a href=\"./\" >интерактивной Новостной карте</a>, списком по местам. "
        "Интерактивная карта рисует область, а не точку: точный адрес события в новости, как правило, не назван. "
        f"Срез {html.escape(as_of or '—')} Europe/Minsk. Материалов: {len(rows)}.</p>",
    ]
    for place in sorted(by, key=lambda x: (-len(by[x]), x.lower())):
        items = by[place]
        parts.append(f"<h2>{html.escape(place)} <small>({len(items)})</small></h2>")
        parts.append("<ul>")
        # свежие сверху, если есть дата
        items = sorted(items, key=lambda r: r.get("published_at_minsk") or r.get("event_date") or "", reverse=True)
        for row in items[:400]:
            title = html.escape(row.get("title_ru") or "")
            url = row.get("url") or ""
            dt = html.escape((row.get("published_at_minsk") or row.get("event_date") or "")[:16])
            oi = html.escape(row.get("oi_evolved") or row.get("oi_initial") or "")
            src = html.escape(row.get("source") or "")
            meta = " · ".join(x for x in (dt, src, ("ОИ " + oi) if oi else "") if x)
            if url.startswith("http"):
                parts.append(f'<li>{title} — {html.escape(meta)} — <a href="{html.escape(url)}" rel="nofollow noopener">источник</a></li>')
            else:
                parts.append(f"<li>{title} — {html.escape(meta)}</li>")
        if len(items) > 400:
            parts.append(f"<li>… и ещё {len(items) - 400} в этом месте, см. интерактивную карту.</li>")
        parts.append("</ul>")
    return "\n".join(parts), len(rows)


def text_map(staging: Path, repo: Path, as_of: str) -> tuple[str, int]:
    p = first_existing(staging / "map" / "locations.csv", repo / "map" / "locations.csv",
                       staging / "companies.csv", repo / "companies.csv")
    rows = []
    if p and p.suffix == ".csv":
        with p.open(encoding="utf-8", errors="replace", newline="") as f:
            r = csv.DictReader(f)
            for row in r:
                name = (row.get("name") or row.get("Name") or row.get("организация") or "").strip()
                if name:
                    rows.append(row)
    parts = [
        "<h1>Карта реестра — текстовая версия</h1>",
        "<p>Организации и программы публичного реестра, тот же состав, что на <a href=\"./\" >интерактивной карте реестра</a>. "
        "Российских юрлиц в реестре нет. Юридический адрес не воспроизводится: это не точка события и не завод. "
        f"Срез {html.escape(as_of or '—')} Europe/Minsk. Записей: {len(rows)}.</p>",
        "<ul>",
    ]
    for row in sorted(rows, key=lambda r: (r.get("name") or "").lower()):
        name = html.escape(row.get("name") or "")
        kind = html.escape(row.get("kind") or "")
        url = (row.get("source_url") or row.get("url") or "").strip()
        extra = f" — {kind}" if kind else ""
        if url.startswith("http"):
            parts.append(f'<li>{name}{extra} — <a href="{html.escape(url)}" rel="nofollow noopener">официальная страница</a></li>')
        else:
            parts.append(f"<li>{name}{extra}</li>")
    parts.append("</ul>")
    return "\n".join(parts), len(rows)


def text_graph(staging: Path, repo: Path, as_of: str) -> tuple[str, int, int]:
    p = first_existing(staging / "graph" / "graph.json", repo / "graph" / "graph.json")
    nodes, edges = [], []
    if p:
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            nodes = data.get("nodes") or []
            edges = data.get("edges") or []
        except Exception:
            pass
    parts = [
        "<h1>Граф связей — текстовая версия</h1>",
        "<p>Узлы и связи публичного графа, тот же состав, что на <a href=\"./\" >интерактивном графе</a>. "
        "Только связи с основанием и URL источника; совместные упоминания не включены. "
        f"Срез {html.escape(as_of or '—')} Europe/Minsk. Узлов: {len(nodes)}, связей: {len(edges)}.</p>",
        "<h2>Узлы</h2><ul>",
    ]
    for n in sorted(nodes, key=lambda x: (x.get("label") or x.get("id") or "").lower()):
        lab = html.escape(n.get("label") or n.get("id") or "")
        kind = html.escape(n.get("kind") or "")
        country = html.escape(n.get("country") or "")
        url = (n.get("url") or n.get("page") or "").strip()
        bits = " · ".join(x for x in (kind, country) if x)
        extra = f" — {bits}" if bits else ""
        if url.startswith("http"):
            parts.append(f'<li>{lab}{extra} — <a href="{html.escape(url)}" rel="nofollow noopener">страница</a></li>')
        else:
            parts.append(f"<li>{lab}{extra}</li>")
    parts.append("</ul><h2>Связи</h2><ul>")
    # подписи узлов
    lab = {n.get("id"): (n.get("label") or n.get("id") or "") for n in nodes}
    shown = 0
    for e in edges:
        a = html.escape(lab.get(e.get("source") or e.get("from") or e.get("a"), e.get("source") or ""))
        b = html.escape(lab.get(e.get("target") or e.get("to") or e.get("b"), e.get("target") or ""))
        reason = html.escape(strip_tags(str(e.get("reason") or e.get("g") or e.get("label") or "связь")))
        url = (e.get("url") or e.get("source_url") or "").strip()
        if url.startswith("http"):
            parts.append(f'<li>{a} — {reason} — {b} — <a href="{html.escape(url)}" rel="nofollow noopener">основание</a></li>')
        else:
            parts.append(f"<li>{a} — {reason} — {b}</li>")
        shown += 1
    parts.append("</ul>")
    return "\n".join(parts), len(nodes), shown


def _timeline_public_stories(data) -> list:
    """Только публичные сюжеты: источники iid_only и метка «источник скрыт» не выводятся."""
    bags = []
    if isinstance(data, list):
        bags = data
    elif isinstance(data, dict):
        for key in ("stories", "news", "iid", "items", "timeline", "events"):
            v = data.get(key)
            if isinstance(v, list):
                bags.extend(v)
            elif isinstance(v, dict):
                bags.extend(v.values())
    out = []
    for st in bags:
        if not isinstance(st, dict):
            continue
        if st.get("iid_only") or st.get("io_name"):
            continue
        title = st.get("title") or st.get("name") or st.get("label") or st.get("head") or ""
        title = strip_tags(str(title))
        if not title or "источник скрыт" in title.lower() or "только для расчёта" in title.lower():
            continue
        out.append(st)
    return out


def text_timeline(staging: Path, repo: Path, as_of: str) -> tuple[str, int]:
    p = first_existing(staging / "iid" / "timeline" / "timeline_data.js",
                       repo / "iid" / "timeline" / "timeline_data.js")
    stories = []
    if p:
        raw = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"window\.CBR_TIMELINE\s*=\s*", raw)
        blob = raw[m.end():].strip() if m else raw
        if blob.endswith(";"):
            blob = blob[:-1]
        # запасной путь: первое большое JSON-тело
        if not m:
            mm = re.search(r"(\{[\s\S]+\})", raw)
            blob = mm.group(1) if mm else raw
        try:
            data = json.loads(blob)
        except Exception:
            data = {}
        stories = _timeline_public_stories(data)

    parts = [
        "<h1>Таймлайн сюжетов — текстовая версия</h1>",
        "<p>Сюжеты той же выгрузки, что на <a href=\"./\" >интерактивном таймлайне</a>. "
        "Сюжеты и материалы только для расчёта ИИД сюда не входят. "
        f"Срез {html.escape(as_of or '—')} Europe/Minsk. Сюжетов: {len(stories)}.</p>",
        "<ul>",
    ]
    n = 0
    for st in stories:
        title = st.get("title") or st.get("name") or st.get("label") or st.get("head") or ""
        title = strip_tags(str(title))
        status = st.get("status") or ""
        country = st.get("country") or st.get("place") or ""
        if isinstance(st.get("countries"), list):
            country = country or ", ".join(str(x) for x in st.get("countries") if x)
        sphere = st.get("sphere") or st.get("sp") or ""
        bits = " · ".join(html.escape(str(x)) for x in (status, sphere, country) if x)
        url = (st.get("url") or "").strip()
        if url.startswith("http"):
            parts.append(f"<li>{html.escape(title)}" + (f" — {bits}" if bits else "") +
                         f' — <a href="{html.escape(url)}" rel="nofollow noopener">источник</a></li>')
        else:
            parts.append(f"<li>{html.escape(title)}" + (f" — {bits}" if bits else "") + "</li>")
        n += 1
    parts.append("</ul>")
    return "\n".join(parts), n


def build_search_index(staging: Path, repo: Path, day_items: list[str],
                       n_news: int, n_org: int, n_nodes: int) -> list[dict]:
    idx = []
    for name, path in NAV:
        idx.append({"t": name, "u": abs_url(path), "g": "раздел"})
    for t in day_items:
        idx.append({"t": t, "u": abs_url(REPORT_HTML) + "#b-glavnoe", "g": "Главное за сутки"})
    # организации с карты реестра (имена)
    p = first_existing(staging / "map" / "locations.csv", repo / "map" / "locations.csv")
    if p:
        with p.open(encoding="utf-8", errors="replace", newline="") as f:
            for row in csv.DictReader(f):
                name = (row.get("name") or "").strip()
                if name:
                    idx.append({"t": name, "u": abs_url("map/text.html"), "g": row.get("kind") or "реестр"})
    p = first_existing(staging / "graph" / "graph.json", repo / "graph" / "graph.json")
    if p:
        try:
            nodes = json.loads(p.read_text(encoding="utf-8")).get("nodes") or []
        except Exception:
            nodes = []
        for n in nodes:
            lab = (n.get("label") or "").strip()
            if lab:
                nid = quote(str(n.get("id") or ""), safe="")
                idx.append({"t": lab, "u": abs_url("graph/") + "#node=" + nid, "g": n.get("kind") or "граф"})
    # программы DARPA — имена каталогов слишком технические; возьмём, если есть index title later
    return idx


def write_assets(staging: Path, templates: Path) -> int:
    src = templates / "assets"
    dst = staging / "assets"
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for name in ("og.png", "favicon.svg", "favicon.ico", "favicon-32.png", "apple-touch-icon.png"):
        s = src / name
        if s.exists():
            data = s.read_bytes()
            (dst / name).write_bytes(data)
            n += 1
    return n


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) < 1:
        print("usage: build_seo.py STAGING [TEMPLATES] [REPO]", file=sys.stderr)
        return 2
    staging = Path(argv[0])
    templates = Path(argv[1]) if len(argv) > 1 else staging
    repo = Path(argv[2]) if len(argv) > 2 else staging
    staging.mkdir(parents=True, exist_ok=True)

    asof = load_asof(staging, repo)
    as_of = (asof.get("as_of") or asof.get("as_of_label") or "").replace(" Europe/Minsk", "").strip()
    oi_as_of = (asof.get("oi_as_of") or "").replace(" Europe/Minsk", "").strip()

    md_path = first_existing(staging / REPORT_MD, repo / REPORT_MD)
    md = md_path.read_text(encoding="utf-8") if md_path else ""
    day_items = extract_day_items(md)
    bullets = extract_news_bullets(md)

    # robots, sitemap, rss, atom, indexnow
    write(staging / "robots.txt", robots_txt())
    entries = collect_sitemap_paths(staging, repo, as_of)
    write(staging / "sitemap.xml", sitemap_xml(entries))
    rss, atom = rss_and_atom(as_of, day_items, bullets)
    write(staging / "rss.xml", rss)
    write(staging / "atom.xml", atom)
    write(staging / f"{INDEXNOW_KEY}.txt", INDEXNOW_KEY + "\n")

    # текстовые версии
    body, n_news = text_news_map(staging, repo, as_of)
    write(staging / "news-map" / "text.html",
          chrome(PAGES["news-map/text.html"]["title"], desc_of("news-map/text.html", as_of),
                 abs_url("news-map/text.html"), as_of, body, depth=1))
    body, n_org = text_map(staging, repo, as_of)
    write(staging / "map" / "text.html",
          chrome(PAGES["map/text.html"]["title"], desc_of("map/text.html", as_of),
                 abs_url("map/text.html"), as_of, body, depth=1))
    body, n_nodes, n_edges = text_graph(staging, repo, as_of)
    write(staging / "graph" / "text.html",
          chrome(PAGES["graph/text.html"]["title"], desc_of("graph/text.html", as_of),
                 abs_url("graph/text.html"), as_of, body, depth=1))
    body, n_stories = text_timeline(staging, repo, as_of)
    write(staging / "iid" / "timeline" / "text.html",
          chrome(PAGES["iid/timeline/text.html"]["title"], desc_of("iid/timeline/text.html", as_of),
                 abs_url("iid/timeline/text.html"), as_of, body, depth=2))

    idx = build_search_index(staging, repo, day_items, n_news, n_org, n_nodes)
    write(staging / "search.html", page_search(as_of, idx))
    write(staging / "404.html", page_404(as_of))

    n_assets = write_assets(staging, templates)

    seo = {
        "as_of": as_of,
        "oi_as_of": oi_as_of,
        "tz": "Europe/Minsk",
        "indexnow_key": INDEXNOW_KEY,
        "indexnow_key_location": f"{SITE}/{INDEXNOW_KEY}.txt",
        "day_items": day_items,
        "sitemap_urls": len(entries),
        "search_index": len(idx),
        "news_text": n_news,
        "map_text": n_org,
        "graph_nodes": n_nodes,
        "graph_edges": n_edges,
        "timeline_stories": n_stories,
        "author": AUTHOR,
        "site": SITE_NAME,
    }
    (staging / "_data").mkdir(parents=True, exist_ok=True)
    write(staging / "_data" / "seo.json", json.dumps(seo, ensure_ascii=False, indent=2) + "\n")
    # пустые коды подтверждения кабинетов — GREEN подставит сам
    wm = first_existing(templates / "_data" / "webmaster.yml", repo / "_data" / "webmaster.yml")
    if wm and not (staging / "_data" / "webmaster.yml").exists():
        write(staging / "_data" / "webmaster.yml", wm.read_text(encoding="utf-8"))
    elif not (staging / "_data" / "webmaster.yml").exists():
        write(staging / "_data" / "webmaster.yml",
              "# Коды подтверждения кабинетов вебмастеров. Пустые, пока GREEN их не пришлёт.\n"
              "# Только публичные строки meta-тегов, без паролей и почт.\n"
              "google: \"\"\n"
              "yandex: \"\"\n"
              "bing: \"\"\n")

    log(
        f"ok as_of={as_of} sitemap={len(entries)} rss_items={len(day_items) or len(bullets[:15])} "
        f"search={len(idx)} news_text={n_news} map_text={n_org} graph={n_nodes}/{n_edges} "
        f"timeline={n_stories} assets={n_assets}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
