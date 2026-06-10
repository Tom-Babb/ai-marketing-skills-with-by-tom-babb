---
name: people-scrape-to-list
description: Build targeted outreach lists by finding high-intent people in public corners of the internet, scraping their identifiers, and enriching them into contactable leads with personalization context attached. Use this skill whenever someone needs to build a cold outreach list, find an audience for a new product, identify leads without buying a database, or do hyper-personalized outreach at scale. Triggers include: "find leads for X," "build an outreach list," "who should I be reaching out to," "find people interested in X," "I need emails for Y audience," or any request to go from zero audience to a list of real people. Always use this skill before paying for a lead database.
---

# People Scrape to List

Your audience is already out there showing intent publicly. They're liking posts, attending conferences, bidding on auctions, commenting on threads. They just haven't heard from you yet. This skill is how you find them, identify them, and reach out in a way that doesn't feel like spam.

## The core idea

People self-select into groups publicly online. Every like, comment, bid, post, and follow is a signal. If you can find where high-intent people are clustering around a topic adjacent to yours, you can scrape that cluster and build a list. Then you enrich it to get contact information, and you use the context of where you found them to write a message that feels personal.

## What you need to start

- A clear picture of who your target audience is (industry, role, interest, or behavior)
- A scraping tool or agent (Firecrawl or Camouflox recommended)
- An enrichment tool (Clay — a la carte pricing, no forced subscription)

## Step 1 — Find the right cluster

Look for a place on the internet where high-intent people are doing something public and specific. The formula: **public engagement + specific niche = scrapeable list**.

Good examples:

**LinkedIn keyword posts** — Search a specific event, conference, tool, or topic. Click Posts. Everyone who posted about it has self-identified as someone who cares about that thing. You can get their name, company, LinkedIn URL, and the content of their post from one search.

**Competitor Instagram likes/followers** — If a competitor has 1,000 followers and 25 likes per post, every one of those people has expressed interest in something adjacent to what you're building. That's your list.

**Conference or event hashtags** — Anyone posting about a specific conference attended it or cares about it. That's a very targeted slice of a professional audience.

**Forum engagement** — People commenting on a specific Product Hunt launch, a specific Hacker News thread, or a niche subreddit are self-identifying their interests.

**eBay live auctions** ⚠️ — Against eBay's terms of service, but worth knowing what's possible: bidders in niche live auctions (precious metals, collectibles, etc.) are extremely high-intent buyers. Usernames can be backfilled to real identities at roughly a 60% hit rate when names are unique enough. Not advised. Included here so you understand the ceiling of what's possible with this approach.

## Step 2 — Scrape the identifiers

You're not just looking for contact info. You're looking for identifiers you can use to enrich later AND context you'll use to personalize your message.

For each person, try to capture:
- First name
- Last name
- Company
- LinkedIn URL (or platform-specific URL)
- The URL or content of the specific post/action that surfaced them
- Any other public context (what they said, what they bid on, what they liked)

The context is not optional. You'll need it in Step 4.

Use an agent or scraping tool to build a spreadsheet. Don't do this manually.

## Step 3 — Enrich to get contact info

Take your spreadsheet into Clay. You pay per record rather than a monthly minimum — useful when you're running targeted lists of 50–500 people rather than mass outreach.

Give the enrichment tool as many identifying tokens as you have. First name + last name + company is the minimum. LinkedIn URL is better. More tokens = higher match rate.

The tool will return email addresses and often additional firmographic data (company size, job title, tech stack, etc.).

You can also run this backwards: if you have a list of emails from somewhere, dump them into Clay and have it tell you who the person is, where they work, and what their role is. Then segment from there.

## Step 4 — Store the context with the scrape

Before you write a single message, make sure your spreadsheet has a column for the context of how you found each person. This is the most important column.

- What did they post about?
- What conference were they at?
- What did they comment on?
- What were they bidding on?

When you message them, this context is your opening line. Not your product. Not your pitch. The thing they did publicly that tells you they might care.

## Step 5 — Write the outreach

The goal of the first message is not to pitch. It's to get a yes. One yes — to a call, to a reply, to a click. Save the product for after you have their attention.

Use the context to open. Examples:

- "Saw you posted about the Gartner Data & Analytics conference — [specific observation from their post]. Curious what you took away from it."
- "Noticed you're following [competitor] — we're building something in the same space and I'd love to get your take on it."
- "You bid on [item] at [auction] — we sell directly to collectors like you and thought you might want to hear about it."

The more specific the context, the better the reply rate. The goal, eventually, is one-to-one personalization at scale — a message so specific to each person that they wonder if you've been watching them. That's the ceiling to build toward.

**One caution:** context becomes creepy past a certain point. If it reads like surveillance, you've gone too far. A good test — would the person feel seen, or would they feel watched? Seen is good. Watched kills the reply.

## Notes

- You do not need to buy a lead database. Everything you need is already public. The database companies are just selling you a shortcut to information you could find yourself.
- Clay's a la carte model means you can run 20-record tests before committing to a bigger list. Do this.
- The LinkedIn keyword approach (conference or event name → Posts tab → scrape) is the cleanest, most defensible version of this workflow. Start here.
- Your competitor's Instagram audience is your most targeted possible cold list. They've already been sold on the category. You just have to be the better option.
