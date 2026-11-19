# Services: AI in OT Risk Assessment

Preceptor Defense’s first revenue line: a fixed-price assessment that finds every AI system able to reach a customer’s control systems, rates what each could physically do, and delivers policy, roadmap and compliance evidence. It funds the early company, builds credibility, and leads into the Preceptor product.

**Sales sheet (send to prospects):** https://claude.ai/artifact/VJoRGsRqkAArEjyBpdKnsj (private until shared from its Share menu). Source: `sales-sheet.html`.

| File | Use it for |
|---|---|
| `offering.md` | The offer: problem, deliverables, packages and pricing, delivery team, targets |
| `playbook.md` | Running an engagement week by week, from kickoff to readout |
| `rules-of-engagement.md` | What we will and won’t do; customer signs before work starts |
| `intake-questionnaire.md` | Sent at kickoff; doubles as the interview guide |
| `risk-register-template.csv` | The AI inventory and risk scores for each engagement |
| `ai-in-ot-policy-template.md` | Policy we tailor for the customer |
| `report-template.md` | Structure of the final report |
| `proposal-template.md` | Proposal and statement of work |
| `tools/ai_traffic_scan.py` | Finds AI-service traffic in customer DNS, proxy or firewall log exports |

## Selling it

- **Discovery calls are the pipeline.** When an interviewee describes real AI concerns, offer a Snapshot. Offer design-partner pricing (about 40% off) to the first three in exchange for a case study and a reference.
- **Bundle the product.** Close every readout by proposing a Preceptor watch-only pilot or an advisory retainer.

## Running the scanner

```bash
python3 tools/ai_traffic_scan.py customer-dns.log            # plain-text logs
python3 tools/ai_traffic_scan.py proxy.csv --csv results.csv  # CSV logs, with a detailed export
python3 tools/ai_traffic_scan.py tools/sample-dns.log         # try it on the sample
```

Only run it on exports the customer has provided, on an encrypted machine, per the rules of engagement.

## Before the first engagement

- [ ] Lawyer review of the rules of engagement, proposal terms and an NDA template.
- [ ] Professional liability and cyber insurance. Utilities will ask.
- [ ] An OT/ICS-experienced lead assessor: the grid-security co-founder, or a contracted consultant until then.
- [ ] A compliance specialist to review NERC CIP mappings.
