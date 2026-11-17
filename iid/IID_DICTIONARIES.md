# ИИД-100 — словари признаков, упоминаний, топонимов и организаций

Версия словарей: `iid-lex-2` (2026-11-16). Методика: `iid100-2`. Составлены вручную, без обучения и без машинного перевода; изменение словаря — новая версия методики, прежние значения не перезаписываются.

Правила совпадения:

- **Признак окраса и субъективности** — основа слова; совпадение с начала слова (основа + любое окончание). Основа из 4 и менее букв — только целое слово с окончаниями языка. Фраза — основы подряд.
- **Упоминание, топоним, организация** — основа + фиксированный список окончаний языка, по границе слова (языки iid-lex-1). Для языков iid-lex-2 (fr, it, es, pt, ca, ro, nl, sv, da, nb, is, fi, et, hu, cs, sk, sl, hr, bs, sr, mk, bg, sq, el, tr, fa) — основа из 5 и более символов совпадает с начала слова (основа + любое окончание), короче — целое слово с окончаниями языка.
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
| fr (французский) | 10 | 29 | 108 | 17 | 81 | 15 |
| it (итальянский) | 11 | 27 | 109 | 15 | 81 | 13 |
| es (испанский) | 12 | 26 | 109 | 15 | 82 | 14 |
| pt (португальский) | 12 | 29 | 111 | 15 | 91 | 14 |
| ca (каталанский) | 8 | 24 | 98 | 9 | 82 | 14 |
| ro (румынский) | 14 | 24 | 113 | 14 | 84 | 17 |
| nl (нидерландский) | 6 | 24 | 110 | 13 | 80 | 15 |
| sv (шведский) | 10 | 24 | 110 | 11 | 78 | 14 |
| da (датский) | 10 | 25 | 103 | 10 | 78 | 14 |
| nb (норвежский (букмол)) | 10 | 25 | 104 | 10 | 79 | 14 |
| is (исландский) | 14 | 22 | 93 | 9 | 82 | 13 |
| fi (финский) | 29 | 19 | 118 | 11 | 83 | 12 |
| et (эстонский) | 18 | 20 | 102 | 9 | 78 | 13 |
| hu (венгерский) | 41 | 20 | 107 | 9 | 79 | 14 |
| cs (чешский) | 28 | 24 | 113 | 10 | 81 | 15 |
| sk (словацкий) | 27 | 24 | 110 | 10 | 81 | 15 |
| sl (словенский) | 28 | 22 | 100 | 9 | 82 | 14 |
| hr (хорватский) | 27 | 23 | 107 | 9 | 82 | 16 |
| bs (боснийский) | 27 | 23 | 107 | 8 | 81 | 15 |
| sr (сербский (кириллица и латиница)) | 49 | 43 | 212 | 16 | 132 | 29 |
| mk (македонский) | 20 | 21 | 101 | 7 | 45 | 13 |
| bg (болгарский) | 23 | 23 | 102 | 9 | 49 | 12 |
| sq (албанский) | 15 | 21 | 103 | 8 | 82 | 13 |
| el (греческий) | 22 | 23 | 111 | 9 | 32 | 11 |
| tr (турецкий) | 67 | 19 | 101 | 9 | 76 | 15 |
| fa (персидский) | 12 | 27 | 99 | 11 | 28 | 15 |

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
- fr: `biélorussie`, `biélorusse`, `bielorussie`, `bielorusse`, `bélarus`, `belarus`, `bélarusse`
- it: `bielorussia`, `bielorusso`, `bielorussa`, `bielorussi`, `bielorusse`, `belarus`
- es: `bielorrusia`, `bielorruso`, `bielorrusa`, `bielorrusos`, `bielorrusas`, `belarús`, `belarus`
- pt: `bielorrússia`, `bielorrussia`, `bielorrusso`, `bielorrussa`, `belarus`, `bielo-rússia`
- ca: `bielorússia`, `bielorús`, `bielorussa`, `belarús`
- ro: `belarus`, `bielorusia`, `bielorus`, `belarusi`
- nl: `wit-rusland`, `witrusland`, `belarus`, `wit-russisch`, `belarussisch`
- sv: `belarus`, `vitryssland`, `vitrysk`, `belarusisk`
- da: `hviderusland`, `hviderussisk`, `belarus`, `belarusisk`
- nb: `hviterussland`, `hviterussisk`, `belarus`, `belarusisk`
- is: `hvíta-rússland`, `hvíta-rússlandi`, `hvítrússnesk`, `belarús`
- fi: `valko-venäj`, `valkovenäj`, `belarus`
- et: `valgevene`, `belarus`
- hu: `fehérorosz`, `belarusz`
- cs: `bělorus`, `belarus`
- sk: `bielorus`, `belarus`
- sl: `belorus`, `belarus`
- hr: `bjelorus`, `belarus`
- bs: `bjelorus`, `belarus`
- sr: `belorus`, `bjelorus`, `belarus`, `белорус`, `беларус`
- mk: `белорус`, `беларус`
- bg: `беларус`, `белорус`
- sq: `bjellorusi`, `bjellorus`, `belarus`
- el: `λευκορωσ`, `λευκορώσ`, `μπελαρούσ`
- tr: `belarus`, `beyaz rusya`
- fa: `بلاروس`, `روسیه سفید`, `روسيه سفيد`

**BY-PRES — Лукашенко А.Г. (Президент РБ)** (лицо)  
- ru: `лукашенк`, `лукашенко`
- be: `лукашэнк`, `лукашэнка`
- uk: `лукашенк`, `лукашенко`
- pl: `łukaszenk`, `lukaszenk`, `łukaszenka`, `lukaszenka`, `łukaszenko`
- lt: `lukašenk`, `lukasenk`, `lukašenka`
- lv: `lukašenk`, `lukasenk`, `lukašenko`
- en: `lukashenk`, `lukashenko`, `lukashenka`
- de: `lukaschenk`, `lukaschenko`
- fr: `loukachenko`, `loukachenka`, `lukashenko`, `lukashenka`
- it: `lukashenko`, `lukashenka`, `lukašenko`
- es: `lukashenko`, `lukashenka`
- pt: `lukashenko`, `lukachenko`, `lukashenka`
- ca: `lukaixenko`, `lukashenko`
- ro: `lukașenko`, `lukaşenko`, `lukasenko`, `lukashenko`, `lukașenka`
- nl: `loekasjenko`, `lukashenko`, `loekasjenka`
- sv: `lukasjenk`, `lukashenk`
- da: `lukasjenk`, `lukashenk`
- nb: `lukasjenk`, `lukashenk`
- is: `lúkasjenk`, `lukashenk`
- fi: `lukašenk`, `lukashenk`, `lukasenk`
- et: `lukašenk`, `lukashenk`
- hu: `lukasenk`
- cs: `lukašenk`, `lukasenk`
- sk: `lukašenk`, `lukasenk`
- sl: `lukašenk`, `lukasenk`
- hr: `lukašenk`, `lukasenk`
- bs: `lukašenk`, `lukasenk`
- sr: `lukašenk`, `lukasenk`, `лукашенк`
- mk: `лукашенк`
- bg: `лукашенк`
- sq: `lukashenk`, `llukashenk`
- el: `λουκασένκ`, `λουκασενκ`
- tr: `lukaşenk`, `lukashenk`
- fa: `لوکاشنکو`, `لوكاشنكو`

**BY-GOV — органы власти РБ (белорусские министерства и ведомства)** (организация)  
- ru: `минобороны беларуси`, `мид беларуси`, `госпогранкомитет`, `кгб беларуси`, `мвд беларуси`, `совмин беларуси`, `белорусск мид`, `белорусск минобороны`, `белорусск пограничник`, `белорусск власт`, `официальн минск`
- be: `міністэрства абароны беларусі`, `мзс беларусі`, `дзяржпамежкамітэт`, `кдб беларусі`, `беларуск памежнік`, `беларуск улад`, `афіцыйн мінск`
- uk: `міноборони білорусі`, `мзс білорусі`, `кдб білорусі`, `білоруськ прикордонник`, `білоруськ влад`, `офіційн мінськ`
- pl: `białorusk mswiz`, `białorusk msz`, `białorusk kgb`, `białorusk pogranicz`, `białorusk władz`, `oficjaln mińsk`
- lt: `baltarusijos užsienio reikalų ministerij`, `baltarusijos kgb`, `baltarusijos pasienieč`, `baltarusijos valdži`, `oficialus minskas`
- lv: `baltkrievijas ārlietu ministrij`, `baltkrievijas čeka`, `baltkrievijas robežsarg`, `baltkrievijas varas`, `oficiālā minska`
- en: `belarusian foreign ministry`, `belarusian defence ministry`, `belarusian defense ministry`, `belarusian kgb`, `belarusian border guard`, `belarusian authorities`, `official minsk`
- de: `belarussisch außenministerium`, `belarussisch grenzschutz`, `belarussisch behörden`, `belarussisch kgb`, `offizielle minsk`
- fr: `autorités biélorusses`, `gouvernement biélorusse`, `régime biélorusse`, `kgb biélorusse`, `minsk officiel`, `ministère biélorusse`
- it: `autorità bielorusse`, `governo bielorusso`, `regime bielorusso`, `kgb bielorusso`, `ministero bielorusso`, `minsk ufficiale`
- es: `autoridades bielorrusas`, `gobierno bielorruso`, `régimen bielorruso`, `kgb bielorruso`, `ministerio bielorruso`, `minsk oficial`
- pt: `autoridades bielorrussas`, `governo bielorrusso`, `regime bielorrusso`, `kgb bielorrusso`, `ministério bielorrusso`, `minsk oficial`
- ca: `autoritats bielorusses`, `govern bielorús`, `règim bielorús`
- ro: `autoritățile belaruse`, `autoritățile de la minsk`, `guvernul belarus`, `regimul de la minsk`, `ministerul belarus`
- nl: `wit-russische autoriteiten`, `belarussische autoriteiten`, `wit-russische regering`, `wit-russisch regime`, `wit-russische kgb`
- sv: `belarusiska myndighet`, `belarusiska regering`, `belarusiska regim`, `vitryska regim`, `belarusiska kgb`
- da: `hviderussiske myndighed`, `hviderussiske regering`, `hviderussiske regime`, `belarusiske myndighed`
- nb: `hviterussiske myndighet`, `hviterussiske regjering`, `hviterussiske regime`, `belarusiske myndighet`
- is: `hvítrússnesk yfirvöld`, `stjórnvöld í hvíta-rússlandi`, `hvítrússnesk stjórnvöld`
- fi: `valko-venäjän hallin`, `valko-venäjän viranomai`, `valko-venäjän ulkoministeri`, `valko-venäjän puolustusministeri`, `valko-venäjän kgb`
- et: `valgevene võim`, `valgevene režiim`, `valgevene välisministeerium`, `valgevene kaitseministeerium`, `valgevene kgb`
- hu: `fehérorosz hatóság`, `fehérorosz kormány`, `fehérorosz külügyminiszt`, `fehérorosz védelmi miniszt`, `fehérorosz kgb`, `fehérorosz rezsim`
- cs: `běloruské úřad`, `běloruská vláda`, `běloruské vlád`, `běloruský režim`, `běloruské ministerstv`, `běloruská kgb`
- sk: `bieloruské úrad`, `bieloruská vláda`, `bieloruskej vlád`, `bieloruský režim`, `bieloruské ministerstv`, `bieloruská kgb`
- sl: `beloruske oblasti`, `beloruska vlada`, `beloruski režim`, `belorusko ministrstv`, `beloruski kgb`
- hr: `bjeloruske vlasti`, `bjeloruska vlada`, `bjeloruski režim`, `bjelorusko ministarstv`, `bjeloruski kgb`
- bs: `bjeloruske vlasti`, `bjeloruska vlada`, `bjeloruski režim`, `bjelorusko ministarstv`
- sr: `beloruske vlasti`, `beloruska vlada`, `beloruski režim`, `belorusko ministarstv`, `белоруске власти`, `белоруска влада`, `белоруски режим`, `белоруско министарств`
- mk: `белоруските власти`, `белоруската влада`, `белорускиот режим`, `белоруското министерств`
- bg: `беларуските власти`, `белоруските власти`, `беларуското правителство`, `беларуският режим`, `беларуското министерств`, `официален минск`
- sq: `autoritetet bjelloruse`, `qeveria bjelloruse`, `regjimi bjellorus`
- el: `λευκορωσικές αρχές`, `λευκορωσική κυβέρνησ`, `λευκορωσικό καθεστώς`, `λευκορωσικό υπουργεί`
- tr: `belarus yetkilileri`, `belarus hükümeti`, `belarus dışişleri`, `belarus savunma bakanlığı`, `belarus rejimi`
- fa: `دولت بلاروس`, `مقامات بلاروس`, `وزارت خارجه بلاروس`, `وزارت دفاع بلاروس`, `رژیم بلاروس`, `رژيم بلاروس`

## Топонимы (ключи «место»; BY — населённый пункт РБ, тоже признак упоминания)

