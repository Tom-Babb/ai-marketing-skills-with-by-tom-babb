# Marketing with AI by Tom Babb

Marketing is being repriced. Marketing is being repriced. I want to show you why.

The people who win are not going to be the ones who generate the most content. They are going to be the ones who can segment and differentiate while everyone else drowns in sameness. That is the whole argument. This repo is where I put the skills that make it real.

Everything here comes from running it myself. I subscribe to everything, I test everything, and I have turned myself into a live AI marketing lab. When something works, I document it. When it does not, I move on. These skills are the ones that held up.

---

## The one-line version of why this matters

AI did not eliminate the work. It eliminated the handoffs. A typical agency account is a chain: brief to strategist to writer to designer to editor. Each box is a person, and most of the cost lives in passing the baton between them. That chain now collapses to two boxes: operator plus AI, then output. One person who knows how to drive the tools does research, copy, design, video, audio, and analysis in one motion instead of routing it through five specialists.

That is why roughly 75% of agency roles are gone within three years. Not because the work disappears, but because the assembly line does.

---

## What this repo is

A collection of documented, repeatable workflows built from real use. Each skill lives in its own folder under `/skills` and has a `SKILL.md` that covers what it does and when to use it, what you need to start, the step-by-step process, the tools involved, and notes from actually running it.

