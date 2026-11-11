# darpa-programs — рабочий реестр программ DARPA

**Рабочий реестр, не перепись всех программ DARPA.** Реестр растёт по мере появления программ в новостях агрегатора cbr-srv-big.

Дата проверки: 2026-11-11. Источник истины — `darpa_data.py` в проекте агрегатора (копия в `scripts/`, таблицы — `data/`).

Правило: каждая строка имеет URL источника. Заявления из вводного списка, которые не подтверждены, записаны в `LEAD_CHECK.md` как «не подтверждено» и в таблицы не внесены.

## Как устроен «отдельный проект на программу»

Каждая программа — каталог `programs/<slug>/`: `README.md` (карточка, организации, листинг, персоналии, все совпадения из хранилища новостей). Добавление новой программы — `ADD_PROGRAM.md`.

## Программы (31)

| Программа | Полное название | Офис | Статус | Организаций | Новостей |
|---|---|---|---|---|---|
| [ACE](programs/ace/README.md) | Air Combat Evolution | Tactical Technology Office (ранее Strategic Technology Office) | завершена | 4 | 0 |
| [ACK](programs/ack/README.md) | Adapting Cross-Domain Kill-Webs | — | статус не установлен | 1 | 0 |
| [ADEPT](programs/adept/README.md) | Autonomous Diagnostics to Enable Prevention and Therapeutics | Biological Technologies Office | завершена | 1 | 0 |
| [AMPED](programs/amped/README.md) | Area-Multiplied Photonic-crystal Enhanced Devices | Multi X Office | действует | 0 | 1 |
| [ANCILLARY](programs/ancillary/README.md) | AdvaNced airCraft Infrastructure-Less Launch And RecoverY | Tactical Technology Office | статус не установлен | 3 | 0 |
| [Angler](programs/angler/README.md) | Angler | — | статус не установлен | 4 | 0 |
| [ARPANET](programs/arpanet/README.md) | ARPANET | — | завершена | 1 | 0 |
| [ASTARTE](programs/astarte/README.md) | Air Space Total Awareness for Rapid Tactical Execution | Strategic Technology Office | статус не установлен | 1 | 0 |
| [BEAMERS](programs/beamers/README.md) | BEamspace Analog processing for Multi-functional Enhanced RF Systems | — | статус не установлен | 0 | 1 |
| [BigDog](programs/bigdog/README.md) | BigDog | — | завершена | 0 | 0 |
| [DRC](programs/drc/README.md) | DARPA Robotics Challenge | Tactical Technology Office | завершена | 0 | 0 |
| [FLA](programs/fla/README.md) | Fast Lightweight Autonomy | Defense Sciences Office | завершена | 2 | 0 |
| [Grand Challenge](programs/grand-challenge/README.md) | DARPA Grand Challenge | Tactical Technology Office | завершена | 0 | 0 |
| [Gremlins](programs/gremlins/README.md) | Gremlins | Tactical Technology Office | завершена | 1 | 0 |
| [Lift Challenge](programs/lift/README.md) | DARPA Lift Challenge | Tactical Technology Office | действует | 2 | 5 |
| [LS3](programs/ls3/README.md) | Legged Squad Support System | Tactical Technology Office | завершена | 0 | 0 |
| [LunA-10](programs/luna-10/README.md) | 10-Year Lunar Architecture Capability Study | Strategic Technology Office | завершена | 7 | 0 |
| [Manta Ray](programs/manta-ray/README.md) | Manta Ray | Tactical Technology Office | действует | 2 | 0 |
| [Mosaic Warfare](programs/mosaic-warfare/README.md) | Mosaic Warfare | Strategic Technology Office | статус не установлен | 0 | 0 |
| [OFFSET](programs/offset/README.md) | OFFensive Swarm-Enabled Tactics | Tactical Technology Office | завершена | 5 | 0 |
| [PAL](programs/pal/README.md) | Personalized Assistant that Learns | — | завершена | 2 | 0 |
| [Perrseus](programs/perrseus/README.md) | Perrseus | Multi X Office | действует | 0 | 1 |
| [QBI](programs/qbi/README.md) | Quantum Benchmarking Initiative | Multi X Office | действует | 10 | 0 |
| [RACER](programs/racer/README.md) | Robotic Autonomy in Complex Environments with Resiliency | Tactical Technology Office | действует | 3 | 1 |
| [REMA](programs/rema/README.md) | Rapid Experimental Missionized Autonomy | Tactical Technology Office | действует | 5 | 0 |
| [SCEPTER](programs/scepter/README.md) | Strategic Chaos Engine for Planning, Tactics, Experimentation and Resiliency | Strategic Technology Office | действует | 3 | 0 |
| [SHEPARD](programs/shepard/README.md) | Series Hybrid Electric Propulsion AiRcraft Demonstration (XRQ-73) | Tactical Technology Office | завершена | 1 | 1 |
| [SubT](programs/subt/README.md) | DARPA Subterranean Challenge | Tactical Technology Office | завершена | 0 | 0 |
| [DTC](programs/triage/README.md) | DARPA Triage Challenge | Biological Technologies Office | действует | 0 | 1 |
| [Urban Challenge](programs/urban-challenge/README.md) | DARPA Urban Challenge | Tactical Technology Office | завершена | 1 | 0 |
| [US2QC](programs/us2qc/README.md) | Underexplored Systems for Utility-Scale Quantum Computing | — | статус не установлен | 2 | 0 |

