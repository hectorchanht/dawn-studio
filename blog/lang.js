/* Dawn Studio blog language toggle — EN / 廣東話繁中.
   Shares the homepage's localStorage key ("dawn-lang") so a visitor's
   choice carries across the whole site. EN is the default and the
   original text; the zh blocks are Cantonese (spoken-register
   Traditional Chinese), added alongside — never replacing — the EN. */
(function () {
  function apply(lang) {
    document.documentElement.lang = lang === "zh" ? "zh-Hant" : "en";
    document.querySelectorAll(".i18n-en").forEach(function (el) { el.hidden = lang !== "en"; });
    document.querySelectorAll(".i18n-zh").forEach(function (el) { el.hidden = lang !== "zh"; });
    document.querySelectorAll("[data-lang]").forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-lang") === lang ? "true" : "false");
    });
    var t = document.documentElement.getAttribute(lang === "zh" ? "data-title-zh" : "data-title-en");
    if (t) document.title = t;
    try { localStorage.setItem("dawn-lang", lang); } catch (e) {}
  }
  var saved = "en";
  try { saved = localStorage.getItem("dawn-lang") || "en"; } catch (e) {}
  document.querySelectorAll("[data-lang]").forEach(function (b) {
    b.addEventListener("click", function () { apply(b.getAttribute("data-lang")); });
  });
  apply(saved === "zh" ? "zh" : "en");
})();
