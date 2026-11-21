#!/usr/bin/env python3
"""LINK MEDIA CARD gate (GOLD rule, Hector 2026-11-20): fail if the media card breaks.
Checks index.html OG/Twitter tags + og.png is a real 1200x630 PNG. Run before deploy."""
import re, struct, sys
html = open("index.html", encoding="utf-8").read()
need = ['property="og:title"', 'property="og:description"', 'property="og:type"',
        'property="og:url" content="https://dawnstudio.app/"',
        'property="og:image" content="https://dawnstudio.app/og.png"',
        'property="og:image:width" content="1200"', 'property="og:image:height" content="630"',
        'property="og:image:alt"', 'name="twitter:card" content="summary_large_image"',
        'name="twitter:image" content="https://dawnstudio.app/og.png"']
missing = [n for n in need if n not in html]
raw = open("og.png", "rb").read()
ok_png = raw[:8] == b"\x89PNG\r\n\x1a\n"
w, h = struct.unpack(">II", raw[16:24]) if ok_png else (0, 0)
if missing: print("FAIL missing tags:", missing); sys.exit(1)
if not ok_png or (w, h) != (1200, 630): print(f"FAIL og.png is {w}x{h}, need 1200x630 PNG"); sys.exit(1)
print("OK media card: tags complete, og.png 1200x630")
