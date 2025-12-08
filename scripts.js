document.addEventListener("DOMContentLoaded", function () {
  var modal = document.getElementById("leadModal");
  var openBtn = document.getElementById("openLead");
  var closeBtn = document.getElementById("closeLead");

  if (openBtn && modal) {
    openBtn.addEventListener("click", function (e) {
      e.preventDefault();
      modal.style.display = "block";
    });
  }

  if (closeBtn && modal) {
    closeBtn.addEventListener("click", function () {
      modal.style.display = "none";
    });
  }

  window.addEventListener("click", function (e) {
    if (e.target === modal) modal.style.display = "none";
  });

  var waLink = document.getElementById("waLink");
  if (waLink) {
    var part1 = "+91";
    var part2 = "7075";
    var part3 = "103333";

    waLink.addEventListener("click", function (e) {
      e.preventDefault();
      var phone = part1 + part2 + part3;
      var href = "https://wa.me/" + phone.replace(/\D/g, "");
      window.open(href, "_blank");
    });

    waLink.innerText = "WhatsApp Business";
  }

  var cta = document.getElementById("leadCta");
  if (cta) {
    cta.addEventListener("click", function (e) {
      e.preventDefault();
      if (modal) modal.style.display = "block";
    });
  }
});
