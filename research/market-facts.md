# Market facts and sources

Every number used in the deck, where it came from, and how much to trust it. Researched November 2026. **Re-check before investor meetings**, especially anything marked *verify*.

## Market size

| Fact | Figure | Source | Confidence |
|---|---|---|---|
| Global OT security market, 2025 | $23.5B, forecast $58.9B by 2031 (16.6% CAGR) | [MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/operative-technology-ot-security-market-18524133.html) | Medium. Estimates range from ~$22B to ~$44B depending on how firms define the market |
| US OT security market, 2025 | $4.64B, forecast $9.37B by 2030 | [MarketsandMarkets](https://www.marketsandmarkets.com/PressReleases/us-operational-technology-ot-security.asp) | Medium |
| Other estimates | Mordor: $22.2B (2025); Fortune Business Insights: $24.2B (2025); SNS Insider: $44.3B (2025) | Various paid reports | Use only as a range |

## US utilities

| Fact | Figure | Source | Confidence |
|---|---|---|---|
| Total US electric utilities | ~2,900–3,000 | [EIA, 2017](https://www.eia.gov/todayinEnergy/detail.php?id=40913) | High, but dated; counts change slowly |
| Investor-owned | 168, serving ~72% of customers | EIA, 2017 | High |
| Public power | ~2,000 (EIA counted 1,958) | [APPA](https://www.publicpower.org/system/files/documents/Chapter%201%20-%20What%20is%20Public%20Power.pdf); EIA | High |
| Cooperatives | ~812 distribution co-ops (NRECA: 832 distribution + 63 G&T) | EIA; [NRECA fact sheet](https://www.cooperative.com/programs-services/bts/Documents/Data/Electric-Co-op-Fact-Sheet.pdf) | High |

## AI adoption in utilities

| Fact | Figure | Source | Confidence |
|---|---|---|---|
| Utilities deploying AI at scale | 62%; security gaps named as the main limit on scaling | [Cisco, 2026 State of Industrial AI: Utilities](https://www.cisco.com/c/dam/en/us/solutions/networking/industrial-iot/2026-state-of-industrial-ai-report-utilities.pdf) | Low–medium. Vendor survey; label it as such |
| Governance concern | IEA warns AI risks in grid operations need governance before deeper deployment | [IEA](https://www.iea.org/reports/modernising-grids-in-the-age-of-electricity/ai-enhanced-solutions) | High (qualitative) |

## Threats

| Fact | Detail | Source | Confidence |
|---|---|---|---|
| AI-orchestrated espionage campaign (GTG-1002) | Detected mid-Sept 2025 and disclosed Nov 2025; AI agent did ~80–90% of tactical work; ~30 organizations targeted; attributed to a Chinese state-sponsored group | [Anthropic report (PDF)](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf); [MITRE ATT&CK C0062](https://attack.mitre.org/campaigns/C0062/) | High |
| Volt Typhoon | US agencies warned in 2024 that this PRC state group was pre-positioned in US critical infrastructure networks, including energy, water and transportation | CISA joint advisory, Feb 2024 | High. *Add the direct CISA link* |

## Regulation

| Fact | Detail | Source | Confidence |
|---|---|---|---|
| NERC CIP-015 (internal network security monitoring) | FERC Order 907 approved it June 26, 2025; compliance effective Oct 1, 2028; FERC directed an expansion (CIP-015-2) | [Dragos](https://www.dragos.com/blog/ferc-approves-nerc-cip-015-2-insm-expansion); [Federal Register 2025-12309](https://public-inspection.federalregister.gov/2025-12309.pdf) | High. *Verify the CIP-015-2 schedule* |
| EU AI Act, high-risk rules (incl. critical infrastructure) | Moved to Dec 2, 2027 for stand-alone (Annex III) systems under the Digital Omnibus; provisional agreement May 2026 | [CMS](https://cms.law/en/gbr/publication/the-eu-s-digital-omnibus-on-ai-what-the-provisional-agreement-really-changes); [Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules) | Medium. *Verify formal adoption in the Official Journal* |
| SBIR/STTR | Lapsed Oct 1, 2025; reauthorized April 13, 2026 through Sept 30, 2031; new Phase II “strategic breakthrough” awards up to $30M | [CRS IN12705](https://www.everycrsreport.com/reports/IN12705.html); [Crowell](https://www.crowell.com/en/insights/client-alerts/sbirsttr-programs-reauthorized-after-six-month-lapse) | High |

## Acquisitions and valuations

| Buyer → company | Category | Reported price | Source | Confidence |
|---|---|---|---|---|
| Mitsubishi Electric → Nozomi Networks (Sept 2025) | OT security | $883M cash for the ~93% not already owned; ~$1B total | [SiliconANGLE](https://siliconangle.com/2025/09/09/mitsubishi-electric-acquires-cybersecurity-provider-nozomi-networks-883m/); [Cybersecurity Dive](https://www.cybersecuritydive.com/news/mitsubishi-electric-buy-nozomi-networks-1b/759637/) | High |
| Palo Alto Networks → Protect AI (2025) | AI security | ~$500–700M (not officially disclosed) | GeekWire, Calcalist via [deal tracker](https://guptadeepak.com/agent-security/deals/) | Medium |
| Check Point → Lakera (2025) | AI security | ~$300M reported | [Infosecurity Magazine](https://www.infosecurity-magazine.com/news-features/cybersecurity-ma-crowdstrike) | Medium |
| SentinelOne → Prompt Security (2025) | AI security | ~$250–300M reported | Globes via [deal tracker](https://guptadeepak.com/agent-security/deals/) | Medium |
| F5 → CalypsoAI (2025) | AI security | $180M | [SiliconANGLE](https://siliconangle.com/?p=706164) | High |
| Total AI security M&A | >$2B spent by 8 major vendors in ~18 months | [Forrester](https://www.forrester.com/blogs/securing-ais-ma-feeding-frenzy-is-on) | Medium |
| Claroty | ~$3B reported valuation on a $150M raise (2026) | [SC Media](https://www.scworld.com/brief/claroty-secures-150-million-to-protect-industrial-equipment-from-cyber-threats) | Medium. Not confirmed by Claroty |
| Dragos | $1.7B valuation (2021 Series D); no newer figure found | SecurityWeek | Dated. *Check for newer rounds* |

## Still to research

- Direct CISA link for the Volt Typhoon advisory.
- What incumbents (Dragos, Claroty, Nozomi, Palo Alto, Microsoft) currently offer for AI visibility in OT. This is the feature-risk question.
- Startups already working on AI agent security for OT or industrial settings.
- Typical pre-seed round sizes for security startups in 2026.
- TSA security directive scope for aviation, to support phase 3.
