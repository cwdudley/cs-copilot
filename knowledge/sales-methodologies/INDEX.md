# Sales Methodology Corpus — Index

A sourced knowledge corpus for an Account Management / Customer Success Copilot
that coaches AMs on account strategy, expansion, renewals, stakeholder
management, discovery and opportunity execution.

- **Primary sources:** first-party MEDDICC content (MEDDPICC) and first-party
  Winning by Design content (SPICED, the Bowtie, account management, expansion).
- **Retrieved:** 2026-09-12. Public content only; no logins, paywalls or forms
  were bypassed.
- **Documents:** 72 source documents across five folders.

---

## Design principle

The frameworks are complementary, not competing:

| Layer | Job | Used when |
|---|---|---|
| **SPICED** | Continuous customer diagnosis and discovery | Always — every account conversation, at every lifecycle stage |
| **Account planning / expansion** | Deciding where opportunity exists across the account and what the AM should pursue | Planning the account, reviewing whitespace, deciding upsell vs. cross-sell vs. resell |
| **MEDDPICC** | Qualifying and executing a concrete commercial opportunity | Once a credible renewal or expansion opportunity exists |

**Do not force every account interaction through MEDDPICC.** It becomes most
prominent once there is a real opportunity to qualify and advance.

---

## Conventions

Every source document carries YAML frontmatter:

| Field | Meaning |
|---|---|
| `framework` | `meddpicc`, `spiced`, `account-management`, `expansion`, or `account-planning` |
| `topic` | The specific subject |
| `source_url` / `source_title` / `source_org` | Attribution for the primary source |
| `retrieved_date` | When the content was retrieved |
| `also_covers` | Additional URLs merged into this document because they substantially overlapped (deduplication) |
| `content_status` | `public`, or a note explaining partial coverage (gated PDF, course outline only, direct PDF, promotional page) |
| `bias_note` | Present where a vendor compares its own framework with a rival's |

**Content is paraphrased and restructured, not mirrored.** Substance —
definitions, questions, examples, failure modes, plays — is preserved with short
attributed phrases only. Sources are kept separate; cross-framework synthesis is
deliberately limited to short, labeled notes.

---

## Coverage map — the ten AM Copilot jobs

| # | Job | Primary documents |
|---|---|---|
| 1 | Understand an account | `spiced/spiced-framework`, `spiced/spiced-across-the-customer-journey`, `spiced/operating-model-for-recurring-revenue`, `account-management/bowtie-model`, `account-management/meddpicc-customer-lifecycle-intro` |
| 2 | Identify whitespace and expansion hypotheses | `expansion/bowtie-expansion-types`, `expansion/expansion-and-retention-playbooks`, `account-management/account-management-for-growth`, `account-planning/target-account-tiering`, `expansion/meddpicc-for-account-expansion` |
| 3 | Diagnose customer problems | `spiced/how-to-diagnose`, `spiced/operating-model-for-recurring-revenue`, `meddpicc/pain-are-you-really-implicating`, `meddpicc/pain-stakeholder-specific`, `meddpicc/decision-process-three-discovery-questions`, `meddpicc/metrics-uncovering-more-metrics` |
| 4 | Quantify business impact | `spiced/emotional-vs-rational-impact`, `meddpicc/metrics`, `meddpicc/metrics-personalizing-metrics`, `account-management/customer-success-metrics-harvesting-vs-mining`, `account-management/customer-success-as-profit-center` |
| 5 | Identify relevant stakeholders | `account-planning/mapping-relationships`, `account-planning/multi-threading`, `account-planning/the-stakeholder-meeting`, `meddpicc/economic-buyer*`, `meddpicc/champion*` |
| 6 | Recognize critical / compelling events | `meddpicc/compelling-event`, `spiced/operating-model-for-recurring-revenue` (note the terminology conflict), `spiced/how-to-diagnose` |
| 7 | Turn expansion signals into opportunities | `expansion/bowtie-expansion-types`, `expansion/meddpicc-for-account-expansion`, `account-management/customer-success-for-impact`, `meddpicc/qualifying-out` |
| 8 | Advance opportunities commercially | `expansion/trade-instead-of-negotiate`, `expansion/value-based-negotiation-meddicc`, `meddpicc/decision-process`, `meddpicc/paper-process*`, `meddpicc/economic-buyer-dunkel-executive-selling` |
| 9 | Protect renewals | `account-management/meddic-for-customer-success-webinar`, `account-management/meddpicc-for-customer-success`, `account-management/first-impact`, `account-management/joint-impact-plan`, `expansion/bowtie-expansion-types` (resell), `meddpicc/competition-the-wrong-competition` |
| 10 | Coach the next best action | `meddpicc/failure-modes`, `meddpicc/deal-reviews`, `meddpicc/deal-reviews-lessons-from-implementation`, `meddpicc/coaching-three-ts`, `account-management/meddpicc-for-revops`, `spiced/deal-analysis-with-spiced` |

