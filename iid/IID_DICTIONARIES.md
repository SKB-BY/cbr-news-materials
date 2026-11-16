# ИИД-100 — словари признаков, упоминаний, топонимов и организаций

Версия словарей: `iid-lex-1` (2026-11-16). Методика: `iid100-1`. Составлены вручную, без обучения и без машинного перевода; изменение словаря — новая версия методики, прежние значения не перезаписываются.

Правила совпадения:

- **Признак окраса и субъективности** — основа слова; совпадение с начала слова (основа + любое окончание). Основа из 4 и менее букв — только целое слово с окончаниями языка. Фраза — основы подряд.
- **Упоминание, топоним, организация** — основа + фиксированный список окончаний языка, по границе слова.
- Окрас считается только по предложениям, где названа Беларусь; Субъективность — по всему материалу.
- Организации реестра (`companies_data.MENTION_RE`, в т. ч. организации системы ГВПК с пометкой BY) подключаются при каждом расчёте; организации с пометкой BY — тоже признак упоминания Беларуси.

## Размер словарей по языкам

| Язык | окончаний | служебных слов | признаков окраса/субъективности | форм упоминаний РБ | форм топонимов | форм организаций |
|---|---|---|---|---|---|---|
| ru (русский) | 45 | 31 | 135 | 19 | 44 | 12 |
| be (белорусский) | 30 | 25 | 117 | 12 | 46 | 10 |
| uk (украинский) | 29 | 27 | 118 | 12 | 42 | 13 |
| pl (польский) | 30 | 28 | 117 | 17 | 58 | 12 |
| lt (литовский) | 36 | 26 | 115 | 11 | 41 | 12 |
| lv (латышский) | 25 | 22 | 115 | 10 | 39 | 10 |
| en (английский) | 11 | 25 | 121 | 15 | 50 | 11 |
| de (немецкий) | 16 | 26 | 124 | 14 | 41 | 11 |

## Упоминания Беларуси

**BY — Беларусь** (страна)  
- ru: `беларус`, `белорус`, `белоруси`, `белорусск`, `белорусси`, `республик беларусь`
- be: `беларус`, `беларуск`, `рэспублік беларусь`
- uk: `білорус`, `біларус`, `білоруськ`, `республік білорусь`
- pl: `białoru`, `białorusk`, `bialorus`, `bialorusk`, `białorusin`, `białorusini`
- lt: `baltarus`, `baltarusij`, `baltarusiš`
- lv: `baltkriev`, `baltkrievij`
- en: `belarus`, `belarusian`, `byelorussia`, `belorussia`, `belarussian`
- de: `belarus`, `belarussisch`, `belarusse`, `weißrussland`, `weissrussland`, `weißrussisch`, `weissrussisch`

**BY-PRES — Лукашенко А.Г. (Президент РБ)** (лицо)  
- ru: `лукашенк`, `лукашенко`
- be: `лукашэнк`, `лукашэнка`
- uk: `лукашенк`, `лукашенко`
- pl: `łukaszenk`, `lukaszenk`, `łukaszenka`, `lukaszenka`, `łukaszenko`
- lt: `lukašenk`, `lukasenk`, `lukašenka`
- lv: `lukašenk`, `lukasenk`, `lukašenko`
- en: `lukashenk`, `lukashenko`, `lukashenka`
- de: `lukaschenk`, `lukaschenko`

**BY-GOV — органы власти РБ (белорусские министерства и ведомства)** (организация)  
- ru: `минобороны беларуси`, `мид беларуси`, `госпогранкомитет`, `кгб беларуси`, `мвд беларуси`, `совмин беларуси`, `белорусск мид`, `белорусск минобороны`, `белорусск пограничник`, `белорусск власт`, `официальн минск`
- be: `міністэрства абароны беларусі`, `мзс беларусі`, `дзяржпамежкамітэт`, `кдб беларусі`, `беларуск памежнік`, `беларуск улад`, `афіцыйн мінск`
- uk: `міноборони білорусі`, `мзс білорусі`, `кдб білорусі`, `білоруськ прикордонник`, `білоруськ влад`, `офіційн мінськ`
- pl: `białorusk mswiz`, `białorusk msz`, `białorusk kgb`, `białorusk pogranicz`, `białorusk władz`, `oficjaln mińsk`
- lt: `baltarusijos užsienio reikalų ministerij`, `baltarusijos kgb`, `baltarusijos pasienieč`, `baltarusijos valdži`, `oficialus minskas`
- lv: `baltkrievijas ārlietu ministrij`, `baltkrievijas čeka`, `baltkrievijas robežsarg`, `baltkrievijas varas`, `oficiālā minska`
- en: `belarusian foreign ministry`, `belarusian defence ministry`, `belarusian defense ministry`, `belarusian kgb`, `belarusian border guard`, `belarusian authorities`, `official minsk`
- de: `belarussisch außenministerium`, `belarussisch grenzschutz`, `belarussisch behörden`, `belarussisch kgb`, `offizielle minsk`

## Топонимы (ключи «место»; BY — населённый пункт РБ, тоже признак упоминания)

