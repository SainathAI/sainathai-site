(function(){
 if(window.RAM_ACTIVE)return;
 window.RAM_ACTIVE=true;
 const h=document.createElement("div");
 h.style.position="fixed";
 h.style.bottom="24px";
 h.style.right="24px";
 h.style.zIndex="999999";
 document.body.appendChild(h);
 const s=h.attachShadow({mode:"open"});
 s.innerHTML=
 <style>
 .ram{width:280px;background:#020617;color:#e5e7eb;font-family:system-ui;
 border-radius:12px;box-shadow:0 0 40px rgba(0,255,255,.2)}
 .hdr{padding:12px;background:linear-gradient(90deg,#0ea5e9,#22d3ee);
 font-weight:700;text-align:center;color:#020617}
 .msg{padding:12px;font-size:14px}
 button{margin-top:10px;padding:8px 12px;border:none;border-radius:6px;
 background:#2563eb;color:#fff;cursor:pointer}
 </style>
 <div class="ram">
  <div class="hdr">RAM • Healthcare Intelligence</div>
  <div class="msg">
   Are you a hospital, supplier, or technology provider?
   <br><br>
   <button onclick="location.href='#lead-form'">
    Get Qualified Leads
   </button>
  </div>
 </div>;
})();
