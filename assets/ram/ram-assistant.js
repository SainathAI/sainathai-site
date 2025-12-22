// RAM Assistant — Guided Intelligence
(function () {
  const panel = document.createElement("div");
  panel.id = "ram-assistant";
  panel.innerHTML = `
    <div class="ram-header">RAM</div>
    <div class="ram-body">
      <p>What brings you here?</p>
      <button data-intent="automation">Automation</button>
      <button data-intent="seo">SEO</button>
      <button data-intent="growth">Growth</button>
    </div>
  `;
  document.body.appendChild(panel);

  panel.addEventListener("click", (e) => {
    if (e.target.tagName === "BUTTON") {
      const intent = e.target.dataset.intent;
      RAM.updateMemory("intent", intent);
      panel.querySelector(".ram-body").innerHTML = `
        <p>Intent noted: <strong>${intent}</strong></p>
        <p>Would you like an audit?</p>
        <button data-next="yes">Yes</button>
        <button data-next="later">Later</button>
      `;
      RAM.log("Intent captured: " + intent);
    }
  });

  RAM.log("RAM assistant initialized");
})();
