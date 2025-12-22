(function() {
  console.log('[RAM] Initializing');
  const btn = document.createElement('button');
  btn.innerHTML = '💬 Ask RAM';
  btn.style.cssText = 'position: fixed; bottom: 20px; right: 20px; padding: 12px 16px; background: linear-gradient(135deg, #1A73E8, #EFB800); color: white; border: none; border-radius: 50px; cursor: pointer; z-index: 10000;';
  document.body.appendChild(btn);
  window.RAM = {version: '1.0.0', initialized: true};
})();