---

## Retained sources

### `meddpicc/` — MEDDICC (40)

| Document | Topic | Source | Why it is valuable to the AM Copilot |
|---|---|---|---|
| [overview](meddpicc/overview.md) | overview | [MEDDPICC Methodology and Process](https://meddicc.com/meddpicc-sales-methodology-and-process) · also [AI Info](https://meddicc.com/ai-info) | Authoritative element definitions, lineage, and the "Implicate the Pain" terminology. |
| [metrics](meddpicc/metrics.md) | metrics | [Metrics](https://meddicc.com/what-is-meddpicc/metrics) | The M1/M2/M3 value cycle that links pre-sale promises to post-sale realized value and renewal evidence. |
| [metrics-uncovering-more-metrics](meddpicc/metrics-uncovering-more-metrics.md) | metrics | [Uncover More Metrics](https://meddicc.com/resources/medmen-uncover-more-metrics) | The Three Ps give the AM a concrete way to find metrics customers will not volunteer. |
| [metrics-personalizing-metrics](meddpicc/metrics-personalizing-metrics.md) | metrics | [Personalize Metrics](https://meddicc.com/resources/medmen-why-you-need-to-personalize-metrics) | Teaches per-stakeholder value, essential when multithreading an expansion. |
| [metrics-solution-to-inertia](meddpicc/metrics-solution-to-inertia.md) | metrics | [Metrics as a Solution to Inertia](https://meddicc.com/resources/metrics-as-a-solution-to-inertia) | Frames no-decision as the main competitor and quantified value as the remedy. |
| [economic-buyer](meddpicc/economic-buyer.md) | economic-buyer | [Economic Buyer](https://meddicc.com/what-is-meddpicc/economic-buyer) | Identification markers and the Champion-access test for executive authority. |
| [economic-buyer-qualifying](meddpicc/economic-buyer-qualifying.md) | economic-buyer | [Qualifying the Economic Buyer](https://meddicc.com/resources/qualifying-the-economic-buyer) | Separates Budget Holder from EB and recommends keeping the EB informed post-sale for upsell. |
| [economic-buyer-five-mistakes](meddpicc/economic-buyer-five-mistakes.md) | economic-buyer | [5 Things Not to Do With the EB](https://meddicc.com/resources/medmen-5-things-not-to-do-when-engaging-with-the-economic-buyer) | A ready checklist for preparing an AM before an executive meeting. |
| [economic-buyer-dunkel-executive-selling](meddpicc/economic-buyer-dunkel-executive-selling.md) | economic-buyer | [EB Selling with Dick Dunkel](https://meddicc.com/resources/economic-buyer-selling-takeaways) | Executive research, outreach and funding-discovery questions from MEDDIC's originator. |
| [economic-buyer-value-pyramid](meddpicc/economic-buyer-value-pyramid.md) | economic-buyer | [Value Pyramid With the EB](https://meddicc.com/resources/medmen-using-a-value-pyramid-with-the-economic-buyer) | A tool for re-establishing strategic alignment after executive or priority changes. |
| [economic-buyer-vs-champion](meddpicc/economic-buyer-vs-champion.md) | economic-buyer | [Misidentifying Champions](https://meddicc.com/meddicc-media/medmen-s2-ep1-misidentifying-champions) | Discovery questions to find the real EB and the "CFO by default" rule. |
| [decision-criteria](meddpicc/decision-criteria.md) | decision-criteria | [Decision Criteria](https://meddicc.com/what-is-meddpicc/decision-criteria) | Technical, economic and relationship criteria, and why sellers should shape them. |
| [decision-criteria-three-dimensional](meddpicc/decision-criteria-three-dimensional.md) | decision-criteria | [3-Dimensional Decision Criteria](https://meddicc.com/resources/3-dimensional-decision-criteria) | Shows how relationship and economic criteria differentiate near-identical offerings. |
| [decision-criteria-proactive](meddpicc/decision-criteria-proactive.md) | decision-criteria | [Proactive Decision Criteria](https://meddicc.com/resources/medmen-take-a-proactive-approach-to-decision-criteria) | Buyer-side lessons on what makes deals collapse to price. |
| [decision-process](meddpicc/decision-process.md) | decision-process | [Decision Process](https://meddicc.com/what-is-meddpicc/decision-process) | "Engagement is not progress" — a core correction for stalled expansions. |
| [decision-process-three-discovery-questions](meddpicc/decision-process-three-discovery-questions.md) | decision-process | [Three Discovery Questions](https://meddicc.com/resources/medmen-three-discovery-questions-that-feel-like-cheating) | Question scripts that map directly to how the last renewal or add-on was approved. |
| [paper-process](meddpicc/paper-process.md) | paper-process | [Paper Process](https://meddicc.com/what-is-meddpicc/paper-process) | Explains why "yes" is not closed — the main renewal slip point. |
| [paper-process-mastering](meddpicc/paper-process-mastering.md) | paper-process | [Master the Paper Process](https://meddicc.com/resources/meddpicc-paper-process-meddicc) | Operational components of contracting that an AM can start in parallel. |
| [paper-process-go-live-plan](meddpicc/paper-process-go-live-plan.md) | paper-process | [Go-Live Plan](https://meddicc.com/resources/go-live-plan) | Mutual plan anchored on time-to-impact; transferable to expansion timelines. |
| [implicate-the-pain](meddpicc/implicate-the-pain.md) | implicate-the-pain | [Implicate the Pain](https://meddicc.com/what-is-meddpicc/implicate-the-pain) | The Identify → Indicate → Implicate progression behind "why now." |
| [pain-are-you-really-implicating](meddpicc/pain-are-you-really-implicating.md) | implicate-the-pain | [Are You Really Implicating the Pain?](https://meddicc.com/resources/are-you-really-implicating-the-pain) | A pipeline self-check and the warning that implications fade over time. |
| [pain-stakeholder-specific](meddpicc/pain-stakeholder-specific.md) | implicate-the-pain | [Pain is Stakeholder-Specific](https://meddicc.com/resources/pain-is-stakeholder-specific) | Worked example of mapping one pain across seven executive roles. |
| [champion](meddpicc/champion.md) | champion | [Champion](https://meddicc.com/what-is-meddpicc/champion) · also [No Champion, No Deal](https://meddicc.com/resources/no-champion-no-deal) | The three-trait definition and the Champion / Coach / Friend distinction. |
| [champion-five-signs](meddpicc/champion-five-signs.md) | champion | [5 Signs You Don't Have a Champion](https://meddicc.com/resources/5-signs-you-dont-have-a-champion) | Observable tests the copilot can apply to an AM's claimed Champion. |
| [champion-getting-in-trouble](meddpicc/champion-getting-in-trouble.md) | champion | [Getting in Trouble With Your Champion](https://meddicc.com/resources/getting-in-trouble-with-your-champion) | Coaches AMs past "nice seller" avoidance of uncomfortable asks. |
| [champion-vested-interest](meddpicc/champion-vested-interest.md) | champion | [The Overlooked Champion Trait](https://meddicc.com/resources/medmen-the-crucial-but-overlooked-champion-trait) | How to uncover what a Champion personally gains. |
| [champion-building-in-a-downturn](meddpicc/champion-building-in-a-downturn.md) | champion | [Champion Building During a Downturn](https://meddicc.com/resources/champion-building-takeaways) | Risk-reduction tactics for Champions staking credibility on an expansion. |
| [champion-closing-without-being-in-the-room](meddpicc/champion-closing-without-being-in-the-room.md) | champion | [Close Deals Without Being in the Room](https://meddicc.com/meddicc-media/medmen-how-to-close-deals-without-being-in-the-room) | Multiple-Champion strategy and a practical Champion engagement test. |
| [competition](meddpicc/competition.md) | competition | [Competition](https://meddicc.com/what-is-meddpicc/competition) | Four competitor types, including inertia and competing initiatives. |
| [competition-the-wrong-competition](meddpicc/competition-the-wrong-competition.md) | competition | [Obsessing Over the Wrong Competition](https://meddicc.com/resources/medmen-obsessing-over-the-wrong-competition) | Diagnoses slippage to inertia across value, stakeholders and process. |
| [competition-dont-knock-the-competition](meddpicc/competition-dont-knock-the-competition.md) | competition | [Don't Knock the Competition](https://meddicc.com/resources/why-you-shouldnt-knock-the-competition) | How to defend a renewal against a returning competitor without FUD. |
| [compelling-event](meddpicc/compelling-event.md) | compelling-event | [The Necessity of a Compelling Event](https://meddicc.com/resources/the-necessity-of-a-compelling-event) | Real vs. manufactured urgency, with a test the copilot can apply. |
| [deal-reviews](meddpicc/deal-reviews.md) | deal-inspection | [Deal Reviews](https://meddicc.com/resources/mastering-meddpicc-deal-reviews) · also [Directing](https://meddicc.com/resources/leadership-in-meddpicc-mastery), [Reinventing](https://meddicc.com/resources/reinventing-deal-reviews) | Forward-looking review cadence and psychological safety for honest inspection. |
| [deal-reviews-lessons-from-implementation](meddpicc/deal-reviews-lessons-from-implementation.md) | deal-inspection | [Lessons Since Implementing MEDDICC](https://meddicc.com/resources/lessons-ive-learnt-since-implementing-meddic) | Ten practical adoption lessons including 1–10 confidence scoring. |
| [coaching-three-ts](meddpicc/coaching-three-ts.md) | coaching | [MEDDIC Coaching](https://meddicc.com/resources/medmen-meddic-coaching) | Trust, Timing, Tactics — how coaching lands. |
| [failure-modes](meddpicc/failure-modes.md) | failure-modes | [Why MEDDPICC Fails](https://meddicc.com/meddicc-media/medmen-why-meddpicc-fails-in-your-team-its-not-what-you-think) · also [Not a Checklist](https://meddicc.com/resources/meddic-is-not-a-checklist), [Isn't One and Done](https://meddicc.com/resources/medmen-meddic-isnt-one-and-done) | Keeps the copilot from turning MEDDPICC into a checkbox exercise. |
| [qualifying-out](meddpicc/qualifying-out.md) | opportunity-qualification | [Nobody Regrets Qualifying Out](https://meddicc.com/resources/alexa-email-cadence-meddicc) | Permission to drop weak expansion hypotheses. |
| [forecast-confidence](meddpicc/forecast-confidence.md) | deal-inspection | [Forecast Confidence](https://meddicc.com/resources/achieving-forecast-confidence-with-meddicc) | Maps forecast misses to specific MEDDPICC weaknesses. |
| [expert-panel-elements](meddpicc/expert-panel-elements.md) | practitioner-perspectives | [Experts Discuss the Elements](https://meddicc.com/resources/meddicon-experts) | Practitioner views on underrated elements and uncovering pain. |
| [comparison-spiced-vs-meddpicc-meddicc-view](meddpicc/comparison-spiced-vs-meddpicc-meddicc-view.md) | framework-comparison | [SPICED vs MEDDPICC](https://meddicc.com/resources/spiced-sales-methodology-vs-meddpicc-meddicc) | MEDDICC's element mapping and claimed SPICED gaps (vendor-biased). |

### `spiced/` — Winning by Design (8)

| Document | Topic | Source | Why it is valuable to the AM Copilot |
|---|---|---|---|
| [spiced-framework](spiced/spiced-framework.md) | overview | [SPICED Framework](https://winningbydesign.com/spiced-framework/) · also [SPICED Operating Model](https://winningbydesign.com/design/spiced-operating-model/) | First-party SPICED definitions and its role across the lifecycle. |
| [operating-model-for-recurring-revenue](spiced/operating-model-for-recurring-revenue.md) | diagnosis | [Fundamental Models of Recurring Revenue (PDF)](https://winningbydesign.com/wp-content/uploads/2022/06/Research-Paper_-The-Fundamental-Models-of-Recurring-Revenue.pdf) | The deepest public SPICED source: definitions, conversation flow, Critical vs. compelling event, granular post-sale metrics. |
| [the-spiced-framework-blueprint](spiced/the-spiced-framework-blueprint.md) | overview | [The SPICED Framework blueprint](https://winningbydesign.com/resources/blueprints/the-spiced-framework/) | Takeaways on non-linear discovery and summarizing (partial, gated). |
| [spiced-across-the-customer-journey](spiced/spiced-across-the-customer-journey.md) | customer-journey | [SPICED Across the Customer Journey](https://winningbydesign.com/resources/blueprints/spiced-across-the-customer-journey/) | Treats SPICED as a living account record owned by CSMs and AMs (partial, gated). |
| [how-to-diagnose](spiced/how-to-diagnose.md) | diagnosis | [How to Diagnose](https://winningbydesign.com/resources/blueprints/how-to-diagnose/) | Diagnosis-before-prescription flow for QBRs and expansion conversations (partial, gated). |
| [emotional-vs-rational-impact](spiced/emotional-vs-rational-impact.md) | impact | [Emotional Versus Rational Impact](https://winningbydesign.com/resources/blog/emotional-versus-rational-impact/) | Adds the emotional dimension of impact and its post-sale use in renewal and expansion. |
| [deal-analysis-with-spiced](spiced/deal-analysis-with-spiced.md) | deal-inspection | [Analyzing a Deal](https://winningbydesign.com/resources/blog/deal-analysis/) | Win/loss analysis questions transferable to churn and expansion post-mortems. |
| [comparison-meddic-and-spiced-wbd-view](spiced/comparison-meddic-and-spiced-wbd-view.md) | framework-comparison | [MEDDIC and SPICED 2023](https://winningbydesign.com/resources/blog/meddic-and-spiced-2023-two-different-approaches-2/) | Winning by Design's integration steps for using both frameworks together (vendor-biased). |

### `account-management/` — Winning by Design and MEDDICC (14)

| Document | Topic | Source | Why it is valuable to the AM Copilot |
|---|---|---|---|
| [account-management-for-growth](account-management/account-management-for-growth.md) | account-management-curriculum | [Account Management for Growth](https://winningbydesign.com/training-coaching/account-management-for-growth/) · also [Revenue Academy listing](https://winningbydesign.com/revenue-academy/course-account-management-for-growth/) | Winning by Design's own sequence for AM: diagnose, plan, earn renewal, whitespace, executives, trade, storytelling. |
| [customer-success-for-impact](account-management/customer-success-for-impact.md) | customer-success-curriculum | [Customer Success for Impact](https://winningbydesign.com/training-coaching/customer-success-for-impact/) | Vocabulary for EBRs, save plays, and First Value / Full Value. |
| [customer-success-operating-model](account-management/customer-success-operating-model.md) | customer-success-operating-model | [CS Operating Model blueprint](https://winningbydesign.com/resources/blueprints/customer-success-operating-model/) | States that expansion is gated on achieved impact (partial, gated). |
| [customer-success-as-profit-center](account-management/customer-success-as-profit-center.md) | expansion-economics | [CS as a Profit Center (PDF)](https://winningbydesign.com/wp-content/uploads/2022/05/WbD-Research-Customer-Success-as-a-Profit-Center.pdf) | The economic case for in-year expansion cadence and time-based coverage. |
| [first-impact](account-management/first-impact.md) | value-realization | [First Impact](https://winningbydesign.com/resources/blueprints/first-impact/) | Defines the first value milestone that renewal evidence rests on (partial, gated). |
| [joint-impact-plan](account-management/joint-impact-plan.md) | value-realization | [Joint Impact Plan](https://winningbydesign.com/resources/blueprints/create-a-joint-impact-plan/) | A 12-month co-created plan extending past renewal (partial, gated). |
| [the-saas-sales-method](account-management/the-saas-sales-method.md) | operating-model | [The SaaS Sales Method](https://winningbydesign.com/resources/blog/the-saas-sales-method-2/) | The post-sale stance: orchestrating, results, and growing instead of upselling. |
| [saas-roles-and-definitions](account-management/saas-roles-and-definitions.md) | roles-and-definitions | [SaaS Roles Definitions](https://winningbydesign.com/resources/blog/saas-role-definitions/) · also [SaaS Definitions](https://winningbydesign.com/resources/blog/saas-definitions/) | Distinguishes AM (commercial) from CSM (adoption, retention) responsibilities. |
| [bowtie-model](account-management/bowtie-model.md) | bowtie | [The Bowtie](https://winningbydesign.com/bowtie/) · also [Bowtie Standard landing page](https://winningbydesign.com/resources/research/bowtie-standard/) | The lifecycle model the AM's territory sits on. |
| [meddpicc-for-customer-success](account-management/meddpicc-for-customer-success.md) | customer-success | [MEDDPICC for Customer Success](https://meddicc.com/resources/meddpicc-as-framework-customer-success) | What each MEDDPICC element means after the sale. |
| [meddic-for-customer-success-webinar](account-management/meddic-for-customer-success-webinar.md) | customer-success | [MEDDIC for CS Takeaways](https://meddicc.com/resources/meddic-for-customer-success-live-webinar-takeaways) | Pain amnesia, renewal decision process, and five CS plays. |
| [customer-success-metrics-harvesting-vs-mining](account-management/customer-success-metrics-harvesting-vs-mining.md) | value-realization | [Harvesting vs Mining](https://meddicc.com/resources/generating-customer-success-metrics) | How to rebuild value evidence and reset a drifted account. |
| [meddpicc-customer-lifecycle-intro](account-management/meddpicc-customer-lifecycle-intro.md) | customer-lifecycle | [Customer Lifecycle Framework Intro](https://meddicc.com/resources/meddpicc-customer-lifecycle-marketing-framework-introduction) | The Value / Stakeholders / Process lens for inspecting any account. |
| [meddpicc-for-revops](account-management/meddpicc-for-revops.md) | customer-lifecycle | [MEDDPICC for RevOps](https://meddicc.com/resources/meddpicc-as-framework-revops) | Eight pressure-test questions for renewal and expansion forecasts. |

### `expansion/` — Winning by Design and MEDDICC (5)

| Document | Topic | Source | Why it is valuable to the AM Copilot |
|---|---|---|---|
| [bowtie-expansion-types](expansion/bowtie-expansion-types.md) | expansion-types | [The Bowtie: A Proposed Standard (PDF)](https://winningbydesign.com/wp-content/uploads/2026/02/The-Bowtie-A-Proposed-Standard.pdf) | First-party definitions of upsell, cross-sell, renewal and resell, with ownership guidance. |
| [expansion-and-retention-playbooks](expansion/expansion-and-retention-playbooks.md) | expansion-system | [Playbooks](https://winningbydesign.com/deploy/playbooks/) | Names the components of a systematic expansion and retention motion (promotional). |
| [trade-instead-of-negotiate](expansion/trade-instead-of-negotiate.md) | commercial-conversations | [How to Trade Instead of Negotiate](https://winningbydesign.com/resources/blog/how-to-trade-instead-of-negotiate/) | A step-by-step renewal and expansion commercial conversation. |
| [meddpicc-for-account-expansion](expansion/meddpicc-for-account-expansion.md) | expansion | [MEDDPICC for Account Executives](https://meddicc.com/resources/meddpicc-as-framework-account-executive) | Four MEDDPICC questions for expansion, including who has veto over it. |
| [value-based-negotiation-meddicc](expansion/value-based-negotiation-meddicc.md) | commercial-conversations | [Rethinking Negotiation](https://meddicc.com/resources/rethinking-negotiation-in-sales) | Why the business case, not tactics, wins procurement conversations. |

### `account-planning/` — Winning by Design and MEDDICC (5)

| Document | Topic | Source | Why it is valuable to the AM Copilot |
|---|---|---|---|
| [mapping-relationships](account-planning/mapping-relationships.md) | stakeholder-mapping | [Mapping Relationships](https://winningbydesign.com/resources/blueprints/mapping-relationships/) | Influence mapping reveals risk that stages cannot (partial, gated). |
| [the-stakeholder-meeting](account-planning/the-stakeholder-meeting.md) | executive-engagement | [The Stakeholder Meeting](https://winningbydesign.com/resources/blueprints/the-stakeholder-meeting/) | A three-phase structure that maps onto an expansion-focused EBR (partial, gated). |
| [target-account-tiering](account-planning/target-account-tiering.md) | account-prioritization | [Target Account List](https://winningbydesign.com/resources/blog/how-to-create-a-target-account-list-for-your-enterprise-team/) | The only public Winning by Design tiering logic, transferable to an existing book. |
| [multi-threading](account-planning/multi-threading.md) | multithreading | [What It Really Means to Multi-Thread](https://meddicc.com/resources/what-it-really-means-to-multi-thread) | Quality over contact count, and threading your own side too. |
| [sales-velocity-account-level-thinking](account-planning/sales-velocity-account-level-thinking.md) | account-prioritization | [Opportunity Obsession](https://meddicc.com/resources/your-obsession-with-opportunities-is-costing-you-revenue) | Why deal size and conversion beat opportunity count for an AM. |

---

## Sources reviewed but excluded

| Source | Reason |
|---|---|
| [MEDDICC — Net Revenue Retention use case](https://meddicc.com/use-case/increase-nrr) | Mostly marketing; no methodology beyond one framing line |
| [MEDDICC — MEDDPICC-R Risk Level Matrix](https://meddicc.com/resources/meddpicc-r-meddpiccr-risks) | Page failed to load (redirect loop); appears member-gated |
| MEDDICC Deal Sheet, Go-Live Plan template, Masterclass, Playbook | Gated or paid |
| MEDDICC media and resource index pages | Discovery indexes only; individual articles were ingested |
| Winning by Design CS Operating Model chapter PDFs (Core Elements, Metrics, Onboarding, Expansion, Skills) | Returned 404 at retrieval |
| Winning by Design combined CS Operating Model PDF | Marked proprietary and confidential; gated behind a form — not accessed |
| Winning by Design "How to Get the Renewal" blueprint PDF | Marked proprietary and confidential; gated blueprint — not accessed |
| Winning by Design "The SaaS Sales Method" blueprint PDF | Marked proprietary and confidential; the public blog version was used instead |
| Winning by Design "SPICED Blueprints Workshop" PDF | Marked proprietary and confidential — not accessed |
| Winning by Design "How to Establish Impact" blueprint PDF | Direct link to a gated blueprint; the public emotional-vs-rational impact post was used instead |
| [Winning by Design — The Bowtie Standard](https://winningbydesign.com/resources/research/bowtie-standard/) (full PDF) | Gated; public landing summary merged into `bowtie-model` |
| [Winning by Design — Growth Governance Guide](https://winningbydesign.com/resources/blueprints/growth-governance-guide/) | Gated; public summary is board- and CRO-level governance with little AM relevance |
| [Winning by Design — Expansion & Growth Playbook service page](https://winningbydesign.com/services/expansion-growth-playbook/) | Redirected to a generic services page; content captured from the playbooks page |
| Winning by Design `resource_type` archive pages (Expansion, Impact) | Rendered without resource listings |
| Winning by Design Growth Journal articles | Subscription publication — not accessed |

---

## Known gaps

These are the areas where the public record is thin, so the copilot should
reason carefully and say when it is inferring:

- **Whitespace analysis method, account-plan templates, expansion signal and
  trigger-play catalogs, next-best-action logic.** Winning by Design teaches these
  in paid courses and playbooks; the public corpus has only their named components
  and learning objectives.
- **Prioritizing an existing book.** No first-party public method beyond
  new-logo tiering and the profit-center economics.
- **MEDDICC question banks and scoring rubrics.** Held in the paid Masterclass;
  the corpus has practitioner questions from articles instead.
- **Renewal-specific Winning by Design playbooks.** Gated.

## Relationship to `coach/kb/`

`coach/kb/` holds the SuccessCOACHING playbook and earlier model-authored SPICED,
MEDDPICC and framework-selection documents. Those were written from general
knowledge rather than these sources and were kept unchanged. Where they differ
from this corpus — for example, older "Identify Pain" wording versus MEDDICC's
"Implicate the Pain" — treat this sourced corpus as authoritative.
