# Prompt recipes

## Shared edit prompt

```text
Use case: ads-marketing
Asset type: Meta ad creative adaptation
Primary request: Adapt the attached finished ad into [TARGET FORMAT]. This is a layout adaptation, not a redesign or crop. [RATIO-SPECIFIC COMPOSITION]
Input image: Edit target and sole source of truth.
Style: Match the source exactly, including typography, palette, logo, lighting, graphic language, shadows, spacing rhythm, and hierarchy.
Text: Preserve every visible character verbatim. Do not paraphrase, correct, add, remove, or invent text, numbers, punctuation, labels, logo lettering, chart values, or UI copy.
Constraints: Do not stretch or simply crop. Intelligently reposition and proportionally resize elements. Preserve screenshots, UI, charts, product details, and brand marks. Maintain legibility and intentional spacing. No watermark.
```

## Ratio instructions

- **1:1 — 1080x1080:** Create a balanced square feed composition. Condense spacing only as needed. Preserve the original focal order.
- **4:5 — 1080x1350:** Create a true portrait feed composition. Expand vertical rhythm and reposition elements; do not merely add empty space.
- **9:16 — 1080x1920:** Create a true full-height Stories/Reels composition. Keep all critical copy, logos, UI, and CTA content in a central safe column with generous unobstructed space at the top and bottom.

## Focused retry

```text
Revise only the identified fidelity problem: [PROBLEM]. Preserve all other composition, copy, colors, imagery, and spacing unchanged. The corrected content must match the source image exactly.
```

