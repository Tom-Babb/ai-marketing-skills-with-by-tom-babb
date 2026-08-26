# Dossier structure

Write for someone who wasn't in the room while you researched — usually whoever owns the budget. They should be able to disagree with the recommendation and still find the evidence useful.

Deliver as HTML for a Pursue or Real-not-ours verdict, and render it to PDF with `scripts/html_to_pdf.py` when it's going outside the company. For an Archive verdict a short in-chat writeup is usually enough, but still show the evidence — the user may need to explain the decision to someone.

## Structure

**Header.** Event name as the title. Beneath it: organizer, sender and date of the approach. Then a row of facts — dates, venue, the ask, the price (or "not quoted," which is itself information).

**Verdict, first thing.** Pursue / Real, not ours / Archive, as a sentence a person could repeat in a meeting. Then two or three short paragraphs: what the checks found, the one thing that decides it, and what to do. Someone should be able to read only this block and act correctly.

**Screen 01 — Is it real?** A table: check, status, what you found. Status is `Verified`, `Organizer-claimed`, `Thin`, or `Could not check` — keep these visible rather than flattening them into prose. Close with an explicit note on which predatory markers are present or absent; naming their absence is as useful as naming their presence, because it stops the reader over-reading the flags that follow.

**Flags.** Only the discrepancies that change the decision. Each one: what the organizer claims, what the evidence says, what the gap plausibly means, and the specific question that would settle it. Be careful here — most flags have a boring explanation, and the dossier is more persuasive when it says so.

**Screen 02 — Is the room ours?** The audience case for and against, side by side, with the strongest version of each. If there's a market or timing argument in play, evidence it properly; a verifiable external trend is often the strongest thing in the whole document.

**The arithmetic.** Realistic attendance (independently observed, not claimed), qualified subset, cost of each instrument on offer, cost per person in the room, and what the cheaper instrument doesn't buy. State the assumptions inline so they can be replaced when real numbers arrive.

**Recommendation.** Numbered, sequenced, each step something a person does. Include what to settle internally before replying, what to ask for before discussing money, and what would change the answer next cycle.

**Evidence.** Every source as a link, grouped roughly by what it establishes. This section is what makes the dossier forwardable.

## Tone

Concrete over hedged. "The only independent headcount is 130, against a claimed 450" beats "attendance figures may be optimistic." Where you're uncertain, be specific about the uncertainty rather than softening the whole sentence.

Give the organizer the benefit they've earned. A real event with sloppy marketing reads very differently from a fake one, and conflating them costs the user a relationship. If the finding is "legitimate but not worth sponsoring," the document should make that easy to say warmly.
