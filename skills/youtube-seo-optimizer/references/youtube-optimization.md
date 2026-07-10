# Building the package

Eight sections, in this order. Each cites the keyword table.

## Hard limits (YouTube enforces these silently)

| Field | Limit | What happens if you exceed it |
|---|---|---|
| Title | 100 chars | Truncated. Only ~60 show on mobile/search |
| Description | 5,000 chars | Truncated |
| Description "above fold" | ~120 chars | Rest hidden behind "...more" |
| Tags | 500 chars **total, all tags combined** | Extra tags dropped |
| Hashtags | 15 max | **All hashtags ignored** if you exceed 15 |
| Hashtags shown above title | first 3 | Rest only in description |
| Chapters | ≥3, first must be `0:00`, each ≥10s | Chapters silently don't appear |
| Thumbnail | 1280×720, <2MB | Rejected |
| Shorts | ≤3 min, vertical | Not classified as a Short |

`scripts/validate_package.py` checks all of these. Run it.

## 1. Titles — 7 options, ranked

Give 7, ranked, each with a one-line rationale naming which keyword it targets and which pattern it uses. The user picks; your job is to make the tradeoffs legible, not to hide them behind one "best" answer.

Front-load the primary keyword when it can be done without contorting the sentence. YouTube truncates around 60 characters in most surfaces, and the first few words carry disproportionate weight for both ranking and click decisions.

Cover a spread of patterns rather than seven variations on one:

- **Direct//informational** — `How MCP Servers Actually Work` — wins search, loses browse
- **Outcome/number** — `We Cut Agent Latency 80% With One Change` — specific, credible
- **Contrarian** — `Stop Using RAG For This` — high CTR, needs the video to deliver
- **Question** — `Why Do AI Agents Keep Failing In Production?` — matches how people search
- **Named-entity** — `Claude Code + MCP: A Complete Walkthrough` — captures brand search
- **Curiosity gap** — `The Eval Mistake Everyone Makes` — earn it or pay for it later
- **Comparative** — `Claude Code vs Cursor For Large Codebases` — rides both terms' demand

For a Gauntlet AI video, expect the outcome/number, named-entity, and contrarian patterns to win. The audience clicks specificity. Avoid ALL CAPS beyond a single word, and avoid more than one punctuation flourish.

Note the character count next to each. Anything over 60 chars, mark where mobile truncates.

## 2. Description

Structure:

```
[Hook — 2 sentences, <120 chars for the first one. Contains primary keyword.]

[Body — 2-3 paragraphs. What's covered, who it's for, what they'll be able to do.
 Weave secondary + long-tail keywords in naturally. This is where indexing happens.]

⏱️ Chapters
0:00 ...

🔗 Links
[Resources mentioned, in transcript order]

[CTA — subscribe / learn more about Gauntlet AI]

#hashtag #hashtag #hashtag
```

The first sentence is doing two jobs at once: it appears in search results as the snippet, and it's the only line most viewers ever read. Write it as ad copy that happens to contain a keyword — not as a keyword that happens to be a sentence.

Below the fold, keyword density matters and readability doesn't, much. This is the right place to put the long-tail terms that would look stuffed in the title.

Never write "In this video, we..." as an opener. It burns the highest-value 20 characters on your channel saying nothing.

## 3. Tags

15–25 tags, under 500 characters total. Order matters — the first few carry the most weight.

Composition:
- Exact primary keyword, first
- Secondary keywords
- Long-tail phrases from Rising queries and YouTube autocomplete
- Common misspellings of named tools, if any are frequent
- Channel name

Tags are a weak ranking signal in 2026 — YouTube leans on title, description, and engagement. They help most for disambiguating uncommon terms and correcting misspellings. Don't spend much effort here, and don't let the user believe tags will rescue a bad title.

## 4. Hashtags

Pick 3. Exactly 3, because only 3 render above the title and additional ones just clutter the description. More than 15 causes YouTube to ignore all of them, which is a footgun worth knowing but not one you should get near.

Choose broad-but-relevant: `#AIAgents #ClaudeCode #SoftwareEngineering`. Hashtags are a discovery surface, not a ranking one — they should match how the topic is *categorized*, not how it's searched.

## 5. Chapters

Derive from the topic shifts you noted while reading the transcript.

Rules: first chapter must be `0:00`. Minimum 3 chapters. Each at least 10 seconds. Ascending order.

Each chapter title should read like something a person would type into a search box. Google indexes chapters and surfaces them as individual results with their own thumbnails — a good chapter list is a second set of titles competing for a second set of queries.

Bad: `0:00 Intro / 2:15 Main Section / 18:40 Wrap Up`
Good: `0:00 Why agent evals are broken / 2:15 Building your first eval harness / 18:40 Common eval failure modes`

Aim for 5–10 chapters on a talk-length video. Fewer than 5 and you're not covering enough queries; more than 12 and each is too granular to be a real query.

## 6. Thumbnail concepts

Three concepts. For each: the **text overlay** (≤5 words — anything more is unreadable at mobile size), the **visual**, and the **emotional beat**.

Thumbnail text should not repeat the title. It should complete it. Title says what the video is; thumbnail says why you'd care. Together they should form one thought that neither expresses alone.

Note the strongest 30 seconds from the transcript as a frame-grab candidate. Real footage of a real moment beats a staged shot for this audience — a screenshot of an actual terminal error outperforms a stock photo of a person looking concerned.

## 7. Pinned comment

One paragraph, first person, from the creator. Its job is to seed the comment section with a real conversation, because comment velocity in the first hours feeds distribution.

The strongest pattern is a genuine open question the video *doesn't* answer, tied to something specific in the video. "What's the hardest part of evals for you?" is generic. "We punted on multi-turn eval entirely — has anyone found something that works there?" gets replies from people who know things.

Include timestamp links to the 2–3 best moments. This lifts session time on the exact segments that retain best.

## 8. Shorts

Three suggestions. For each:

- **Timestamps** in the source video
- **The hook line** — the literal first sentence, which must land within 1.5 seconds
- **Why it works standalone** — a Short cut from a talk fails if it needs the previous ten minutes of context

Best Shorts candidates in a transcript: a counterintuitive claim stated flatly, a specific number, a strong opinion, or a demo moment where something visibly works. Look for where the speaker's energy changes — that's usually where the good stuff is.

A Short is not a trailer. It should fully deliver one small idea, and let the viewer discover the long-form video afterward if they want more.

---

## Deliverable template

```markdown
# YouTube SEO Package — [Video Topic]
*Generated [date] · Keyword data: [Trends via browser / API / unverified]*

## TL;DR
**Recommended title:** [pick]
**Primary keyword:** [term] — [why]
**Biggest opportunity:** [the breakout term, if any]

## Keyword research
[the keyword table + 2-3 sentences of interpretation]

## 1. Title options
## 2. Description  (copy-paste block, in a fenced code block)
## 3. Tags        (comma-separated, char count noted)
## 4. Hashtags
## 5. Chapters
## 6. Thumbnail concepts
## 7. Pinned comment
## 8. Shorts
```

Put the description in a fenced code block so it can be copied into YouTube Studio without picking up markdown formatting. Small thing, saves the user a real annoyance every single time.
