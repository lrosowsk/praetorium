# Discovery interview guide

**Goal:** find out whether utility security and compliance teams have a real, funded problem with AI touching their operational systems. You are **not** selling. You are learning.

**Length:** 25–30 minutes. **Format:** video or phone, one interviewer plus one note-taker if possible.

## Ground rules

1. **Ask about the past, not the future.** “Tell me about the last time…” beats “Would you use…?” People are polite about hypotheticals and honest about history.
2. **Don’t pitch.** If they ask what you’re building, give one sentence and turn it back: “We’re exploring how utilities keep AI tools away from control systems. Before I say more, I’d love to hear how you think about it.”
3. **Listen for money, time and pain already spent.** Workarounds, spreadsheets, consultants, audit findings and budget lines are signals. “That’s interesting” is not.
4. **Shut up after a question.** Let silence do the work.
5. **Get the next step.** Every call should end with a referral, a follow-up or a no.

## Hypotheses we’re testing

| # | Hypothesis | Confirms it | Kills it |
|---|---|---|---|
| H1 | AI tools (vendor copilots, agents, analytics) are reaching OT or OT-adjacent systems now or within 24 months | Named tools, projects or vendor roadmaps | “We don’t allow AI anywhere near OT and won’t for years” from most interviewees |
| H2 | Security teams lack visibility into what AI touches | They can’t answer “which AI tools can reach your historian?” | They already inventory and govern AI well |
| H3 | Compliance (NERC CIP, board, insurer) is the trigger to buy | Audit findings, board questions, CIP-015 planning mention AI | AI governance never comes up in compliance work |
| H4 | There is budget for this, roughly $50–150K a year for a mid-size utility | Comparable tools bought at that price; named budget line | Only free tools or “we’d need a grant” |
| H5 | Co-ops and municipal utilities move faster than investor-owned ones | Pilot decision in under 6 months | Same or longer cycles as large utilities |
| H6 | Existing OT security tools (Dragos, Claroty, Nozomi) don’t cover AI governance | “Our Dragos shows traffic, not which AI did what” | Most say their current tool already identifies and controls AI agents |
| H7 | Watch-only deployment is acceptable to start | “We could put a passive sensor in” or “use our existing Dragos feed” | Even watch-only needs a multi-year approval |

After every 5 interviews, mark each hypothesis **supported / mixed / not supported** in `05-scoring-and-synthesis.md`.

## The script

### 1. Opening (2 min)

> Thanks for making time. I’m [name]. I’m researching how utilities are handling AI showing up in and around operational systems. This isn’t a sales call: I don’t have anything to sell you yet. I’m trying to learn what’s real and what’s hype. Is it OK if I take notes? Nothing you say will be quoted or attributed without your permission.

### 2. Their world (5 min)

1. What’s your role, and what does your team own?
2. Roughly how big is your environment? Customers served, generation, substations, control centers?
3. Who do you report to, and who else weighs in on OT security decisions?
4. What are the top two or three things keeping your team busy this year?

*Listen for whether AI comes up unprompted. Note it if it does.*

### 3. AI today (7 min)

5. Where is AI showing up in your organization right now? Anything from ChatGPT on laptops to vendor features.
6. Is any of it in or near operational systems: SCADA, EMS/ADMS, historians, asset management, engineering workstations?
7. Tell me about the last time someone asked to use an AI tool that touched operational data. What happened?
8. Have any of your OT vendors turned on AI features in their products? How did you find out?
9. Are engineers using AI coding assistants or agents for scripts, configs or ladder logic? How do you know?

### 4. Governance and visibility (6 min)

10. If I asked you today, “Which AI tools can read from or write to your control environment?”, how would you find the answer?
11. Do you have a policy for AI in OT? Who wrote it, and how is it enforced?
12. What’s the worst realistic thing an AI tool could do in your environment? Has anything close to that happened, here or at a peer?
13. How worried are you about attackers using AI against you? What, if anything, have you changed because of it?

### 5. Compliance and money (5 min)

14. How does AI come up, if at all, in NERC CIP work, audits, board meetings or cyber insurance renewals?
15. How are you approaching CIP-015 internal network security monitoring? Which tools are you looking at?
16. What did you buy most recently for OT security? Roughly what did it cost, and how long did it take from first call to signed contract?
17. If you had to solve AI visibility in OT this year, where would the money come from?
18. Which OT security tools do you run today (Dragos, Claroty, Nozomi, other)? Do they tell you what your AI tools are doing, and could they stop one?
19. If you needed to control what AI can reach in your control environment, which tools you already own would you try first?
20. Would you trust a control built by the same vendor whose AI it’s controlling, or would you want something independent?
21. What would it take to approve a watch-only sensor or software gateway in your environment? How long did your last OT tool take?

### 6. Close (3 min)

22. Is there anything I should have asked but didn’t?
23. Who else should I talk to, inside your organization or at a peer utility? Would you be willing to introduce me?
24. Once I have something to show, could I come back for 20 minutes of feedback?

*If the pain was strong:* offer the 5-minute demo, then: “Some utilities are helping us shape this as design partners: early access and input on the roadmap in exchange for feedback, with a paid pilot later. Would that interest you?”

## After the call (within 1 hour)

- Fill in `04-interview-notes-template.md` while it’s fresh.
- Score the call (rubric in `05-scoring-and-synthesis.md`).
- Update the row in `target-list.csv`.
- Send the thank-you email (template in `03-outreach-templates.md`) and any intros promised.

## Questions for adjacent roles

**OT engineers and operators:** What AI tools do you or your colleagues actually use day to day? What would you never let an AI do? What would make your job easier?

**Compliance managers:** Walk me through your last CIP audit. Where did you spend the most time gathering evidence? Has AI come up with auditors?

**OT security vendors and integrators:** What are utility clients asking you about AI? What gaps do you see that your products don’t cover?
