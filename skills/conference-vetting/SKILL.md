---
name: conference-vetting
description: Research and vet inbound conference, summit, expo, awards, and event outreach — a desk check that establishes whether the event is real, an audience check against who you actually sell to, a dossier of the findings, the questions to send the organizer, and a read on their reply. Use this skill whenever someone forwards, pastes, or screenshots a conference invitation, a sponsorship or exhibitor prospectus, a speaking invitation, an awards nomination, or a booth or partnership pitch, and whenever the user asks "is this conference legit", "should we sponsor this", "have you heard of this event", "is this worth our time", "who runs this", or wants an event checked out before replying. Also use it when an organizer's reply to those questions comes back and needs grading. Trigger even when the user shares only a URL or an organizer's name with no framing, and even when they sound like they've already decided — the research is the point.
---

# Vetting inbound conference outreach

Cold conference outreach is high-volume with a wide quality range. At the bad end sit operations whose whole revenue model is selling speaking slots, booths, and awards to people flattered into a call — documented well enough to have produced FTC judgments and collapsed conferences. At the good end sit real, well-run events aimed at the wrong audience for us. Both end in a decline, but for different reasons and with different follow-up, so the analysis has to keep them apart.

The output is a written dossier the user can forward to whoever owns the budget. Every claim in it has to survive being read by someone who wasn't there when you researched it.

## Two questions, asked in order

**Is the event real?** Verifiable facts about the organizer, venue, speakers, prior editions, and money.

**Is the room ours?** Legitimacy is not fit. A well-run event aimed at the wrong buyer is still a decline, and the reason has to be stated as such. Before scoring anything, write down who actually holds the budget for what you sell — the title that can authorize the spend — and be honest about which parts of the audience only *look* valuable. The most common way an event evaluation goes wrong is mistaking a room full of interesting people for a room full of buyers.

Keep that definition in a file of your own at `references/audience-fit.md` and point the analysis at it, so the part that goes stale lives in one place. Everything else in this skill is general-purpose event forensics.

Run legitimacy first. If the event fails it, the fit analysis is wasted and including it muddies the recommendation.

## Process

### 1. Intake

Pull from whatever the user pasted or screenshotted: event name, dates, city, venue, organizing entity, sender name and email domain, the specific ask (speak / sponsor / exhibit / award / attend), price if stated, and every number claimed. Note what's *missing* — a prospectus with no legal entity and no price is itself a finding.

Watch for claims the email makes about **us**: "welcome you back as a sponsor," "as we discussed last year," "several of your competitors are already in." These are checkable, and when they turn out to be unsupported they tell you how much of the rest was written from records rather than momentum. Flag them for the user to confirm internally rather than asserting they're false.

If the user gave only a name or a URL, start there and don't ask them for more. The research is what they wanted.

### 2. Desk check — six verifications, run in parallel

`references/verification-playbook.md` has the method for each, the exact lookups, and what separates a pass from a fail. In one line each:

1. **Prior editions** — third-party evidence it happened, not organizer-published.
2. **Domain age** — registration date and first archive capture against the claimed edition count.
3. **Speakers** — do the named people exist, and have they said anything themselves?
4. **Venue** — is the date contracted, or is this "venue partner" language?
5. **Legal entity** — incorporation date, status, officers, and whether those officers run other summits.
6. **Staff and sender** — real people with a real history, or a Gmail address and a WhatsApp number?

Spawn subagents for these where the environment offers them; they're independent and each involves several lookups. Where something is genuinely inconclusive, record it as inconclusive. Fabricating a verification is worse than admitting a check didn't land, because the user is going to act on this.

### 3. Fit analysis

Only for events that survive step 2. Read your `references/audience-fit.md` and score the room on six things, roughly in order of how much they move the decision:

**Buyer density.** What fraction of last year's attendees held titles that can authorize the spend? This is the number the whole evaluation turns on. Ask for the breakdown by job title and seniority; if the organizer won't produce one, assume the answer is unflattering.

**Named accounts.** Run last year's attendee company list against your current customers and target list. Named accounts in the room is the only attendance figure that matters — a 2,000-person event with none of them is worth less than a 120-person event with fifteen.

