# Узлы без точки на карте

Правило (с 11.11.2026): узел ставится на карту только по официально опубликованному адресу штаб-квартиры; если адреса нет — минимум город, район (область) или штат. Источник и дата — в [locations.csv](locations.csv). Узлы ниже не размещены, потому что на открытых официальных страницах такой локации не найдено (точки не придумываются).

Размещено: адрес (улица) — 76, город — 16, район / область — 1, штат — 1; без точки — 17.

| id | Название | Тип | Причина |
|---|---|---|---|
| afwerx | AFWERX | agency | на afwerx.com (contact, about-us) адрес/город штаб-квартиры не указан; в новостях упоминается WRIGHT-PATTERSON AFB как дателайн — не как HQ |
| cdao | CDAO — Chief Digital and Artificial Intelligence Office | agency | ai.mil/Contact (через WebFetch) не содержит адреса; ai.mil закрыт для curl (403) |
| iqt | In-Q-Tel (IQT) | agency | iqt.org/about перечисляет офисы (Tysons VA, Menlo Park, …) без указания штаб-квартиры |
| trmc | TRMC — Test Resource Management Center | agency | на trmc.osd.mil адрес не найден |
| brave1 | Brave1 | agency | brave1.gov.ua/en/contacts — адреса нет |
| ukdi | UK Defence Innovation (UKDI) | agency | страница gov.uk UKDI — адреса нет |
| cubic | Cubic Defense | company | официальные страницы cubic.com не отдают текст (пустой ответ/ошибка PDF); адрес только на сторонних агрегаторах — не используется |
| ghost-robotics | Ghost Robotics | company | ghostrobotics.io (about, contact, privacy) — город/адрес не указан |
| bae | BAE Systems | company | baesystems.com закрыт (Incapsula/пусто); зарегистрированный офис только на сторонних сайтах — не используется |
| deviro | Deviro | company | deviro.ua: контакты без адреса; «founded in Dnipro» — место основания, не штаб-квартира |
| taf-industries | TAF Industries | company | taf-ua.com/en/contacts — только e-mail и телефон, адреса нет |
| uav-navigation | UAV Navigation (Grupo Oesía) | company | uavnavigation.com возвращает 202/500 для автоматических запросов; адрес не подтверждён открытой страницей |
| jco | JCO — Joint Counter-small UAS Office | program | программа/офис без опубликованного адреса на странице-источнике |
| replicator | Replicator (Replicator 1 и 2) | program | программа (инициатива), а не организация с адресом |
| gcap | GCAP — Global Combat Air Programme | program | международная программа; адрес не указан на странице-источнике |
| drone-wall | European Drone Defence Initiative (European Drone Wall) | program | инициатива ЕС, адреса нет |
| x-irgc-asf | Аэрокосмические силы КСИР (IRGC ASF) | внешний узел | военная структура (Аэрокосмические силы КСИР); официального опубликованного адреса нет |

Связи, которые не рисуются на карте (один из концов без точки; перечислены в боковой панели):

- x-cto → cdao (structure): CDAO — под CTO
- x-cto → trmc (structure): TRMC — под CTO
- diu → replicator (structure): DIU — Office of Primary Responsibility процесса Replicator
- x-irgc-asf → shahed (ubo): по Минфину США: Shahed Aviation Industries Research Center подчинён IRGC ASF
