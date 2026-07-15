---
name: beehiiv-ad-campaign
description: >
  Build and format ad creative submissions for the beehiiv Ad Network. Use this skill whenever
  the user wants to create, draft, or prepare newsletter ad campaigns for beehiiv — including
  writing ad copy, formatting creative submissions, building campaign spreadsheets, or
  mapping existing ad assets to beehiiv's required form fields. Also trigger when the user
  mentions "beehiiv", "newsletter ads", "newsletter campaign", "ad creative submission",
  "newsletter ad network", or references running ads across newsletter publishers. This skill
  handles the full workflow: gathering campaign info, drafting or adapting ad copy to beehiiv's
  constraints, validating against word/character limits, structuring trackable URLs with UTM
  parameters, and producing a ready-to-submit XLSX spreadsheet.
---

# beehiiv Ad Network — Creative Submission Skill

This skill produces campaign spreadsheets formatted for beehiiv's Ad Network Creative Submission form. Each campaign submission includes campaign-level metadata and 6 ad units across 3 tiers.

## Workflow

Follow these steps in order. Do not skip the validation step.

### Step 1: Gather Campaign-Level Info

Collect or confirm these fields for each campaign:

| Field | Notes |
|---|---|
| Email | Submitter's email |
| Advertiser Name | Company or brand name |
| Campaign Name | Internal name (e.g., "Apply — Cohort 6") |
| Campaign Start Date | Format: Month Day, Year |
| Campaign End Date | Format: Month Day, Year |
| Primary Contact Name | Person beehiiv should contact |
| Primary Contact Email | Their email |
| Transparent Logo | Google Drive share link, PNG, 600×300px, transparent background |
| Total Budget | Dollar amount across all 6 ad units |
| Target Audience | Who should see these ads — job titles, geography, company profile, psychographic, newsletter targeting guidance |
| Notes for beehiiv team | Any context for the account manager |

If the user is running multiple campaigns simultaneously, note this in the "Notes for beehiiv team" field so the account manager has context.

### Step 2: Understand the 6 Ad Slots

Every beehiiv campaign submission includes exactly 6 ad units across 3 tiers. Each tier has different constraints:

#### Primary Ads (2 slots)
The highest-impact units. Include logo, hero image, headline, and long-form body copy.

| Field | Constraint |
|---|---|
| Creative Name | Short internal label (e.g., "Catalyst, June — Primary 1") |
| Headline | ≤ 10 words |
| Hero Image | Google Drive share link, PNG, 1200×600px |
| Body Copy | ≤ 150 words. Up to 2 hyperlinked phrases using `{{linked text}}` syntax |
| CTA Text | 3–5 words |
| Trackable URL | Must include `{{publication_alphanumeric_id}}` merge field |
| Optional Disclaimer | Leave blank if not needed |

#### Secondary Ads (2 slots)
Shorter, text-forward units. Hero image is optional.

| Field | Constraint |
|---|---|
| Creative Name | Short internal label |
| Headline | ≤ 10 words |
| Hero Image | Optional. Same specs as Primary if included |
| Body Copy | ≤ 50 words. Up to 2 hyperlinked phrases using `{{linked text}}` syntax |
| CTA Text | 3–5 words |
| Trackable URL | Must include `{{publication_alphanumeric_id}}` merge field |
| Optional Disclaimer | Leave blank if not needed |

#### Text-Only Secondary Ads (2 slots)
No image, no headline. Copy-only with a CTA.

| Field | Constraint |
|---|---|
| Creative Name | Short internal label |
| Body Text | ≤ 200 characters. Up to 2 hyperlinked phrases using `{{linked text}}` syntax |
| CTA Text | 3–5 words |
| Trackable URL | Must include `{{publication_alphanumeric_id}}` merge field |

### Step 3: Draft or Adapt Ad Copy

When the user provides source material (website copy, case studies, transcripts, existing ad copy from other platforms), draft body copy that fits beehiiv's constraints. Key principles:

- **Always introduce the product/program before citing results.** A newsletter reader has no context. Explain what the thing is before telling them what it achieved.
- **Respect word and character limits strictly.** Count words/characters for every ad and include the count in the output.
- **Hyperlink syntax:** Wrap linked phrases in double curly braces: `{{linked text}}`. The destination is set via the Trackable URL field. Use natural link anchors like the brand name, "Learn more", "Apply now", or "Get started" — max 2 per ad.
- **CTA text must be 3–5 words.** Single-word CTAs like "Apply" are too short.
- **Headlines must be ≤ 10 words.** If a provided headline exceeds 10 words, trim it and note the change.
- **Case study usage:** When incorporating case studies, limit to 1 case study per ad. If the user wants multiple case studies, distribute them across different ad slots rather than stacking them in one ad.
- **Evergreen vs. time-bound:** Consider which ads should reference specific dates/cohorts (time-bound) vs. being reusable (evergreen). Ask the user if this isn't clear.

