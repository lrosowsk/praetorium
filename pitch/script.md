# Preceptor Defense: pitch script

Full run: about **13 minutes** across 20 slides. The same text is in each slide’s speaker notes.

Fill in everything in [brackets] before you present. Speak to the idea, don’t read word for word: the bold first line of each slide is the one point to land.

**Short on time?** For a 10-minute slot, skip *Strategic interest*, *Moats* and *Roadmap*, and cut *Platform*, *Competition* and *Business model* to one sentence each. That brings it to about 10 minutes. For a 5-minute slot, use slides 1–3, 5, 7, 9, 12, 18 and 20.

---

## 1. Cover  ·  15s  ·  starts at 0:00

**Hi, I’m [your name], founder of Preceptor Defense.** We’re building the human sign-off for AI in critical infrastructure, starting with the electric grid. Here’s the short version.

## 2. In 30 seconds  ·  45s  ·  starts at 0:15

**Power companies are connecting AI to the systems that run the grid, and right now nobody controls what that AI is allowed to do.** At the same time, hackers have started using AI to attack. Preceptor is a checkpoint between AI and the physical world. Safe actions go through, risky ones wait for a human, dangerous ones are blocked, and everything is recorded. The timing is driven by new federal grid-security rules and AI moving into everyday utility operations. We sell annual subscriptions, starting with the 3,000 power companies in the US. And we’re raising $[__] to turn our working prototype into paid pilots. Let me walk you through it.

## 3. The problem  ·  60s  ·  starts at 1:00

**Start with the problem.** Sixty-two percent of utilities say they’re already rolling out AI at scale, and that security is what’s holding them back. AI is showing up in three ways. It’s built into the software that runs the grid, often switched on by a routine update. Engineers are connecting AI tools to systems that sit right next to the controls. And if you ask a utility, “What did your AI touch last week?”, nobody can answer. There’s no list, no rules and no record a regulator would accept. Here’s the key point: in most industries an AI mistake leaks data. Here, it causes a blackout.

## 4. The threat  ·  45s  ·  starts at 2:00

**And it isn’t just mistakes.** Last year Anthropic disclosed a state-sponsored hacking campaign where an AI agent did 80 to 90 percent of the work, against about 30 organizations. US agencies have also warned that Chinese state hackers are already hiding inside American power and water networks. Put those together and you get attackers who are already inside, now with AI that moves faster than any human defender.

## 5. The gap  ·  45s  ·  starts at 2:45

**So why can’t existing tools handle this? Because each one sees half the picture.** Grid security companies like Dragos and Claroty are very good at watching grid equipment, but they can’t tell which AI sent a command. AI security tools, the ones Palo Alto, Check Point and SentinelOne have been buying, check what an AI says, but they don’t know that an action could cut power to a city. Preceptor sees both: which AI is acting, and what that action would do in the real world.

## 6. The vision  ·  30s  ·  starts at 3:30

**Here’s the bigger picture.** More and more software is getting permission to move physical things. Today it’s AI assistants, next it’s automation and outside vendors, and eventually it’s robots, drones and self-running plants. All of it needs a safety layer. Our vision is that Preceptor makes it safe to let software act on the physical world. We start where it’s most urgent: AI on the grid.

## 7. What we do  ·  45s  ·  starts at 4:00

**Concretely, Preceptor does four things.** It finds every AI system that can reach the grid, including ones nobody approved. It lets the utility set rules in plain language: this AI can read meter data, needs a human to approve voltage changes, and can never touch a breaker. It catches AI behaving like an attacker and locks it out. And it keeps a tamper-proof record, so the utility can prove to regulators and its board that AI is under control.

## 8. How it works  ·  40s  ·  starts at 4:45

