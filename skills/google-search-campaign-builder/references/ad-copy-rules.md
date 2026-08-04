# Ad copy rules — RSA limits, house style, and validation

The single most common way a Search build fails review or wastes effort is ad
copy that violates a character limit or trips an editorial policy. Get this right
the first time. Every headline and description you write must be validated before
it goes in the build spec.

## Hard character limits (count characters, including spaces)

| Element | Limit | Count / notes |
|---|---|---|
| RSA headline | **30 chars** | 3–15 per ad. Supply all 15 — more assets = more combinations Google can test. |
| RSA description | **90 chars** | 2–4 per ad. Supply all 4. Each must stand alone as a complete thought. |
| Display path (2 fields) | **15 chars each** | Descriptive, need not be a real folder. |
| Sitelink text | **25 chars** | Build ≥6. |
| Sitelink description (2 lines) | **~35 chars each** | Fill both to unlock richer formats. |
| Callout | **25 chars** | Supply ~10. |
| Structured snippet value | short | ≥3 values, 4+ recommended. Use a valid header (see below). |
| Business name | **25 chars** | Must match the domain / verified identity. |
| Promotion text fields | short | Only if a real dated offer exists. |

**Validation is not optional.** Before finalizing, count every headline and
description. A reliable way: write them out, then check each length
programmatically rather than by eye — off-by-one errors are easy to miss and
Google will silently truncate or reject. A tiny script is worth it:

```python
H = ["Recombinant Human Albumin", "rHSA Supplier in the USA", ...]
D = ["Recombinant human albumin, animal-origin-free and chemically defined."]
for h in H:
    assert len(h) <= 30, (len(h), h)
for d in D:
    assert len(d) <= 90, (len(d), d)
print("all headlines/descriptions within limits")
```

## House style (unless the client specifies otherwise)

The default voice for B2B / considered-purchase advertising is **plain, factual,
specification-driven**. It earns trust with buyers who evaluate on specs, not
adjectives. Apply these defaults, but always honor an explicit client style guide
over them:

- **No emojis.**
- **No em dashes (—).** Use short sentences or commas. (Em dashes also render
  inconsistently and read as AI-generated to many buyers.)
- **Avoid filler buzzwords:** unlock, leverage, transform, revolutionize,
  game-changer, cutting-edge, best-in-class, world-class, seamless (as filler),
  synergy, empower, supercharge. These are low-information and often trip
  "gimmicky" editorial flags. Say the actual spec instead.
- **No ad-unsafe symbols inside headlines/descriptions:** avoid ≤, ≥, µ, ×, ®, ™,
  and non-ASCII punctuation. Google's editorial policy restricts symbol use and
  they can cause disapprovals. Write "at or below 0.01 EU/ug", "about 100x",
  "greater than 99%". Keep the accurate symbols for the landing page and the
  claim-source table, not the ad.
- **No phone numbers in ad text** — use a call asset.
- **No excessive capitalization, repetition, or gimmicky spacing.**
- **Every claim must be substantiated on the destination page** (see §Claims).

## Each headline should do a distinct job

Fifteen near-duplicate headlines waste the format. Google assembles combinations,
so give it genuinely different building blocks. Aim to cover these message
functions across the 15 headlines:

| Function | Example |
|---|---|
| Intent confirmation (echo the query) | `Recombinant Human Albumin` |
| Product / service specificity | `Cell Culture Albumin` |
| Benefit | `Consistent Lot-to-Lot rHSA` |
| Proof / evidence | `Used in Approved Biologics` |
| Spec / number | `Greater Than 99% Purity` |
| Offer / next step (CTA) | `Request Bulk Pricing` |
| Risk reversal | `No TSE/BSE, No Donor Risk` |
| Brand / origin | `Made in the USA` |

Descriptions: write 4 that each stand alone, lead with the strongest concrete
fact, and end at least one with a clear call to action ("Request pricing.",
"Request a quote.").

## Pins — use sparingly

Pinning locks a headline/description to a position and reduces the combinations
Google can test. Pin only when necessary:

- Brand campaigns: pin the brand/official-site headline to position 1.
- Legal/regulatory disclaimers: pin to a description slot (or use a dedicated
  text-disclaimer asset).
- Otherwise, leave unpinned. If you pin, pin 2–3 assets to the same slot so
  there's still variety.

## Structured snippet headers (must be a valid Google header)

Valid headers include: Amenities, Brands, Courses, Degree programs, Destinations,
Featured hotels, Insurance coverage, Models, Neighborhoods, Service catalog,
Shows, Styles, Types. "Applications", "Products", "Features" are **not** valid.
For a product portfolio use **Types**; for solution areas use **Service catalog**.

## Display path

Two 15-char fields after the visible domain. Use them to reinforce intent, e.g.
`/Recombinant/Albumin` or `/OptiLeukin-2/IL-2`. They don't need to be real URL
folders, but must not imply a destination the page doesn't deliver.

## Claims discipline (regulated and considered-purchase categories)

For life sciences, finance, health, legal, and any category with claims, every
spec or superlative in the copy must map to a statement on the destination page.
Build a small "claim → source page" table in the output spec so the reviewer (and
the ad reviewer at Google) can see the substantiation. Never invent a number,
certification, award, or "#1 / only / best" claim the site does not support.