### Step 4: Structure Trackable URLs

Every ad needs a trackable URL containing beehiiv's required merge field. Build URLs like this:

```
https://[destination]?utm_campaign={{publication_alphanumeric_id}}&utm_source=beehiiv&utm_medium=newsletter&utm_content=[unique_id]
```

- `{{publication_alphanumeric_id}}` is required by beehiiv — it auto-populates with each publisher's unique ID at send time
- `utm_content` should be unique per ad so the user can track which copy/creative performed best (e.g., `primary1_copyB`, `secondary2_immersion`, `textonly1`)
- Ask the user if they want additional UTM parameters beyond campaign, source, medium, and content

### Step 5: Allocate Budget

If the user provides a total budget, allocate across the 6 ad units using this default split unless they specify otherwise:

| Tier | % of Total | Per Ad |
|---|---|---|
| Primary Ads (×2) | 50% | 25% each |
| Secondary Ads (×2) | 30% | 15% each |
| Text-Only Secondary (×2) | 20% | 10% each |

This weights spend toward the highest-impact ad units. Always include a SUM formula in the budget total row so the user can adjust individual amounts and verify the total.

### Step 6: Validate Before Building

Before generating the spreadsheet, check every ad unit against these rules:

- [ ] Headlines ≤ 10 words
- [ ] Primary body copy ≤ 150 words
- [ ] Secondary body copy ≤ 50 words
- [ ] Text-Only body text ≤ 200 characters
- [ ] CTA text is 3–5 words
- [ ] Trackable URLs include `{{publication_alphanumeric_id}}`
- [ ] Each `utm_content` value is unique across all 6 ads
- [ ] No more than 2 `{{hyperlinked phrases}}` per ad
- [ ] Google Drive links for logo and hero images are share links (not edit links)
- [ ] Text-Only ads have "N/A" for Headline and Hero Image fields

If any field is missing (e.g., hero image not yet created), use a red-font placeholder like `[PLACEHOLDER — Upload hero image to Google Drive and paste share link here]` so it's visually obvious in the spreadsheet.

### Step 7: Generate the XLSX

Read `/mnt/skills/public/xlsx/SKILL.md` before building. Produce an XLSX workbook with 2 tabs:

**Tab 1: Campaign Info**
- Two columns: Field Label (col A, bold) and Value (col B)
- Include all campaign-level fields from Step 1
- Column widths: A=32, B=100
- Use thin borders on all cells, wrap text alignment

**Tab 2: Ad Units**
- One row per ad unit (6 rows of data + header row)
- Columns: Ad Slot, Creative Name, Headline, Hero Image, Body Copy, Word/Char Count, CTA Text, Trackable URL, Optional Disclaimer, Budget
- Header row: white text on dark fill (#1A1A2E), frozen
- Alternating row fills for readability
- Budget column formatted as currency ($#,##0)
- Row height ~140 for body copy readability
- TOTAL row at bottom with SUM formula for budget column
- Red font on any placeholder values so they stand out

After generating, run the recalculation script:
```bash
python3 /mnt/skills/public/xlsx/scripts/recalc.py [path_to_file]
```

Copy to `/mnt/user-data/outputs/` and present via `present_files`.

## Asking Good Questions

When the user provides campaign information, identify gaps and ask about them in a single organized pass rather than one at a time. Common gaps:

- Destination URL (what page should ads link to?)
- Campaign dates (start and end)
- Budget (total amount to allocate)
- CTA direction (what should the button say?)
- Hero image and logo Drive links
- Target audience (who should see these ads?)
- Whether copy should be evergreen or time-bound

If the user provides existing ad copy from another platform (e.g., Meta ads), note that newsletter ads are a different format — word limits are strict, images don't have text overlays, and the audience may need different messaging than social.

## Multiple Campaigns

When running multiple campaigns in a single session, produce a separate XLSX per campaign. Each one is self-contained with its own Campaign Info and Ad Units tabs. Name files distinctly (e.g., `gauntlet_apply_campaign.xlsx`, `gauntlet_catalyst_campaign.xlsx`).

If all campaigns share a logo, contact info, or other fields, reuse them across files without re-asking.
