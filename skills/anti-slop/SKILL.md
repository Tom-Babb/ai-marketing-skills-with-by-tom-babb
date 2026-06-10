---
name: anti-slop
description: Detect and remove AI writing patterns from any copy — blogs, social posts, emails, landing pages, ad copy, pitch decks, or internal documents — so the writing sounds like a real person thinking out loud instead of a language model producing persuasive text. Use this skill whenever someone needs to write or edit copy that should not read as AI-generated, whenever previous AI output has come back generic or hollow, or whenever a piece of writing feels technically correct but somehow off. Triggers include: "this sounds like AI," "make this sound more human," "edit this copy," "write a LinkedIn post," "write a blog," "rewrite this," "clean up this draft," or any request to produce or improve written marketing copy. Always apply the master prompt at the end of any copy prompt, never at the beginning.
---

# Anti-Slop

AI writing is recognizable not because of emojis or em dashes anymore. Those were the first generation of tells and most people have already eliminated them. The current tells live in structure — repeating sentence patterns, rhetorical framing borrowed from persuasive writing, and hype language that sounds like something without actually saying anything.

The way to identify a slop pattern is to copy examples of writing that feel off and ask an AI: "What grammatical structure is happening here?" It will identify the pattern by name. Then ask: "Write a prompt that prevents this structure from appearing." AI is useful for teaching you exactly how to stop writing like AI.

Below are the five labeled patterns, what they look like, and how to prompt against them. After the patterns is the master prompt — a single block you paste at the end of any copy prompt to enforce all of them at once.

---

## The five slop patterns

### 1. ANAPHORA — repeated sentence openings

AI repeats the same opening word or phrase across consecutive sentences because the rhythm sounds persuasive.

What it looks like:
> "We tested the system. We deployed the system. We expanded the system."

Once readers notice this pattern it feels mechanical and staged, even if they cannot name what they are seeing.

Prompt to fix it:
```
Avoid anaphora and repeated opening phrases. Do not repeat the same beginning 
across multiple sentences. Write sentences with varied structure and natural flow.
```

---

### 2. DUAL_CLAUSE_CONTRAST — the "X, not Y" construction

AI defines ideas through comparison, setting up one concept and dismissing another in the same sentence. It creates a false sense of clarity.

What it looks like:
> "Great operators build systems, not workflows."
> "This is a leadership decision, not a technical one."

When every post uses this pattern, the writing starts to sound scripted regardless of what is being said.

Prompt to fix it:
```
Avoid contrast-based sentence structures and rhetorical opposition. 
Explain ideas directly without defining them through comparison with another concept.
```

---

### 3. COLON_TITLE — dual clause headers that simulate depth

AI writes titles that split into two halves around a colon. The first half creates intrigue, the second half sounds analytical.

What it looks like:
> "The Future Of Marketing: Why Systems Win"
> "From Data To Strategy: A New Perspective"

The structure looks organized but it is mostly decorative. It signals that the writer was performing depth rather than expressing it.

Prompt to fix it:
```
Avoid colon-based dual clause titles. Write titles that describe the idea directly 
without splitting a concept into two rhetorical halves.
```

---

### 4. BUZZWORD_GENERIC — hype language that carries no information

AI relies on words that sound impressive but do not say anything specific. If you remove the adjective and the meaning stays the same, it was filler.

What it looks like:
> "Unlocking the power of AI for actionable insights."
> "Cutting-edge solutions that empower teams to drive impact."

Prompt to fix it:
```
No emojis. Avoid using em dashes — use commas or periods instead. Do not use any 
of the following words or any derivatives: unlock, leverage, harness, insights, 
democratize, explore, discover, dive in, elevate, enhance, witness, revolutionize, 
transform, embrace, unleash, dive, indulge, actionable, reveal, unmatched, delve, 
era, collaboration, cutting-edge, matters, impact, fusion, advancing, navigate, 
drive, problem solver, changemaker, game changer, ensure, transformational, 
powerful, derailed, delighted, cheat code.
```

---

### 5. NO_SPECIFICS — vague claims without evidence