| Код | Место | BY | Формы по языкам |
|---|---|---|---|
| BY-MSQ | Минск | да | ru: минск; be: мінск; uk: мінськ, минск; pl: mińsk, minsk; lt: minsk; lv: minsk; en: minsk; de: minsk |
| BY-BRE | Брест | да | ru: брест; be: брэст; uk: брест; pl: brześć, brześci, brzesc; lt: brest; lv: brest; en: brest-litovsk, brest, belarus; de: brest-litowsk |
| BY-GRO | Гродно | да | ru: гродн; be: гродн; uk: гродн; pl: grodn; lt: gardin; lv: grodņ, grodn; en: grodno, hrodna; de: grodno |
| BY-GOM | Гомель | да | ru: гомел; be: гомел; uk: гомел; pl: homel, homl; lt: gomel; lv: gomeļ, gomel; en: gomel, homel; de: gomel |
| BY-VIT | Витебск | да | ru: витебск; be: віцебск; uk: вітебськ; pl: witebsk; lt: vitebsk; lv: vitebsk; en: vitebsk, viciebsk; de: witebsk |
| BY-MOG | Могилёв | да | ru: могилев, могилёв; be: магілёв, магілев; uk: могильов; pl: mohylew; lt: mogiliov; lv: mogiļov, mogilev; en: mogilev, mahilyow; de: mogiljow |
| BY-BAR | Барановичи | да | ru: баранович; be: баранавіч; uk: баранович; pl: baranowicz; lt: baranovič; lv: baranoviči; en: baranovichi; de: baranowitschi |
| BY-BOR | Борисов | да | ru: борисов; be: барысаў, барысав; uk: борисов; pl: borysów, borysow; lt: borisov; lv: borisov; en: borisov, barysaw; de: baryssau, borissow |
| BY-BOB | Бобруйск | да | ru: бобруйск; be: бабруйск; uk: бобруйськ; pl: bobrujsk; lt: babruisk; lv: bobruiska; en: bobruisk, babruysk; de: babrujsk |
| BY-PIN | Пинск | да | ru: пинск; be: пінск; uk: пінськ; pl: pińsk; lt: pinsk; lv: pinsk; en: pinsk; de: pinsk |
| BY-ORS | Орша | да | ru: орш; be: орш; uk: орш; pl: orsz; lt: orša; lv: orša; en: orsha; de: orscha |
| BY-LID | Лида | да | ru: лид; be: лід; uk: лід; pl: lid; lt: lyd; lv: lida; en: lida; de: lida |
| BY-MOZ | Мозырь | да | ru: мозыр; be: мазыр; uk: мозир; pl: mozyrz; lt: mozyr; lv: mozira; en: mozyr; de: masyr |
| BY-POL | Полоцк/Новополоцк | да | ru: полоцк, новополоцк; be: полацк, наваполацк; uk: полоцьк, новополоцьк; pl: połock, nowopołock; lt: polock; lv: polocka; en: polotsk, novopolotsk; de: polozk, nowopolozk |
| BY-OST | Островец (БелАЭС) | да | ru: островец, белаэс, белорусск аэс; be: астравец, беларуск аэс; uk: островець, білоруськ аес; pl: ostrowiec, elektrowni w ostrowcu, astraviec; lt: astravo, astravj, astravas; lv: astravjec, astravas; en: astravets, ostrovets; de: astrawez, ostrowez |
| BY-MCH | Мачулищи | да | ru: мачулищ; be: мачулішч; uk: мачулищ; pl: maczuliszcz; lt: mačuliš; lv: mačulišči; en: machulishchy, machulishchi; de: matschulischtschy |
| BY-ZYA | Зябровка | да | ru: зябровк; be: зябраўк; uk: зябровк; pl: ziabrowk; lt: zabrovk; lv: zjabrovk; en: zyabrovka, ziabrauka; de: sjabrowka |
| BY-PTK | пункты пропуска РБ (Брузги, Беняконе, Каменный Лог, Григоровщина, Козловичи, Песчатка, Новая Гута) | да | ru: брузг, бенякон, каменн лог, григоровщин, козлович, песчатк, нов гут; be: брузгі, беняконі, каменн лог, грыгароўшчын, казловіч, пясчатк, нов гут; uk: брузг, бенякон, кам'ян лог, григорівщин, козлович; pl: bruzgi, kuźnic, bobrownik, terespol, koroszczyn, sławatycz, połowc; lt: medinink, šalčinink, lavoriškės, raigard, tverečius, vidzai; lv: paterniek, silen, urbanov; en: bruzgi, kuznica, medininkai, salcininkai, paternieki, terespol; de: bruzgi, kuźnica, medininkai, terespol |
| LT-VNO | Вильнюс |  | ru: вильнюс; be: вільнюс, вільня; uk: вільнюс; pl: wilno, wilni, wilnie, wilnem, vilnius; lt: vilni, vilnius; lv: viļņ; en: vilnius; de: vilnius, wilna |
| PL-WAW | Варшава |  | ru: варшав; be: варшав; uk: варшав; pl: warszaw; lt: varšuv; lv: varšav; en: warsaw; de: warschau |
| PL-BIA | Белосток |  | ru: белосток; be: беласток; uk: білосток; pl: białyst, białymst, bialyst; lt: balstog; lv: belostok; en: bialystok; de: bialystok |
| LV-RIX | Рига |  | ru: риг; be: рыг; uk: риг; pl: ryd, ryg; lt: ryg; lv: rīg; en: riga; de: riga |
| UA-KYI | Киев |  | ru: киев; be: кіев; uk: київ, києв; pl: kijów, kijow, kijow; lt: kyjiv, kijev; lv: kijiv, kijev; en: kyiv, kiev; de: kiew |
| RU-MOW | Москва |  | ru: москв; be: маскв; uk: москв; pl: moskw; lt: maskv; lv: maskav; en: moscow; de: moskau |
| SUW | Сувалкский коридор |  | ru: сувалк; be: сувалк; uk: сувалк; pl: suwał, suwal; lt: suvalk; lv: suvalk; en: suwalki; de: suwalki |
| LT | Литва |  | ru: литв, литовск; be: літв, літоўск; uk: литв, литовськ; pl: litw, litewsk; lt: lietuv; lv: lietuv, lietuviešu; en: lithuania; de: litauen, litauisch |
| PL | Польша |  | ru: польш, польск; be: польшч, польск; uk: польщ, польськ; pl: polsk, polsc; lt: lenkij, lenkų; lv: polij, poļu; en: poland, polish; de: polen, polnisch |
| LV | Латвия |  | ru: латви, латвийск; be: латвi, латвійск; uk: латві, латвійськ; pl: łotw, łotewsk; lt: latvij; lv: latvij; en: latvia, latvian; de: lettland, lettisch |
| UA | Украина |  | ru: украин; be: украін, украiн; uk: україн; pl: ukrain; lt: ukrain; lv: ukrain; en: ukrain; de: ukrain |
| RU | Россия |  | ru: росси, российск; be: расі, расійск; uk: росі, російськ; pl: rosj, rosyjsk; lt: rusij, rusijos; lv: krievij; en: russia, russian; de: russland, russisch |

