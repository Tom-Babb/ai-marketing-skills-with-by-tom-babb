---
name: og-image-system
description: Design a consistent, on-brand Open Graph (OG) image system across every page of a site instead of one-off social cards. Use this skill whenever someone needs OG / social share images, link preview images, Twitter/X cards, or a thumbnail that shows up when a URL is pasted into LinkedIn, Slack, iMessage, or X. Triggers include "make an OG image," "our links look bad when shared," "we need social share images," "build link previews for the whole site," "design a social card," or any request to control how pages look when shared. The core move is segmentation: route each page to a visual treatment based on who the page is for, rather than designing each card from scratch.
---

# OG Image System

An OG image is the picture that shows up when a link gets pasted anywhere — LinkedIn, X, Slack, iMessage, a Discord channel. Most sites either have none (so the link renders as a gray box) or have one generic card slapped on every page. Both are a wasted impression. Every shared link is a free ad placement, and most companies leave it blank.

The mistake people make is treating each card as a one-off design problem. The win is treating it as a *system*: decide the rules once, route every page through them, and produce the whole set in an afternoon. The rule that does the heavy lifting is segmentation — who is this page for — because that one answer decides the look.

## The core idea

Do not design OG images page by page. Build a decision table, then execute it.

You need exactly three decisions per page, and the first one drives the other two:

1. **Audience** — who lands on this page? (the segment)
2. **Mode** — what visual treatment does that segment get? (derived from audience)
3. **Real people?** — does this page carry a real photo, or is it brand-only?

Once the table is filled in, generation is mechanical. The thinking is all in the segmentation.

---

## The workflow

### Step 1 — Inventory every public page

Pull the full list of URLs you want to control. Sitemap, `robots.txt`, or a crawl all work. Include landing pages and subdomains, not just the main nav. Flag anything internal or `disallow`-ed in robots — those usually don't need a public OG image, and you skip them rather than design for them.

The output of this step is a row per URL.

### Step 2 — Tag each page with its audience

This is the only judgment call in the whole process. For each page, answer: who is this page actually for?

Most sites collapse into a small number of segments. For a two-sided business it's usually some version of:

- **Demand side / B2B** — the people who buy, hire, or sponsor (hiring partners, corporate buyers, funds)
- **Supply side / individual** — the people who apply, join, or learn (applicants, students, members)
- **Universal** — pages that serve everyone (home, pricing, privacy, program overviews)
- **Internal / unknown** — flag and confirm before designing, or skip

If you can't decide which segment a page belongs to, it's probably universal.

### Step 3 — Derive the mode from the audience

Mode is the visual treatment. Pick a small, fixed set of modes — two is ideal — and bind each one to a segment so the choice is automatic, not aesthetic. The point of binding it to audience is that a person scanning their feed gets a consistent signal: this style means "for me."

A clean default split:

| Audience | Mode |
|----------|------|
| B2B / demand-side (hiring partners, corporate, PE/VC) | **Dark** |
| Applicant / individual / member facing | **Light** |
| Universal (serves multiple audiences) | **Light** |

Dark reads as enterprise and serious; light reads as open and aspirational. The specific colors matter less than the consistency — every B2B link looks like a set, every applicant link looks like a set.

### Step 4 — Decide real people vs. brand-only

Third column. Three values:

- **Yes** — use a real photo of real people. Default for pages that already have a strong human hero (apply pages, case studies, instructor/speaker shots, partner testimonials). Real faces outperform graphics on social.
- **Optional** — works with or without. Use a photo if you have a good one, fall back to brand graphic if not.
- **No** — brand/graphic only. Right for legal, contact forms, and pure-CTA pages where a photo would feel arbitrary.

For case studies and proof pages, prefer **real partner or testimonial people** plus a result stat — that combination is the highest-performing OG card you can make.

### Step 5 — Capture image direction per page

For each row, write one line of art direction pulled from the page's *existing* hero or content. You're not inventing a concept — you're describing what's already working on the page so the card matches the destination. Pair it with the page's own headline where one exists ("Stop Waiting. Start Shipping.").

This is reverse prompting applied to OG images: start from what the page already shows, describe it, and generate from that description. (See the **reverse-prompting-for-image-gen** skill for the full technique.)

### Step 6 — Generate the set

Lock a template per mode so every card in a mode is visually identical except for the variable content. A template fixes: background treatment, logo placement, type system, safe margins, and aspect ratio. You swap only the headline, the photo (or not), and any stat.

