---
name: long-form-to-content-pipeline
description: Turn one piece of long-form content — a podcast, YouTube video, essay, transcript, or interview — into a full content pipeline across written and video formats. Use this skill whenever someone has a long-form asset and wants to get maximum distribution from it, or whenever someone needs to produce a lot of content without creating everything from scratch. Triggers include: "turn this podcast into content," "repurpose this video," "I did an interview and want to get content out of it," "make social posts from this transcript," "turn this YouTube video into blogs," or any request to take one input and produce many outputs. Always use this skill before paying someone to create content from scratch.
---

# Long-Form to Content Pipeline

One piece of long-form content — a podcast, a YouTube video, an essay, an interview — contains more content than most brands publish in a month. This skill is how you pull all of it out without recycling the same insight twice.

## The core idea

Long-form is a goldmine because it's dense with individual insights. An 80-minute podcast likely has 10 distinct things worth saying. Each of those is its own blog. Each blog powers 4–5 social posts across platforms. One recording session, done intentionally, can power a month of distribution.

## What you need to start

- One piece of long-form content (podcast episode, YouTube video, essay, speech, interview transcript)
- Access to a transcription tool if starting from audio/video (Whisper API, Riverside, or similar)
- Access to Claude for extraction and writing
- Access to Claude Design for social post creation
- A short-form video editing tool if you want video clips (Riverside recommended over Opus Clip)

## The two tracks

Long-form splits into two parallel tracks. Run both.

```
LONG-FORM INPUT
      |
      |-------- WRITTEN TRACK -----------------> blogs → social posts
      |
      |-------- VIDEO TRACK -------------------> long-form video → short clips → reels/shorts/TikTok
```

The written track powers captions for the video track. They feed each other.

---

## Written track

### Step 1 — Transcribe

If your long-form is audio or video, transcribe it first. Tools: Riverside, Whisper API, or any transcription service. The transcript is the raw material for everything written.

If you're starting from an essay or written piece, skip this step.

### Step 2 — Extract the insights

Do not give the transcript to AI and say "write me a blog." That produces one generic blog that tries to cover everything. Instead, extract first.

Give the transcript to Claude and ask:

- "What are the distinct themes or topics covered in this content? List each one separately."
- "What are the most specific, non-obvious points made in this piece?"
- "What questions does this content answer? List them."

You're looking for individual insights — each one should be specific enough to title a blog. If two "insights" are really the same point, they count as one.

**Rule: one insight per blog.** Google penalizes content that restates the same idea in different words. Each blog needs to say something the others don't.

### Step 3 — Write the blogs

For each insight, write one blog. The blog should:
- Answer one specific question or address one specific pain point
- Use the verbatim language from the original content where possible
- Not overlap with the other blogs in your pipeline

Aim for 10 blogs from an 80-minute piece. Fewer if the content is less dense. The ratio is roughly one insight per 8–10 minutes of good long-form.

### Step 4 — Turn each blog into social posts

Each blog becomes posts for each platform you're active on. The format changes, the insight doesn't.

- **LinkedIn** — professional framing, first-person POV, slightly longer
- **X (Twitter)** — punchy, single idea, can thread if needed
- **Instagram** — carousel format works best; use Claude Design to make it visual
- **Reddit** — conversational, community-first, never pitchy

Use Claude Design to produce the Instagram carousels and any other visual posts. Your brand reference files from `brand-from-references` should already be loaded — build on those.

One blog → four posts (one per platform). Ten blogs → forty posts.

---

## Video track

### Step 1 — Keep the long-form as-is

The full recording lives on YouTube. Don't cut it down. Long-form video builds authority and gives LLMs and search engines a lot to index. Upload it, title it with your target keywords, write a real description.

If it's audio-only, upload to Spotify and Apple Podcasts as an MP3.

### Step 2 — Cut short-form clips

Use Riverside (preferred) to identify and cut the strongest 60–90 second moments. Look for:
- A single punchy insight delivered clearly
- A moment of tension or surprise
- A practical tip someone could act on immediately

Each clip goes to: Instagram Reels, TikTok, YouTube Shorts, X video.

### Step 3 — Use written track for captions

Pull the caption for each short-form clip directly from the social post you wrote for the same insight in the written track. They're already written. Don't write them twice.

---

## Advanced: training a voice and publishing as a new format

If you want to go further with repurposing, you can take the transcript, reverse-prompt the voice and tone out of it, and use that voice to produce entirely new content. Or you can take someone else's essay, train a voice model on their existing audio (via ElevenLabs or similar), and publish their written work in their voice as a podcast they never recorded.

Example: Paul Graham's "Founder Mode" essay, read by Paul Graham, published as a podcast on Spotify — without Graham ever recording it. Transcript + 6 YouTube interviews → ElevenLabs voice model → audio file → Spotify upload.

This is a legitimate form of repurposing for content you have rights to or that is in the public domain. For others' work, understand the legal and ethical line before publishing.

---

## Notes

- A podcast appearance is a month of content. Treat every long-form recording session like it has to justify itself across 40 posts.
- The written and video tracks feed each other. Don't run one without the other.
- Riverside is preferred over Opus Clip for short-form cutting — better control, better output.
- The most valuable long-form you can create contains original POV that doesn't exist anywhere else. Interviews, internal conversations, and transcribed thinking count. Scripted recaps of things people already know don't.
- YouTube creators have already done the research. An 80-minute video in your space is a free content brief. Transcribe it, extract the insights, and write the blogs. The creator spent weeks on the research. You spent an hour on the pipeline.
