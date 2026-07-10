---
name: youtube-seo-optimizer
description: Turn a video transcript into a complete, search-optimized YouTube publishing package — ranked title options, a full description, tags, hashtags, chapter markers, thumbnail text concepts, a pinned comment, and Shorts cut suggestions — grounded in real Google Trends demand data. Use this skill whenever the user has a video transcript, recording, talk, lecture, or Night School session and wants help with the title, description, tags, metadata, thumbnail copy, chapters, or "how do I get this video to rank." Also trigger on "optimize my YouTube video," "what should I call this video," "write a YouTube description," "YouTube SEO," "help this video get views," "check Google Trends for this topic," or any request to research search demand for video topics. Trigger even when the user only mentions one piece (e.g., just the title) — the full package is almost always what they actually want. Delivers the result as a Google Doc.
---

# YouTube SEO Optimizer

Transform a raw transcript into a publishing package that is *grounded in what people actually search for*, not in what sounds clever.

The central discipline of this skill: **never invent keywords.** Every keyword claim in the final deliverable traces back to observed Trends data or a real YouTube search result. Guessed keywords are worse than no keywords, because they create false confidence and the video gets built around a phrase nobody types.

## Workflow

1. Read the transcript. Extract the actual topic, not the stated one.
2. Research search demand (see `references/trends-research.md`).
3. Build the package (see `references/youtube-optimization.md`).
4. Validate against YouTube's hard limits with `scripts/validate_package.py`.
5. Deliver as a Google Doc.

Run steps 1–2 before writing a single title. A title written before the research is an anchor you will spend the rest of the task rationalizing.

---

## Step 1: Read the transcript

Look for the gap between what the video *says it's about* and what it's *actually about*. Transcripts routinely bury the lede — the most searchable moment is often 20 minutes in, when the speaker goes off-script and answers the question the audience actually has.

Pull out:

- **The core claim.** One sentence. What does the viewer believe after watching that they didn't before?
- **Named entities.** Tools, models, companies, people, frameworks. These are high-intent search terms and they're free — the speaker already said them.
- **Question moments.** Any point where the speaker says "the question I get all the time is..." or answers something directly. These map to real search queries.
- **The strongest 30 seconds.** Where the energy peaks. This becomes the thumbnail concept and the first Short.
- **Timestamps of topic shifts.** Raw material for chapters.

Write these down before continuing. You'll reference them constantly, and reconstructing them later means rereading the transcript.

## Step 2: Research search demand

Read `references/trends-research.md` for the full procedure. Summary:

- Derive 5–10 **seed terms** from the entities and questions above.
- Pull Trends data: interest over time, rising queries, related queries, regional breakdown.
- Cross-check against YouTube's own autocomplete — Google Trends measures *web* search demand, YouTube autocomplete measures *video* search demand, and they diverge more than people expect. A term can be huge on Google and dead on YouTube (people want to read about it, not watch it).
- Classify each term: **Rising** (breakout, low competition, act now), **Steady** (durable, competitive), **Declining** (skip unless the video is explicitly retrospective).

The output of this step is a keyword table. Everything downstream cites it.

If Trends data is genuinely unavailable (see the fallback ladder in the reference), say so plainly in the deliverable rather than quietly substituting intuition. A package labeled "keywords unverified" is useful. A package that pretends to have data it doesn't is actively harmful.

## Step 3: Build the package

Read `references/youtube-optimization.md`. It contains the format rules, character limits, and the reasoning behind each field. The deliverable has eight sections — titles, description, tags, hashtags, chapters, thumbnail, pinned comment, Shorts.

## Step 4: Validate

```bash
python scripts/validate_package.py <path-to-package.md>
```

This checks every hard limit YouTube enforces (title 100 chars, tags 500 chars total, ≤15 hashtags, chapter rules, etc.). These limits are not suggestions — exceeding them causes silent truncation or, in the hashtag case, YouTube ignoring *all* your hashtags. Fix anything it flags before delivering.

## Step 5: Deliver

Create a Google Doc via the Drive connector's `create_file` tool: pass the package as `textContent` with `contentMimeType: "text/markdown"` and a title like `YouTube SEO — <video topic> — <date>`. Drive converts it to a native Doc automatically.

Then give the user the Doc link and a two-line summary: the recommended title and the single highest-leverage keyword. Don't restate the package in chat — they can open it.

If the Drive connector isn't available, write a `.md` file to the outputs folder and present it instead.

---

## Channel context: Gauntlet AI

Default assumption unless the user says otherwise: this is a **Gauntlet AI** video — technical AI education, aimed at engineers and ambitious career-switchers who want to build with AI rather than read takes about it.

What this means concretely:

- **The audience is smart and allergic to hype.** Titles that would work on a general-audience channel ("This AI Tool Will BLOW YOUR MIND") actively repel this audience. Specificity is the hook: a number, a named tool, a concrete outcome.
- **Lean into named entities.** "Claude Code," "MCP," "agent harness," "eval," specific model names. This audience searches for tools by name. Generic terms like "AI productivity" attract the wrong viewer, who bounces, which hurts the video.
- **Curiosity gaps are fine; dishonest ones are not.** "Why our agents kept failing until we changed one thing" is good. "The SECRET Anthropic doesn't want you to know" is a channel-credibility tax.
- **Assume the viewer might be evaluating the program.** A meaningful fraction of viewers are deciding whether Gauntlet is for them. The description should always leave a clear, non-desperate path to learn more.

When the user indicates a different channel or audience, discard this section and ask what replaces it.

---

## Things that go wrong

**Optimizing the title for the wrong search surface.** YouTube titles are ranked by YouTube search *and* browse/suggested. Browse is usually the bigger traffic source. A title stuffed with keywords wins search and loses browse, because it reads like a robot wrote it and nobody clicks. Write for a human, place keywords where they land naturally, and accept a keyword you love in position 40 rather than forcing it to position 1.

**Treating Trends "interest" as volume.** Google Trends normalizes to 0–100 relative to the peak *within your query set*. A term at 100 might get 200 searches a month. Never report Trends numbers as search volume, and never compare scores across two separate Trends queries — the scaling differs. (The alpha API changes this; see the reference.)

**Chapters that describe structure instead of content.** "Introduction / Main Content / Q&A" is worthless. Chapters are indexed by Google and surface as separate results — each one should read like a search query someone would type.

**Writing the description for the algorithm.** The first 120 characters appear in search results and above the fold. That's ad copy for a human. Keywords go in the body, where they're doing indexing work and nobody's reading anyway.

**Shorts that are just clips.** A Short cut from a long-form video needs a hook in the first 1.5 seconds and a reason to exist on its own. "Timestamp 14:20 to 15:10" is not a Short; it's a fragment. Specify the hook line.
