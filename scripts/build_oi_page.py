#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Строит публичное пояснение ОИ 5×5: OI_5x5.md и oi-5x5/index.html (t50u, 12.11.2026).

Шкалы и правила копируются из методики OI_5x5.md без изменений (разделы 1, 3, 4, 5 и абзац о Europol).
Цвет — представление уже присвоенного кода; палитра — PALETTE из public_export.py.
Нужен пакет `markdown` (только для HTML-страницы).
"""
import html, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from public_export import PALETTE, SOURCES, INFOS, status_of, PAGES, badge  # noqa: E402

if len(sys.argv) < 2:
    sys.exit("usage: build_oi_page.py <методика OI_5x5.md> [каталог репозитория]")
METHOD = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE.parent
DATE = "12.11.2026"

SRC_NAME = {"А": "официальный первоисточник", "Б": "обычно надёжен", "В": "иногда надёжен",
            "Г": "обычно ненадёжен", "Д": "оценить нельзя"}
INFO_NAME = {"1": "точность не вызывает сомнений", "2": "сведения от первоисточника, одной цепочки",
             "3": "не от первоисточника, но согласуется с уже учтёнными материалами",
             "4": "оценить нельзя", "5": "сомнительно или противоречит уже подтверждённому"}
INFO_COLOR = {"1": "зелёный — подтверждено; статус «новость»",
              "2": "синий — одна цепочка; статус «утверждение» при источнике А, Б, В",
              "3": "жёлтый — согласуется, ещё не подтверждено; статус «слух»",
              "4": "серо-оранжевый — оценить нельзя; статус «слух»",
              "5": "красный — сомнительно / противоречит; статус «слух»"}

# Дополнение к методике — указание GREEN 12.11.2026 (t46u), дословно
INITIAL = ("**Первоначальная ОИ** — код на момент первой публикации (дата публикации элемента). Ставится только по тому, "
           "что было известно на эту дату: сам элемент, его источник и материалы базы с более ранней (или той же) датой "
           "публикации. Более поздние новости в эту оценку не входят.")
EVOLVED = ("**ОИ со временем** — дополняется, если позднее другие новости ссылаются на эту новость (в том числе не один раз) "
           "и подтверждают её содержание. Основание: ссылки на подтверждающие элементы (URL, источник, дата публикации, "
           "дата события если есть). Если более поздних ссылок/подтверждений нет, поле «ОИ со временем» остаётся пустым "
           "(не копировать Первоначальную ОИ — пусто значит «пересмотра ещё не было»).")
EVOLVED2 = ("Источник и сведения по-прежнему независимы. Подтверждение со временем обычно поднимает сведения "
            "(например 2→1 или 5→1), надёжность издателя само по себе не повышает.")


def sections(md: str):
    parts, cur, buf = {}, None, []
    for line in md.splitlines():
        m = re.match(r"^## (\d+)\. ", line)
        if m:
            if cur:
                parts[cur] = "\n".join(buf).strip()
            cur, buf = m.group(1), [line]
        elif cur:
            buf.append(line)
    if cur:
        parts[cur] = "\n".join(buf).strip()
    return parts


def demote(block: str) -> str:
    return re.sub(r"^## ", "### ", block, flags=re.M)


def cell(code, small=True):
    bg, fg = PALETTE[code]
    st = status_of(code)
    sub = f'<br><small>{st}</small>' if small else ""
    return (f'<td style="background:{bg};color:{fg};text-align:center;padding:.6em .4em;min-width:4.5em">'
            f'<b style="font-size:1.25em">{code}</b>{sub}</td>')


def matrix_html() -> str:
    head = "".join(f'<th style="padding:.4em;width:16%">сведения {i}<br><small>{INFO_NAME[i]}</small></th>' for i in INFOS)
    rows = []
    for s in SOURCES:
        rows.append(f'<tr><th style="padding:.4em;text-align:left">источник {s}<br><small>{SRC_NAME[s]}</small></th>'
                    + "".join(cell(s + i) for i in INFOS) + "</tr>")
    return ('<table class="oi-matrix" style="border-collapse:separate;border-spacing:3px;table-layout:fixed;width:100%">\n'
            f'<thead><tr><th></th>{head}</tr></thead>\n<tbody>\n' + "\n".join(rows) + "\n</tbody></table>")


def palette_md() -> str:
    L = ["| Код | Фон | Текст | Источник | Сведения | Статус | Назначение цвета |", "|---|---|---|---|---|---|---|"]
    for i in INFOS:
        for s in SOURCES:
            code = s + i
            bg, fg = PALETTE[code]
            L.append(f"| {badge(code)} | `{bg}` | `{fg}` | {s} — {SRC_NAME[s]} | {i} — {INFO_NAME[i]} | {status_of(code)} | "
                     f"сведения {i}: {INFO_COLOR[i]}; оттенок источника {s} |")
    return "\n".join(L)


def build_md(method: str) -> str:
    sec = sections(method)
    europol = next(l for l in method.splitlines() if l.startswith("У Europol"))
    return f"""# ОИ 5×5 — буквенно-цифровой и цветовой код