**The design is simple.** Every AI request, whether it comes from a vendor’s assistant, an engineer’s tool or a forecasting model, goes through one gate. The gate asks four questions: who is this AI, is this action allowed, is it risky enough to need a human, and then it records the decision. Data systems can be read, grid controls need approval, and safety equipment is off limits. We start in watch-only mode, so a utility gets value before we ever block anything. That matters a lot to very cautious buyers.

## 9. Working prototype  ·  60s  ·  starts at 5:25

**This isn’t a concept.** We’ve built it. This is our prototype running against a simulated substation that speaks a real industrial protocol. A vendor’s AI asks to raise the voltage, and nothing happens until an operator clicks Approve. An AI tool nobody registered tries to connect and gets blocked. And a hijacked AI tries to open a breaker, gets denied, starts scanning the network, and is locked out within seconds. Every one of those decisions goes into a tamper-proof log that exports as an evidence report. [If you can, run the live demo here instead: two to three minutes.]

## 10. The platform  ·  40s  ·  starts at 6:25

**Over time this becomes a platform.** In year one we sell two products: AI governance and compliance proof. From there we add vendor access control, attack detection, a certification program where grid software vendors pay to have their AI tested, and threat intelligence from across our customers. It all sits on one core: a library that knows what every digital command does physically. That’s the hard part to build, and it compounds.

## 11. Why now  ·  40s  ·  starts at 7:05

**Why now? Two forces are arriving together.** On the rules side, US regulators have ordered power companies to monitor activity inside their control networks, with a 2028 deadline, and Europe’s rules for high-risk AI are coming. On the threat side, the first AI-run cyberattacks are public, and utilities are moving AI from experiments into daily operations. Utilities have to start watching inside their networks, and AI is now one of the things in there.

## 12. Market  ·  40s  ·  starts at 7:45

**Companies spent 23.5 billion dollars securing industrial systems in 2025, and that’s forecast to reach almost 59 billion by 2031.** We start with about 3,000 US power companies, then expand into wastewater, drinking water, pipelines and airports: tens of thousands more operators, most of them small, with almost no security staff. Getting to 100 million dollars a year means roughly a thousand customers at 100 thousand each, across those industries.

## 13. Strategic interest  ·  30s  ·  starts at 8:25

**There’s also strong strategic interest in this space.** Mitsubishi Electric paid about a billion dollars for Nozomi, an industrial security company. And Palo Alto, Check Point, SentinelOne and F5 have all bought AI security startups: more than 2 billion dollars in about 18 months. We sit exactly where those two categories meet.

## 14. Competition  ·  40s  ·  starts at 8:55

**On competition: grid security tools understand equipment but not AI, and AI security tools understand AI but not equipment.** We cover both, and we’re built for utility buyers. We plug into the tools utilities already own instead of replacing them. The honest risk is that a big vendor bolts on an AI feature. Our answer is to be the neutral checkpoint across every vendor, and to move fast.

## 15. Moats  ·  30s  ·  starts at 9:35

**Over time we get harder to copy: a growing library of what digital commands do physically, data from hundreds of sites, a certification standard vendors build to, and being the record auditors rely on.** And utilities want a checkpoint that’s independent of the vendors whose AI it controls. Incumbents can’t credibly offer that.

## 16. Business model  ·  40s  ·  starts at 10:05

**Utilities pay an annual subscription per site.** Grid software vendors pay to certify their AI. Insurers buy risk data, government funds research and protects federal sites, and security providers resell us to small utilities. We land with smaller power companies, co-ops and city-owned utilities, because they decide faster. Then we expand to larger utilities and new industries.

## 17. Roadmap  ·  25s  ·  starts at 10:45

**The roadmap is deliberately sequenced.** Year one, prove the first product with smaller utilities. Year two, full enforcement and large utilities. Year three, attack detection, certification and water. Year four, threat intelligence and new industries. The biggest risk for a company like this is building everything at once, and we won’t.

## 18. Next 12 months  ·  40s  ·  starts at 11:10