| Код | Место | BY | Формы по языкам |
|---|---|---|---|
| BY-MSQ | Минск | да | ru: минск; be: мінск; uk: мінськ, минск; pl: mińsk, minsk; lt: minsk; lv: minsk; en: minsk; de: minsk; fr: minsk; it: minsk; es: minsk; pt: minsk; ca: minsk; ro: minsk; nl: minsk; sv: minsk; da: minsk; nb: minsk; is: minsk; fi: minsk; et: minsk; hu: minszk, minsk; cs: minsk; sk: minsk; sl: minsk; hr: minsk; bs: minsk; sr: minsk, минск; mk: минск; bg: минск; sq: minsk; el: μινσκ; tr: minsk; fa: مینسک, مينسك |
| BY-BRE | Брест | да | ru: брест; be: брэст; uk: брест; pl: brześć, brześci, brzesc; lt: brest; lv: brest; en: brest-litovsk, brest, belarus; de: brest-litowsk; fr: brest-litovsk, brest litovsk; it: brest-litovsk, brest litovsk; es: brest-litovsk, brest litovsk; pt: brest-litovsk, brest litovsk; ca: brest-litovsk, brest litovsk; ro: brest-litovsk, brest litovsk; nl: brest-litovsk, brest litovsk; sv: brest-litovsk, brest litovsk; da: brest-litovsk, brest litovsk; nb: brest-litovsk, brest litovsk; is: brest-litovsk, brest litovsk; fi: brest-litovsk, brest litovsk; et: brest-litovsk, brest litovsk; hu: breszt-litovszk, brest-litovsk, brest litovsk; cs: brest-litovsk, brest litovsk; sk: brest-litovsk, brest litovsk; sl: brest-litovsk, brest litovsk; hr: brest-litovsk, brest litovsk; bs: brest-litovsk, brest litovsk; sr: brest-litovsk, brest litovsk, брест-литовск; mk: брест-литовск; bg: брест-литовск; sq: brest-litovsk, brest litovsk; el: μπρεστ-λιτόφσκ; tr: brest-litovsk, brest litovsk; fa:  |
| BY-GRO | Гродно | да | ru: гродн; be: гродн; uk: гродн; pl: grodn; lt: gardin; lv: grodņ, grodn; en: grodno, hrodna; de: grodno; fr: grodno, hrodna; it: grodno, hrodna; es: grodno, hrodna; pt: grodno, hrodna; ca: grodno, hrodna; ro: grodno, hrodna; nl: grodno, hrodna; sv: grodno, hrodna; da: grodno, hrodna; nb: grodno, hrodna; is: grodno, hrodna; fi: grodno, hrodna; et: grodno, hrodna; hu: grodno, hrodna; cs: grodno, hrodna; sk: grodno, hrodna; sl: grodno, hrodna; hr: grodno, hrodna; bs: grodno, hrodna; sr: grodno, hrodna, гродно, гродна; mk: гродно, гродна; bg: гродно, гродна; sq: grodno, hrodna; el: γκρόντνο, γκροντνο; tr: grodno, hrodna; fa: گرودنو |
| BY-GOM | Гомель | да | ru: гомел; be: гомел; uk: гомел; pl: homel, homl; lt: gomel; lv: gomeļ, gomel; en: gomel, homel; de: gomel; fr: gomel, homel; it: gomel, homel; es: gomel, homel; pt: gomel, homel; ca: gomel, homel; ro: gomel, homel; nl: gomel, homel; sv: gomel, homel; da: gomel, homel; nb: gomel, homel; is: gomel, homel; fi: gomel, homel; et: gomel, homel; hu: gomel, homel; cs: gomel, homel; sk: gomel, homel; sl: gomel, homel; hr: gomel, homel; bs: gomel, homel; sr: gomel, homel, гомел; mk: гомел; bg: гомел; sq: gomel, homel; el: γκόμελ, γκομελ; tr: gomel, homel; fa: گومل |
| BY-VIT | Витебск | да | ru: витебск; be: віцебск; uk: вітебськ; pl: witebsk; lt: vitebsk; lv: vitebsk; en: vitebsk, viciebsk; de: witebsk; fr: vitebsk, viciebsk, witebsk; it: vitebsk, viciebsk, witebsk; es: vitebsk, viciebsk, witebsk; pt: vitebsk, viciebsk, witebsk; ca: vitebsk, viciebsk, witebsk; ro: vitebsk, viciebsk, witebsk; nl: vitebsk, viciebsk, witebsk; sv: vitebsk, viciebsk, witebsk; da: vitebsk, viciebsk, witebsk; nb: vitebsk, viciebsk, witebsk; is: vitebsk, viciebsk, witebsk; fi: vitebsk, viciebsk, witebsk; et: vitebsk, viciebsk, witebsk; hu: vityebszk, vitebsk, viciebsk, witebsk; cs: vitebsk, viciebsk, witebsk; sk: vitebsk, viciebsk, witebsk; sl: vitebsk, viciebsk, witebsk; hr: vitebsk, viciebsk, witebsk; bs: vitebsk, viciebsk, witebsk; sr: vitebsk, viciebsk, witebsk, витебск; mk: витебск; bg: витебск; sq: vitebsk, viciebsk, witebsk; el: βίτεμπσκ; tr: vitebsk, viciebsk, witebsk; fa: ویتبسک, ويتبسك |
| BY-MOG | Могилёв | да | ru: могилев, могилёв; be: магілёв, магілев; uk: могильов; pl: mohylew; lt: mogiliov; lv: mogiļov, mogilev; en: mogilev, mahilyow; de: mogiljow; fr: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; it: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; es: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; pt: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; ca: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; ro: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; nl: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; sv: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; da: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; nb: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; is: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; fi: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; et: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; hu: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; cs: mohylev, mogilev, mogiljov, mahiliou, mahilyow, mahiljou; sk: mohylev, mogilev, mogiljov, mahiliou, mahilyow, mahiljou; sl: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; hr: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; bs: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; sr: mogilev, mogiljov, mahiliou, mahilyow, mahiljou, могилев, могильов, могилёв; mk: могилев, могильов, могилёв; bg: могилев, могильов, могилёв; sq: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; el: μογκιλιόφ; tr: mogilev, mogiljov, mahiliou, mahilyow, mahiljou; fa: موگیلف, موگيلف |
| BY-BAR | Барановичи | да | ru: баранович; be: баранавіч; uk: баранович; pl: baranowicz; lt: baranovič; lv: baranoviči; en: baranovichi; de: baranowitschi; fr: baranovitch, baranovic, baranavic, baranowicz; it: baranovic, baranavic, baranowicz; es: baranovic, baranavic, baranowicz; pt: baranovic, baranavic, baranowicz; ca: baranovic, baranavic, baranowicz; ro: baranovic, baranavic, baranowicz; nl: baranovic, baranavic, baranowicz; sv: baranovic, baranavic, baranowicz; da: baranovic, baranavic, baranowicz; nb: baranovic, baranavic, baranowicz; is: baranovic, baranavic, baranowicz; fi: baranovic, baranavic, baranowicz; et: baranovic, baranavic, baranowicz; hu: baranovic, baranavic, baranowicz; cs: baranovic, baranavic, baranowicz; sk: baranovic, baranavic, baranowicz; sl: baranovic, baranavic, baranowicz; hr: baranovic, baranavic, baranowicz; bs: baranovic, baranavic, baranowicz; sr: baranovic, baranavic, baranowicz, баранович; mk: баранович; bg: баранович; sq: baranovic, baranavic, baranowicz; el: μπαράνοβιτσ; tr: baranovic, baranavic, baranowicz; fa:  |
| BY-BOR | Борисов | да | ru: борисов; be: барысаў, барысав; uk: борисов; pl: borysów, borysow; lt: borisov; lv: borisov; en: borisov, barysaw; de: baryssau, borissow; fr: barysaw, barysau, borisov; it: barysaw, barysau, borisov; es: barysaw, barysau, borisov; pt: barysaw, barysau, borisov; ca: barysaw, barysau, borisov; ro: barysaw, barysau, borisov; nl: barysaw, barysau, borisov; sv: barysaw, barysau, borisov; da: barysaw, barysau, borisov; nb: barysaw, barysau, borisov; is: barysaw, barysau, borisov; fi: barysaw, barysau, borisov; et: barysaw, barysau, borisov; hu: barysaw, barysau, borisov; cs: barysaw, barysau, borisov; sk: barysaw, barysau, borisov; sl: barysaw, barysau, borisov; hr: barysaw, barysau, borisov; bs: barysaw, barysau, borisov; sr: barysaw, barysau, borisov, борисов; mk: борисов; bg: борисов; sq: barysaw, barysau, borisov; el: ; tr: barysaw, barysau, borisov; fa:  |
| BY-BOB | Бобруйск | да | ru: бобруйск; be: бабруйск; uk: бобруйськ; pl: bobrujsk; lt: babruisk; lv: bobruiska; en: bobruisk, babruysk; de: babrujsk; fr: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; it: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; es: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; pt: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; ca: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; ro: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; nl: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; sv: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; da: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; nb: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; is: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; fi: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; et: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; hu: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; cs: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; sk: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; sl: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; hr: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; bs: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; sr: bobruisk, bobrujsk, babruisk, babruysk, babrujsk, бобруйск, бобрујск; mk: бобруйск, бобрујск; bg: бобруйск, бобрујск; sq: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; el: μπομπρούισκ; tr: bobruisk, bobrujsk, babruisk, babruysk, babrujsk; fa:  |
| BY-PIN | Пинск | да | ru: пинск; be: пінск; uk: пінськ; pl: pińsk; lt: pinsk; lv: pinsk; en: pinsk; de: pinsk; fr: pinsk; it: pinsk; es: pinsk; pt: pinsk; ca: pinsk; ro: pinsk; nl: pinsk; sv: pinsk; da: pinsk; nb: pinsk; is: pinsk; fi: pinsk; et: pinsk; hu: pinsk; cs: pinsk; sk: pinsk; sl: pinsk; hr: pinsk; bs: pinsk; sr: pinsk, пинск; mk: пинск; bg: пинск; sq: pinsk; el: πινσκ; tr: pinsk; fa:  |
| BY-ORS | Орша | да | ru: орш; be: орш; uk: орш; pl: orsz; lt: orša; lv: orša; en: orsha; de: orscha; fr: orsha, orša; it: orsha, orša; es: orsha, orša; pt: orsha, orša; ca: orsha, orša; ro: orsha, orša; nl: orsha, orša; sv: orsha, orša; da: orsha, orša; nb: orsha, orša; is: orsha, orša; fi: orsha, orša; et: orsha, orša; hu: orsha, orša; cs: orsha, orša; sk: orsha, orša; sl: orsha, orša; hr: orsha, orša; bs: orsha, orša; sr: orsha, orša, орша; mk: орша; bg: орша; sq: orsha, orša; el: ; tr: orsha, orša; fa:  |
| BY-LID | Лида | да | ru: лид; be: лід; uk: лід; pl: lid; lt: lyd; lv: lida; en: lida; de: lida; fr: lida; it: lida; es: lida; pt: lida; ca: lida; ro: lida; nl: lida; sv: lida; da: lida; nb: lida; is: lida; fi: lida; et: lida; hu: lida; cs: lida; sk: lida; sl: lida; hr: lida; bs: lida; sr: lida, лида; mk: лида; bg: лида; sq: lida; el: ; tr: lida; fa:  |
| BY-MOZ | Мозырь | да | ru: мозыр; be: мазыр; uk: мозир; pl: mozyrz; lt: mozyr; lv: mozira; en: mozyr; de: masyr; fr: mozyr, mazyr; it: mozyr, mazyr; es: mozyr, mazyr; pt: mozyr, mazyr; ca: mozyr, mazyr; ro: mozyr, mazyr; nl: mozyr, mazyr; sv: mozyr, mazyr; da: mozyr, mazyr; nb: mozyr, mazyr; is: mozyr, mazyr; fi: mozyr, mazyr; et: mozyr, mazyr; hu: mozyr, mazyr; cs: mozyr, mazyr; sk: mozyr, mazyr; sl: mozyr, mazyr; hr: mozyr, mazyr; bs: mozyr, mazyr; sr: mozyr, mazyr, мозир, мозыр; mk: мозир, мозыр; bg: мозир, мозыр; sq: mozyr, mazyr; el: ; tr: mozyr, mazyr; fa:  |
| BY-POL | Полоцк/Новополоцк | да | ru: полоцк, новополоцк; be: полацк, наваполацк; uk: полоцьк, новополоцьк; pl: połock, nowopołock; lt: polock; lv: polocka; en: polotsk, novopolotsk; de: polozk, nowopolozk; fr: polotsk, polock, polack, navapolack, novopolotsk, novopolock; it: polotsk, polock, polack, navapolack, novopolotsk, novopolock; es: polotsk, polock, polack, navapolack, novopolotsk, novopolock; pt: polotsk, polock, polack, navapolack, novopolotsk, novopolock; ca: polotsk, polock, polack, navapolack, novopolotsk, novopolock; ro: polotsk, polock, polack, navapolack, novopolotsk, novopolock; nl: polotsk, polock, polack, navapolack, novopolotsk, novopolock; sv: polotsk, polock, polack, navapolack, novopolotsk, novopolock; da: polotsk, polock, polack, navapolack, novopolotsk, novopolock; nb: polotsk, polock, polack, navapolack, novopolotsk, novopolock; is: polotsk, polock, polack, navapolack, novopolotsk, novopolock; fi: polotsk, polock, polack, navapolack, novopolotsk, novopolock; et: polotsk, polock, polack, navapolack, novopolotsk, novopolock; hu: polotsk, polock, polack, navapolack, novopolotsk, novopolock; cs: polotsk, polock, polack, navapolack, novopolotsk, novopolock; sk: polotsk, polock, polack, navapolack, novopolotsk, novopolock; sl: polotsk, polock, polack, navapolack, novopolotsk, novopolock; hr: polotsk, polock, polack, navapolack, novopolotsk, novopolock; bs: polotsk, polock, polack, navapolack, novopolotsk, novopolock; sr: polotsk, polock, polack, navapolack, novopolotsk, novopolock, полоцк, новополоцк; mk: полоцк, новополоцк; bg: полоцк, новополоцк; sq: polotsk, polock, polack, navapolack, novopolotsk, novopolock; el: πόλοτσκ; tr: polotsk, polock, polack, navapolack, novopolotsk, novopolock; fa:  |
| BY-OST | Островец (БелАЭС) | да | ru: островец, белаэс, белорусск аэс; be: астравец, беларуск аэс; uk: островець, білоруськ аес; pl: ostrowiec, elektrowni w ostrowcu, astraviec; lt: astravo, astravj, astravas; lv: astravjec, astravas; en: astravets, ostrovets; de: astrawez, ostrowez; fr: astravets, astravec, ostrovets, astravyets; it: astravets, astravec, ostrovets, astravyets; es: astravets, astravec, ostrovets, astravyets; pt: astravets, astravec, ostrovets, astravyets; ca: astravets, astravec, ostrovets, astravyets; ro: astravets, astravec, ostrovets, astravyets; nl: astravets, astravec, ostrovets, astravyets; sv: astravets, astravec, ostrovets, astravyets; da: astravets, astravec, ostrovets, astravyets; nb: astravets, astravec, ostrovets, astravyets; is: astravets, astravec, ostrovets, astravyets; fi: astravets, astravec, ostrovets, astravyets; et: astravets, astravec, ostrovets, astravyets; hu: astravets, astravec, ostrovets, astravyets; cs: astravets, astravec, ostrovets, astravyets; sk: astravets, astravec, ostrovets, astravyets; sl: astravets, astravec, ostrovets, astravyets; hr: astravets, astravec, ostrovets, astravyets; bs: astravets, astravec, ostrovets, astravyets; sr: astravets, astravec, ostrovets, astravyets, островец; mk: островец; bg: островец; sq: astravets, astravec, ostrovets, astravyets; el: οστρόβετς; tr: astravets, astravec, ostrovets, astravyets; fa:  |
| BY-MCH | Мачулищи | да | ru: мачулищ; be: мачулішч; uk: мачулищ; pl: maczuliszcz; lt: mačuliš; lv: mačulišči; en: machulishchy, machulishchi; de: matschulischtschy; fr: machulishch, mačulišč, matchoulichtch; it: machulishch, mačulišč, matchoulichtch; es: machulishch, mačulišč, matchoulichtch; pt: machulishch, mačulišč, matchoulichtch; ca: machulishch, mačulišč, matchoulichtch; ro: machulishch, mačulišč, matchoulichtch; nl: machulishch, mačulišč, matchoulichtch; sv: machulishch, mačulišč, matchoulichtch; da: machulishch, mačulišč, matchoulichtch; nb: machulishch, mačulišč, matchoulichtch; is: machulishch, mačulišč, matchoulichtch; fi: machulishch, mačulišč, matchoulichtch; et: machulishch, mačulišč, matchoulichtch; hu: machulishch, mačulišč, matchoulichtch; cs: machulishch, mačulišč, matchoulichtch; sk: machulishch, mačulišč, matchoulichtch; sl: machulishch, mačulišč, matchoulichtch; hr: machulishch, mačulišč, matchoulichtch; bs: machulishch, mačulišč, matchoulichtch; sr: machulishch, mačulišč, matchoulichtch, мачулищ, мачулишт; mk: мачулищ, мачулишт; bg: мачулищ, мачулишт; sq: machulishch, mačulišč, matchoulichtch; el: ; tr: machulishch, mačulišč, matchoulichtch; fa:  |
| BY-ZYA | Зябровка | да | ru: зябровк; be: зябраўк; uk: зябровк; pl: ziabrowk; lt: zabrovk; lv: zjabrovk; en: zyabrovka, ziabrauka; de: sjabrowka; fr: zyabrovk, ziabrauk, zjabrovk, zjabrauk; it: zyabrovk, ziabrauk, zjabrovk, zjabrauk; es: zyabrovk, ziabrauk, zjabrovk, zjabrauk; pt: zyabrovk, ziabrauk, zjabrovk, zjabrauk; ca: zyabrovk, ziabrauk, zjabrovk, zjabrauk; ro: zyabrovk, ziabrauk, zjabrovk, zjabrauk; nl: zyabrovk, ziabrauk, zjabrovk, zjabrauk; sv: zyabrovk, ziabrauk, zjabrovk, zjabrauk; da: zyabrovk, ziabrauk, zjabrovk, zjabrauk; nb: zyabrovk, ziabrauk, zjabrovk, zjabrauk; is: zyabrovk, ziabrauk, zjabrovk, zjabrauk; fi: zyabrovk, ziabrauk, zjabrovk, zjabrauk; et: zyabrovk, ziabrauk, zjabrovk, zjabrauk; hu: zyabrovk, ziabrauk, zjabrovk, zjabrauk; cs: zyabrovk, ziabrauk, zjabrovk, zjabrauk; sk: zyabrovk, ziabrauk, zjabrovk, zjabrauk; sl: zyabrovk, ziabrauk, zjabrovk, zjabrauk; hr: zyabrovk, ziabrauk, zjabrovk, zjabrauk; bs: zyabrovk, ziabrauk, zjabrovk, zjabrauk; sr: zyabrovk, ziabrauk, zjabrovk, zjabrauk, зябровк; mk: зябровк; bg: зябровк; sq: zyabrovk, ziabrauk, zjabrovk, zjabrauk; el: ; tr: zyabrovk, ziabrauk, zjabrovk, zjabrauk; fa:  |
| BY-PTK | пункты пропуска РБ (Брузги, Беняконе, Каменный Лог, Григоровщина, Козловичи, Песчатка, Новая Гута) | да | ru: брузг, бенякон, каменн лог, григоровщин, козлович, песчатк, нов гут; be: брузгі, беняконі, каменн лог, грыгароўшчын, казловіч, пясчатк, нов гут; uk: брузг, бенякон, кам'ян лог, григорівщин, козлович; pl: bruzgi, kuźnic, bobrownik, terespol, koroszczyn, sławatycz, połowc; lt: medinink, šalčinink, lavoriškės, raigard, tverečius, vidzai; lv: paterniek, silen, urbanov; en: bruzgi, kuznica, medininkai, salcininkai, paternieki, terespol; de: bruzgi, kuźnica, medininkai, terespol; fr: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; it: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; es: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; pt: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; ca: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; ro: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; nl: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; sv: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; da: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; nb: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; is: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; fi: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; et: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; hu: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; cs: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; sk: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; sl: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; hr: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; bs: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; sr: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol, брузги, кузница, медининкай, тереспол; mk: брузги, кузница, медининкай, тереспол; bg: брузги, кузница, медининкай, тереспол; sq: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; el: ; tr: bruzgi, kuźnica, kuznica, medininkai, šalčininkai, salcininkai, paternieki, terespol; fa:  |
| LT-VNO | Вильнюс |  | ru: вильнюс; be: вільнюс, вільня; uk: вільнюс; pl: wilno, wilni, wilnie, wilnem, vilnius; lt: vilni, vilnius; lv: viļņ; en: vilnius; de: vilnius, wilna; fr: vilnius, vilniu; it: vilnius, vilniu; es: vilnius, vilniu; pt: vílnius, vilnius, vilniu; ca: vilnius, vilniu; ro: vilnius, vilniu; nl: vilnius, vilniu; sv: vilnius, vilniu; da: vilnius, vilniu; nb: vilnius, vilniu; is: vilníus, vilnius, vilniu; fi: vilna, vilnius, vilniu; et: vilnius, vilniu; hu: vilnius, vilniu; cs: vilnius, vilniu; sk: vilnius, vilniu; sl: vilnius, vilniu; hr: vilnius, vilniu; bs: vilnius, vilniu; sr: vilnius, vilniu, вилнюс, вилњус; mk: вилнюс, вилњус; bg: вилнюс, вилњус; sq: vilnius, vilniu; el: βίλνιους, βιλνιους; tr: vilnius, vilniu; fa: ویلنیوس, ويلنيوس |
| PL-WAW | Варшава |  | ru: варшав; be: варшав; uk: варшав; pl: warszaw; lt: varšuv; lv: varšav; en: warsaw; de: warschau; fr: varsovie; it: varsavia; es: varsovia; pt: varsóvia; ca: varsòvia; ro: varșovia, varşovia, varsovia; nl: warschau; sv: warszawa; da: warszawa; nb: warszawa; is: varsjá; fi: varsova; et: varssavi; hu: varsó; cs: varšav; sk: varšav; sl: varšav; hr: varšav; bs: varšav; sr: varšav, варшав; mk: варшава; bg: варшава; sq: varshav; el: βαρσοβί; tr: varşova; fa: ورشو |
| PL-BIA | Белосток |  | ru: белосток; be: беласток; uk: білосток; pl: białyst, białymst, bialyst; lt: balstog; lv: belostok; en: bialystok; de: bialystok; fr: białystok, bialystok, białymstok; it: białystok, bialystok, białymstok; es: białystok, bialystok, białymstok; pt: białystok, bialystok, białymstok; ca: białystok, bialystok, białymstok; ro: białystok, bialystok, białymstok; nl: białystok, bialystok, białymstok; sv: białystok, bialystok, białymstok; da: białystok, bialystok, białymstok; nb: białystok, bialystok, białymstok; is: białystok, bialystok, białymstok; fi: białystok, bialystok, białymstok; et: białystok, bialystok, białymstok; hu: białystok, bialystok, białymstok; cs: białystok, bialystok, białymstok; sk: białystok, bialystok, białymstok; sl: białystok, bialystok, białymstok; hr: białystok, bialystok, białymstok; bs: białystok, bialystok, białymstok; sr: białystok, bialystok, białymstok, бялисток, бјалисток, белосток; mk: бялисток, бјалисток, белосток; bg: бялисток, бјалисток, белосток; sq: białystok, bialystok, białymstok; el: μπιάλιστοκ; tr: białystok, bialystok, białymstok; fa:  |
| LV-RIX | Рига |  | ru: риг; be: рыг; uk: риг; pl: ryd, ryg; lt: ryg; lv: rīg; en: riga; de: riga; fr: riga, rīga; it: riga, rīga; es: riga, rīga; pt: riga, rīga; ca: riga, rīga; ro: riga, rīga; nl: riga, rīga; sv: riga, rīga; da: riga, rīga; nb: riga, rīga; is: ríga, riga, rīga; fi: riika, riga, rīga; et: riia, riga, rīga; hu: riga, rīga; cs: riga, rīga; sk: riga, rīga; sl: riga, rīga; hr: riga, rīga; bs: riga, rīga; sr: riga, rīga, рига; mk: рига; bg: рига; sq: riga, rīga; el: ρίγα; tr: riga, rīga; fa: ریگا, ريگا |
| UA-KYI | Киев |  | ru: киев; be: кіев; uk: київ, києв; pl: kijów, kijow, kijow; lt: kyjiv, kijev; lv: kijiv, kijev; en: kyiv, kiev; de: kiew; fr: kiev, kyiv; it: kiev, kyiv; es: kiev, kyiv; pt: kiev, kyiv; ca: kíiv, kíev, kyiv; ro: kiev, kyiv; nl: kiev, kyiv; sv: kiev, kyiv; da: kyiv, kiev; nb: kyiv, kiev; is: kænugarð, kyiv, kíev; fi: kiova, kiev, kyiv; et: kiiev, kyiv; hu: kijev, kijiv; cs: kyjev, kyjiv; sk: kyjev, kyjiv; sl: kijev, kijiv; hr: kijev, kijiv; bs: kijev, kijiv; sr: kijev, kijiv, кијев, кијив; mk: киев; bg: киев; sq: kiev, kyiv; el: κίεβο, κιέβο, κίεβ; tr: kiev, kyiv; fa: کی‌یف, كي‌يف, کییف, كييف |
| RU-MOW | Москва |  | ru: москв; be: маскв; uk: москв; pl: moskw; lt: maskv; lv: maskav; en: moscow; de: moskau; fr: moscou; it: mosca; es: moscú, moscu; pt: moscou, moscovo; ca: moscou; ro: moscov; nl: moskou; sv: moskva; da: moskva; nb: moskva; is: moskv; fi: moskov; et: moskv; hu: moszkv; cs: moskv; sk: moskv; sl: moskv; hr: moskv; bs: moskv; sr: moskv, москв; mk: москв; bg: москв; sq: moskë, moska, moskës; el: μόσχα, μόσχας, μοσχα; tr: moskova; fa: مسکو, مسكو |
| SUW | Сувалкский коридор |  | ru: сувалк; be: сувалк; uk: сувалк; pl: suwał, suwal; lt: suvalk; lv: suvalk; en: suwalki; de: suwalki; fr: suwałk, suwalk, suvalk; it: suwałk, suwalk, suvalk; es: suwałk, suwalk, suvalk; pt: suwałk, suwalk, suvalk; ca: suwałk, suwalk, suvalk; ro: suwałk, suwalk, suvalk; nl: suwałk, suwalk, suvalk; sv: suwałk, suwalk, suvalk; da: suwałk, suwalk, suvalk; nb: suwałk, suwalk, suvalk; is: suwałk, suwalk, suvalk; fi: suwałk, suwalk, suvalk; et: suwałk, suwalk, suvalk; hu: suwałk, suwalk, suvalk; cs: suwałk, suwalk, suvalk; sk: suwałk, suwalk, suvalk; sl: suwałk, suwalk, suvalk; hr: suwałk, suwalk, suvalk; bs: suwałk, suwalk, suvalk; sr: suwałk, suwalk, suvalk, сувалк; mk: сувалк; bg: сувалк; sq: suwałk, suwalk, suvalk; el: σουβάλκ; tr: suwałk, suwalk, suvalk; fa:  |
| LT | Литва |  | ru: литв, литовск; be: літв, літоўск; uk: литв, литовськ; pl: litw, litewsk; lt: lietuv; lv: lietuv, lietuviešu; en: lithuania; de: litauen, litauisch; fr: lituanie, lituanien; it: lituani; es: lituani; pt: lituâni, lituani; ca: lituàni, lituan; ro: lituani; nl: litouw; sv: litau; da: litau; nb: litau; is: litháen; fi: liettu; et: leedu; hu: litván; cs: litva, litvy, litvě, litvu, litevsk; sk: litva, litvy, litve, litvu, litovsk; sl: litva, litve, litvi, litvo, litovsk, litvansk; hr: litva, litve, litvi, litvu, litavsk, litvansk; bs: litva, litve, litvi, litvu, litvansk; sr: litva, litve, litvi, litvu, litvansk, литва, литве, литви, литву, литванск; mk: литва, литванск; bg: литва, литовск; sq: lituani; el: λιθουαν; tr: litvanya; fa: لیتوانی, ليتواني |
| PL | Польша |  | ru: польш, польск; be: польшч, польск; uk: польщ, польськ; pl: polsk, polsc; lt: lenkij, lenkų; lv: polij, poļu; en: poland, polish; de: polen, polnisch; fr: pologne, polonais; it: polonia, polacc; es: polonia, polac; pt: polónia, polônia, polaco, polaca, polonês, polonesa; ca: polònia, polonès, polonesa; ro: polonia, polonez; nl: polen, pools, poolse; sv: polen, polsk; da: polen, polsk; nb: polen, polsk; is: pólland, póllandi, pólsk; fi: puola, puolan, puolassa, puolaan, puolalai; et: poola; hu: lengyel; cs: polsk; sk: poľsk; sl: poljsk; hr: poljsk; bs: poljsk; sr: poljsk, пољск; mk: полск; bg: полш, полск; sq: poloni; el: πολων; tr: polonya; fa: لهستان |
| LV | Латвия |  | ru: латви, латвийск; be: латвi, латвійск; uk: латві, латвійськ; pl: łotw, łotewsk; lt: latvij; lv: latvij; en: latvia, latvian; de: lettland, lettisch; fr: lettonie, letton; it: lettoni; es: letoni; pt: letóni, letôni, letão; ca: letòni; ro: letoni; nl: letland; sv: lettland; da: letland; nb: latvia, lettland; is: lettland; fi: latvia; et: läti; hu: lettorsz; cs: lotyš; sk: lotyš; sl: latvij; hr: latvij; bs: latvij; sr: letonij, latvij, летониј, латвиј; mk: латвиј; bg: латвия, латвий, латвийск; sq: letoni; el: λετονί; tr: letonya; fa: لتونی, لتوني |
| UA | Украина |  | ru: украин; be: украін, украiн; uk: україн; pl: ukrain; lt: ukrain; lv: ukrain; en: ukrain; de: ukrain; fr: ukrain; it: ucrain; es: ucrani; pt: ucrâni, ucrani; ca: ucraïn; ro: ucrain; nl: oekraïn, oekrain; sv: ukrain; da: ukrain; nb: ukrain; is: úkraín; fi: ukrain; et: ukrain; hu: ukrajn; cs: ukrajin; sk: ukrajin; sl: ukrajin; hr: ukrajin; bs: ukrajin; sr: ukrajin, украјин; mk: украин; bg: украйн, украин; sq: ukrain; el: ουκραν; tr: ukrayna; fa: اوکراین, اوكراين |
| RU | Россия |  | ru: росси, российск; be: расі, расійск; uk: росі, російськ; pl: rosj, rosyjsk; lt: rusij, rusijos; lv: krievij; en: russia, russian; de: russland, russisch; fr: russie, russe; it: russia, russo, russa, russi, russe; es: rusia, ruso, rusa, rusos, rusas; pt: rússia, russo, russa, russos, russas; ca: rússia, russos, russes; ro: rusia, rusie, rusesc, ruseasc, rușii, ruşii; nl: rusland, russisch; sv: ryssland, rysk; da: rusland, russisk; nb: russland, russisk; is: rússland, rússnesk; fi: venäj; et: venemaa, vene; hu: orosz; cs: rusk; sk: rusk; sl: rusij, rusk; hr: rusij, rusk; bs: rusij, rusk; sr: rusij, rusk, русиј, руск; mk: русиј, руск; bg: русия, руск; sq: rusi, rusia, rusisë, ruse, rusët; el: ρωσί, ρωσικ, ρώσ; tr: rusya; fa: روسیه, روسيه |