The sentence makes an assertion but contains no concrete detail. Readers stop trusting writing that stays abstract for too long.

What it looks like:
> "A tool that helps teams move with clarity and get answers faster."
> "A solution that helps companies make better decisions."

Prompt to fix it:
```
Avoid vague claims without specifics. Include numbers, concrete examples, named 
tools, or measurable outcomes when possible.
```

---

## Why these patterns keep appearing

Language models are trained on massive collections of persuasive writing — blog posts, LinkedIn content, marketing copy, keynote transcripts. The patterns above are common in that training data because they were effective at one point. When millions of people start using the same model, those structures appear everywhere at once and readers begin to recognize the rhythm before they can articulate what is wrong.

Removing the em dash was a surface fix. The structure underneath did not change. That is why people can still sense slop even in writing that has been cleaned up at the punctuation level.

---

## The master prompt

Paste this block at the end of any copy prompt. It must come last — after your context, after your instructions, after your examples. Placing it at the beginning reduces its effectiveness. The reason is not fully understood, but in practice it consistently performs better as the final instruction.

```
No emojis. Avoid using em dashes; use commas or periods instead. Do not use any 
of the following words or any derivatives: unlock, leverage, harness, insights, 
democratize, explore, discover, dive in, elevate, enhance, witness, revolutionize, 
transform, embrace, unleash, dive, indulge, actionable, reveal, unmatched, delve, 
era, collaboration, cutting-edge, matters, impact, fusion, advancing, navigate, 
drive, problem solver, changemaker, game changer, ensure, transformational, 
powerful, derailed, delighted, cheat code.

If there are titles or headers, write them as direct one-liners under 10 words 
based on the actual insight, not the topic category. Titles can be informal but 
they need to say something specific.

Avoid contrastive negation, antithesis, and rhetorical contrast. No "X, not Y" 
constructions. Write in a natural, conversational tone.

Avoid sentence fragments, anaphora, and asyndeton. Do not use short standalone 
phrases or stacked clauses without conjunctions. Write in complete, naturally 
flowing sentences.

Avoid repeated sentence openings across multiple sentences and vary sentence 
structure so the same word or phrase does not begin consecutive sentences.

Do not structure paragraphs around rhythmic rhetorical patterns that sound like 
speeches or persuasion frameworks. Prioritize clarity over dramatic phrasing.

Avoid colon-based dual clause titles or headings that try to simulate depth. 
Write titles that describe the idea directly.

Remove buzzwords, hype language, and filler adjectives. Replace vague 
marketing-style phrasing with clear descriptions of what actually happens.

Avoid vague claims and include concrete examples, numbers, tools, constraints, 
or specific situations whenever possible so the writing contains real information.

Prefer straightforward explanation over rhetorical emphasis. Write sentences 
that sound like a thoughtful person explaining an idea, not a motivational post 
or keynote speech.

When editing text, simplify sentences that sound formulaic or generic and replace 
abstract language with precise wording that reflects a real observation or 
experience.
```

---

## How to use this in practice

For any piece of copy — blog, email, social post, landing page, ad, deck slide — build your prompt normally: give context, specify the audience, explain what the piece needs to do. Then paste the master prompt at the very end before hitting send.

For editing existing copy, paste the copy and the master prompt together and ask the AI to rewrite it according to those constraints.

For evaluating copy before publishing, paste it and ask: "Does any of this violate the constraints in the following prompt?" Then paste the master prompt. The AI will flag what it finds.

---

## Notes

- The master prompt is a constraint block, not a style guide. It tells the AI what not to do. You still need to give it the context, voice, and substance of what to write. Constraints protect the output; context shapes the thinking.
- This prompt was developed by running real examples of slop through an AI, identifying the grammatical structure behind each pattern, and building a targeted constraint for each one. The five labeled patterns above came from that process.
- The master prompt works for all copy types: blogs, LinkedIn posts, email campaigns, landing pages, ad copy, pitch decks, internal communications, and anywhere else writing needs to sound like a real person.
- Apply it last. Every time.
