# Campaign build-spec template

This is the structure the final deliverable should follow. It is written so an
agent operating a Google Ads MCP can build the account top-down, field by field,
without re-deriving anything. Fill every section. Keep the "why" notes — they stop
the executing agent from making the common mistakes (optimizing to the wrong
conversion, leaving Search Partners on, over-broad geo).

Replace every `{PLACEHOLDER}`. Delete guidance in (parentheses) once filled.
Keep ad copy pre-validated against `ad-copy-rules.md`.

---

```markdown
# {Company} Google Search Campaign — Full Build Specification

**Prepared for:** {Company} ({domain})
**Date:** {date}
**Purpose:** Execution-ready build sheet to hand to the Google Ads MCP to
construct and launch the campaign field-by-field.
**Scope:** Google Search only. Priority categories: {list}.

## 0. How to use this document with the Google Ads MCP
(Short build order: account foundations → campaign shells → ad groups → keywords
→ RSAs → assets → negatives → tracking/QA. Note that all ad copy is pre-validated
to Google's limits and lists the house-style constraints applied.)

## 1. Positioning & strategy summary
### 1.1 What {Company} is  (one paragraph; the brand line / tagline)
### 1.2 The wedge (why we win the click)  (3–6 defensible, specific claims)
### 1.3 Buyer personas  (who we target; who we exclude)
### 1.4 Campaign architecture (and why)
(Table of campaigns. Default pattern: separate Brand from Nonbrand, and separate
each priority category into its own campaign for budget isolation and clean
measurement. Product/brand-name terms live in their category campaign mapped to
the exact product page; only the company name lives in the Brand campaign.)

## 2. Account-level foundations (build first)
### 2.1 Conversion actions
(Table: action | category | primary/secondary | count | click window | value |
notes. Only true business outcomes are Primary and feed bidding. Page views,
newsletter signups → Secondary/observation. Measurement is upstream of every
automated decision, so this is built before anything bids.)
### 2.2 Enhanced conversions for leads + offline import  (for lead-gen accounts)
### 2.3 Account settings  (auto-tagging ON; time zone; currency; final URL suffix)
### 2.4 Business information  (business name ≤25 chars; logo; verification)
### 2.5 Brand list  (for brand exclusions on nonbrand campaigns)

## 3. Campaign settings (applies to all unless noted)
(Table of settings. Sensible defaults for a lead-gen / considered-purchase build:
Search only; Search Partners OFF at launch; Display OFF; Presence-based location;
language matched to the offer; AI Max OFF at launch; final URL expansion OFF;
brand exclusion on nonbrand campaigns. Explain the AI Max-off rationale.)
### 3.1 Location targeting  (tiered list; presence, not presence-or-interest)
### 3.2 Budget  (per-campaign daily/monthly table; note ~2x daily / ~30.4x monthly)
### 3.3 Bid strategy phasing  (Phase 1 Manual CPC / capped Max Clicks to gather
clean data → Phase 2 Max Conversions → tCPA from observed CPA. Don't set an
aggressive target on day one; it starves a low-volume account before it learns.)

## 4..N. CAMPAIGN {n} — {Nonbrand/Brand} — {Category}
**Landing-page map**  (each ad group → one exact product URL)
### Ad Group {n.m} — {tight theme}
**Final URL:** {url}
**Display path:** /{≤15}/{≤15}
**Keywords**  (table: keyword | match type; exact + phrase to start; high-intent
bottom-of-funnel only)
**RSA — Headlines (15)**  (each ≤30 chars, distinct message functions)
**RSA — Descriptions (4)**  (each ≤90 chars, standalone)
**Pins:** (only if necessary)
(Repeat per ad group. Keep each ad group to one intent + one landing page.)

## Brand campaign
(Company-name terms only. Pin H1 to the official-site headline.)

## 7. Assets (extensions)
### 7.1 Sitelinks (≥6; text ≤25, two descriptions each)  (per-campaign emphasis)
### 7.2 Callouts (~10; ≤25 each)
### 7.3 Structured snippets (valid headers: Types, Service catalog, ...)
### 7.4 Call asset (phone; call reporting; count qualified calls as conversions)
### 7.5 Business name & logo
### 7.6 Image assets (≥4; square 1200x1200 + landscape 1200x628)
### 7.7 Lead form asset (optional; qualification questions only; measure quality)
### 7.8 Price / promotion assets (only with real prices / real dated offers)

## 8. Negative keywords
### 8.1 Shared "Universal Exclusions" list  (informational, careers, academic,
free/DIY, wrong-industry)
### 8.2 Category-specific negatives  (e.g. clinical/patient meanings, wrong senses
of an ambiguous product term)
### 8.3 Ambiguous-token disambiguation  (if a product term collides with unrelated
high-volume meanings, run that ad group exact/phrase only and negative the other
meanings; call this out explicitly)
### 8.4 Brand separation  (negative the company name on nonbrand campaigns so the
Brand campaign owns it; do NOT negative product names — they belong to their
category ad groups)

## 9. Tracking, URLs, and QA
### 9.1 Final URL suffix (UTMs via ValueTrack)   ### 9.2 Parallel tracking ON
### 9.3 Pre-launch URL QA  (every final URL 200 + correct page + tag fires)

## 10. Policy pre-flight
(Verification done; business name matches domain; every claim maps to a page
statement; no unsafe symbols; regulated-category review expectations.)

## 11. Phase 2 roadmap
(Smart Bidding move; audiences in Observation; test Search Partners; broad-match
experiment vs a stable control; AI Max pilot with URL inclusions + brand controls
+ text guidelines; geo expansion; secondary categories.)

## 12. Quick-reference build checklist  (tickable list of every step above)

## Appendix A — Landing-page URL reference  (every URL used, one table)
## Appendix B — Claim → source-page table  (each ad claim mapped to its evidence)
## Appendix C — Estimated volumes & CPCs  (planning only, if data available)
```

---

## Notes on adapting the template by objective

The default above is tuned for **lead generation / considered purchase** (B2B,
services, high-consideration). Adjust for other objectives — the field framework
reference has per-objective tables:

- **Ecommerce:** value-based bidding (Max Conversion Value / tROAS) with real
  transaction values; price and promotion assets; product-page landing.
- **Local / store visits:** tight radius or service-area targeting, presence
  based; location + call assets; accurate hours; store-visit or call conversions.
- **Brand visibility:** Target Impression Share only when there is a genuine
  visibility mandate; otherwise still optimize to conversions.

Whatever the objective: keep ad groups tight (one intent, one landing page),
validate every character limit, only Primary-mark true outcomes, and make every
claim substantiated.