## Организации (ключи «организация»)

| Код | Организация | Формы по языкам |
|---|---|---|
| NATO | НАТО | ru: нато; be: ната; uk: нато; pl: nato; lt: nato; lv: nato; en: nato; de: nato; fr: otan, nato; it: nato; es: otan, nato; pt: otan, nato; ca: otan, nato; ro: nato; nl: navo, nato; sv: nato; da: nato; nb: nato; is: nato, atlantshafsbandalag; fi: nato; et: nato; hu: nato; cs: nato; sk: nato; sl: nato; hr: nato; bs: nato; sr: nato, нато; mk: нато; bg: нато; sq: nato; el: νατο; tr: nato; fa: ناتو |
| EU | Европейский союз | ru: евросоюз, европейск союз, ес; be: еўрасаюз, еўрапейск саюз; uk: євросоюз, європейськ союз, єс; pl: unia europejsk, ue; lt: europos sąjung, es; lv: eiropas savienīb; en: european union, eu; de: europäisch union, eu; fr: union européenne, ue; it: unione europea, ue; es: unión europea, ue; pt: união europeia, ue; ca: unió europea, ue; ro: uniunea europeană, uniunii europene, ue; nl: europese unie, eu; sv: europeiska unionen, eu; da: europæiske union, eu; nb: europeiske union, eu; is: evrópusamband, esb; fi: euroopan unioni, eu; et: euroopa liit; hu: európai unió, eu; cs: evropská unie, evropské unie, eu; sk: európska únia, európskej únie, eú; sl: evropska unija, evropske unije, eu; hr: europska unija, europske unije, eu; bs: evropska unija, evropske unije, eu; sr: evropska unija, evropske unije, eu, европска унија, европске уније, еу; mk: европска унија, европската унија, еу; bg: европейски съюз, европейския съюз, ес; sq: bashkimi evropian, bashkimit evropian; el: ευρωπαϊκή ένωσ, ευρωπαϊκής ένωσ; tr: avrupa birliği, ab; fa: اتحادیه اروپا, اتحاديه اروپا |
| UN | ООН | ru: оон; be: аан; uk: оон; pl: onz; lt: jt, jungtinių tautų; lv: ano; en: united nations, un; de: vereinten nationen, uno; fr: onu, nations unies; it: onu, nazioni unite; es: onu, naciones unidas; pt: onu, nações unidas; ca: onu, nacions unides; ro: onu, națiunile unite; nl: verenigde naties, vn; sv: förenta nationerna, fn; da: forenede nationer, fn; nb: forente nasjoner, fn; is: sameinuðu þjóðirnar, sþ; fi: yhdistyneet kansakunnat, yk; et: ühinenud rahvaste organisatsioon, üro; hu: ensz; cs: osn; sk: osn; sl: ozn, združeni narodi; hr: ujedinjeni narodi, ujedinjenih naroda; bs: ujedinjene nacije, ujedinjenih nacija; sr: ujedinjene nacije, ujedinjenih nacija, уједињене нације, уједињених нација, оун; mk: оон, обединетите нации; bg: оон; sq: kombet e bashkuara, okb; el: οηε; tr: birleşmiş milletler, bm; fa: سازمان ملل |
| OSCE | ОБСЕ | ru: обсе; be: абсе; uk: обсє; pl: obwe; lt: esbo; lv: edso; en: osce; de: osze; fr: osce; it: osce; es: osce; pt: osce; ca: osce; ro: osce; nl: ovse; sv: osse; da: osce; nb: osse; is: öse; fi: etyj; et: osce; hu: ebesz; cs: obse; sk: obse; sl: ovse; hr: oess, ebs; bs: osce, oebs; sr: oebs, оебс; mk: обсе; bg: обсе; sq: osbe; el: οασε; tr: agit; fa: سازمان امنیت و همکاری اروپا, سازمان امنيت و همكاري اروپا |
| FRONTEX | Frontex | ru: фронтекс; be: фронтэкс; uk: фронтекс; pl: frontex; lt: frontex; lv: frontex; en: frontex; de: frontex; fr: frontex; it: frontex; es: frontex; pt: frontex; ca: frontex; ro: frontex; nl: frontex; sv: frontex; da: frontex; nb: frontex; is: frontex; fi: frontex; et: frontex; hu: frontex; cs: frontex; sk: frontex; sl: frontex; hr: frontex; bs: frontex; sr: frontex, фронтекс; mk: фронтекс; bg: фронтекс; sq: frontex; el: frontex, φρόντεξ; tr: frontex; fa: فرونتکس, فرونتكس |
| WAGNER | ЧВК «Вагнер» | ru: вагнер, чвк вагнер; be: вагнер; uk: вагнер, пвк вагнер; pl: wagner, grupa wagnera; lt: vagner, wagner; lv: vāgner, wagner; en: wagner; de: wagner; fr: wagner, vagner; it: wagner, vagner; es: wagner, vagner; pt: wagner, vagner; ca: wagner, vagner; ro: wagner, vagner; nl: wagner, vagner; sv: wagner, vagner; da: wagner, vagner; nb: wagner, vagner; is: wagner, vagner; fi: wagner, vagner; et: wagner, vagner; hu: wagner, vagner; cs: wagner, vagner; sk: wagner, vagner; sl: wagner, vagner; hr: wagner, vagner; bs: wagner, vagner; sr: wagner, vagner, вагнер; mk: вагнер; bg: вагнер; sq: wagner, vagner; el: βάγκνερ, wagner; tr: wagner, vagner; fa: واگنر |
| ORESHNIK | «Орешник» | ru: орешник; be: арэшнік; uk: орєшнік, орешник; pl: oriesznik, oresznik; lt: orešnik; lv: orešņik; en: oreshnik; de: oreschnik; fr: orechnik, oreshnik, orešnik; it: oreshnik, orešnik; es: oreshnik, orešnik; pt: oreshnik, orešnik; ca: oreshnik, orešnik; ro: oreșnik, oreşnik, oreshnik, orešnik; nl: oresjnik, oreshnik, orešnik; sv: oresjnik, oreshnik, orešnik; da: oresjnik, oreshnik, orešnik; nb: oresjnik, oreshnik, orešnik; is: oreshnik, orešnik; fi: oreshnik, orešnik; et: oreshnik, orešnik; hu: oresnyik, oreshnik, orešnik; cs: oreshnik, orešnik; sk: oreshnik, orešnik; sl: oreshnik, orešnik; hr: oreshnik, orešnik; bs: oreshnik, orešnik; sr: oreshnik, orešnik, орешник, орешњик; mk: орешник, орешњик; bg: орешник, орешњик; sq: oreshnik, orešnik; el: ορέσνικ; tr: oreşnik, oreshnik, orešnik; fa: اورشنیک, اورشنيك |
| CSTO | ОДКБ | ru: одкб; be: адкб; uk: одкб; pl: oubz; lt: kssto; lv: kdlo; en: csto; de: ovks; fr: otsc, csto; it: otsc, csto; es: otsc, csto; pt: otsc, csto; ca: otsc, csto; ro: otsc, csto; nl: csto; sv: csto; da: csto; nb: csto; is: csto; fi: csto; et: kjlo, csto; hu: kbszsz, csto; cs: odkb, csto; sk: odkb, csto; sl: odkb, csto; hr: odkb, csto; bs: odkb, csto; sr: odkb, csto, одкб; mk: одкб; bg: одкб; sq: otsk, csto; el: οσσα; tr: kgaö, csto; fa: سازمان پیمان امنیت جمعی, سازمان پيمان امنيت جمعي |
| UNION-STATE | Союзное государство | ru: союзн государств; be: саюзн дзяржав; uk: союзн держав; pl: państw związkow; lt: sąjungin valstyb; lv: savienīb valst; en: union state; de: unionsstaat; fr: ; it: ; es: ; pt: ; ca: ; ro: statul unional; nl: uniestaat; sv: unionsstaten; da: unionsstaten; nb: unionsstaten; is: ; fi: ; et: liiduriik; hu: uniós állam; cs: svazový stát, svazového státu; sk: zväzový štát, zväzového štátu; sl: ; hr: savezna država rusije; bs: ; sr: savezna država rusije, савезна држава русије; mk: сојузната држава; bg: съюзната държава; sq: ; el: ; tr: birlik devleti; fa: دولت اتحادیه روسیه و بلاروس, دولت اتحاديه روسيه و بلاروس |

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

### fr — французский

- **сильные негативные (вес 2)** (23): `sanction`, `arrestation`, `arrêté`, `catastroph`, `accident`, `tué`, `morts`, `faillite`, `accus`, `corruption`, `fraude`, `pot-de-vin`, `détourn`, `répression`, `dictateur`, `dictature`, `terroris`, `crime de guerre`, `complice`, `attaque hybride`, `agression`, `occupation`, `marionnette`
- **негативные (вес 1)** (39): `retard`, `critiqu`, `problème`, `pénurie`, `manque`, `risque`, `litige`, `procès`, `tribunal`, `refus`, `panne`, `vulnérab`, `annul`, `détruit`, `abattu`, `frappe`, `attaque`, `pertes`, `menace`, `provocation`, `violation`, `escalade`, `interdi`, `restriction`, `fermeture de la frontière`, `expuls`, `protest`, `condamn`, `espion`, `contrebande`, `illégal`, `pression`, `régime de loukachenko`, `régime loukachenko`, `invasion`, `déstabilis`, `désinformation`, `crise migratoire`, `instrumentalis`
- **сильные позитивные (вес 2)** (6): `percée`, `record`, `levée des restrictions`, `levée des sanctions`, `milliards d'investissement`, `contrat d'un milliard`
- **позитивные (вес 1)** (21): `contrat`, `commande`, `lancement`, `croissance`, `hausse`, `augment`, `élargi`, `succès`, `réussi`, `modernis`, `livraison`, `coopération`, `partenariat`, `dialogue`, `normalisation`, `libération`, `libéré`, `gracié`, `accord`, `aide humanitaire`, `désescalade`
- **оценочные слова (Субъективность)** (13): `choquant`, `scandaleu`, `honteu`, `désastre`, `humiliant`, `brillant`, `incroyable`, `absurde`, `cynique`, `monstrueu`, `hystéri`, `inouï`, `révoltant`
- **речь от первого лица (Субъективность)** (6): `je pense`, `à mon avis`, `selon moi`, `je crois`, `nous pensons`, `je suis convaincu`
- **окончания** (10): `∅`, `s`, `e`, `es`, `ne`, `nes`, `ien`, `iens`, `ienne`, `iennes`
- **служебные слова для определения языка** (29): le, la, les, de, des, du, et, en, un, une, est, que, qui, dans, pour, sur, pas, par, avec, au, aux, ce, cette, il, elle, sont, été, plus, selon
- **месяцы (для ключей-дат)**: janvier, février, mars, avril, mai, juin, juillet, août, septembre, octobre, novembre, décembre