**Mechanism.** Curated 1:1 meetings, a hosted-buyer program, a meeting room, a hosted dinner, a workshop slot. Booth traffic is a weak channel; scheduled conversations are the value. Ask what number of meetings sponsors averaged last year.

**Vendor density.** If the sponsor floor is mostly vendors selling to each other, it's a vendor-to-vendor event wearing a buyer's badge. Ask for the buyer-to-vendor ratio; an organizer who has never calculated it is telling you something.

**Distribution.** Are sessions recorded, do you get the file, and can you cut and post it? One good recorded talk outlives the event by a year, and this can carry an otherwise marginal event.

**Counterfactual.** A day at a conference costs a day of outbound plus travel plus the fee. Say which looks better.

Then do the arithmetic out loud. Attendance claims tend to inflate — compare the organizer's number against any independently observed headcount, and price the opportunity against the smaller one. Work out cost per person in the room for each instrument on offer (ticket, booth, sponsorship, hosted dinner), and say plainly which one the evidence supports. Frequently the answer is "attend this year, sponsor next year once you know the room converts" — that's a real recommendation, not a hedge.

### 4. Verdict

One of three, stated plainly with the evidence that drove it:

- **Pursue** — legitimacy clean, buyer density real, and a mechanism to reach them.
- **Real, not ours** — checks out, audience is wrong. Decline warmly; honest organizers are worth staying in touch with and audiences change.
- **Archive** — a legitimacy kill shot, or a refusal to put price and numbers in writing. Don't negotiate the price down; the price was never the problem.

If the evidence is genuinely mixed, say so and name the one question that would settle it, rather than splitting the difference into a non-recommendation.

### 5. Dossier, then questions

Write the dossier to `references/dossier-template.md`. Then draft the outbound questions from `references/question-bank.md`, selected for what's *still* unknown after the research — never ask for something you already found, it wastes the user's credibility.

### 6. Grade the reply, when it comes

The organizer's response is itself evidence, and often better evidence than anything on their website. When the user brings a reply back, read `references/question-bank.md` for how to grade it. In short: what arrived attached versus deflected, how long it took, whether a second sender with a different signature appeared, and above all whether numbers and prices came back in writing or got redirected to a call. A real organizer has the post-event report and the rate card sitting in a folder and sends both in one reply; steering everything to a call is a pricing tactic, not an admin delay.

## Using browser access

Much of the best evidence lives on LinkedIn, which blocks automated fetching — so when Chrome browser tools are available, use them. They're usually the difference between "couldn't confirm" and a verified finding.

What's worth the browser: attendee posts and photos from prior editions (search the event name filtered to last year's dates); the sender's profile, tenure, and history; the organizing company page and its real employee count; whether listed speakers posted about speaking there themselves; and the event hashtag. Facebook and Instagram recaps are similarly gated and similarly useful.

Two boundaries. The user is already signed in — never ask for or enter credentials. And this is read-only reconnaissance from the user's own logged-in account: don't connect, message, follow, react, or post. Approaching a speaker to ask whether they signed an agreement is a legitimate and sometimes decisive move, but it's the user's call and their name on it, so recommend it rather than doing it.

## Making claims about real companies

This dossier can end up saying a named, real organization is running a scam. Sometimes that's correct and the user needs to hear it. The standard for saying it is evidence, not pattern-matching.

Label every finding by how well it's established — verified, organizer-claimed, or could-not-check — and keep those labels visible in the dossier rather than flattening them into confident prose. Separate what you observed ("the domain was registered in March 2026") from what you infer ("which contradicts the '8th annual' claim"). One red flag is a question; a cluster is a pattern; neither is proof, and the dossier should be checkable by someone who wants to redo your work.

Where the honest answer is "this looks like a weak event but I can't demonstrate anything improper," write that. It's still a decline, and it's more useful than an overreach that falls apart when the user forwards it.

## Reference files

- `references/verification-playbook.md` — how to run each desk check, plus the phrasebook of lines that recur in predatory outreach
- `references/audience-fit.md` — not included: write your own. Who you sell to, which titles hold the budget, and which parts of the audience only look valuable. **Edit this file when the audience changes.**
- `references/question-bank.md` — the questions, what good and bad answers look like, and how to grade the reply
- `references/dossier-template.md` — the output structure
- `scripts/html_to_pdf.py` — render a finished HTML dossier to a shareable PDF
