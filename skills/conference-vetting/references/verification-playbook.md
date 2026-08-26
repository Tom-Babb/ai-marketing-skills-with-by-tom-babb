# Verification playbook

Six checks. Each is independent, each is doable without contacting the organizer, and each has a failure mode that ends the evaluation on its own. Run them before drafting any reply — roughly half of cold conference outreach dies here, and dying here costs nothing.

Use WebSearch and WebFetch for all of it. When a lookup is inconclusive, say so; a dossier with three verified checks and three honest "couldn't confirm" lines is more useful than six confident-sounding ones.

## 1. Prior edition — third-party evidence

The single hardest signal to fake and the easiest to check. An event that ran last year leaves traces that the organizer didn't publish.

Look for: session recordings on YouTube or Vimeo; the event hashtag on X and LinkedIn filtered to last year's dates; recap posts written by *attendees*; press coverage from outlets that aren't listed as media partners; photos posted by people who were there.

Then Wayback the prior-year site and compare the advertised speaker list against any photo or video evidence of who actually appeared. At predatory events roughly a third of advertised speakers simply don't show up, and keynotes no-show — this has been documented firsthand more than once.

**Fails if:** an event claiming multiple prior editions has no third-party trace of any of them. Organizer-published photo galleries don't count; they're free to stage or lift.

## 2. Domain age against the claimed history

Fetch `https://rdap.org/domain/<domain>` for registration date, registrar, and status. Check the Wayback Machine's first capture (`http://archive.org/wayback/available?url=<domain>`, or the CDX API for the full capture history).

Compare against what the site claims. A "10th Annual Summit" on a nine-month-old domain with no archive history is disqualifying by itself.

Also worth noting: registrant privacy combined with no corporate entity findable anywhere; a domain that re-registers annually with the year baked in (`event2026.com`); a subdomain piggybacking on a generic host; or a domain one character off a real event's.

## 3. Speakers — do they exist, and did they agree?

Reverse-image-search the headshots. Stock photography, reused faces across unrelated summits, and AI-generated faces (check ears, earrings, background warping) are all common.

Then check whether the named speakers have promoted it themselves. Every real keynoter posts about their own talk. A senior engineer at a major company with no LinkedIn or conference footprint at all is not a real person.

This is where DevTernity collapsed in 2023: fabricated women speakers with invented Coinbase and Microsoft affiliations, unravelled the moment someone asked the companies. And the FTC's judgment against OMICS specifically bars claiming people "have agreed to participate" when they haven't — because that misrepresentation is the core of the fraud, not a peripheral detail.

**The kill shot, when it's warranted:** contact two listed speakers through their own channels and ask whether they've signed a speaker agreement. Suggest this to the user rather than doing it unprompted — it's outreach in their name.

## 4. Venue — booked, or "partnered"?

Most convention centers and large hotels publish a public event calendar. Check whether the date is on it.

Watch the language on the event site. "Official venue partner," "in association with [Hotel]," and "a 5-star venue in central London, details to follow" are all ways of not saying "we have a signed space contract." Real events name the hall.

The definitive version is a phone call to the venue's events desk asking whether the organizer has contracted space for those dates — flag this as a step the user can take, since it's a phone call rather than a lookup.

Also check the "official hotel partner" against the hotel itself. Fake housing partners are a well-documented parasite business around real and fake events alike.

## 5. Legal entity

Search OpenCorporates, Companies House, or the relevant Secretary of State for the entity named on the site or the invoice.

Check: incorporation date, active vs. dissolved status, registered address (a mail drop or virtual office is a flag), and the officers. Then search those officers' names — operators frequently run several "summit" entities at once, and dissolve-and-reincorporate annually to outrun chargebacks.

**Fails if:** no legal entity is named anywhere on the site, or the entity is a shell incorporated months ago, or the entity's jurisdiction is unrelated to both the event and the staff.

## 6. Staff

Search the organizing company on LinkedIn. A real event has named staff with corporate email addresses and a phone number that reaches a human.

**Fails if:** zero employees findable, and the only contact channels are a free mailbox and a WhatsApp number while the site displays a corporate domain.

---

# Phrasebook: lines that recur in predatory outreach

