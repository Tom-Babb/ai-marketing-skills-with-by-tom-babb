---
name: google-search-campaign-builder
description: >-
  Build a complete, execution-ready Google Search Ads campaign specification for
  any company from their website, delivered as a Markdown + PDF build sheet that
  can be handed to a Google Ads MCP (or a human) to construct and launch the
  campaign field-by-field. Use this whenever the user wants to create, build,
  plan, set up, or launch a Google Search / Google Ads / paid search / SEM
  campaign, wants ad copy (responsive search ads, headlines, descriptions),
  keyword + match-type plans, negative keywords, ad extensions/assets, bidding
  and budget settings, conversion tracking setup, or a campaign "build spec" or
  "media plan" for Google. Trigger it even when the user only names one piece
  ("write me some Google search ads for X", "what keywords should I bid on",
  "set up conversion tracking for my site") — the full build sheet is almost
  always what they actually need. Also trigger when a user hands over a company
  URL and asks to advertise it on Google, or wants to feed a plan into a Google
  Ads / Google Search MCP. Works for any industry (B2B, ecommerce, local,
  services). Not for Meta/Facebook, LinkedIn, TikTok, YouTube/Display, or
  organic SEO — this is Google Search paid campaigns only.
---

# Google Search Campaign Builder

## What this produces

A single, thorough **build specification** — delivered as both `.md` and `.pdf` —
that contains every field, setting, keyword, ad, asset, and negative needed to
stand up a Google Search campaign, written so a Google Ads MCP or a human media
buyer can execute it top-down without guessing. The InVitria build this skill was
distilled from ran ~13 PDF pages: 3 campaigns, tight ad groups each mapped to one
landing page, 15 character-validated headlines + 4 descriptions per ad group, a
layered negative strategy, full asset set, conversion/bidding/tracking settings,
and a policy pre-flight.

The value is in being **complete and correct**: measurement defined before
bidding, ad copy that passes character limits and editorial policy on the first
try, keywords that match real buyer intent, and every claim tied to something on
the client's site.

## The bundled resources — read these at the right moments

- **`references/google-ads-field-framework.md`** — the vendor-neutral 2026 catalog
  of every editable Google Search object plus the audit logic. This is the source
  of truth for *what fields exist and how they interact*. Consult it when deciding
  settings (bidding families, location options, budget mechanics, asset types,
  match-type behavior, AI Max, conversion/attribution) and when you need the
  authoritative limit or default. You don't need to read it end-to-end every time;
  jump to the "Master editable-field inventory" and "Audit checklist" tables.
- **`references/discovery-checklist.md`** — what to gather from the user and the
  website before building. Read at the start.
- **`references/ad-copy-rules.md`** — character limits, house style, banned words,
  structured-snippet headers, and the validation step. Read before writing any RSA.
- **`references/campaign-build-template.md`** — the exact structure of the output
  deliverable. Follow it when writing the spec.
- **`scripts/md2pdf.py`** — converts the finished `.md` spec into a clean PDF.

## Workflow

Work through these phases in order. Earlier phases feed later ones, so don't jump
to writing ads before you understand the positioning.

### Phase 1 — Discovery
Read `references/discovery-checklist.md`. Establish: the website URL, priority
products/categories, geography, budget, what counts as a conversion, and any house
-style constraints. Ask the user only for what you genuinely can't infer and that
would change the build; otherwise research it and state your assumption. A good
default with a stated assumption beats making the user answer twenty questions.

If the user gave you research documents, keyword lists, or a strategy doc, mine
them — but verify anything client-specific against the live site (docs go stale).

### Phase 2 — Website research (this is what makes the ads good)
Fetch the homepage and the key product/category pages (WebFetch is ideal; use
WebSearch or `site:domain product` to locate exact URLs). Extract:
- the exact positioning language, tagline, and repeated value-prop words,
- the **wedge**: specific, defensible differentiators that beat bigger competitors
  (certifications, proprietary tech, regulatory precedent, spec numbers, scale,
  guarantees, origin),
- exact **landing-page URLs** for each priority product and for the quote/contact,
  quality/compliance, catalog, and privacy pages,
- hard specs (numbers, grades, formats) you can turn into spec headlines,
- the business name and phone number for assets.

Echo the site's own strong language in the ad copy. Buyers trust copy that sounds
like the specs on the page, not generic marketing.

