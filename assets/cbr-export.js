/* © 2026 GREEN-CBR. Все права защищены. Разработчик — GREEN-CBR.
   t171u: выгрузка отфильтрованных срезов в CSV, JSON и GraphML прямо со страницы (без сервера).
   Данные — только те, что уже загружены страницей из публичного среза (одни и те же значения на всех страницах, t153u).
   Материалы «только для расчёта ИИД-100» (iid_only) в выгрузки не попадают: строки с признаком iid_only отбрасываются. */
(function(){
var COPY="© 2026 GREEN-CBR. Все права защищены. Разработчик — GREEN-CBR";
var PROJECT="КОНТУР - I-OSINT BY";
function minskNow(){ var d=new Date(Date.now()+3*3600e3); return d.toISOString().slice(0,19).replace("T"," ")+" Europe/Minsk"; }
function meta(page, scope, filters, extra){
  var a=window.CBR_ASOF||{};
  var m={project:PROJECT, page:page, scope:scope||"текущий срез по фильтрам страницы", slice_as_of:a.as_of||"", oi_as_of:a.oi_as_of||"",
         tz:"Europe/Minsk", exported_at:minskNow(), filters:filters||{}, copyright:COPY,
         note:"Новости — собственность их источников. Материалы «только для расчёта ИИД-100» не выгружаются."};
  if(extra) for(var k in extra) m[k]=extra[k];
  return m; }
function clean(rows){ return (rows||[]).filter(function(r){ return !(r&&(r.iid_only||r._iid_only)); }); }
function cell(v){ if(v==null) return ""; if(typeof v==="object") v=JSON.stringify(v); v=String(v);
  return /[",\n\r;]/.test(v) ? '"'+v.replace(/"/g,'""')+'"' : v; }
function stamp(){ return new Date(Date.now()+3*3600e3).toISOString().slice(0,16).replace(/[-:T]/g,""); }
function save(name, text, mime){
  var b=new Blob([text],{type:mime+";charset=utf-8"}), u=URL.createObjectURL(b), a=document.createElement("a");
  a.href=u; a.download=name; document.body.appendChild(a); a.click(); setTimeout(function(){ URL.revokeObjectURL(u); a.remove(); },500); }
function csvText(fields, rows, m){
  var head="# "+[m.project, m.page, m.scope, "срез "+m.slice_as_of, "ОИ "+m.oi_as_of, "выгружено "+m.exported_at, m.copyright].join(" · ");
  var out=[head, fields.map(cell).join(",")];
  clean(rows).forEach(function(r){ out.push(fields.map(function(f){ return cell(r[f]); }).join(",")); });
  return "\ufeff"+out.join("\r\n")+"\r\n"; }
function xesc(s){ return String(s==null?"":s).replace(/[<>&"']/g,function(c){ return {"<":"&lt;",">":"&gt;","&":"&amp;",'"':"&quot;","'":"&apos;"}[c]; }); }
function graphmlText(nodes, edges, m, nkeys, ekeys){
  nodes=clean(nodes); var ids={}; nodes.forEach(function(n){ ids[n.id]=1; });
  edges=clean(edges).filter(function(e){ return ids[e.s]&&ids[e.t]; });
  var o=['<?xml version="1.0" encoding="UTF-8"?>','<!-- '+xesc(m.project+" · "+m.page+" · "+m.scope+" · срез "+m.slice_as_of+" · "+m.copyright)+' -->',
         '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">'];
  nkeys.forEach(function(k){ o.push('<key id="n_'+k+'" for="node" attr.name="'+k+'" attr.type="string"/>'); });
  ekeys.forEach(function(k){ o.push('<key id="e_'+k+'" for="edge" attr.name="'+k+'" attr.type="string"/>'); });
  o.push('<key id="g_meta" for="graph" attr.name="meta" attr.type="string"/>');
  o.push('<graph id="kontur" edgedefault="directed"><data key="g_meta">'+xesc(JSON.stringify(m))+'</data>');
  nodes.forEach(function(n){ o.push('<node id="'+xesc(n.id)+'">'+nkeys.filter(function(k){ return n[k]!=null&&n[k]!==""; }).map(function(k){ return '<data key="n_'+k+'">'+xesc(typeof n[k]==="object"?JSON.stringify(n[k]):n[k])+'</data>'; }).join("")+'</node>'); });
  edges.forEach(function(e,i){ o.push('<edge id="'+xesc(e.id||("e"+i))+'" source="'+xesc(e.s)+'" target="'+xesc(e.t)+'">'+ekeys.filter(function(k){ return e[k]!=null&&e[k]!==""; }).map(function(k){ return '<data key="e_'+k+'">'+xesc(typeof e[k]==="object"?JSON.stringify(e[k]):e[k])+'</data>'; }).join("")+'</edge>'); });
  o.push("</graph></graphml>"); return o.join("\n")+"\n"; }
var API={
  COPY:COPY, meta:meta, clean:clean, csvText:csvText, graphmlText:graphmlText,
  csv:function(base, fields, rows, m){ save(base+"_"+stamp()+".csv", csvText(fields, rows, m), "text/csv"); },
  json:function(base, data, m){ var o={meta:m}; for(var k in data) o[k]=clean(data[k]); save(base+"_"+stamp()+".json", JSON.stringify(o,null,1), "application/json"); },
  graphml:function(base, nodes, edges, m, nkeys, ekeys){ save(base+"_"+stamp()+".graphml", graphmlText(nodes, edges, m, nkeys, ekeys), "application/xml"); },
  /* панель кнопок: btns = [[подпись, функция], ...] */
  panel:function(el, title, btns, note){ if(!el) return; var h='<div class="cbr-exp"><b>'+xesc(title)+'</b> ';
    h+=btns.map(function(b,i){ return '<button type="button" data-i="'+i+'">'+xesc(b[0])+'</button>'; }).join(" ");
    if(note) h+='<div class="cbr-exp-n">'+note+'</div>';
    el.innerHTML=h+'</div>'; el.querySelectorAll("button[data-i]").forEach(function(x){ x.onclick=function(){ btns[+x.getAttribute("data-i")][1](); }; }); }
};
window.CBR_EXPORT=API;
if(!document.getElementById("cbr-exp-css")){ var s=document.createElement("style"); s.id="cbr-exp-css";
  s.textContent=".cbr-exp{margin:8px 0;padding:6px 8px;border:1px solid var(--line,#ccc);border-radius:4px;font-size:12.5px}.cbr-exp button{margin:2px 2px 2px 0;font:inherit;cursor:pointer;padding:2px 8px;background:var(--bg-2,#eee);color:var(--text,#000);border:1px solid var(--line-2,#aaa);border-radius:3px}.cbr-exp-n{margin-top:4px;opacity:.75;font-size:11.5px}";
  document.head.appendChild(s); }
})();
