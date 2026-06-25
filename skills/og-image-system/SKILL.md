---
name: og-image-system
description: Design a consistent, on-brand Open Graph (OG) image system across every page of a site instead of one-off social cards. Use this skill whenever someone needs OG or social share images, link preview images, Twitter/X cards, or a thumbnail that shows up when a URL is pasted into LinkedIn, Slack, iMessage, or X. Triggers include "make an OG image," "our links look bad when shared," "we need social share images," "build link previews for the whole site," "design a social card," or any request to control how pages look when shared. The core move is segmentation, where you route each page to a visual treatment based on who the page is for, rather than designing each card from scratch.
---

# OG Image System

An OG image is the picture that appears when a link gets pasted anywhere, like LinkedIn, X, Slack, or iMessage. Most sites either have none, so the link renders as a gray box, or they put one generic card on every page. Both options waste the impression. Every shared link is a free ad placement, and most companies leave it blank.

The common mistake is treating each card as its own design task. The better way is to treat it as a system. You decide the rules once, route every page through them, and produce the whole set in an afternoon. The rule that does most of the work is segmentation, which means asking who each page is for, because that one answer decides the look.

## Before you start

This skill assumes you have a design system in place. A full brand and design system is recommended because it gives the design tool enough to work with on its own. If you do not have one yet, the minimum bar to run this skill is brand colors plus a clear font direction, so the outputs stay cohesive. If you have neither, you can pull a baseline from the inspiration gallery in Step 5, or run a separate brand or design-system skill first (see brand-from-references and brand-operating-system).

## The core idea

Do not design OG images page by page. Build a decision table, then execute it.

You need three decisions per page, and the first one settles the other two:

1. Audience. Who lands on this page? This is the segment.
2. Mode. What visual treatment does that segment get? This follows from the audience.
3. Real people. Does this page carry a real photo, or is it brand only?

Once the table is filled in, generation becomes mechanical. The thinking lives in the segmentation.

---

## The workflow

### Step 1, inventory every public page

Pull the full list of URLs you want to control. Start with sitemap.xml and the reference inside robots.txt. If there is no published sitemap, crawl from the homepage and follow internal links to build the map yourself. Include landing pages and subdomains, not only the main navigation. Flag anything internal or disallowed in robots.txt, because those usually do not need a public OG image, so you skip them.

One caveat. Some pages are JavaScript rendered and return empty HTML to a raw crawl even though they load fine in a browser. If a page comes back empty, render it with browser tools so you can read its content.

The output of this step is one row per URL.

### Step 2, tag each page with its audience

This is the only judgment call in the process. For each page, answer who the page is for.

Most sites collapse into a small number of segments. For a two-sided business it is usually some version of:

- Demand side or B2B, meaning the people who buy, hire, or sponsor, such as hiring partners, corporate buyers, and funds.
- Supply side or individual, meaning the people who apply, join, or learn, such as applicants, students, and members.
- Universal, meaning pages that serve everyone, such as the home page, pricing, privacy, and program overviews.
- Internal or unknown, which you flag and confirm before designing, or skip.

If you cannot decide which segment a page belongs to, it is probably universal.

### Step 3, derive the mode from the audience

Mode is the visual treatment. Pick a small, fixed set of modes, ideally two, and bind each one to a segment so the choice is automatic and does not need a fresh aesthetic decision each time. Binding the mode to the audience gives someone scanning their feed a consistent signal that this style means the content is for them.

A clean default split:

| Audience | Mode |
|----------|------|
| B2B or demand side (hiring partners, corporate, PE/VC) | Dark |
| Applicant, individual, or member facing | Light |
| Universal (serves multiple audiences) | Light |

Dark reads as enterprise and serious. Light reads as open and aspirational. The specific colors are less important than the consistency, because every B2B link should look like a set and every applicant link should look like a set.

### Step 4, decide real people versus brand only

Third column, with three values:

- Yes. Use a real photo of real people. This is the default for pages that have a strong human hero, such as apply pages, case studies, instructor or speaker shots, and partner testimonials. Real faces outperform graphics on social.
- Optional. Works with or without. Use a photo if you have a good one, and fall back to a brand graphic if you do not.
- No. Brand or graphic only. This fits legal pages, contact forms, and pure call-to-action pages where a photo would feel arbitrary.

For case studies and proof pages, prefer real partner or testimonial people paired with a result stat, because that combination is the highest-performing OG card you can make.

### Step 5, capture image direction per page

For each row, write one line of art direction pulled from the existing hero or content on that page. Describe what is working on the page so the card matches the destination, rather than inventing a fresh concept. Pair it with the page's own headline where one exists, for example "Stop Waiting. Start Shipping."

This is reverse prompting applied to OG images. You start from what the page shows, describe it, and generate from that description. See the reverse-prompting-for-image-gen skill for the full technique.

For broader inspiration, use https://www.ogimage.gallery/, which is a gallery of strong OG images from many sites. It is a good source for layout and treatment ideas, and it is also where you can establish a baseline look if you do not have a design system yet. If you are working without a design system, study the gallery to settle on brand colors and a font direction before you generate anything.

### Step 6, generate the set

Lock a template per mode so every card in a mode looks identical except for the variable content. A template fixes the background treatment, logo placement, type system, safe margins, and aspect ratio. You swap only the headline, the photo or absence of one, and any stat.

Specs to hold to:

- Aspect ratio. 1200 by 630 px is the standard OG size at 1.91 to 1. It renders correctly on LinkedIn, X, Facebook, and Slack.
- Safe zone. Keep the logo and headline away from the edges, because some platforms crop. Center the critical 1200 by 600 region.
- Typography rule. Set the website name or URL at 32 point. Set every other text element above 45 point. This keeps the website name the smallest element on the card and keeps the primary message readable at thumbnail size.
- Export format. The final export is WebP. WebP is the lightest format, the fastest to process, and it will not slow page load or affect SEO. If your design tool cannot export WebP, convert the files with a separate tool afterward.
- Tools. Use Claude Design, or any design tool, to build the two templates, then batch the variants. Generate or source the photos with your normal image pipeline.

Build the two mode templates first and get sign-off on those before you mass-produce. If you design twenty cards and then find the template was wrong, you redo all twenty.

### Step 7, hand off to the design tool in order

If you are building this in Claude Design, give it one kickoff prompt that puts it in charge of collecting assets from you one at a time, in order, so nothing gets designed out of sequence. When you drop in that first prompt, you should not have to attach anything yet. The design tool should request, one item at a time:

1. The plan spreadsheet or CSV, which is the master list of pages, modes, and directions.
2. The inspiration images you pulled from the gallery.
3. The in-person event photos for the pages marked Yes for real people.
4. The output specs, including the WebP export format, the 1200 by 630 dimensions, and the typography rule.
5. The page to start with.

The design tool should design nothing until it has each item. This keeps the run orderly when you step back after the first prompt. The tool can know your brand well enough to be dangerous on its own, so the value of this step is sequencing the inputs, not re-explaining the brand.

### Step 8, wire up the tags and verify

Each page needs the meta tags pointing at its image:

```html
<meta property="og:image" content="https://yoursite.com/og/page-name.webp" />
<meta property="og:title" content="Page Title" />
<meta property="og:description" content="One line." />
<meta name="twitter:card" content="summary_large_image" />
```

In your plan spreadsheet, keep an OG Image column with a "HERE" placeholder on each row, and replace each one with the finished image URL once the card is built. That gives you a single source of truth that tracks which pages are done.

Then verify before you call it finished. Paste the live URL into:

- LinkedIn Post Inspector
- X or Twitter Card Validator
- A real Slack or iMessage message, which is the true test.

Platforms cache OG images aggressively. If you update an image, use the platform inspector to force a re-scrape, or it will keep serving the old one for days.

---

## Worked example, GauntletAI rollout

This is the segmentation I ran across the GauntletAI site. Two modes, dark for B2B and light for applicant or universal, a real-people flag per page, and direction pulled from each page's existing hero. The site had no published sitemap, so I built the page list by crawling from the homepage, which found 23 URLs.

| Page | Audience | Mode | Real People? | Direction |
|------|----------|------|--------------|-----------|
| Home | Universal | Light | Yes | Hero crowd of challengers / Austin space; logo mark over warm bg |
| Privacy Policy | Universal | Light | No | Clean brand-only layout, logo + title |
| Program Overview | Universal | Light | Optional | Split visual hinting both programs |
| Apply, Fellowship | Applicant | Light | Yes | Fellows on laptops in Austin; "Stop Waiting. Start Shipping." |
| Night School | Applicant | Light | Yes | Speaker mid-lecture or class audience shot |
| See What They Build | Champion | Light | Optional | Challenger portrait + project screenshot, or project grid |
| Champions Registration | Champion | Light | Yes | Aspirational single challenger / "become a champion" energy |
| Hire Proven Talent | B2B, Hiring | Dark | Yes | Confident engineer headshots / talent roster; dark hero |
| Catalyst, Upskill Teams | B2B, Corporate | Dark | Optional | Engineering team in workshop/immersive; dark |
| PE & VC Training | B2B, PE/VC | Dark | Optional | Executive/boardroom or portfolio-scale graphic; dark |
| Hire Case Studies | B2B, Hiring | Dark | Yes | Partner leader portrait + result stat (Zapier, SkyFi, Splash) |
| Catalyst Case Studies | B2B, Corporate | Dark | Yes | Engineer testimonial portrait + result (Rev.io, Pilotbase) |
| Hiring Partner Contact | B2B, Hiring | Dark | No | Brand-only CTA layout; dark |
| Catalyst / PE & VC Contact | B2B | Dark | No | Brand-only CTA layout; dark |
| Internal / subdomain pages | Internal | n/a | n/a | Confirm purpose or skip (robots: disallow) |

The pattern reads clearly. Anything a company buys is dark, anything a person joins is light, contact and legal pages go brand only, and proof pages lead with real people plus a number. Nobody had to make an aesthetic decision per card, because the audience tag settled everything downstream.

---

## Notes

- Segmentation is the whole skill. Once the audience column is right, the rest is execution. If you find yourself debating the look of an individual card, you skipped the table, so go back and tag the audience.
- Keep it to two modes. The value comes from consistency, and every extra mode dilutes the signal and multiplies the work.
- Real faces usually beat graphics on social. Use brand-only mode for the pages where a photo would feel arbitrary, such as legal and contact pages.
- Build templates before variants. Get the two mode templates approved, then batch.
- A design system is the precondition. If you do not have one, brand colors and a font direction are the minimum, and the gallery at https://www.ogimage.gallery/ can help you set that baseline.
- Hold the typography rule on every card. The website name or URL stays at 32 point, and everything else stays above 45 point.
- Export to WebP. It keeps the files light, so the images do not slow the page or affect SEO.
- Verify on the real platforms and force a re-scrape after any change, because OG caching will otherwise serve stale images for days.
- This skill pairs with reverse-prompting-for-image-gen for the image direction and with brand-operating-system for locking the mode templates as reusable brand prompts.