### Phase 3 — Strategy & architecture
Decide the campaign structure. The reliable default:
- **Separate Brand from Nonbrand** (brand is cheap, high-intent, and would distort
  nonbrand economics if mixed in).
- **One campaign per priority category** for budget isolation and clean data.
- **Tight ad groups:** one intent, one landing page each. Product/brand-name terms
  live in their category campaign mapped to the exact product page; only the
  company name lives in the Brand campaign.
Name the buyer personas to target and — just as important — who to exclude; the
exclusions become the negative strategy.

### Phase 4 — Keywords
Per ad group, choose high-intent, **bottom-of-funnel** keywords (supplier, buy,
price, quote, "for {application}", product names). Start with **exact + phrase**
for control; note broad match as a Phase-2 experiment, not a launch default.
Watch for **ambiguous tokens** (a product term that collides with unrelated
high-volume meanings, e.g. "LIF" = life insurance): run those exact/phrase only
and plan heavy negatives.

### Phase 5 — Ad copy (RSAs)
Read `references/ad-copy-rules.md` first. For each ad group write **15 headlines
(≤30 chars) and 4 descriptions (≤90 chars)**, each headline doing a distinct job
(intent echo, spec, benefit, proof, offer, risk reversal, origin). Apply house
style (no emojis, no em dashes, no banned buzzwords, no ad-unsafe symbols like ≤ µ
× ® — spell them out). **Then validate every length**, ideally with a quick script,
because Google silently truncates or rejects over-limit assets. This validation
step is what let the reference build pass on the first try.

### Phase 6 — Negatives, assets, settings
- **Negatives:** a universal exclusions list (informational, careers, academic,
  free/DIY, wrong-industry) + category-specific + ambiguous-token disambiguation +
  brand separation (negative the company name on nonbrand campaigns).
- **Assets:** sitelinks (≥6), callouts (~10), structured snippets (valid header),
  call asset, business name + logo, image assets, optional lead form. Character
  limits in `ad-copy-rules.md`.
- **Settings** (consult the field framework for specifics): conversion actions
  with only true outcomes marked Primary; enhanced conversions + offline import for
  lead gen; Search only, Partners OFF at launch, Display OFF; presence-based
  location; language matched to the offer; AI Max and final-URL expansion OFF at
  launch (explain why); budget per campaign; bid-strategy phasing (Manual/capped to
  gather data → Smart Bidding → tCPA from observed CPA); UTM tracking.

Tune the defaults to the objective — ecommerce wants value-based bidding and price
assets; local wants radius targeting and location/call assets. The field framework
has per-objective tables.

### Phase 7 — Assemble the deliverable
Write the full spec to a `.md` file following `references/campaign-build-template.md`.
Include Appendix A (every landing-page URL), Appendix B (claim → source-page table
so each ad claim's evidence is visible), and a build checklist. Verify each final
URL resolves (HTTP 200, correct page); flag any URL you had to infer.

### Phase 8 — Generate the PDF and deliver
Ensure deps are present, then convert:

```bash
python -m pip install --quiet markdown xhtml2pdf   # if not already installed
python scripts/md2pdf.py "<path>/{Company}_Google_Search_Campaign_BUILD.md"
```

The script auto-derives the `.pdf` path and registers a Unicode font so specs and
symbols render without replacement characters. Deliver both files to the user
(SendUserFile if available), and give a short summary of what was built plus any
URLs the user should double-check.

## Guardrails and quality bar

- **Measurement before bidding.** If conversion tracking is wrong, every automated
  decision optimizes toward the wrong outcome. Define conversions first.
- **Never invent claims.** No certification, award, "#1 / only / best", or spec the
  site doesn't support. Regulated categories (health, finance, legal, life
  sciences) especially — map every claim to a page statement.
- **Validate every character limit.** Non-negotiable; it's the top cause of rework.
- **Every landing page must resolve and match intent.** A 404 or off-topic page is
  wasted spend and a policy risk.
- **Keep ad groups tight.** One intent, one landing page. Sprawling ad groups
  produce weak Quality Scores and irrelevant matches.
- **Recommend, don't hedge.** Give concrete defaults (budgets, geos, bid strategy)
  with the reasoning, so the user can execute or adjust — not a menu of options.