## Организации (ключи «организация»)

| Код | Организация | Формы по языкам |
|---|---|---|
| NATO | НАТО | ru: нато; be: ната; uk: нато; pl: nato; lt: nato; lv: nato; en: nato; de: nato |
| EU | Европейский союз | ru: евросоюз, европейск союз, ес; be: еўрасаюз, еўрапейск саюз; uk: євросоюз, європейськ союз, єс; pl: unia europejsk, ue; lt: europos sąjung, es; lv: eiropas savienīb; en: european union, eu; de: europäisch union, eu |
| UN | ООН | ru: оон; be: аан; uk: оон; pl: onz; lt: jt, jungtinių tautų; lv: ano; en: united nations, un; de: vereinten nationen, uno |
| OSCE | ОБСЕ | ru: обсе; be: абсе; uk: обсє; pl: obwe; lt: esbo; lv: edso; en: osce; de: osze |
| FRONTEX | Frontex | ru: фронтекс; be: фронтэкс; uk: фронтекс; pl: frontex; lt: frontex; lv: frontex; en: frontex; de: frontex |
| WAGNER | ЧВК «Вагнер» | ru: вагнер, чвк вагнер; be: вагнер; uk: вагнер, пвк вагнер; pl: wagner, grupa wagnera; lt: vagner, wagner; lv: vāgner, wagner; en: wagner; de: wagner |
| ORESHNIK | «Орешник» | ru: орешник; be: арэшнік; uk: орєшнік, орешник; pl: oriesznik, oresznik; lt: orešnik; lv: orešņik; en: oreshnik; de: oreschnik |
| CSTO | ОДКБ | ru: одкб; be: адкб; uk: одкб; pl: oubz; lt: kssto; lv: kdlo; en: csto; de: ovks |
| UNION-STATE | Союзное государство | ru: союзн государств; be: саюзн дзяржав; uk: союзн держав; pl: państw związkow; lt: sąjungin valstyb; lv: savienīb valst; en: union state; de: unionsstaat |

## Признаки окраса и субъективности

### ru — русский

- **сильные негативные (вес 2)** (25): `санкци`, `уголовн`, `арест`, `авари`, `катастроф`, `крушени`, `погиб`, `гибел`, `банкрот`, `обвин`, `коррупц`, `мошенн`, `хищен`, `взятк`, `репресси`, `диктатор`, `диктатур`, `террор`, `военн преступлен`, `соучаст`, `пособни`, `гибридн атак`, `агресси`, `оккупац`, `марионет`
- **негативные (вес 1)** (46): `задерж`, `срыв`, `сорва`, `отстава`, `сокращ`, `критик`, `проблем`, `дефицит`, `нехватк`, `недостат`, `риск`, `спор`, `иск`, `суд`, `отказ`, `сбой`, `уязвим`, `отмен`, `уничтож`, `сбит`, `поражен`, `удар`, `атак`, `потер`, `угроз`, `провокац`, `нарушен`, `нарушил`, `эскалац`, `запрет`, `ограничен`, `закрыт границ`, `закрыли границ`, `высыл`, `протест`, `осужд`, `осудил`, `шпион`, `контрабанд`, `нелегальн`, `незаконн`, `давлени`, `режим лукашенк`, `лукашенковск режим`, `вторжен`, `дестабилиз`
- **сильные позитивные (вес 2)** (10): `крупн инвестиц`, `рекордн`, `прорыв`, `снят ограничен`, `господдержк`, `государственн поддержк`, `млрд инвестиц`, `млрд контракт`, `снят санкц`, `отмен санкц`
- **позитивные (вес 1)** (23): `контракт`, `заказ`, `запуск`, `запустил`, `рост`, `увелич`, `расшир`, `успешн`, `принят на вооружение`, `модерниз`, `поставк`, `получил`, `сотруднич`, `партнерств`, `партнёрств`, `диалог`, `нормализац`, `освобожд`, `помилов`, `соглашен`, `договор`, `гуманитарн помощ`, `деэскалац`
- **оценочные слова (Субъективность)** (25): `позор`, `шок`, `сенсац`, `катастрофическ`, `ужасн`, `предательств`, `героическ`, `блестящ`, `триумф`, `провал`, `бездарн`, `невероятн`, `скандальн`, `чудовищн`, `циничн`, `наглый`, `наглая`, `наглое`, `наглые`, `абсурдн`, `возмутительн`, `кровав`, `преступн режим`, `людоедск`, `истерик`
- **речь от первого лица (Субъективность)** (6): `я считаю`, `по моему мнению`, `на мой взгляд`, `мы считаем`, `по-моему`, `я уверен`
- **окончания** (45): `∅`, `ь`, `ью`, `а`, `я`, `у`, `ю`, `е`, `и`, `ы`, `о`, `ом`, `ем`, `ой`, `ей`, `ою`, `ею`, `ам`, `ям`, `ами`, `ями`, `ах`, `ях`, `ов`, `ев`, `ий`, `ый`, `ая`, `яя`, `ое`, `ее`, `ие`, `ые`, `ого`, `его`, `ому`, `ему`, `ым`, `им`, `ых`, `их`, `ую`, `юю`, `ыми`, `ими`
- **служебные слова для определения языка** (31): и, в, не, на, что, с, по, как, это, его, но, он, из, за, от, для, то, же, уже, или, так, при, было, который, которые, также, после, чтобы, ещё, может, более
- **месяцы (для ключей-дат)**: январ, феврал, март, апрел, ма, июн, июл, август, сентябр, октябр, ноябр, декабр

