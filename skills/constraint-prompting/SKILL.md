---
name: constraint-prompting
description: Build AI prompts that produce clean, on-brand marketing copy by separating context (what the AI needs to understand) from constraints (what the AI must never do). Use this skill whenever someone needs to write a prompt for marketing copy, social posts, blogs, emails, or any brand writing — especially when previous AI outputs have come back generic, sloppy, or off-voice. Triggers include: "the AI keeps writing generic copy," "how do I prompt for better writing," "write me a prompt for X," "the output sounds like AI," "how do I get Claude to write like me," or any request to improve AI writing quality. Always use this skill before writing any marketing prompt from scratch.
---

# Constraint Prompting

Generic prompt → generic output. The reason AI copy sounds like AI copy is almost always a prompting problem, not a model problem. This skill fixes that.

## The two-part structure

Every effective marketing prompt has two distinct jobs:

**Context** — Everything the AI needs to understand before it starts writing. The brand, the audience, the goal, the tone, the specific piece of content. Context shapes the thinking.

**Constraints** — The rules that prevent known failure modes. Not suggestions. Hard rules that block the AI from producing output you'd never use. Constraints protect the output.

Most people write prompts that are all context and no constraints. The AI understands what to write but has no guardrails on how not to write it. Slop gets through.

---

## Building the context block

Context answers: what is this, who is it for, what should it do?

Include:
- What you're writing (blog, LinkedIn post, email subject line, etc.)
- Who the audience is — be specific, not demographic
- What the piece should accomplish (drive a click, explain a concept, start a conversation)
- Voice and tone reference — either describe it or point to an example
- Any specific facts, angles, or insights that must appear

The more specific the context, the less the AI has to guess. Guessing is where slop comes from.

---

## Building the constraint block

Constraints answer: what must this never do or sound like?

Start with the five labeled slop patterns and add constraints for each one that applies:

**BUZZWORD_GENERIC** — words that sound impressive but say nothing
```
Avoid: unlocking, transformative, cutting-edge, empower, leverage, revolutionize, 
seamless, robust, innovative, game-changing. Replace with specific, plain language.
```

**DUAL_CLAUSE_TITLE** — the "X, not Y" construction that's everywhere on LinkedIn
```
Avoid contrast-based sentence structures and rhetorical opposition. 
Explain ideas directly without defining them through comparison with another concept.
```

**NO_SPECIFICS** — claims without evidence or examples
```
Every claim needs a specific detail, number, example, or observation to back it up. 
No assertions without evidence.
```

**NO_AUDIENCE** — writing that could apply to anyone
```
Write as if addressing [specific person / role / situation]. 
The reader should feel like this was written for them, not a category they belong to.
```

**PREMATURE_STRUCTURE** — bullet points and headers before the idea deserves them
```
Write in prose. No bullet points, numbered lists, or headers unless explicitly requested. 
Vary sentence structure and length. No repeated sentence openings across a paragraph.
```

**Additional structural constraints to add when relevant:**
```
Avoid anaphora and repeated opening phrases. Do not repeat the same beginning 
across multiple sentences. Write sentences with varied structure and natural flow.
```

```
No em dashes. No sentence fragments used for dramatic effect. 
No "Here's the thing:" or "Let's be honest:" openers.
```

---

## The full prompt structure

```
[CONTEXT]
You are writing [piece type] for [brand/person].
The audience is [specific description].
The goal is [specific outcome].
Tone: [description or reference example].
Key information to include: [facts, angles, insights].

[CONSTRAINTS]
- Avoid buzzwords: [list specific ones relevant to this brand]
- No contrast framing ("X, not Y" structures)
- No bullet points or headers
- No repeated sentence openings
- No em dashes
- Every claim needs a specific supporting detail
- Write as if speaking to [specific person], not a general audience
```

---

## Context tools worth knowing

**Granola** — transcription tool for capturing meetings and conversations. The raw transcript becomes context you can drop directly into a prompt. Real conversations produce the most specific context.

**Timeglass** — screen time and activity tracking. Useful for understanding how your audience actually spends their time — can inform what problems they're solving and what language they're using.

Both feed the context block. The more raw, specific input you give the AI before it writes, the less it has to invent.

---

## Evaluating output

Before accepting any AI-written copy, run it through this check:

1. Could this have been written about any company in this space? If yes, it failed the specificity test.
2. Does it use any words from the buzzword list? If yes, revise.
3. Do multiple sentences start the same way? If yes, rewrite for variation.
4. Could you identify the specific audience from the copy alone? If no, it's not targeted enough.
5. Does it sound like a real person thinking out loud? If no, it's still slop.

If it passes all five, it's ready. If not, add the failing constraint back into the prompt and regenerate.

---

## Notes

- Removing the em dash did not fix your AI writing. The slop patterns are structural, not punctuation-level. Fix the structure.
- Constraint prompting is an evaluation problem. You need criteria before you can judge output. Define the criteria first, then write the prompt, then evaluate the output against the same criteria.
- The constraint block is cumulative. Every time you get output you'd never publish, add the failure mode as a new constraint. Your prompts get better with each bad output.
- Context is about meaning and relevance. Constraints are about failure prevention. Keep them separate in your prompt — it makes debugging easier when output is wrong.
