#!/usr/bin/env python3
"""Validate a YouTube SEO package against YouTube's hard limits.

Usage:  python validate_package.py <package.md>

Exits 1 if any ERROR is found. WARNs don't fail the run but should be read.

The limits here are the ones YouTube enforces *silently* — it won't tell you
your hashtags were ignored, it just ignores them. That's why this exists.
"""
import re
import sys
from pathlib import Path

ERRORS: list[str] = []
WARNS: list[str] = []


def err(msg: str) -> None:
    ERRORS.append(msg)


def warn(msg: str) -> None:
    WARNS.append(msg)


def section(text: str, heading: str) -> str:
    """Grab the body of a '## N. Heading' section, up to the next '## '."""
    pat = rf"^##\s*\d*\.?\s*{heading}.*?$(.*?)(?=^##\s|\Z)"
    m = re.search(pat, text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ""


def check_titles(text: str) -> None:
    body = section(text, "Title")
    if not body:
        err("No '## Title options' section found.")
        return
    # Titles look like:  1. **Some Title** (52 chars)  — or bare quoted lines
    titles = re.findall(r"^\s*\d+\.\s*\**\"?(.+?)\"?\**\s*(?:\(|—|$)", body, re.MULTILINE)
    titles = [t.strip() for t in titles if t.strip()]
    if not titles:
        warn("Couldn't parse any titles — check formatting (expect '1. **Title**').")
    if len(titles) < 5:
        warn(f"Only {len(titles)} titles found; the skill asks for 7.")
    for t in titles:
        n = len(t)
        if n > 100:
            err(f"Title over 100 chars ({n}): {t[:60]}...")
        elif n > 70:
            warn(f"Title is {n} chars — truncates on mobile (~60): {t[:60]}...")


def check_description(text: str) -> None:
    body = section(text, "Description")
    if not body:
        err("No '## Description' section found.")
        return
    blocks = re.findall(r"```[a-z]*\n(.*?)```", body, re.DOTALL)
    if not blocks:
        warn("Description isn't in a fenced code block — it should be, for clean copy-paste.")
        desc = body
    else:
        desc = max(blocks, key=len)

    n = len(desc)
    if n > 5000:
        err(f"Description is {n} chars, over the 5000 limit.")
    if n < 300:
        warn(f"Description is only {n} chars — thin. Below-fold text does indexing work.")

    first = desc.strip().split("\n")[0]
    if len(first) > 120:
        warn(f"First line is {len(first)} chars; only ~120 show before '...more'.")
    if re.match(r"^\s*in this video", first, re.IGNORECASE):
        warn("Description opens with 'In this video' — wastes the highest-value characters.")


def check_tags(text: str) -> None:
    body = section(text, "Tags")
    if not body:
        err("No '## Tags' section found.")
        return
    blocks = re.findall(r"```[a-z]*\n(.*?)```", body, re.DOTALL)
    raw = blocks[0] if blocks else body
    raw = re.sub(r"^\s*[-*]\s*", "", raw, flags=re.MULTILINE)
    tags = [t.strip() for t in raw.replace("\n", ",").split(",") if t.strip()]
    tags = [t for t in tags if not t.startswith("#") and len(t) < 80]
    if not tags:
        warn("Couldn't parse tags.")
        return
    total = sum(len(t) for t in tags) + max(0, len(tags) - 1)  # commas
    if total > 500:
        err(f"Tags total {total} chars across {len(tags)} tags — over the 500 limit.")
    if len(tags) < 10:
        warn(f"Only {len(tags)} tags; 15-25 is the target.")


def check_hashtags(text: str) -> None:
    tags = re.findall(r"(?<!\w)#(\w+)", section(text, "Hashtag"))
    if not tags:
        warn("No hashtags found.")
        return
    if len(tags) > 15:
        err(f"{len(tags)} hashtags — over 15 means YouTube ignores ALL of them.")
    elif len(tags) != 3:
        warn(f"{len(tags)} hashtags; only the first 3 render above the title.")


def _secs(ts: str) -> int:
    parts = [int(p) for p in ts.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def check_chapters(text: str) -> None:
    body = section(text, "Chapter")
    if not body:
        err("No '## Chapters' section found.")
        return
    rows = re.findall(r"^\s*[-*]?\s*((?:\d+:)?\d{1,2}:\d{2})\s+(.+?)\s*$", body, re.MULTILINE)
    if not rows:
        err("No chapter timestamps parsed.")
        return
    if len(rows) < 3:
        err(f"Only {len(rows)} chapters — YouTube needs at least 3 or none appear.")
    if rows[0][0] not in ("0:00", "00:00", "0:00:00"):
        err(f"First chapter must be 0:00, found {rows[0][0]}.")

    secs = [_secs(ts) for ts, _ in rows]
    for i in range(1, len(secs)):
        if secs[i] <= secs[i - 1]:
            err(f"Chapters out of order at '{rows[i][1]}' ({rows[i][0]}).")
        elif secs[i] - secs[i - 1] < 10:
            err(f"Chapter '{rows[i][1]}' is under 10s long — chapters will not appear.")

    generic = {"intro", "introduction", "outro", "conclusion", "main content",
               "wrap up", "wrap-up", "q&a", "questions", "overview", "summary"}
    for _, title in rows:
        if title.strip().lower().strip("*_ ") in generic:
            warn(f"Chapter '{title.strip()}' is generic — chapters get indexed as searches.")

    if len(rows) > 12:
        warn(f"{len(rows)} chapters — over ~12 each is too granular to be a real query.")


def check_sections(text: str) -> None:
    for name in ["Keyword", "Thumbnail", "Pinned comment", "Shorts"]:
        if not section(text, name):
            warn(f"Missing '{name}' section.")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: validate_package.py <package.md>")
        return 2
    p = Path(sys.argv[1])
    if not p.exists():
        print(f"No such file: {p}")
        return 2
    text = p.read_text(encoding="utf-8")

    for fn in (check_titles, check_description, check_tags,
               check_hashtags, check_chapters, check_sections):
        fn(text)

    for w in WARNS:
        print(f"WARN   {w}")
    for e in ERRORS:
        print(f"ERROR  {e}")

    print()
    if ERRORS:
        print(f"FAILED — {len(ERRORS)} error(s), {len(WARNS)} warning(s). Fix errors before delivering.")
        return 1
    print(f"PASSED — 0 errors, {len(WARNS)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
