# AI in OT Risk Assessment: [Organization]

**Prepared by:** Preceptor Defense  **Date:** [date]  **Engagement:** [Snapshot / Full Assessment]  **Classification:** Confidential, [Organization] internal

---

## 1. Executive summary (one page)

**Bottom line:** [One sentence, e.g. “We found 14 AI systems that can reach your OT environment; 3 could change control parameters without human approval.”]

| | Count |
|---|---|
| AI systems found | [ ] |
| …that can read operational data | [ ] |
| …that can change control parameters | [ ] |
| …with human approval before acting | [ ] |
| …not previously known to security | [ ] |
| High / medium / low risk | [ ] / [ ] / [ ] |

**Top three risks:**
1. [Plain-language risk and its potential consequence]
2. [ ]
3. [ ]

**Top three actions for the next 30 days:**
1. [ ]
2. [ ]
3. [ ]

## 2. Scope and approach
- In scope: [sites, systems]. Out of scope: [ ].
- Method: document and configuration review, [N] interviews, passive log analysis ([N] days of DNS/proxy logs), vendor review, lab testing of [N] scenarios, [tabletop exercise].
- **No testing was performed on live operational systems.**

## 3. AI inventory
Summary table (full register in Appendix A):

| ID | AI system | Type | Owner | Can read | Can write | Path to OT | Human approval | Risk |
|---|---|---|---|---|---|---|---|---|
| AI-01 | [ ] | [vendor feature / engineering tool / model / shadow AI] | [ ] | [ ] | [ ] | [ ] | [Y/N] | [H/M/L] |

**AI traffic seen in logs:** [summary from `ai_traffic_scan.py`: which hosts contacted which AI services, how often, and whether those were expected].

## 4. Key findings
For each finding:

### Finding [n]: [title]
- **Risk:** [High / Medium / Low]  (consequence [1–5] × likelihood [1–5])
- **What we found:** [ ]
- **Why it matters:** [the physical or compliance consequence, in plain language]
- **Evidence:** [interview, log excerpt, configuration, lab result]
- **Recommendation:** [ ]

## 5. Lab test results
For each scenario: setup, what the AI attempted, outcome without controls, outcome with recommended controls. Include dashboard screenshots and evidence-report excerpts.

## 6. Policy and governance gaps
[Gaps against the AI-in-OT policy principles: known, approved, least privilege, humans decide physical changes, recorded.]

## 7. Roadmap

| Horizon | Action | Owner | Effort | Risk reduced |
|---|---|---|---|---|
| 30 days | [ ] | [ ] | [S/M/L] | [ ] |
| 90 days | [ ] | | | |
| 12 months | [ ] | | | |

## 8. Compliance mapping
*Indicative only. Confirm with your compliance team.*

| Finding / control | NERC CIP (if applicable) | NIST AI RMF | EU AI Act (if applicable) |
|---|---|---|---|
| AI inventory | CIP-002 (asset identification context), CIP-010 (configuration baselines) | Map | Art. 9 risk management |
| Monitoring AI activity in OT | CIP-015 (internal network security monitoring), CIP-007 (logging) | Measure, Manage | Art. 12 record-keeping |
| Vendor AI disclosure and contracts | CIP-013 (supply chain risk management) | Govern | Art. 25 value chain |
| Human approval for AI control actions | CIP-010 (change management) | Manage | Art. 14 human oversight |
| AI access through remote paths | CIP-005 (remote access) | Manage | |

## Appendices
- A. Full risk register
- B. Interview list (roles only)
- C. Log analysis method and results
- D. Lab scenario details
- E. Tailored AI-in-OT policy
