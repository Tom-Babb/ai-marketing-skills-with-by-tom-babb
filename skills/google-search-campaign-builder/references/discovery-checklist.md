# Discovery checklist — what to gather before building

A campaign is only as good as the inputs. Gather these before writing the build
spec. Anything the user did not provide, either ask for it (if it materially
changes the build and you cannot infer it) or research it from the site and state
your assumption. Prefer researching over interrogating — a good default with a
stated assumption beats a wall of questions.

## From the user (ask if not provided)

1. **Website URL** (required). The homepage is the starting point.
2. **Priority products / categories.** Which offerings should the campaign push?
   If unspecified, infer from what has the clearest transactional pages and
   highest apparent deal value; state your pick and why.
3. **Geographic targeting.** Where do they sell / serve? Countries, regions, or a
   local radius. If unknown, default to the country the site targets, presence-based.
4. **Budget.** Monthly total, or a per-day figure. If unknown, propose a starting
   budget and let them adjust.
5. **Primary conversion(s).** What counts as a win — quote request, purchase,
   demo booking, call, form fill? Find the actual form/CTA URLs on the site.
6. **Brand constraints / house style.** Any banned words, required disclaimers,
   tone, or an existing style guide. Default to the house style in
   `ad-copy-rules.md` if none given.
7. **Any known competitors** (helps sharpen positioning and conquesting).

## From the website (research these)

Pull these directly; they drive both positioning and the field values.

- **Messaging & positioning:** homepage tagline, value-prop headings, "why choose
  us" bullets, the descriptor words they repeat. Quote exact phrasing — the ad
  copy should echo the site's own language where it's strong.
- **Differentiators / the wedge:** the specific, defensible claims that make them
  win the click versus bigger competitors (certifications, proprietary tech,
  regulatory precedent, spec numbers, supply/scale, guarantees, origin). These
  become headlines and callouts.
- **Product / category pages:** exact names and **exact landing-page URLs**, plus
  hard specs (numbers, grades, formats, sizes) you can turn into spec headlines.
- **Buyer-facing pages you'll need for assets:**
  - Quote / contact / demo / pricing request page (conversion destination)
  - Quality / certifications / compliance / trust page
  - Product catalog or overview
  - Contact page and **phone number** (call asset)
  - Privacy policy URL (needed for lead-form assets)
- **Business identity:** legal/customer-facing name (for the business-name asset,
  ≤25 chars) and whether a logo is available.
- **Proof assets:** certifications, notable customers, awards, published results,
  years in business — anything that substantiates a claim.

## Personas (derive from the site + category)

Name the 3–5 buyer personas the campaign is trying to reach, and — just as
important — who to **exclude** (students, job seekers, DIY, patients/clinical,
wrong-industry, tire-kickers). The exclusions become the negative-keyword
strategy. High-intent, bottom-of-funnel buyers are the target; informational and
research traffic is waste in a lead-gen or ecommerce Search campaign.

## Landing-page URL verification (do this before finalizing)

Every final URL and sitelink URL in the build must resolve (HTTP 200) and load
the intended page. A broken or redirecting landing page is wasted spend and a
policy risk. If a URL 404s, find the correct one (site search, sitemap, or a web
search of `site:domain product-name`) rather than guessing. Flag any URL you had
to infer so the user can confirm it.

## Output of discovery

By the end you should be able to fill in, per priority category:
- the exact landing-page URL,
- 3–5 spec/benefit facts unique to that product,
- the buyer persona and their search intent,
- the differentiators that separate it from the obvious competitor.

If you have that, you can build the campaign.
