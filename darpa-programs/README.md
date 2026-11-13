# Программы DARPA — реестр по всем офисам

Проверка 2026-11-13 (Europe/Minsk). В реестре 778 программ: все страницы программ из карты сайта darpa.mil (https://www.darpa.mil/sitemap.xml, раздел /research/programs/) и программы, найденные в новостях агрегатора без страницы darpa.mil.

Источники: страница программы на darpa.mil (название, офис, назначение — цитата, руководитель, пометка «This program is now complete»); исполнители — открытый API USAspending.gov (агентство-заказчик DARPA; в реестр попадают только записи, где описание контракта называет программу); новости — совпадение названия программы в хранилище агрегатора (live и архив). Пустое поле — в источнике нет. Непроверенные совпадения на публичные страницы не выносятся.

Офис I2O на darpa.mil на дату проверки не значится; программы информационной тематики там указаны с офисом IPTO. MTO расширен в Multi X Office (MXO) — по странице https://www.darpa.mil/about/offices/mxo.

## Сводка по офисам (категориям)

| Офис | Программ | Действуют | Завершены | С исполнителями | С новостями |
|---|---|---|---|---|---|
| [Tactical Technology Office (TTO) — тактические технологии](#office-tto) | 76 | 22 | 54 | 48 | 14 |
| [Strategic Technology Office (STO) — стратегические технологии](#office-sto) | 71 | 23 | 46 | 30 | 0 |
| [Information Processing Techniques Office (IPTO) — обработка информации](#office-ipto) | 137 | 37 | 100 | 48 | 0 |
| [Multi X Office (MXO; расширение Microsystems Technology Office, MTO)](#office-mxo) | 128 | 44 | 84 | 62 | 3 |
| [Defense Sciences Office (DSO) — оборонные науки](#office-dso) | 137 | 45 | 92 | 59 | 0 |
| [Biological Technologies Office (BTO) — биологические технологии](#office-bto) | 110 | 41 | 69 | 44 | 1 |
| [Small Business Programs Office (SBPO) — программы малого бизнеса](#office-sbpo) | 50 | 0 | 50 | 0 | 0 |
| [Director's Office (DO) — офис директора](#office-do) | 1 | 0 | 1 | 0 | 0 |
| [Офис не указан на странице darpa.mil](#office-none) | 68 | 20 | 46 | 19 | 1 |

## Сферы (ось сайта)

| Сфера | Программ |
|---|---|
| вооружение | 5 |
| бронетехника | 0 |
| армейские джипы | 0 |
| артиллерийские системы | 0 |
| системы ПВО и РВСН | 0 |
| авиация | 12 |
| средства связи и коммуникаций | 6 |
| программное обеспечение специального назначения | 1 |
| тактика и стратегия | 6 |
| БПЛА | 30 |

Сфера назначается словарём sphere.py (термин в названии или цитате назначения; иначе ≥2 разных термина в описании). У остальных программ признаков нет — сфера не назначается.

<a id="office-tto"></a>

## Tactical Technology Office (TTO) — тактические технологии — 76

| Программа | Полное название | Статус | Сфера | Руководитель (darpa.mil) | Исполнителей | Новостей |
|---|---|---|---|---|---|---|
| [ACE](programs/ace/README.md) | Air Combat Evolution | завершена |  |  | 7 | 2 |
| [ACTUV](programs/anti-submarine-warfare/README.md) | Anti-Submarine Warfare (ASW) Continuous Trail Unmanned Vessel | завершена | БПЛА |  | 3 | 0 |
| [AFRE](programs/advanced-full-range-engine/README.md) | Advanced Full Range Engine | завершена |  |  | 1 | 0 |
| [ALASA](programs/airborne-launch-assist-space-access/README.md) | Airborne Launch Assist Space Access | завершена |  |  | 3 | 0 |
| [ALIAS](programs/aircrew-labor-in-cockpit-automation-system/README.md) | Aircrew Labor In-Cockpit Automation System | действует | авиация | Matthew Sambora | 2 | 0 |
| [ALTA](programs/adaptable-lighter-than-air/README.md) | Adaptable Lighter Than Air | завершена |  |  | 0 | 0 |
| [ANCILLARY](programs/ancillary/README.md) | AdvaNced airCraft Infrastructure-Less Launch And RecoverY | действует | БПЛА, авиация | Phillip Smith | 3 | 4 |
| [Anzio](programs/anzio/README.md) | Anzio | действует |  | Matthew Sambora | 0 | 0 |
| [APEX](programs/advanced-propulsor-experimental/README.md) | Advanced Propulsor, Experimental | действует | БПЛА | Mark Rice | 3 | 0 |
| [ARES](programs/aerial-reconfigurable-embedded-system/README.md) | Aerial Reconfigurable Embedded System | завершена |  |  | 0 | 1 |
| [AVM](programs/adaptive-vehicle-make/README.md) | Adaptive Vehicle Make | завершена |  |  | 0 | 0 |
| [Blackjack](programs/blackjack/README.md) | Blackjack | завершена |  |  | 6 | 0 |
| [Blue Wolf](programs/blue-wolf/README.md) | Blue Wolf | завершена | БПЛА |  | 0 | 0 |
| [BnG](programs/burn-n-go/README.md) | Burn n’ Go | действует |  | Hunter Martin | 0 | 0 |
| [Carbon Crunch](programs/carbon-crunch/README.md) | Carbon Crunch | действует |  | Michael Mulqueen | 0 | 0 |
| [CODE](programs/collaborative-operations-in-denied-environment/README.md) | Collaborative Operations in Denied Environment | завершена | БПЛА |  | 0 | 0 |
| [CONFERS](programs/consortium-for-execution-of-rendezvous-and-servicing-operations/README.md) | Consortium for Execution of Rendezvous and Servicing Operations | завершена |  |  | 1 | 0 |
| [CRANE](programs/control-of-revolutionary-aircraft-with-novel-effectors/README.md) | Control of Revolutionary Aircraft with Novel Effectors | действует | авиация | Chris Cotting | 3 | 2 |
| [CyPhER Forge](programs/cypher-forge/README.md) | Cyber Physical System Executing in Real Time | действует |  | Chris Cotting | 0 | 0 |
| [DARPA Launch Challenge](programs/launch-challenge/README.md) | DARPA Launch Challenge | завершена |  |  | 0 | 0 |
| [Deep Thoughts](programs/deep-thoughts/README.md) | Deep Thoughts | действует |  | Kevin Sloan | 0 | 0 |
| [DRACO](programs/demonstration-rocket-for-agile-cislunar-operations/README.md) | Demonstration Rocket for Agile Cislunar Operations | завершена |  |  | 2 | 0 |
| [DRC](programs/drc/README.md) | DARPA Robotics Challenge | завершена |  |  | 5 | 0 |
| [EXACTO](programs/extreme-accuracy-tasked-ordnance/README.md) | EXtreme ACcuracy Tasked Ordnance | завершена | вооружение |  | 2 | 0 |
| [Galileo](programs/galileo/README.md) | Galileo | завершена |  |  | 0 | 0 |
| [Gambit](programs/gambit/README.md) | Gambit | завершена |  |  | 1 | 0 |
| [Glide Breaker](programs/glide-breaker/README.md) | Glide Breaker | завершена |  |  | 4 | 0 |
| [Grand Challenge](programs/grand-challenge/README.md) | DARPA Grand Challenge | завершена |  |  | 0 | 0 |
| [Gremlins](programs/gremlins/README.md) | Gremlins | завершена | авиация |  | 2 | 0 |
| [GXV-T](programs/ground-x-vehicle-technologies/README.md) | Ground X-Vehicle Technologies | завершена |  |  | 1 | 0 |
| [Hallmark](programs/hallmark/README.md) | Hallmark | завершена |  |  | 1 | 0 |
| [HAWC](programs/hypersonic-air-breathing-weapon-concept/README.md) | Hypersonic Air-breathing Weapon Concept | завершена |  |  | 4 | 0 |
| [Heimdall](programs/heimdall/README.md) | Heimdall | действует |  | Mark Rice | 0 | 0 |
| [HTV-2](programs/falcon-htv-2/README.md) | Falcon Hypersonic Technology Vehicle 2 | завершена |  |  | 3 | 0 |
| [Hydra](programs/hydra/README.md) | Hydra | завершена |  |  | 0 | 0 |
| [Liberty Lifter](programs/liberty-lifter/README.md) | Liberty Lifter | завершена |  |  | 2 | 0 |
| [Lift Challenge](programs/lift/README.md) | DARPA Lift Challenge | действует | БПЛА | Phillip Smith | 2 | 5 |
| [LongShot](programs/longshot/README.md) | LongShot | действует | БПЛА | Shawn Naigle | 3 | 1 |
| [LRASM](programs/long-range-anti-ship-missile/README.md) | Long Range Anti-Ship Missile | завершена |  |  | 0 | 0 |
| [LS3](programs/ls3/README.md) | Legged Squad Support System | завершена |  |  | 0 | 0 |
| [MACH](programs/materials-architectures-and-characterization-for-hypersonics/README.md) | Materials Architectures and Characterization for Hypersonics | завершена |  |  | 3 | 0 |
| [MAD-FIRES](programs/multi-azimuth-defense-fast-intercept-round-engagement-system/README.md) | Multi-Azimuth Defense Fast Intercept Round Engagement System | завершена | вооружение |  | 2 | 0 |
| [MAHEM](programs/magneto-hydrodynamic-explosive-munition/README.md) | MAgneto Hydrodynamic Explosive Munition | завершена | вооружение |  | 0 | 0 |
| [Manta Ray](programs/manta-ray/README.md) | Manta Ray | действует |  | Kevin Sloan | 6 | 6 |
| [MFP](programs/mobile-force-protection/README.md) | Mobile Force Protection | завершена | БПЛА |  | 0 | 1 |
| [MOHAWC](programs/mohawc/README.md) | More Opportunities with HAWC | действует |  | Clark McGehee | 0 | 0 |
| [NOMARS](programs/no-manning-required-ship/README.md) | No Manning Required Ship | действует |  | Mark Rice | 4 | 2 |
| [OFFSET](programs/offset/README.md) | OFFensive Swarm-Enabled Tactics | завершена | тактика и стратегия |  | 11 | 0 |
| [OpFires](programs/operational-fires/README.md) | Operational Fires | завершена |  |  | 2 | 0 |
| [Otter](programs/otter/README.md) | Otter | действует |  | Michael Mulqueen | 0 | 0 |
| [Oversight](programs/oversight/README.md) | Oversight | действует |  | John Main | 0 | 0 |
| [PCAS](programs/persistent-close-air-support/README.md) | Persistent Close Air Support | завершена |  |  | 1 | 0 |
| [Phoenix](programs/phoenix/README.md) | Phoenix | завершена |  |  | 0 | 0 |
| [POWER](programs/power/README.md) | Persistent Optical Wireless Energy Relay | завершена |  |  | 1 | 3 |
| [Pulling Guard](programs/pulling-guard/README.md) | Pulling Guard | действует |  | Mark Rice | 0 | 0 |
| [RACER](programs/racer/README.md) | Robotic Autonomy in Complex Environments with Resiliency | действует | БПЛА | John Main | 6 | 2 |
| [REMA](programs/rema/README.md) | Rapid Experimental Missionized Autonomy | действует | БПЛА | Phillip Smith | 5 | 3 |
| [RNET](programs/rnet/README.md) | RNET | завершена |  |  | 1 | 0 |
| [RSGS](programs/robotic-servicing-of-geosynchronous-satellites/README.md) | Robotic Servicing of Geosynchronous Satellites | действует |  | James Shoemaker | 1 | 0 |
| [Sea Train](programs/sea-train/README.md) | Sea Train | завершена | БПЛА |  | 2 | 0 |
| [SeeMe](programs/space-enabled-effects-military-engagements/README.md) | Space Enabled Effects for Military Engagements | завершена |  |  | 1 | 0 |
| [SHEPARD](programs/shepard/README.md) | Series Hybrid Electric Propulsion AiRcraft Demonstration (XRQ-73) | завершена | авиация |  | 1 | 7 |
| [SPRINT](programs/speed-runway-independent-technologies/README.md) | Speed and Runway Independent Technologies | действует | авиация | Ian Higgins | 3 | 1 |
| [Squad X](programs/squad-x/README.md) | Squad X Core Technologies | завершена |  |  | 3 | 0 |
| [SST](programs/space-surveillance-telescope/README.md) | Space Surveillance Telescope | завершена |  |  | 0 | 0 |
| [SubT](programs/subt/README.md) | DARPA Subterranean Challenge | завершена |  |  | 3 | 0 |
| [System F6](programs/system-f6/README.md) | System F6 | завершена |  |  | 2 | 0 |
| [TBG](programs/tactical-boost-glide/README.md) | Tactical Boost Glide | завершена |  |  | 4 | 0 |
| [TEMP](programs/tactically-expandable-maritime-platform/README.md) | Tactically Expandable Maritime Platform | завершена |  |  | 1 | 0 |
| [Tern](programs/tern/README.md) | Tactically Exploited Reconnaissance Node | завершена | БПЛА, авиация |  | 2 | 0 |
| [Underminer](programs/underminer/README.md) | Underminer | завершена |  |  | 0 | 0 |
| [Urban Challenge](programs/urban-challenge/README.md) | DARPA Urban Challenge | завершена |  |  | 1 | 0 |
| [URSA](programs/urban-reconnaissance-through-supervised-autonomy/README.md) | Urban Reconnaissance through Supervised Autonomy | завершена |  |  | 0 | 0 |
| [VTOL X-Plane](programs/vertical-takeoff-and-landing-experimental-plane/README.md) | Vertical Takeoff and Landing Experimental Plane | завершена | авиация |  | 2 | 0 |
| [Vulture](programs/vulture/README.md) | Vulture | завершена |  |  | 0 | 0 |
| [XSP](programs/experimental-space-plane/README.md) | Experimental Spaceplane | завершена | авиация |  | 1 | 0 |

<a id="office-sto"></a>

## Strategic Technology Office (STO) — стратегические технологии — 71

| Программа | Полное название | Статус | Сфера | Руководитель (darpa.mil) | Исполнителей | Новостей |
|---|---|---|---|---|---|---|
| [100G](programs/100-gb-s-rf-backbone/README.md) | 100 Gb/s RF Backbone | завершена | средства связи и коммуникаций |  | 0 | 0 |
| [AAA](programs/assured-arctic-awareness/README.md) | Assured Arctic Awareness | завершена |  |  | 0 | 0 |
| [ACK](programs/ack/README.md) | Adapting Cross-Domain Kill-Webs | завершена |  |  | 1 | 0 |
| [ADAPT](programs/adaptable-sensor-system/README.md) | ADAPTable Sensor System | завершена |  |  | 1 | 0 |
| [Advanced RF Mapping](programs/advance-rf-mapping/README.md) | Advanced RF Mapping | завершена |  |  | 0 | 0 |
| [Aerial Dragnet](programs/aerial-dragnet/README.md) | Aerial Dragnet | завершена | БПЛА |  | 1 | 0 |
| [Albatross](programs/albatross/README.md) | Albatross | действует | авиация | Steven Chambers | 0 | 0 |
| [ANS](programs/adaptable-navigation-systems/README.md) | Adaptable Navigation Systems | завершена |  |  | 0 | 0 |
| [ASIMOV](programs/autonomy-standards-and-ideals-with-military-operational-values/README.md) | Autonomy Standards and Ideals with Military Operational Values | завершена |  |  | 0 | 0 |
| [ASTARTE](programs/astarte/README.md) | Air Space Total Awareness for Rapid Tactical Execution | статус не установлен |  |  | 1 | 0 |
| [BLiP](programs/beyond-linear-processing/README.md) | Beyond Linear Processing | завершена |  |  | 0 | 0 |
| [BRIDGES](programs/bridges/README.md) | Bringing Classified Innovation to Defense and Government Systems | завершена |  |  | 0 | 0 |
| [C-Sniper](programs/counter-sniper-program/README.md) | Counter-Sniper Program | завершена |  |  | 0 | 0 |
| [C2E](programs/communications-in-contested-environments/README.md) | Communications in Contested Environments | завершена | средства связи и коммуникаций |  | 0 | 0 |
| [CBMEN](programs/content-based-mobile-edge-networking/README.md) | Content-Based Mobile Edge Networking | завершена |  |  | 1 | 0 |
| [CDMaST](programs/cross-domain-maritime-surveillance-and-targeting/README.md) | Cross-Domain Maritime Surveillance and Targeting | завершена | БПЛА |  | 1 | 0 |
| [CLASS](programs/computational-leverage-against-surveillance-systems/README.md) | Computational Leverage Against Surveillance Systems | завершена |  |  | 0 | 0 |
| [COMBAT](programs/constructive-machine-learning-battles-with-adversary-tactics/README.md) | COnstructive Machine-learning Battles with Adversary Tactics | завершена | тактика и стратегия |  | 1 | 0 |
| [CommEx](programs/communications-under-extreme-rf-spectrum-conditions/README.md) | Communications Under Extreme RF Spectrum Conditions | завершена |  |  | 0 | 0 |
| [COMPASS](programs/collection-and-monitoring-via-planning-for-active-situational-scenarios/README.md) | Collection and Monitoring via Planning for Active Situational Scenarios | завершена |  |  | 0 | 0 |
| [CONCERTO](programs/converged-collaborative-elements-for-rf-task-operations/README.md) | CONverged Collaborative Elements for RF Task Operations | завершена |  |  | 4 | 0 |
| [CREATE](programs/context-reasoning-for-autonomous-teaming/README.md) | Context Reasoning for Autonomous Teaming | завершена |  |  | 0 | 0 |
| [DAIRS](programs/defense-applications-of-innovative-remote-sensing/README.md) | Defense Applications of Innovative Remote Sensing | действует |  | Frank Robey | 1 | 0 |
| [DASH](programs/distributed-agile-submarine-hunting/README.md) | Distributed Agile Submarine Hunting | завершена | БПЛА |  | 1 | 0 |
| [DBM](programs/distributed-battle-management/README.md) | Distributed Battle Management | завершена | программное обеспечение специального назначения |  | 1 | 0 |
| [DISCORD](programs/discord/README.md) | Disruption through Intelligent Strategies, Counter Options, and Resilient Defenses | действует | тактика и стратегия | Eric Davis | 0 | 0 |
| [DyNAMO](programs/dynamic-network-adaptation-for-mission-optimization/README.md) | Dynamic Network Adaptation for Mission Optimization | завершена |  |  | 0 | 0 |
| [Fixed Wireless at a Distance](programs/fixed-wireless-at-a-distance/README.md) | Fixed Wireless at a Distance | завершена | средства связи и коммуникаций |  | 0 | 0 |
| [FLUID](programs/fluid/README.md) | FLUID | действует |  | Tamer Refaei | 0 | 0 |
| [Frosty](programs/frosty/README.md) | Frosty | действует |  | Frank Robey | 0 | 0 |
| [Gamebreaker](programs/gamebreaker/README.md) | Gamebreaker | завершена | тактика и стратегия |  | 0 | 0 |
| [GCA](programs/geospatial-cloud-analytics/README.md) | Geospatial Cloud Analytics | завершена |  |  | 1 | 0 |
| [GeCCO](programs/generating-communication-channels-to-operate/README.md) | Generating Communication Channels to Operate | действует |  | Tamer Refaei | 2 | 0 |
| [HELLADS](programs/high-energy-liquid-laser-area-defense-system/README.md) | High Energy Liquid Laser Area Defense System | завершена | авиация |  | 1 | 0 |
| [Hunter](programs/hunter/README.md) | Hunter | завершена | БПЛА |  | 1 | 0 |
| [Integrated Sensor is Structure](programs/integrated-sensor-is-structure/README.md) | Integrated Sensor is Structure | завершена |  |  | 1 | 0 |
| [LASSO](programs/lunar-assay-small-satellite-orbiter/README.md) | Lunar Assay via Small Satellite Orbiter | действует |  | Steven Chambers | 1 | 0 |
| [LOGIC](programs/logic-operating-guidelines/README.md) | Lunar Operating Guidelines for Infrastructure Consortium | действует |  | Steven Chambers | 1 | 0 |
| [LogX](programs/logx/README.md) | LogX | завершена |  |  | 2 | 0 |
| [LunA-10](programs/luna-10/README.md) | 10-Year Lunar Architecture Capability Study | завершена |  |  | 7 | 0 |
| [M-GRIN](programs/manufacturable-gradient-index-optics/README.md) | Manufacturable Gradient Index Optics | завершена |  |  | 2 | 0 |
| [MDA](programs/multi-domain-analytics/README.md) | Multi-Domain Analytics | завершена |  |  | 0 | 0 |
| [MFRF](programs/multifunction-rf/README.md) | Multifunction RF | завершена |  |  | 0 | 0 |
| [MINC](programs/mission-integrated-network-control/README.md) | Mission-Integrated Network Control | действует |  | Tamer Refaei | 1 | 0 |
| [MIST](programs/military-imaging-and-surveillance-technology/README.md) | Military Imaging and Surveillance Technology | завершена |  |  | 1 | 0 |
| [Mobile Hotspots](programs/mobile-hotspots/README.md) | Mobile Hotspots | завершена |  |  | 0 | 0 |
| [Mosaic Warfare](programs/mosaic-warfare/README.md) | Mosaic Warfare | статус не установлен |  |  | 0 | 0 |
| [NGEST](programs/next-generation-electronic-surveillance-technology/README.md) | Next Generation Electronic Surveillance Technology | действует |  | Steven Chambers | 0 | 0 |
| [Ocean of Things](programs/ocean-of-things/README.md) | Ocean of Things | завершена |  |  | 0 | 0 |
| [OPEN](programs/open-price-exploration/README.md) | Open Price Exploration for National security | действует |  | Jonathan Doyle | 1 | 0 |
| [Ouija](programs/ouija/README.md) | Ouija | действует |  | Dave Burke | 0 | 0 |
| [PIE](programs/process-intensified-energetics/README.md) | Process Intensified Energetics | действует | вооружение | Hunter Martin | 0 | 0 |
| [R2](programs/rubble-rockets-r2/README.md) | Rapid Reconstitution | действует |  | Hunter Martin | 0 | 0 |
| [Retrodirective Arrays for Coherent Transmission](programs/retrodirective-arrays/README.md) | Retrodirective Arrays for Coherent Transmission | завершена |  |  | 0 | 0 |
| [SCEPTER](programs/scepter/README.md) | Strategic Chaos Engine for Planning, Tactics, Experimentation and Resiliency | действует | тактика и стратегия | Eric Davis | 4 | 0 |
| [SHARE](programs/secure-handhelds/README.md) | Secure Handhelds on Assured Resilient networks at the tactical Edge | завершена |  |  | 2 | 0 |
| [Space-BACN](programs/space-based-adaptive-communications-node/README.md) | Space-Based Adaptive Communications Node | действует |  | John Bruzzese | 0 | 0 |
| [Space-WATCH](programs/space-domain-wide-area-tracking/README.md) | Space-domain Wide Area Tracking and Characterization | действует |  | Stefano Galli | 0 | 0 |
| [STOIC](programs/spatial-temporal-orientation-information-contested-environments/README.md) | Spatial, Temporal, and Orientation Information in Contested Environments | завершена |  |  | 0 | 0 |
| [Sync](programs/sync/README.md) | Sync | действует | БПЛА | Adam Bryant | 0 | 0 |
| [TBD2](programs/tbd2/README.md) | Track at Big Distances with Track-Before-Detect | действует |  | Stefano Galli | 0 | 0 |
| [TIM](programs/tim-transponders-ionospheric-measurement/README.md) | Transponders in Ionospheric Measurement | действует |  | Frank Robey | 0 | 0 |
| [TIMEly](programs/timely-information-for-maritime-engagements/README.md) | Timely Information for Maritime Engagements | завершена |  |  | 2 | 0 |
| [TRACE](programs/trace/README.md) | Target Recognition and Adaption in Contested Environments | завершена |  |  | 0 | 0 |
| [Trenton](programs/trenton/README.md) | Trenton | действует |  | Christine Sanders | 0 | 0 |
| [TUNA](programs/tactical-undersea-network-architectures/README.md) | Tactical Undersea Network Architectures | завершена |  |  | 2 | 0 |
| [UFP](programs/upward-falling-payloads/README.md) | Upward Falling Payloads | завершена |  |  | 1 | 0 |
| [Unison](programs/unison/README.md) | Unison | действует |  | Tamer Refaei | 0 | 0 |
| [ViSAR](programs/video-synthetic-aperture-radar/README.md) | Video Synthetic Aperture Radar | завершена |  |  | 2 | 0 |
| [Wireless Network Defense](programs/wireless-network-defense/README.md) | Wireless Network Defense | завершена |  |  | 0 | 0 |
| [XENA](programs/xena-x-ray-extreme/README.md) | X-ray Extreme-range Non-imaging Analysis | действует |  | Stefano Galli | 0 | 0 |

<a id="office-ipto"></a>

## Information Processing Techniques Office (IPTO) — обработка информации — 137

| Программа | Полное название | Статус | Сфера | Руководитель (darpa.mil) | Исполнителей | Новостей |
|---|---|---|---|---|---|---|
| [A3ML](programs/a3ml-anticipatory-adaptive/README.md) | Anticipatory and Adaptive Anti-Money Laundering | действует |  | David Dewhurst | 0 | 0 |
| [ACD](programs/active-cyber-defense/README.md) | Active Cyber Defense | завершена |  |  | 0 | 0 |
| [Active Authentication](programs/active-authentication/README.md) | Active Authentication | завершена |  |  | 1 | 0 |
| [ADAMS](programs/anomaly-detection-at-multiple-scales/README.md) | Anomaly Detection at Multiple Scales | завершена |  |  | 0 | 0 |
| [AI Next Campaign](programs/ai-next-campaign/README.md) | AI Next Campaign | завершена |  |  | 0 | 0 |
| [AIDA](programs/active-interpretation-of-disparate-alternatives/README.md) | Active Interpretation of Disparate Alternatives | завершена |  |  | 0 | 0 |
| [AIMEE](programs/artificial-intelligence-mitigations-of-emergent-execution/README.md) | Artificial Intelligence Mitigations of Emergent Execution | завершена |  |  | 0 | 0 |
| [AIxCC](programs/ai-cyber/README.md) | AI Cyber Challenge | завершена |  |  | 0 | 0 |
| [AMP](programs/assured-micropatching/README.md) | Assured Micropatching | завершена |  |  | 0 | 0 |
| [ANSR](programs/assured-neuro-symbolic-learning-and-reasoning/README.md) | Assured Neuro Symbolic Learning and Reasoning | действует |  | Susmit Jha | 1 | 0 |
| [APAC](programs/automated-program-analysis-for-cybersecurity/README.md) | Automated Program Analysis for Cybersecurity | завершена |  |  | 0 | 0 |
| [ARCOS](programs/automated-rapid-certification-of-software/README.md) | Automated Rapid Certification Of Software | действует |  | Matthew Wilding | 1 | 0 |
| [ARGUS-I](programs/autonomous-real-time-ground-ubiquitous-surveillance-infrared/README.md) | Autonomous Real-time Ground Ubiquitous Surveillance - Infrared | завершена |  |  | 0 | 0 |
| [ASED](programs/active-social-engineering-defense/README.md) | Active Social Engineering Defense | завершена |  |  | 1 | 0 |
| [ASIST](programs/artificial-social-intelligence-for-successful-teams/README.md) | Artificial Social Intelligence for Successful Teams | завершена |  |  | 7 | 0 |
| [ASKE](programs/automating-scientific-knowledge-extraction/README.md) | Automating Scientific Knowledge Extraction | завершена |  |  | 6 | 0 |
| [ASKEM](programs/automating-scientific-knowledge-extraction-modeling/README.md) | Automating Scientific Knowledge Extraction and Modeling | завершена |  |  | 6 | 0 |
| [Assured Autonomy](programs/assured-autonomy/README.md) | Assured Autonomy | завершена |  |  | 0 | 0 |
| [Big Mechanism](programs/big-mechanism/README.md) | Big Mechanism | завершена |  |  | 0 | 0 |
| [BOLT](programs/broad-operational-language-translation/README.md) | Broad Operational Language Translation | завершена |  |  | 3 | 0 |
| [BPL](programs/business-process-logic/README.md) | Business Process Logic | действует |  | David Dewhurst | 0 | 0 |
| [Brandeis](programs/brandeis/README.md) | Brandeis | завершена |  |  | 0 | 0 |
| [BRASS](programs/building-resource-adaptive-software-systems/README.md) | Building Resource Adaptive Software Systems | завершена |  |  | 0 | 0 |
| [CASE](programs/cyber-assured-systems-engineering/README.md) | Cyber Assured Systems Engineering | завершена |  |  | 3 | 0 |
| [CASTLE](programs/cyber-agents-for-security-testing-and-learning-environments/README.md) | Cyber Agents for Security Testing and Learning Environments | действует |  | Jay McNeely | 9 | 0 |
| [Causal Exploration of Complex Operational Environments](programs/causal-exploration/README.md) | Causal Exploration of Complex Operational Environments | завершена |  |  | 0 | 0 |
| [CCU](programs/computational-cultural-understanding/README.md) | Computational Cultural Understanding | действует |  | Matthew Marge | 6 | 0 |
| [CFAR](programs/cyber-fault-tolerant-attack-recovery/README.md) | Cyber Fault-tolerant Attack Recovery | завершена |  |  | 0 | 0 |
| [CGC](programs/cyber-grand-challenge/README.md) | Cyber Grand Challenge | завершена |  |  | 3 | 0 |
| [CHASE](programs/cyber-hunting-at-scale/README.md) | Cyber-Hunting At Scale | завершена |  |  | 0 | 0 |
| [CHESS](programs/computers-and-humans-exploring-software-security/README.md) | Computers and Humans Exploring Software Security | завершена |  |  | 0 | 0 |
| [Civil Sanctuary](programs/civil-sanctuary/README.md) | Civil Sanctuary | завершена |  |  | 0 | 0 |
| [ConSec](programs/configuration-security/README.md) | Configuration Security | завершена |  |  | 0 | 0 |
| [CPM](programs/compartmentalization-and-privilege-management/README.md) | Compartmentalization and Privilege Management | действует |  | Howard Shrobe | 0 | 0 |
| [CRASH](programs/clean-slate-design-of-resilient-adaptive-secure-hosts/README.md) | Clean-slate design of Resilient, Adaptive, Secure Hosts | завершена |  |  | 0 | 0 |
| [CriticalMAAS](programs/critical-mineral-assessments-with-ai-support/README.md) | Critical Mineral Assessments with AI Support | завершена |  |  | 0 | 0 |
| [CSFV](programs/crowd-sourced-formal-verification/README.md) | Crowd Sourced Formal Verification | завершена |  |  | 0 | 0 |
| [CSL](programs/cooperative-secure-learning/README.md) | Cooperative Secure Learning | завершена |  |  | 0 | 0 |
| [CSSG](programs/computer-science-study-group/README.md) | Computer Science Study Group | завершена |  |  | 4 | 0 |
| [CwC](programs/communicating-with-computers/README.md) | Communicating with Computers | завершена |  |  | 0 | 0 |
| [Cyber Education Efforts](programs/cyber-education-efforts/README.md) | Cyber Education Efforts | действует |  | Nathaniel Bastian | 0 | 0 |
| [D3M](programs/data-driven-discovery-of-models/README.md) | Data-Driven Discovery of Models | завершена |  |  | 0 | 0 |
| [DCAPS](programs/detection-and-computational-analysis-of-psychological-signals/README.md) | Detection and Computational Analysis of Psychological Signals | завершена |  |  | 0 | 0 |
| [DEFT](programs/deep-exploration-and-filtering-of-text/README.md) | Deep Exploration and Filtering of Text | завершена |  |  | 0 | 0 |
| [DICE](programs/decentralized-artificial-intelligence-through-controlled-emergence/README.md) | Decentralized Artificial Intelligence through Controlled Emergence | действует |  | Susmit Jha | 0 | 0 |
| [Dispersed Computing](programs/dispersed-computing/README.md) | Dispersed Computing | завершена |  |  | 2 | 0 |
| [E-BOSS](programs/enhanced-sbom-for-optimized-software-sustainment/README.md) | Enhanced SBOM for Optimized Software Sustainment | действует |  | Stephen Kuhn | 6 | 0 |
| [ECOLE](programs/environment-driven-conceptual-learning/README.md) | Environment-driven Conceptual Learning | завершена |  |  | 0 | 0 |
| [ECoSystemic](programs/ensuring-consistency-of-systemic-information/README.md) | Ensuring Consistency of Systemic Information | завершена |  |  | 0 | 0 |
| [EdgeCT](programs/edge-directed-cyber-technologies-for-reliable-mission-communication/README.md) | Edge-Directed Cyber Technologies for Reliable Mission Communication | завершена |  |  | 4 | 0 |
| [EMHAT](programs/exploratory-models-of-human-ai-teams/README.md) | Exploratory Models of Human-AI Teams | завершена |  |  | 0 | 0 |
| [ENGAGE](programs/engage/README.md) | ENGAGE | завершена |  |  | 0 | 0 |
| [Enhanced Attribution](programs/enhanced-attribution/README.md) | Enhanced Attribution | завершена |  |  | 1 | 0 |
| [expMath](programs/expmath-exponential-mathematics/README.md) | Exponentiating Mathematics | действует |  | Patrick Shafto | 13 | 0 |
| [FACT](programs/friction-for-accountability-in-conversational-transactions/README.md) | Friction for Accountability in Conversational Transactions | завершена |  |  | 0 | 0 |
| [FastNICs](programs/fast-network-interface-cards/README.md) | Fast Network Interface Cards | действует |  | John-Francis Mergen | 2 | 0 |
| [FoundSci](programs/foundation-models-for-scientific-discovery/README.md) | Foundation Models for Scientific Discovery | завершена |  |  | 0 | 0 |
| [GAILA](programs/grounded-artificial-intelligence-language-acquisition/README.md) | Grounded Artificial Intelligence Language Acquisition | завершена |  |  | 0 | 0 |
| [GARD](programs/guaranteeing-ai-robustness-against-deception/README.md) | Guaranteeing AI Robustness Against Deception | завершена |  |  | 14 | 0 |
| [HACCS](programs/harnessing-autonomy-for-countering-cyberadversary-systems/README.md) | Harnessing Autonomy for Countering Cyberadversary Systems | завершена |  |  | 7 | 0 |
| [HACMS](programs/high-assurance-cyber-military-systems/README.md) | High-Assurance Cyber Military Systems | завершена |  |  | 1 | 0 |
| [HARDEN](programs/hardening-development-toolchains-against-emergent-execution-engines/README.md) | Hardening Development Toolchains Against Emergent Execution Engines | действует |  | Derek Bernsen | 0 | 0 |
| [ICAS](programs/integrated-cyber-analysis-system/README.md) | Integrated Cyber Analysis System | завершена |  |  | 0 | 0 |
| [ICS](programs/intrinsic-cognitive-security/README.md) | Intrinsic Cognitive Security | действует |  | Matthew Wilding | 3 | 0 |
| [IDAS](programs/intent-defined-adaptive-software/README.md) | Intent-Defined Adaptive Software | завершена |  |  | 0 | 0 |
| [IMR](programs/intrinsic-market-resilience-imr/README.md) | Intrinsic Market Resilience | действует |  | Matthew Wilding | 0 | 0 |
| [INCAS](programs/influence-campaign-awareness-and-sensemaking/README.md) | Influence Campaign Awareness and Sensemaking | завершена |  |  | 7 | 0 |
| [INGOTS](programs/intelligent-generation-tools-security/README.md) | Intelligent Generation of Tools for Security | действует |  | Derek Bernsen | 5 | 0 |
| [Insight](programs/insight/README.md) | Insight | завершена |  |  | 0 | 0 |
| [ITM](programs/in-the-moment/README.md) | In the Moment | действует |  | Patrick Shafto | 2 | 0 |
| [KAIROS](programs/knowledge-directed-artificial-intelligence-reasoning-over-schemas/README.md) | Knowledge-directed Artificial Intelligence Reasoning Over Schemas | завершена |  |  | 0 | 0 |
| [LADS](programs/leveraging-the-analog-domain-for-security/README.md) | Lifelong Learning Machines | завершена |  |  | 2 | 0 |
| [LINC](programs/learning-introspective-control/README.md) | Learning Introspective Control | действует | БПЛА | John-Francis Mergen | 0 | 0 |
| [LORELEI](programs/low-resource-languages-for-emergent-incidents/README.md) | Low Resource Languages for Emergent Incidents | завершена |  |  | 11 | 0 |
| [LUC](programs/lightweight-universal-codec/README.md) | Lightweight Universal Codec | действует |  | Allyson O’Brien | 0 | 0 |
| [LUCID](programs/lucid/README.md) | Logic Understanding for Complex Information Dissemination | действует |  | Byron Cook | 1 | 0 |
| [LwLL](programs/learning-with-less-labeling/README.md) | Learning with Less Labeling | завершена |  |  | 0 | 0 |
| [MAA](programs/modeling-adversarial-activity/README.md) | Modeling Adversarial Activity | завершена |  |  | 0 | 0 |
| [MADCAT](programs/multilingual-automatic-document-classification-analysis-and-translation/README.md) | Multilingual Automatic Document Classification, Analysis and Translation | завершена |  |  | 1 | 0 |
| [MCS](programs/machine-common-sense/README.md) | Machine Common Sense | завершена |  |  | 0 | 0 |
| [MediFor](programs/media-forensics/README.md) | Media Forensics | завершена |  |  | 2 | 0 |
| [Memex](programs/memex/README.md) | Memex | завершена |  |  | 0 | 0 |
| [MICE](programs/measuring-the-information-control-environment/README.md) | Measuring the Information Control Environment | завершена |  |  | 0 | 0 |
| [MIPs](programs/modeling-influence-pathways/README.md) | Modeling Influence Pathways | завершена |  |  | 0 | 0 |
| [ML2P](programs/mapping-machine-learning-physics/README.md) | Mapping Machine Learning to Physics | действует |  | Matthew Marge | 0 | 0 |
| [MOCHA](programs/mocha-machine-learning/README.md) | Machine Learning and Optimization-guided Compilers for Heterogeneous Architectures | действует |  | Howard Shrobe | 3 | 0 |
| [MRC](programs/mission-oriented-resilient-clouds/README.md) | Mission-oriented Resilient Clouds | завершена |  |  | 0 | 0 |
| [MUSE](programs/mining-and-understanding-software-enclaves/README.md) | Mining and Understanding Software Enclaves | завершена |  |  | 0 | 0 |
| [NASCENT](programs/nascent-national-security-economic-theory/README.md) | National Security Economic Theory | действует |  | David Dewhurst | 1 | 0 |
| [OPS-5G](programs/open-programmable-secure-5g/README.md) | Open, Programmable, Secure 5G | действует |  | Allyson O’Brien | 5 | 0 |
| [PEARLS](programs/proof-engineering-adaptation-repair-and-learning-for-software/README.md) | Proof Engineering, Adaptation, Repair, and Learning for Software | завершена |  |  | 0 | 0 |
| [Plan X](programs/plan-x/README.md) | Plan X | завершена |  |  | 0 | 0 |
| [PPAML](programs/probabilistic-programming-for-advancing-machine-learning/README.md) | Probabilistic Programming for Advancing Machine Learning | завершена |  |  | 0 | 0 |
| [PROCEED](programs/programming-computation-on-encrypted-data/README.md) | PROgramming Computation on EncryptEd Data | завершена |  |  | 0 | 0 |
| [PROVERS](programs/pipelined-reasoning-of-verifiers-enabling-robust-systems/README.md) | Pipelined Reasoning of Verifiers Enabling Robust Systems | действует |  | Xenofon Koutsoukos | 0 | 0 |
| [PTG](programs/perceptually-enabled-task-guidance/README.md) | Perceptually-enabled Task Guidance | завершена |  |  | 9 | 0 |
| [PWND2](programs/provably-weird-network/README.md) | Provably Weird Network Deployment and Detection | действует |  | Michael Lack | 5 | 0 |
| [QCR](programs/quantitative-crisis-response/README.md) | Quantitative Crisis Response | завершена |  |  | 0 | 0 |
| [QED for RML](programs/quantifying-ensemble-diversity-for-robust-machine-learning/README.md) | Quantifying Ensemble Diversity for Robust Machine Learning | завершена |  |  | 0 | 0 |
| [QuANET](programs/quantum-augmented-network/README.md) | Quantum-Augmented Network | действует |  | Allyson O’Brien | 2 | 0 |
| [RACE](programs/resilient-anonymous-communication/README.md) | Resilient Anonymous Communication for Everyone | действует |  | Michael Lack | 0 | 0 |
| [RADICS](programs/rapid-attack-detection/README.md) | Rapid Attack Detection, Isolation and Characterization Systems | завершена |  |  | 0 | 0 |
| [RATS](programs/robust-automatic-transcription-of-speech/README.md) | Robust Automatic Transcription of Speech | завершена |  |  | 2 | 0 |
| [RED](programs/reverse-engineering-of-deceptions/README.md) | Reverse Engineering of Deceptions | завершена |  |  | 0 | 0 |
| [Red-C](programs/red-c-reclaiming/README.md) | Reclaiming Bus-based Systems During Compromise | действует |  | Derek Bernsen | 0 | 0 |
| [ReMath](programs/recovery-symbolic-mathematics-from-code/README.md) | Recovery of Symbolic Mathematics from Code | завершена |  |  | 0 | 0 |
| [REPO](programs/reduction-entropy/README.md) | Reduction of Entropy for Probabilistic Organization | завершена |  |  | 0 | 0 |
| [RSDN](programs/resilient-supply-demand/README.md) | Resilient Supply-and-Demand Networks | действует |  | David Dewhurst | 6 | 0 |
| [SABER](programs/saber/README.md) | Securing Autonomy for Battlefield Effective Robustness | действует |  | Nathaniel Bastian | 2 | 0 |
| [SafeDocs](programs/safe-documents/README.md) | Safe Documents | завершена |  |  | 7 | 0 |
| [SAFER](programs/safer-warfighter-communications/README.md) | Safer Warfighter Communications | завершена |  |  | 0 | 0 |
| [SafeWare](programs/safeware/README.md) | SafeWare | завершена |  |  | 0 | 0 |
| [SciFy](programs/scientific-feasibility/README.md) | Scientific Feasibility | действует |  | Victoria Romero | 5 | 0 |
| [SD2](programs/synergistic-discovery-and-design/README.md) | Synergistic Discovery and Design | завершена |  |  | 2 | 0 |
| [SDCPS](programs/symbiotic-design-cyber-physical-systems/README.md) | Symbiotic Design for Cyber Physical Systems | завершена |  |  | 0 | 0 |
| [Searchlight](programs/searchlight/README.md) | Searchlight | завершена |  |  | 0 | 0 |
| [SemaFor](programs/semantic-forensics/README.md) | Semantic Forensics | завершена |  |  | 5 | 0 |
| [SI Forge](programs/si-forge/README.md) | SI Forge | действует |  | Matthew Marge | 0 | 0 |
| [SIEVE](programs/securing-information-for-encrypted-verification-and-evaluation/README.md) | Securing Information for Encrypted Verification and Evaluation | завершена |  |  | 8 | 0 |
| [SIQ](programs/siq-super-intelligence-quantified/README.md) | Super Intelligence Quantified | действует |  | Patrick Shafto | 0 | 0 |
| [SMISC](programs/social-media-in-strategic-communication/README.md) | Social Media in Strategic Communication | завершена |  |  | 0 | 0 |
| [SMOKE](programs/signature-management-using-operational-knowledge/README.md) | Signature Management using Operational Knowledge and Environments | действует |  | Derek Bernsen | 3 | 0 |
| [SocialCyber](programs/hybrid-ai-to-protect-integrity-of-open-source-code/README.md) | Hybrid AI to Protect Integrity of Open Source Code | завершена |  |  | 0 | 0 |
| [SocialSim](programs/computational-simulation-of-online-social-behavior/README.md) | Social Simulation for Evaluating Online Messaging Campaigns | завершена |  |  | 0 | 0 |
| [STAC](programs/space-time-analysis-cybersecurity/README.md) | Space/Time Analysis for Cybersecurity | завершена |  |  | 0 | 0 |
| [TC](programs/transparent-computing/README.md) | Transparent Computing | завершена |  |  | 0 | 0 |
| [TRACTOR](programs/translating-all-c-to-rust/README.md) | Translating All C to Rust | действует |  | Stephen Kuhn | 0 | 0 |
| [TransApps](programs/transformative-apps/README.md) | Transformative Apps | завершена |  |  | 3 | 0 |
| [Transfer from Imprecise and Abstract Models to Autonomous Technologies](programs/transfer-from-imprecise/README.md) | Transfer from Imprecise and Abstract Models to Autonomous Technologies | действует |  | Susmit Jha | 0 | 0 |
| [V-SPELLS](programs/verified-security-and-performance-enhancement-of-large-legacy-software/README.md) | Verified Security and Performance Enhancement of Large Legacy Software | завершена |  |  | 0 | 0 |
| [VET](programs/vetting-commodity-it-software-and-firmware/README.md) | Vetting Commodity IT Software and Firmware | завершена |  |  | 0 | 0 |
| [VMR](programs/visual-media-reasoning/README.md) | Visual Media Reasoning | завершена |  |  | 0 | 0 |
| [WASH](programs/warfighter-analytics-using-smartphones-for-health/README.md) | Warfighter Analytics using Smartphones for Health | завершена |  |  | 0 | 0 |
| [World Modelers](programs/world-modelers/README.md) | World Modelers | завершена |  |  | 0 | 0 |
| [XAI](programs/explainable-artificial-intelligence/README.md) | Explainable Artificial Intelligence | завершена |  |  | 0 | 0 |
| [XD3](programs/extreme-ddos-defense/README.md) | Extreme DDoS Defense | завершена |  |  | 6 | 0 |
| [XDATA](programs/xdata/README.md) | XDATA | завершена |  |  | 0 | 0 |

<a id="office-mxo"></a>

## Multi X Office (MXO; расширение Microsystems Technology Office, MTO) — 128

| Программа | Полное название | Статус | Сфера | Руководитель (darpa.mil) | Исполнителей | Новостей |
|---|---|---|---|---|---|---|
| [3DSoC](programs/three-dimensional-monolithic-system-on-a-chip/README.md) | Three Dimensional Monolithic System-on-a-Chip | завершена |  |  | 1 | 0 |
| [A-PhI](programs/atomic-photonic-integration/README.md) | Atomic-Photonic Integration | завершена |  |  | 0 | 0 |
| [A-to-I](programs/analog-to-information-a-to-i-look-through/README.md) | Analog-to-Information | завершена |  |  | 0 | 0 |
| [ACES](programs/atomic-clock-with-enhanced-stability/README.md) | Atomic Clock with Enhanced Stability | завершена |  |  | 5 | 0 |
| [ACT](programs/arrays-at-commercial-timescales/README.md) | Arrays at Commercial Timescales | завершена |  |  | 2 | 0 |
| [AISS](programs/automatic-implementation-of-secure-silicon/README.md) | Automatic Implementation of Secure Silicon | завершена |  |  | 1 | 0 |
| [AMBIIENT](programs/atomic-magnetometer-for-biological-imaging-in-earths-native-terrain/README.md) | Atomic Magnetometer for Biological Imaging In Earth’s Native Terrain | завершена |  |  | 0 | 0 |
| [AMME](programs/amme-additive-manufacturing/README.md) | Additive Manufacturing of MicrosystEms | действует |  | David Meyer | 0 | 0 |
| [AMPED](programs/amped/README.md) | Area-Multiplied Photonic-crystal Enhanced Devices | действует |  | David Meyer | 0 | 1 |
| [APM](programs/apm/README.md) | Atomically Precise Molecules | действует |  | John M. Hoffman | 0 | 0 |
| [ARC](programs/adaptive-radar-countermeasures/README.md) | Adaptive Radar Countermeasures | завершена |  |  | 5 | 0 |
| [ART](programs/adaptive-rf-technologies/README.md) | Adaptive RF Technology | завершена |  |  | 0 | 0 |
| [ASSERT](programs/assert-alternative-sources/README.md) | Advanced Sources for Single-event Effects Radiation Testing | действует |  | Thomas Schratwieser | 2 | 0 |
| [ATOM](programs/accelerating-discovery-of-tunable-optical-material/README.md) | Accelerating Discovery of Tunable Optical Materials | завершена |  |  | 0 | 0 |
| [AWARE](programs/advanced-wide-fov-architectures-for-image-reconstruction-and-exploitation/README.md) | Advanced Wide FOV Architectures for Image Reconstruction and Exploitation | завершена |  |  | 0 | 0 |
| [BLADE](programs/behavioral-learning-for-adaptive-electronic-warfare/README.md) | Behavioral Learning for Adaptive Electronic Warfare | завершена | БПЛА |  | 1 | 0 |
| [CHIPS](programs/common-heterogeneous-integration-and-ip-reuse-strategies/README.md) | Common Heterogeneous Integration and IP Reuse Strategies | завершена |  |  | 3 | 0 |
| [CIDAR](programs/cidar-computational-imaging/README.md) | Computational Imaging Detection and Ranging Challenge | завершена |  |  | 0 | 0 |
| [COFFEE](programs/compact-front-end-filters-at-the-element-level/README.md) | Compact Front-End Filters at the Element-Level | действует |  | Todd Bauer | 5 | 0 |
| [COOP](programs/coop-continuous-correctness/README.md) | Continuous-correctness On Opaque Processors | завершена |  |  | 2 | 0 |
| [COSMOS](programs/compound-semiconductor-materials-on-silicon/README.md) | Compound Semiconductor Materials on Silicon | завершена |  |  | 0 | 0 |
| [COSMOS](programs/cosmos/README.md) | COSMOS | завершена |  |  | 0 | 0 |
| [CRAFT](programs/circuit-realization-at-faster-timescales/README.md) | Circuit Realization at Faster Timescales | завершена |  |  | 4 | 0 |
| [Crystal Palace](programs/crystal-palace/README.md) | Crystal Palace | действует |  | Huanan Zhang | 0 | 0 |
| [DAHI](programs/diverse-accessible-heterogeneous-integration/README.md) | Diverse Accessible Heterogeneous Integration | завершена |  |  | 1 | 0 |
| [DAHI - E-PHI](programs/dahi-electronic-photonic-heterogenous-integration/README.md) | Electronic-Photonic Heterogeneous Integration | завершена |  |  | 0 | 0 |
| [DAHI - Foundry Technology](programs/dahi-foundry-technology/README.md) | DAHI - Foundry Technology | завершена |  |  | 0 | 0 |
| [DISARMER](programs/direct-sampling-digital-receiver/README.md) | Direct Sampling Digital Receiver | завершена |  |  | 1 | 0 |
| [DODOS](programs/direct-on-chip-digital-optical-synthesizer/README.md) | Direct On-Chip Digital Optical Synthesizer | завершена |  |  | 4 | 0 |
| [DPRIVE](programs/data-protection-in-virtual-environments/README.md) | Data Protection in Virtual Environments | завершена |  |  | 3 | 0 |
| [DRBE](programs/digital-rf-battlespace-emulator/README.md) | Digital RF Battlespace Emulator | действует | БПЛА | Anna Tauke-Pedretti | 0 | 0 |
| [DREaM](programs/dynamic-range-enhanced-electronics-and-materials/README.md) | Dynamic Range-enhanced Electronics and Materials | завершена |  |  | 0 | 0 |
| [DSSoC](programs/domain-specific-system-on-chip/README.md) | Domain-Specific System on Chip | завершена |  |  | 1 | 0 |
| [ELASTx-ICs](programs/efficient-linearized-all-silicon-transmitter-ics/README.md) | Efficient Linearized All-Silicon Transmitter ICs | завершена |  |  | 0 | 0 |
| [ELGAR](programs/electronics-for-g-band-arrays/README.md) | Electronics for G-band Arrays | действует |  | David Meyer | 4 | 0 |
| [ENVision](programs/envision/README.md) | Enhanced Night Vision in Eyeglass Form | завершена |  |  | 7 | 0 |
| [EXCALIBUR](programs/excalibur/README.md) | EXCALIBUR | завершена |  |  | 0 | 0 |
| [FENCE](programs/fast-event-based-neuromorphic-camera-and-electronics/README.md) | Fast Event-based Neuromorphic Camera and Electronics | действует |  | Timothy Klausutis | 3 | 0 |
| [FIRE](programs/faithful-integrated-reverse-engineering-and-exploitation/README.md) | Faithful Integrated Reverse-engineering and Exploitation | действует |  | Jonathan Hoffman | 0 | 0 |
| [FOCII](programs/focal-arrays-for-curved-infrared-imagers/README.md) | Focal arrays for Curved Infrared Imagers | действует |  | Thomas Schratwieser | 0 | 0 |
| [FRANC](programs/foundations-required-for-novel-compute/README.md) | Foundations Required for Novel Compute | завершена |  |  | 0 | 0 |
| [GAPS](programs/guaranteed-architecture-for-physical-security/README.md) | Guaranteed Architecture for Physical Security | завершена |  |  | 6 | 0 |
| [GENII](programs/gain-enhancement-by-novel-impact-ionization/README.md) | Gain Enhancement by Novel Impact Ionization | завершена |  |  | 0 | 0 |
| [GRYPHON](programs/generating-rf-with-photonic-oscillators/README.md) | Generating RF with Photonic Oscillators for Low Noise | завершена |  |  | 7 | 0 |
| [H2](programs/heterogeneous-heterostructures/README.md) | Heterogeneous Heterostructures | завершена |  |  | 0 | 0 |
| [H6](programs/h6/README.md) | H6 | действует |  | Travis Autry | 0 | 0 |
| [HAPPI](programs/happi-heterogeneous/README.md) | Heterogeneous Adaptively Produced Photonic Interfaces | действует |  | Anna Tauke-Pedretti | 4 | 0 |
| [HARQ](programs/heterogeneous-architectures-for-quantum/README.md) | Heterogeneous Architectures for Quantum | действует |  | Justin Cohen | 0 | 0 |
| [HAVOC](programs/high-power-amplifier-using-vacuum-electronics-for-overmatch-capability/README.md) | High power Amplifier using Vacuum electronics for Overmatch Capability | завершена |  |  | 3 | 0 |
| [HEALICs](programs/self-healing-mixed-signal-integrated-circuits/README.md) | Self-HEALing Mixed-Signal Integrated Circuits | завершена |  |  | 0 | 0 |
| [HERMES](programs/hyper-wideband-enabled-rf-messaging/README.md) | Hyper-wideband Enabled RF Messaging | завершена | БПЛА |  | 1 | 0 |
| [HiFIVE](programs/high-frequency-integrated-vacuum-electronics/README.md) | High Frequency Integrated Vacuum Electronics | завершена |  |  | 0 | 0 |
| [HIVE](programs/hierarchical-identify-verify-exploit/README.md) | Hierarchical Identify Verify Exploit | завершена | тактика и стратегия |  | 1 | 0 |
| [HOTS](programs/hots-high-operational/README.md) | High Operational Temperature Sensors | завершена |  |  | 4 | 0 |
| [ICECool](programs/intrachip-interchip-enhanced-cooling/README.md) | Intrachip/Interchip Enhanced Cooling | завершена |  |  | 1 | 0 |
| [IDEA](programs/intelligent-design-of-electronic-assets/README.md) | Intelligent Design of Electronic Assets | завершена |  |  | 1 | 0 |
| [INSPIRED](programs/intensity-squeezed-photonic/README.md) | Intensity-Squeezed Photonic Integration for Revolutionary Detectors | действует |  | Justin Cohen | 3 | 0 |
| [IRIS](programs/integrity-and-reliability-of-integrated-circuits/README.md) | Integrity and Reliability of Integrated Circuits | завершена |  |  | 9 | 0 |
| [JUMP](programs/joint-university-microelectronics-program/README.md) | Joint University Microelectronics Program | завершена |  |  | 2 | 0 |
| [JUMP 2.0](programs/jump/README.md) | Joint University Microelectronics Program | действует |  | Jonathan Hoffman | 2 | 0 |
| [L2M](programs/lifelong-learning-machines/README.md) | Lifelong Learning Machines | завершена |  |  | 1 | 0 |
| [LCTI-M](programs/low-cost-thermal-imager-manufacturing/README.md) | Low Cost Thermal Imager - Manufacturing | завершена |  |  | 2 | 0 |
| [LOTS](programs/limits-of-thermal-sensors/README.md) | Limits of Thermal Sensors | завершена |  |  | 0 | 0 |
| [LTLT](programs/low-temperature-logic-technology/README.md) | Low Temperature Logic Technology | завершена |  |  | 0 | 0 |
| [LUMOS](programs/lasers-for-universal-microscale-optical-systems/README.md) | Lasers for Universal Microscale Optical Systems | действует |  | Anna Tauke-Pedretti | 8 | 0 |
| [LUSTER](programs/laser-uv-sources-for-tactical-efficient-raman/README.md) | Laser UV Sources for Tactical Efficient Raman | завершена |  |  | 3 | 0 |
| [M-STUDIO](programs/m-studio-material-synthesis/README.md) | Material Synthesis Technologies for Universal and Diverse Integration Opportunities | действует |  | Huanan Zhang | 3 | 0 |
| [M3IC](programs/magnetic-miniaturized-and-monolithically-integrated-components/README.md) | Magnetic Miniaturized and Monolithically Integrated Components | завершена | БПЛА |  | 0 | 0 |
| [Macaroni](programs/macaroni/README.md) | Macaroni | действует |  | David Meyer | 0 | 0 |
| [MagHITS](programs/magnetic-high-temperature-sensors/README.md) | Magnetic High Temperature Sensors | завершена |  |  | 0 | 0 |
| [MAX](programs/massive-cross-correlation/README.md) | Massive Cross-Correlation | завершена |  |  | 0 | 0 |
| [MELT](programs/modular-efficient-laser-technology/README.md) | Modular Efficient Laser Technology | действует |  | Thomas Schratwieser | 2 | 0 |
| [Meso](programs/mesodynamic-architectures/README.md) | Mesodynamic Architectures | завершена |  |  | 0 | 0 |
| [MGM](programs/millimeter-wave-gan-maturation/README.md) | Millimeter Wave GaN Maturation | завершена |  |  | 0 | 0 |
| [MICA](programs/microsystem-induced/README.md) | Microsystem Induced CAtalysis | действует |  | Todd Bauer | 5 | 0 |
| [Micro-PNT](programs/micro-technology-for-positioning-navigation-and-timing/README.md) | Micro-Technology for Positioning, Navigation and Timing | завершена |  |  | 0 | 0 |
| [Microsystems Exploration](programs/microsystems-exploration/README.md) | Microsystems Exploration | действует |  | Whitney Mason | 0 | 0 |
| [MIDAS](programs/millimeter-wave-digital-arrays/README.md) | Millimeter Wave Digital Arrays | завершена |  |  | 2 | 0 |
| [Minitherms3D](programs/Minitherms3D/README.md) | Minitherms3D | действует |  | Jeffrey Daulton | 3 | 0 |
| [N-ZERO](programs/near-zero-rf-and-sensor-operations/README.md) | Near Zero Power RF and Sensor Operations | завершена |  |  | 6 | 0 |
| [OPTIMA](programs/optimum-processing-technology-inside-memory-arrays/README.md) | Optimum Processing Technology Inside Memory Arrays | действует |  | Todd Bauer | 1 | 0 |
| [ORCHID](programs/optical-radiation-cooling-and-heating-in-integrated-devices/README.md) | Optical Radiation Cooling and Heating in Integrated Devices | завершена |  |  | 0 | 0 |
| [PALADIN&T](programs/test-and-evaluation/README.md) | Platform for Acquisition, Logging, and Analysis of Devices for Inertial Navigation and Timing | завершена |  |  | 0 | 0 |
| [PERFECT](programs/power-efficiency-revolution-for-embedded-computing-technologies/README.md) | Power Efficiency Revolution for Embedded Computing Technologies | завершена |  |  | 7 | 0 |
| [Perrseus](programs/perrseus/README.md) | Perrseus | действует |  | Travis Autry | 0 | 1 |
| [PICASSO](programs/picasso/README.md) | Photonic Integrated Circuit Architectures for Scalable System Objectives | действует |  | Anna Tauke-Pedretti | 0 | 0 |
| [PIPES](programs/photonics-in-the-package-for-extreme-scalability/README.md) | Photonics in the Package for Extreme Scalability | действует |  | Anna Tauke-Pedretti | 5 | 0 |
| [PIXNET](programs/pixel-network-for-dynamic-visualization/README.md) | Pixel Network for Dynamic Visualization | завершена |  |  | 1 | 0 |
| [POEM](programs/photonically-optimized-embedded-microprocessors/README.md) | Photonically Optimized Embedded Microprocessors | завершена |  |  | 0 | 0 |
| [PRIGM](programs/precise-robust-inertial-guidance-for-munitions/README.md) | Precise Robust Inertial Guidance for Munitions | завершена | вооружение |  | 1 | 0 |
| [Promethean Clay](programs/promethean-clay/README.md) | Promethean Clay | действует |  | Thomas Schratwieser | 1 | 0 |
| [PROSE](programs/protein-sequencing-prose/README.md) | PROtein SEquencing | действует |  | John M. Hoffman | 0 | 0 |
| [Protein Palace](programs/protein-palace/README.md) | Protein Palace | действует |  | Huanan Zhang | 0 | 0 |
| [PROWESS](programs/processor-reconfiguration-for-wideband-spectrum-sensing/README.md) | Processor Reconfiguration for Wideband Spectrum Sensing | завершена |  |  | 3 | 0 |
| [QA](programs/quantum-apertures/README.md) | Quantum Apertures | завершена |  |  | 0 | 0 |
| [QB](programs/quantum-benchmarking/README.md) | Quantum Benchmarking | завершена |  |  | 0 | 0 |
| [QBI](programs/qbi/README.md) | Quantum Benchmarking Initiative | действует |  | Micah Stoutimore | 11 | 0 |
| [QuIVER](programs/quantum-imaging-of-vector-electromagnetic-radiation/README.md) | Quantum Imaging of Vector Electromagnetic Radiation | действует |  | Jonathan Hoffman | 0 | 0 |
| [RAAPTR](programs/raaptr/README.md) | RF Architectures Applying Photonic Timing and Routing | действует | БПЛА | Justin Cohen | 0 | 0 |
| [ReImagine](programs/reconfigurable-imaging/README.md) | Reconfigurable Imaging | завершена |  |  | 5 | 0 |
| [RFMLS](programs/radio-frequency-machine-learning-systems/README.md) | Radio Frequency Machine Learning Systems | завершена |  |  | 1 | 0 |
| [RoQS](programs/roqs-robust-quantum-sensors/README.md) | Robust Quantum Sensors | действует |  | Travis Autry | 0 | 1 |
| [RTML](programs/real-time-machine-learning/README.md) | Real Time Machine Learning | завершена |  |  | 0 | 0 |
| [SC2](programs/spectrum-collaboration-challenge/README.md) | Spectrum Collaboration Challenge | завершена |  |  | 0 | 0 |
| [ScAN](programs/scan/README.md) | Scalable Analog Neural-networks | действует |  | Jason Chou | 0 | 0 |
| [SDH](programs/software-defined-hardware/README.md) | Software Defined Hardware | завершена |  |  | 1 | 0 |
| [SHIELD](programs/supply-chain-hardware-integrity-for-electronics-defense/README.md) | Supply Chain Hardware Integrity for Electronics Defense | завершена |  |  | 5 | 0 |
| [Smash](programs/smash/README.md) | Smash | действует |  | Julian McMorrow | 0 | 0 |
| [SOAP](programs/soap-scalable-on-array/README.md) | Scalable On-Array Processing | действует |  | Anna Tauke-Pedretti | 0 | 0 |
| [SOAR](programs/steerable-optical-aperture-receivers/README.md) | Steerable Optical Aperture Receivers | завершена |  |  | 0 | 0 |
| [SPCE](programs/spce-space-power/README.md) | Space Power Conversion Electronics | действует |  | Julian McMorrow | 0 | 0 |
| [Spectrum Challenge](programs/spectrum-challenge/README.md) | Spectrum Challenge | завершена |  |  | 1 | 0 |
| [SSITH](programs/ssith/README.md) | System Security Integration Through Hardware and Firmware | завершена |  |  | 10 | 0 |
| [STARnet](programs/starnet/README.md) | Semiconductor Technology Advanced Research Network | завершена |  |  | 0 | 0 |
| [T-MUSIC](programs/technologies-for-mixed-mode-ultra-scaled-integrated-circuits/README.md) | Technologies for Mixed-mode Ultra Scaled Integrated Circuits | завершена |  |  | 0 | 0 |
| [THREADS](programs/threads-heat-removal/README.md) | Technologies for Heat Removal in Electronics at the Device Scale | действует |  | Jeffrey Daulton | 2 | 0 |
| [THz Electronics](programs/thz-electronics/README.md) | THz Electronics | завершена |  |  | 1 | 0 |
| [TMT](programs/thermal-management-technologies/README.md) | Thermal Management Technologies | завершена |  |  | 0 | 0 |
| [TROPHY](programs/transmit-and-receive-optimized-photonics/README.md) | Transmit and Receive Optimized Photonics | завершена |  |  | 0 | 0 |
| [TRUST](programs/trusted-integrated-circuits/README.md) | Trusted Integrated Circuits | завершена |  |  | 0 | 0 |
| [TUFEN](programs/tunable-ferroelectric-nitrides/README.md) | Tunable Ferroelectric Nitrides | завершена |  |  | 0 | 0 |
| [TWEED](programs/traveling-wave-energy-enhancement-devices/README.md) | Traveling-Wave Energy Enhancement Devices | завершена |  |  | 0 | 0 |
| [US2QC](programs/us2qc/README.md) | Underexplored Systems for Utility-Scale Quantum Computing | действует |  | Micah Stoutimore | 4 | 0 |
| [UWBGS](programs/uwbgs-band-gap/README.md) | Ultra-Wide Band Gap Semiconductors | действует |  | David Meyer | 2 | 0 |
| [WARDEN](programs/waveform-agile-radio-frequency-directed-energy/README.md) | Waveform Agile Radio-frequency Directed ENergy | действует | БПЛА | Julian McMorrow | 5 | 0 |
| [WARP](programs/wideband-adaptive-rf-protection/README.md) | Wideband Adaptive RF Protection | действует | средства связи и коммуникаций | Todd Bauer | 0 | 0 |
| [WIRED](programs/wafer-scale-infrared-detectors/README.md) | Wafer Scale Infrared Detectors | завершена |  |  | 0 | 0 |
| [WiSPER](programs/wisper-wideband-secure/README.md) | Wideband Secure and Protected Emitter and Receiver | действует |  | Michael Sangillo | 3 | 0 |

<a id="office-dso"></a>

## Defense Sciences Office (DSO) — оборонные науки — 137

| Программа | Полное название | Статус | Сфера | Руководитель (darpa.mil) | Исполнителей | Новостей |
|---|---|---|---|---|---|---|
| [A-Teams](programs/agile-teams/README.md) | Agile Teams | завершена |  |  | 2 | 0 |
| [A2P](programs/atoms-to-product/README.md) | Atoms to Product | завершена |  |  | 1 | 0 |
| [ACCEL](programs/advanced-concept-compact-electron-linear-accelerator/README.md) | Advanced Concept Compact Electron Linear-accelerator | завершена |  |  | 0 | 0 |
| [ACCESS](programs/accelerated-computation/README.md) | Accelerated Computation for Efficient Scientific Simulation | завершена |  |  | 2 | 0 |
| [ACDC](programs/agnostic-compact-demilitarization-of-chemical-agents/README.md) | Agnostic Compact Demilitarization of Chemical Agents | завершена |  |  | 1 | 0 |
| [ACTM](programs/ai-assisted-climate-tipping-point-modeling/README.md) | AI-assisted Climate Tipping-point Modeling | завершена |  |  | 0 | 0 |
| [AIRA](programs/artificial-intelligence-research-associate/README.md) | Artificial Intelligence Research Associate | завершена |  |  | 0 | 0 |
| [AMD](programs/accelerated-molecular-discovery/README.md) | Accelerated Molecular Discovery | завершена |  |  | 4 | 0 |
| [APAQuS](programs/automated-prediction-aided-by-quantized-simulators/README.md) | Automated Prediction Aided by Quantized Simulators | действует |  | Mukund Vengalattore | 0 | 0 |
| [ARM](programs/autonomous-robotic-manipulation/README.md) | Autonomous Robotic Manipulation | завершена |  |  | 2 | 0 |
| [ARRIVE](programs/applications-resulting-from-recent-insights-in-vacuum-engineering/README.md) | Applications Resulting from Recent Insights in Vacuum Engineering | завершена |  |  | 0 | 0 |
| [AtmoSense](programs/atmosphere-as-a-sensor/README.md) | Atmosphere as a Sensor | завершена |  |  | 6 | 0 |
| [ATN](programs/all-together-now/README.md) | All Together Now | завершена |  |  | 0 | 0 |
| [AutoDIDACTS](programs/autodidacts/README.md) | Automated Discovery for Design and Control of Turbulent Systems | действует |  | Mukund Vengalattore | 0 | 0 |
| [AWE](programs/atmospheric-water-extraction/README.md) | Atmospheric Water Extractio | завершена |  |  | 5 | 0 |
| [Biofuels](programs/biofuels/README.md) | Biofuels | завершена |  |  | 0 | 0 |
| [CAML](programs/competency-aware-machine-learning/README.md) | Competency-Aware Machine Learning | завершена |  |  | 5 | 0 |
| [CASCADE](programs/complex-adaptive-system-composition-and-design-environment/README.md) | Complex Adaptive System Composition And Design Environment | завершена |  |  | 5 | 0 |
| [CASTOR](programs/castor/README.md) | CASTOR | действует |  | Michael McDonald | 0 | 0 |
| [CHAOS](programs/changing-hydrodynamics-and-aerodynamics-on-structures/README.md) | Changing Hydrodynamics and Aerodynamics On Structures | завершена |  |  | 0 | 0 |
| [Charge Harmony](programs/charge-harmony/README.md) | Charge Harmony | завершена |  |  | 0 | 0 |
| [CLARA](programs/clara/README.md) | Compositional Learning-And-Reasoning for Automated Complex Systems Engineering | действует |  | Benjamin Grosof | 0 | 0 |
| [CLOAK](programs/cloak-chemistries-monolayers/README.md) | Chemistries and monoLayers for Anti-aging Kinematics | действует |  | Sunil Bhave | 0 | 0 |
| [Coded Visibility](programs/coded-visibility/README.md) | Coded Visibility | завершена |  |  | 0 | 0 |
| [CODORD](programs/codord/README.md) | Human-Machine Communication for Deontic Reasoning Devops | действует |  | Benjamin Grosof | 1 | 0 |
| [Computable Models](programs/computable-models/README.md) | Computable Models | завершена |  |  | 0 | 0 |
| [Decay on Demand](programs/decay-on-demand/README.md) | Decay on Demand | действует |  | Tabitha Dodson | 0 | 0 |
| [Deep Purple](programs/deep-purposeful-learning/README.md) | Deep Purposeful Learning | завершена |  |  | 1 | 0 |
| [Detect](programs/fundamental-limits-of-photon-detection/README.md) | Fundamental Limits of Photon Detection | завершена |  |  | 0 | 0 |
| [DIAL](programs/mathematics-for-the-discovery-of-algorithms-and-architectures/README.md) | Mathematics for the Discovery of Algorithms and Architectures | действует |  | Yannis Kevrekidis | 0 | 0 |
| [DRAG](programs/drag-reducing-architected-geometries/README.md) | Drag Reducing Architected Geometries | завершена |  |  | 0 | 0 |
| [DRINQS](programs/driven-and-nonequilibrium-quantum-systems/README.md) | Driven and Nonequilibrium Quantum Systems | завершена |  |  | 0 | 0 |
| [EDGE](programs/enhancing-design-for-graceful-extensibility/README.md) | Enhancing Design for Graceful Extensibility | завершена |  |  | 0 | 0 |
| [EQUiPS](programs/equips/README.md) | Enabling Quantification of Uncertainty in Physical Systems | завершена |  |  | 0 | 0 |
| [ExCURSion](programs/expeditionary-carbon-utilization-for-energy-resilience-and-stabilization/README.md) | Expeditionary Carbon Utilization for Energy Resilience and Stabilization | действует |  | Keith Whitener | 5 | 0 |
| [ExPEDitions](programs/expeditions/README.md) | Expeditionary Power- and Energy-Dense Implementations | действует |  | Keith Whitener | 0 | 0 |
| [EXTREME](programs/extreme-optics-and-imaging/README.md) | Extreme Optics and Imaging | завершена |  |  | 0 | 0 |
| [Fast and Curious](programs/fast-and-curious/README.md) | Fast and Curious | действует |  | Sunil Bhave | 0 | 0 |
| [Fat Cat](programs/fat-cat/README.md) | Fast Capacitance | действует |  | Tabitha Dodson | 0 | 0 |
| [FETT](programs/thwart-tampering-bug-bounty/README.md) | Finding Exploits to Thwart Tampering Bug Bounty | завершена |  |  | 0 | 0 |
| [FLA](programs/fla/README.md) | Fast Lightweight Autonomy | завершена |  |  | 5 | 0 |
| [Fold F(x)](programs/folded-non-natural-polymers-with-biologicial-function/README.md) | Folded Non-Natural Polymers with Biological Function | завершена |  |  | 0 | 0 |
| [FS2](programs/foundational-security-for-food-systems/README.md) | Foundational Security for Food Systems | завершена |  |  | 0 | 0 |
| [FUN Design](programs/fundamental-design/README.md) | Fundamental Design | завершена |  |  | 0 | 0 |
| [FunCC](programs/fundamentals-of-complex-collectives/README.md) | Fundamentals of Complex Collectives | завершена |  |  | 0 | 0 |
| [FunLoL](programs/fundamental-limits-of-learning/README.md) | Fundamental Limits of Learning | завершена |  |  | 0 | 0 |
| [GRAPHS](programs/graphs/README.md) | Graph-theoretic Research in Algorithms and the PHenomenology of Social networks | завершена |  |  | 0 | 0 |
| [GRIT](programs/gamma-ray-inspection-technology/README.md) | Gamma Ray Inspection Technology | завершена |  |  | 1 | 0 |
| [GS3](programs/gamifying-the-search-for-strategic-surprise/README.md) | Gamifying the Search for Strategic Surprise - Polyplexus | завершена |  |  | 6 | 0 |
| [GT](programs/ground-truth/README.md) | Ground Truth | завершена |  |  | 3 | 0 |
| [Habitus](programs/habitus/README.md) | Habitus | завершена |  |  | 0 | 0 |
| [HNO3](programs/hno3/README.md) | High-efficiency Nitrogen Oxidation | действует |  | Keith Whitener | 3 | 0 |
| [HORCREX](programs/horcrex-composite-resonators/README.md) | Higher-Order Composite Resonators for Extra resilience | действует |  | Sunil Bhave | 0 | 0 |
| [IAMBIC](programs/investigating-adaptive-modal-bases-for-intelligent-classification/README.md) | Investigating Adaptive Modal Bases for Intelligent Classification | завершена |  |  | 1 | 0 |
| [ICONS](programs/intense-and-compact-neutron-sources/README.md) | Intense and Compact Neutron Sources | завершена |  |  | 5 | 0 |
| [Improv](programs/improv/README.md) | Improv | завершена |  |  | 24 | 0 |
| [Improv 2](programs/improv2/README.md) | Improv 2 | завершена |  |  | 0 | 0 |
| [InPho](programs/information-in-a-photon/README.md) | Information in a Photon | завершена |  |  | 0 | 0 |
| [INTACT](programs/intact-intrinsically-tough/README.md) | Intrinsically Tough and Affordable Ceramics Today | действует |  | Andrew Detor | 0 | 0 |
| [Invisible Headlights](programs/invisible-headlights/README.md) | Invisible Headlights | завершена |  |  | 1 | 0 |
| [It's About Time](programs/its-about-time/README.md) | It's About Time | действует |  | Mukund Vengalattore | 0 | 0 |
| [ITA3](programs/imaging-through-almost-anything-anywhere/README.md) | Imaging Through Almost Anything Anywhere | завершена |  |  | 2 | 0 |
| [KMASS](programs/knowledge-management-at-scale-and-speed/README.md) | Knowledge Management at Scale and Speed | завершена |  |  | 2 | 0 |
| [Lagrange](programs/lagrange/README.md) | Lagrange | завершена |  |  | 0 | 0 |
| [LeviTAS](programs/levitated-and-trapped-accurate-microsystems/README.md) | Levitated and Trapped Accurate microSystems | действует |  | Sunil Bhave | 0 | 0 |
| [Liquid Surge](programs/liquid-surge/README.md) | Liquid Surge | действует |  | Carlo Scalo | 0 | 0 |
| [LoCo](programs/local-control-of-materials-synthesis/README.md) | Local Control of Materials Synthesis | завершена |  |  | 4 | 0 |
| [M3](programs/maximum-mobility-and-manipulation/README.md) | Maximum Mobility and Manipulation | завершена |  |  | 0 | 0 |
| [Make-It](programs/make-it/README.md) | Make-It | завершена |  |  | 1 | 0 |
| [MARRS](programs/marrs-mechanisms-amplification-fusion-reaction-rates-solids/README.md) | Mechanisms for Amplification of fusion Reaction Rates in Solids | действует |  | Thomas Schenkel | 3 | 0 |
| [MATHBAC](programs/mathbac/README.md) | Mathematics of Boosting Agentic Communication | действует |  | Yannis Kevrekidis | 0 | 0 |
| [MATRIX](programs/matrix/README.md) | Materials for Transduction | завершена |  |  | 3 | 0 |
| [MCMA](programs/materials-with-controlled-microstructural-architecture/README.md) | Materials with Controlled Microstructural Architecture | завершена |  |  | 1 | 0 |
| [MDP](programs/materials-development-for-platforms/README.md) | Materials Development for Platforms | завершена |  |  | 6 | 0 |
| [MeasQuIT](programs/measurement-based-quantum-information-and-transduction/README.md) | Measurement-based Quantum Information and Transduction | действует |  | Mukund Vengalattore | 0 | 0 |
| [MENTOR2](programs/manufacturing-experimentation-and-outreach/README.md) | Manufacturing Experimentation and Outreach Two | завершена |  |  | 4 | 0 |
| [Metals](programs/multiobjective-engineering-and-testing-of-alloy-structures/README.md) | Multiobjective Engineering and Testing of Alloy Structures | действует |  | Gautam Parthasarathy | 6 | 0 |
| [MINOS](programs/materials-investigation-novel-operations/README.md) | Materials Investigation for Novel Operations in Space | действует |  | Michael McDonald | 0 | 0 |
| [MINT](programs/morphogenic-interfaces/README.md) | Morphogenic Interfaces | действует |  | Yannis Kevrekidis | 6 | 0 |
| [MMoMA](programs/multi-modal-materials-analysis/README.md) | Multi Modal Materials Analysis | действует |  | Thomas Schenkel | 0 | 0 |
| [MoDyL](programs/models-dynamics-and-learning/README.md) | Models, Dynamics and Learning | завершена |  |  | 0 | 0 |
| [MSDC](programs/molecular-scaffold-design-collective/README.md) | Molecular Scaffold Design Collective | завершена |  |  | 0 | 0 |
| [MSEE](programs/mathematics-of-sensing-exploitation-and-execution/README.md) | Mathematics of Sensing, Exploitation and Execution | завершена |  |  | 1 | 0 |
| [MuS2](programs/muons-for-science-and-security/README.md) | Muons for Science and Security | завершена |  |  | 0 | 0 |
| [NaPSAC](programs/nanowatt-platforms-for-sensing-analysis-and-computation/README.md) | NanoWatt Platforms for Sensing, Analysis and Computation | действует |  | Mukund Vengalattore | 0 | 0 |
| [NEAT](programs/neural-evidence-aggregation-tool/README.md) | Neural Evidence Aggregation Tool | завершена |  |  | 1 | 0 |
| [NIMBUS](programs/nimble-ultrafast-microsystems/README.md) | Nimble Ultrafast Microsystems | действует |  | Sunil Bhave | 1 | 0 |
| [NOM4D](programs/novel-orbital-and-moon-manufacturing-materials-and-mass-efficient-design/README.md) | Novel Orbital and Moon Manufacturing, Materials, and Mass-efficient Design | действует |  | Andrew Detor | 8 | 0 |
| [ONISQ](programs/optimization-with-noisy-intermediate-scale-quantum-devices/README.md) | Optimization with Noisy Intermediate-Scale Quantum devices | завершена |  |  | 2 | 0 |
| [Open Manufacturing](programs/open-manufacturing/README.md) | Open Manufacturing | завершена |  |  | 9 | 0 |
| [OpTIm](programs/optomechanical-thermal-imaging/README.md) | Optomechanical Thermal Imaging | действует |  | Mukund Vengalattore | 9 | 0 |
| [PAI](programs/physics-of-artificial-intelligence/README.md) | Physics of Artificial Intelligence | завершена |  |  | 0 | 0 |
| [PENG](programs/peng/README.md) | Protein ENGineering | действует |  | Robin Bonomi | 0 | 0 |
| [PhENOM](programs/photon-efficient-nanoscale-optical-metrology/README.md) | Photon-Efficient Nanoscale Optical Metrology | действует |  | Mukund Vengalattore | 0 | 0 |
| [PINPOINT](programs/pinpoint/README.md) | Precision Inertial Navigation & Positioning On an Integrated Tesseract | действует |  | Sunil Bhave | 0 | 0 |
| [PULSE](programs/program-in-ultrafast-laser-science-and-engineering/README.md) | Program in Ultrafast Laser Science and Engineering | завершена |  |  | 1 | 0 |
| [PUMP](programs/principles-of-undersea-magnetohydrodynamic-pumps/README.md) | Principles of Undersea Magnetohydrodynamic Pumps | завершена |  |  | 1 | 0 |
| [QORS](programs/quantum-orbital-resonance-spectroscopy/README.md) | Quantum Orbital Resonance Spectroscopy | завершена |  |  | 0 | 0 |
| [QuASAR](programs/quantum-assisted-sensing-and-readout/README.md) | Quantum-Assisted Sensing and Readout | завершена |  |  | 0 | 0 |
| [QuBE](programs/quantum-effects-in-biological-environments/README.md) | Quantum effects in Biological Environments | завершена |  |  | 1 | 0 |
| [QUEST](programs/quest/README.md) | Quest for Undiscovered Energy Storage and Thrust | завершена |  |  | 0 | 0 |
| [Quiness](programs/quiness/README.md) | Quiness | завершена |  |  | 0 | 0 |
| [QuSeN](programs/qusen/README.md) | Quantum Sensing of Neutrinos | действует |  | Thomas Schenkel | 3 | 0 |
| [RadioBio](programs/radiobio/README.md) | RadioBio | завершена |  |  | 3 | 0 |
| [Rads to Watts](programs/rads-watts/README.md) | Rads to Watts | действует |  | Tabitha Dodson | 1 | 0 |
| [REM REST](programs/rapid-eye-movement/README.md) | Rapid Eye Movement Restoration and Enhancement of Sleep-derived Trauma-adaptation | завершена |  |  | 0 | 0 |
| [Resilient](programs/resilient/README.md) | Resilient | действует |  | Christine Sanders | 0 | 0 |
| [RESTORE](programs/restore-reengineering-enabling-sleep/README.md) | Reengineering Enabling Sleep Transitions in Operationally Restrictive Environments | завершена |  |  | 1 | 0 |
| [RIDE](programs/rational-integrated-design-energetics/README.md) | Rational Integrated Design of Energetics | завершена |  |  | 3 | 0 |
| [ROCkN](programs/robust-optical-clock-network/README.md) | Robust Optical Clock Network | действует |  | Mukund Vengalattore | 2 | 0 |
| [RPOD](programs/recycling-at-the-point-of-disposal/README.md) | Recycling at the Point of Disposal | завершена |  |  | 0 | 0 |
| [RQMLS](programs/reversible-quantum-machine-learning-and-simulation/README.md) | Reversible Quantum Machine Learning and Simulation | завершена |  |  | 0 | 0 |
| [SAVaNT](programs/science--atomic-vapors-for-new-technologies/README.md) | Science of Atomic Vapors for New Technologies | действует |  | Mukund Vengalattore | 3 | 0 |
| [SCOPE](programs/spin-controlled-chemical-process-engineering/README.md) | Spin-COntrolled chemical Process Engineering | завершена |  |  | 0 | 0 |
| [SCORE](programs/systematizing-confidence-in-open-research-and-evidence/README.md) | Systematizing Confidence in Open Research and Evidence | завершена |  |  | 1 | 0 |
| [SEE](programs/space-environment-exploitation/README.md) | Space Environment Exploitation | завершена |  |  | 0 | 0 |
| [SENSE](programs/structural-evaluation/README.md) | Structural Evaluation through Non-contact Sensor Embedding | завершена |  |  | 0 | 0 |
| [SeREne](programs/serene/README.md) | Switchable Reactives and Energetics | действует |  | Keith Whitener | 0 | 0 |
| [SHINE](programs/shine/README.md) | Selective Harnessing of Intrinsic Neuroplasticity Engineering | действует |  | Robin Bonomi | 0 | 0 |
| [SIGMA](programs/sigma/README.md) | SIGMA | завершена |  |  | 8 | 0 |
| [SIGMA+](programs/sigma-plus/README.md) | SIGMA+ | завершена |  |  | 4 | 0 |
| [STRENGTHEN](programs/strengthening-resilient-emotions/README.md) | Strengthening Resilient Emotions and Nimble Cognition through Engineering Neuroplasticity | действует |  | Robin Bonomi | 3 | 0 |
| [SUNSPOT](programs/sunspot/README.md) | Sources for Ultraviolet Nuclear Spectroscopy of Thorium | действует |  | Mukund Vengalattore | 4 | 0 |
| [SURGE](programs/structures-uniquely-resolved-guarantee-endurance/README.md) | Structures Uniquely Resolved to Guarantee Endurance | действует |  | Andrew Detor | 5 | 0 |
| [SynQuaNon](programs/synthetic-quantum-nanostructures/README.md) | Synthetic Quantum Nanostructures | действует |  | Mukund Vengalattore | 5 | 0 |
| [TAILOR](programs/teaching-ai-to-leverage-overlooked-residuals/README.md) | Teaching AI to Leverage Overlooked Residuals | завершена |  |  | 0 | 0 |
| [TALOS](programs/thruster-advancements-for-low-altitude-operations-in-space/README.md) | Thruster Advancements for Low-altitude Operations in Space | действует |  | Michael McDonald | 0 | 0 |
| [TAMI](programs/time-aware-machine-intelligence/README.md) | Time-Aware Machine Intelligence | завершена |  |  | 0 | 0 |
| [TEE](programs/topological-excitations-in-electronics/README.md) | Topological Excitations in Electronics | завершена |  |  | 0 | 0 |
| [TEMPS](programs/thermal-engineering-using-metamaterial/README.md) | Thermal Engineering using Materials Physics | завершена |  |  | 0 | 0 |
| [TFF](programs/tailorable-feedstock-and-forming/README.md) | Tailorable Feedstock and Forming | завершена |  |  | 0 | 0 |
| [TRADES](programs/transformative-design/README.md) | Transformative Design | завершена |  |  | 3 | 0 |
| [TRS](programs/trs-the-right-space/README.md) | The Right Space | действует |  | Yannis Kevrekidis | 0 | 0 |
| [UGB](programs/understanding-group-biases/README.md) | Understanding Group Biases | завершена |  |  | 0 | 0 |
| [VIP](programs/virtual-intelligence-processing/README.md) | Virtual Intelligence Processing | завершена |  |  | 0 | 0 |
| [Z-Man](programs/z-man/README.md) | Z-Man | завершена |  |  | 0 | 0 |
| [Zenith](programs/zenith/README.md) | Zenith | завершена |  |  | 2 | 0 |

<a id="office-bto"></a>

## Biological Technologies Office (BTO) — биологические технологии — 110

| Программа | Полное название | Статус | Сфера | Руководитель (darpa.mil) | Исполнителей | Новостей |
|---|---|---|---|---|---|---|
| [ABC](programs/anesthetics-battlefield-care/README.md) | Anesthetics for Battlefield Care | действует |  | Jeremy Pamplin | 0 | 0 |
| [ADAPTER](programs/advanced-acclimation-protection/README.md) | ADvanced Acclimation and Protection Tool for Environmental Readiness | завершена |  |  | 0 | 0 |
| [ADEPT](programs/adept/README.md) | Autonomous Diagnostics to Enable Prevention and Therapeutics | завершена |  |  | 3 | 0 |
| [Ag x BTO](programs/ag-bto/README.md) | Ag x BTO | действует |  | Michael Koeris | 0 | 0 |
| [AIM](programs/assessing-immune-memory/README.md) | Assessing Immune Memory | завершена |  |  | 0 | 0 |
| [AMPHORA](programs/assured-microbial-preservation-in-harsh-or-remote-areas/README.md) | Assured Microbial Preservation in Harsh Or Remote Areas | действует |  | Robert Murray | 3 | 0 |
| [APT](programs/advanced-plant-technologies/README.md) | Advanced Plant Technologies | завершена |  |  | 2 | 0 |
| [Arcadia](programs/arcadia/README.md) | Arcadia | действует |  | Jeffrey Zaleski | 3 | 0 |
| [AWARE](programs/alert-warfighter-enablement/README.md) | Alert WARfighter Enablement | действует |  | Pedro Irazoqui | 0 | 0 |
| [B-SURE](programs/biomanufacturing-survival-utility-and-reliability-beyond-earth/README.md) | Biomanufacturing: Survival, Utility, and Reliability beyond Earth | завершена |  |  | 0 | 0 |
| [Battlefield Medicine](programs/battlefield-medicine/README.md) | Battlefield Medicine | завершена |  |  | 0 | 0 |
| [BEST](programs/best-bioelectronics/README.md) | BioElectronics to Sense and Treat | действует |  | Roozbeh Jafari | 0 | 0 |
| [BETR](programs/bioelectronics-for-tissue-regeneration/README.md) | Bioelectronics for Tissue Regeneration | действует |  | Roozbeh Jafari | 0 | 0 |
| [BG+](programs/bridging-the-gap-plus/README.md) | Bridging the Gap Plus | завершена |  |  | 0 | 0 |
| [Biochronicity](programs/biochronicity/README.md) | Biochronicity | завершена |  |  | 0 | 0 |
| [Biological Control](programs/biological-control/README.md) | Biological Control | завершена |  |  | 4 | 0 |
| [Biostasis](programs/biostasis/README.md) | Biostasis | завершена |  |  | 0 | 0 |
| [BLUE](programs/biological-undersea-energy/README.md) | BioLogical Undersea Energy | действует |  | William Mounfield | 3 | 0 |
| [BRACE](programs/bio-inspired-restoration-of-aged-concrete-edifices/README.md) | Bio-inspired Restoration of Aged Concrete Edifices | действует |  | Catherine Campbell | 0 | 0 |
| [BRICS](programs/biological-robustness-in-complex-settings/README.md) | Biological Robustness in Complex Settings | завершена |  |  | 8 | 0 |
| [Ceres](programs/ceres/README.md) | Ceres | завершена |  |  | 0 | 0 |
| [CoasterChase](programs/coasterchase/README.md) | CoasterChase | действует |  | Pedro Irazoqui | 1 | 0 |
| [Control Systems and Biology](programs/control-systems-biology/README.md) | Control Systems and Biology | завершена |  |  | 0 | 0 |
| [Convergence](programs/convergence/README.md) | Convergence | действует |  | Mark Salvador | 0 | 0 |
| [Cornerstone](programs/cornerstone/README.md) | Cornerstone | завершена |  |  | 2 | 0 |
| [Cornucopia](programs/cornucopia/README.md) | Cornucopia | завершена |  |  | 1 | 0 |
| [DIGET](programs/detect-it-with-gene-editing-technologies/README.md) | Detect It with Gene Editing Technologies | завершена |  |  | 0 | 0 |
| [DLT](programs/dialysis-like-therapeutics/README.md) | Dialysis-Like Therapeutics | завершена |  |  | 0 | 0 |
| [DTC](programs/triage/README.md) | DARPA Triage Challenge | действует |  | Jeremy Pamplin | 9 | 1 |
| [ECHO](programs/epigenetic-characterization-and-observation/README.md) | Epigenetic CHaracterization and Observation | завершена |  |  | 0 | 0 |
| [ElectRx](programs/electrical-prescriptions/README.md) | Electrical Prescriptions | завершена |  |  | 7 | 0 |
| [ELM](programs/engineered-living-materials/README.md) | Engineered Living Materials | завершена |  |  | 1 | 0 |
| [EMBER](programs/environmental-microbes-as-a-bioengineering-resource/README.md) | Environmental Microbes as a BioEngineering Resource | действует |  | William Mounfield | 1 | 0 |
| [Enabling Stress Resistance](programs/enabling-stress-resistance/README.md) | Enabling Stress Resistance | завершена |  |  | 0 | 0 |
| [EQUIP-A-Pharma](programs/establishing-qualification-processes-for-agile-pharmaceutical-manufacturing/README.md) | Establishing Qualification Processes for Agile Pharmaceutical Manufacturing | действует |  | Sushma Savarala | 0 | 0 |
| [eXVi](programs/ex-virentia/README.md) | eX Virentia | действует |  | Mark Salvador | 0 | 0 |
| [Firefox](programs/firefox/README.md) | Firefox | действует |  | Pedro Irazoqui | 0 | 0 |
| [Fleetwood](programs/fleetwood/README.md) | Fleetwood | действует |  | William Mounfield | 0 | 0 |
| [Focused Pharma](programs/focused-pharma/README.md) | Focused Pharma | завершена |  |  | 2 | 0 |
| [Friend or Foe](programs/friend-or-foe/README.md) | Friend or Foe | завершена |  |  | 0 | 0 |
| [FSHARP](programs/fieldable-solutions-for-hemorrhage-with-bio-artificial-resuscitation-products/README.md) | Fieldable Solutions for Hemorrhage with bio-Artificial Resuscitation Products | завершена |  |  | 0 | 0 |
| [GO](programs/go/README.md) | Generative Optogenetics | действует |  | Matthew Pava | 2 | 0 |
| [GOLDEVAC](programs/golden-hour-extended-evacuation/README.md) | GOLDen hour extended EVACuation | действует |  | Jeremy Pamplin | 1 | 0 |
| [GUARDIAN](programs/guardian-genetic-utilization/README.md) | Genetic Utilization for Advanced Regulation and Defense of Indigenous and Native Species | действует |  | Catherine Campbell | 0 | 0 |
| [HAPTIX](programs/hand-proprioception-and-touch-interfaces/README.md) | Hand Proprioception and Touch Interfaces | завершена |  |  | 2 | 0 |
| [HEALR](programs/healr/README.md) | Harnessing Enzymatic Activity for Lifesaving Remedies | действует |  | Jeremy Pamplin | 4 | 0 |
| [Hermes](programs/hermes/README.md) | Hermes | действует |  | Catherine Campbell | 0 | 0 |
| [Hubble](programs/hubble/README.md) | High-throughput Unmasking of Biological Interactomes with Binding Landscape Emulators | действует |  | Abhishek Singharoy | 0 | 0 |
| [ICE](programs/ice-control-for-cold-environments/README.md) | Ice Control for cold Environments | действует |  | Jeffrey Zaleski | 1 | 0 |
| [INI](programs/intelligent-neural-interfaces/README.md) | Intelligent Neural Interfaces | завершена |  |  | 0 | 0 |
| [Insect Allies](programs/insect-allies/README.md) | Insect Allies | завершена |  |  | 0 | 0 |
| [INTERCEPT](programs/intercept/README.md) | INTERfering and Co-Evolving Prevention and Therapy | завершена |  |  | 5 | 0 |
| [IVN](programs/in-vivo-nanoplatforms/README.md) | In Vivo Nanoplatforms | завершена |  |  | 1 | 0 |
| [Laguna](programs/laguna/README.md) | Laguna | действует |  | William Mounfield | 0 | 0 |
| [Living Foundries](programs/living-foundries/README.md) | Living Foundries | завершена |  |  | 12 | 0 |
| [MASH](programs/medics-autonomously-stopping-hemorrhage/README.md) | Medics Autonomously Stopping Hemorrhage | действует |  | Roozbeh Jafari | 0 | 0 |
| [MBA](programs/measuring-biological-aptitude/README.md) | Measuring Biological Aptitude | завершена |  |  | 0 | 0 |
| [MIMs](programs/mechanically-interlocked-materials/README.md) | Mechanically Interlocked Materials | завершена |  |  | 7 | 0 |
| [MPS](programs/microphysiological-systems/README.md) | Microphysiological Systems | завершена |  |  | 0 | 0 |
| [N3](programs/next-generation-nonsurgical-neurotechnology/README.md) | Next-Generation Nonsurgical Neurotechnology | завершена |  |  | 0 | 0 |
| [Narrative Networks](programs/narrative-networks/README.md) | Narrative Networks | завершена |  |  | 0 | 0 |
| [NESD](programs/neural-engineering-system-design/README.md) | Neural Engineering System Design | завершена |  |  | 1 | 0 |
| [Neuro-FAST](programs/neuro-function-activity-structure-and-technology/README.md) | Neuro Function, Activity, Structure, and Technology | завершена |  |  | 0 | 0 |
| [NODES](programs/nodes/README.md) | Network of Optimal Dynamic Energy Signatures | действует |  | Abhishek Singharoy | 1 | 0 |
| [NOW](programs/nucleic-acids-on-demand-worldwide/README.md) | Nucleic acids On-demand Worldwide | завершена |  |  | 0 | 0 |
| [O-Circuit](programs/o-circuit/README.md) | Organoid Cytomorphic Intelligence Resulting from Convergent Understanding and Information Transfer | действует |  | Jeffrey Zaleski | 0 | 0 |
| [OP TEMPO](programs/objective-prediction-of-team-effectiveness-via-models-of-performance-outcomes/README.md) | Objective Prediction of Team Effectiveness via Models of Performance Outcomes | действует |  | Kyle Schwing | 3 | 0 |
| [P3](programs/pandemic-prevention-platform/README.md) | Pandemic Prevention Platform | завершена |  |  | 0 | 0 |
| [PALS](programs/persistent-aquatic-living-sensors/README.md) | Persistent Aquatic Living Sensors | завершена |  |  | 1 | 0 |
| [Panacea](programs/panacea/README.md) | Panacea | завершена |  |  | 2 | 0 |
| [Pathogen Predators](programs/pathogen-predators/README.md) | Pathogen Predators | завершена |  |  | 0 | 0 |
| [PPB](programs/personalized-protective-biosystem/README.md) | Personalized Protective Biosystem | завершена |  |  | 0 | 0 |
| [PREEMPT](programs/preventing-emerging-pathogenic-threats/README.md) | PREventing EMerging Pathogenic Threats | завершена |  |  | 0 | 0 |
| [PREPARE](programs/preemptive-expression-of-protective-alleles-and-response-elements/README.md) | PReemptive Expression of Protective Alleles and Response Elements | завершена |  |  | 3 | 0 |
| [PREVENT](programs/preventing-violent-explosive-neurologic-trauma/README.md) | Preventing Violent Explosive Neurologic Trauma | завершена |  |  | 0 | 0 |
| [Prometheus](programs/prometheus/README.md) | Prometheus | завершена |  |  | 1 | 0 |
| [Prophecy](programs/prophecy-pathogen-defeat/README.md) | Prophecy | завершена |  |  | 3 | 0 |
| [Protean](programs/protean/README.md) | Protean | действует |  | Abhishek Singharoy | 1 | 0 |
| [RAM](programs/restoring-active-memory/README.md) | Restoring Active Memory | завершена |  |  | 0 | 0 |
| [RAPIID](programs/rapiid/README.md) | Resuscitation and Prevention of Ischemia-Induced Dysfunction | действует |  | Robert Murray | 0 | 0 |
| [RBC-Factory](programs/rbc-factory/README.md) | RBC-Factory | действует |  | Robert Murray | 0 | 0 |
| [RE-NET](programs/re-net-reliable-peripheral-interfaces/README.md) | Reliable Neural-Interface Technology | завершена |  |  | 0 | 0 |
| [RE-NET HIST](programs/histology-for-interface-stability-over-time/README.md) | Reliable Neural-Interface Technology - Histology for Interface Stability over-time | завершена |  |  | 0 | 0 |
| [RE-NET RCI](programs/reliable-central-nervous-system/README.md) | Reliable Neural-Interface Technology - Reliable Central-Nervous-System Interfaces | завершена |  |  | 0 | 0 |
| [Reefense](programs/reefense/README.md) | Reefense | действует |  | Catherine Campbell | 4 | 0 |
| [REPAIR](programs/reorganization-and-plasticity-to-accelerate-injury-recovery/README.md) | Reorganization and Plasticity to Accelerate Injury Recovery | завершена |  |  | 0 | 0 |
| [ReSource](programs/resource/README.md) | ReSource | завершена |  |  | 5 | 0 |
| [ReVector](programs/revector/README.md) | ReVector | завершена |  |  | 2 | 0 |
| [Revolutionizing Prosthetics](programs/revolutionizing-prosthetics/README.md) | Revolutionizing Prosthetics | завершена |  |  | 0 | 0 |
| [RIDDL](programs/rapid-inhibitor-discovery-riddl/README.md) | Rapid Inhibitor Discovery and Development pipeLine | действует |  | Catherine Campbell | 0 | 0 |
| [RITMO](programs/research-trauma/README.md) | Research Infrastructure for Trauma with Medical Observations | действует |  | Jeremy Pamplin | 2 | 0 |
| [RPI](programs/reliable-peripheral-interfaces/README.md) | Reliable Peripheral Interfaces | завершена |  |  | 0 | 0 |
| [RPM](programs/reimagining-protein-manufacturing/README.md) | Reimagining Protein Manufacturing | завершена |  |  | 0 | 0 |
| [RTA](programs/rapid-threat-assessment/README.md) | Rapid Threat Assessment | завершена |  |  | 0 | 0 |
| [Safe Genes](programs/safe-genes/README.md) | Safe Genes | завершена |  |  | 1 | 0 |
| [SBL](programs/surviving-blood-loss/README.md) | Surviving Blood Loss | завершена |  |  | 0 | 0 |
| [SHIELD](programs/SHIELD/README.md) | Synthetic Hemo-technologIEs to Locate and Disinfect | действует |  | Jeremy Pamplin | 3 | 0 |
| [Smart-RBC](programs/smart-rbc/README.md) | Smart Red Blood Cells | действует |  | Robert Murray | 0 | 0 |
| [SMS](programs/simulating-microbial-systems/README.md) | Simulating Microbial Systems | действует |  | Russell Schwartz | 0 | 0 |
| [SNAP](programs/smart-non-invasive-assays-physiology/README.md) | Smart Non-invasive Assays of Physiology | завершена |  |  | 0 | 0 |
| [SSIM](programs/strategic-social-interaction-modules/README.md) | Strategic Social Interaction Modules | завершена |  |  | 0 | 0 |
| [SUBNETS](programs/systems-based-neurotechnology-for-emerging-therapies/README.md) | Systems-Based Neurotechnology for Emerging Therapies | завершена |  |  | 1 | 0 |
| [Switch](programs/switch/README.md) | Switch | действует |  | William Mounfield | 1 | 0 |
| [Tellus](programs/tellus/README.md) | Tellus | завершена |  |  | 2 | 0 |
| [THoR](programs/technologies-for-host-resilience/README.md) | Technologies for Host Resilience | завершена |  |  | 1 | 0 |
| [TNT](programs/targeted-neuroplasticity-training/README.md) | Targeted Neuroplasticity Training | завершена |  |  | 0 | 0 |
| [VITAL](programs/virtual-integrated-twin-for-autonomous-lifesaving/README.md) | Virtual-Integrated Twin for Autonomous Lifesaving | действует |  | Roozbeh Jafari | 0 | 0 |
| [Warrior Web](programs/warrior-web/README.md) | Warrior Web | завершена |  |  | 0 | 0 |
| [WSS](programs/wound-stasis-system/README.md) | Wound Stasis System | завершена |  |  | 0 | 0 |
| [WUD](programs/waste-upcycling-for-defense/README.md) | Waste Upcycling for Defense | действует |  | William Mounfield | 5 | 0 |

<a id="office-sbpo"></a>

## Small Business Programs Office (SBPO) — программы малого бизнеса — 50

| Программа | Полное название | Статус | Сфера | Руководитель (darpa.mil) | Исполнителей | Новостей |
|---|---|---|---|---|---|---|
| [ALIAS Missionized Autonomy for Emergency Services - SBIR XL / SBIR](programs/alias-missionized-autonomy-for-emergency-services/README.md) | ALIAS Missionized Autonomy for Emergency Services - SBIR XL / SBIR | завершена |  |  | 0 | 0 |
| [Art of Novel Signals / SBIR](programs/predicting-forecasting-high-confidence/README.md) | Predicting and Forecasting with High Confidence | завершена |  |  | 0 | 0 |
| [ASEMA / SBIR](programs/asema/README.md) | Assessing Security of Encrypted Messaging Applications | завершена |  |  | 0 | 0 |
| [Automated Process for Codesign of Radiation Hardening and Security / SBIR](programs/automated-process-for-codesign-of-radiation-hardening-and-security/README.md) | Automated Process for Codesign of Radiation Hardening and Security / SBIR | завершена |  |  | 0 | 0 |
| [BARK / SBIR](programs/bark/README.md) | Broadening Availability of Regimens for K-9s - Open Topic | завершена |  |  | 0 | 0 |
| [Biomanufacturing of Hierarchical Biocomposites for High-Performance Thermal Interface Materials / STTR](programs/biomanufacturing-of-hierarchical-biocomposites-for-high-performance-thermal-interface-materials/README.md) | Biomanufacturing of Hierarchical Biocomposites for High-Performance Thermal Interface Materials / STTR | завершена |  |  | 0 | 0 |
| [CHAMP / SBIR](programs/champ/README.md) | Cooperative Heuristics for Additive Manufacturing Processing | завершена |  |  | 0 | 0 |
| [Commercialization of Ultra-High Payload-to-Weight UAS Subsystems / SBIR](programs/commercialization-ultra-high-payload-to-weight-uas-subsystems/README.md) | Commercialization of Ultra-High Payload-to-Weight UAS Subsystems / SBIR | завершена | БПЛА |  | 0 | 0 |
| [Compact Wideband Tunable Filters / SBIR](programs/compact-wideband-tunable-filters/README.md) | Compact Wideband Tunable Filters / SBIR | завершена |  |  | 0 | 0 |
| [CORPS / SBIR](programs/corps/README.md) | Casualty Operations & Resource Prediction Software | завершена |  |  | 0 | 0 |
| [Engineering Sleep for Cognitive Performance / SBIR](programs/engineering-sleep-for-cognitive-performance/README.md) | Engineering Sleep for Cognitive Performance / SBIR | завершена |  |  | 0 | 0 |
| [ExCAIPE / SBIR](programs/excaipe/README.md) | Expeditionary Closed and Air-Independent Power and Energy | завершена |  |  | 0 | 0 |
| [Extremity Platform for On-demand Surgical Implantation and Tissue Integration with Osteochondral Neogenesis / SBIR](programs/extremity-platform-for-on-demand-surgical-implantation-and-tissue-integration-with-osteochondral-neogenesis/README.md) | Extremity Platform for On-demand Surgical Implantation and Tissue Integration with Osteochondral Neogenesis / SBIR | завершена |  |  | 0 | 0 |
| [FALCON / SBIR](programs/falcon/README.md) | Fusion of Abstract Learning and Context-Optimized Neural-methods | завершена |  |  | 0 | 0 |
| [Fuel-Flexible Spacecraft Electric Propulsion System / STTR](programs/fuel-flexible-spacecraft-electric-propulsion-system/README.md) | Fuel-Flexible Spacecraft Electric Propulsion System / STTR | завершена |  |  | 0 | 0 |
| [High Power Fiber Amplifier (HPFA) Power Scaling / SBIR](programs/hpfa-power-scaling/README.md) | High Power Fiber Amplifier (HPFA) Power Scaling / SBIR | завершена |  |  | 0 | 0 |
| [Hoboken / SBIR XL](programs/hoboken/README.md) | Hoboken / SBIR XL | завершена |  |  | 0 | 0 |
| [ICU-in-a-Box / SBIR](programs/icu-in-a-box/README.md) | Autonomous Extracorporeal Multiple-Organ Support Therapies | завершена |  |  | 0 | 0 |
| [Improving Battle Planning through AI / SBIR](programs/improving-battle-planning-through-ai/README.md) | Improving Battle Planning through AI / SBIR | завершена |  |  | 0 | 0 |
| [Influence Benchmarks for AI Systems / SBIR](programs/influence-benchmarks-ai-systems/README.md) | Influence Benchmarks for AI Systems / SBIR | завершена |  |  | 0 | 0 |
| [ISaAc / SBIR](programs/isaac/README.md) | Inertially Scaled Aircraft | завершена | БПЛА, авиация |  | 0 | 0 |
| [LM4VSP / SBIR](programs/lm4vsp/README.md) | Language Models for Veteran Suicide Prevention | завершена |  |  | 0 | 0 |
| [Localization, Characterization, and Modeling of Freestream Disturbances in Hypersonic Wind Tunnels / STTR](programs/localization-characterization-modeling-freestream-disturbances-hypersonic-wind-tunnels/README.md) | Localization, Characterization, and Modeling of Freestream Disturbances in Hypersonic Wind Tunnels / STTR | завершена |  |  | 0 | 0 |
| [Low Resource Computing / SBIR](programs/low-resource-computing/README.md) | Low Resource Computing / SBIR | завершена |  |  | 0 | 0 |
| [MANTRAS / SBIR-XL](programs/mantras/README.md) | Manufacturing Technologies for Ryberg-based Atomic Sensors | завершена |  |  | 0 | 0 |
| [MCAWDE / SBIR](programs/mcawde/README.md) | Multi-factor Continuous Authentication for Wearable Defense Equipment | завершена |  |  | 0 | 0 |
| [Medical Swarm Robotics for Extraction and Life-Saving Interventions / STTR](programs/medical-swarm-robotics-for-extraction-and-life-saving-interventions/README.md) | Medical Swarm Robotics for Extraction and Life-Saving Interventions / STTR | завершена |  |  | 0 | 0 |
| [Nanopore Bioelectronics for Next Generation Proteomics / SBIR](programs/nanopore-bioelectronics-for-next-generation-proteomics/README.md) | Nanopore Bioelectronics for Next Generation Proteomics / SBIR | завершена |  |  | 0 | 0 |
| [New World Screwworm Networked Detection, Identification, and Surveillance System / SBIR](programs/new-world-screwworm-networked-detection-identification-surveillance-system/README.md) | New World Screwworm Networked Detection, Identification, and Surveillance System / SBIR | завершена |  |  | 0 | 0 |
| [Non-destructive Viral ID / SBIR](programs/non-destructive-viral-id/README.md) | Non-destructive Viral ID / SBIR | завершена |  |  | 0 | 0 |
| [Non-Volatile Memory for Extreme Environments / SBIR (Amended)](programs/non-volatile-memory-extreme-environments/README.md) | Non-Volatile Memory for Extreme Environments / SBIR (Amended) | завершена |  |  | 0 | 0 |
| [Noninvasive Detection and Localization of Occult Hemorrhage / SBIR](programs/noninvasive-detection-localization-occult-hemorrhage/README.md) | Noninvasive Detection and Localization of Occult Hemorrhage / SBIR | завершена |  |  | 0 | 0 |
| [Novel Radio Frequency Sensing Technologies / SBIR](programs/novel-radio-frequency-sensing-technologies/README.md) | Novel Radio Frequency Sensing Technologies / SBIR | завершена |  |  | 0 | 0 |
| [On-Chip Wavelength Generation for DWDM Photonic Transceivers / SBIR](programs/on-chip-wavelength-generation-for-dwdm-photonic-transceivers/README.md) | On-Chip Wavelength Generation for DWDM Photonic Transceivers / SBIR | завершена |  |  | 0 | 0 |
| [Open Architecture Platform for Underwater Vehicles for Rapid Adaptation, Collaborative Sensing, Navigation, and Autonomy / SBIR](programs/open-architecture-platform-underwater-vehicles/README.md) | Open Architecture Platform for Underwater Vehicles for Rapid Adaptation, Collaborative Sensing, Navigation, and Autonomy / SBIR | завершена |  |  | 0 | 0 |
| [PEPI / SBIR](programs/pepi/README.md) | Photonic-electronic Panels Integration | завершена |  |  | 0 | 0 |
| [PHLASH / SBIR](programs/phlash/README.md) | Pulsed High-power Laser Accelerators to Study radiation Hardening | завершена |  |  | 0 | 0 |
| [PPADM / SBIR](programs/ppadm/README.md) | Predictive Psychological Architectures for Decision-Making | завершена |  |  | 0 | 0 |
| [Real-Time Pathogen-Host Interactome Prediction / SBIR](programs/real-time-pathogen-host-interactome-prediction/README.md) | Real-Time Pathogen-Host Interactome Prediction / SBIR | завершена |  |  | 0 | 0 |
| [Semantically-Aware ISR / SBIR](programs/semantically-aware-isr/README.md) | Semantically-Aware ISR / SBIR | завершена |  |  | 0 | 0 |
| [SHIELDER / STTR](programs/shielder/README.md) | Scalable Hard-mask materials with Improved Etch resistance and Low Degradation for Extreme-aspect-Ratio fabrication | завершена |  |  | 0 | 0 |
| [SMART / SBIR](programs/smart/README.md) | Spectrum Monitoring and Awareness in Real-Time - Open Topic | завершена |  |  | 0 | 0 |
| [SPEED DIAL / STTR](programs/speed-dial/README.md) | Scalable Platform for Enterprise Engineering and Deployment towards Mathematics for the Discovery of Algorithms and Architectures | завершена |  |  | 0 | 0 |
| [Spreaders for Microsystems with Advanced Thermal Resilience / SBIR](programs/spreaders-for-microsystems-with-advanced-thermal-resilience/README.md) | Spreaders for Microsystems with Advanced Thermal Resilience / SBIR | завершена | БПЛА |  | 0 | 0 |
| [SWiFT / SBIR](programs/swift/README.md) | Smart Whole Blood Field Transfusion System | завершена |  |  | 0 | 0 |
| [THERMAL / SBIR](programs/thermal/README.md) | Temperature-Hardened Electronics for Reliable Mission-Critical Applications | завершена |  |  | 0 | 0 |
| [TurboFCL](programs/turbofcl/README.md) | Turbo Facility Clearance (TurboFCL) | завершена |  |  | 0 | 0 |
| [Turbulent Boundary Layer Drag Reduction via Surface Actuators / SBIR](programs/turbulent-boundary-layer-drag-reduction-vias-surface-actuators/README.md) | Turbulent Boundary Layer Drag Reduction via Surface Actuators / SBIR | завершена |  |  | 0 | 0 |
| [UC-RAPID / SBIR](programs/uc-rapid/README.md) | Universal Cell Culture Platform for Rapid Establishment of Species-Agnostic Cell Lines and Autonomous Culture Operations | завершена |  |  | 0 | 0 |
| [Unbiased Behavioral Discovery Platforms / SBIR](programs/unbiased-behavioral-discovery-platforms/README.md) | Unbiased Behavioral Discovery Platforms / SBIR | завершена |  |  | 0 | 0 |

<a id="office-do"></a>

## Director's Office (DO) — офис директора — 1

| Программа | Полное название | Статус | Сфера | Руководитель (darpa.mil) | Исполнителей | Новостей |
|---|---|---|---|---|---|---|
| [IMPAQT](programs/impaqt/README.md) | Imaging Practical Applications for a Quantum Tomorrow | завершена |  |  | 0 | 0 |

<a id="office-none"></a>

## Офис не указан на странице darpa.mil — 68

| Программа | Полное название | Статус | Сфера | Руководитель (darpa.mil) | Исполнителей | Новостей |
|---|---|---|---|---|---|---|
| [AI Forward](programs/ai-forward/README.md) | AI Forward | действует |  |  | 0 | 0 |
| [AI Next](programs/ai-next/README.md) | AI Next | завершена |  |  | 0 | 0 |
| [AMCOM-DI / SBIR](programs/amcom-di/README.md) | Autonomous Metacognitive Collection Orchestration for Multi-Domain Intelligence | действует |  |  | 0 | 0 |
| [Angler](programs/angler/README.md) | Angler | статус не установлен |  |  | 4 | 0 |
| [ARPANET](programs/arpanet/README.md) | ARPANET | завершена |  |  | 1 | 0 |
| [BEAMERS](programs/beamers/README.md) | BEamspace Analog processing for Multi-functional Enhanced RF Systems | статус не установлен |  |  | 0 | 1 |
| [BigDog](programs/bigdog/README.md) | BigDog | завершена |  |  | 0 | 0 |
| [CKC](programs/ckc/README.md) | Collaborative Knowledge Curation | действует |  |  | 0 | 0 |
| [COMPASS](programs/compass/README.md) | Critical Orientation of Mathematics to Produce Advancements in Science and Security | действует |  |  | 0 | 0 |
| [CRYSTAL](programs/crystal-substrate-bonding/README.md) | Crystal Substrate Bonding Technologies and Algorithms | действует |  |  | 0 | 0 |
| [DUF](programs/duf/README.md) | Discovering Unknome Function | действует |  |  | 0 | 0 |
| [FAARM](programs/faarm/README.md) | Fuel Access Anywhere, Regardless of Means | действует |  |  | 0 | 0 |
| [GLUE](programs/glue/README.md) | Grip Likelihood in Underwater Environments | действует |  |  | 0 | 0 |
| [HALOVS](programs/halovs/README.md) | Highly Accelerated Learning of Vibratory Systems | действует |  | Sunil Bhave | 0 | 0 |
| [Human Universal Remote / SBIR](programs/human-universal-remote/README.md) | Human Universal Remote / SBIR | действует |  |  | 0 | 0 |
| [HyBRIDS](programs/hybrids/README.md) | Hybridizing Biology and Robotics through Integration for Deployable Systems | действует |  |  | 0 | 0 |
| [HYPER-CAP / SBIR](programs/hyper-cap/README.md) | Hyperdimensional Neurosymbolic Cyber Course-of-Action Planning and Replanning under Obfuscation | действует |  |  | 0 | 0 |
| [INSPIRE](programs/inspire/README.md) | Investigating how Neurological Systems Process Information in Reality | действует |  |  | 0 | 0 |
| [MAGICS](programs/methodological-advancements-generalizable-insights-complex-systems/README.md) | Methodological Advancements for Generalizable Insights into Complex Systems | действует |  |  | 0 | 0 |
| [MOABB](programs/modular-optical-aperture-building-blocks/README.md) | Modular Optical Aperture Building Blocks | завершена |  |  | 1 | 0 |
| [MOCCA](programs/mobile-offboard-clandestine-communications-and-approach/README.md) | Mobile Offboard Clandestine Communications and Approach | завершена | БПЛА |  | 1 | 0 |
| [MOIRE](programs/membrane-optic-imager-real-time-exploitation/README.md) | Membrane Optic Imager Real-Time Exploitation | завершена |  |  | 0 | 0 |
| [Molecular Informatics](programs/molecular-informatics/README.md) | Molecular Informatics | завершена |  |  | 0 | 0 |
| [MPD](programs/microscale-plasma-devices/README.md) | Microscale Plasma Devices | завершена |  |  | 0 | 0 |
| [MTM](programs/military-tactical-means/README.md) | Military Tactical Means | завершена |  |  | 0 | 0 |
| [NAC](programs/nature-as-computer/README.md) | Nature as Computer | завершена |  |  | 0 | 0 |
| [Network UP](programs/network-universal-persistence/README.md) | Network Universal Persistence | завершена |  |  | 0 | 0 |
| [NEXT](programs/nitride-electronic-next-generation-technology/README.md) | Nitride Electronic NeXt-Generation Technology | завершена |  |  | 0 | 0 |
| [NGMM](programs/next-generation-microelectronics/README.md) | Next-Generation Microelectronics Manufacturing | действует |  | Michael Holmes | 0 | 0 |
| [NGS2](programs/next-generation-social-science/README.md) | Next Generation Social Science | завершена |  |  | 3 | 0 |
| [Nimbus](programs/nimbus/README.md) | Nimbus | завершена |  |  | 1 | 0 |
| [NLMI](programs/nascent-light-matter-interactions/README.md) | Nascent Light-Matter Interactions | завершена |  |  | 0 | 0 |
| [O2](programs/orbitoutlook/README.md) | OrbitOutlook | завершена |  |  | 0 | 0 |
| [PAL](programs/pal/README.md) | Personalized Assistant that Learns | завершена |  |  | 2 | 0 |
| [PAPPA](programs/performant-automation-of-parallel-program-assembly/README.md) | Performant Automation of Parallel Program Assembly | завершена |  |  | 0 | 0 |
| [PFC](programs/protected-forward-communications/README.md) | Protected Forward Communications | завершена | БПЛА, средства связи и коммуникаций |  | 0 | 0 |
| [Phorcys](programs/phorcys/README.md) | Phorcys | завершена |  |  | 0 | 0 |
| [POSH](programs/posh-open-source-hardware/README.md) | Posh Open Source Hardware | завершена |  |  | 0 | 0 |
| [POSYDON](programs/positioning-system-for-deep-ocean-navigation/README.md) | Positioning System for Deep Ocean Navigation | завершена |  |  | 0 | 0 |
| [PROTEUS](programs/prototype-resilient-operations-testbed-for-expeditionary-urban-scenarios/README.md) | Prototype Resilient Operations Testbed for Expeditionary Urban Scenarios | завершена |  |  | 2 | 0 |
| [QUAMELEON](programs/quameleon/README.md) | QUAntum Materials Engineering using eLEctrOmagNetic fields | действует |  |  | 0 | 0 |
| [RADER](programs/remoted-analog-to-digital-converter-with-de-serialization-and-reconstruction/README.md) | Remoted Analog-to-Digital Converter with De-serialization and Reconstruction | завершена |  |  | 1 | 0 |
| [Resilient Software Systems Capstone](programs/resilient-software-systems-capstone/README.md) | Resilient Software Systems Capstone | действует |  | Stephen Kuhn | 0 | 0 |
| [REVEAL](programs/revolutionary-enhancement-visibility/README.md) | Revolutionary Enhancement of Visibility by Exploiting Active Light-fields | завершена |  |  | 7 | 0 |
| [RMS](programs/reactive-material-structures/README.md) | Reactive Material Structures | завершена |  |  | 1 | 0 |
| [RSPACE](programs/resilient-synchronized-planning/README.md) | Resilient Synchronized Planning and Assessment for the Contested Environment | завершена |  |  | 0 | 0 |
| [SAFRON](programs/safron/README.md) | Safe and Assured Foundation Robots for Open Environments | действует |  |  | 0 | 0 |
| [SAIL-ON](programs/science-artificial-intelligence-and-learning-for-open-world-novelty/README.md) | Science of Artificial Intelligence and Learning for Open-world Novelty | завершена |  |  | 4 | 0 |
| [SCENICC](programs/soldier-centric-imaging-via-computational-cameras/README.md) | Soldier Centric Imaging via Computational Cameras | завершена |  |  | 0 | 0 |
| [SCOUT](programs/spectral-combs-uv-to-thz/README.md) | Spectral Combs from UV to THz | завершена |  |  | 0 | 0 |
| [SDR 4.0](programs/software-defined-radio/README.md) | Software Defined Radio 4.0 | завершена | средства связи и коммуникаций |  | 0 | 0 |
| [SECTR](programs/seeker-cost-transformation/README.md) | Seeker Cost Transformation | завершена |  |  | 0 | 0 |
| [SenSARS](programs/sensars/README.md) | SenSARS | завершена |  |  | 0 | 0 |
| [SESU](programs/system-of-systems-enhanced-small-unit/README.md) | System-of-Systems Enhanced Small Unit | завершена | БПЛА |  | 5 | 0 |
| [SI3-CMD](programs/serial-interactions-in-imperfect-information-games-applied-to-complex-military-decision-making/README.md) | Serial Interactions in Imperfect Information Games Applied to Complex Military Decision Making | завершена |  |  | 0 | 0 |
| [SIMPLEX](programs/simplifying-complexity-in-scientific-discovery/README.md) | Simplifying Complexity in Scientific Discovery | завершена |  |  | 2 | 0 |
| [Small Satellite Sensors](programs/small-satellite-sensors/README.md) | Small Satellite Sensors | завершена |  |  | 0 | 0 |
| [SoSITE](programs/system-of-systems-integration-technology-and-experimentation/README.md) | System of Systems Integration Technology and Experimentation | завершена |  |  | 1 | 0 |
| [SPAR](programs/signal-processing-at-rf/README.md) | Signal Processing at RF | завершена |  |  | 2 | 0 |
| [SPREE](programs/spree/README.md) | Separation and Purification of Rare Earth Elements | действует |  |  | 0 | 0 |
| [SPS](programs/soldier-protection-systems/README.md) | Soldier Protection Systems | завершена |  |  | 0 | 0 |
| [SSPARC](programs/shared-spectrum-access-for-radar-and-communications/README.md) | Shared Spectrum Access for Radar and Communications | завершена |  |  | 8 | 0 |
| [Structural Logic](programs/structural-logic/README.md) | Structural Logic | завершена |  |  | 3 | 0 |
| [SWEEPER](programs/short-range-wide-field-of-view-extremely-agile-electronically-steered-photonic-emitter/README.md) | Short-Range, Wide Field-of-View Extremely agile, Electronically Steered Photonic Emitter | завершена |  |  | 3 | 0 |
| [SyNAPSE](programs/systems-of-neuromorphic-adaptive-plastic-scalable-electronics/README.md) | Systems of Neuromorphic Adaptive Plastic Scalable Electronics | завершена |  |  | 0 | 0 |
| [TRIAGE-X / SBIR](programs/triage-x/README.md) | Autonomous Casualty Triage and Treatment in Chemically Contaminated Mass Casualty Events | действует |  |  | 0 | 0 |
| [XSolids](programs/extended-solids/README.md) | Extended Solids | завершена |  |  | 0 | 0 |
| [µBRAIN](programs/microbrain/README.md) | µBRAIN | завершена |  |  | 0 | 0 |

## Таблицы

- `data/darpa_programs.csv`, `data/darpa_orgs.csv`, `data/darpa_program_orgs.csv`, `data/darpa_personnel.csv` — реестр;
- `data/darpa_contracts_usaspending.csv` — контракты и гранты по программам (USAspending.gov);
- `data/darpa_item_tags.json` — разметка новостей; `LEAD_CHECK.md` — проверка вводного списка; `UNASSIGNED.md` — материалы с DARPA без названной программы.

## Листинг организаций

- поглощена / входит в группу: 10
- закрыта: 1
- торгуется на бирже: 24
- частная: 22
- не установлено: 302

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