### be — белорусский

- **сильные негативные (вес 2)** (26): `санкцы`, `крымінальн`, `арышт`, `аварыі`, `аварый`, `катастроф`, `крушэнн`, `загін`, `гібел`, `банкрут`, `абвінав`, `карупц`, `махляр`, `крадзеж`, `хабар`, `рэпрэсі`, `дыктатар`, `дыктатур`, `тэрор`, `ваенн злачынств`, `саўдзел`, `памагат`, `гібрыдн атак`, `агрэсі`, `акупац`, `марыянет`
- **негативные (вес 1)** (43): `затрым`, `зрыў`, `сарва`, `адстава`, `скарач`, `крытык`, `праблем`, `дэфіцыт`, `недахоп`, `рызык`, `спрэчк`, `іск`, `суд`, `адмов`, `збой`, `уразлів`, `адмен`, `знішч`, `збіт`, `паражэнн`, `удар`, `атак`, `страт`, `пагроз`, `правакац`, `парушэнн`, `парушыў`, `эскалац`, `забарон`, `абмежаван`, `закрыццё мяж`, `высыл`, `пратэст`, `асудж`, `асудзіў`, `шпіён`, `кантрабанд`, `нелегальн`, `незаконн`, `ціск`, `рэжым лукашэнк`, `уварван`, `дэстабіліз`
- **сильные позитивные (вес 2)** (7): `буйн інвестыц`, `рэкордн`, `прарыў`, `зняцц абмежаван`, `дзяржпадтрымк`, `зняцц санкц`, `адмен санкц`
- **позитивные (вес 1)** (18): `кантракт`, `заказ`, `запуск`, `рост`, `павелічэн`, `пашырэн`, `паспяхов`, `мадэрніз`, `пастаўк`, `атрымаў`, `супрацоўніц`, `партнёрств`, `дыялог`, `нармалізац`, `вызвален`, `памілав`, `пагадненн`, `дамов`
- **оценочные слова (Субъективность)** (19): `ганьб`, `шок`, `сенсацы`, `катастрафічн`, `жахлів`, `здрад`, `гераічн`, `бліскуч`, `трыумф`, `правал`, `бяздарн`, `неверагодн`, `скандальн`, `пачварн`, `цынічн`, `нахабн`, `абсурдн`, `крывав`, `злачынн рэжым`
- **речь от первого лица (Субъективность)** (4): `я лічу`, `на маю думку`, `на мой погляд`, `мы лічым`
- **окончания** (30): `∅`, `ь`, `і`, `ю`, `а`, `у`, `е`, `ы`, `ам`, `ем`, `ай`, `ой`, `ою`, `ам`, `амі`, `ах`, `оў`, `ая`, `ае`, `ія`, `ыя`, `ага`, `аму`, `ым`, `ім`, `ых`, `іх`, `ую`, `ымі`, `імі`
- **служебные слова для определения языка** (25): і, ў, не, на, што, з, па, як, гэта, яго, але, ён, з, за, ад, для, таксама, пасля, каб, яшчэ, можа, больш, які, якія, было
- **месяцы (для ключей-дат)**: студзен, лют, сакавік, красавік, мая, чэрвен, ліпен, жнівен, верасн, кастрычнік, лістапад, снежн

### uk — украинский

