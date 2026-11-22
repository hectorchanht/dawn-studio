#!/usr/bin/env python3
"""BLOG SEAM gate: fail if any blog post would ship broken. Run before deploy.
Every blog/<slug>.html must have: canonical + og:url = https://dawnstudio.app/blog/<slug>,
og:title / og:description / og:image (+ width/height), an og:image file that exists in this repo
(PNG cards must be real 1200x630 PNGs), a link from blog.html and a <loc> in sitemap.xml.
Posts dated on/after 2026-11-22 must also carry the full Twitter large card (link media card rule)."""
import glob, os, re, struct, sys

BASE = "https://dawnstudio.app"
index = open("blog.html", encoding="utf-8").read()
sitemap = open("sitemap.xml", encoding="utf-8").read()
fails = []

def meta(html, attr, name):
    m = re.search(r'<meta %s="%s" content="([^"]*)"' % (attr, re.escape(name)), html)
    return m.group(1) if m else None

for path in sorted(glob.glob("blog/*.html")):
    slug = os.path.basename(path)[:-5]
    url = f"{BASE}/blog/{slug}"
    html = open(path, encoding="utf-8").read()
    bad = lambda msg: fails.append(f"{path}: {msg}")
    if f'<link rel="canonical" href="{url}" />' not in html: bad("canonical missing or wrong")
    if meta(html, "property", "og:url") != url: bad("og:url missing or wrong")
    for p in ("og:title", "og:description", "og:image", "og:image:width", "og:image:height", "og:image:alt"):
        if not meta(html, "property", p): bad(f"{p} missing")
    if not re.search(r"<title>[^<]+</title>", html): bad("<title> missing")
    if not meta(html, "name", "description"): bad("meta description missing")
    img = meta(html, "property", "og:image") or ""
    if img.startswith(BASE + "/"):
        local = img[len(BASE) + 1:]
        if not os.path.isfile(local): bad(f"og:image file {local} not in repo")
        elif local.endswith(".png"):
            raw = open(local, "rb").read()
            if raw[:8] != b"\x89PNG\r\n\x1a\n" or struct.unpack(">II", raw[16:24]) != (1200, 630):
                bad(f"og:image {local} is not a 1200x630 PNG")
    else:
        bad(f"og:image {img!r} is not on {BASE}")
    if f'href="/blog/{slug}"' not in index: bad("not linked from blog.html")
    if f"<loc>{url}</loc>" not in sitemap: bad("not in sitemap.xml")
    m = re.search(r'<time datetime="(\d{4}-\d{2}-\d{2})"', html)
    if m and m.group(1) >= "2026-11-22":
        if meta(html, "name", "twitter:card") != "summary_large_image": bad("twitter:card summary_large_image missing")
        if meta(html, "name", "twitter:image") != img: bad("twitter:image missing or differs from og:image")

if fails:
    print("FAIL blog seam:"); [print("  " + f) for f in fails]; sys.exit(1)
print(f"OK blog seam: {len(glob.glob('blog/*.html'))} posts — cards, index links, sitemap all present")
