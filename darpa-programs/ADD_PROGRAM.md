# Добавление новой программы DARPA

Правило для агрегатора cbr-srv-big. Программа добавляется, когда её название появилось в собранных новостях или на darpa.mil.

## 1. Обнаружение

1. `python3 darpa.py tag` размечает материалы live и архива.
2. Материалы со строкой «DARPA без названной программы» (`program_ids = []` в `darpa_item_tags`) просматриваются при каждой сводке.
3. Кандидат — название программы (аббревиатура или полное название) в тексте такого материала.

## 2. Проверка

1. Найти страницу программы на darpa.mil: `https://www.darpa.mil/sitemap.xml`, путь `/research/programs/<slug>` или новость `/news/<год>/...`.
2. Записать с официальной страницы: полное название, аббревиатуру, офис, статус (`This program is now complete` → completed), руководителя программы, одну фразу назначения (цитата на английском).
3. Если страницы на darpa.mil нет: `darpa_url = ''`, `status = unknown`, источник — SAM.gov или релиз исполнителя. Это указывается в карточке.
4. Исполнители — только из darpa.mil или релиза самой компании, с датой.
5. Листинг компании — SEC `company_tickers_exchange.json` / EDGAR submissions (тикер, биржа, IPO-проспект 424B4). Поглощение или закрытие — 8-K, релиз покупателя. Тикер не угадывается.
6. «PM DARPA основал компанию» записывается только при прямой формулировке источника.

## 3. Внесение

1. Добавить строку в `PROGRAMS` в `darpa_data.py`: сильные шаблоны (полное название, уникальные обозначения вроде `XRQ-73`) и слабые (аббревиатура; срабатывает только при упоминании DARPA в тексте).
2. Добавить организации в `ORGS`, связи в `PROGRAM_ORGS`, людей в `PERSONNEL`.
3. Выполнить `python3 darpa.py all --out <клон darpa-programs>` — появится каталог `programs/<slug>/` с README (карточка и список новостей); разметка — в `data/darpa_item_tags.json`.
4. Закоммитить в GitLab только markdown, csv, json и код. SQLite, `telegram_probe.json` и секреты не коммитятся.
5. Обновить таблицу Google «DARPA — программы, компании, инвестиции» из `data/*.csv`.

## 4. Непроверенное

Утверждение без источника записывается в `LEAD_CHECK` с вердиктом «не подтверждено» и перечнем проверенных страниц. В таблицы фактов оно не вносится.

## 5. Поля «слепых зон» (с 11.11.2026)

1. Поглощённая организация (`listing_status=acquired`): заполнить в `ACQUISITION` (`darpa_data.py`) `successor_entity` + `successor_source` и, только если открытый источник прямо называет дату закрытия сделки, `acquisition_date` + `acquisition_source`. Иначе дата пустая, причина — в `acquisition_note`. Для мониторинга правопреемника добавить шаблон в `SUCCESSOR_RX`.
2. `entity_type` организации — в `ENTITY_TYPE` по словарю из README (`prime`, `company`, `corporate_division`, `FFRDC`, `UARC`, `university`, `university_spinout`, `nonprofit_research`, `other`) и с URL источника. `FFRDC` — только по Master Government List NSF; `university_spinout` — только при прямой формулировке источника. Без источника — пусто.
3. `adversarial_mirror` программы — в `MIRROR` только при источнике, прямо описывающем программу-аналог. Предложение без источника — строка в `LEAD_CHECK` с вердиктом «не подтверждено».
4. После внесения: `python3 darpa.py all --out <клон darpa-programs>`, затем рабочие списки: `python3 scripts/sam_subawards.py`, `SEC_EDGAR_USER_AGENT=… python3 scripts/revolving_door.py`, `SEC_EDGAR_USER_AGENT=… python3 scripts/proxy_detector.py --db news.sqlite`. Их результаты (`data/*.md`) в таблицы фактов автоматически не переносятся.
