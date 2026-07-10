# Trends research

## The access situation (read this first)

Google Trends has **no public API**. This surprises people, so it's worth being precise:

- Google announced an official Trends API in **July 2025**. It is still in **gated alpha** — access is granted by application, rolling out to a small number of developers. Public availability is not expected until roughly 2027.
- There is no API key you can buy or generate. If the user says "there's a Trends API," they're right, but they almost certainly don't have access to it.
- `pytrends` and similar libraries scrape the undocumented endpoints behind trends.google.com. They work intermittently and get rate-limited hard (HTTP 429) — Google actively throttles them. Treat as unreliable.

So: **the browser is the real primary path.** Everything below assumes that, with the API as an upgrade if the user has it.

## Fallback ladder

Work down this list. Stop at the first rung that produces data.

### Rung 1 — Official Trends API (only if the user has alpha access)

Ask once, early: "Do you have Google Trends API alpha access?" If no, skip permanently — don't ask again in later runs.

If yes, the API returns **consistently scaled** data, which is meaningfully better: values are comparable across separate requests, so you can merge queries and compare more than five terms. The 0–100 caveat below does not apply. Use the user's own endpoint documentation, since the alpha's surface is not public and may have changed.

### Rung 2 — Chrome browser on trends.google.com (default path)

Use the Claude-in-Chrome tools (`mcp__claude-in-chrome__*`). Load them in one batched `ToolSearch` call:

```
select:mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page
```

Trends is a client-rendered app, so plain `web_fetch` returns an empty shell. You need a real browser.

Construct URLs directly rather than clicking through the UI — faster and more reproducible:

```
https://trends.google.com/trends/explore?date=today%2012-m&geo=US&q=<term1>,<term2>&hl=en-US
```

Parameters worth knowing:

| Param | Values | Notes |
|---|---|---|
| `date` | `today 12-m`, `today 5-y`, `now 7-d`, `2025-01-01 2026-07-10` | 12-m is the right default for evergreen video topics |
| `geo` | `US`, `GB`, `` (worldwide) | Leave empty for worldwide |
| `q` | comma-separated | **Max 5 terms.** Batch in groups of 5 with one shared anchor term |
| `gprop` | ``, `youtube`, `news`, `images` | **`gprop=youtube` filters to YouTube search** — use it |

`gprop=youtube` is the single most valuable parameter in this whole skill and almost nobody uses it. It restricts Trends to YouTube search data specifically. Always run your seed terms both with and without it, and note where they disagree — a term with high web interest and low YouTube interest means people want to *read* about this, and a video will underperform.

After navigating, call `get_page_text` and read: Interest over time, Related queries (both "Top" and "Rising"), Related topics, and Interest by subregion.

**Rising queries with a "Breakout" label** are the highest-value finding in the entire report. Breakout means >5000% growth, which means low competition and a term that no existing video is optimized for. Surface these prominently.

### Rung 3 — YouTube autocomplete (always do this, regardless of rung)

This is not a fallback; it's a required cross-check. It's the closest thing to a free read on YouTube's own query logs.

Navigate to `https://www.youtube.com/results?search_query=<seed term>` and read the suggestions, or type the seed into the search box and capture the dropdown. The suggestions are ordered by actual query frequency.

Do this for each seed term, plus each seed term followed by a space (which yields longer-tail completions). Terms that appear in autocomplete are terms real people type into YouTube — that's a stronger signal for a video than anything Google Trends gives you.

### Rung 4 — Web search

If the browser is unavailable, use `WebSearch` to find recent keyword-research writeups, competitor video titles, and "best X 2026" listicles. This gives you competitor titles and rough topical framing.

Label everything from this rung as **unverified** in the deliverable. It is directional, not measured. Being explicit about this is not a weakness in the report — it tells the user which claims to trust.

## Reading the data correctly

**0–100 is relative, not absolute.** Trends normalizes to the peak *within the query set and time range you requested*. A score of 100 means "the highest point in this chart," which might be 50 searches. Consequences:

- Never report Trends scores as search volume.
- Never compare a score from one Trends query against a score from a different query. Different scaling. This is the single most common analytical error people make with Trends.
- To compare across batches, include one **anchor term** in every batch — a term with moderate, stable interest that appears in all queries. Then normalize each batch by its anchor's score. This is how you legitimately compare more than five terms.

**Seasonality is a trap.** A 12-month view of a term that spikes every January looks like "rising" in December. Pull `today 5-y` on anything that looks like a breakout, to check whether it's a real trend or an annual cycle.

**Low-volume terms return noise.** If interest-over-time is mostly zeros with occasional spikes to 100, there's not enough search volume for Trends to say anything. Don't build a title around it. Note it as "insufficient data" and move on.

## Building the keyword table

Produce this table. It's the evidentiary backbone of the deliverable — every title, tag, and chapter cites it.

| Term | Web interest (0–100) | YouTube interest (gprop=youtube) | Trajectory | In YT autocomplete? | Verdict |
|---|---|---|---|---|---|
| claude code | 78 | 91 | Rising | Yes (pos. 1) | **Primary** |
| mcp server | 34 | 52 | Breakout | Yes (pos. 3) | **Primary — low competition** |
| ai agent framework | 100 | 41 | Steady | No | Secondary (web-skewed) |
| prompt engineering | 62 | 28 | Declining | Yes (pos. 7) | Skip |

**Verdict logic:**

- **Primary** (1–2 terms): high YouTube interest, appears in autocomplete, rising or steady. These go in the title.
- **Secondary** (3–5 terms): decent interest but competitive, or web-skewed. These go in the description's first paragraph and in chapters.
- **Long-tail** (5–15 terms): low volume, high specificity, from autocomplete and Rising queries. These go in tags and later description paragraphs. Collectively they often outperform the primaries, because you can actually rank for them.
- **Skip**: declining, or the search intent doesn't match a video (e.g., people searching it want documentation, not a talk).

A **Breakout** rising query with even moderate YouTube interest beats a high-volume steady term almost every time. You cannot outrank an established video on a competitive term with a new upload; you can own a breakout term before anyone else notices it. Bias the recommendation accordingly, and say so explicitly in the report so the user understands why you passed on the bigger number.