Read the skill, follow the steps, adapt where your situation calls for it. If you have feedback or want to talk through something, find me on [LinkedIn](https://www.linkedin.com/in/tbabb02/) or [X](https://x.com/TBabb02).

---

## The skills

### Distribution

**[The internet is full of raw material most people scroll past](skills/knowledge-scrape-to-content/SKILL.md)**

This is the system for turning what already exists online into a content strategy, a lead list, and a distribution engine. Three skills make up this system:

| Skill | What it does |
|-------|-------------|
| [Knowledge Scrape to Content](skills/knowledge-scrape-to-content/SKILL.md) | Scrape Reddit threads, YouTube videos, and forums for pain points and questions. Turn those into blogs that rank. |
| [People Scrape to List](skills/people-scrape-to-list/SKILL.md) | Find high-intent people in public corners of the internet and enrich them into a contactable list with personalization context attached. |
| [Long-Form to Content Pipeline](skills/long-form-to-content-pipeline/SKILL.md) | Take one podcast, video, or essay and pull a month of content from it across written and video formats. |

---

### Brand

**[Build a brand visual system in under an hour](skills/brand-from-references/SKILL.md)**

Using an inspiration library and Claude Design, you can go from a rough direction to a full design system the same day. Start from a concept and end with something you can build on indefinitely.

**[Future brands will ship with prompts, not PDFs](skills/brand-operating-system/SKILL.md)**

A brand guide tells you what the brand is. A brand operating system tells AI how to produce it. This skill converts a brand guide into a set of reusable prompts, one for voice, one for design, one for messaging, and one for identity, so any AI tool can produce on-brand output without a designer in the loop every time.

---

### Prompting

**[A generic prompt will always produce generic output](skills/constraint-prompting/SKILL.md)**

The mechanism is simple: most people hand the model a generic, underspecified request and ask for a generic asset. This skill fixes that by separating context, which is what the AI needs to understand before it starts, from constraints, which are the rules that prevent known failure modes from getting through.

**[The em dash was never the real problem](skills/anti-slop/SKILL.md)**

Removing the em dash is a surface fix. The slop lives in structure: repeated sentence openings, "X, not Y" contrast framing, colon-split titles, buzzword filler, and vague claims with no evidence behind them. This skill names all five patterns, explains where they come from, and gives you a single master prompt to paste at the end of any copy prompt to eliminate all of them at once. Works for blogs, emails, social posts, landing pages, ad copy, and anything else that needs to sound like a person wrote it.

**[Describe an existing image and use that description as your prompt](skills/reverse-prompting-for-image-gen/SKILL.md)**

Normal prompting goes from prompt to output. Reverse prompting goes from output to prompt. You start from something you already like and work backwards to the instructions that reproduce it. This skill covers the full technique for image generation, including the subject and setting synthesis method for placing any subject into any environment.

---

### Content and Video

**[Never start with video](skills/ai-video-production/SKILL.md)**

Text-to-video is inconsistent. The pipeline that actually works goes prompt to image to video to edit, cheapest to most expensive. Reve handles text-to-image, Veo 3 via Google Flow handles image-to-video, and Adobe Premiere handles editing. The skill includes a decision framework for when to stop at each stage.

**[Every audience can have its own spokesperson](skills/personal-content-engine/SKILL.md)**

This skill builds a full content distribution system around a single person, covering LinkedIn, podcast, voice clone, and short-form video. It takes a subject matter expert and turns them into a content presence that builds over time. Each audience segment gets its own voice and its own content stream.

**[Build a persistent visual world in Reve](skills/reve-world-builder/SKILL.md)**

Reve holds the context of a character, environment, and visual style across an entire session, so every image you generate is consistent without re-describing it from scratch. This skill covers world building from reference images, bounding box editing to change specific elements without touching the rest of the image, and exporting frames for animation.

---

### Paid Advertising

**[What replaced a $4,000 agency in 35 minutes](skills/google-ads-with-ai/SKILL.md)**

The month before I built this workflow, we paid an agency $4,000 for a Google Search campaign. This skill walks through the exact replacement: Manus to generate the keyword and messaging report, Claude and the Pipeboard connector to build the campaign directly in Google Ads, and a scheduled daily report so the numbers are waiting when you wake up.

---

### Music and Creative Distribution

**[Getting AI music heard without a label or a budget](skills/music-distribution-strategy/SKILL.md)**

Four distribution tactics built from real experimentation: naming songs around trending Google searches so people can actually find them, building trojan horse playlists on Spotify to reach listeners who came for someone else, scraping radio station emails for slow-drip outreach, and making trend-reactive music videos during the window when a topic is still spiking.

---

### Discoverability

**[The agent is becoming the customer](skills/geo-optimization/SKILL.md)**

Search is collapsing into answers. Google is replacing blue links with AI summaries, and your reader is increasingly an AI, not a person. GEO, Generative Engine Optimization, is what SEO becomes when the model is the audience. This skill covers authority, structure, discoverability, and conciseness, and what it means to write for something that never assumes anything.

Note: This skill is actively being expanded. More tactical workflows are coming.

---

## Coming next

These ideas are documented but not yet built into full skills.

**Segmentation at Scale** is what becomes economically viable once production drops to pennies. When you can run 100 audiences, 100 messages, and 100 campaigns simultaneously, the whole frame shifts from making content faster to finally segmenting at a scale that used to be impossible.

**Reverse Prompting a Brand** is the process of extracting voice, design language, messaging, and identity from existing brand materials. The output is a set of prompt sentences that reliably reproduce the brand, which turns out to be a real and weirdly valuable skill.

**Agent-First Web Presence** is about writing documentation and web content for AI agents as the primary reader. Humans infer. Agents read literally. Everything needs to be stated.

---

## About

I am Tom Babb, Director of Marketing at [Gauntlet AI](https://www.gauntletai.com) and the first marketing hire there. I also run an AI-first side projects. I broke my neck at 19 in Maui in 2015, so I use a wheelchair, and I am an open book about it.

I am not nervous about what is coming in this industry. I know what is coming, and I would rather be the person creating far more value than everyone else than the person who got blindsided. A lot of people are going to get blindsided. This repo is how I build in public.

Making the internet less sloppy one skill at a time.

[LinkedIn](https://www.linkedin.com/in/tbabb02/) · [X](https://x.com/TBabb02) · [Gauntlet AI](https://www.gauntletai.com)
