/* Контур информационного мониторинга OSINT ЦБР РБ — шапка (последнее обновление, актуально, СБОР ДАННЫХ),
   справка по окрасу, субъективности и ОИ 5×5, разъяснение текущего значения при наведении (t72u, 13.11.2026). */
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
function fmtHMS(ms){ if(ms<0) ms=0; var s=Math.floor(ms/1000); return pad2(Math.floor(s/3600))+":"+pad2(Math.floor((s%3600)/60))+":"+pad2(s%60); }
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
  return "Следующая порция: "+fmtMinsk(dt)+" "+TZ+". Интервал обновления публичных страниц — 2 часа (чётные часы 00:00, 02:00, … 22:00). Если слот попадает в окно сводки, выгрузка ждёт конца окна.";
}
function tickNext(){
  var a=window.CBR_ASOF||{};
  var el=document.getElementById("cbr-next-val");
  var box=document.getElementById("cbr-next");
  if(!el||!box) return;
  var nxt=parseIso(a.next_export)||nextEvenExport();
  var now=new Date();
  var last=parseAsof(a.as_of||"");
  if(now.getTime()>=nxt.getTime() && (!last || last.getTime()<nxt.getTime())){
    el.textContent="СБОР ДАННЫХ";
    box.classList.add("cbr-next-wait");
    box.setAttribute("data-tipc", "Назначенное время порции ("+fmtMinsk(nxt)+" "+TZ+") уже наступило, новая порция ещё не выложена. Статус остаётся «СБОР ДАННЫХ». Интервал обновления — 2 часа.");
    return;
  }
  if(now.getTime()>=nxt.getTime()) nxt=nextEvenExport(now);
  el.textContent=fmtHMS(nxt.getTime()-now.getTime());
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
  var nxt=parseIso(a.next_export)||nextEvenExport();
  el.classList.add("cbr-asof");
  el.removeAttribute("title");
  el.innerHTML=
    '<span class="cbr-st" tabindex="0" data-tipc="Статус: идёт сбор данных к очередной порции новостей. Когда порция выйдет, «последнее обновление» сменится на время её выхода, и статус снова будет «СБОР ДАННЫХ» — сбор к следующей порции."><i class="dot-warn"></i>СБОР ДАННЫХ</span>'+
    '<span class="cbr-last" tabindex="0" data-tipc="Последнее обновление — дата и время выхода последней порции: выгрузки актуального отчёта и данных на страницы. Сведения на страницах — на это время.">последнее обновление <b>'+esc(last)+' '+TZ+'</b></span>'+
    '<span class="cbr-now" tabindex="0" data-tipc="Актуально — текущие дата и время Europe/Minsk по часам вашего устройства; обновляются на странице каждую секунду. Это не время сведений."><i class="dot-live"></i>актуально <b id="cbr-now">'+nowMinsk()+' '+TZ+'</b></span>'+
    '<span class="cbr-next" id="cbr-next" tabindex="0" data-tipc="'+esc(nextTip(nxt))+'">до следующей порции <b id="cbr-next-val">'+fmtHMS(Math.max(0,nxt.getTime()-Date.now()))+'</b></span>'+
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
  var h='<div class="cbr-legend"><h4>Окрас</h4><p>Окрас — тональность материала, упоминания или связи. Гибридная шкала: категория, целое число −2…+2 и Sentiment Score −1.0…+1.0 с шагом 0.1.</p><table><tr><th></th><th>окрас</th><th>число</th><th>Sentiment Score</th><th>цвет</th></tr>';
  OKR.forEach(function(o){ h+='<tr><td><span class="cbr-sw" style="background:'+o[4]+'"></span></td><td>'+o[1]+'</td><td class="mono">'+sgn(o[0])+'</td><td class="mono">'+o[2]+'</td><td>'+o[3]+'</td></tr>'; });
  h+='</table><p class="m">Окрас ставит контур по правилам на тексте материала (версия расчёта t60u-contour-1): Sentiment Score = (2·сильные позитивные + позитивные − 2·сильные негативные − негативные) / (сумма весов + 2) по словарю признаков; без сильных признаков — не дальше ±0.5. Окрас упоминания и связи — по предложению, где они названы.</p>'+
     '<h4>Субъективность / манипулятивность</h4><p>Шкала 0…+1. 0 — нижний край шкалы: субъективность / манипулятивность наименьшая. 1 — верхний край шкалы: субъективность / манипулятивность наибольшая. Промежуточное значение — положение материала между этими краями; показывается число.</p>'+
     '<p class="m">Контур считает значение по правилам на тексте материала: начальное значение 0.1; +0.15 за каждое оценочное слово (не более 4); +0.1 за два и более «!» в тексте или «!!!» в заголовке; +0.15 за речь от первого лица; +0.05 за два и более «?»; +0.1 за два и более слова заглавными буквами в заголовке; не выше 1.0.</p>'+
     '<h4>ОИ 5×5</h4><p>Буква — надёжность источника: А — официальный первоисточник, Б — обычно надёжен, В — иногда надёжен, Г — обычно ненадёжен, Д — оценить нельзя. Цифра — достоверность сведений: 1 — точность не вызывает сомнений, 2 — сведения от первоисточника, одной цепочки, 3 — не от первоисточника, но согласуется с уже учтёнными материалами, 4 — оценить нельзя, 5 — сомнительно или противоречит уже подтверждённому.</p>'+
     '<p><b>Первоначальная ОИ</b> — код на дату публикации. <b>ОИ со временем</b> — код после независимого подтверждения более поздними материалами. Статус: сведения 1 — «новость»; А2, Б2, В2 — «утверждение»; остальное — «слух».</p>'+
     '<p class="m">Наведите курсор на значок ОИ, окраса или субъективности у материала — появится разъяснение его текущего значения и записанное основание. <a href="'+BASE+'OI_5x5.html">ОИ 5×5 — правила</a> · <a href="'+BASE+'oi-5x5/">цветная матрица</a></p></div>';
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
        '<div>Категория «'+o[1]+'»: число '+sgn(o[0])+', Sentiment Score '+o[2]+', цвет — '+o[3]+'.</div>';
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
         '<div class="b">Значение вычислено контуром по правилам на тексте материала: от 0.1, +0.15 за оценочное слово (не более 4), +0.1 за «!», +0.15 за первое лицо, +0.05 за «?», +0.1 за слова заглавными в заголовке. Какие признаки сработали в этом материале, в контуре не записано.</div>';
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
      var h=D.U[fnv(u)], x=h&&D.X[h]; if(!x) return;
      var last=sp[sp.length-1], w=document.createElement("span"); w.innerHTML=" · "+API.okrBadge(x[1],x[0],{h:h})+" "+API.subjBadge(x[2],{h:h});
      last.parentNode.insertBefore(w,last.nextSibling);
    });
  });
}
function init(){ chrome(); enhanceReport(); }
if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",init); else init();
})();