- **сильные негативные (вес 2)** (25): `санкці`, `кримінальн`, `арешт`, `аварі`, `катастроф`, `загин`, `загибел`, `банкрут`, `обвинув`, `звинува`, `корупці`, `шахрай`, `розкрадан`, `хабар`, `репресі`, `диктатор`, `диктатур`, `терор`, `воєнн злочин`, `співучас`, `посібни`, `гібридн атак`, `агресі`, `окупац`, `маріонет`
- **негативные (вес 1)** (42): `затрим`, `зрив`, `зірва`, `відстава`, `скороч`, `критик`, `проблем`, `дефіцит`, `нестач`, `ризик`, `супереч`, `позов`, `суд`, `відмов`, `збій`, `вразлив`, `скасув`, `знищ`, `збит`, `ураж`, `удар`, `атак`, `втрат`, `загроз`, `провокац`, `поруш`, `ескалац`, `заборон`, `обмеж`, `закрит кордон`, `закрили кордон`, `вислан`, `протест`, `засуд`, `шпигун`, `контрабанд`, `нелегальн`, `незаконн`, `тиск`, `режим лукашенк`, `вторгнен`, `дестабіліз`
- **сильные позитивные (вес 2)** (7): `велик інвестиц`, `рекордн`, `прорив`, `зняття обмежен`, `держпідтримк`, `зняття санкц`, `скасуван санкц`
- **позитивные (вес 1)** (18): `контракт`, `замовлен`, `запуск`, `зростан`, `успішн`, `збільш`, `розшир`, `модернізац`, `постачан`, `отримав`, `співпрац`, `партнерств`, `діалог`, `нормалізац`, `звільнен`, `помилув`, `угод`, `домовленіст`
- **оценочные слова (Субъективность)** (21): `ганьб`, `шок`, `сенсаці`, `катастрофічн`, `жахлив`, `зрад`, `героїчн`, `блискуч`, `тріумф`, `провал`, `бездарн`, `неймовірн`, `скандальн`, `жахлив`, `цинічн`, `нахабн`, `абсурдн`, `кривав`, `злочинн режим`, `людожерськ`, `істери`
- **речь от первого лица (Субъективность)** (5): `я вважаю`, `на мою думку`, `на мій погляд`, `ми вважаємо`, `я впевнений`
- **окончания** (29): `∅`, `ь`, `і`, `ю`, `а`, `у`, `е`, `и`, `ом`, `ем`, `ою`, `ею`, `ам`, `ами`, `ах`, `ів`, `ий`, `ій`, `а`, `е`, `ого`, `ому`, `им`, `их`, `ої`, `ою`, `ими`, `ія`, `ії`
- **служебные слова для определения языка** (27): і, в, не, на, що, з, по, як, це, його, але, він, із, за, від, для, також, після, щоб, ще, може, більш, який, які, було, та, у
- **месяцы (для ключей-дат)**: січ, лют, берез, квіт, травн, червн, липн, серпн, вересн, жовтн, листопад, грудн

### pl — польский

- **сильные негативные (вес 2)** (24): `sankcj`, `karn`, `areszt`, `awari`, `katastrof`, `zgin`, `śmier`, `bankruct`, `oskarż`, `korupc`, `oszust`, `defraudac`, `łapówk`, `represj`, `dyktator`, `dyktatur`, `terror`, `zbrodni wojenn`, `współudział`, `współsprawc`, `atak hybrydow`, `agresj`, `okupac`, `marionet`
- **негативные (вес 1)** (42): `opóźni`, `zerwa`, `ograniczen`, `krytyk`, `problem`, `niedobór`, `brak`, `ryzyk`, `spór`, `pozew`, `sąd`, `odmow`, `awari`, `podatn`, `odwoła`, `zniszcz`, `zestrzel`, `uderz`, `atak`, `strat`, `zagroż`, `groź`, `prowokac`, `narusz`, `eskalac`, `zakaz`, `zamknięci granic`, `zamknął granic`, `wydal`, `protest`, `potępi`, `szpieg`, `przemyt`, `nielegaln`, `bezprawn`, `presj`, `reżim łukaszenk`, `reżim lukaszenk`, `inwazj`, `destabiliz`, `dezinformac`, `prowokator`
- **сильные позитивные (вес 2)** (6): `duż inwestyc`, `rekordow`, `przełom`, `zniesieni ograniczeń`, `zniesieni sankcj`, `wsparci państw`
- **позитивные (вес 1)** (20): `kontrakt`, `zamówieni`, `uruchom`, `wzrost`, `zwiększ`, `rozszerz`, `sukces`, `udan`, `modernizac`, `dostaw`, `otrzymał`, `współprac`, `partnerstw`, `dialog`, `normalizac`, `uwolni`, `ułaskawi`, `porozumieni`, `umow`, `deeskalac`
- **оценочные слова (Субъективность)** (20): `hańb`, `szok`, `sensac`, `katastrofaln`, `straszn`, `zdrad`, `bohatersk`, `znakomit`, `triumf`, `klęsk`, `nieudoln`, `niewiarygodn`, `skandaliczn`, `potworn`, `cyniczn`, `bezczeln`, `absurdaln`, `krwaw`, `zbrodnicz reżim`, `histeri`
- **речь от первого лица (Субъективность)** (5): `uważam`, `moim zdaniem`, `w mojej opinii`, `uważamy`, `jestem przekonany`
- **окончания** (30): `∅`, `a`, `y`, `i`, `u`, `e`, `ie`, `ę`, `ą`, `em`, `om`, `ami`, `ach`, `ów`, `owi`, `ego`, `emu`, `ym`, `im`, `ych`, `ich`, `ymi`, `imi`, `ej`, `ś`, `si`, `sią`, `iego`, `iemu`, `iej`
- **служебные слова для определения языка** (28): i, w, nie, na, że, z, po, jak, to, jego, ale, on, za, od, dla, też, także, po, aby, jeszcze, może, więcej, który, które, było, się, jest, oraz
- **месяцы (для ключей-дат)**: styczn, lut, marc, kwietn, maj, czerwc, lipc, sierpn, wrześn, październik, listopad, grudn

### lt — литовский

