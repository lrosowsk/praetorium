# Deployment roadmap

Two parts: **(1) how the company gets from today’s prototype to a product utilities run in production**, and **(2) how each customer rollout works**, step by step. Timelines assume the $2M pre-seed closes; month 0 is the close.

---

## Part 1: From prototype to production

| Phase | When | What we build | What customers see | Exit criteria (move on only when true) |
|---|---|---|---|---|
| **0. Prototype** | Done | Simulated substation, policy gate, dashboard, audit log, evidence report (`demo/`) | Demos | ✓ Working end-to-end demo |
| **1. Assessments and design partners** | Months 0–4 | Assessment toolkit (`services/`), AI traffic scanner, prototype hardened for lab use | Paid AI in OT assessments; 2–3 design partners reviewing the product | 3 paid assessments · 2–3 design partners signed · grid-security co-founder hired |
| **2. Watch-only product (v0.5)** | Months 3–8 | On-premises install package; AI tool gateway (software, IT side); read-only connectors to Dragos, Claroty and Nozomi data; AI inventory; policy editor in “record only” mode; evidence reports | A pilot that sees and records AI activity but blocks nothing | Installs in under a day · runs 30 days without operator intervention · passes a utility security review · SOC 2 Type I started |
| **3. Paid watch-only pilots** | Months 6–12 | Pilot support, fixes from real environments, more protocols (DNP3, IEC 61850 in addition to Modbus), role-based access, single sign-on | 2 paid pilots at smaller utilities | Both pilots convert to annual contracts · first case study published |
| **4. Approval workflow (v1.0)** | Months 12–18 | Human approval for AI tool actions (step 1 customers); approvals routed to operators by phone, console or existing ticketing; high availability; tamper-evident log export for auditors | Customers turn on approval for the AI tools they control | Zero unplanned outages caused by Preceptor · approval adds under 1 minute to normal workflows · SOC 2 Type II |
| **5. In-path enforcement (v2.0)** | Year 2+ | Hardware appliance or validated virtual appliance in the control path; fail-safe design reviewed with utility engineers; vendor integrations so AI inside grid software asks Preceptor first | Enforcement on grid control paths, at customers who have run watch-only for 6+ months | Independent safety review · real-hardware test lab sign-off · first vendor integration live |

### Engineering principles throughout
- **Never the cause of an outage.** Until phase 5, Preceptor is not in the path of any control command. In phase 5, failure modes are designed with utility engineers, and the default is that the grid keeps running.
- **On-premises first.** No cloud connection is required from the control network. Optional cloud features only on the IT side.
- **Use what’s already there.** Read from existing OT sensors before asking for new hardware.
- **Everything is evidence.** Every decision is logged in a form an auditor can verify.
- **Secure by design.** Preceptor will be a high-value target: signed releases, least-privilege service accounts, external penetration tests before each major release.

### Team needed by phase
| Phase | Team |
|---|---|
| 1 | Founder, grid-security co-founder (or OT consultant) |
| 2–3 | + 2 engineers (backend/security, OT protocols) |
| 4 | + 1 engineer (reliability), part-time compliance specialist |
| 5 | Seed-funded: + hardware/embedded, field engineering, vendor partnerships |

---

## Part 2: A customer rollout, step by step

Each customer moves through the same three steps from the deck. They can stop at any step and still get value.

### Before anything is installed (weeks −12 to 0)
Usually starts with an AI in OT assessment, which produces the AI inventory and policy the product then enforces.
- [ ] Contract and pilot scope signed
- [ ] Customer security review (questionnaire, architecture, SOC 2 report or bridge letter)
- [ ] Change request approved through the customer’s change management (and CIP process if applicable)
- [ ] Install location agreed: a virtual machine in the customer’s IT environment or OT DMZ

**Typical duration:** 1–3 months at a small utility, 3–12 months at a large one. This is the longest part, so start it early.

### Step 1: Gate the AI tools the customer controls (weeks 1–4)
- Install the Preceptor gateway as software in the customer’s environment.
- Point engineers’ AI tools and analytics models at the gateway instead of directly at systems.
- Load the AI inventory and starter policy from the assessment.
- Run in **record-only** mode for two weeks, then review what was seen with the customer.
- **Value delivered:** a live AI inventory and an audit trail for every AI tool action.

### Step 2: Watch the control network (weeks 4–12)
- Connect read-only to the customer’s existing OT monitoring (Dragos, Claroty or Nozomi), or install a passive network sensor where none exists.
- Correlate AI tool activity with what happens on the control network.
- Turn on alerts for policy violations and machine-speed behavior. Nothing is blocked.
- Monthly evidence reports for compliance and the board.
- **Value delivered:** visibility into AI-related activity across the control environment, plus compliance evidence.

### Step 3: Enforce (month 6 onward, only when the customer is ready)
- Turn on human approval for AI actions the customer selects, starting with the AI tools from step 1.
- Expand to control-path enforcement only after 6+ months of watch-only operation, a joint failure-mode review, and sign-off by the customer’s operations leadership.
- **Value delivered:** risky AI actions wait for a person; dangerous ones are blocked.

### Success measures for every rollout
- AI systems inventoried versus found in the assessment
- Percentage of AI actions covered by a policy
- Time from AI request to human decision
- Unplanned operational impact caused by Preceptor (target: zero)
- Evidence reports accepted by the customer’s compliance team

---

## Biggest deployment risks

| Risk | Mitigation |
|---|---|
| Customer approvals take a year | Start with smaller utilities; begin security reviews during the assessment; have SOC 2 and architecture documents ready |
| Every environment is different | Standard install package; connectors for the three major OT monitoring platforms; budget hands-on support for the first 5–10 rollouts |
| AI inside vendor grid software is hard to see | Behavioral correlation in step 2; vendor integrations in phase 5; certification program gives vendors a reason to integrate |
| Preceptor itself is attacked | Security engineering from day one, external penetration tests, no inbound connections from the internet |
| Operators see approvals as friction | Approvals only for genuinely risky actions; fast routing to the right person; measure added time |