### it — итальянский

- **сильные негативные (вес 2)** (23): `sanzion`, `arrest`, `catastrof`, `incidente`, `uccis`, `morti`, `fallimento`, `accus`, `corruzion`, `frode`, `tangent`, `appropriazione`, `repression`, `dittatore`, `dittatura`, `terroris`, `crimini di guerra`, `crimine di guerra`, `complic`, `attacco ibrido`, `aggression`, `occupazion`, `fantoccio`
- **негативные (вес 1)** (41): `ritard`, `critic`, `problem`, `carenz`, `mancanz`, `rischi`, `controversi`, `processo`, `tribunale`, `rifiut`, `guasto`, `vulnerab`, `annull`, `distrutt`, `abbattut`, `attacc`, `perdite`, `minacc`, `provocazion`, `violazion`, `escalation`, `divieto`, `vietat`, `restrizion`, `chiusura del confine`, `chiusura della frontiera`, `espuls`, `protest`, `condann`, `spia`, `spie`, `spionaggio`, `contrabband`, `illegal`, `pression`, `regime di lukashenko`, `invasion`, `destabilizz`, `disinformazion`, `crisi migratoria`, `strumentalizz`
- **сильные позитивные (вес 2)** (6): `svolta`, `record`, `revoca delle restrizioni`, `revoca delle sanzioni`, `miliardi di investimenti`, `contratto miliardario`
- **позитивные (вес 1)** (20): `contratto`, `ordine`, `lancio`, `crescita`, `aument`, `ampliament`, `successo`, `riuscit`, `modernizz`, `fornitur`, `cooperazion`, `partenariato`, `dialogo`, `normalizzazion`, `liberazion`, `liberat`, `grazia`, `accordo`, `aiuti umanitari`, `distension`
- **оценочные слова (Субъективность)** (13): `scioccant`, `scandalos`, `vergognos`, `disastro`, `umiliant`, `brillant`, `incredibil`, `assurd`, `cinic`, `mostruos`, `isteri`, `inaudit`, `sconvolgent`
- **речь от первого лица (Субъективность)** (6): `penso che`, `a mio avviso`, `secondo me`, `credo che`, `riteniamo`, `sono convinto`
- **окончания** (11): `∅`, `a`, `e`, `i`, `o`, `ia`, `ie`, `no`, `na`, `ni`, `ne`
- **служебные слова для определения языка** (27): il, lo, la, gli, le, di, del, della, che, e, è, un, una, per, con, non, sono, nel, nella, al, alla, dei, delle, ha, anche, più, secondo
- **месяцы (для ключей-дат)**: gennaio, febbraio, marzo, aprile, maggio, giugno, luglio, agosto, settembre, ottobre, novembre, dicembre

### es — испанский

- **сильные негативные (вес 2)** (24): `sancion`, `detenido`, `arrest`, `catástrof`, `accidente`, `muertos`, `asesinad`, `quiebra`, `acus`, `corrupción`, `fraude`, `soborno`, `malversación`, `represión`, `dictador`, `dictadura`, `terroris`, `crimen de guerra`, `crímenes de guerra`, `cómplice`, `ataque híbrido`, `agresión`, `ocupación`, `títere`
- **негативные (вес 1)** (41): `retras`, `crític`, `critica`, `problema`, `escasez`, `falta`, `riesgo`, `disputa`, `demanda`, `tribunal`, `rechaz`, `fallo`, `vulnerab`, `cancel`, `destrui`, `derriba`, `ataque`, `atac`, `pérdida`, `amenaz`, `provocación`, `violación`, `escalada`, `prohib`, `restricci`, `cierre de la frontera`, `cierre fronterizo`, `expuls`, `protest`, `conden`, `espía`, `espionaje`, `contraband`, `ilegal`, `presión`, `régimen de lukashenko`, `invasión`, `desestabiliz`, `desinformación`, `crisis migratoria`, `instrumentaliz`
- **сильные позитивные (вес 2)** (5): `avance histórico`, `récord`, `levantamiento de las restricciones`, `levantamiento de las sanciones`, `levantó las sanciones`
- **позитивные (вес 1)** (20): `contrato`, `pedido`, `lanzamiento`, `crecimiento`, `aument`, `ampliación`, `éxito`, `moderniz`, `suministro`, `entrega`, `cooperación`, `asociación`, `diálogo`, `normalización`, `liberación`, `liberad`, `indult`, `acuerdo`, `ayuda humanitaria`, `desescalada`
- **оценочные слова (Субъективность)** (13): `impactant`, `escandalos`, `vergonzos`, `desastre`, `humillant`, `brillant`, `increíble`, `absurd`, `cínic`, `monstruos`, `histéri`, `inaudit`, `indignant`
- **речь от первого лица (Субъективность)** (6): `creo que`, `en mi opinión`, `a mi juicio`, `pienso que`, `consideramos`, `estoy convencido`
- **окончания** (12): `∅`, `s`, `a`, `as`, `o`, `os`, `es`, `ia`, `no`, `na`, `nos`, `nas`
- **служебные слова для определения языка** (26): el, la, los, las, de, del, que, y, en, un, una, es, por, con, no, para, se, al, lo, como, más, pero, sus, ha, según, también
- **месяцы (для ключей-дат)**: enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre

### pt — португальский

- **сильные негативные (вес 2)** (23): `sanç`, `detido`, `prisão`, `catástrof`, `acidente`, `mortos`, `falência`, `acus`, `corrupção`, `fraude`, `suborno`, `desvio`, `repressão`, `ditador`, `ditadura`, `terroris`, `crime de guerra`, `crimes de guerra`, `cúmplice`, `ataque híbrido`, `agressão`, `ocupação`, `fantoche`
- **негативные (вес 1)** (43): `atras`, `crític`, `critica`, `problema`, `escassez`, `falta`, `risco`, `disputa`, `processo`, `tribunal`, `recus`, `falha`, `vulnerá`, `cancel`, `destruí`, `destruid`, `abatid`, `ataque`, `atac`, `perda`, `ameaç`, `provocação`, `violação`, `escalada`, `proib`, `restriç`, `fecho da fronteira`, `fechamento da fronteira`, `expuls`, `protest`, `conden`, `espião`, `espiões`, `espionagem`, `contraband`, `ilegal`, `pressão`, `regime de lukashenko`, `invasão`, `desestabiliz`, `desinformação`, `crise migratória`, `instrumentaliz`
- **сильные позитивные (вес 2)** (5): `avanço histórico`, `recorde`, `levantamento das restrições`, `levantamento das sanções`, `levantou as sanções`
- **позитивные (вес 1)** (21): `contrato`, `encomenda`, `lançamento`, `crescimento`, `aument`, `ampliação`, `sucesso`, `bem-sucedid`, `moderniz`, `fornecimento`, `entrega`, `cooperação`, `parceria`, `diálogo`, `normalização`, `libertação`, `libertad`, `indult`, `acordo`, `ajuda humanitária`, `desescalada`
- **оценочные слова (Субъективность)** (13): `chocant`, `escandalos`, `vergonhos`, `desastre`, `humilhant`, `brilhant`, `incrível`, `absurd`, `cínic`, `monstruos`, `histéri`, `inaudit`, `revoltant`
- **речь от первого лица (Субъективность)** (6): `acho que`, `na minha opinião`, `creio que`, `penso que`, `consideramos`, `estou convencido`
- **окончания** (12): `∅`, `s`, `a`, `as`, `o`, `os`, `es`, `ia`, `no`, `na`, `nos`, `nas`
- **служебные слова для определения языка** (29): o, a, os, as, de, do, da, dos, das, que, e, em, um, uma, é, por, com, não, para, se, ao, mais, como, mas, foi, pelo, pela, segundo, também
- **месяцы (для ключей-дат)**: janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro

### ca — каталанский

- **сильные негативные (вес 2)** (22): `sancion`, `detingut`, `detenció`, `catàstrof`, `accident`, `morts`, `fallida`, `acusa`, `corrupció`, `frau`, `suborn`, `repressió`, `dictador`, `dictadura`, `terroris`, `crim de guerra`, `crims de guerra`, `còmplice`, `atac híbrid`, `agressió`, `ocupació`, `titella`
- **негативные (вес 1)** (37): `retard`, `crític`, `problema`, `escassetat`, `manca`, `risc`, `disputa`, `judici`, `tribunal`, `rebuig`, `fallada`, `vulnerab`, `cancel`, `destruï`, `abatut`, `atac`, `pèrdu`, `amenaç`, `provocació`, `violació`, `escalada`, `prohib`, `restricci`, `tancament de la frontera`, `expuls`, `protest`, `condemn`, `espia`, `espionatge`, `contraban`, `il·legal`, `pressió`, `règim de lukaixenko`, `invasió`, `desestabilitz`, `desinformació`, `crisi migratòria`
- **сильные позитивные (вес 2)** (4): `avenç històric`, `rècord`, `aixecament de les restriccions`, `aixecament de les sancions`
- **позитивные (вес 1)** (19): `contracte`, `comanda`, `llançament`, `creixement`, `augment`, `ampliació`, `èxit`, `moderniz`, `subministrament`, `cooperació`, `associació`, `diàleg`, `normalització`, `alliberament`, `alliberat`, `indult`, `acord`, `ajuda humanitària`, `desescalada`
- **оценочные слова (Субъективность)** (11): `impactant`, `escandalós`, `vergonyós`, `desastre`, `humiliant`, `brillant`, `increïble`, `absurd`, `cínic`, `monstruós`, `histèri`
- **речь от первого лица (Субъективность)** (5): `crec que`, `en la meva opinió`, `penso que`, `considerem`, `estic convençut`
- **окончания** (8): `∅`, `s`, `a`, `es`, `os`, `ia`, `ià`, `ns`
- **служебные слова для определения языка** (24): el, la, els, les, de, del, que, i, en, un, una, és, per, amb, no, als, al, més, com, però, ha, segons, també, aquest
- **месяцы (для ключей-дат)**: gener, febrer, març, abril, maig, juny, juliol, agost, setembre, octubre, novembre, desembre

### ro — румынский

- **сильные негативные (вес 2)** (27): `sancțiun`, `sancţiun`, `sanctiun`, `arestat`, `arestar`, `catastrof`, `accident`, `uciși`, `morți`, `faliment`, `acuza`, `acuzat`, `corupți`, `fraud`, `mită`, `delapidar`, `represiun`, `dictator`, `dictatur`, `terori`, `crime de război`, `crimă de război`, `complic`, `atac hibrid`, `agresiun`, `ocupați`, `marionet`
- **негативные (вес 1)** (42): `întârzi`, `critic`, `problem`, `deficit`, `lipsa`, `lipsă`, `risc`, `dispută`, `proces`, `instanț`, `refuz`, `defecțiun`, `vulnerab`, `anulat`, `anular`, `distrus`, `doborât`, `lovitur`, `atac`, `pierder`, `amenința`, `amenint`, `provocar`, `încălca`, `escaladar`, `interzi`, `restricți`, `închiderea frontierei`, `expulz`, `protest`, `condamn`, `spion`, `contraband`, `ilegal`, `presiun`, `regimul lui lukașenko`, `regimul de la minsk`, `invazi`, `destabiliz`, `dezinformar`, `criza migranț`, `criză migrator`
- **сильные позитивные (вес 2)** (5): `descoperire`, `record`, `ridicarea restricțiilor`, `ridicarea sancțiunilor`, `investiție de miliarde`
- **позитивные (вес 1)** (22): `contract`, `comand`, `lansar`, `creșter`, `creşter`, `majorar`, `extinder`, `succes`, `reușit`, `moderniz`, `livrar`, `cooperar`, `parteneriat`, `dialog`, `normalizar`, `eliberar`, `eliberat`, `grațier`, `acord`, `ajutor umanitar`, `detensionar`, `dezescaladar`
- **оценочные слова (Субъективность)** (12): `șocant`, `scandalos`, `rușinos`, `dezastru`, `umilitor`, `strălucit`, `incredibil`, `absurd`, `cinic`, `monstruos`, `isteri`, `revoltător`
- **речь от первого лица (Субъективность)** (5): `cred că`, `în opinia mea`, `părerea mea`, `considerăm`, `sunt convins`
- **окончания** (14): `∅`, `a`, `ul`, `ului`, `ei`, `ii`, `ilor`, `e`, `i`, `le`, `lor`, `ă`, `ia`, `iei`
- **служебные слова для определения языка** (24): și, în, de, la, cu, pe, nu, care, este, un, o, a, al, ale, lui, din, pentru, mai, dar, sunt, fost, după, că, se
- **месяцы (для ключей-дат)**: ianuarie, februarie, martie, aprilie, mai, iunie, iulie, august, septembrie, octombrie, noiembrie, decembrie

### nl — нидерландский

- **сильные негативные (вес 2)** (23): `sanctie`, `arrestat`, `gearresteerd`, `ramp`, `ongeluk`, `gedood`, `doden`, `faillis`, `beschuldig`, `corruptie`, `fraude`, `omkoping`, `verduister`, `repressie`, `dictator`, `terreur`, `terroris`, `oorlogsmisdad`, `medeplichtig`, `hybride aanval`, `agressie`, `bezetting`, `marionet`
- **негативные (вес 1)** (42): `vertraging`, `kritiek`, `probleem`, `problemen`, `tekort`, `risico`, `geschil`, `rechtszaak`, `rechtbank`, `weiger`, `storing`, `kwetsbaar`, `geannuleerd`, `vernietig`, `neergeschoten`, `aanval`, `verlies`, `verliezen`, `dreig`, `provocatie`, `schending`, `geschonden`, `escalatie`, `verbod`, `verboden`, `beperking`, `grenssluiting`, `grens gesloten`, `uitgezet`, `uitzetting`, `protest`, `veroordeel`, `spion`, `smokkel`, `illegaal`, `onwettig`, `regime van loekasjenko`, `loekasjenko-regime`, `invasie`, `destabilis`, `desinformatie`, `migratiecrisis`
- **сильные позитивные (вес 2)** (6): `doorbraak`, `record`, `opheffing van de beperkingen`, `opheffing van de sancties`, `sancties opgeheven`, `miljardeninvestering`
- **позитивные (вес 1)** (21): `contract`, `bestelling`, `lancering`, `groei`, `toename`, `uitbreiding`, `succes`, `geslaagd`, `modernis`, `levering`, `samenwerking`, `partnerschap`, `dialoog`, `normalisatie`, `vrijlating`, `vrijgelaten`, `gratie`, `akkoord`, `overeenkomst`, `humanitaire hulp`, `de-escalatie`
- **оценочные слова (Субъективность)** (12): `schokkend`, `schandalig`, `beschamend`, `rampzalig`, `vernederend`, `briljant`, `ongelooflijk`, `absurd`, `cynisch`, `monsterlijk`, `hysteri`, `stuitend`
- **речь от первого лица (Субъективность)** (6): `ik denk`, `naar mijn mening`, `volgens mij`, `ik geloof`, `wij vinden`, `ik ben ervan overtuigd`
- **окончания** (6): `∅`, `s`, `e`, `en`, `se`, `'s`
- **служебные слова для определения языка** (24): de, het, een, en, van, in, is, dat, op, te, met, voor, niet, zijn, aan, door, ook, als, bij, om, naar, maar, heeft, werd
- **месяцы (для ключей-дат)**: januari, februari, maart, april, mei, juni, juli, augustus, september, oktober, november, december

### sv — шведский

- **сильные негативные (вес 2)** (24): `sanktion`, `gripen`, `arrester`, `katastrof`, `olycka`, `dödad`, `döda`, `konkurs`, `anklag`, `korruption`, `bedrägeri`, `muta`, `mutor`, `förskingr`, `förtryck`, `diktator`, `diktatur`, `terror`, `krigsbrott`, `medbrottsl`, `hybridattack`, `aggression`, `ockupation`, `marionett`
- **негативные (вес 1)** (41): `försen`, `kritik`, `problem`, `brist`, `risk`, `tvist`, `stämning`, `domstol`, `vägra`, `avslag`, `sårbar`, `inställ`, `förstör`, `skjuts ner`, `skjutits ner`, `angrepp`, `attack`, `förlust`, `hot`, `provokation`, `kränkning`, `brott mot`, `eskaler`, `förbud`, `förbjud`, `begränsning`, `stänger gränsen`, `stängd gräns`, `utvis`, `protest`, `fördöm`, `spion`, `smuggl`, `olaglig`, `olagligt`, `påtryckning`, `lukasjenkos regim`, `invasion`, `destabilis`, `desinformation`, `migrationskris`
- **сильные позитивные (вес 2)** (6): `genombrott`, `rekord`, `hävde restriktionerna`, `hävda sanktioner`, `sanktionerna hävs`, `miljardinvestering`
- **позитивные (вес 1)** (22): `kontrakt`, `beställning`, `lansering`, `tillväxt`, `ökning`, `utbyggnad`, `framgång`, `lyckad`, `modernis`, `leverans`, `samarbet`, `partnerskap`, `dialog`, `normalisering`, `frisläpp`, `frigiv`, `benådning`, `benådad`, `avtal`, `överenskommelse`, `humanitärt bistånd`, `nedtrappning`
- **оценочные слова (Субъективность)** (12): `chockerande`, `skandalös`, `skamlig`, `katastrofal`, `förnedrande`, `lysande`, `otrolig`, `absurd`, `cynisk`, `monstruös`, `hysteri`, `upprörande`
- **речь от первого лица (Субъективность)** (5): `jag tror`, `jag anser`, `enligt min mening`, `vi anser`, `jag är övertygad`
- **окончания** (10): `∅`, `s`, `en`, `ens`, `et`, `ets`, `a`, `as`, `isk`, `iska`
- **служебные слова для определения языка** (24): och, i, att, det, som, en, på, är, av, för, med, till, den, inte, har, de, om, ett, var, från, också, efter, kan, sig
- **месяцы (для ключей-дат)**: januari, februari, mars, april, maj, juni, juli, augusti, september, oktober, november, december