- **сильные негативные (вес 2)** (22): `sankcij`, `baudžiam`, `areštuot`, `suim`, `avarij`, `katastrof`, `žuv`, `bankrot`, `kaltin`, `korupcij`, `sukčiav`, `kyšin`, `represij`, `diktator`, `diktatūr`, `teror`, `karo nusikalt`, `bendrinink`, `hibridin atak`, `agresij`, `okupac`, `marionet`
- **негативные (вес 1)** (42): `vėlav`, `sutrik`, `apribojim`, `kritik`, `problem`, `trūkum`, `trūksta`, `rizik`, `ginč`, `ieškin`, `teism`, `atsisak`, `gedim`, `pažeidžiam`, `atšauk`, `sunaik`, `numušt`, `smūg`, `ataka`, `atakav`, `praradim`, `nuostol`, `grėsm`, `provokac`, `pažeid`, `eskalac`, `draud`, `uždar sien`, `uždarė sien`, `išsiunt`, `protest`, `pasmerk`, `šnip`, `kontraband`, `nelegal`, `neteisėt`, `spaudim`, `lukašenk režim`, `invazij`, `destabiliz`, `dezinformac`, `migrantų kriz`
- **сильные позитивные (вес 2)** (6): `didel investic`, `rekordin`, `proverž`, `panaikin apribojim`, `panaikin sankcij`, `valstyb parama`
- **позитивные (вес 1)** (20): `kontrakt`, `užsakym`, `paleid`, `augim`, `padidin`, `išplėt`, `sėkming`, `modernizav`, `tiekim`, `gavo`, `bendradarbiav`, `partnerys`, `dialog`, `normalizav`, `paleido`, `išlaisvin`, `malon`, `susitarim`, `sutart`, `deeskalac`
- **оценочные слова (Субъективность)** (20): `gėd`, `šok`, `sensacij`, `katastrofišk`, `baisu`, `baisus`, `išdavyst`, `didvyrišk`, `puikus`, `triumf`, `nesėkm`, `neįtikėtin`, `skandaling`, `siaubing`, `cinišk`, `įžūl`, `absurdišk`, `kruvin`, `nusikalstam režim`, `isterij`
- **речь от первого лица (Субъективность)** (5): `manau`, `mano nuomone`, `mano manymu`, `mes manome`, `esu įsitikinęs`
- **окончания** (36): `∅`, `as`, `o`, `ui`, `ą`, `u`, `e`, `ai`, `ų`, `ams`, `us`, `uose`, `ija`, `ijos`, `ijai`, `iją`, `ijoje`, `iečiai`, `iečių`, `iečiams`, `ietis`, `ių`, `iai`, `ius`, `ė`, `ės`, `ei`, `ę`, `ėje`, `is`, `io`, `iui`, `į`, `yje`, `iu`, `o`
- **служебные слова для определения языка** (26): ir, į, ne, kad, su, po, kaip, tai, jo, bet, jis, iš, už, nuo, dėl, taip, pat, po, kad, dar, gali, daugiau, kuris, kurie, buvo, yra
- **месяцы (для ключей-дат)**: sausio, vasario, kovo, balandžio, gegužės, birželio, liepos, rugpjūčio, rugsėjo, spalio, lapkričio, gruodžio

### lv — латышский

- **сильные негативные (вес 2)** (23): `sankcij`, `krimināl`, `arest`, `avārij`, `katastrof`, `gāj boj`, `bojāej`, `bankrot`, `apsūdz`, `korupcij`, `krāpšan`, `kukuļ`, `represij`, `diktator`, `diktatūr`, `teror`, `kara noziegum`, `līdzdalīb`, `hibrīdusbruk`, `hibrīdā uzbruk`, `agresij`, `okupācij`, `marionet`
- **негативные (вес 1)** (43): `kavēj`, `izjauk`, `ierobežojum`, `kritik`, `problēm`, `trūkum`, `trūkst`, `risk`, `strīd`, `prasīb`, `tiesa`, `atteik`, `bojājum`, `ievainojam`, `atceļ`, `iznīcin`, `notriekt`, `trieciens`, `triecien`, `uzbruk`, `zaudējum`, `draud`, `provokācij`, `pārkāp`, `eskalācij`, `aizliedz`, `aizliegum`, `slēdz robež`, `slēgt robež`, `izraid`, `protest`, `nosoda`, `nosodī`, `spieg`, `kontraband`, `nelegāl`, `nelikumīg`, `spiedien`, `lukašenko režīm`, `invāzij`, `destabiliz`, `dezinformācij`, `migrantu krīz`
- **сильные позитивные (вес 2)** (6): `liel investīcij`, `rekord`, `izrāviens`, `atcel ierobežojum`, `atcel sankcij`, `valsts atbalst`
- **позитивные (вес 1)** (18): `līgum`, `pasūtījum`, `palaišan`, `pieaugum`, `palielin`, `paplašin`, `veiksmīg`, `modernizācij`, `piegād`, `saņēm`, `sadarbīb`, `partnerīb`, `dialog`, `normalizācij`, `atbrīvo`, `apžēlo`, `vienošan`, `deeskalācij`
- **оценочные слова (Субъективность)** (20): `kaun`, `šok`, `sensācij`, `katastrofāl`, `šausmīg`, `nodevīb`, `varonīg`, `izcil`, `triumf`, `neveiksm`, `neticam`, `skandalоz`, `skandaloz`, `briesmīg`, `cinisk`, `nekaunīg`, `absurd`, `asiņain`, `noziedzīg režīm`, `histērij`
- **речь от первого лица (Субъективность)** (5): `es uzskatu`, `manuprāt`, `pēc manām domām`, `mēs uzskatām`, `esmu pārliecināts`
- **окончания** (25): `∅`, `s`, `a`, `am`, `u`, `ā`, `i`, `ija`, `ijas`, `ijai`, `iju`, `ijā`, `ietis`, `ieši`, `iešu`, `iešiem`, `iem`, `ais`, `ai`, `o`, `ie`, `us`, `os`, `ēm`, `as`
- **служебные слова для определения языка** (22): un, ar, ne, uz, ka, par, kā, tas, viņa, bet, viņš, no, pēc, arī, lai, vēl, var, vairāk, kurš, kuri, bija, ir
- **месяцы (для ключей-дат)**: janvār, februār, mart, aprīl, maij, jūnij, jūlij, august, septembr, oktobr, novembr, decembr

