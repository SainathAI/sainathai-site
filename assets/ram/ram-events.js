// RAM Events — Awareness Layer
(function () {
  const idleLimit = 15000;

  document.addEventListener("mousemove", () => {
    RAM.state.lastInteraction = Date.now();
    RAM.state.idle = false;
    document.body.classList.remove("ram-idle");
  });

  document.addEventListener("scroll", () => {
    RAM.state.lastInteraction = Date.now();
  });

  setInterval(() => {
    if (Date.now() - RAM.state.lastInteraction > idleLimit) {
      if (!RAM.state.idle) {
        RAM.state.idle = true;
        document.body.classList.add("ram-idle");
        RAM.log("User idle");
      }
    }
  }, 3000);
})();