### da — датский

- **сильные негативные (вес 2)** (23): `sanktion`, `anholdt`, `arrestat`, `katastrof`, `ulykke`, `dræbt`, `døde`, `konkurs`, `anklag`, `korruption`, `bedrageri`, `bestikkelse`, `underslæb`, `undertrykk`, `diktator`, `diktatur`, `terror`, `krigsforbryd`, `medskyldig`, `hybridangreb`, `aggression`, `besættelse`, `marionet`
- **негативные (вес 1)** (36): `forsink`, `kritik`, `problem`, `mangel`, `risiko`, `tvist`, `retssag`, `domstol`, `afvis`, `sårbar`, `aflys`, `ødelag`, `skudt ned`, `angreb`, `trussel`, `trusler`, `provokation`, `krænkelse`, `overtræd`, `eskaler`, `forbud`, `begrænsning`, `lukker grænsen`, `lukket grænse`, `udvis`, `protest`, `fordøm`, `spion`, `smugl`, `ulovlig`, `pres`, `lukasjenkos regime`, `invasion`, `destabilis`, `desinformation`, `migrationskrise`
- **сильные позитивные (вес 2)** (6): `gennembrud`, `rekord`, `ophævelse af restriktion`, `ophævelse af sanktion`, `sanktionerne ophæv`, `milliardinvestering`
- **позитивные (вес 1)** (21): `kontrakt`, `bestilling`, `lancering`, `vækst`, `stigning`, `udvidelse`, `succes`, `vellykk`, `modernis`, `levering`, `samarbejd`, `partnerskab`, `dialog`, `normalisering`, `løsladel`, `løsladt`, `benådning`, `benådet`, `aftale`, `humanitær hjælp`, `nedtrapning`
- **оценочные слова (Субъективность)** (12): `chokerende`, `skandaløs`, `skammelig`, `katastrofal`, `ydmygende`, `strålende`, `utrolig`, `absurd`, `kynisk`, `monstrøs`, `hysteri`, `oprørende`
- **речь от первого лица (Субъективность)** (5): `jeg tror`, `jeg mener`, `efter min mening`, `vi mener`, `jeg er overbevist`
- **окончания** (10): `∅`, `s`, `en`, `ens`, `et`, `ets`, `e`, `es`, `isk`, `iske`
- **служебные слова для определения языка** (25): og, i, at, det, som, en, på, er, af, for, med, til, den, ikke, har, de, om, et, var, fra, også, efter, kan, sig, blev
- **месяцы (для ключей-дат)**: januar, februar, marts, april, maj, juni, juli, august, september, oktober, november, december

### nb — норвежский (букмол)

- **сильные негативные (вес 2)** (23): `sanksjon`, `pågrepet`, `arrestert`, `katastrofe`, `ulykke`, `drept`, `døde`, `konkurs`, `anklag`, `korrupsjon`, `bedrageri`, `bestikkelse`, `underslag`, `undertrykk`, `diktator`, `diktatur`, `terror`, `krigsforbryt`, `medskyldig`, `hybridangrep`, `aggresjon`, `okkupasjon`, `marionett`
- **негативные (вес 1)** (37): `forsink`, `kritikk`, `problem`, `mangel`, `risiko`, `tvist`, `søksmål`, `domstol`, `avvis`, `sårbar`, `avlys`, `ødelagt`, `skutt ned`, `angrep`, `trussel`, `trusler`, `provokasjon`, `krenkelse`, `brudd på`, `eskaler`, `forbud`, `forbudt`, `begrensning`, `stenger grensen`, `stengt grense`, `utvis`, `protest`, `fordøm`, `spion`, `smugl`, `ulovlig`, `press`, `lukasjenkos regime`, `invasjon`, `destabilis`, `desinformasjon`, `migrasjonskrise`
- **сильные позитивные (вес 2)** (6): `gjennombrudd`, `rekord`, `opphevelse av restriksjon`, `opphevelse av sanksjon`, `sanksjonene oppheves`, `milliardinvestering`
- **позитивные (вес 1)** (21): `kontrakt`, `bestilling`, `lansering`, `vekst`, `økning`, `utvidelse`, `suksess`, `vellykk`, `modernis`, `levering`, `samarbeid`, `partnerskap`, `dialog`, `normalisering`, `løslatelse`, `løslatt`, `benådning`, `benådet`, `avtale`, `humanitær hjelp`, `nedtrapping`
- **оценочные слова (Субъективность)** (12): `sjokkerende`, `skandaløs`, `skammelig`, `katastrofal`, `ydmykende`, `strålende`, `utrolig`, `absurd`, `kynisk`, `monstrøs`, `hysteri`, `opprørende`
- **речь от первого лица (Субъективность)** (5): `jeg tror`, `jeg mener`, `etter min mening`, `vi mener`, `jeg er overbevist`
- **окончания** (10): `∅`, `s`, `en`, `ens`, `et`, `ets`, `e`, `es`, `isk`, `iske`
- **служебные слова для определения языка** (25): og, i, at, det, som, en, på, er, av, for, med, til, den, ikke, har, de, om, et, var, fra, også, etter, kan, seg, ble
- **месяцы (для ключей-дат)**: januar, februar, mars, april, mai, juni, juli, august, september, oktober, november, desember

### is — исландский

- **сильные негативные (вес 2)** (24): `refsiaðgerð`, `viðskiptaþving`, `handtek`, `hamfar`, `slys`, `drepin`, `látnir`, `gjaldþrot`, `sakað`, `ákær`, `spilling`, `svik`, `mútur`, `fjárdrátt`, `kúgun`, `einræðisherr`, `einræði`, `hryðjuverk`, `stríðsglæp`, `samsek`, `fjölþátta árás`, `hernám`, `leppríki`, `leppstjórn`
- **негативные (вес 1)** (36): `seink`, `gagnrýn`, `vandamál`, `skortur`, `áhætt`, `deil`, `málsókn`, `dómstól`, `neita`, `bilun`, `viðkvæm`, `aflýs`, `eyðilag`, `skotin niður`, `árás`, `tjón`, `ógn`, `ögrun`, `brot á`, `stigmögn`, `bann`, `takmörk`, `lokun landamær`, `vísað úr landi`, `brottvís`, `mótmæl`, `fordæm`, `njósn`, `smygl`, `ólögleg`, `þrýsting`, `stjórn lúkasjenkó`, `innrás`, `óstöðug`, `upplýsingaóreið`, `falsfrétt`
- **сильные позитивные (вес 2)** (3): `tímamót`, `afnám takmarkana`, `afnám refsiaðgerða`
- **позитивные (вес 1)** (16): `samning`, `pöntun`, `vöxt`, `aukning`, `stækkun`, `árangur`, `nútímavæð`, `afhending`, `samvinn`, `samstarf`, `viðræð`, `lausn úr haldi`, `látinn laus`, `náðun`, `samkomulag`, `mannúðaraðstoð`
- **оценочные слова (Субъективность)** (10): `sjokker`, `hneyksl`, `skammarleg`, `hörmung`, `auðmýkj`, `frábær`, `ótrúleg`, `fáránleg`, `kaldhæðn`, `skelfileg`
- **речь от первого лица (Субъективность)** (4): `ég held`, `að mínu mati`, `ég tel`, `við teljum`
- **окончания** (14): `∅`, `s`, `i`, `a`, `u`, `ur`, `ar`, `ir`, `um`, `nna`, `num`, `inn`, `ið`, `ins`
- **служебные слова для определения языка** (22): og, í, að, á, er, sem, um, til, við, með, ekki, það, var, fyrir, hann, hún, af, eru, frá, þess, einnig, eftir
- **месяцы (для ключей-дат)**: janúar, febrúar, mars, apríl, maí, júní, júlí, ágúst, september, október, nóvember, desember

### fi — финский

- **сильные негативные (вес 2)** (23): `pakote`, `pidätet`, `pidätys`, `katastrofi`, `onnettomuus`, `kuoli`, `kuollut`, `konkurssi`, `syyte`, `syytt`, `korruptio`, `petos`, `lahjus`, `kavallu`, `sorto`, `diktaattori`, `diktatuuri`, `terrori`, `sotarikos`, `rikoskumppani`, `hybridihyökkäy`, `miehity`, `nukkehallit`
- **негативные (вес 1)** (48): `viivästy`, `kritiik`, `ongelm`, `pula`, `puute`, `riski`, `kiista`, `oikeudenkäyn`, `tuomioistuin`, `kieltäyty`, `häiriö`, `haavoittuv`, `peruttu`, `tuhottu`, `tuhosi`, `ammuttiin alas`, `isku`, `hyökkä`, `menetys`, `tappio`, `uhka`, `uhkaa`, `provokaatio`, `rikkomu`, `loukkau`, `eskaloi`, `kielto`, `kielsi`, `rajoitu`, `rajan sulke`, `sulki rajan`, `karkot`, `protesti`, `mielenosoitu`, `tuomitsi`, `tuomitse`, `vakoil`, `salakuljet`, `laiton`, `laittom`, `painost`, `lukašenkan hallin`, `lukashenkan hallin`, `invaasio`, `horjutta`, `disinformaatio`, `maahanmuuttokriisi`, `välineellist`
- **сильные позитивные (вес 2)** (6): `läpimurto`, `ennätys`, `rajoitusten poist`, `pakotteiden poist`, `pakotteet poistet`, `miljardin investoin`
- **позитивные (вес 1)** (23): `sopimus`, `sopimuk`, `tilaus`, `käynnisty`, `kasvu`, `kasvoi`, `lisäys`, `laajennu`, `menesty`, `onnistu`, `modernisoi`, `toimitu`, `yhteistyö`, `kumppanuu`, `vuoropuhel`, `dialogi`, `normalisoi`, `vapautt`, `vapautu`, `armahdu`, `armahti`, `humanitaarinen apu`, `jännitteiden lieven`
- **оценочные слова (Субъективность)** (13): `järkyttäv`, `skandaali`, `häpeällis`, `katastrofaali`, `nöyryyttäv`, `loistav`, `uskomato`, `absurdi`, `kyynis`, `kyyninen`, `hirviömäi`, `hysteeri`, `törkeä`
- **речь от первого лица (Субъективность)** (5): `mielestäni`, `uskon`, `minusta`, `katsomme`, `olen vakuuttunut`
- **окончания** (29): `∅`, `n`, `a`, `ä`, `an`, `än`, `ssa`, `ssä`, `sta`, `stä`, `lla`, `llä`, `lta`, `ltä`, `lle`, `ksi`, `ta`, `tä`, `ja`, `jä`, `in`, `en`, `iin`, `:n`, `:ssa`, `:lle`, `:ta`, `:sta`, `:n`
- **служебные слова для определения языка** (19): ja, on, ei, se, että, oli, mutta, myös, kun, joka, sekä, mukaan, ovat, olla, tai, kanssa, jälkeen, hän, nyt
- **месяцы (для ключей-дат)**: tammikuu, helmikuu, maaliskuu, huhtikuu, toukokuu, kesäkuu, heinäkuu, elokuu, syyskuu, lokakuu, marraskuu, joulukuu

### et — эстонский

- **сильные негативные (вес 2)** (23): `sanktsioon`, `vahistat`, `arreteeri`, `katastroof`, `õnnetus`, `hukkus`, `tapeti`, `pankrot`, `süüdist`, `korruptsioon`, `pettus`, `altkäemaks`, `omastami`, `repressioon`, `diktaator`, `diktatuur`, `terror`, `sõjakuri`, `kaasosal`, `hübriidrünnak`, `agressioon`, `okupatsioon`, `marionett`
- **негативные (вес 1)** (39): `viivit`, `kriitik`, `probleem`, `puudu`, `risk`, `vaidlu`, `kohtuasi`, `kohus`, `keeldu`, `rike`, `haavatav`, `tühista`, `hävita`, `alla tulistat`, `rünna`, `kaotus`, `kahju`, `oht`, `ähvard`, `provokatsioon`, `rikkum`, `eskaleer`, `piirang`, `piiri sulge`, `sulges piiri`, `välja saade`, `protest`, `hukka mõist`, `spioon`, `salakaub`, `ebaseaduslik`, `surve`, `lukašenka režiim`, `lukašenko režiim`, `invasioon`, `destabilise`, `desinformatsioon`, `rändekriis`, `migratsioonikriis`
- **сильные позитивные (вес 2)** (5): `läbimurre`, `rekord`, `piirangute kaotami`, `sanktsioonide kaotami`, `miljardiline investeering`
- **позитивные (вес 1)** (19): `leping`, `tellimus`, `käivita`, `kasv`, `suurene`, `laiene`, `edukas`, `edukal`, `moderniseeri`, `tarne`, `koostöö`, `partnerlus`, `dialoog`, `normaliseeri`, `vabastami`, `vabastati`, `kokkulepe`, `humanitaarabi`, `pingete maandami`
- **оценочные слова (Субъективность)** (11): `šokeeriv`, `skandaalne`, `häbiväärne`, `katastroofiline`, `alandav`, `hiilgav`, `uskumatu`, `absurdne`, `küüniline`, `koletu`, `hüsteeri`
- **речь от первого лица (Субъективность)** (5): `minu arvates`, `ma arvan`, `ma usun`, `me leiame`, `olen veendunud`
- **окончания** (18): `∅`, `a`, `i`, `e`, `u`, `s`, `st`, `le`, `lt`, `l`, `ga`, `ks`, `ni`, `ta`, `d`, `de`, `id`, `sse`
- **служебные слова для определения языка** (20): ja, on, ei, et, see, oli, kui, ka, mis, aga, ning, nagu, või, kes, veel, pärast, tema, seda, selle, kõik
- **месяцы (для ключей-дат)**: jaanuar, veebruar, märts, aprill, mai, juuni, juuli, august, september, oktoober, november, detsember

### hu — венгерский

- **сильные негативные (вес 2)** (25): `szankci`, `letartóztat`, `őrizetbe`, `katasztróf`, `baleset`, `meghalt`, `megölt`, `csőd`, `vádol`, `vádat`, `korrupci`, `csalás`, `megveszteget`, `sikkaszt`, `elnyom`, `diktátor`, `diktatúr`, `terror`, `háborús bűn`, `bűnrészes`, `hibrid támad`, `agresszi`, `megszáll`, `bábállam`, `bábkormány`
- **негативные (вес 1)** (40): `késés`, `késik`, `kritik`, `bírál`, `problém`, `hiány`, `kockázat`, `bíróság`, `elutasít`, `meghibásod`, `sebezhet`, `megsemmisít`, `lelőtt`, `csapás`, `támadás`, `veszteség`, `fenyeget`, `provokáci`, `megsért`, `eszkalál`, `tilalom`, `betilt`, `korlátoz`, `határzár`, `lezárta a határ`, `kiutasít`, `tiltakoz`, `elítél`, `kémked`, `kémek`, `csempész`, `illegális`, `törvénytelen`, `nyomás`, `lukasenka-rezsim`, `lukasenko-rezsim`, `invázi`, `destabiliz`, `dezinformáci`, `migrációs válság`
- **сильные позитивные (вес 2)** (5): `áttörés`, `rekord`, `korlátozások feloldás`, `szankciók feloldás`, `milliárdos beruházás`
- **позитивные (вес 1)** (20): `szerződés`, `megrendel`, `elindít`, `növeked`, `bővít`, `siker`, `korszerűsít`, `moderniz`, `szállítás`, `együttműköd`, `partnerség`, `párbeszéd`, `normaliz`, `szabadon enged`, `szabadul`, `kegyelm`, `megállapodás`, `humanitárius segély`, `deeszkal`, `enyhülés`
- **оценочные слова (Субъективность)** (12): `sokkol`, `botrány`, `szégyen`, `katasztrofális`, `megalázó`, `ragyogó`, `hihetetlen`, `abszurd`, `cinikus`, `szörnyű`, `hisztéri`, `felháborító`
- **речь от первого лица (Субъективность)** (5): `szerintem`, `véleményem szerint`, `úgy gondolom`, `úgy véljük`, `meggyőződésem`
- **окончания** (41): `∅`, `t`, `ot`, `et`, `öt`, `at`, `nak`, `nek`, `ban`, `ben`, `ba`, `be`, `ból`, `ből`, `ra`, `re`, `ról`, `ről`, `val`, `vel`, `hoz`, `hez`, `höz`, `ért`, `i`, `n`, `on`, `en`, `ön`, `ként`, `-t`, `-nak`, `-nek`, `-ban`, `-ben`, `-ra`, `-re`, `-val`, `-vel`, `-hoz`, `-hez`
- **служебные слова для определения языка** (20): a, az, és, hogy, nem, is, egy, van, volt, meg, de, már, ezt, azt, mint, csak, után, szerint, pedig, lesz
- **месяцы (для ключей-дат)**: január, február, március, április, május, június, július, augusztus, szeptember, október, november, december

### cs — чешский

- **сильные негативные (вес 2)** (25): `sankc`, `zatčen`, `zadržen`, `katastrof`, `nehod`, `zabit`, `zemřel`, `bankrot`, `obvin`, `obžalo`, `korupc`, `podvod`, `úplat`, `zpronever`, `represe`, `diktátor`, `diktatur`, `teror`, `válečn zločin`, `spoluvin`, `spolupachatel`, `hybridní útok`, `agrese`, `okupac`, `loutkov`
- **негативные (вес 1)** (43): `zpožd`, `kritik`, `problém`, `nedostat`, `riziko`, `rizik`, `spor`, `žalob`, `soud`, `odmít`, `porucha`, `zranitel`, `zruš`, `zničen`, `sestřel`, `úder`, `útok`, `ztrát`, `hrozb`, `výhrůž`, `provokac`, `porušen`, `eskalac`, `zákaz`, `omezen`, `uzavřen hranic`, `uzavřel hranic`, `vyhoš`, `vypověz`, `protest`, `odsoud`, `špion`, `pašerák`, `pašov`, `nelegáln`, `nezákon`, `nátlak`, `lukašenkův režim`, `lukašenkova režim`, `invaz`, `destabiliz`, `dezinformac`, `migrační kriz`
- **сильные позитивные (вес 2)** (5): `průlom`, `rekord`, `zrušení omezení`, `zrušení sankcí`, `miliardov investic`
- **позитивные (вес 1)** (23): `kontrakt`, `smlouv`, `zakázk`, `objednáv`, `spuštěn`, `spustil`, `růst`, `zvýšen`, `rozšířen`, `úspěch`, `úspěšn`, `moderniz`, `dodávk`, `spoluprác`, `partnerstv`, `dialog`, `normalizac`, `propuštěn`, `propustil`, `milost`, `dohod`, `humanitární pomoc`, `deeskalac`
- **оценочные слова (Субъективность)** (12): `šokující`, `skandáln`, `hanebn`, `katastrofáln`, `ponižující`, `skvěl`, `neuvěřiteln`, `absurdn`, `cynick`, `zrůdn`, `hysteri`, `pobuřující`
- **речь от первого лица (Субъективность)** (5): `myslím si`, `podle mého názoru`, `domnívám se`, `jsme přesvědčeni`, `jsem přesvědčen`
- **окончания** (28): `∅`, `a`, `e`, `ě`, `i`, `o`, `u`, `y`, `ou`, `em`, `ům`, `ech`, `ách`, `ami`, `ý`, `á`, `é`, `ého`, `ému`, `ým`, `ých`, `ými`, `ská`, `ský`, `ské`, `ska`, `sku`, `sko`
- **служебные слова для определения языка** (24): a, v, na, se, je, že, s, z, do, o, to, by, k, ve, jako, pro, ale, jsou, podle, také, po, který, která, bylo
- **месяцы (для ключей-дат)**: led, únor, břez, dub, květ, červn, červenc, srp, září, říj, listopad, prosin

