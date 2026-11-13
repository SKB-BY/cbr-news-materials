# Узлы без точки на карте

Правило (с 13.11.2026, t79u/t80u): точка ставится по официально опубликованному адресу штаб-квартиры или (минимум) городу / району / штату — поле location_precision «точно». Если официального адреса нет, допустима приблизительная точка по косвенным признакам (официальный пресс-релиз или страница контактов, вакансии, выставка, город в реестре, даталайн новости, место исполнения контракта) — «приблизительно». У каждой приблизительной точки в location_basis в начале стоит формулировка «Местоположение не официальное, установлено по признакам», затем перечень признаков (URL, цитата, дата проверки). Нет признака — точки нет (список ниже). Столица или центр страны без признака не ставятся. Юридический адрес подписывается «юридический адрес», не как завод. Домашние адреса не публикуются. Российских юрлиц в реестре нет. Источник и дата — в [locations.csv](locations.csv).

Размещено: адрес (улица) — 142, город — 51, район / область — 1, штат — 0; точно — 189, приблизительно — 5; без точки — 17.

| id | Название | Тип | Причина |
|---|---|---|---|
| kara-dag | Kara Dag Technologies | company | официальный адрес не найден: на karadagtech.com указаны только e-mail |
| taf-industries | TAF Industries | company | официальный адрес не найден: на taf-ua.com указаны только e-mail и телефон (город в вакансиях — не адрес штаб-квартиры) |
| jco | JCO — Joint Counter-small UAS Office | program | точка не ставится: JCO упразднён и заменён JIATF 401 (релиз war.gov и Defense News, 28.08.2025); адрес офиса не опубликован |
| replicator | Replicator (Replicator 1 и 2) | program | программа (инициатива), а не организация с адресом |
| drone-wall | European Drone Defence Initiative (European Drone Wall) | program | инициатива ЕС, адреса нет |
| phantom-defense | Phantom Defense | company | официальный адрес не найден: на phantomdefense.tech (Contacts) только телефоны и e-mail; на сайте — «nine production sites» без мест; адреса Creative States (Киев) и 1055 Thomas Jefferson St NW (Вашингтон) на usubc.org — офисы USUBC (страница Contacts USUBC), не Phantom Defense |
| delta | DELTA — система ситуационной осведомлённости (Минобороны Украины) | program | система (программа) Минобороны Украины, а не организация с адресом |
| drone-dominance | Drone Dominance Program (DDP) | program | программа МВ США; адрес не указан на странице-источнике |
| 3avada | 3AVADA (Завада) | company | официальный адрес не найден: на zavada.co указано только «Україна» (город Ивано-Франковск — только LinkedIn, не источник) |
| skilur | SKILUR | company | официальный адрес не найден: на skilur.tech только «registered in Ukraine» |
| realgold | Realgold (ThrustNova) | company | официальный адрес не найден: на сайте адреса нет; совпадение юрлица в реестре только по названию и КВЭД, без ссылки на сайт |
| ptashka-drones | Ptashka Drones | company | официальный адрес не найден: на ptashkadrones.com только контакты без адреса |
| vyriy | Vyriy Industries | company | официальный адрес не найден: на сайте адреса нет; совпадение юрлица в реестре только по названию и КВЭД, без ссылки на сайт |
| innovation-development-fund | Фонд развития инноваций (Innovation Development Fund) | agency | официальный адрес не найден: на страницах Минцифры (03.06.2025, 20.08.2026) и Brave1 адреса нет; адрес Brave1 по умолчанию не переносится |
| unite-brave-nato | UNITE – Brave NATO | program | совместная программа НАТО и Украины; одной локации нет |
| bravetech-eu | BraveTech EU | program | совместная инициатива ЕС и Украины; одной локации нет |
| x-irgc-asf | Аэрокосмические силы КСИР (IRGC ASF) | внешний узел | военная структура (Аэрокосмические силы КСИР); официального опубликованного адреса нет |

Связи, которые не рисуются на карте (один из концов без точки; перечислены в боковой панели):

- diu → replicator (structure): DIU — Office of Primary Responsibility процесса Replicator
- x-irgc-asf → shahed (ubo): по Минфину США: Shahed Aviation Industries Research Center подчинён IRGC ASF
- anduril → kara-dag (partner): Kara Dag Technologies начала сотрудничество с Anduril: передаёт практики противодействия дронам, полученные в боевых условиях, для систем Anduril, уже используемых в Украине (сайт Kara Dag, 03.2026)
- phantom-defense → drone-dominance (partner): Phantom Defense участвовала в Gauntlet II программы Drone Dominance (Форт-Карсон): одна из трёх компаний, создававших РЭБ-среду противодействия для испытаний БЛА; после этапа получила приглашения на дальнейшие мероприятия (по сайту компании). Испытания, не подчинённость
- diu → drone-dominance (structure): DDP «jointly administered by the Test Resource Management Center (TRMC) and the Defense Innovation Unit (DIU)»; DIU курирует работу с промышленностью
- trmc → drone-dominance (structure): TRMC — «primary execution authority and test range coordinator» программы Drone Dominance
- nswc-crane → drone-dominance (structure): NSWC Crane «holds contracting authority and issues prototype delivery orders based on Gauntlet test results» в программе Drone Dominance
- general-cherry → drone-dominance (partner): по сайту General Cherry: компания прошла первый и второй этапы DDP; Wilcox Cherry Defense (совместное производство с американской Wilcox) — среди 19 компаний, прошедших квалификационный этап
- taf-industries → wingcopter (partner): меморандум (MoU) 13.02.2026 о намерении создать совместное предприятие для производства разведывательных БЛА TAF в Германии (сайты TAF и Wingcopter); СП в стадии намерения
- taf-industries → pgz (partner): письмо о намерениях (LoI) 25.06.2026, Гданьск: локализация производства БЛА в Польше (сайт TAF)
- innovation-development-fund → brave1 (structure): Brave1 — государственная инициатива, реализуемая Фондом развития инноваций (страница About Brave1, 12.11.2026); решения о грантах — большинством голосов наблюдательного совета Фонда (МО Украины, 06.11.2026)
- unite-brave-nato → brave1 (structure): с украинской стороны программу координирует Brave1, первый конкурс со стороны НАТО ведёт NCIA (МО Украины)
- bravetech-eu → brave1 (structure): BraveTech EU связывает платформу Brave1 Минцифры с European Defence Fund и EUDIS (Еврокомиссия, 11.07.2025)
- eda → bravetech-eu (partner): DefTech Forges — конкурсы в рамках BraveTech EU: финансирует Еврокомиссия, поддерживают Brave1 и EDA; победители смогут продолжить испытания с EDA (Brave1, 12.08.2026)
