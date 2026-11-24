# Unified chrome — single source

`header.html` (the site topnav) and `footer.html` in this folder are the
CANONICAL chrome for dawnstudio.app. Every page of the site embeds a copy of
these exact blocks:

- header: index.html, blog.html, blog/*.html, changelog.html, examples.html,
  canon.html, privacy.html, 404.html
- footer: same list
- EXCLUDED: gateway.html (Dawn Free Port is a separate product surface with
  its own chrome) and this chrome/ folder itself.

Static hosting has no includes, so pages carry embedded copies. When the
chrome changes: edit the fragment here FIRST, then re-apply it to every page
above in the same commit. Run `python3 chrome/check_chrome.py` — it diffs the
embedded header/footer of every page against these fragments and fails on
drift. A page whose chrome differs from the fragment is a defect.
