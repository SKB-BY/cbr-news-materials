# Узлы без точки на карте

Правило (с 11.11.2026): узел ставится на карту только по официально опубликованному адресу штаб-квартиры; если адреса нет — минимум город, район (область) или штат. Источник и дата — в [locations.csv](locations.csv). Узлы ниже не размещены, потому что на открытых официальных страницах такой локации не найдено (точки не придумываются).

Размещено: адрес (улица) — 94, город — 18, район / область — 1, штат — 0; без точки — 20.

| id | Название | Тип | Причина |
|---|---|---|---|
| brave1 | Brave1 | agency | официальный адрес не найден: на brave1.gov.ua (контакты) указаны только e-mail и телефон; адрес из каталога выставки AUSA не официален |
| kara-dag | Kara Dag Technologies | company | официальный адрес не найден: на karadagtech.com указаны только e-mail |
| taf-industries | TAF Industries | company | официальный адрес не найден: на taf-ua.com указаны только e-mail и телефон (город в вакансиях — не адрес штаб-квартиры) |
| jco | JCO — Joint Counter-small UAS Office | program | программа/офис без опубликованного адреса на странице-источнике |
| replicator | Replicator (Replicator 1 и 2) | program | программа (инициатива), а не организация с адресом |
| gcap | GCAP — Global Combat Air Programme | program | международная программа; адрес не указан на странице-источнике |
| drone-wall | European Drone Defence Initiative (European Drone Wall) | program | инициатива ЕС, адреса нет |
| ukrspecsystems | Ukrspecsystems | company | официальный адрес не найден: на ukrspecsystems.com (Contact, About) указаны только телефон и e-mail |
| wild-hornets | Wild Hornets (Дикі Шершні) | company | официальный адрес не найден: на wildhornets.com указан только e-mail |
| techex | TechEx | company | официальный адрес не найден: на techex.com.ua адрес не опубликован (упоминание обороны Киева в 2022 г. — история, не адрес) |
| militech | MILITECH (Militech Group) | company | официальный адрес не найден: на militech.com.ua указаны только телефоны и e-mail |
| phantom-defense | Phantom Defense | company | официальный адрес не найден: на phantomdefense.tech (Contacts) указаны только телефоны и e-mail |
| devdroid | DevDroid | company | официальный адрес не найден: на devdroid.tech адрес штаб-квартиры не опубликован (сервисные команды во Львове, Харькове и Днепре — не адрес) |
| sine-engineering | Sine Engineering (Sine.Engineering) | company | официальный адрес не найден: на sineeng.com адрес не опубликован |
| inlab | InLab | company | официальный адрес не найден: на inlab.kyiv.ua указаны только e-mail и телефон (домен kyiv.ua — не адрес) |
| defika | Defika | company | официальный адрес не найден: на defika.com.ua указан только e-mail |
| delta | DELTA — система ситуационной осведомлённости (Минобороны Украины) | program | система (программа) Минобороны Украины, а не организация с адресом |
| drone-dominance | Drone Dominance Program (DDP) | program | программа МВ США; адрес не указан на странице-источнике |
| x-irgc-asf | Аэрокосмические силы КСИР (IRGC ASF) | внешний узел | военная структура (Аэрокосмические силы КСИР); официального опубликованного адреса нет |
| x-skyfall | SkyFall | внешний узел | официальный сайт skyfall.ua 11.11.2026 не открылся; адрес не установлен |

Связи, которые не рисуются на карте (один из концов без точки; перечислены в боковой панели):

- diu → replicator (structure): DIU — Office of Primary Responsibility процесса Replicator
- x-irgc-asf → shahed (ubo): по Минфину США: Shahed Aviation Industries Research Center подчинён IRGC ASF
- diehl → brave1 (partner): Diehl — первая иностранная компания, испытавшая свой НРК (UGV) в рамках платформы Test in Ukraine (Brave1), на полигоне 3-й штурмовой бригады (Минцифры, 28.07.2025)
- shieldai → brave1 (partner): через Brave1 Shield AI установила партнёрство с украинской компанией (название не раскрыто): ПО Shield AI интегрировано с дронами этой компании (пост Brave1; Shield AI в X, по «Украинской правде», 13.03.2026)
- palantir → brave1 (partner): Brave1 Dataroom — защищённая среда для обучения военных ИИ-моделей на ПО Palantir; запущена МО и Минцифры Украины, ВСУ, НИИ военной разведки и Palantir (МО Украины, 21.01.2026)
- anduril → kara-dag (partner): Kara Dag Technologies начала сотрудничество с Anduril: передаёт практики противодействия дронам, полученные в боевых условиях, для систем Anduril, уже используемых в Украине (сайт Kara Dag, 03.2026)
- airbus-ds → x-skyfall (partner): Airbus Defence and Space и SkyFall подписали меморандум (MoU) о стратегическом партнёрстве на ILA Berlin, 12.06.2026 (релиз Airbus); партнёрство, не подчинённость
- x-japan-mod → x-skyfall (customer): министр обороны Японии С. Коидзуми, 09.10.2026: «既に防衛省では、ウクライナのスカイフォール社の迎撃用ドローンの取得契約を締結しており» — контракт на приобретение дронов-перехватчиков уже подписан; модель, количество и сумма не названы
- redcat → sine-engineering (partner): Red Cat и Sine Advanced Engineering, Inc. (американское подразделение Sine) подписали неэксклюзивный MoU о стратегическом партнёрстве: интеграция связи и навигации Sine в БЭК Blue Ops и БЛА Red Cat (релиз Red Cat, 02.11.2026)
- phantom-defense → drone-dominance (partner): Phantom Defense участвовала в Gauntlet II программы Drone Dominance (Форт-Карсон): одна из трёх компаний, создававших РЭБ-среду противодействия для испытаний БЛА; после этапа получила приглашения на дальнейшие мероприятия (по сайту компании). Испытания, не подчинённость
- diu → drone-dominance (structure): DDP «jointly administered by the Test Resource Management Center (TRMC) and the Defense Innovation Unit (DIU)»; DIU курирует работу с промышленностью
- trmc → drone-dominance (structure): TRMC — «primary execution authority and test range coordinator» программы Drone Dominance
- techex → brave1 (partner): по сайту TechEx: «TechEx works with the Ukrainian state through the BRAVE1 defense innovation cluster and the Dot Chain procurement system» (заявление компании)
- militech → brave1 (partner): по сайту MILITECH: решения «available on the government portals DOT and Brave1» (заявление компании)