None of these is proof on its own. Two in one email is a pattern worth naming in the dossier.

| Line | What it indicates |
|---|---|
| "Our scientific committee would like to offer you the position of Speaker." | Flattery-first outreach. In one study, fraudulent organizers invited 73% of recipients to *speak* and only 24% to attend — the speaker offer is the mass-market channel, not an honor. |
| "Please don't miss the last chance — the deadline is Friday." | Manufactured urgency. On a fake event the "limited slots" number never changes across weeks. |
| "Let's get you on a quick call to walk through the packages." | Refusal to put price in writing. Legitimate events attach the rate card. This is the most reliable single tell in the category. |
| "You've been shortlisted for the [X] Award." | Awards you didn't enter are sold, not won. Documented pricing runs into the thousands, with awards going exclusively to sponsors and judging seats sold separately. |
| "We can provide the full attendee list with verified emails." | Immediate disqualification. Real organizers publicly state they never sell attendee contact data; this is the parasite-vendor business, and the sender is often not affiliated with the event at all. |
| "Kindly revert back at the earliest so we may do the needful." | Weak on its own. Combined with a scraped name, a misapplied honorific, or a field mismatch, it fits the template. |

Two structural tells live in the *thread* rather than any single message: the first reply always pushes to a call instead of sending a rate card, and a second sender with a different signature block ("Sponsorship Director") appears once you engage.

One more: impersonation of real media and event brands is now common enough that the sender's domain deserves its own look. TechCrunch has published a list of two dozen lookalike domains used to run fake "media inquiry" outreach at companies. Check the sending domain character by character against the real one.

---

# Sources

- FTC v. OMICS Group — https://www.ftc.gov/news-events/news/press-releases/2019/04/court-rules-ftcs-favor-against-predatory-academic-publisher-omics-group-imposes-501-million-judgment
- The Register on DevTernity — https://www.theregister.com/2023/11/28/devternity_conference_fake_speakers/
- ICIJ, "Fake Science Factories" — https://www.icij.org/inside-icij/2018/09/undercover-reporters-expose-bogus-scientific-conferences/
- PCMA on predatory conferences — https://www.pcma.org/fake-predatory-conferences/
- BizBash, how event vendors spot scams — https://www.bizbash.com/production-strategy/opinion-experts/article/22889332/how-event-vendors-can-spot-scams
- AAM attendee-list and hotel scam warning — https://annualmeeting.aam-us.org/attendee-list-hotel-scam-warning/
- TechCrunch on impersonation outreach — https://techcrunch.com/2026/03/05/impersonators-scammers-targeting-companies-with-fake-techcrunch-outreach/
- Think. Check. Attend. — https://thinkcheckattend.org/
- AAM/BPA event attendance audits — https://auditedmedia.com/industry-certifications/events
- OpenCorporates — https://opencorporates.com/

---

# When you have browser access

LinkedIn, Facebook and Instagram all block automated fetching, and they hold the evidence that matters most: what actual attendees said, unprompted, at the time. With Chrome tools available and the user already signed in, these become the highest-yield checks in the whole playbook.

**Prior editions.** Search the event name on LinkedIn and filter to the dates of last year's edition. You're looking for posts by attendees rather than the organizer — "great few days at X," photos of the room, people thanking speakers. A real event of 150 people generates a dozen of these. A photo of the actual room also settles attendance claims faster than any number the organizer gives you: count the chairs.

**The sender.** Open their profile. How long have they been in the role? Is the events history real? Someone who ran a large community conference for two years is a different proposition from a profile created last quarter.

**The company.** The company page shows a real employee count, post history, and whether the organization has any life outside this one event.

**Speakers.** Check whether the listed speakers posted about speaking. Silence from a headline name is a genuine signal — real keynoters promote their own talks.

**The hashtag.** Prior-year event hashtags on LinkedIn and Instagram surface vendor and attendee content that never gets indexed by search.

Read-only, always. The user is signed in as themselves; don't connect, message, follow, react, or post from their account, and never ask for credentials. If reaching out to a speaker looks like the decisive move — and sometimes it is — recommend it and draft it, but leave the sending to them.