### en — английский

- **сильные негативные (вес 2)** (22): `sanction`, `indict`, `arrest`, `crash`, `killed`, `death`, `bankrupt`, `accus`, `corrupt`, `fraud`, `bribe`, `embezzl`, `repressi`, `dictator`, `terror`, `war crime`, `complicit`, `accomplice`, `hybrid attack`, `aggression`, `occupation`, `puppet`
- **негативные (вес 1)** (44): `delay`, `shortfall`, `cuts`, `critic`, `problem`, `shortage`, `risk`, `dispute`, `lawsuit`, `failure`, `failed`, `vulnerab`, `cancel`, `destroy`, `shot down`, `strike`, `attack`, `loss`, `losses`, `threat`, `provocat`, `violat`, `escalat`, `ban`, `banned`, `restrict`, `border closure`, `closed the border`, `close the border`, `expel`, `protest`, `condemn`, `spy`, `smuggl`, `illegal`, `unlawful`, `pressure`, `lukashenko regime`, `lukashenka regime`, `invasion`, `destabiliz`, `disinformation`, `migrant crisis`, `weaponiz`
- **сильные позитивные (вес 2)** (11): `breakthrough`, `record-`, `record `, `lifted the restrictions`, `lifted restrictions`, `lifted the ban`, `billion investment`, `billion contract`, `sanctions relief`, `lifted sanctions`, `eased sanctions`
- **позитивные (вес 1)** (21): `contract`, `award`, `launch`, `growth`, `increase`, `expand`, `success`, `milestone`, `deliver`, `upgrade`, `approved`, `order`, `cooperat`, `partnership`, `dialogue`, `normaliz`, `released`, `pardon`, `agreement`, `de-escalat`, `humanitarian aid`
- **оценочные слова (Субъективность)** (17): `shocking`, `stunning`, `disaster`, `humiliat`, `brilliant`, `epic`, `incredible`, `outrage`, `unbelievable`, `cynical`, `brazen`, `absurd`, `bloody`, `criminal regime`, `hysteri`, `monstrous`, `scandalous`
- **речь от первого лица (Субъективность)** (6): `i think`, `in my view`, `i believe`, `we believe`, `in my opinion`, `i am convinced`
- **окончания** (11): `∅`, `s`, `'s`, `’s`, `ian`, `ians`, `ian's`, `n`, `ns`, `an`, `ans`
- **служебные слова для определения языка** (25): the, and, of, to, in, is, that, for, on, with, as, by, from, this, it, was, are, be, which, also, after, has, have, will, its
- **месяцы (для ключей-дат)**: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec

### de — немецкий

- **сильные негативные (вес 2)** (27): `sanktion`, `strafrecht`, `verhaft`, `festnahm`, `unfall`, `katastroph`, `absturz`, `getötet`, `tod`, `bankrott`, `anklag`, `beschuldig`, `korruption`, `betrug`, `bestechung`, `repression`, `diktator`, `diktatur`, `terror`, `kriegsverbrech`, `mittäter`, `komplize`, `hybrid angriff`, `hybride angriff`, `aggression`, `besatzung`, `marionett`
- **негативные (вес 1)** (45): `verzöger`, `ausfall`, `kürzung`, `kritik`, `problem`, `mangel`, `engpass`, `risik`, `streit`, `klage`, `gericht`, `ablehn`, `störung`, `verwundbar`, `abgesagt`, `zerstör`, `abgeschossen`, `schlag`, `angriff`, `verlust`, `bedroh`, `drohung`, `provokation`, `verletz`, `verstoß`, `eskalation`, `verbot`, `beschränk`, `grenzschließung`, `grenze geschlossen`, `ausgewiesen`, `auswei`, `protest`, `verurteil`, `spion`, `schmuggel`, `illegal`, `rechtswidrig`, `druck`, `lukaschenko-regime`, `regime lukaschenko`, `invasion`, `destabilisier`, `desinformation`, `migrationskrise`
- **сильные позитивные (вес 2)** (7): `durchbruch`, `rekord`, `aufhebung der beschränk`, `aufhebung der sanktion`, `sanktionen aufgehoben`, `milliardeninvestition`, `staatliche förderung`
- **позитивные (вес 1)** (20): `vertrag`, `auftrag`, `start`, `wachstum`, `steiger`, `erweiter`, `erfolg`, `modernisier`, `lieferung`, `erhalten`, `zusammenarbeit`, `partnerschaft`, `dialog`, `normalisier`, `freigelassen`, `freilassung`, `begnadig`, `abkommen`, `vereinbarung`, `deeskalation`
- **оценочные слова (Субъективность)** (19): `schande`, `schock`, `sensation`, `katastrophal`, `schrecklich`, `verrat`, `heldenhaft`, `brillant`, `triumph`, `debakel`, `unglaublich`, `skandalös`, `ungeheuerlich`, `zynisch`, `dreist`, `absurd`, `blutig`, `verbrecherisch regime`, `hysteri`
- **речь от первого лица (Субъективность)** (6): `ich denke`, `meiner meinung nach`, `ich glaube`, `wir glauben`, `aus meiner sicht`, `ich bin überzeugt`
- **окончания** (16): `∅`, `s`, `en`, `n`, `e`, `er`, `es`, `em`, `isch`, `ische`, `ischen`, `ischer`, `isches`, `ischem`, `land`, `lands`
- **служебные слова для определения языка** (26): der, die, das, und, zu, in, den, nicht, von, mit, sich, des, auf, für, ist, im, dem, ein, eine, als, auch, es, an, wird, nach, bei
- **месяцы (для ключей-дат)**: jan, feb, märz, apr, mai, jun, jul, aug, sep, okt, nov, dez

