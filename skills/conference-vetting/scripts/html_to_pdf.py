#!/usr/bin/env python3
"""Render a dossier HTML file to a shareable PDF.

Usage:
    python3 html_to_pdf.py input.html output.pdf ["Footer label"]

Handles the two things that usually go wrong when printing a themed HTML page:
it forces the light palette (so a dark-mode host doesn't produce a black PDF),
and it adds print pagination rules so cards, tables and rows don't split across
pages. Requires playwright with chromium available.
"""
import sys, pathlib, re

PRINT_CSS = """
<style>
@page { size: Letter; margin: 0.55in 0.6in 0.7in 0.6in; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { background:#FFFFFF !important; font-size:10.3pt; line-height:1.5; }
.wrap, .container, main { max-width:none !important; padding-left:0 !important; padding-right:0 !important; }
h1 { font-size:38pt !important; }
h2 { font-size:19pt !important; }
h3 { font-size:12.5pt !important; }
p, li, td, dd, blockquote { font-size:10.3pt !important; }
table { font-size:9.4pt !important; min-width:0 !important; }
td, th { padding:8px 11px !important; font-size:9.4pt !important; }
*[class*="shadow"], .card, .panel, table, blockquote { box-shadow:none !important; }
section { margin-top:26pt; }
h1, h2, h3 { break-after:avoid; }
tr, blockquote, li, .card, .panel { break-inside:avoid; }
thead { display:table-header-group; }
a { text-decoration:none; }
</style>
"""


def build_print_doc(src_path: pathlib.Path) -> pathlib.Path:
    src = src_path.read_text()
    if "<body" in src.lower():
        # already a full document: just inject the print css before </head>
        doc = re.sub(r"</head>", PRINT_CSS + "</head>", src, count=1, flags=re.I)
        if PRINT_CSS not in doc:                      # no head to inject into
            doc = PRINT_CSS + src
    else:
        # artifact-style fragment: wrap it
        marker = '<div class="wrap">'
        head, _, body = src.partition(marker)
        doc = (
            '<!doctype html>\n<html lang="en" data-theme="light">\n<head>\n'
            '<meta charset="utf-8">\n' + head + PRINT_CSS +
            "</head>\n<body>\n" + (marker + body if body else src) + "\n</body>\n</html>"
        )
    out = src_path.with_name(src_path.stem + "-print.html")
    out.write_text(doc)
    return out


def render(src: str, dest: str, label: str = "") -> None:
    from playwright.sync_api import sync_playwright

    print_html = build_print_doc(pathlib.Path(src).resolve())
    footer = (
        '<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:7.5pt;'
        'color:#78838F;padding:0 0.6in;display:flex;justify-content:space-between;">'
        f"<span>{label}</span>"
        '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>'
        "</div>"
    )
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(color_scheme="light")
        page.goto(f"file://{print_html}", wait_until="networkidle")
        page.emulate_media(media="print", color_scheme="light")
        page.wait_for_timeout(1200)          # let webfonts settle
        page.pdf(
            path=dest,
            format="Letter",
            print_background=True,
            display_header_footer=bool(label),
            header_template="<div></div>",
            footer_template=footer,
            margin={"top": "0.55in", "bottom": "0.7in", "left": "0.6in", "right": "0.6in"},
        )
        browser.close()
    print(f"wrote {dest}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    render(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "")
