# Сферы — проверка вводных (реестр сил и компаний)

Проверка 12.11.2026 (Europe/Minsk; время проверки в колонке — UTC). Источник вводных — сущности контура (компания, организация, программа) из новых сфер и [Разрыв упоминаний](data/mention_gap.md). В [Реестр сил и компаний](companies.csv) строка вносится только после открытия официальной страницы на дату проверки. Вводные — не факт.

## Внесены 12.11.2026 (официальная страница открыта, HTTP 200)

| название | страна | официальный URL | результат |
|---|---|---|---|
| AEVEX Aerospace | США | https://aevex.com/ | HTTP 200, «Home», 2026-11-12T15:36:45Z |
| CHAOS Industries | США | https://www.chaosinc.com/ | HTTP 200, «A NEW WAR ORDER \| CHAOS Industries», 2026-11-12T15:36:45Z |
| Neros Technologies | США | https://www.neros.tech/ | HTTP 200, «Home - Neros», 2026-11-12T15:36:45Z |
| Dassault Aviation | Франция | https://www.dassault-aviation.com/ | HTTP 200, «Dassault Aviation, a major player to aeronautics», 2026-11-12T15:36:45Z |
| Frankenburg Technologies | Эстония | https://frankenburg.tech/ | HTTP 200, «Frankenburg Technologies – Guided Missile Systems», 2026-11-12T15:36:45Z |
| MSI-Defence Systems | Великобритания | https://www.msi-dsl.com/ | HTTP 200, «Home - MSI Defence Systems», 2026-11-12T15:36:45Z |
| Naval Group | Франция | https://www.naval-group.com/ | HTTP 200, «Homepage \| Naval Group», 2026-11-12T15:36:45Z |
| Nordic Air Defence | Швеция | https://www.nordicairdefence.com/ | HTTP 200, «Nordic Air Defence», 2026-11-12T15:36:45Z |
| TYTAN Technologies | Германия | https://www.tytan-technologies.com/ | HTTP 200, «TYTAN Technologies \| Building the new era of European Air Defense», 2026-11-12T15:36:45Z |
| D-Fend Solutions | Израиль | https://d-fendsolutions.com/ | HTTP 200, «Counter-Drone Takeover Technology \| D-Fend Solutions», 2026-11-12T15:36:45Z |
| Embraer | Бразилия | https://embraer.com/ | HTTP 200, «Welcome to Embraer», 2026-11-12T15:36:45Z |

Адрес штаб-квартиры этих компаний в этот проход по официальной странице не подтверждался: на Карте реестра они без точки ([map/UNLOCATED.md](map/UNLOCATED.md)).

## Не внесены

| вводная | проверенный URL | результат | причина |
|---|---|---|---|
| GE Aerospace | https://www.geaerospace.com/ | HTTP 403, «GE Aerospace», 2026-11-12T15:34:49Z | защита от ботов, страница не открылась |
| SpaceX | https://www.spacex.com/ | HTTP 403, 2026-11-12T15:34:49Z | защита от ботов, страница не открылась |
| EDGE Group | https://edgegroup.ae/ | HTTP 403, «Attention Required! \| Cloudflare», 2026-11-12T15:34:55Z | Cloudflare, страница не открылась |
| AIRO Group | https://www.airogroup.com/ | HTTP 200, «Airogroup \| Specialist in sustainable formulas for private labeling», 2026-11-12T15:35:03Z → https://www.airogroup.nl/ | адрес ведёт на постороннюю компанию; официальный сайт не установлен |
| Griffon Aerospace | https://www.griffonaerospace.com/ | HTTP 200, «Griffon Aerospace – The Unfair Advantage», 2026-11-12T15:34:54Z | страница открыта, но упоминания в ленте не подтверждают отношение к сферам; отложено |
| ГЛОНАСС, Рособоронэкспорт, RuDrones, «Стратос», «Калашников», Ростех, «Высокоточные комплексы» | — | не проверялись | российские юрлица в публичный реестр не входят |
| Пентагон, US Army, US Air Force, US Navy, US Marine Corps, НАТО, Европейский союз | — | не проверялись в этот проход | органы и структуры; в реестре — профильные организации и агентства, отдельные строки не добавлялись |
| JIATF 401, Project Vanquish, Project BEEHIVE, Project Agincourt, Project Convergence-Capstone | — | не проверялись в этот проход | программа вносится только после открытия официальной страницы программы |

Иранские компании — объекты анализа угроз и цепочек поставок, в контур Программ DARPA не входят.
