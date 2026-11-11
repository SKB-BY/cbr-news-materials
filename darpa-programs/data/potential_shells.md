# Дочерние структуры вне реестра (potential shells) — рабочий список

**Рабочий список, не обвинение и не факты реестра.** Строка = юридическая дочерняя структура компании из `darpa_orgs.csv` (по Exhibit 21 последнего годового отчёта в SEC EDGAR), которая названа в материале с контекстом DARPA (`darpa_item_tags.json`), но отсутствует в `darpa_orgs.csv`. В реестр ничего не вносится автоматически.

Компаний с листингом: 24; дочерних структур в Exhibit 21: 845 (`sec_subsidiaries.csv`); материалов в разметке: 23 (с текстом из news.sqlite).

## Кандидаты

Совпадений нет: ни одна дочерняя структура из Exhibit 21 не названа в размеченных материалах с контекстом DARPA.

## Проверенные отчёты

| Компания | CIK | Отчёт | Источник | Результат |
|---|---|---|---|---|
| Lockheed Martin | 936468 | 10-K 2026-01-29 | [SEC](https://www.sec.gov/Archives/edgar/data/936468/000162828026004195/ex21q42025.htm) | дочерних структур: 14 |
| Boeing | 12927 | 10-K 2026-01-30 | [SEC](https://www.sec.gov/Archives/edgar/data/12927/000162828026004357/a202512dec3110kex21.htm) | дочерних структур: 19 |
| Northrop Grumman | 1133421 | 10-K 2026-01-27 | [SEC](https://www.sec.gov/Archives/edgar/data/1133421/000113342126000003/noc-12312025xex21.htm) | дочерних структур: 2 |
| RTX (Raytheon) | 101829 | 10-K 2026-02-06 | [SEC](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/exhibit212025-12x3110xk.htm) | дочерних структур: 36 |
| Moderna | 1682852 | 10-K 2026-02-20 | [SEC](https://www.sec.gov/Archives/edgar/data/1682852/000168285226000033/exhibit211subsidiaries1231.htm) | дочерних структур: 29 |
| SpaceX (Space Exploration Technologies Corp.) | 1181412 |  | — | годового отчёта 10-K/20-F/40-F в последних подачах нет |
| IonQ | 1824920 | 10-K 2026-02-25 | [SEC](https://www.sec.gov/Archives/edgar/data/1824920/000119312526071562/ionq-ex21_1.htm) | дочерних структур: 21 |
| Rigetti Computing | 1838359 | 10-K 2026-03-04 | [SEC](https://www.sec.gov/Archives/edgar/data/1838359/000110465926023454/rgti-20251231xex21d1.htm) | дочерних структур: 7 |
| Quantinuum | 2110105 |  | — | годового отчёта 10-K/20-F/40-F в последних подачах нет |
| IBM | 51143 | 10-K 2026-02-24 | [SEC](https://www.sec.gov/Archives/edgar/data/51143/000005114326000010/ibm-20251231x10kex21.htm) | дочерних структур: 100 |
| Microsoft | 789019 | 10-K 2026-07-29 | [SEC](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-ex21.htm) | дочерних структур: 9 |
| Xanadu | 2097163 | 20-F 2026-04-09 | [SEC](https://www.sec.gov/Archives/edgar/data/2097163/000121390026042080/0001213900-26-042080-index.htm) | Exhibit 21 в подаче не найден |
| Firefly Aerospace | 1860160 | 10-K 2026-03-20 | [SEC](https://www.sec.gov/Archives/edgar/data/1860160/000119312526116309/0001193125-26-116309-index.htm) | Exhibit 21 в подаче не найден |
| Redwire | 1819810 | 10-K 2026-02-27 | [SEC](https://www.sec.gov/Archives/edgar/data/1819810/000181981026000029/exhibit21-subsidiariesofth.htm) | дочерних структур: 32 |
| Amentum | 2011286 | 10-K 2025-11-25 | [SEC](https://www.sec.gov/Archives/edgar/data/2011286/000162828025053993/amtm100325ex211.htm) | дочерних структур: 181 |
| Booz Allen Hamilton | 1443646 | 10-K 2026-05-22 | [SEC](https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/exhibit21-subsidiarieslist.htm) | дочерних структур: 61 |
| BAE Systems | 895564 |  | — | годового отчёта 10-K/20-F/40-F в последних подачах нет |
| Palantir Technologies | 1321655 | 10-K 2026-02-17 | [SEC](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/a2025fyexhibit211.htm) | дочерних структур: 31 |
| Leidos | 1336920 | 10-K 2026-02-17 | [SEC](https://www.sec.gov/Archives/edgar/data/1336920/000133692026000030/ldos1022026ex21.htm) | дочерних структур: 24 |
| AeroVironment | 1368622 | 10-K 2026-06-29 | [SEC](https://www.sec.gov/Archives/edgar/data/1368622/000110465926078906/avav-20260430xex21d1.htm) | дочерних структур: 2 |
| Aurora Innovation | 1828108 | 10-K 2026-02-11 | [SEC](https://www.sec.gov/Archives/edgar/data/1828108/000182810826000016/a25q4ex211.htm) | дочерних структур: 3 |
| Palladyne AI (бывш. Sarcos) | 1826681 | 10-K 2026-03-05 | [SEC](https://www.sec.gov/Archives/edgar/data/1826681/000119312526092443/pdyn-ex21.htm) | дочерних структур: 8 |
| L3Harris Technologies | 202058 | 10-K 2026-02-12 | [SEC](https://www.sec.gov/Archives/edgar/data/202058/000020205826000015/a10-kexhibit21cy25xq4.htm) | дочерних структур: 126 |
| Textron | 217346 | 10-K 2026-02-11 | [SEC](https://www.sec.gov/Archives/edgar/data/217346/000021734626000006/q4202510k-exx21.htm) | дочерних структур: 140 |