- **Aspect ratio:** 1200 × 630 px is the standard OG size (1.91:1). It renders correctly on LinkedIn, X, Facebook, and Slack.
- **Safe zone:** keep the logo and headline away from the edges — some platforms crop. Center the critical 1200 × 600 region.
- **Text:** large enough to read as a thumbnail. If you can't read the headline at the size of a feed preview, it's too small.
- **Tools:** Claude Design (or any design tool) to build the two templates, then batch the variants. Generate or source the photos with your normal image pipeline.

Build the two mode templates first, get sign-off on those, *then* mass-produce. Don't design 20 cards and discover the template was wrong on card 19.

### Step 7 — Wire up the tags and verify

Each page needs the meta tags pointing at its image:

```html
<meta property="og:image" content="https://yoursite.com/og/page-name.png" />
<meta property="og:title" content="Page Title" />
<meta property="og:description" content="One line." />
<meta name="twitter:card" content="summary_large_image" />
```

Then verify before you call it done. Paste the live URL into:

- LinkedIn Post Inspector
- X / Twitter Card Validator
- An actual Slack or iMessage message (the real test)

Platforms cache OG images aggressively. If you update an image, use the platform's inspector to force a re-scrape, or it'll keep serving the old one for days.

---

## Worked example — GauntletAI rollout

This is the actual segmentation I ran across the GauntletAI site. Two modes (dark for B2B, light for applicant/universal), real-people flag per page, direction pulled from each page's existing hero.

| Page | Audience | Mode | Real People? | Direction |
|------|----------|------|--------------|-----------|
| Home | Universal | Light | Yes | Hero crowd of challengers / Austin space; logo mark over warm bg |
| Privacy Policy | Universal | Light | No | Clean brand-only layout, logo + title |
| Program Overview | Universal | Light | Optional | Split visual hinting both programs |
| Apply — Fellowship | Applicant | Light | Yes | Fellows on laptops in Austin; "Stop Waiting. Start Shipping." |
| Night School | Applicant | Light | Yes | Speaker mid-lecture or class audience shot |
| See What They Build | Champion | Light | Optional | Challenger portrait + project screenshot, or project grid |
| Champions Registration | Champion | Light | Yes | Aspirational single challenger / "become a champion" energy |
| Hire Proven Talent | B2B — Hiring | Dark | Yes | Confident engineer headshots / talent roster; dark hero |
| Catalyst — Upskill Teams | B2B — Corporate | Dark | Optional | Engineering team in workshop/immersive; dark |
| PE & VC Training | B2B — PE/VC | Dark | Optional | Executive/boardroom or portfolio-scale graphic; dark |
| Hire Case Studies | B2B — Hiring | Dark | Yes | Partner leader portrait + result stat (Zapier, SkyFi, Splash) |
| Catalyst Case Studies | B2B — Corporate | Dark | Yes | Engineer testimonial portrait + result (Rev.io, Pilotbase) |
| Hiring Partner Contact | B2B — Hiring | Dark | No | Brand-only CTA layout; dark |
| Catalyst / PE & VC Contact | B2B | Dark | No | Brand-only CTA layout; dark |
| Internal / subdomain pages | Internal | — | — | Confirm purpose or skip (robots: disallow) |

The pattern reads clearly: anything a company buys is dark, anything a person joins is light, contact and legal pages go brand-only, and proof pages lead with real people plus a number. Nobody had to make an aesthetic decision per card — the audience tag decided everything downstream.

---

## Notes

- **Segmentation is the whole skill.** Once the audience column is right, the rest is execution. If you find yourself debating the *look* of an individual card, you skipped the table — go back and tag the audience.
- **Two modes, not five.** The value is the consistency. Every additional mode dilutes the "this set is for me" signal and multiplies the work.
- **Real faces beat graphics** on social almost every time. Use brand-only mode for the pages where a photo would be arbitrary (legal, contact), not as the default.
- **Build templates before variants.** Get the two mode templates approved, then batch. Never mass-produce on an unproven template.
- **Verify on the real platforms** and force a re-scrape after any change — OG caching will otherwise serve stale images for days.
- This skill pairs with **reverse-prompting-for-image-gen** (describe the existing hero, generate from that) and **brand-operating-system** (lock the mode templates as reusable brand prompts).
