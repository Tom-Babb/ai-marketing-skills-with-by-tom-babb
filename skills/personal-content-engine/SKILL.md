---
name: personal-content-engine
description: Build a full content distribution system around a single person — their LinkedIn presence, podcast, voice, and short-form video — using AI to amplify their existing knowledge and reach new audiences. Use this skill whenever someone wants to grow a personal brand, help a founder or executive build an audience, turn a subject matter expert into a content presence, or create a spokesperson for a specific audience segment. Triggers include: "help X build a personal brand," "turn this person into a content creator," "build content around our founder," "grow X's LinkedIn," "create a podcast for X," or any request to build audience and distribution around a specific individual. Always use this skill before recommending a generic content strategy.
---

# Personal Content Engine

Every audience can have its own spokesperson. This skill is how you build one — taking a real person with real knowledge and turning them into a content presence that compounds over time.

The Mike Rugg case is the clearest example: a food and agriculture consultant with 2,678 LinkedIn followers, a Spotify podcast, AI-cloned voice content, and a short-form video presence — all built around one person's existing expertise.

## What you need to start

- A person with genuine knowledge in a specific domain
- Access to their existing content (LinkedIn posts, interviews, talks, emails, anything they've written or said)
- Their permission and involvement — this doesn't work without the person's voice
- Basic tools: LinkedIn, a podcast host (Spotify/Apple), ElevenLabs for voice, Riverside for video

---

## The four pillars

### 1. LinkedIn

LinkedIn is the foundation. It's where the person establishes credibility, grows connections, and builds an audience that carries over to everything else.

**Connection strategy:** Max out weekly connection requests. Target people in the exact niche — use keywords, conference hashtags, and job titles to find the right people. Don't connect randomly. Every connection should be someone who'd actually care about what this person knows.

**Warming connections:** Don't just connect and go silent. Send a short message after connecting — not a pitch, just a human observation or question. The goal is one yes: a reply, a call, a reaction. The product conversation comes later.

**Content:** Post consistently from the person's actual point of view. Use their voice, their observations, their specific experiences. Generic industry takes don't build audience. Specific, opinionated thinking does.

**The nerve problem:** Most people are scared to post. The way past it is to write like you're messaging a friend who asked you a question — not broadcasting to an audience. Start there.

### 2. Podcast

A podcast creates long-form credibility and produces raw material for everything else. Even a small podcast (single-digit monthly listeners) establishes authority in a specific niche and generates content that can be repurposed indefinitely.

**Setup:** Pick a narrow topic the person knows better than most. Name it after the specific topic, not the person — topic-first naming is more discoverable.

**Production:** Record conversations, not monologues. Interviews are easier to produce, more interesting to listen to, and generate relationship equity with guests.

**Distribution:** Spotify and Apple Podcasts cover 90% of listeners. Upload to both. Don't obsess over production quality early — content density matters more than audio perfection at the start.

**The real value of the podcast:** It's a long-form content asset that feeds the rest of the pipeline. See `long-form-to-content-pipeline` for how to extract blogs, clips, and social posts from each episode.

### 3. Voice (ElevenLabs)

Once the person has enough recorded audio (podcast episodes, interviews, talks), you can train a voice model on their voice using ElevenLabs. This lets you produce audio content in their voice without them recording every piece.

**Use cases:**
- Turn written content into audio in their voice
- Produce podcast episodes from transcripts without a recording session
- Create voiceovers for short-form video

**How to build the model:**
1. Collect 10-30 minutes of clean audio in their voice (podcast episodes work well)
2. Upload to ElevenLabs and train a custom voice model
3. Feed it text — scripts, blog posts, summaries — and it outputs audio in their voice

**Important:** This is a tool for scaling content the person has already approved, not for putting words in their mouth they haven't agreed to. Use it to produce more of their voice, not a different voice.

### 4. Short-Form Video

Short-form video is the highest distribution channel. It's where new audiences discover the person.

**The simplest workflow:** Record the person talking for 5-10 minutes about something they know. Use Riverside to identify and cut the strongest 60-90 second moments. Add captions. Distribute to Instagram Reels, TikTok, YouTube Shorts, and LinkedIn video.

**If the person won't record:** Use the AI video production stack (`ai-video-production` skill) to build video content around their ideas without them on camera. Voice clone + generated visuals can produce short-form content without a recording session.

**Captions:** Pull captions directly from the transcript. Don't write them separately.

---

## The compounding effect

These four pillars feed each other:

- LinkedIn grows the audience that subscribes to the podcast
- The podcast produces the long-form content that becomes blogs and clips
- The clips bring new followers to LinkedIn
- The voice model scales content production without requiring more of the person's time

Each piece of content the person produces becomes more valuable over time because the audience compounds.

---

## Segmentation: every audience gets its own spokesperson

One person can speak to multiple distinct audiences with different messaging, different content angles, and different platform presences. A food and agriculture consultant can speak to farmers, to AgTech investors, and to policy people — with different LinkedIn content and different podcast angles for each.

This is the direction marketing is heading: 100 audiences, 100 messages, 100 campaigns. The personal content engine makes that economically viable for a single person or small team.

---

## Notes

- Start with LinkedIn. Build the foundation before adding podcast and video. An audience of 500 engaged connections is more valuable than 5,000 passive followers.
- The person has to be involved. AI can amplify their voice, but it can't replace their actual point of view. The content engine breaks down if there's no real person behind it.
- Don't confuse volume with quality. One post a week that's specific and opinionated beats five generic posts. Same rule applies to podcast episodes.
- The nerve problem is real. Most people freeze when they think about posting publicly. Frame it as a message to one specific person, not a broadcast. That removes the performance anxiety.
- Follower count is a lagging indicator. Reply rate, connection acceptance rate, and direct messages are the leading indicators that the content is working.
