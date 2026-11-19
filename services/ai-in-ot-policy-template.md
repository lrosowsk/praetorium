# [Organization] policy: AI in operational technology

**Owner:** [CISO / OT security manager]  **Approved by:** [executive]  **Effective:** [date]  **Review:** annually, or when a new AI system is introduced into OT

*Template from Preceptor Defense. Tailor to your environment and have it reviewed by your compliance and legal teams.*

## 1. Purpose
AI tools can now read from and act on operational systems. This policy makes sure AI is used in OT only where it is known, approved, limited to what it needs, supervised by people for anything that could change physical operations, and recorded.

## 2. Scope
Any AI system (including AI features inside vendor software, AI coding assistants, AI agents, and analytics or machine-learning models) that can read data from, send commands to, or run on systems in the OT environment, including engineering workstations and remote access paths into OT.

## 3. Principles
1. **Known:** every AI system that can reach OT is in the AI inventory, with a named owner.
2. **Approved:** no AI system or AI feature is used in OT until it passes the approval process in section 5. This includes AI features delivered through vendor software updates.
3. **Least privilege:** AI systems get only the access they need, through their own identities, never shared or personal operator credentials.
4. **Humans decide physical changes:** see section 4.
5. **Recorded:** AI activity in OT is logged so that, for any action, we can show which AI acted, under which rule, and who approved it.

## 4. What AI may do

| Action class | Examples | Rule |
|---|---|---|
| **Read** | Telemetry, historian data, alarms, maintenance records | Allowed for approved AI systems, within their approved scope |
| **Recommend** | Suggested switching orders, setpoint changes, maintenance schedules | Allowed; recommendations must be clearly marked as AI-generated |
| **Change control parameters** | Setpoints, schedules, configurations, PLC logic | **Only with explicit approval by a qualified person before the change takes effect** |
| **Operate protection or safety equipment** | Breakers, relays, safety instrumented systems, emergency shutdown | **Never** by AI, directly or indirectly |

## 5. Approval of AI systems
Before an AI system is used in OT, the owner submits: purpose; vendor and model; data it reads; actions it can take; credentials it uses; how its activity is logged; and the vendor’s data-use terms. The [OT security manager] approves, approves with conditions, or rejects, and updates the AI inventory. Material changes (new capabilities, wider access) need re-approval.

## 6. Vendors
- Vendors must disclose AI features in their products before delivery and say whether they are enabled by default.
- AI features that can change control parameters must support human approval and activity logging, or stay disabled.
- Vendors may not use our operational data to train models without written agreement.
- These requirements are included in new and renewed contracts [and in our supply chain risk management plan, where NERC CIP-013 applies].

## 7. Engineering use of AI tools
- Only approved AI tools may be used on engineering workstations and jump hosts.
- AI-generated code, scripts, configurations or logic are reviewed and tested by a qualified engineer before use in OT, following normal change management.
- Operational data and network details are not entered into unapproved AI services.

## 8. Monitoring and response
- AI activity in OT is logged and reviewed [monthly / continuously].
- Unexpected AI behaviour (actions outside approved scope, unusual speed or volume, attempts to reach protection equipment) is treated as a security incident.
- The [OT security manager] can suspend any AI system’s access immediately.

## 9. Roles
- **AI system owner:** keeps the inventory entry accurate and requests approvals.
- **OT security manager:** runs approvals, monitoring and the inventory.
- **Qualified operators and engineers:** approve AI-proposed control changes.
- **Compliance:** maintains evidence for auditors.

## 10. Exceptions
Exceptions require written approval from [CISO], a documented risk acceptance, and an expiry date.
