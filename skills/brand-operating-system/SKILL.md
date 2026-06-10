---
name: brand-operating-system
description: Convert a brand guide into a Brand Operating System — a set of reusable prompts that any AI tool can use to produce on-brand output without a designer or strategist in the loop. Use this skill whenever a brand needs to produce consistent AI-generated content at scale, when a team needs to maintain brand standards without a dedicated designer, or when a brand guide exists but nobody uses it because it's a PDF that lives in a folder. Triggers include: "make our brand guide useful for AI," "build a brand prompt," "how do we keep AI output on-brand," "create a system for brand consistency," "turn our brand guidelines into prompts," or any request to systematize brand output using AI. Always use this skill before manually writing brand context into every individual AI prompt.
---

# Brand Operating System

A brand guide tells you what the brand is. A Brand Operating System tells AI how to produce it. The difference is the difference between a document that sits in a folder and a system that actually gets used.

Future brands won't have brand guides. They'll have prompts.

## What a Brand Operating System is

A Brand OS is a collection of reusable prompts — one for each output type the brand produces — that encodes the brand's voice, design, messaging, and identity into a format AI can act on directly.

Instead of explaining the brand every time you open a new AI session, you load the relevant prompt and the brand is already in context.

## The four components

### 1. Voice Prompt

Encodes how the brand speaks — sentence structure, tone, vocabulary, what it avoids.

Built by: feeding existing brand copy into an AI and asking it to reverse-prompt the voice. Give it your best-performing content — the copy that sounds most like you — and ask:

> "Analyze the voice and tone of this copy. Describe the writing style in enough detail that another writer could replicate it exactly. Include: sentence length patterns, vocabulary level, what the writer avoids, how they handle emphasis, and the overall personality. Then write a reusable prompt that would instruct an AI to write in this voice."

The output is your voice prompt. Test it by generating new copy and comparing it against the original. Refine until it produces output you'd actually publish.

### 2. Design Prompt

Encodes visual identity — color palette, typography, composition style, mood, what the brand should look like.

Built by: using the `brand-from-references` skill to build a reference library, then extracting the design language from Claude Design's output into a reusable prompt.

For image generation specifically, the design prompt takes the form of a locked template with one variable. Example:

```
A dramatic monochrome of [SCENE], atmospheric depth, moody lighting, high contrast, 
cinematic wide shot, epic scale, ultra-detailed, black and white photography / 
digital art aesthetic --ar 16:9 --v 6.0 --chaos 20 --raw
```

Every image produced from this template is on-brand. The only thing that changes is the scene.

### 3. Messaging Prompt

Encodes what the brand says — the core claims, the value proposition, the proof points, the things the brand always says and never says.

Built by: extracting the brand's strongest positioning statements from existing materials (website, pitch decks, sales calls) and organizing them into a structured context block:

```
Brand: [name]
What we do: [one sentence, plain language]
Who we serve: [specific description]
Core claim: [the thing we believe that our competitors don't]
Proof points: [3-5 specific, factual supporting details]
What we never say: [list of terms, claims, or framings to avoid]
```

This becomes the context block that precedes any copy prompt. It ensures the AI is always writing from the brand's actual positioning, not generic category language.

### 4. Identity Prompt

Encodes who the brand is — the personality, the worldview, the things the brand cares about beyond its product. This is the hardest to codify and the most powerful when done right.

Built by: interviewing the founder or brand lead and capturing their unscripted answers to questions like: What does this brand believe that most people don't? Who is this brand for and who is it not for? What would the brand say at a dinner party? Transcribe the answers and reverse-prompt the identity out of them.

---

## How to deploy it

Once built, the Brand OS lives as a set of documents or a Claude Project that any team member can access. Before any content production session:

1. Load the relevant prompt (voice, design, messaging, or identity)
2. Add the specific task
3. Generate

No brand briefing required. No designer needed for standard output. The brand is already in context.

---

## What this replaces

| Old way | Brand OS way |
|---------|-------------|
| Brief a designer for every asset | Load design prompt, generate |
| Explain the brand voice every session | Load voice prompt, write |
| PDF brand guide nobody reads | Active prompts everyone uses |
| Inconsistent AI output across the team | Consistent output from shared prompts |
| $4,000/month agency retainer for standard content | Internal team with a Brand OS |

---

## Notes

- The Brand OS is only as good as the prompts it's built from. Prompts built from weak or generic brand materials produce weak output. Feed it the best stuff the brand has ever produced.
- Start with the voice prompt. It's the most immediately useful and the easiest to test. If the voice prompt produces copy you'd publish, the system is working.
- The design prompt is most powerful when paired with Claude Design — load the reference files and the design prompt into the same session and the output will be visually and tonally consistent.
- This is a living system. Every time AI produces output that's off-brand, identify the failure mode and add a constraint to the relevant prompt. The Brand OS improves with use.
- The Brand OS is also a training tool. New team members can produce on-brand output from day one without a lengthy onboarding — they just use the prompts.
