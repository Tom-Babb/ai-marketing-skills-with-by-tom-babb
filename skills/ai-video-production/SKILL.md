---
name: ai-video-production
description: Produce AI-generated video content using a three-stage tool stack: text-to-image, image-to-video, and editing. Use this skill whenever someone wants to create video content without filming, produce brand videos, make social media video clips, or animate a still image concept. Triggers include: "make a video of X," "create a brand video," "animate this image," "produce a short-form video," "I need video content without a camera," or any request to produce video from a text concept or image. Always use this skill before reaching for a camera or hiring a videographer for short-form content.
---

# AI Video Production

Three tools, three stages. Each stage is cheaper than the last if you stop early. Most people make the mistake of trying to start with video generation directly — don't. Start with image, get that right, then animate.

## The stack

| Stage | Tool | Role | Cost |
|-------|------|------|------|
| 1 | Reve App | Text-to-image | Cheapest |
| 2 | Veo 3 via Google Flow | Image-to-video | Mid |
| 3 | Adobe Premiere Pro | Editing | Most expensive |

Go as far down the stack as you need. A great still image might be enough. A short clip might not need editing. Stop when you have what you need.

---

## Stage 1 — Text to Image (Reve App)

Reve is the starting point. It takes text prompts and produces high-quality images that are optimized to animate well in the next stage.

**Why Reve over other image tools here:** Images generated in Reve are designed with video generation in mind. The subject placement, lighting, and composition tend to produce cleaner motion when fed into Veo 3.

**Workflow:**
1. Write your image prompt (use the `reverse-prompting-for-image-gen` skill if you have a reference image in mind)
2. Generate multiple variations — aim for 3-5 before picking one
3. Use Reve's "Edit" mode to refine specific elements (add objects, change backgrounds, adjust subjects) before animating
4. Export the final still

**What to optimize for at this stage:** Clean subject isolation, clear focal point, lighting that suggests motion direction. Avoid overly complex backgrounds — they create noise when animated.

---

## Stage 2 — Image to Video (Veo 3 via Google Flow)

Take your Reve image into Google Flow and use Veo 3 to animate it.

**Why image-to-video over text-to-video:** Starting from a defined image gives you control over exactly what's in the frame. Text-to-video is unpredictable — you get something, but rarely what you imagined. Image-to-video lets you lock the visual and just add motion.

**Workflow:**
1. Upload your Reve image to Google Flow
2. Write a motion prompt — describe what should move and how
3. Keep motion prompts simple: "camera slowly pushes in," "subject walks forward," "clouds drift left"
4. Generate 2-3 variations before committing
5. Download the clip

**Motion prompt principles:**
- Describe camera movement separately from subject movement
- Be specific about speed (slowly, gently, quickly)
- Avoid asking for too many simultaneous movements — the model gets confused
- Short clips (4-8 seconds) animate more cleanly than long ones

---

## Stage 3 — Editing (Adobe Premiere Pro)

Only enter Premiere if you need to combine multiple clips, add audio, add text, or produce a final deliverable longer than a single clip.

**When to use Premiere:**
- Combining multiple Veo 3 clips into a sequence
- Adding voiceover or music
- Adding captions or lower thirds
- Color grading for brand consistency
- Exporting for specific platform formats (Reels, TikTok, YouTube Shorts)

**When to skip Premiere:**
- Single clip social post — export directly from Flow
- Internal use or demo — Flow export is sufficient
- Quick test — don't edit until you know the concept works

---

## The decision framework

Before starting, ask: what's the minimum viable output?

- Need a still for a blog or social post → **Stop at Stage 1**
- Need a short animated clip for social → **Stop at Stage 2**
- Need a produced video with audio and multiple scenes → **Go to Stage 3**

Most short-form social content stops at Stage 2. Most people over-engineer into Stage 3 before they need to.

---

## Notes

- Don't start with video. Start with image. Get the image right before you animate. Every minute fixing a video clip is 10x more expensive than fixing the still it came from.
- Reve's Edit mode is underused. Use it to composite elements before animating — adding a product into a scene, placing a logo, adjusting a subject's position.
- Veo 3 is currently accessed via Google Flow — it is not a standalone app.
- Adobe Premiere is expensive and has a learning curve. For simple edits, CapCut or a free editor is fine. Premiere is for polished final output.
- The full stack (Reve → Flow → Premiere) is still cheaper than one day of professional video production.