**Here’s the next year.** First quarter: 30 interviews with utility security leaders and three letters of intent. Second: refine the prototype with design partners and apply for government grants. Third: two paid pilots in watch-only mode. Fourth: turn those into annual contracts and raise a seed round on real revenue. Today we have a working prototype, [__] interviews done and [__] letters of intent.

## 19. Team  ·  40s  ·  starts at 11:50

**[One or two sentences about you: what you’ve built or led, and why you’re the person to do this.] We’re adding a grid security lead, someone from a utility, a national lab or an industrial security company, and a founding AI security engineer.** And we’re building an advisory bench that includes a utility security chief, a national lab researcher and a grid compliance expert.

## 20. The ask  ·  40s  ·  starts at 12:30

**We’re raising $[__] at pre-seed.** It goes to three things: the team, turning the prototype into something a utility can pilot, and running those pilots. That buys 12 to 18 months to prove the first product with paying customers, and we’ll stretch it with government grants. AI is going to run more and more of the physical world. Preceptor makes sure a human signs off before it does anything dangerous. Thank you. I’m happy to take questions.

---

## The 2-minute version

Use this for a hallway intro, a phone call or the opening of a first meeting.

> Power companies are connecting AI to the systems that run the grid, and nobody controls what that AI is allowed to do. In most industries an AI mistake leaks data; here it causes a blackout. And hackers have started using AI to attack, at machine speed.
>
> Preceptor Defense is a checkpoint between AI and the physical world. Every AI request goes through us: safe actions pass, risky ones wait for a human to approve, dangerous ones are blocked, and everything is recorded so the utility can prove to regulators that AI is under control.
>
> Existing tools see half the picture. Grid security tools don’t understand AI, and AI security tools don’t understand the grid. We do both.
>
> The timing is right: US regulators now require power companies to monitor inside their control networks, and utilities are moving AI into daily operations. We start with the 3,000 US power companies and expand to water, pipelines and airports.
>
> We’ve built a working prototype, and we’re raising $[__] to turn it into paid pilots.

---

## Likely questions

**Isn’t this just a feature CrowdStrike, Dragos or Palo Alto will add?**

They’ll add pieces. CrowdStrike already has an AI kill switch for office IT. But none of them understand both AI and grid equipment, and utilities want a checkpoint that’s independent of the vendors whose AI it controls. We integrate with incumbents rather than fight them, and if they want this capability, we’re the natural acquisition.

**Will a utility really let a startup sit in front of its control systems?**

Not on day one, which is why we start in watch-only mode: we see and record everything but block nothing. Utilities get the inventory and compliance evidence immediately, and only turn on enforcement once they trust us. A grid-security co-founder and national lab partners help with credibility.

**How much AI is actually touching grid controls today?**

Honestly, it’s early, and that’s the point of our discovery interviews. Adoption is moving fast and vendors are embedding AI in grid software now. That’s also why we lead with visibility and compliance, which utilities need even before AI is deeply embedded.

**Utility sales cycles are long. How do you survive them?**

We start with co-ops and city-owned utilities, which decide faster, and sell through the agencies and cooperatives that serve dozens of them at once. Government grants and early services revenue extend our runway while larger deals close.

**What will a customer pay?**

We’re validating pricing in discovery. The working assumption is a paid pilot of $[__]K, then $50K to $150K a year for a mid-size utility, more for large utilities with many sites.

**What’s the hardest technical problem?**

Knowing what a digital command does physically, safely and reliably. That rule library is our core asset. We manage the risk by staying out of the critical path until a utility trusts us, and by testing on simulated and real equipment with grid engineers.

**What if AI adoption at utilities is slower than you expect?**

The compliance need doesn’t depend on AI: regulators already require monitoring inside control networks by 2028. And AI-powered attacks are coming regardless of how fast utilities adopt AI themselves.

**Why you?**

[Your answer: your background, what you’ve built, and what you’ve learned from the utility interviews so far.]