Пояснение к кодам ОИ 5×5 в этом репозитории. Дата: {DATE}, Europe/Minsk. Цветная матрица на отдельной странице: [{PAGES}/oi-5x5/]({PAGES}/oi-5x5/).

## Как читать код

- Код ОИ 5×5 — **буква и цифра**: буква — надёжность источника (А–Д), цифра — достоверность сведений (1–5). Это две независимые шкалы.
- Официальный источник не делает сведения подтверждёнными: официальное заявление без независимого подтверждения — сведения «2», статус «утверждение».
- Подтверждённая информация — **только сведения «1»**.
- **Цвет** — представление уже присвоенного кода, на расчёт кода не влияет. Основной цвет — по сведениям: 1 — зелёный, 2 — синий, 3 — жёлтый, 4 — серо-оранжевый, 5 — красный. Оттенок — по источнику: А темнее и насыщеннее, Д светлее и глуше. Д4 — серый, Д5 — тёмно-бордовый.
- У каждой новости два кода:
    - {INITIAL}
    - {EVOLVED}
    - {EVOLVED2}
- Статус по коду (расчёт `t46u-oi5x5-2`): сведения 1 — «новость»; сведения 2 при источнике А, Б, В — «утверждение»; Г2 и Д2 — «слух»; сведения 3, 4, 5 — «слух». Правило методики — таблица раздела 5 ниже.

## Матрица 5×5

Цвета видны на GitHub Pages ([{PAGES}/oi-5x5/]({PAGES}/oi-5x5/)); в просмотре файла на github.com цвет не отображается — коды и цвета перечислены в таблице «Палитра».

{matrix_html()}

## Палитра

{palette_md()}

## Где коды в репозитории

- [Актуальный отчёт](АКТУАЛЬНЫЙ_ОТЧЁТ.md) — у каждого материала Первоначальная ОИ и, если был пересмотр, ОИ со временем.
- [data/oi5x5/](data/oi5x5/README.md) — таблицы кодов ОИ 5×5 по новостям (без текста новостей) и связи новость–новость.
- Новые материалы живой базы, поступившие после прохода ОИ, остаются без кода до следующего прохода ОИ. Код для них не выдумывается.

## Шкалы и правила (из методики ОИ 5×5 без изменений)

{demote(sec["1"])}

{europol}

{demote(sec["3"])}

{demote(sec["4"])}

{demote(sec["5"])}
"""


def build_html(md_text: str) -> str:
    import markdown
    body = markdown.markdown(md_text, extensions=["tables"])
    body = body.replace('href="АКТУАЛЬНЫЙ_ОТЧЁТ.md"', 'href="../АКТУАЛЬНЫЙ_ОТЧЁТ.html"')
    body = body.replace('href="data/oi5x5/README.md"', 'href="https://github.com/SKB-BY/cbr-news-materials/tree/main/data/oi5x5"')
    return f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ОИ 5×5 — буквенно-цифровой и цветовой код | cbr-news-materials</title>
<style>
body{{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;max-width:1100px;margin:0 auto;padding:1.2em;line-height:1.5;color:#1b1b1b}}
table{{border-collapse:collapse;margin:1em 0}} th,td{{border:1px solid #ddd;padding:.35em .5em;vertical-align:top}}
table.oi-matrix th,table.oi-matrix td{{border:0}} table.oi-matrix{{font-size:1.02em}}
code{{background:#f3f3f3;padding:0 .25em;border-radius:3px}} small{{opacity:.85}}
a{{color:#0b57d0}} .back{{font-size:.95em}}
</style></head><body>
<p class="back"><a href="../">← Материалы CBR</a></p>
{body}
</body></html>
"""


def main():
    method = METHOD.read_text(encoding="utf-8")
    md = build_md(method)
    (OUT / "OI_5x5.md").write_text(md, encoding="utf-8")
    (OUT / "oi-5x5").mkdir(exist_ok=True)
    # на странице Pages ссылки на страницу матрицы с самой себя не нужны — оставляем как есть
    (OUT / "oi-5x5" / "index.html").write_text(build_html(md), encoding="utf-8")
    print("written", OUT / "OI_5x5.md", OUT / "oi-5x5" / "index.html")


if __name__ == "__main__":
    main()