### sk — словацкий

- **сильные негативные (вес 2)** (25): `sankci`, `zatknut`, `zadržan`, `katastrof`, `nehod`, `zabit`, `zomrel`, `bankrot`, `obvin`, `obžalo`, `korupci`, `podvod`, `úplat`, `spreneverovan`, `represi`, `diktátor`, `diktatúr`, `teror`, `vojnov zločin`, `spoluvin`, `spolupáchateľ`, `hybridný útok`, `agresi`, `okupáci`, `bábkov`
- **негативные (вес 1)** (41): `oneskor`, `kritik`, `problém`, `nedostat`, `riziko`, `rizik`, `spor`, `žalob`, `súd`, `odmiet`, `porucha`, `zraniteľ`, `zruš`, `zničen`, `zostrel`, `úder`, `útok`, `strat`, `hrozb`, `vyhráž`, `provokáci`, `porušen`, `eskaláci`, `zákaz`, `obmedzen`, `uzavretie hraníc`, `uzavrel hranic`, `vyhost`, `protest`, `odsúd`, `špión`, `pašerák`, `pašovan`, `nelegáln`, `nezákon`, `nátlak`, `lukašenkov režim`, `invázi`, `destabiliz`, `dezinformáci`, `migračn kríz`
- **сильные позитивные (вес 2)** (5): `prielom`, `rekord`, `zrušenie obmedzení`, `zrušenie sankcií`, `miliardov investíci`
- **позитивные (вес 1)** (23): `kontrakt`, `zmluv`, `zákazk`, `objednávk`, `spusten`, `spustil`, `rast`, `zvýšen`, `rozšíren`, `úspech`, `úspešn`, `moderniz`, `dodávk`, `spoluprác`, `partnerstv`, `dialóg`, `normalizáci`, `prepusten`, `prepustil`, `milosť`, `dohod`, `humanitárn pomoc`, `deeskaláci`
- **оценочные слова (Субъективность)** (11): `šokujúc`, `škandáln`, `hanebn`, `katastrofáln`, `ponižujúc`, `skvel`, `neuveriteľn`, `absurdn`, `cynick`, `hystéri`, `pobuřujúc`
- **речь от первого лица (Субъективность)** (5): `myslím si`, `podľa môjho názoru`, `domnievam sa`, `sme presvedčení`, `som presvedčený`
- **окончания** (27): `∅`, `a`, `e`, `i`, `o`, `u`, `y`, `ou`, `om`, `ov`, `och`, `ách`, `ami`, `ý`, `á`, `é`, `ého`, `ému`, `ým`, `ých`, `ými`, `ská`, `ský`, `ské`, `sko`, `ska`, `sku`
- **служебные слова для определения языка** (24): a, v, na, sa, je, že, s, z, do, o, to, by, k, vo, ako, pre, ale, sú, podľa, tiež, po, ktorý, ktorá, bolo
- **месяцы (для ключей-дат)**: január, február, marc, apríl, máj, jún, júl, august, septemb, októb, novemb, decemb

### sl — словенский

- **сильные негативные (вес 2)** (23): `sankcij`, `aretir`, `priprt`, `katastrof`, `nesreč`, `ubit`, `umrl`, `stečaj`, `obtož`, `korupcij`, `goljufij`, `podkupnin`, `poneverb`, `represij`, `diktator`, `diktatur`, `teror`, `vojn zločin`, `sokrivd`, `hibridn napad`, `agresij`, `okupacij`, `marionet`
- **негативные (вес 1)** (36): `zamud`, `kritik`, `problem`, `pomanjkan`, `tvegan`, `tožb`, `sodišč`, `zavrn`, `okvar`, `ranljiv`, `odpoved`, `uničen`, `sestrel`, `napad`, `izgub`, `grožnj`, `provokacij`, `kršitev`, `eskalacij`, `prepoved`, `omejitev`, `zaprtje mej`, `zaprl mej`, `izgon`, `izgnal`, `protest`, `obsod`, `vohun`, `tihotapl`, `nezakonit`, `pritisk`, `lukašenkov režim`, `invazij`, `destabiliz`, `dezinformacij`, `migrantsk kriz`
- **сильные позитивные (вес 2)** (5): `preboj`, `rekord`, `odprava omejitev`, `odprava sankcij`, `milijardn naložb`
- **позитивные (вес 1)** (20): `pogodb`, `naročil`, `zagon`, `rast`, `povečan`, `razširit`, `uspeh`, `uspešn`, `moderniz`, `dobav`, `sodelovanj`, `partnerstv`, `dialog`, `normalizacij`, `izpust`, `pomilost`, `dogovor`, `sporazum`, `humanitarn pomoč`, `deeskalacij`
- **оценочные слова (Субъективность)** (11): `šokantn`, `škandalozn`, `sramotn`, `katastrofaln`, `ponižujoč`, `briljantn`, `neverjetn`, `absurdn`, `ciničn`, `pošastn`, `histeri`
- **речь от первого лица (Субъективность)** (5): `mislim, da`, `po mojem mnenju`, `menim, da`, `menimo, da`, `prepričan sem`
- **окончания** (28): `∅`, `a`, `e`, `i`, `o`, `u`, `om`, `em`, `ima`, `ama`, `ih`, `im`, `og`, `oj`, `ov`, `ova`, `ove`, `ovi`, `ski`, `ska`, `sko`, `ske`, `ijo`, `ije`, `iji`, `ija`, `ške`, `ški`
- **служебные слова для определения языка** (22): in, je, v, na, da, se, z, za, so, pa, ki, tudi, po, kot, ne, bo, bi, iz, pri, ali, še, do
- **месяцы (для ключей-дат)**: januar, februar, marc, april, maj, junij, julij, avgust, septemb, oktob, novemb, decemb

### hr — хорватский

- **сильные негативные (вес 2)** (24): `sankcij`, `uhićen`, `uhapšen`, `katastrof`, `nesreć`, `ubijen`, `poginu`, `stečaj`, `optuž`, `korupcij`, `prijevar`, `mito`, `mita`, `pronevjer`, `represij`, `diktator`, `diktatur`, `teror`, `ratn zločin`, `suučesni`, `hibridn napad`, `agresij`, `okupacij`, `marionet`
- **негативные (вес 1)** (40): `kašnjen`, `kritik`, `problem`, `nedostat`, `nestašic`, `rizik`, `tužb`, `sud`, `odbi`, `kvar`, `ranjiv`, `otkaz`, `uništen`, `oboren`, `udar`, `napad`, `gubit`, `prijetnj`, `prijeti`, `provokacij`, `kršenj`, `eskalacij`, `zabran`, `ograničenj`, `zatvaranje granic`, `zatvorio granic`, `protjer`, `prosvjed`, `osud`, `špijun`, `krijumčar`, `nezakonit`, `ilegaln`, `pritisak`, `pritisk`, `lukašenkov režim`, `invazij`, `destabiliz`, `dezinformacij`, `migrantsk kriz`
- **сильные позитивные (вес 2)** (5): `proboj`, `rekord`, `ukidanje ograničenja`, `ukidanje sankcija`, `milijardsk investicij`
- **позитивные (вес 1)** (22): `ugovor`, `narudžb`, `pokretanj`, `pokrenu`, `rast`, `povećanj`, `proširenj`, `uspjeh`, `uspješn`, `moderniz`, `isporuk`, `suradnj`, `partnerstv`, `dijalog`, `normalizacij`, `oslobođen`, `oslobodi`, `pomilov`, `sporazum`, `dogovor`, `humanitarn pomoć`, `deeskalacij`
- **оценочные слова (Субъективность)** (11): `šokantn`, `skandalozn`, `sramotn`, `katastrofaln`, `ponižavajuć`, `briljantn`, `nevjerojatn`, `apsurdn`, `ciničn`, `monstruozn`, `histeri`
- **речь от первого лица (Субъективность)** (5): `mislim da`, `po mom mišljenju`, `smatram da`, `smatramo da`, `uvjeren sam`
- **окончания** (27): `∅`, `a`, `e`, `i`, `o`, `u`, `om`, `em`, `ima`, `ama`, `ih`, `im`, `og`, `oj`, `ov`, `ova`, `ove`, `ovi`, `ski`, `ska`, `sko`, `ske`, `ija`, `ije`, `iji`, `iju`, `ijom`
- **служебные слова для определения языка** (23): i, je, u, na, da, se, s, za, su, što, od, koji, kao, ne, će, bi, iz, po, ali, još, do, te, prema
- **месяцы (для ключей-дат)**: siječ, velja, ožuj, trav, svib, lipanj, srpanj, kolovoz, rujan, listopad, studen, prosin

### bs — боснийский

- **сильные негативные (вес 2)** (24): `sankcij`, `uhapšen`, `uhićen`, `katastrof`, `nesreć`, `ubijen`, `poginu`, `stečaj`, `optuž`, `korupcij`, `prevar`, `mito`, `mita`, `pronevjer`, `represij`, `diktator`, `diktatur`, `teror`, `ratn zločin`, `saučesni`, `hibridn napad`, `agresij`, `okupacij`, `marionet`
- **негативные (вес 1)** (40): `kašnjen`, `kritik`, `problem`, `nedostat`, `nestašic`, `rizik`, `tužb`, `sud`, `odbi`, `kvar`, `ranjiv`, `otkaz`, `uništen`, `oboren`, `udar`, `napad`, `gubit`, `prijetnj`, `prijeti`, `provokacij`, `kršenj`, `eskalacij`, `zabran`, `ograničenj`, `zatvaranje granic`, `protjer`, `protest`, `osud`, `špijun`, `krijumčar`, `šverc`, `nezakonit`, `ilegaln`, `pritisak`, `pritisk`, `lukašenkov režim`, `invazij`, `destabiliz`, `dezinformacij`, `migrantsk kriz`
- **сильные позитивные (вес 2)** (5): `proboj`, `rekord`, `ukidanje ograničenja`, `ukidanje sankcija`, `milijardsk investicij`
- **позитивные (вес 1)** (22): `ugovor`, `narudžb`, `pokretanj`, `pokrenu`, `rast`, `povećanj`, `proširenj`, `uspjeh`, `uspješn`, `moderniz`, `isporuk`, `saradnj`, `partnerstv`, `dijalog`, `normalizacij`, `oslobođen`, `oslobodi`, `pomilov`, `sporazum`, `dogovor`, `humanitarn pomoć`, `deeskalacij`
- **оценочные слова (Субъективность)** (11): `šokantn`, `skandalozn`, `sramotn`, `katastrofaln`, `ponižavajuć`, `briljantn`, `nevjerovatn`, `apsurdn`, `ciničn`, `monstruozn`, `histeri`
- **речь от первого лица (Субъективность)** (5): `mislim da`, `po mom mišljenju`, `smatram da`, `smatramo da`, `uvjeren sam`
- **окончания** (27): `∅`, `a`, `e`, `i`, `o`, `u`, `om`, `em`, `ima`, `ama`, `ih`, `im`, `og`, `oj`, `ov`, `ova`, `ove`, `ovi`, `ski`, `ska`, `sko`, `ske`, `ija`, `ije`, `iji`, `iju`, `ijom`
- **служебные слова для определения языка** (23): i, je, u, na, da, se, s, za, su, što, od, koji, kao, ne, će, bi, iz, po, ali, još, do, te, prema
- **месяцы (для ключей-дат)**: januar, februar, mart, april, maj, jun, jul, august, septemb, oktob, novemb, decemb

### sr — сербский (кириллица и латиница)

- **сильные негативные (вес 2)** (46): `sankcij`, `uhapšen`, `katastrof`, `nesreć`, `ubijen`, `poginu`, `stečaj`, `optuž`, `korupcij`, `prevar`, `mito`, `mita`, `pronever`, `represij`, `diktator`, `diktatur`, `teror`, `ratn zločin`, `saučesni`, `hibridn napad`, `agresij`, `okupacij`, `marionet`, `санкциј`, `ухапшен`, `катастроф`, `несрећ`, `убијен`, `погину`, `стечај`, `оптуж`, `корупциј`, `превар`, `мито`, `мита`, `проневер`, `репресиј`, `диктатор`, `диктатур`, `терор`, `ратн злочин`, `саучесни`, `хибридн напад`, `агресиј`, `окупациј`, `марионет`
- **негативные (вес 1)** (80): `kašnjen`, `kritik`, `problem`, `nedostat`, `nestašic`, `rizik`, `tužb`, `sud`, `odbi`, `kvar`, `ranjiv`, `otkaz`, `uništen`, `oboren`, `udar`, `napad`, `gubit`, `pretnj`, `preti`, `provokacij`, `kršenj`, `eskalacij`, `zabran`, `ograničenj`, `zatvaranje granic`, `proter`, `protest`, `osud`, `špijun`, `krijumčar`, `šverc`, `nezakonit`, `ilegaln`, `pritisak`, `pritisk`, `lukašenkov režim`, `invazij`, `destabiliz`, `dezinformacij`, `migrantsk kriz`, `кашњењ`, `критик`, `проблем`, `недостат`, `несташиц`, `ризик`, `тужб`, `суд`, `одби`, `квар`, `рањив`, `отказ`, `уништен`, `оборен`, `удар`, `напад`, `губит`, `претњ`, `прети`, `провокациј`, `кршењ`, `ескалациј`, `забран`, `ограничењ`, `затварање границ`, `протер`, `протест`, `осуд`, `шпијун`, `кријумчар`, `шверц`, `незаконит`, `илегалн`, `притисак`, `притиск`, `лукашенков режим`, `инвазиј`, `дестабилиз`, `дезинформациј`, `мигрантск криз`
- **сильные позитивные (вес 2)** (10): `proboj`, `rekord`, `ukidanje ograničenja`, `ukidanje sankcija`, `milijardsk investicij`, `пробој`, `рекорд`, `укидање ограничења`, `укидање санкција`, `милијардск инвестициј`
- **позитивные (вес 1)** (44): `ugovor`, `porudžbin`, `pokretanj`, `pokrenu`, `rast`, `povećanj`, `proširenj`, `uspeh`, `uspešn`, `moderniz`, `isporuk`, `saradnj`, `partnerstv`, `dijalog`, `normalizacij`, `oslobođen`, `oslobodi`, `pomilov`, `sporazum`, `dogovor`, `humanitarn pomoć`, `deeskalacij`, `уговор`, `поруџбин`, `покретањ`, `покрену`, `раст`, `повећањ`, `проширењ`, `успех`, `успешн`, `модерниз`, `испорук`, `сарадњ`, `партнерств`, `дијалог`, `нормализациј`, `ослобођен`, `ослободи`, `помилов`, `споразум`, `договор`, `хуманитарн помоћ`, `деескалациј`
- **оценочные слова (Субъективность)** (22): `šokantn`, `skandalozn`, `sramotn`, `katastrofaln`, `ponižavajuć`, `briljantn`, `neverovatn`, `apsurdn`, `ciničn`, `monstruozn`, `histeri`, `шокантн`, `скандалозн`, `срамотн`, `катастрофалн`, `понижавајућ`, `бриљантн`, `невероватн`, `апсурдн`, `циничн`, `монструозн`, `хистери`
- **речь от первого лица (Субъективность)** (10): `mislim da`, `po mom mišljenju`, `smatram da`, `smatramo da`, `uveren sam`, `мислим да`, `по мом мишљењу`, `сматрам да`, `сматрамо да`, `уверен сам`
- **окончания** (49): `∅`, `a`, `e`, `i`, `o`, `u`, `om`, `em`, `ima`, `ama`, `ih`, `im`, `og`, `oj`, `ov`, `ova`, `ove`, `ovi`, `ski`, `ska`, `sko`, `ske`, `ija`, `ije`, `iji`, `iju`, `ijom`, `а`, `е`, `и`, `о`, `у`, `ом`, `ем`, `ог`, `ој`, `има`, `ама`, `их`, `им`, `ија`, `ије`, `ији`, `ију`, `ијом`, `ски`, `ска`, `ско`, `ске`
- **служебные слова для определения языка** (43): i, je, u, na, da, se, s, za, su, što, od, koji, kao, ne, će, bi, iz, po, ali, još, do, prema, и, је, у, на, да, се, за, су, што, од, који, као, не, ће, би, из, по, али, још, до, према
- **месяцы (для ключей-дат)**: januar, februar, mart, april, maj, jun, jul, avgust, septemb, oktob, novemb, decemb

### mk — македонский

