---
name: google-ads-with-ai
description: Build and manage Google Search Ad campaigns using AI to replace the strategy, copywriting, keyword research, and reporting that agencies charge thousands of dollars a month to do. Use this skill whenever someone needs to set up a Google Ads campaign, audit an existing one, or replace an agency managing paid search. Triggers include: "set up Google ads," "replace our ads agency," "build a search campaign," "write Google ad copy," "research keywords for ads," "set up campaign reporting," or any request involving Google paid search. Always use this skill before paying an agency or spending more than an hour on a campaign manually.
---

# Google Ads with AI

A Google Search Ads agency charges $4,000 or more a month to do keyword research, write ad copy, build campaigns, and send you a weekly report. This skill replaces all of that. The full workflow takes about 10 minutes to run and about 30 minutes total including setup.

## What you need

- A Google Ads account
- Access to Manus (or ChatGPT, Claude, or Perplexity for the research step)
- Pipeboard installed and connected to your Google Ads account
- Access to Claude with the Pipeboard MCP connector enabled

---

## How Google Search Ads actually work

Before running the workflow, understanding the structure saves a lot of confusion.

A campaign contains ad groups. Each ad group targets a set of keywords. For each keyword, you need ad copy — Google recommends around 10 headline and description variations per ad group so it can test which combinations perform best. Keywords also have match types: exact match means the ad only shows for that specific query, phrase match means it shows for queries containing that phrase, and broad match means Google decides when it's relevant. Match type selection affects both cost and quality of traffic significantly.

An agency earns its retainer by doing the research to figure out which keywords to buy, which match types to use, what the intent behind each keyword is, and then writing all the copy. That's what this skill automates.

---

## Step 1 — Build the campaign report

Open Manus (or any capable AI with web research ability) and dump everything relevant into a single prompt. Include:

- What your product or service does
- Who you are trying to reach (job title, company type, situation)
- What action you want them to take (book a demo, sign up, download)
- Any competitors you know about
- Any keywords you already know you want to target
- Your budget range if you have one

Then add this instruction at the end:

> "Research best practices for Google Search campaigns. Then build a complete campaign report that includes: recommended keywords, the match type for each keyword, the search intent behind each keyword, the recommended ad group structure, and at least 8 headline and 4 description variations per ad group. Format it as a structured document I can hand directly to someone building the campaign."

Manus will come back with a full report. Review it. If anything looks off — wrong audience, wrong keywords, wrong messaging — correct it before moving to the next step. This report is the source of truth for the entire campaign.

---

## Step 2 — Connect Google Ads via Pipeboard

Pipeboard is a connector that gives Claude access to your Google Ads account. Install it at pipeboard.co and connect your Google Ads account. Once connected, enable the Pipeboard MCP in Claude.

You only have to do this once. After setup, Claude can read and write to your Google Ads account directly.

---

## Step 3 — Build the campaign in Claude

Open a new Claude session with the Pipeboard MCP enabled. Paste the full Manus report and give Claude a single instruction:

> "Using this report, build the complete Google Ads campaign in my account. Create the campaign, ad groups, keywords with the correct match types, and all ad copy exactly as specified in this report."

Claude will work through the report and build everything. When it finishes — typically within a few minutes — go into your Google Ads account and verify that the structure matches the report. Check that keywords have the right match types, that ad copy is loaded, and that the campaign settings look correct before turning anything on.

---

## Step 4 — Set up daily reporting

Once the campaign is live, set up a daily reporting loop so you get the same information an agency would send you in a weekly report, every morning automatically.

In the same Claude session, give it this instruction:

> "Every morning at [time], pull the performance data from my Google Ads account and send me a report that includes: cost per click, impressions, clicks, CTR, conversions, and cost per conversion broken down by campaign and ad group. Format it the same way as this report I'm sharing from our previous agency."

Give it a sample report from your old agency or describe the format you want. Claude will set the schedule and generate the report from your live account data each morning.

---

## What this replaces

| Agency task | AI replacement |
|-------------|---------------|
| Keyword research | Manus research step |
| Match type strategy | Included in the Manus report |
| Ad copywriting | Included in the Manus report |
| Campaign build | Claude + Pipeboard MCP |
| Weekly reporting | Claude daily report loop |
| Monthly strategy review | Re-run the Manus report with updated context |

---

## Notes

- Review the Manus report before giving it to Claude. The report is only as good as the context you gave it. If you dumped vague information in, you will get vague keywords and generic copy out. Be specific about your audience and what makes your product different.
- Do not turn the campaign on until you have reviewed the build in Google Ads. Claude builds what the report says, but Google Ads has a lot of small settings — bidding strategy, location targeting, ad scheduling — that may need manual adjustment based on your situation.
- The daily reporting loop requires keeping the Claude session or project active. If you close the session, re-run the reporting instruction in a new session with the Pipeboard MCP connected.
- This workflow works for new campaigns. For auditing and optimizing existing campaigns, give Claude access via Pipeboard and ask it to review performance data and recommend changes. Same connector, different prompt.
- Google's own AI features inside the Ads interface are separate from this workflow. This workflow gives you more control and transparency than Google's automated recommendations.
