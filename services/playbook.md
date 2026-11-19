# Delivery playbook: AI in OT Risk Assessment

How to run an assessment from signed proposal to final readout. Times are for the **Full Assessment** (4–6 weeks); the **Snapshot** follows the same steps with interviews and questionnaires only, and no lab testing or tabletop.

**Golden rule: never touch live control systems.** We read documents, configurations, logs and existing sensor data. Anything active happens in our lab.

---

## Week 0: Kickoff

- [ ] NDA and statement of work signed (`proposal-template.md`).
- [ ] Rules of engagement agreed and signed (`rules-of-engagement.md`).
- [ ] Name a customer sponsor and a day-to-day contact; agree the escalation path for anything urgent found.
- [ ] Send the intake questionnaire (`intake-questionnaire.md`), due back within 5 business days.
- [ ] Request data exports (see “Data to request” below).
- [ ] Schedule interviews and site days.
- [ ] Set up a dedicated, encrypted engagement folder. Customer data never goes into shared or AI tools without written permission.

### Data to request (customer provides exports; we never pull)

| Data | Why |
|---|---|
| Asset inventory of OT and engineering systems | Know what exists |
| Network diagrams, especially IT/OT boundary and remote access paths | Find how AI could reach OT |
| Firewall, web proxy and DNS logs (30 days) for the IT/OT boundary, engineering workstations and the OT demilitarized zone | Find AI service traffic (run `tools/ai_traffic_scan.py`) |
| Installed software list for engineering workstations and jump hosts | Find AI tools and extensions |
| Vendor list with recent release notes for control system software (SCADA/EMS/DMS/historian/asset management) | Find vendor AI features |
| Vendor contracts or terms covering data use and AI | Find what vendors may do with customer data |
| Existing OT monitoring data (Dragos, Claroty, Nozomi exports), if any | Reuse what they already have |
| Relevant policies: acceptable use, remote access, change management, any AI policy | Find policy gaps |

## Week 1–2: Discover

**Interviews (45 minutes each).** Use the questions in `intake-questionnaire.md` as the guide.

| Who | Focus |
|---|---|
| CISO or security lead | AI policy, approvals, incidents, compliance pressure |
| OT/SCADA manager and control room lead | AI features in control software, who can change what |
| Engineering (protection, automation, substation) | AI coding assistants, scripts, agents, tools on engineering workstations |
| Data and analytics team | Models in production, what data they read, whether outputs drive actions |
| Compliance manager | NERC CIP evidence, auditor questions, AI in audit scope |
| Procurement / vendor management | Vendor AI disclosures, contract terms |

**Technical discovery (all passive):**
- Run `tools/ai_traffic_scan.py` over the DNS and proxy logs to find which hosts talk to AI services, and how often.
- Review engineering workstation software lists for AI tools, IDE extensions and agent frameworks.
- Read vendor release notes for AI features, and check whether they’re enabled.
- Review existing OT monitoring data for unusual automated activity patterns.

**Output:** a draft AI inventory, one row per AI system, in `risk-register-template.csv`.

## Week 2–3: Assess

For every AI system in the inventory, fill in the risk register:

1. **Owner and purpose.** Who uses it and why.
2. **Reach.** What it can read, what it can write, and the path from the AI to control systems (direct, via an engineering workstation, via vendor software, none).
3. **Credentials.** Whose identity it acts as, and whether those permissions are broader than it needs.
4. **Human in the loop.** Does a person approve its actions before they take effect?
5. **Physical consequence (1–5).**
   1 = reads non-sensitive data only
   2 = reads sensitive operational data
   3 = can change non-safety configurations or schedules
   4 = can change setpoints or control parameters
   5 = could operate breakers, valves or safety systems
6. **Likelihood (1–5)** of misuse or error: exposure to untrusted input (prompt injection), permissions, maturity, vendor controls.
7. **Risk = consequence × likelihood.** 15+ is high, 8–14 medium, under 8 low.

Pick the **top 3–5 paths** for lab testing.

## Week 3–4: Test (lab only)

- Rebuild each top-risk path in the simulated substation (`../demo/`), adjusting `points.json` and `policy.json` to mirror the customer’s setup.
- Typical scenarios:
  - an AI agent with tool access is fed malicious instructions through a document, ticket or email (prompt injection) and tries a control action
  - an over-permissioned credential lets an AI tool reach systems it shouldn’t
  - a vendor AI feature issues commands that look like normal operator activity
  - machine-speed scanning by a compromised AI tool
- Record what happens with and without the recommended controls (human approval, per-agent rules, scanning detection). Screenshots from the dashboard and the evidence report make strong report exhibits.
- **Tabletop exercise (2 hours, Full Assessment):** walk the customer’s team through “an AI agent goes rogue in your control environment.” Who notices? Who can stop it? What evidence exists afterwards?

## Week 4–5: Recommend

- Tailor the AI-in-OT policy (`ai-in-ot-policy-template.md`).
- Build the 30/90/365-day roadmap. Quick wins usually include: inventory sign-off, removing unneeded AI write access, requiring vendor AI disclosure, logging AI activity, and human approval for any AI-initiated control change.
- Map findings and controls to NERC CIP (where applicable), the NIST AI RMF and the EU AI Act. **Have a compliance specialist review the NERC CIP mapping before it goes to the customer.**
- Write the report (`report-template.md`).

## Week 5–6: Readout and close

- [ ] Send the draft report; allow 5 business days for factual corrections.
- [ ] Deliver the final report and the 60-minute executive readout.
- [ ] Present the next step: a Preceptor watch-only pilot or an advisory retainer.
- [ ] Ask for a reference and, for design partners, agree the case study.
- [ ] Return or securely delete customer data as agreed in the rules of engagement, and confirm in writing.
- [ ] Internal retro: add anonymized findings to our knowledge base (patterns, common AI tools, typical gaps).

## If you find something urgent

If you find an AI system with an active path to operate safety equipment or breakers without human approval, or evidence of compromise: **stop, and tell the customer sponsor the same day**, by phone, following the escalation path agreed at kickoff. Don’t wait for the report.