- **сильные негативные (вес 2)** (23): `санкци`, `уапсен`, `приведен`, `катастроф`, `несреќ`, `убиен`, `загина`, `стечај`, `обвин`, `корупциј`, `измам`, `мито`, `проневер`, `репресиј`, `диктатор`, `диктатур`, `терор`, `воен злостор`, `соучесни`, `хибриден напад`, `агресиј`, `окупациј`, `марионет`
- **негативные (вес 1)** (37): `доцнењ`, `критик`, `проблем`, `недостиг`, `ризик`, `тужб`, `суд`, `одби`, `дефект`, `ранлив`, `откаж`, `уништ`, `соборен`, `удар`, `напад`, `загуб`, `закан`, `провокациј`, `прекрш`, `ескалациј`, `забран`, `ограничув`, `затворање на граница`, `протер`, `протест`, `осуд`, `шпион`, `шверц`, `криумчар`, `нелегал`, `незаконск`, `притисок`, `режимот на лукашенко`, `инвазиј`, `дестабилиз`, `дезинформациј`, `мигрантск криз`
- **сильные позитивные (вес 2)** (5): `пробив`, `рекорд`, `укинување на ограничувањ`, `укинување на санкции`, `милијардск инвестициј`
- **позитивные (вес 1)** (20): `договор`, `нарачк`, `лансирањ`, `раст`, `зголемув`, `проширув`, `успех`, `успешн`, `модерниз`, `испорак`, `соработк`, `партнерств`, `дијалог`, `нормализациј`, `ослободен`, `ослободи`, `помилув`, `спогодб`, `хуманитарн помош`, `деескалациј`
- **оценочные слова (Субъективность)** (11): `шокантн`, `скандалозн`, `срамн`, `катастрофалн`, `понижувачк`, `брилијантн`, `неверојатн`, `апсурдн`, `цинич`, `монструозн`, `хистери`
- **речь от первого лица (Субъективность)** (5): `мислам дека`, `според мене`, `сметам дека`, `сметаме дека`, `убеден сум`
- **окончания** (20): `∅`, `а`, `е`, `и`, `о`, `у`, `от`, `та`, `то`, `те`, `ата`, `ите`, `ски`, `ска`, `ско`, `ските`, `скиот`, `ската`, `ија`, `ии`
- **служебные слова для определения языка** (21): и, е, во, на, да, се, со, за, што, од, кој, како, не, ќе, би, по, но, уште, до, според, тоа
- **месяцы (для ключей-дат)**: јануар, февруар, март, април, мај, јуни, јули, август, септемв, октомв, ноемв, декемв

### bg — болгарский

- **сильные негативные (вес 2)** (22): `санкци`, `арестув`, `задържан`, `катастроф`, `загина`, `убит`, `фалит`, `обвин`, `корупци`, `измам`, `подкуп`, `присвоява`, `репреси`, `диктатор`, `диктатур`, `терор`, `военн престъплен`, `съучастни`, `хибридн атак`, `агреси`, `окупаци`, `марионет`
- **негативные (вес 1)** (39): `забав`, `критик`, `проблем`, `недостиг`, `риск`, `спор`, `съд`, `отказ`, `повред`, `уязвим`, `отмен`, `унищож`, `свален`, `удар`, `атак`, `загуб`, `заплах`, `провокаци`, `нарушен`, `наруши`, `ескалаци`, `забран`, `ограничен`, `затваряне на границ`, `затвори границ`, `експулсир`, `изгон`, `протест`, `осъд`, `шпион`, `контрабанд`, `незаконн`, `нелегалн`, `натиск`, `режимът на лукашенко`, `инвази`, `дестабилиз`, `дезинформаци`, `мигрантск криз`
- **сильные позитивные (вес 2)** (6): `пробив`, `рекорд`, `отмяна на ограничения`, `отмяна на санкции`, `вдигане на санкции`, `милиардн инвестици`
- **позитивные (вес 1)** (19): `договор`, `поръчк`, `стартир`, `ръст`, `увеличен`, `разширен`, `успех`, `успешн`, `модерниз`, `доставк`, `сътрудничеств`, `партньорств`, `диалог`, `нормализаци`, `освобод`, `помилв`, `споразумен`, `хуманитарн помощ`, `деескалаци`
- **оценочные слова (Субъективность)** (11): `шокиращ`, `скандалн`, `позорн`, `катастрофалн`, `унизителн`, `блестящ`, `невероятн`, `абсурдн`, `цинич`, `чудовищн`, `истери`
- **речь от первого лица (Субъективность)** (5): `смятам, че`, `според мен`, `мисля, че`, `смятаме, че`, `убеден съм`
- **окончания** (23): `∅`, `а`, `я`, `е`, `и`, `о`, `у`, `ът`, `та`, `то`, `те`, `ата`, `ите`, `ия`, `ият`, `ски`, `ска`, `ско`, `ските`, `ския`, `ският`, `ската`, `ии`
- **служебные слова для определения языка** (23): и, е, в, на, да, се, с, за, са, че, от, който, като, не, ще, би, по, но, още, до, според, това, във
- **месяцы (для ключей-дат)**: януари, февруари, март, април, май, юни, юли, август, септември, октомври, ноември, декември

### sq — албанский

- **сильные негативные (вес 2)** (23): `sanksion`, `arrestu`, `arrestim`, `katastrof`, `aksident`, `vrarë`, `vdekur`, `falimentim`, `akuz`, `korrupsion`, `mashtrim`, `ryshfet`, `përvetësim`, `represion`, `diktator`, `diktatur`, `terror`, `krim luft`, `bashkëfajtor`, `sulm hibrid`, `agresion`, `pushtim`, `marionet`
- **негативные (вес 1)** (43): `vonesë`, `vones`, `kritik`, `problem`, `mungesë`, `mungesa`, `rrezik`, `mosmarrëveshj`, `padi`, `gjykat`, `refuz`, `defekt`, `cenues`, `anulim`, `anuloi`, `shkatërr`, `rrëzuar`, `goditj`, `sulm`, `humbj`, `kërcënim`, `kërcënoi`, `provokim`, `shkelj`, `përshkallëzim`, `ndalim`, `ndaloi`, `kufizim`, `mbyllja e kufirit`, `dëbim`, `dëboi`, `protest`, `dënoi`, `dënim`, `spiun`, `kontraband`, `paligjshëm`, `presion`, `regjimi i lukashenkos`, `pushtim`, `destabiliz`, `dezinformim`, `kriza e migrant`
- **сильные позитивные (вес 2)** (5): `përparim historik`, `rekord`, `heqja e kufizimeve`, `heqja e sanksioneve`, `miliarda investime`
- **позитивные (вес 1)** (16): `kontrat`, `porosi`, `rritj`, `zgjerim`, `sukses`, `modernizim`, `furnizim`, `bashkëpunim`, `partneritet`, `dialog`, `normalizim`, `lirim`, `liruar`, `marrëveshj`, `ndihmë humanitare`, `uljen e tensionit`
- **оценочные слова (Субъективность)** (11): `tronditës`, `skandaloz`, `turpshëm`, `katastrofik`, `poshtërues`, `shkëlqyer`, `pabesueshëm`, `absurd`, `cinik`, `monstruoz`, `histeri`
- **речь от первого лица (Субъективность)** (5): `mendoj se`, `sipas mendimit tim`, `besoj se`, `konsiderojmë`, `jam i bindur`
- **окончания** (15): `∅`, `a`, `e`, `i`, `u`, `ë`, `ës`, `it`, `in`, `ia`, `isë`, `inë`, `ve`, `të`, `s`
- **служебные слова для определения языка** (21): dhe, të, në, e, i, për, me, që, nga, një, është, së, se, u, nuk, ka, por, edhe, si, më, sipas
- **месяцы (для ключей-дат)**: janar, shkurt, mars, prill, maj, qershor, korrik, gusht, shtator, tetor, nëntor, dhjetor

### el — греческий

- **сильные негативные (вес 2)** (26): `κυρώσ`, `κυρωσ`, `συνελήφθ`, `σύλληψ`, `καταστροφ`, `δυστύχημ`, `σκοτώθ`, `νεκρ`, `πτώχευσ`, `κατηγορ`, `διαφθορ`, `απάτη`, `απάτες`, `δωροδοκ`, `υπεξαίρεσ`, `καταστολ`, `δικτάτορ`, `δικτατορ`, `τρομοκρατ`, `εγκλήματα πολέμου`, `έγκλημα πολέμου`, `συνενοχ`, `υβριδική επίθεσ`, `επιθετικότητ`, `κατοχ`, `μαριονέτ`
- **негативные (вес 1)** (47): `καθυστέρ`, `κριτικ`, `πρόβλημ`, `ελλείψ`, `έλλειψ`, `κίνδυν`, `διαφωνί`, `αγωγ`, `δικαστήρι`, `αρνήθ`, `άρνησ`, `βλάβ`, `ευάλωτ`, `ακύρωσ`, `ακυρώθ`, `κατέστρεψ`, `καταρρίφθ`, `πλήγμ`, `επίθεσ`, `επιθέσ`, `απώλει`, `απειλ`, `πρόκλησ`, `προκλήσ`, `παραβίασ`, `κλιμάκωσ`, `απαγόρευσ`, `απαγορ`, `περιορισμ`, `κλείσιμο των συνόρων`, `έκλεισε τα σύνορα`, `απέλασ`, `διαμαρτυρ`, `καταδίκ`, `κατασκοπ`, `κατάσκοπ`, `λαθρεμπόρ`, `λαθραί`, `παράνομ`, `πίεσ`, `πιέσ`, `καθεστώς λουκασένκο`, `καθεστώς του λουκασένκο`, `εισβολ`, `αποσταθεροποί`, `παραπληροφόρησ`, `μεταναστευτική κρίσ`
- **сильные позитивные (вес 2)** (5): `επίτευγμα`, `ρεκόρ`, `άρση των περιορισμών`, `άρση των κυρώσεων`, `επενδύσεις δισεκατομμυρίων`
- **позитивные (вес 1)** (17): `σύμβασ`, `συμβόλαι`, `παραγγελί`, `αύξησ`, `ανάπτυξ`, `επέκτασ`, `επιτυχ`, `εκσυγχρονισμ`, `παράδοσ`, `συνεργασί`, `διάλογ`, `ομαλοποίησ`, `απελευθέρωσ`, `αποφυλάκισ`, `συμφωνί`, `ανθρωπιστική βοήθει`, `αποκλιμάκωσ`
- **оценочные слова (Субъективность)** (11): `σοκαριστικ`, `σκανδαλώδ`, `επαίσχυντ`, `καταστροφικ`, `ταπεινωτικ`, `απίστευτ`, `παράλογ`, `κυνικ`, `τερατώδ`, `υστερί`, `εξοργιστικ`
- **речь от первого лица (Субъективность)** (5): `πιστεύω ότι`, `κατά τη γνώμη μου`, `θεωρώ ότι`, `θεωρούμε`, `είμαι πεπεισμένος`
- **окончания** (22): `∅`, `α`, `ας`, `ες`, `η`, `ης`, `ή`, `ής`, `ο`, `ος`, `ου`, `οι`, `ων`, `ους`, `ό`, `ός`, `ού`, `ά`, `ία`, `ίας`, `ιά`, `ιάς`
- **служебные слова для определения языка** (23): και, το, η, ο, να, του, της, την, τα, με, σε, για, από, που, στο, στη, στην, είναι, οι, των, θα, δεν, ως
- **месяцы (для ключей-дат)**: ιανουαρ, φεβρουαρ, μαρτ, απριλ, μαΐ, ιουν, ιουλ, αυγουστ, σεπτεμβρ, οκτωβρ, νοεμβρ, δεκεμβρ

### tr — турецкий

- **сильные негативные (вес 2)** (22): `yaptırım`, `tutuklan`, `gözaltı`, `felaket`, `kaza`, `öldürül`, `hayatını kaybet`, `iflas`, `suçla`, `yolsuzluk`, `dolandırıcı`, `rüşvet`, `zimmet`, `baskı rejim`, `diktatör`, `terör`, `savaş suç`, `suç ortağ`, `hibrit saldırı`, `saldırganlık`, `işgal`, `kukla`
- **негативные (вес 1)** (40): `gecikme`, `eleştir`, `sorun`, `eksiklik`, `kıtlık`, `risk`, `anlaşmazlık`, `dava`, `mahkeme`, `reddet`, `arıza`, `savunmasız`, `iptal`, `imha`, `düşürül`, `vuruldu`, `darbe`, `saldırı`, `kayıp`, `tehdit`, `provokasyon`, `ihlal`, `tırman`, `yasak`, `kısıtlama`, `sınırı kapat`, `sınır dışı`, `protesto`, `kınadı`, `kınama`, `casus`, `kaçakçı`, `yasadışı`, `yasa dışı`, `baskı`, `lukaşenko rejim`, `istikrarsız`, `dezenformasyon`, `göç kriz`, `araçsallaştır`
- **сильные позитивные (вес 2)** (5): `atılım`, `rekor`, `kısıtlamaların kaldırıl`, `yaptırımların kaldırıl`, `milyar dolarlık yatırım`
- **позитивные (вес 1)** (18): `sözleşme`, `sipariş`, `başlatıl`, `büyüme`, `artış`, `genişleme`, `başarı`, `modernize`, `teslimat`, `işbirliği`, `iş birliği`, `ortaklık`, `diyalog`, `normalleşme`, `serbest bırak`, `anlaşma`, `insani yardım`, `gerilimi azalt`
- **оценочные слова (Субъективность)** (11): `şok edici`, `skandal`, `utanç verici`, `felaket`, `aşağılayıcı`, `inanılmaz`, `absürt`, `saçma`, `kinik`, `korkunç`, `histeri`
- **речь от первого лица (Субъективность)** (5): `bence`, `kanımca`, `düşünüyorum`, `inanıyorum`, `kanaatindeyiz`
- **окончания** (67): `∅`, `a`, `e`, `ı`, `i`, `u`, `ü`, `ya`, `ye`, `yı`, `yi`, `da`, `de`, `ta`, `te`, `dan`, `den`, `tan`, `ten`, `nın`, `nin`, `ın`, `in`, `un`, `ün`, `lı`, `li`, `lar`, `ler`, `'a`, `'e`, `'ı`, `'i`, `'da`, `'de`, `'ta`, `'te`, `'dan`, `'den`, `'tan`, `'ten`, `'nın`, `'nin`, `'ın`, `'in`, `'ya`, `'ye`, `'yı`, `'yi`, `'nun`, `'nün`, `'un`, `'ün`, `’a`, `’e`, `’ı`, `’i`, `’da`, `’de`, `’ın`, `’in`, `’nın`, `’nin`, `’ya`, `’ye`, `’dan`, `’den`
- **служебные слова для определения языка** (19): ve, bir, bu, da, de, ile, için, olarak, gibi, daha, çok, ne, ama, olan, kadar, sonra, göre, en, ise
- **месяцы (для ключей-дат)**: ocak, şubat, mart, nisan, mayıs, haziran, temmuz, ağustos, eylül, ekim, kasım, aralık

### fa — персидский

- **сильные негативные (вес 2)** (27): `تحریم`, `تحريم`, `بازداشت`, `دستگیر`, `دستگير`, `فاجعه`, `کشته`, `كشته`, `جان باخت`, `ورشکست`, `ورشكست`, `فساد`, `کلاهبردار`, `كلاهبردار`, `رشوه`, `اختلاس`, `سرکوب`, `سركوب`, `دیکتاتور`, `ديكتاتور`, `تروریست`, `تروريست`, `جنایت جنگی`, `جنايت جنگي`, `تجاوز`, `اشغال`, `دست نشانده`
- **негативные (вес 1)** (21): `تأخیر`, `تأخير`, `تاخیر`, `تاخير`, `انتقاد`, `مشکل`, `مشكل`, `کمبود`, `كمبود`, `خطر`, `اختلاف`, `دادگاه`, `نقص`, `لغو`, `منهدم`, `سرنگون`, `حمله`, `آسیب`, `آسيب`, `شکست`, `شكست`
- **сильные позитивные (вес 2)** (7): `دستاورد`, `رکورد`, `ركورد`, `رفع تحریم`, `رفع تحريم`, `لغو تحریم`, `لغو تحريم`
- **позитивные (вес 1)** (23): `قرارداد`, `سفارش`, `راه‌اندازی`, `راه‌اندازي`, `راه اندازی`, `راه اندازي`, `رشد`, `افزایش`, `افزايش`, `گسترش`, `موفقیت`, `موفقيت`, `نوسازی`, `نوسازي`, `تحویل`, `تحويل`, `همکاری`, `همكاري`, `مشارکت`, `مشاركت`, `گفتگو`, `گفت‌وگو`, `تفاهم`
- **оценочные слова (Субъективность)** (14): `تکان‌دهنده`, `تكان‌دهنده`, `رسوایی`, `رسوايي`, `شرم‌آور`, `فاجعه‌بار`, `باورنکردنی`, `باورنكردني`, `مضحک`, `مضحك`, `وحشتناک`, `وحشتناك`, `هیستری`, `هيستري`
- **речь от первого лица (Субъективность)** (7): `به نظر من`, `معتقدم`, `فکر می‌کنم`, `فكر مي‌كنم`, `به عقیده من`, `به عقيده من`, `به اعتقاد ما`
- **окончания** (12): `∅`, `ی`, `ها`, `های`, `‌ها`, `‌های`, `ای`, `‌ای`, `ان`, `یان`, `ي`, `هاي`
- **служебные слова для определения языка** (27): و, در, به, از, که, كه, این, اين, را, با, است, برای, براي, آن, یک, يك, تا, می, مي, بر, هم, شد, خود, نیز, نيز, پس, اما
- **месяцы (для ключей-дат)**: ژانویه, فوریه, مارس, آوریل, مه, ژوئن, ژوئیه, اوت, سپتامبر, اکتبر, نوامبر, دسامبر

## Страна источника

Страна — страна издателя по карточке источника; каждая страна — отдельная строка (iid100-2, GREEN t153s804). Явный список ниже (в т. ч. все ленты группы «Европа и НАТО» — страна из каталога vsesmi.online и проверки сайта); иначе домен верхнего уровня (национальные домены стран Европы и ряда других стран — список tld); иначе «Прочие страны» с пометкой «страна не установлена» (в т. ч. каналы Telegram без установленной страны). Источники группы «наши официальные ресурсы РБ» — Беларусь. Источники из Беларуси в ИИД не входят. Источники группы «только для расчёта» (решение GREEN t153s804) учитываются по серверной карточке и в публичных файлах не называются.