## Страна источника

Страна — страна издателя по карточке источника. Явный список ниже; иначе домен верхнего уровня (.ru/.рф Россия, .ua Украина, .by Беларусь, .pl Польша, .lt Литва, .lv Латвия, .de Германия); иначе «Прочие страны» с пометкой «страна не установлена». Источники группы «наши официальные ресурсы РБ» — Беларусь. Источники из Беларуси в ИИД не входят (внутренние/наши).

| Источник | Страна |
|---|---|
| `belta.by` | Беларусь |
| `belta.by-bpla` | Беларусь |
| `belvpo.com` | Беларусь |
| `mil.by` | Беларусь |
| `sb.by-bpla` | Беларусь |
| `tg:Drones_Belarus` | Беларусь |
| `tg:modmilby` | Беларусь |
| `tg:otvinta_by` | Беларусь |
| `tg:vpk_gov_by` | Беларусь |
| `tg:vpkgovby` | Беларусь |
| `vpk.gov.by` | Беларусь |
| `dw.com-bpla` | Германия |
| `esut.de` | Германия |
| `hartpunkt.de` | Германия |
| `soldat-und-technik.de` | Германия |
| `defence24.com` | Польша |
| `defence24.pl` | Польша |
| `dziennikzbrojny.pl` | Польша |
| `zbiam.pl` | Польша |
| `1prime.ru` | Россия |
| `armiyaonline.ru` | Россия |
| `arms-expo.ru` | Россия |
| `armstrade.org` | Россия |
| `arsenal-otechestva.ru` | Россия |
| `bastion-karpenko.ru` | Россия |
| `bmpd.livejournal.com` | Россия |
| `bo.nalog.ru` | Россия |
| `cbr.ru` | Россия |
| `cos-news.ru` | Россия |
| `dronus.ru` | Россия |
| `egrul.nalog.ru` | Россия |
| `expouav.ru` | Россия |
| `fssp.gov.ru` | Россия |
| `function.mil.ru` | Россия |
| `impnavigator.ru` | Россия |
| `interfax.ru` | Россия |
| `kad.arbitr.ru` | Россия |
| `kommersant.ru` | Россия |
| `mil.ru` | Россия |
| `minpromtorg.gov.ru` | Россия |
| `nvo.ng.ru` | Россия |
| `oborona.ru` | Россия |
| `rbc.ru` | Россия |
| `ria.ru` | Россия |
| `roe.ru` | Россия |
| `rostec.ru` | Россия |
| `smart-lab.ru` | Россия |
| `tass.ru` | Россия |
| `tg:FPV_Moscow` | Россия |
| `tg:INFRONT_Z` | Россия |
| `tg:ZOV_DRONOVODA` | Россия |
| `tg:dronesrussia` | Россия |
| `tg:fpv_dron_kazan` | Россия |
| `tg:kalashnikovgroup` | Россия |
| `tg:milinfolive` | Россия |
| `tg:mod_russia` | Россия |
| `tg:rybar` | Россия |
| `topwar.ru` | Россия |
| `uacrussia.ru` | Россия |
| `uvz.ru` | Россия |
| `vedomosti.ru` | Россия |
| `voennoe.rf` | Россия |
| `vpk-news.ru` | Россия |
| `vpk.name` | Россия |
| `zakupki.gov.ru` | Россия |
| `armyinform.com.ua` | Украина |
| `bihus.info` | Украина |
| `brave1.gov.ua` | Украина |
| `defence-ua.com` | Украина |
| `euromaidanpress.com` | Украина |
| `kyivindependent.com` | Украина |
| `mil.in.ua` | Украина |
| `militarnyi.com` | Украина |
| `mod.gov.ua-en` | Украина |
| `pravda.com.ua-eng` | Украина |
| `sanctions.nazk.gov.ua` | Украина |
| `slidstvo.info` | Украина |
| `tg:GeneralStaffZSU` | Украина |
| `tg:brave1ukraine` | Украина |
| `tg:defence_ua` | Украина |
| `tg:militarnyi` | Украина |
| `tg:militarnyi_ua` | Украина |
| `tg:ministry_of_defense_ua` | Украина |
| `tg:operativnoZSU` | Украина |
| `tg:toro_ua` | Украина |
| `tg:ukroboronprom` | Украина |
| `ukrinform` | Украина |
| `ukrmilitary.com` | Украина |
| `united24media.com` | Украина |
| `youcontrol.com.ua` | Украина |

---
© 2026 GREEN-CBR. Все права защищены. Разработчик — GREEN-CBR.
