---
name: ai-visibility-audit
description: Measure how visible a brand is across AI models, identify the specific questions where competitors are appearing instead of the brand, and track whether that visibility improves after publishing GEO-optimized content. Use this skill whenever a brand wants to know where they stand in AI-generated answers, when a content team needs a prioritized list of what to write next, when a client needs to see measurable results from a GEO content program, or when the goal is to build a repeatable system for improving AI visibility over time. Triggers include: "do we show up in ChatGPT," "where are we appearing in AI answers," "which questions are competitors winning," "track our GEO results," "build a visibility baseline," or any request to measure or improve AI search presence. Always run this audit before starting a GEO content program so there is a baseline to measure against.
---

# AI Visibility Audit

You cannot improve what you cannot measure. Before writing a single piece of GEO content, you need a snapshot of where the brand currently appears — and where it does not — across AI models. That snapshot becomes the baseline. Everything published after that gets measured against it. Over time, the goal is to find the equation: X pieces of content equals Y points of visibility improvement. Once you have that equation, you can forecast the resources needed to own a space.

This skill documents how to build and run that audit system, how to turn the results into a content brief, and how to track progress over repeated cycles.

---

## The two types of AI answers

Every question you ask an AI model produces one of two types of answers. Understanding the distinction matters for how you interpret the audit results.

**Parametric** answers come directly from the model's training data. The model is not searching the web. It is answering from what it already knows. If your brand appears in a parametric answer, it means the model has encountered enough about you in its training data to recall you without any web search. This is harder to influence in the short term.

**Retrieval** answers come from a live web search. The model queries the web, finds sources, and synthesizes an answer. If your brand appears in a retrieval answer, it means your content ranked well enough in that search to be included in the model's source set. This is what GEO content directly affects. Focus here first. Retrieval improvements tend to feed parametric improvements over time as models retrain on indexed content.

---

## Step 1 — Generate the question set

The audit is only as useful as the questions it tests. The question set should reflect what real people actually ask AI models about your brand's category, not the keywords your SEO team has been targeting.

**How to generate questions:**

Scrape each page of the target website and give the content to an AI with this prompt:

```
What questions does this page answer? List every question a person might type 
into an AI model and expect this page to be the source of the answer. 
Be specific. Include questions about features, use cases, comparisons, 
and problems this page addresses.
```

The AI will return a list of questions. These are the questions the page is supposed to answer. They are also the questions the audit will test.

**Important:** the questions the AI generates from a page are often phrased oddly because they are derived from marketing copy. Before using them in the audit, paraphrase them into natural language, the way a real person would actually type the question into ChatGPT. A question like "How does a geospatial company facilitate multi-spectral imaging acquisition workflows?" should become "How do I get satellite imagery for agricultural monitoring?" Use judgment here. The goal is realistic questions, not literal transcriptions.

**Also look for inference gaps:** sometimes you will read a cluster of questions and notice they all point to something the website has but has not explained. A set of questions like "where can I learn about remote sensing," "how do I get started with satellite data," and "is there documentation for this product" all point to a learning hub. If the website has one but has not written a page explaining what it is, add "What is [learning hub name]?" to the question set. Use inference to find the gaps that literal question generation misses.

A starting set of 50 to 100 questions is enough for the first audit cycle. Expand from there.

---

## Step 2 — Run the audit

For each question in the set, ask it to the target AI models with web search enabled. The models to test as a baseline are ChatGPT, Claude, Gemini, and Copilot. Perplexity is worth adding if the audience is research-oriented.

For each question, record:
- Whether the brand appears in the answer
- Whether a competitor appears in the answer
- The brand's position if it appears (first mention, secondary mention, not mentioned)
- Which model surfaced the answer

Aggregate this into a visibility score per model. A simple scoring system: 1 point for any mention, 2 points for a primary mention, 0 points for no mention. Out of the total possible points across all questions, calculate a percentage score per model. This is the baseline.

---

## Step 3 — Analyze the gaps

The audit will produce three categories of questions:

**Category 1 — Not appearing, competitors are.** These are the highest priority. A competitor is winning a question that should belong to the brand. For each of these, note which competitor appears and what their page does that the brand's does not. This becomes the content brief: write something that directly answers the question, addresses the same points the competitor addresses, and adds something the competitor does not have.

**Category 2 — Appearing, but not first.** The brand is in the answer but is not the primary source. These are the second priority. The content exists but is not authoritative enough. Improving the answer quality, adding more specific detail, and building backlinks to the relevant page will move these up.

**Category 3 — Not appearing, no one is.** These questions have no good answer anywhere on the web. This is a pure content opportunity. Write the answer and you win the question by default.

---

## Step 4 — Build the content brief

Group the gaps into clusters of related questions. One blog or FAQ page can answer multiple related questions at once. The goal is to cover the most questions per piece of content, not to write one piece per question.

For each content cluster, the brief should include:
- The questions being addressed
- The competitor page currently winning those questions and what it covers
- The recommended page title and URL slug
- The target keyword cluster
- The outline of the article (following the GEO content format from the `geo-optimization` skill)
- The FAQ questions and answers that should appear at the bottom of the page
- The schema markup for the page backend

Deliver this as a structured document the content team can act on directly. They should not have to make any strategic decisions. Every decision is made in the brief.

---

## Step 5 — Publish and track

Before the content team publishes anything, lock in the baseline scores for the specific questions being addressed. Re-run those exact questions across all models and record the results. This is the pre-publication snapshot.

After publishing, wait for the content to index. Use Google Search Console to manually submit the pages and shorten the indexing window. Then re-run the same questions in the same models and compare.

The delta — the change in visibility score from pre-publication to post-publication — is the result. Track this across multiple content cycles. Over time, a pattern will emerge: a certain number of pieces of content produces a certain number of points of visibility improvement. Once that equation is stable, the program can be forecasted. "We need to move 8 points this quarter, and each batch of 10 pieces moves us roughly 1 point, so we need 80 pieces" becomes a real planning conversation instead of a guess.

---

## What the deliverable looks like

The output of each audit cycle is three things:

**1. Visibility report:** a table showing the brand's current score per AI model across the full question set, with competitive benchmarks for each question where a competitor is appearing.

**2. Content brief:** the prioritized list of content to write, grouped by theme, with full specifications for each piece including questions, outline, FAQ content, and schema.

**3. Infrastructure audit:** a separate list of technical recommendations — schema markup, A2A protocol, robots.txt settings, missing pages — that are not content changes but will improve AI accessibility across the site.

---

## Notes

- The audit is a snapshot in time. AI models update constantly and answers change. Run the full audit quarterly at minimum, and track the specific questions being addressed monthly.
- Do not ask the same AI model the same question in the same session. Each question should be run in a fresh session with no prior context. Prior context changes the answer.
- Retrieval results vary. The same question asked three times may return three slightly different answers. Run each question at least twice and use the consistent pattern, not a single result.
- The question set is the most valuable asset produced by this process. As it grows and gets refined across cycles, it becomes an increasingly accurate picture of what the brand's audience is actually asking. Treat it as a living document.
- Parametric and retrieval are both worth tracking, but retrieval is what GEO content directly affects. Do not deprioritize parametric entirely — it is the long-term goal — but focus optimization effort on retrieval results first.
- Always benchmark before publishing. Running the audit after the fact gives you no way to measure what changed. The before snapshot is not optional.
