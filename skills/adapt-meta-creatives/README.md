# Adapt Meta Creatives

One flattened ad in. Three Meta-ready formats out. About five minutes.

## Why this exists

In 2020 I was running Meta ads out of Photoshop. Every ad needed multiple variations at different aspect ratios, the square for feed, the vertical for IG Stories, and each one meant adjusting every little element by hand. That was real design work, and it added up fast.

The next step was Canva, because it had a feature that auto-corrected to the aspect ratio. It was not perfect, but it got you 70% of the way there. We would move elements around to finish the job, and it probably cut the process down by an hour or so per ad.

This skill takes it down to about five minutes, and the output holds up every time. You hand it a finished PNG or JPEG with no editable layers, and it recomposes the ad into each format independently. Not a crop, not a stretch. A real layout adaptation that preserves the copy, the logo, the charts, the screenshots, and the spacing the designer intended.

## What you get

For every source ad:

| File | Format | Where it runs |
|------|--------|---------------|
| `1080x1080.png` | 1:1 | Feed |
| `1080x1350.png` | 4:5 | Portrait feed |
| `1080x1920.png` | 9:16 | Stories and Reels |
| `qa-report.md` | — | The receipts |

Each format is composed on its own, so the Story version actually uses the vertical space instead of floating a square in the middle of it. The 9:16 keeps critical content in a central safe column with clear space at the top and bottom for the interface overlays.

## The QA gates

Generation can drift, so every output gets checked before it is approved: exact copy and numbers, logo fidelity, screenshot and chart accuracy, colors, margins, hierarchy, and exact pixel dimensions. Anything that changed a logo, a legal line, a QR code, or a UI detail gets flagged for review instead of silently shipped.

## If the logo keeps changing

This is the most common issue. If your outputs come back with the product logo altered, upload the logo file alongside the source ad and the generation will hold it steady.

## What is in this folder

- [SKILL.md](SKILL.md) — the full workflow the agent follows, including the QA gates and delivery structure
- [references/prompts.md](references/prompts.md) — the edit prompts for each ratio and the focused retry prompt
- [scripts/finalize_meta_images.ps1](scripts/finalize_meta_images.ps1) — normalizes accepted outputs to exact delivery dimensions without distorting or cropping

Enjoy saving time.
