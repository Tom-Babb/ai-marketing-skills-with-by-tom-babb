---
name: knowledge-scrape-to-content
description: Turn publicly available knowledge on the internet — Reddit threads, YouTube videos, forums, Slack channels — into a content strategy and blog pipeline. Use this skill whenever someone needs to build a content foundation for a brand, find pain points to write about, generate blog topics, or figure out what their audience actually cares about. Triggers include: "what should I write about," "find pain points for X," "turn this Reddit thread into content," "build a content strategy," "scrape YouTube for blog ideas," or any request to go from raw internet knowledge to publishable content. Always use this skill before guessing what to write about.
---

# Knowledge Scrape to Content

Your audience has already told you exactly what they care about. It's sitting on Reddit, YouTube, forums, and Slack. This skill is how you go find it, pull the signal out, and turn it into content that ranks.

## The core idea

Don't create content from scratch. Scrape what already exists, extract the insights, and write about those. The verbatim words people use to describe their problems are the same words they type into search engines. Match those words and you win the audience.

## What you need to start

- A product, brand, or topic you want to create content around
- Access to a scraping tool (Firecrawl recommended) or the ability to copy/paste thread content
- Access to an AI model for extraction

## Step 1 — Find the right sources

Look for places where your audience is already talking. Best sources in order of value:

**Reddit** — The richest source. Find subreddits adjacent to your product or category. Look for threads with high engagement (100+ comments). These are full of verbatim pain points, questions, and opinions.

**YouTube** — Underused. Long-form videos from credible creators in your space are weeks of research you didn't have to do. An 80-minute video likely contains 10 distinct insights.

**Forums and communities** — Product Hunt, Hacker News, niche Slack communities, Discord servers. Anywhere people talk publicly about problems in your space.

**Your own Slack or internal channels** — If your team is having deep conversations about a topic, that knowledge probably doesn't exist on the internet yet. That's an edge.

## Step 2 — Scrape with a purpose

Scraping without intent is just collecting noise. Before you scrape anything, know what you're looking for:

- Pain points (what are people frustrated about?)
- Questions (what are people asking repeatedly?)
- Recurring themes (what topics keep coming up?)

Use Firecrawl or Camouflox to pull the full content of threads or pages. For YouTube, use Whisper or any transcription API to convert the video to text first.

## Step 3 — Extract the signal

Give the scraped content to an AI and ask with intent. Don't just say "write me a blog from this." Ask specifically:

- "What are the top 5 pain points people are expressing in this thread?"
- "What questions are being asked repeatedly?"
- "What are the distinct themes in this video? List each one separately."
- "What exact phrases are people using to describe their frustration with X?"

Each answer to those questions is a potential blog topic. Each distinct theme in a YouTube video is its own content pipeline.

**Keep the verbatim language.** When someone says "I hate how HubSpot doesn't let me connect directly to my database" — that exact phrasing is your blog title. Don't paraphrase it into marketing speak. The words people use online are the words they search.

## Step 4 — Write one insight per blog

Google penalizes content that recycles the same insight in different formats. One insight = one blog. That's it.

The brown dog walks to the trees.
A brown dog walked toward the trees.
There were trees. A brown dog approached.

Same insight. Three versions. Google counts it once and dings you for the other two. Find a new insight for every new blog.

**What counts as an insight:** a specific pain point, a specific question with a specific answer, a POV that doesn't exist elsewhere, a comparison, a how-to built around a real use case.

**What doesn't count:** a rewording of something you already published, a summary of another blog, a general overview of a topic you've already covered.

## Step 5 — Write for LLMs, not just humans

LLMs and search crawlers are looking for words sitting next to each other. If "your company name" sits next to "AI upskilling" enough times across enough pages, the model learns that's what you do.

Two things this means practically:

1. Use the verbatim pain point language from your scrape. Don't clean it up into polished marketing copy.
2. Answer seemingly obvious questions explicitly. If a geospatial company has a feature called "Planet University," they need a blog called "What is Planet University?" LLMs don't assume. They need to be told.

Play dumb. Write like you're explaining your product to something that has never seen a website before. Because you are.

## Step 6 — Build out the content pipeline

Once you have your list of insights from the scrape, you have a content calendar. Each insight becomes:

- One blog post
- Input for the long-form-to-content-pipeline skill (social posts, short form, etc.)

Don't try to write everything at once. Pick the 3 insights that match the most specific pain points your audience expressed in their own words. Write those first.

## Notes

- Reddit moderators are good. Don't try to hack engagement on Reddit. Just read it and scrape the knowledge.
- YouTube is a library that most people walk past. A creator who spent 3 weeks on research handed you that research for free.
- The goal of blogs is not for humans to read them — it's for LLMs and crawlers to associate your brand with the right words. Humans finding them is a bonus.
- Internal Slack is one of the most underused content sources. Real conversations about new ideas haven't been indexed yet. That's your edge.
