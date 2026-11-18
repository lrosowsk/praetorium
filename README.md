# Preceptor Defense

**The human sign-off for AI in critical infrastructure.** Preceptor Defense ("Preceptor" for short) is a policy layer between AI (vendor copilots, engineering agents, analytics models) and the operational systems that run the grid. It discovers what AI can reach, enforces what it may do, detects machine-speed attacks, and produces audit evidence for regulators.

A preceptor is the one who sets the rules others must follow. The product borrows the utility “hold point”: a step nobody may pass until a qualified person signs off. Preceptor is the working name: web searches found no company using it and only cancelled PRECEPTOR trademarks, but run a full USPTO search before filing (see `research/name-check.md`).

## Where we are

Pre-product, in customer discovery. The plan is to **validate before building**: 30 interviews with utility security and compliance leads, aiming for 3 pilot letters of intent, then a prototype.

## What’s in this repo

| Path | What it is |
|---|---|
| `discovery/01-interview-guide.md` | The interview script, hypotheses under test, and ground rules |
| `discovery/02-target-list.md` | Who to talk to, the interview mix, and where to find people |
| `discovery/target-list.csv` | Tracking sheet for every contact (opens in Excel or Google Sheets) |
| `discovery/03-outreach-templates.md` | Cold email, LinkedIn note, follow-ups, warm-intro and thank-you templates |
| `discovery/04-interview-notes-template.md` | Copy for each interview |
| `discovery/05-scoring-and-synthesis.md` | Scoring rubric, synthesis table, decision rules, pilot LOI template |
| `discovery/06-one-page-brief.md` | Research brief to send ahead of calls |
| `research/market-facts.md` | Every number in the deck, with sources and confidence |
| `research/name-check.md` | Trademark check for the Preceptor name |
| `discovery/prospects.csv` | 61 organizations to contact first, prioritized (guide in `prospects.md`) |
| `demo/` | Working prototype: AI agents, a simulated substation, the Preceptor gate and dashboard |
| `deck/project/` | Source files for the pitch deck (one HTML file per slide) |

## The pitch deck

The deck is published at **https://claude.ai/artifact/TEbnr6VxraKc357uZLCqgs**. It’s private until shared from its Share menu, and it can be exported to PowerPoint or PDF from there.

`deck/project/` holds its source: `deck.json` (slide order and fonts), `deck.css` (shared styles) and `slides/*.html` (one per slide, with speaker notes in each `<aside>`). Placeholders in `[brackets]` still need real values: founder details, raise amount, pricing, traction and the beachhead calculation.

## Next steps

1. Fill the target list and start outreach (10–15 messages a week).
2. Run interviews; synthesize every 5.
3. Recruit an OT/ICS co-founder or advisors along the way.
4. After 30 interviews, apply the decision rules in `05-scoring-and-synthesis.md`.
5. Update the deck with real quotes, traction and pricing.