## Листинг организаций

- поглощена / входит в группу: 10
- закрыта: 1
- торгуется на бирже: 24
- частная: 22
- не установлено: 1

Таблицы: `data/darpa_item_tags.json` (разметка новостей), `data/darpa_orgs.csv` (листинг, тикер, биржа, источник), `data/darpa_program_orgs.csv`, `data/darpa_personnel.csv`, `data/darpa_programs.csv`, `data/darpa_lead_check.csv`.

## Слепые зоны реестра: поля и скрипты (11.11.2026)

Это **рабочий** реестр. Пустая ячейка значит «открытого источника на дату проверки нет», а не «нет связи». Непроверенные утверждения и вводные списки остаются в `LEAD_CHECK.md` с вердиктом «не подтверждено» и в основные таблицы не вносятся. Рабочие списки скриптов (`data/*.md`) — кандидаты для ручной проверки, не перепись и не факты реестра; в `darpa_orgs.csv` из них ничего не вносится автоматически.

### Новые колонки

| Таблица | Колонка | Правило |
|---|---|---|
| `darpa_orgs.csv` | `successor_entity`, `successor_source` | правопреемник / материнская группа — только со страницей источника |
| `darpa_orgs.csv` | `acquisition_date`, `acquisition_source`, `acquisition_note` | дата закрытия сделки — только если открытый источник её прямо называет; иначе пусто и причина в `acquisition_note` |
| `darpa_orgs.csv`, `darpa_program_orgs.csv` | `entity_type` (+ `entity_type_source` в orgs) | словарь: `prime`, `company`, `corporate_division`, `FFRDC`, `UARC`, `university`, `university_spinout`, `nonprofit_research`, `other`; пусто — не классифицировано |
| `darpa_programs.csv` | `adversarial_mirror`, `mirror_country`, `mirror_source` | заполняется только при источнике, прямо описывающем программу-аналог; предложения без источника — в `LEAD_CHECK.md` |
| `darpa_personnel.csv` | `red_flag`, `red_flag_source` | только с источником; кандидаты из `revolving_door.py` сюда не переносятся автоматически |

`entity_type`: `FFRDC` — только по Master Government List of FFRDCs (NSF NCSES, https://www.nsf.gov/statistics/ffrdclist/); `university_spinout` — только при прямой формулировке источника; `prime` — только организации, которые `companies.csv` относит к Tier 1.

### Мониторинг правопреемника

Агрегатор продолжает искать старое название организации (`ORG_RX` в `darpa.py`). Если у организации заполнен `successor_entity`, `darpa.py tag` дополнительно размечает материал старым `org_id`, когда в тексте одновременно названы правопреемник (`SUCCESSOR_RX` в `darpa_data.py`) и сильный шаблон программы, с которой старая организация связана в `darpa_program_orgs.csv` (в `matched` — `successor:<org_id>`). Для организаций без связи с программой связка не работает (нет проверенных терминов технологии).

### Скрипты (`scripts/`, только стандартная библиотека Python)

- `sam_subawards.py` — головные контракты и субподряды по исполнителям реестра из открытого API USAspending.gov (агентство DARPA) → `data/sam_subawards.csv`, `data/sam_subawards.md` (рабочий список субподрядчиков, которых нет в `darpa_orgs.csv`).
- `revolving_door.py` — перекрёстная проверка `darpa_personnel.csv` с официальными данными SEC EDGAR (инсайдерские отчёты Forms 3/4/5 и списки должностных лиц компаний с листингом) → `data/revolving_door.md`. LinkedIn не используется.
- `proxy_detector.py` — для компаний с листингом берёт Exhibit 21 («Subsidiaries of the Registrant») из последнего 10-K в SEC EDGAR и сравнивает дочерние структуры с названиями в `data/darpa_item_tags.json` → `data/potential_shells.md` / `.csv`.
- Для запросов к SEC нужна переменная `SEC_EDGAR_USER_AGENT` (описательный User-Agent с контактом); без неё скрипты работают только в режиме `--dry-run`.
