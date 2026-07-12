---
name: adapt-meta-creatives
description: Adapt flattened PNG or JPEG ad creatives into Meta-ready 1080x1080, 1080x1350, and 1080x1920 variants using image-to-image generation, exact-size finishing, safe-area composition, fidelity checks, and review flags. Use when Codex needs to process one ad or a folder of ads without editable design layers while preserving copy, branding, typography, colors, logos, charts, product imagery, and screenshots.
---

# Adapt Meta Creatives

Create three independently composed variants per source ad. Never derive all formats by cropping or stretching one generated result.

## Workflow

1. Inventory source PNG/JPEG files and create one output folder per ad.
2. Inspect every source visually. Record exact copy, logo, UI values, chart labels, hierarchy, palette, and high-risk regions.
3. Treat the source as the edit target and sole visual source of truth. Use the built-in image-generation/editing capability unless the user explicitly requests an API or CLI implementation.
4. Generate each ratio independently using the appropriate prompt from [references/prompts.md](references/prompts.md).
5. Preserve every visible character verbatim. Do not paraphrase, correct, add, remove, or invent text, numbers, punctuation, labels, or logo lettering.
6. Keep logos, UI screenshots, QR codes, product packaging, legal copy, and small icons unchanged. If generation alters them, flag the output. Do not silently approve it.
7. For 9:16, place critical content in a central safe column with generous clear space at the top and bottom for Stories/Reels interface overlays.
8. Normalize accepted outputs to the exact delivery dimensions with `scripts/finalize_meta_images.ps1`. Fit proportionally onto a sampled-background canvas; never distort or crop.
9. Run the QA checks below and write `qa-report.md` or `qa-report.json` beside the outputs.
10. Deliver outputs in this structure:

```text
output/
  ad-name/
    1080x1080.png
    1080x1350.png
    1080x1920.png
    qa-report.md
```

## QA gates

Check every result for:

- Exact copy and numeric values
- Logo and brand-mark fidelity
- Screenshot/UI fidelity
- Chart geometry and labels
- Color and typography consistency
- Clipping, collisions, and minimum margins
- Visual hierarchy and intentional spacing
- 9:16 safe-area placement
- Exact pixel dimensions

Mark `review required` when any critical text, UI, logo, chart, icon, QR code, legal line, or product detail changes. Mark `cannot adapt cleanly` after two focused retries fail or when preserving all content would make the design unreadable.

## Production rules

- Use one generation call per ad and ratio.
- Prefer low-complexity drafts only for exploration; use the highest practical quality for final assets.
- Keep generated originals and exact-size delivery files separate.
- Never claim pixel-perfect preservation based only on visual plausibility.
- Automatically approve only outputs that pass all critical QA gates.
- Explain failures plainly and retain the best candidate for review.

