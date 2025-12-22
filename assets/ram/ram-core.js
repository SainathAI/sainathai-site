// RAM Core — Central Intelligence
window.RAM = {
  state: {
    active: true,
    idle: false,
    page: document.body.dataset.page || location.pathname,
    lastInteraction: Date.now(),
    memory: JSON.parse(sessionStorage.getItem("RAM_MEMORY") || "{}")
  },

  updateMemory(key, value) {
    this.state.memory[key] = value;
    sessionStorage.setItem("RAM_MEMORY", JSON.stringify(this.state.memory));
  },

  log(event) {
    console.log("[RAM]", event);
  }
};

RAM.log("RAM core initialized");
