#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render a Markdown build spec to a clean, branded-looking PDF.

Usage:
    python md2pdf.py <input.md> [output.pdf]

If output.pdf is omitted, it is derived from the input filename.

Dependencies (pure-Python, no system libraries needed):
    pip install markdown xhtml2pdf

Why this exists: the campaign build spec is delivered as both .md and .pdf. The
PDF must render tables, code (URLs/UTMs), and Unicode specs (<=, micro, x-times,
em dashes) without tofu/replacement chars. xhtml2pdf renders on top of reportlab,
whose built-in Helvetica lacks many glyphs, so we register a full-Unicode TrueType
font up front and map it for regular+bold. Falls back gracefully across platforms.
"""
import os
import sys

import markdown
from xhtml2pdf import pisa
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

# ── Register a Unicode TTF so specs and symbols render (no replacement chars) ──
# Try common fonts across Windows / macOS / Linux. First hit wins.
_FONT_CANDIDATES = [
    # (regular_path, bold_path)
    (r"C:/Windows/Fonts/arial.ttf", r"C:/Windows/Fonts/arialbd.ttf"),
    (r"C:/Windows/Fonts/segoeui.ttf", r"C:/Windows/Fonts/segoeuib.ttf"),
    ("/Library/Fonts/Arial.ttf", "/Library/Fonts/Arial Bold.ttf"),
    ("/System/Library/Fonts/Supplemental/Arial.ttf",
     "/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
     "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
     "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"),
]

BODY_FONT = "Helvetica"  # last-resort default (may drop rare glyphs)
for reg, bold in _FONT_CANDIDATES:
    if os.path.exists(reg):
        try:
            pdfmetrics.registerFont(TTFont("BodyU", reg))
            if os.path.exists(bold):
                pdfmetrics.registerFont(TTFont("BodyU-Bold", bold))
                addMapping("BodyU", 1, 0, "BodyU-Bold")
            else:
                addMapping("BodyU", 1, 0, "BodyU")  # fake-bold via same face
            addMapping("BodyU", 0, 0, "BodyU")
            BODY_FONT = "BodyU"
            break
        except Exception:
            continue

CSS = """
@page {{ size: letter; margin: 1.6cm 1.4cm 1.8cm 1.4cm; }}
body {{ font-family: "{body}", Arial, sans-serif; font-size: 8.6pt; color: #1a1a1a; line-height: 1.4; }}
h1 {{ font-size: 17pt; color: #0b3d5c; border-bottom: 2px solid #0b3d5c; padding-bottom: 4px; margin: 0 0 10px 0; }}
h2 {{ font-size: 12.5pt; color: #0b3d5c; border-bottom: 1px solid #c9d6de; padding-bottom: 3px; margin: 16px 0 6px 0; }}
h3 {{ font-size: 10.5pt; color: #14708f; margin: 12px 0 4px 0; }}
h4 {{ font-size: 9.5pt; color: #333; margin: 9px 0 3px 0; }}
p {{ margin: 4px 0; }}
strong {{ color: #0b3d5c; }}
code {{ font-family: Courier, monospace; font-size: 8pt; background: #f2f4f6; padding: 0 2px; }}
pre {{ background: #f2f4f6; border: 1px solid #dde3e8; padding: 6px; font-size: 7.6pt; }}
ul, ol {{ margin: 4px 0; }}
li {{ margin: 1px 0; }}
table {{ border-collapse: collapse; width: 100%; margin: 6px 0; }}
th {{ background: #0b3d5c; color: #ffffff; font-size: 7.8pt; text-align: left; padding: 4px 5px; border: 0.5px solid #0b3d5c; }}
td {{ font-size: 7.8pt; padding: 3px 5px; border: 0.5px solid #cdd6dd; vertical-align: top; }}
tr:nth-child(even) td {{ background: #f6f8fa; }}
hr {{ border: none; border-top: 1px solid #d0d7dd; margin: 10px 0; }}
em {{ color: #555; }}
""".format(body=BODY_FONT)


def convert(src_path, out_path):
    with open(src_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "toc"],
    )
    html = (
        '<!DOCTYPE html><html><head><meta charset="utf-8">'
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )
    with open(out_path, "w+b") as out:
        result = pisa.CreatePDF(html, dest=out, encoding="utf-8")
    if result.err:
        raise RuntimeError("PDF generation reported errors")
    return out_path


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + ".pdf"
    convert(src, out)
    print(f"OK  font={BODY_FONT}  ->  {out}")


if __name__ == "__main__":
    main()
