// RAM UI — Visual Consciousness
(function () {
  const hud = document.createElement("div");
  hud.id = "ram-hud";
  hud.innerHTML = `
    <div class="ram-ring"></div>
    <div class="ram-status">RAM ACTIVE</div>
  `;
  document.body.appendChild(hud);

  document.addEventListener("mousemove", (e) => {
    const x = e.clientX / window.innerWidth;
    const y = e.clientY / window.innerHeight;
    hud.style.transform = `translate(${x * 10}px, ${y * 10}px)`;
  });

  RAM.log("RAM UI loaded");
})();