| Источник | Страна |
|---|---|
| `derstandard.at` | Австрия |
| `diepresse.com` | Австрия |
| `kleinezeitung.at` | Австрия |
| `krone.at` | Австрия |
| `kurier.at` | Австрия |
| `meinbezirk.at` | Австрия |
| `nachrichten.at` | Австрия |
| `orf.at` | Австрия |
| `tt.com` | Австрия |
| `albeu.com` | Албания |
| `balkanweb.com` | Албания |
| `kohajone.com` | Албания |
| `bondia.ad` | Андорра |
| `diariandorra.ad` | Андорра |
| `elperiodic.ad` | Андорра |
| `zona-militar.com` | Аргентина |
| `belta.by` | Беларусь |
| `belta.by-bpla` | Беларусь |
| `belvpo.com` | Беларусь |
| `gp.by` | Беларусь |
| `grodnonews.by` | Беларусь |
| `mil.by` | Беларусь |
| `sb.by-bpla` | Беларусь |
| `tg:Drones_Belarus` | Беларусь |
| `tg:belta_telegramm` | Беларусь |
| `tg:gpkgovby` | Беларусь |
| `tg:modmilby` | Беларусь |
| `tg:newsby_btrc` | Беларусь |
| `tg:otvinta_by` | Беларусь |
| `tg:pul_1` | Беларусь |
| `tg:sbbytoday_by` | Беларусь |
| `tg:vpk_gov_by` | Беларусь |
| `tg:vpkgovby` | Беларусь |
| `times.by` | Беларусь |
| `vpk.gov.by` | Беларусь |
| `7sur7.be` | Бельгия |
| `armyrecognition.com-aerospace` | Бельгия |
| `armyrecognition.com-army` | Бельгия |
| `demorgen.be` | Бельгия |
| `dhnet.be` | Бельгия |
| `gva.be` | Бельгия |
| `hbvl.be` | Бельгия |
| `knack.be` | Бельгия |
| `lalibre.be` | Бельгия |
| `nieuwsblad.be` | Бельгия |
| `standaard.be` | Бельгия |
| `dir.bg` | Болгария |
| `dnevnik.bg` | Болгария |
| `fakti.bg` | Болгария |
| `nova.bg` | Болгария |
| `offnews.bg` | Болгария |
| `plovdiv24.bg` | Болгария |
| `vesti.bg` | Болгария |
| `6yka.com` | Босния и Герцеговина |
| `avaz.ba` | Босния и Герцеговина |
| `nezavisne.com` | Босния и Герцеговина |
| `oslobodjenje.ba` | Босния и Герцеговина |
| `vaticannews.va` | Ватикан |
| `zenit.org` | Ватикан |
| `airforce-technology.com` | Великобритания |
| `army-technology.com` | Великобритания |
| `bbc-world` | Великобритания |
| `belfastlive.co.uk` | Великобритания |
| `belfastmedia.com` | Великобритания |
| `belfasttelegraph.co.uk` | Великобритания |
| `birminghammail.co.uk` | Великобритания |
| `businessnewswales.com` | Великобритания |
| `caerphillyobserver.co.uk` | Великобритания |
| `cambrian-news.co.uk` | Великобритания |
| `channel4.com` | Великобритания |
| `chroniclelive.co.uk` | Великобритания |
| `dailymail.co.uk` | Великобритания |
| `dailypost.co.uk` | Великобритания |
| `dailyrecord.co.uk` | Великобритания |
| `derryjournal.com` | Великобритания |
| `derrynow.com` | Великобритания |
| `edinburghnews.scotsman.com` | Великобритания |
| `falkirkherald.co.uk` | Великобритания |
| `ft.com` | Великобритания |
| `gbnews.com` | Великобритания |
| `glasgowlive.co.uk` | Великобритания |
| `glasgowworld.com` | Великобритания |
| `golwg.360.cymru` | Великобритания |
| `gov.uk` | Великобритания |
| `gov.uk-dstl` | Великобритания |
| `gov.uk-mod-drone` | Великобритания |
| `herald.wales` | Великобритания |
| `inews.co.uk` | Великобритания |
| `irishnews.com` | Великобритания |
| `liverpoolecho.co.uk` | Великобритания |
| `manchestereveningnews.co.uk` | Великобритания |
| `metro.co.uk` | Великобритания |
| `mirror.co.uk` | Великобритания |
| `nation.cymru` | Великобритания |
| `news.stv.tv` | Великобритания |
| `newsletter.co.uk` | Великобритания |
| `newstatesman.com` | Великобритания |
| `scotsman.com` | Великобритания |
| `scottishdailyexpress.co.uk` | Великобритания |
| `shetlandtimes.co.uk` | Великобритания |
| `sluggerotoole.com` | Великобритания |
| `standard.co.uk` | Великобритания |
| `telegraph.co.uk` | Великобритания |
| `thedetail.tv` | Великобритания |
| `theferret.scot` | Великобритания |
| `theguardian.com` | Великобритания |
| `unmannedairspace.info` | Великобритания |
| `walesonline.co.uk` | Великобритания |
| `yorkshirepost.co.uk` | Великобритания |
| `24.hu` | Венгрия |
| `444.hu` | Венгрия |
| `blikk.hu` | Венгрия |
| `hvg.hu` | Венгрия |
| `index.hu` | Венгрия |
| `magyarnemzet.hu` | Венгрия |
| `napi.hu` | Венгрия |
| `portfolio.hu` | Венгрия |
| `augengeradeaus.net` | Германия |
| `bundesregierung.de` | Германия |
| `derwesten.de` | Германия |
| `dw.com-bpla` | Германия |
| `esut.de` | Германия |
| `euro-sd.com` | Германия |
| `faz.net` | Германия |
| `hartpunkt.de` | Германия |
| `soldat-und-technik.de` | Германия |
| `spiegel.de` | Германия |
| `chronicle.gi` | Гибралтар (Великобритания) |
| `dikaiologitika.gr` | Греция |
| `gazzetta.gr` | Греция |
| `iefimerida.gr` | Греция |
| `newsbomb.gr` | Греция |
| `newsit.gr` | Греция |
| `pentapostagma.gr` | Греция |
| `protothema.gr` | Греция |
| `ptisidiastima.com` | Греция |
| `zougla.gr` | Греция |
| `information.dk` | Дания |
| `jyllands-posten.dk` | Дания |
| `lokalavisen.dk` | Дания |
| `nordjyske.dk` | Дания |
| `eda.europa.eu` | Европейский союз (органы ЕС) |
| `israeldefense.co.il` | Израиль |
| `independent.ie` | Ирландия |
| `irishcentral.com` | Ирландия |
| `irishexaminer.com` | Ирландия |
| `irishmirror.ie` | Ирландия |
| `thejournal.ie` | Ирландия |
| `dv.is` | Исландия |
| `lhg.is` | Исландия |
| `mbl.is` | Исландия |
| `ruv.is` | Исландия |
| `vb.is` | Исландия |
| `visir.is` | Исландия |
| `20minutos.es` | Испания |
| `abc.es` | Испания |
| `defensa.com` | Испания |
| `elcorreo.com` | Испания |
| `elmundo.es` | Испания |
| `expansion.com` | Испания |
| `galaxiamilitar.es` | Испания |
| `lamoncloa.gob.es` | Испания |
| `larazon.es` | Испания |
| `lavanguardia.com` | Испания |
| `libertaddigital.com` | Испания |
| `revistaejercitos.com` | Испания |
| `analisidifesa.it` | Италия |
| `ansa.it` | Италия |
| `governo.it` | Италия |
| `ilfattoquotidiano.it` | Италия |
| `ilmessaggero.it` | Италия |
| `ilsole24ore.com` | Италия |
| `lastampa.it` | Италия |
| `repubblica.it` | Италия |
| `theaviationist.com` | Италия |
| `api.io.canada.ca` | Канада |
| `journaldemontreal.com` | Канада |
| `torontosun.com` | Канада |
| `tvanouvelles.ca` | Канада |
| `aljazeera` | Катар |
| `cyprus-mail.com` | Кипр |
| `cyprusnews.eu` | Кипр |
| `gundemkibris.com` | Кипр |
| `haberkibris.com` | Кипр |
| `sigmalive.com` | Кипр |
| `apollo.lv` | Латвия |
| `delfi.lv` | Латвия |
| `jauns.lv` | Латвия |
| `la.lv` | Латвия |
| `lsm.lv` | Латвия |
| `mixnews.lv` | Латвия |
| `mod.gov.lv` | Латвия |
| `tvnet.lv` | Латвия |
| `krepsinis.net` | Литва |
| `lrytas.lt` | Литва |
| `respublika.lt` | Литва |
| `vz.lt` | Литва |
| `1fl.li` | Лихтенштейн |
| `landesspiegel.li` | Лихтенштейн |
| `lie-zeit.li` | Лихтенштейн |
| `lesfrontaliers.lu` | Люксембург |
| `wort.lu` | Люксембург |
| `maltatoday.com.mt` | Мальта |
| `jurnal.md` | Молдова |
| `noi.md` | Молдова |
| `protv.md` | Молдова |
| `unimedia.info` | Молдова |
| `bellingcat.com` | Нидерланды |
| `dronewatch.eu` | Нидерланды |
| `dvhn.nl` | Нидерланды |
| `nrc.nl` | Нидерланды |
| `nu.nl` | Нидерланды |
| `parool.nl` | Нидерланды |
| `rtlnieuws.nl` | Нидерланды |
| `telegraaf.nl` | Нидерланды |
| `trouw.nl` | Нидерланды |
| `volkskrant.nl` | Нидерланды |
| `adressa.no` | Норвегия |
| `aftenbladet.no` | Норвегия |
| `aftenposten.no` | Норвегия |
| `bt.no` | Норвегия |
| `dagbladet.no` | Норвегия |
| `e24.no` | Норвегия |
| `fvn.no` | Норвегия |
| `nrk.no` | Норвегия |
| `regjeringen.no` | Норвегия |
| `vg.no` | Норвегия |
| `defence24.com` | Польша |
| `defence24.pl` | Польша |
| `dziennik.pl` | Польша |
| `dziennikzachodni.pl` | Польша |
| `dziennikzbrojny.pl` | Польша |
| `gazeta.pl` | Польша |
| `gazetaprawna.pl` | Польша |
| `gazetawroclawska.pl` | Польша |
| `konflikty.pl` | Польша |
| `natemat.pl` | Польша |
| `newsweek.pl` | Польша |
| `niezalezna.pl` | Польша |
| `polityka.pl` | Польша |
| `rp.pl` | Польша |
| `wyborcza.pl` | Польша |
| `zbiam.pl` | Польша |
| `cmjornal.pt` | Португалия |
| `dnoticias.pt` | Португалия |
| `observador.pt` | Португалия |
| `omirante.pt` | Португалия |
| `sabado.pt` | Португалия |
| `sapo.pt` | Португалия |
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
| `eu:ria.ru` | Россия |
| `expouav.ru` | Россия |
| `fssp.gov.ru` | Россия |
| `function.mil.ru` | Россия |
| `impnavigator.ru` | Россия |
| `interfax.ru` | Россия |
| `kad.arbitr.ru` | Россия |
| `kommersant.ru` | Россия |
| `lenta.ru` | Россия |
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
| `adevarul.ro` | Румыния |
| `antena3.ro` | Румыния |
| `b1.ro` | Румыния |
| `dcnews.ro` | Румыния |
| `defenseromania.ro` | Румыния |
| `digi24.ro` | Румыния |
| `gandul.ro` | Румыния |
| `gov.ro` | Румыния |
| `hotnews.ro` | Румыния |
| `libertatea.ro` | Румыния |
| `mediafax.ro` | Румыния |
| `realitatea.net` | Румыния |
| `romaniatv.net` | Румыния |
| `stirileprotv.ro` | Румыния |
| `stiripesurse.ro` | Румыния |
| `zf.ro` | Румыния |
| `af.mil-news` | США |
| `airandspaceforces.com` | США |
| `breakingdefense.com` | США |
| `breakingdefense.com-spheres` | США |
| `c4isrnet.com` | США |
| `c4isrnet.com-battlefield-tech` | США |
| `c4isrnet.com-unmanned` | США |
| `defense.gov` | США |
| `defense.gov-news` | США |
| `defensedaily.com` | США |
| `defensenews.com` | США |
| `defensenews.com-air` | США |
| `defensenews.com-land` | США |
| `defensenews.com-unmanned` | США |
| `defenseone.com` | США |
| `defensescoop.com` | США |
| `dronedj.com` | США |
| `dronelife.com` | США |
| `dronexl.co` | США |
| `foxnews.com` | США |
| `insidegnss.com` | США |
| `latimes.com` | США |
| `militarytimes.com` | США |
| `news.usni.org` | США |
| `newyorker.com` | США |
| `nypost.com` | США |
| `nytimes.com` | США |
| `overtdefense.com` | США |
| `time.com` | США |
| `twz.com` | США |
| `warontherocks.com` | США |
| `a1on.mk` | Северная Македония |
| `kajgana.com` | Северная Македония |
| `kurir.mk` | Северная Македония |
| `press24.mk` | Северная Македония |
| `republika.mk` | Северная Македония |
| `sitel.com.mk` | Северная Македония |
| `time.mk` | Северная Македония |
| `vecer.mk` | Северная Македония |
| `b92.net` | Сербия |
| `blic.rs` | Сербия |
| `danas.rs` | Сербия |
| `espreso.rs` | Сербия |
| `kurir.rs` | Сербия |
| `mod.gov.rs` | Сербия |
| `mondo.rs` | Сербия |
| `naslovi.net` | Сербия |
| `pink.rs` | Сербия |
| `pravda.rs` | Сербия |
| `telegraf.rs` | Сербия |
| `armadnymagazin.sk` | Словакия |
| `dobrenoviny.sk` | Словакия |
| `hnonline.sk` | Словакия |
| `sme.sk` | Словакия |
| `webnoviny.sk` | Словакия |
| `24ur.com` | Словения |
| `delo.si` | Словения |
| `dnevnik.si` | Словения |
| `gov.si` | Словения |
| `pozareport.si` | Словения |
| `siol.net` | Словения |
| `vecer.com` | Словения |
| `zurnal24.si` | Словения |
| `aa.com.tr` | Турция |
| `ahaber.com.tr` | Турция |
| `cumhuriyet.com.tr` | Турция |
| `defenceturk.net` | Турция |
| `haber7.com` | Турция |
| `haberturk.com` | Турция |
| `onedio.com` | Турция |
| `sabah.com.tr` | Турция |
| `savunmasanayist.com` | Турция |
| `sozcu.com.tr` | Турция |
| `yenisafak.com` | Турция |
| `armyinform.com.ua` | Украина |
| `bihus.info` | Украина |
| `brave1.gov.ua` | Украина |
| `defence-ua.com` | Украина |
| `delo.ua` | Украина |
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
| `iltalehti.fi` | Финляндия |
| `20minutes.fr` | Франция |
| `actu.fr` | Франция |
| `cnews.fr` | Франция |
| `defense.gouv.fr-aid` | Франция |
| `euronews-drones` | Франция |
| `forcesoperations.com` | Франция |
| `france24.com` | Франция |
| `humanite.fr` | Франция |
| `ladepeche.fr` | Франция |
| `ledauphine.com` | Франция |
| `lemonde.fr` | Франция |
| `opex360.com` | Франция |
| `rfi.fr` | Франция |
| `sudouest.fr` | Франция |
| `tf1info.fr` | Франция |
| `24sata.hr` | Хорватия |
| `dnevnik.hr` | Хорватия |
| `dnevno.hr` | Хорватия |
| `glasistre.hr` | Хорватия |
| `hr.n1info.com` | Хорватия |
| `index.hr` | Хорватия |
| `jutarnji.hr` | Хорватия |
| `morh.hr` | Хорватия |
| `net.hr` | Хорватия |
| `novilist.hr` | Хорватия |
| `poslovni.hr` | Хорватия |
| `rtl.hr` | Хорватия |
| `slobodnadalmacija.hr` | Хорватия |
| `telegram.hr` | Хорватия |
| `tportal.hr` | Хорватия |
| `vecernji.hr` | Хорватия |
| `pobjeda.me` | Черногория |
| `portalanalitika.me` | Черногория |
| `vijesti.me` | Черногория |
| `aktualne.cz` | Чехия |
| `denik.cz` | Чехия |
| `echo24.cz` | Чехия |
| `ihned.cz` | Чехия |
| `mo.gov.cz` | Чехия |
| `reflex.cz` | Чехия |
| `sport.cz` | Чехия |
| `tyden.cz` | Чехия |
| `blick.ch` | Швейцария |
| `letemps.ch` | Швейцария |
| `newsd.admin.ch` | Швейцария |
| `watson.ch` | Швейцария |
| `dn.se` | Швеция |
| `friatider.se` | Швеция |
| `hd.se` | Швеция |
| `nyheter24.se` | Швеция |
| `omni.se` | Швеция |
| `regeringen.se` | Швеция |
| `samnytt.se` | Швеция |
| `svt.se` | Швеция |
| `sydsvenskan.se` | Швеция |
| `thelocal.se` | Швеция |
| `aripaev.ee` | Эстония |
| `kaitseministeerium.ee` | Эстония |
| `mil.ee` | Эстония |
| `mke.ee` | Эстония |
| `ohtuleht.ee` | Эстония |
| `online.le.ee` | Эстония |
| `telegram.ee` | Эстония |

## Журнал изменений

| Версия | Дата | Изменение | Основание |
|---|---|---|---|
| iid100-1 / iid-lex-1 / iid-sources-1 | 16.11.2026 | Первая версия: 8 языков (ru, be, uk, pl, lt, lv, en, de); страны в таблицах — Украина, Польша, Литва, Латвия, Россия, «Прочие страны» | GREEN t143u |
| iid100-2 / iid-lex-2 / iid-sources-2 | 16.11.2026 | + 26 языков источников «Европа и НАТО» (fr, it, es, pt, ca, ro, nl, sv, da, nb, is, fi, et, hu, cs, sk, sl, hr, bs, sr, mk, bg, sq, el, tr, fa), словари составлены вручную, без ИИ; словари 8 языков iid-lex-1 не изменены. Для новых языков упоминания/топонимы/организации — основа ≥ 5 символов с начала слова. Язык новых лент — язык ленты при совпадении письма (английский текст — по служебным словам); греческое письмо — el. Каждая страна источника — отдельная строка (/iid/, Новостная карта, бот); карточки стран — 477 источников и национальные домены Европы. Источники «только для расчёта»: входят в расчёт, в публичных файлах не показываются (без ссылок, заголовков, текстов и названия). Пересчёт ряда 30 суток по новой версии; ряд источников «только для расчёта» начинается с 12.11.2026 (глубина ленты на момент подключения), поэтому значения iid100-2 с 12.11 выше, чем iid100-1 за те же дни (сравнение — в iid_daily по method_version) | GREEN t153s804 |
| iid100-2 (представление) | 16.11.2026 | Метка материалов «только для расчёта»: суть из заголовка + имя источника спойлером; ссылок и полных заголовков нет. Расчёт не меняется | GREEN t157u, t158u |


---
© 2026 GREEN-CBR. Все права защищены. Разработчик — GREEN-CBR.
