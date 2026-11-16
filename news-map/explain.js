/* Контур информационного мониторинга OSINT ЦБР РБ — шапка (последнее обновление, актуально, СБОР ДАННЫХ, До следующего среза ЧЧ:ММ),
   справка по окрасу, субъективности и ОИ 5×5, разъяснение текущего значения при наведении (t72u, t83u, t113u, 14.11.2026);
   t136u-1 (16.11.2026): значки окраса и субъективности из разметки отчёта. */
(function(){
"use strict";
var TZ="Europe/Minsk";
var BASE=(function(){ var s=document.currentScript; return s? s.src.replace(/news-map\/explain\.js.*$/,"") : "/cbr-news-materials/"; })();
function esc(s){ return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];}); }
// ---------- время Europe/Minsk ----------
var FMT=new Intl.DateTimeFormat("ru-RU",{timeZone:TZ,year:"numeric",month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit",hour12:false});
function nowMinsk(){ var p={}; FMT.formatToParts(new Date()).forEach(function(x){p[x.type]=x.value;}); return p.day+"."+p.month+"."+p.year+" "+(p.hour==="24"?"00":p.hour)+":"+p.minute; }
// ---------- шапка ----------
function pad2(n){ return (n<10?"0":"")+n; }
function fmtHM(ms){ if(ms<0) ms=0; var s=Math.floor(ms/1000); return pad2(Math.floor(s/3600))+":"+pad2(Math.floor((s%3600)/60)); }
function parseIso(s){ if(!s) return null; var d=new Date(s); return isNaN(d.getTime())?null:d; }
function parseAsof(s){
  var m=/^(\d{2})\.(\d{2})\.(\d{4})(?:\s+(\d{2}):(\d{2}))?/.exec(s||"");
  if(!m) return parseIso(s);
  return new Date(Date.UTC(+m[3],+m[2]-1,+m[1],(+m[4]||0)-3,+m[5]||0,0));
}
function nextEvenExport(from){
  var d=from?new Date(from):new Date();
  var parts=new Intl.DateTimeFormat("en-GB",{timeZone:TZ,year:"numeric",month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit",second:"2-digit",hour12:false}).formatToParts(d);
  var p={}; parts.forEach(function(x){p[x.type]=x.value;});
  var y=+p.year, mo=+p.month, da=+p.day, h=+(p.hour==="24"?"0":p.hour), mi=+p.minute, se=+p.second;
  function mk(Y,M,D,H,Min){ return new Date(Date.UTC(Y,M-1,D,H-3,Min,0)); }
  var slots=[];
  for(var add=0; add<=1; add++){
    var dt=new Date(Date.UTC(y,mo-1,da+add,0,0,0));
    var Y=dt.getUTCFullYear(), M=dt.getUTCMonth()+1, D=dt.getUTCDate();
    for(var hh=0; hh<24; hh+=2){
      var mm=0; if(hh===20) mm=50; /* слот 20:00 ждёт конца окна 19:40–20:50 */
      slots.push(mk(Y,M,D,hh,mm));
    }
  }
  var now=mk(y,mo,da,h,mi); now.setUTCSeconds(se);
  for(var i=0;i<slots.length;i++){ if(slots[i].getTime()>now.getTime()) return slots[i]; }
  return slots[slots.length-1];
}
function fmtMinsk(dt){
  var parts=new Intl.DateTimeFormat("ru-RU",{timeZone:TZ,year:"numeric",month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit",hour12:false}).formatToParts(dt);
  var p={}; parts.forEach(function(x){p[x.type]=x.value;});
  return p.day+"."+p.month+"."+p.year+" "+(p.hour==="24"?"00":p.hour)+":"+p.minute;
}
function nextTip(dt){
  return "Следующий срез: "+fmtMinsk(dt)+" "+TZ+". Интервал обновления публичных страниц — 2 часа (чётные часы 00:00, 02:00, … 22:00). Если слот попадает в окно сводки, выгрузка ждёт конца окна.";
}
function resolveNext(){
  var a=window.CBR_ASOF||{};
  var now=Date.now();
  var nxt=parseIso(a.next_export);
  if(!nxt || nxt.getTime()<now) return nextEvenExport();
  return nxt;
}
function tickNext(){
  var el=document.getElementById("cbr-next-val");
  var box=document.getElementById("cbr-next");
  if(!el||!box) return;
  var nxt=resolveNext();
  el.textContent=fmtHM(nxt.getTime()-Date.now());
  box.classList.remove("cbr-next-wait");
  box.setAttribute("data-tipc", nextTip(nxt));
}
function visits(){
  var mark=document.querySelector(".cbr-mark"); if(!mark) return;
  var logo=mark.querySelector("b"); if(!logo) return;
  logo.classList.add("cbr-logo");
  logo.setAttribute("tabindex","0");
  var pop=document.getElementById("cbr-visits-pop");
  if(!pop){ pop=document.createElement("div"); pop.id="cbr-visits-pop"; pop.className="cbr-visits-pop"; pop.hidden=true; pop.setAttribute("role","tooltip"); document.body.appendChild(pop); }
  logo.setAttribute("aria-describedby","cbr-visits-pop");
  var text="счётчик недоступен";
  pop.textContent=text;
  function place(){ var r=logo.getBoundingClientRect(); pop.style.left=Math.max(8,Math.round(r.left))+"px"; pop.style.top=Math.round(r.bottom+6)+"px"; }
  function show(){ pop.textContent=text; pop.hidden=false; place(); }
  function hide(){ pop.hidden=true; }
  logo.addEventListener("mouseenter",show);
  logo.addEventListener("mouseleave",function(e){ if(pop.contains(e.relatedTarget)) return; hide(); });
  logo.addEventListener("focus",show);
  logo.addEventListener("blur",hide);
  window.addEventListener("scroll",function(){ if(!pop.hidden) place(); },true);
  window.addEventListener("resize",function(){ if(!pop.hidden) place(); });
  // Один ключ на весь ресурс; +1 за каждую загрузку страницы. В подсказке только число, без IP.
  var url="https://countapi.mileshilliard.com/api/v1/hit/skb-by-github-io-cbr-news-materials-visits";
  fetch(url,{method:"GET",mode:"cors",credentials:"omit",cache:"no-store"}).then(function(r){
    if(!r.ok) throw new Error("http");
    return r.json();
  }).then(function(j){
    var n=j && j.value;
    if(n==null || isNaN(+n)) throw new Error("bad");
    text="Посещений: "+(+n).toLocaleString("ru-RU")+" (с 13.11.2026)";
    if(!pop.hidden) pop.textContent=text;
  }).catch(function(){ text="счётчик недоступен"; if(!pop.hidden) pop.textContent=text; });
}
function chrome(){
  var el=document.getElementById("cbr-asof")||document.querySelector(".cbr-asof"); if(!el) return;
  var a=window.CBR_ASOF||{}; var last=a.as_of||el.getAttribute("data-asof")||"";
  var nxt=resolveNext();
  el.classList.add("cbr-asof");
  el.removeAttribute("title");
  el.innerHTML=
    '<span class="cbr-st" tabindex="0" data-tipc="Статус: идёт сбор данных к очередной порции новостей. Когда порция выйдет, «последнее обновление» сменится на время её выхода, и статус снова будет «СБОР ДАННЫХ» — сбор к следующей порции."><i class="dot-warn"></i>СБОР ДАННЫХ</span>'+
    '<span class="cbr-last" tabindex="0" data-tipc="Последнее обновление — дата и время выхода последней порции: выгрузки актуального отчёта и данных на страницы. Сведения на страницах — на это время.">последнее обновление <b>'+esc(last)+' '+TZ+'</b></span>'+
    '<span class="cbr-now" tabindex="0" data-tipc="Актуально — текущие дата и время Europe/Minsk по часам вашего устройства; обновляются на странице каждую секунду. Это не время сведений."><i class="dot-live"></i>актуально <b id="cbr-now">'+nowMinsk()+' '+TZ+'</b></span>'+
    '<span class="cbr-next" id="cbr-next" tabindex="0" data-tipc="'+esc(nextTip(nxt))+'">До следующего среза <b id="cbr-next-val">'+fmtHM(Math.max(0,nxt.getTime()-Date.now()))+'</b></span>'+
    '<button type="button" class="cbr-help-btn" aria-expanded="false" aria-controls="cbr-help-pop">СПРАВКА</button>';
  var n=document.getElementById("cbr-now");
  tickNext();
  setInterval(function(){ n.textContent=nowMinsk()+" "+TZ; tickNext(); },1000);
  visits();
  var pop=document.createElement("div"); pop.id="cbr-help-pop"; pop.className="cbr-help-pop"; pop.hidden=true;
  pop.innerHTML='<div class="cbr-help-h">Справка: окрас, субъективность, ОИ 5×5 <button type="button" class="cbr-help-x" aria-label="закрыть">×</button></div>'+legendHtml();
  document.body.appendChild(pop);
  var btn=el.querySelector(".cbr-help-btn");
  function tog(v){ pop.hidden=!v; btn.setAttribute("aria-expanded",v?"true":"false"); }
  btn.addEventListener("click",function(e){ e.stopPropagation(); tog(pop.hidden); });
  pop.querySelector(".cbr-help-x").addEventListener("click",function(){ tog(false); });
  document.addEventListener("keydown",function(e){ if(e.key==="Escape") tog(false); });
  document.addEventListener("click",function(e){ if(!pop.hidden && !pop.contains(e.target)) tog(false); });
}
// ---------- шкалы ----------
var OKR=[[-2,"резко негативный","−1.0…−0.6","красный","var(--s-m2)"],[-1,"умеренно негативный","−0.5…−0.2","оранжевый","var(--s-m1)"],
         [0,"нейтральный","−0.1…+0.1","серый","var(--s-0)"],[1,"умеренно позитивный","+0.2…+0.5","светло-зелёный","var(--s-p1)"],
         [2,"резко позитивный","+0.6…+1.0","ярко-зелёный","var(--s-p2)"]];
function okrOf(k){ for(var i=0;i<OKR.length;i++) if(OKR[i][0]===+k) return OKR[i]; return null; }
function sgn(v){ v=+v; return (v>0?"+":v<0?"−":"")+Math.abs(v); }
function sgn1(v){ v=+v; return (v>0?"+":v<0?"−":"")+Math.abs(v).toFixed(1); }
var SRC={"А":"официальный первоисточник","Б":"обычно надёжен","В":"иногда надёжен","Г":"обычно ненадёжен","Д":"оценить нельзя"};
var INF={"1":"точность не вызывает сомнений","2":"сведения от первоисточника, одной цепочки","3":"не от первоисточника, но согласуется с уже учтёнными материалами","4":"оценить нельзя","5":"сомнительно или противоречит уже подтверждённому"};
function status(c){ if(!c||c.length!==2) return ""; if(c[1]==="1") return "новость"; if(c[1]==="2"&&"АБВ".indexOf(c[0])>=0) return "утверждение"; return "слух"; }
function legendHtml(){
  var h='<div class="cbr-legend">';
  h+='<h4>Окрас</h4>';
  h+='<p>Окрас — тональность материала, упоминания или связи. Контур ставит Окрас по правилам на тексте материала (версия расчёта t60u-contour-1). Это не оценка человека.</p>';
  h+='<p>Шкала гибридная: категория, целое число −2…+2 и Sentiment Score −1.0…+1.0 с шагом 0.1. Края Sentiment Score: −1.0 — наиболее негативный, +1.0 — наиболее позитивный.</p>';
  h+='<table><tr><th></th><th>окрас</th><th>число</th><th>Sentiment Score</th><th>цвет</th></tr>';
  OKR.forEach(function(o){ h+='<tr><td><span class="cbr-sw" style="background:'+o[4]+'"></span></td><td>'+o[1]+'</td><td class="mono">'+sgn(o[0])+'</td><td class="mono">'+o[2]+'</td><td>'+o[3]+'</td></tr>'; });
  h+='</table>';
  h+='<p><b>Как считается.</b> Контур ищет в тексте признаки по словарю и считает Sentiment Score.</p>';
  h+='<ol>';
  h+='<li>Сумма весов = 2·сильные позитивные + позитивные + 2·сильные негативные + негативные.</li>';
  h+='<li>Если признаков нет, Sentiment Score = 0.</li>';
  h+='<li>Иначе Sentiment Score = (2·сильные позитивные + позитивные − 2·сильные негативные − негативные) / (сумма весов + 2).</li>';
  h+='<li>Без сильных признаков значение не дальше ±0.5: категория не выше «умеренно» (±1). Категории ±2 бывают только при сильных признаках.</li>';
  h+='<li>Значение ограничивается краями −1.0…+1.0 и округляется до одного знака. По нему ставится категория (таблица выше).</li>';
  h+='</ol>';
  h+='<p>Окрас материала — по заголовку и тексту материала. Окрас упоминания — по предложениям, где сущность названа (предложения соединяются и считается один Sentiment Score). Окрас связи — по предложению, где связь названа; на карте — среднее Sentiment Score по предложениям-основаниям этой связи. Для типа связи «санкции» значение не выше −0.6 (резко негативный); для типа «судебный спор» — не выше −0.2 (умеренно негативный).</p>';
  h+='<p class="ex"><b>Пример.</b> «В материале отмечен прорыв в разработке и проблема с комплектующими.» Признаки: 1 сильный позитивный («прорыв») и 1 негативный («проблема»). Сумма весов = 2·1 + 1 = 3. Sentiment Score = (2 − 1) / (3 + 2) = 0.2. Категория: умеренно позитивный (+1).</p>';
  h+='<p class="ex"><b>Пример.</b> «Компания получила контракт и сообщила об успешных испытаниях.» Признаки: 3 позитивных, сильных нет. Сумма весов = 3. Sentiment Score = 3 / (3 + 2) = 0.6, без сильных признаков ограничивается до +0.5. Категория: умеренно позитивный (+1), не резко позитивный.</p>';
  h+='<p class="ex"><b>Пример.</b> «Министерство опубликовало график учений на следующий месяц.» Признаков нет. Sentiment Score = 0. Категория: нейтральный (0).</p>';
  h+='<p>Как читать число: Sentiment Score — положение на шкале −1.0…+1.0; целое число −2…+2 и подпись — категория из таблицы.</p>';
  h+='<p class="m">Ограничения. Окрас ставит контур по правилам и словарю признаков, не человек. Слова вне словаря на расчёт не влияют. Окрас упоминания и связи считается не по всему материалу, а по предложению (предложениям), где они названы.</p>';
  h+='<h4>Субъективность / манипулятивность</h4>';
  h+='<p>Субъективность / манипулятивность — положение материала на шкале оценочной, восклицательной или перволичной подачи и заглавных слов в заголовке. Показывается число.</p>';
  h+='<p>Шкала 0…+1 с шагом 0.1. 0 — нижний край шкалы: субъективность / манипулятивность наименьшая. 1 — верхний край шкалы: субъективность / манипулятивность наибольшая. Промежуточное значение — положение материала между этими краями. Контур начинает с 0.1, поэтому у текста без признаков значение 0.1, а не 0.</p>';
  h+='<p><b>Как считается.</b> Контур считает значение по правилам на тексте материала (заголовок входит в текст; «!!!» и заглавные слова проверяются по заголовку):</p>';
  h+='<ol>';
  h+='<li>Начальное значение 0.1.</li>';
  h+='<li>+0.15 за каждое оценочное слово из словаря признаков (не более 4, то есть не более +0.60).</li>';
  h+='<li>+0.1, если в тексте два и более «!» или в заголовке есть «!!!».</li>';
  h+='<li>+0.15 за речь от первого лица по словарю признаков: «я считаю», «по моему мнению», «на мой взгляд», «мы считаем», «на мою думку», «I think», «in my view», «I believe», «we believe».</li>';
  h+='<li>+0.05, если в тексте два и более «?».</li>';
  h+='<li>+0.1, если в заголовке два и более слова из пяти и более заглавных букв.</li>';
  h+='<li>Не выше 1.0; результат округляется до одного знака.</li>';
  h+='</ol>';
  h+='<p class="ex"><b>Пример.</b> «Министерство опубликовало график учений на следующий месяц.» Признаков нет. Значение = 0.1.</p>';
  h+='<p class="ex"><b>Пример.</b> «Я считаю, что это блестящий триумф!!» Оценочные слова «блестящий» и «триумф» — +0.30; два «!» — +0.1; речь от первого лица «Я считаю» — +0.15. 0.1 + 0.30 + 0.1 + 0.15 = 0.65, после округления до одного знака — 0.7.</p>';
  h+='<p class="ex"><b>Пример.</b> Заголовок «СРОЧНО ВАЖНО», текст «Я считаю, это чудовищный позор и ужасный провал!! Что дальше? Кто ответит?» Четыре оценочных слова — +0.60; два «!» — +0.1; речь от первого лица — +0.15; два «?» — +0.05; два заглавных слова из пяти и более букв в заголовке — +0.1. 0.1 + 0.60 + 0.1 + 0.15 + 0.05 + 0.1 = 1.10, ограничивается до 1.0.</p>';
  h+='<p>Как читать число: показывается с одним знаком после запятой. Это положение на шкале 0…+1; отдельных категорий контур не ставит.</p>';
  h+='<p class="m">Ограничения. Субъективность / манипулятивность считает контур по правилам и словарю признаков, не человек. Оценочные слова и речь от первого лица учитываются только из словаря. Значение считается для материала в целом, не для отдельного упоминания или связи. Какие признаки сработали в конкретном материале, в контуре не записано.</p>';
  h+='<h4>ОИ 5×5</h4><p>Буква — надёжность источника: А — официальный первоисточник, Б — обычно надёжен, В — иногда надёжен, Г — обычно ненадёжен, Д — оценить нельзя. Цифра — достоверность сведений: 1 — точность не вызывает сомнений, 2 — сведения от первоисточника, одной цепочки, 3 — не от первоисточника, но согласуется с уже учтёнными материалами, 4 — оценить нельзя, 5 — сомнительно или противоречит уже подтверждённому.</p>';
  h+='<p><b>Первоначальная ОИ</b> — код на дату публикации. <b>ОИ со временем</b> — код после независимого подтверждения более поздними материалами. Статус: сведения 1 — «новость»; А2, Б2, В2 — «утверждение»; остальное — «слух».</p>';
  h+='<p class="m">Наведите курсор на значок ОИ, окраса или субъективности у материала — появится разъяснение его текущего значения и записанное основание. <a href="'+BASE+'OI_5x5.html">ОИ 5×5 — правила</a> · <a href="'+BASE+'oi-5x5/">цветная матрица</a></p></div>';
  return h;
}
// ---------- данные оснований ----------
var DATA=null, waiting=[];
function loadData(cb){ if(DATA){ cb(DATA); return; } waiting.push(cb); if(waiting.length>1) return;
  var s=document.createElement("script"); s.src=BASE+"news-map/explain_data.js?v=t72";
  s.onload=function(){ DATA=window.CBR_EXPLAIN_DATA||{S:[],H:{},U:{},X:{}}; waiting.splice(0).forEach(function(f){f(DATA);}); };
  s.onerror=function(){ DATA={S:[],H:{},U:{},X:{},err:1}; waiting.splice(0).forEach(function(f){f(DATA);}); };
  document.head.appendChild(s); }
function fnv(str){ var h=0x811c9dc5, b=new TextEncoder().encode(str); for(var i=0;i<b.length;i++){ h^=b[i]; h=Math.imul(h,0x01000193)>>>0; } return ("0000000"+h.toString(16)).slice(-8); }
function hashOf(el, D){ var h=el.getAttribute("data-h"); if(h) return h.slice(0,16); var u=el.getAttribute("data-u"); return u&&D.U[fnv(u)]||""; }
function S(D,i){ return i>=0? D.S[i] : ""; }
function q(s){ return "«"+esc(s)+"»"; }
function tipOI(el,D){
  var c=el.getAttribute("data-c"), k=el.getAttribute("data-k")||"0", h=hashOf(el,D), r=h&&D.H[h];
  var t='<b>'+(k==="1"?"ОИ со временем":"Первоначальная ОИ")+': '+esc(c)+'</b> — '+esc(status(c))+
        '<div>Буква '+esc(c[0])+' — надёжность источника: '+esc(SRC[c[0]]||"")+'.</div><div>Цифра '+esc(c[1])+' — достоверность сведений: '+esc(INF[c[1]]||"")+'.</div>';
  if(r && (k==="1"? r[3]===c : r[0]===c)){
    if(k==="1"){ var b=S(D,r[4]); t+='<div class="b"><u>Основание (evolved_basis)</u>: '+(b?q(b):"основание в таблице не записано")+'</div>'; }
    else { var bs=S(D,r[1]), bi=S(D,r[2]);
      t+='<div class="b"><u>Основание по источнику (initial_basis_source)</u>: '+(bs?q(bs):"основание в таблице не записано")+'</div>'+
         '<div class="b"><u>Основание по сведениям (initial_basis_info)</u>: '+(bi?q(bi):"основание в таблице не записано")+'</div>'; }
  } else t+='<div class="b">Основание к этому коду в таблице не записано.</div>';
  return t+'<div class="m">Основания — из таблицы ОИ (проход '+esc(fmtIso(D.oi_basis_as_of))+' Europe/Minsk).</div>';
}
function fmtIso(s){ if(!s) return ""; var m=/^(\d{4})-(\d\d)-(\d\d)T(\d\d):(\d\d)/.exec(s); return m? m[3]+"."+m[2]+"."+m[1]+" "+m[4]+":"+m[5] : s; }
function tipOkr(el,D){
  var k=el.getAttribute("data-s2"), s1=el.getAttribute("data-s1"), lvl=el.getAttribute("data-lvl")||"doc", ev=el.getAttribute("data-q")||"";
  var o=okrOf(k); if(!o) return "";
  var what={doc:"материала",rel:"связи",ment:"упоминания"}[lvl]||"материала";
  var t='<b>Окрас '+what+': '+o[1]+' ('+sgn(o[0])+')</b>'+(s1!=null&&s1!==""?' · Sentiment Score <b>'+sgn1(s1)+'</b>':"")+
        '<div>Категория «'+o[1]+'»: число '+sgn(o[0])+', Sentiment Score '+o[2]+', цвет — '+o[3]+'.</div>'+
        '<div>Окрас ставит контур по словарю признаков на тексте (версия t60u-contour-1). Для упоминания и связи — по предложению, где они названы. Пример: 1 сильный позитивный и 1 негативный признак дают Sentiment Score (2 − 1) / (3 + 2) = 0.2, категория «умеренно позитивный». Полное описание с примерами — кнопка «СПРАВКА».</div>';
  var nn=+(el.getAttribute("data-n")||0);
  if(ev) t+='<div class="b"><u>'+(lvl==="rel"&&nn>1?'Предложение-основание (одно из '+nn+', окрас связи — среднее по ним)':'Предложение-основание')+'</u>: '+q(ev)+'</div>';
  else if(lvl==="doc"){ var h=hashOf(el,D), x=h&&D.X[h];
    t+='<div class="b">Окрас материала вычислен контуром по правилам на тексте материала (t60u-contour-1); отдельная цитата-основание для окраса материала в контуре не записана.'+(x&&x[3]&&x[3].length?' Маркеры рисков в тексте: '+esc(x[3].join(", "))+'.':"")+'</div>'; }
  else t+='<div class="b">Окрас вычислен контуром по правилам на тексте; цитата-основание не записана.</div>';
  return t;
}
function tipSubj(el){
  var v=+el.getAttribute("data-v"); if(isNaN(v)) return "";
  var end = v<0.5? "ближе к нижнему краю шкалы (0 — субъективность / манипулятивность наименьшая)" : v>0.5? "ближе к верхнему краю шкалы (1 — субъективность / манипулятивность наибольшая)" : "середина шкалы между нижним краем 0 и верхним краем 1";
  return '<b>Субъективность / манипулятивность: '+v.toFixed(1)+'</b> (шкала 0…+1)<div>Значение '+v.toFixed(1)+' — '+end+'.</div>'+
         '<div>Контур считает значение по правилам на тексте материала: начало 0.1, надбавки за оценочные слова, «!», речь от первого лица, «?» и заглавные слова в заголовке; не выше 1.0, округление до одного знака. Пример: «Я считаю, что это блестящий триумф!!» — 0.1 + 0.30 + 0.1 + 0.15 = 0.65, после округления 0.7.</div>'+
         '<div class="b">Какие признаки сработали в этом материале, в контуре не записано. Полное описание с примерами — кнопка «СПРАВКА».</div>';
}
// ---------- подсказка ----------
var tip=null, cur=null;
function showTip(el){
  cur=el; var x=el.getAttribute("data-x");
  function render(D){ if(cur!==el) return;
    var h = el.hasAttribute("data-tipc") ? esc(el.getAttribute("data-tipc")) : x==="oi"? tipOI(el,D) : x==="okr"? tipOkr(el,D) : x==="subj"? tipSubj(el) : "";
    if(!h) return;
    if(!tip){ tip=document.createElement("div"); tip.className="cbr-tip"; tip.setAttribute("role","tooltip"); document.body.appendChild(tip); }
    tip.innerHTML=h; tip.style.display="block";
    var r=el.getBoundingClientRect(), w=tip.offsetWidth, hh=tip.offsetHeight, vw=document.documentElement.clientWidth, vh=document.documentElement.clientHeight;
    var left=Math.min(Math.max(6,r.left), vw-w-6), top=r.bottom+6; if(top+hh>vh-6) top=Math.max(6,r.top-hh-6);
    tip.style.left=left+"px"; tip.style.top=top+"px"; }
  if(x==="oi"||x==="okr") loadData(render); else render(DATA||{});
}
function hideTip(el){ if(cur===el){ cur=null; if(tip) tip.style.display="none"; } }
function target(e){ return e.target&&e.target.closest? e.target.closest("[data-x],[data-tipc]") : null; }
document.addEventListener("mouseover",function(e){ var t=target(e); if(t&&t!==cur) showTip(t); });
document.addEventListener("mouseout",function(e){ var t=target(e); if(t&&!(e.relatedTarget&&t.contains(e.relatedTarget))) hideTip(t); });
document.addEventListener("focusin",function(e){ var t=target(e); if(t) showTip(t); });
document.addEventListener("focusout",function(e){ var t=target(e); if(t) hideTip(t); });
window.addEventListener("scroll",function(){ if(cur) hideTip(cur); },true);
// ---------- значки для страниц ----------
var SC={"-2":"var(--s-m2)","-1":"var(--s-m1)","0":"var(--s-0)","1":"var(--s-p1)","2":"var(--s-p2)"};
var API={
  legendHtml:legendHtml, status:status, loadData:loadData,
  okrBadge:function(s2,s1,o){ o=o||{}; if(s2==null||s2==="") return ""; var c=okrOf(s2); if(!c) return "";
    return '<span class="cbr-b cbr-okr" tabindex="0" data-x="okr" data-s2="'+s2+'"'+(s1!=null?' data-s1="'+s1+'"':"")+(o.h?' data-h="'+esc(o.h)+'"':"")+(o.u?' data-u="'+esc(o.u)+'"':"")+(o.lvl?' data-lvl="'+o.lvl+'"':"")+(o.q?' data-q="'+esc(o.q)+'"':"")+' style="background:'+SC[String(s2)]+'">окрас '+sgn(s2)+(s1!=null?' ('+sgn1(s1)+')':"")+'</span>'; },
  subjBadge:function(v,o){ o=o||{}; if(v==null||v==="") return ""; return '<span class="cbr-b cbr-subj" tabindex="0" data-x="subj" data-v="'+v+'"'+(o.h?' data-h="'+esc(o.h)+'"':"")+'>субъективность '+(+v).toFixed(1)+'</span>'; },
  oiAttrs:function(code,k,h,u){ return ' tabindex="0" data-x="oi" data-c="'+esc(code)+'" data-k="'+(k?1:0)+'"'+(h?' data-h="'+esc(h)+'"':"")+(u?' data-u="'+esc(u)+'"':""); }
};
window.CBRX=API;
// ---------- актуальный отчёт: значки ОИ из выгрузки, окрас и субъективность ----------
function enhanceReport(){
  if(!/%D0%9E%D0%A2%D0%A7|ОТЧЁТ/.test(location.pathname+decodeURIComponent(location.pathname))) return;
  var main=document.querySelector(".cbr-doc"); if(!main) return;
  var d=document.createElement("details"); d.className="cbr-help-inline"; d.innerHTML='<summary>Справка: окрас, субъективность, ОИ 5×5</summary>'+legendHtml();
  var h1=main.querySelector("p"); if(h1&&h1.nextSibling) main.insertBefore(d,h1.nextSibling); else main.prepend(d);
  loadData(function(D){
    main.querySelectorAll("li").forEach(function(li){
      var a=li.querySelector("a[href^='http']"); if(!a) return; var u=a.getAttribute("href");
      var sp=[].slice.call(li.querySelectorAll("span[title^='ОИ 5×5:']")); if(!sp.length) return;
      sp.forEach(function(s,i){ var c=s.textContent.trim(); s.removeAttribute("title"); s.setAttribute("tabindex","0"); s.setAttribute("data-x","oi"); s.setAttribute("data-c",c);
        s.setAttribute("data-k", /ОИ со временем\s*$/.test((s.previousSibling&&s.previousSibling.textContent)||"")?"1":"0"); s.setAttribute("data-u",u); s.classList.add("cbr-oi"); });
      /* t136u-1: значки окраса и субъективности уже в разметке отчёта (public_export.okr_badge/subj_badge) — не дублируем */
      li.querySelectorAll("[data-x=okr],[data-x=subj]").forEach(function(b){ b.removeAttribute("title"); });
      if(li.querySelector("[data-x=okr]")) return;
      var h=D.U[fnv(u)], x=h&&D.X[h]; if(!x) return;
      var last=sp[sp.length-1], w=document.createElement("span"); w.innerHTML=" · "+API.okrBadge(x[1],x[0],{h:h})+" "+API.subjBadge(x[2],{h:h});
      last.parentNode.insertBefore(w,last.nextSibling);
    });
  });
}
function init(){ chrome(); enhanceReport(); }
if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",init); else init();
})();
