---
framework: cross-framework
topic: corpus-index
source_title: Sales Methodology Corpus Index
source_org: Project-authored
source_authority: Project-authored synthesis (not from an external source)
source_type: secondary
priority: 5
framework_version: not applicable
public_url: none (not publicly published)
source_url: none (not publicly published)
published_date: '2026-09-13'
date_basis: date of the provenance audit
retrieved_date: not applicable
license: unknown
reproduction_status: model_authored
---

# Sales Methodology Corpus — Index

A sourced knowledge corpus for an Account Management / Customer Success Copilot
that coaches AMs on account strategy, expansion, renewals, stakeholder
management, discovery and opportunity execution.

- **Primary sources:** first-party MEDDICC content (MEDDPICC) and first-party
  Winning by Design content (SPICED, the Bowtie, account management, expansion).
- **Retrieved:** 2026-09-12. Public content only; no logins, paywalls or forms
  were bypassed.
- **Documents:** 72 source documents, plus `TERMINOLOGY.md` (a
  cross-framework crosswalk) and this index.
- **Provenance audit:** 2026-09-13. See *Conflicts and terminology differences*
  and *Documents with unclear or limited provenance* below.

---

## Design principle

The frameworks are complementary, not competing, and no framework wins globally.

| Layer | Job | Used when |
|---|---|---|
| **SPICED** (Winning by Design) | Persistent account and opportunity state; diagnosis and discovery | Maintained continuously. Actively invoked when understanding a customer problem, a change, an opportunity, desired impact, urgency, or the decision process. Not a checklist for every interaction. |
| **Account planning / expansion** | Deciding where opportunity exists across the account and what to pursue | Planning the account, reviewing whitespace, deciding upsell vs. cross-sell vs. resell |
| **MEDDPICC** (MEDDICC) | Qualifying and executing a concrete commercial opportunity | Most prominent once a credible renewal or expansion opportunity exists |

Keep each framework's own terminology. Where concepts overlap, the mapping is in
`TERMINOLOGY.md` and the original terms are kept. For example, Winning by Design's
**Critical Event** and MEDDICC's **Compelling Event** are related but defined
differently, and are never merged.

---

## Provenance and retrieval authority

### Authority ranking

| Rank | `source_type` | `priority` | What qualifies |
|---|---|---|---|
| 1 | `canonical` | 1 | A current first-party page whose purpose is to define the framework or its elements |
| 2 | `practitioner_article` | 2 | Current first-party application material: articles, podcast and webinar summaries, blueprints, course and service descriptions |
| 3 | `research` | 3 | First-party research papers and proposed standards |
| 4 | `historical` | 4 | First-party material with evidence of superseded naming or content (`historical_reason` says why) |
| 5 | `secondary` | 5 | Anything not first-party for the framework in question: project-authored synthesis, model notes, and one vendor's description of another's framework |

- **Authority is assessed per framework.** A MEDDICC document is first-party for
  MEDDPICC and secondary for SPICED; a Winning by Design document is the reverse.
  `first_party_for` and `secondary_for` record this.
- **Older material does not override newer canonical definitions.** Where a
  definition changed over time, both versions are kept and the difference is
  listed under *Conflicts*.
- **`secondary` extends the four requested source types** so the ranking's fifth
  tier can be represented.
- **Model notes.** Headings ending in "(model note)" mark project inference inside
  sourced documents. At upload, `provision.py` tags those sections
  `[model note · secondary · P5]` instead of using the document's own tag. Every
  other heading is tagged with the document's framework, organization, type and
  priority, so provenance travels with each retrieved chunk.

### Metadata fields

| Field | Meaning |
|---|---|
| `framework` | `meddpicc`, `spiced`, `account-management`, `expansion`, `account-planning`, `successcoaching`, or `cross-framework` |
| `topic` | The specific subject |
| `source_title` / `source_org` | The primary source's title and publishing organization |
| `source_authority` | Who stands behind the content, and in what capacity |
| `source_type` / `priority` | Position in the authority ranking above |
| `first_party_for` / `secondary_for` | Frameworks this document is, or is not, a first-party source for |
| `framework_version` | The framework variant or version the source uses, where identifiable |
| `public_url` / `source_url` | Where the source can be read (identical for every sourced document) |
| `also_covers` | Additional URLs merged in because they substantially overlapped |
| `published_date` / `date_basis` | Publication date if identifiable, and how it was determined |
| `retrieved_date` | When the content was retrieved |
| `license` | Explicit license if known, otherwise `unknown` |
| `reproduction_status` | How the content was reproduced (see below) |
| `content_status` | Coverage limits: gated assets, outlines, PDF extraction |
| `historical_reason` / `bias_note` | Why a document is historical; vendor bias in comparisons |

### Publication dates

- **Winning by Design** pages carry `datePublished` metadata, recorded as given.
  Five blueprints share 2022-05-09, which may reflect a site migration rather than
  original publication.
- **MEDDICC** component pages show no date. About 30 MEDDICC articles all show
  25–27 May 2026, including articles whose MEDDIC-era titles suggest older
  content, so that date is treated as a site date: `published_date` is `unknown`
  and the displayed date is kept in `date_basis`. Dates outside that cluster are
  recorded as shown.
- **PDFs** use a date stated in the document text where one exists.

### License and reproduction

**Every document is `license: unknown`.** No source states license terms. Public
accessibility, and the absence of a confidentiality notice, are not treated as
permission to reproduce. All sourced content is attributed paraphrase with only
short quoted phrases — no verbatim mirrors.

| `reproduction_status` | Meaning |
|---|---|
| `paraphrased_notes` | Full public page read; restructured, attributed paraphrase |
| `paraphrased_notes_partial` | Only the public summary of a gated asset was used |
| `paraphrased_notes_outline` | A course or service description; the underlying material was not accessed |
| `paraphrased_notes_pdf_extract` | A PDF reachable by direct link; text extracted locally and paraphrased |
| `restructured_user_provided` | Restructured from the user-provided SuccessCOACHING playbook, with marked model elaboration |
| `model_authored` | Written by this project |

---

## Coverage map — the ten AM Copilot jobs

| # | Job | Primary documents |
|---|---|---|
| 1 | Understand an account | `spiced/spiced-framework`, `spiced/spiced-across-the-customer-journey`, `spiced/operating-model-for-recurring-revenue`, `account-management/bowtie-model`, `account-management/meddpicc-customer-lifecycle-intro` |
| 2 | Identify whitespace and expansion hypotheses | `expansion/bowtie-expansion-types`, `expansion/expansion-and-retention-playbooks`, `account-management/account-management-for-growth`, `account-planning/target-account-tiering`, `expansion/meddpicc-for-account-expansion` |
| 3 | Diagnose customer problems | `spiced/how-to-diagnose`, `spiced/operating-model-for-recurring-revenue`, `meddpicc/pain-are-you-really-implicating`, `meddpicc/pain-stakeholder-specific`, `meddpicc/decision-process-three-discovery-questions`, `meddpicc/metrics-uncovering-more-metrics` |
| 4 | Quantify business impact | `spiced/emotional-vs-rational-impact`, `meddpicc/metrics`, `meddpicc/metrics-personalizing-metrics`, `account-management/customer-success-metrics-harvesting-vs-mining`, `account-management/customer-success-as-profit-center` |
| 5 | Identify relevant stakeholders | `account-planning/mapping-relationships`, `account-planning/multi-threading`, `account-planning/the-stakeholder-meeting`, `meddpicc/economic-buyer*`, `meddpicc/champion*` |
| 6 | Recognize Critical Events (SPICED) and Compelling Events (MEDDPICC) | `TERMINOLOGY` (read first — the two terms are defined differently), `spiced/spiced-framework`, `meddpicc/compelling-event`, `spiced/operating-model-for-recurring-revenue`, `spiced/how-to-diagnose` |
| 7 | Turn expansion signals into opportunities | `expansion/bowtie-expansion-types`, `expansion/meddpicc-for-account-expansion`, `account-management/customer-success-for-impact`, `meddpicc/qualifying-out` |
| 8 | Advance opportunities commercially | `expansion/trade-instead-of-negotiate`, `expansion/value-based-negotiation-meddicc`, `meddpicc/decision-process`, `meddpicc/paper-process*`, `meddpicc/economic-buyer-dunkel-executive-selling` |
| 9 | Protect renewals | `account-management/meddic-for-customer-success-webinar`, `account-management/meddpicc-for-customer-success`, `account-management/first-impact`, `account-management/joint-impact-plan`, `expansion/bowtie-expansion-types` (resell), `meddpicc/competition-the-wrong-competition` |
| 10 | Coach the next best action | `meddpicc/failure-modes`, `meddpicc/deal-reviews`, `meddpicc/deal-reviews-lessons-from-implementation`, `meddpicc/coaching-three-ts`, `account-management/meddpicc-for-revops`, `spiced/deal-analysis-with-spiced` |

---

## Retained sources

Rows are ordered by priority within each folder. Counts: 11 canonical, 55 practitioner_article, 3 research, 3 historical.

### `meddpicc/` — MEDDICC (40)

| Document | Type · priority | Framework version | Published | Source | Why it is valuable to the AM Copilot |
|---|---|---|---|---|---|
| [champion](meddpicc/champion.md) | canonical · P1 | MEDDPICC | unknown | [Champion](https://meddicc.com/what-is-meddpicc/champion) · also [No Champion, No Deal](https://meddicc.com/resources/no-champion-no-deal) | The three-trait definition and the Champion / Coach / Friend distinction. |
| [competition](meddpicc/competition.md) | canonical · P1 | MEDDPICC | unknown | [Competition](https://meddicc.com/what-is-meddpicc/competition) | Four competitor types, including inertia and competing initiatives. |
| [decision-criteria](meddpicc/decision-criteria.md) | canonical · P1 | MEDDPICC | unknown | [Decision Criteria](https://meddicc.com/what-is-meddpicc/decision-criteria) | Technical, economic and relationship criteria, and why sellers should shape them. |
| [decision-process](meddpicc/decision-process.md) | canonical · P1 | MEDDPICC | unknown | [Decision Process](https://meddicc.com/what-is-meddpicc/decision-process) | "Engagement is not progress" — a core correction for stalled expansions. |
| [economic-buyer](meddpicc/economic-buyer.md) | canonical · P1 | MEDDPICC | unknown | [Economic Buyer](https://meddicc.com/what-is-meddpicc/economic-buyer) | Identification markers and the Champion-access test for executive authority. |
| [implicate-the-pain](meddpicc/implicate-the-pain.md) | canonical · P1 | MEDDPICC | unknown | [Implicate the Pain](https://meddicc.com/what-is-meddpicc/implicate-the-pain) | The Identify → Indicate → Implicate progression behind "why now." |
| [metrics](meddpicc/metrics.md) | canonical · P1 | MEDDPICC | unknown | [Metrics](https://meddicc.com/what-is-meddpicc/metrics) | The M1/M2/M3 value cycle that links pre-sale promises to post-sale realized value and renewal evidence. |
| [overview](meddpicc/overview.md) | canonical · P1 | MEDDPICC (current); page also covers MEDDIC and MEDDICC lineage | unknown | [MEDDPICC Methodology and Process](https://meddicc.com/meddpicc-sales-methodology-and-process) · also [AI Info](https://meddicc.com/ai-info) | Authoritative element definitions, lineage, and the "Implicate the Pain" terminology. |
| [paper-process](meddpicc/paper-process.md) | canonical · P1 | MEDDPICC | unknown | [Paper Process](https://meddicc.com/what-is-meddpicc/paper-process) | Explains why "yes" is not closed — the main renewal slip point. |
| [champion-building-in-a-downturn](meddpicc/champion-building-in-a-downturn.md) | practitioner_article · P2 | MEDDPICC | unknown | [Champion Building During a Downturn](https://meddicc.com/resources/champion-building-takeaways) | Risk-reduction tactics for Champions staking credibility on an expansion. |
| [champion-closing-without-being-in-the-room](meddpicc/champion-closing-without-being-in-the-room.md) | practitioner_article · P2 | MEDDPICC | 2026-04-23 | [Close Deals Without Being in the Room](https://meddicc.com/meddicc-media/medmen-how-to-close-deals-without-being-in-the-room) | Multiple-Champion strategy and a practical Champion engagement test. |
| [champion-five-signs](meddpicc/champion-five-signs.md) | practitioner_article · P2 | MEDDPICC | unknown | [5 Signs You Don't Have a Champion](https://meddicc.com/resources/5-signs-you-dont-have-a-champion) | Observable tests the copilot can apply to an AM's claimed Champion. |
| [champion-getting-in-trouble](meddpicc/champion-getting-in-trouble.md) | practitioner_article · P2 | MEDDPICC | unknown | [Getting in Trouble With Your Champion](https://meddicc.com/resources/getting-in-trouble-with-your-champion) | Coaches AMs past "nice seller" avoidance of uncomfortable asks. |
| [champion-vested-interest](meddpicc/champion-vested-interest.md) | practitioner_article · P2 | MEDDPICC | unknown | [The Overlooked Champion Trait](https://meddicc.com/resources/medmen-the-crucial-but-overlooked-champion-trait) | How to uncover what a Champion personally gains. |
| [coaching-three-ts](meddpicc/coaching-three-ts.md) | practitioner_article · P2 | MEDDIC (naming used in source title) | unknown | [MEDDIC Coaching](https://meddicc.com/resources/medmen-meddic-coaching) | Trust, Timing, Tactics — how coaching lands. |
| [comparison-spiced-vs-meddpicc-meddicc-view](meddpicc/comparison-spiced-vs-meddpicc-meddicc-view.md) | practitioner_article · P2 | MEDDPICC; describes SPICED as a third party | 2026-07-30 | [SPICED vs MEDDPICC](https://meddicc.com/resources/spiced-sales-methodology-vs-meddpicc-meddicc) | MEDDICC's element mapping and claimed SPICED gaps (vendor-biased). |
| [compelling-event](meddpicc/compelling-event.md) | practitioner_article · P2 | MEDDPICC | 2026-08-13 | [The Necessity of a Compelling Event](https://meddicc.com/resources/the-necessity-of-a-compelling-event) | Real vs. manufactured urgency, with a test the copilot can apply. |
| [competition-dont-knock-the-competition](meddpicc/competition-dont-knock-the-competition.md) | practitioner_article · P2 | MEDDPICC | unknown | [Don't Knock the Competition](https://meddicc.com/resources/why-you-shouldnt-knock-the-competition) | How to defend a renewal against a returning competitor without FUD. |
| [competition-the-wrong-competition](meddpicc/competition-the-wrong-competition.md) | practitioner_article · P2 | MEDDPICC | unknown | [Obsessing Over the Wrong Competition](https://meddicc.com/resources/medmen-obsessing-over-the-wrong-competition) | Diagnoses slippage to inertia across value, stakeholders and process. |
| [deal-reviews-lessons-from-implementation](meddpicc/deal-reviews-lessons-from-implementation.md) | practitioner_article · P2 | MEDDICC (naming used in source) | unknown | [Lessons Since Implementing MEDDICC](https://meddicc.com/resources/lessons-ive-learnt-since-implementing-meddic) | Ten practical adoption lessons including 1–10 confidence scoring. |
| [deal-reviews](meddpicc/deal-reviews.md) | practitioner_article · P2 | MEDDPICC | unknown | [Deal Reviews](https://meddicc.com/resources/mastering-meddpicc-deal-reviews) · also [Directing](https://meddicc.com/resources/leadership-in-meddpicc-mastery), [Reinventing](https://meddicc.com/resources/reinventing-deal-reviews) | Forward-looking review cadence and psychological safety for honest inspection. |
| [decision-criteria-proactive](meddpicc/decision-criteria-proactive.md) | practitioner_article · P2 | MEDDPICC | unknown | [Proactive Decision Criteria](https://meddicc.com/resources/medmen-take-a-proactive-approach-to-decision-criteria) | Buyer-side lessons on what makes deals collapse to price. |
| [decision-criteria-three-dimensional](meddpicc/decision-criteria-three-dimensional.md) | practitioner_article · P2 | MEDDPICC | unknown | [3-Dimensional Decision Criteria](https://meddicc.com/resources/3-dimensional-decision-criteria) | Shows how relationship and economic criteria differentiate near-identical offerings. |
| [decision-process-three-discovery-questions](meddpicc/decision-process-three-discovery-questions.md) | practitioner_article · P2 | MEDDPICC | unknown | [Three Discovery Questions](https://meddicc.com/resources/medmen-three-discovery-questions-that-feel-like-cheating) | Question scripts that map directly to how the last renewal or add-on was approved. |
| [economic-buyer-dunkel-executive-selling](meddpicc/economic-buyer-dunkel-executive-selling.md) | practitioner_article · P2 | MEDDPICC | unknown | [EB Selling with Dick Dunkel](https://meddicc.com/resources/economic-buyer-selling-takeaways) | Executive research, outreach and funding-discovery questions from MEDDIC's originator. |
| [economic-buyer-five-mistakes](meddpicc/economic-buyer-five-mistakes.md) | practitioner_article · P2 | MEDDPICC | unknown | [5 Things Not to Do With the EB](https://meddicc.com/resources/medmen-5-things-not-to-do-when-engaging-with-the-economic-buyer) | A ready checklist for preparing an AM before an executive meeting. |
| [economic-buyer-qualifying](meddpicc/economic-buyer-qualifying.md) | practitioner_article · P2 | MEDDPICC | unknown | [Qualifying the Economic Buyer](https://meddicc.com/resources/qualifying-the-economic-buyer) | Separates Budget Holder from EB and recommends keeping the EB informed post-sale for upsell. |
| [economic-buyer-value-pyramid](meddpicc/economic-buyer-value-pyramid.md) | practitioner_article · P2 | MEDDPICC | unknown | [Value Pyramid With the EB](https://meddicc.com/resources/medmen-using-a-value-pyramid-with-the-economic-buyer) | A tool for re-establishing strategic alignment after executive or priority changes. |
| [economic-buyer-vs-champion](meddpicc/economic-buyer-vs-champion.md) | practitioner_article · P2 | MEDDPICC | 2024-04-03 | [Misidentifying Champions](https://meddicc.com/meddicc-media/medmen-s2-ep1-misidentifying-champions) | Discovery questions to find the real EB and the "CFO by default" rule. |
| [expert-panel-elements](meddpicc/expert-panel-elements.md) | practitioner_article · P2 | MEDDPICC | unknown | [Experts Discuss the Elements](https://meddicc.com/resources/meddicon-experts) | Practitioner views on underrated elements and uncovering pain. |
| [failure-modes](meddpicc/failure-modes.md) | practitioner_article · P2 | MEDDPICC; two merged articles use MEDDIC naming | 2026-05-17 | [Why MEDDPICC Fails](https://meddicc.com/meddicc-media/medmen-why-meddpicc-fails-in-your-team-its-not-what-you-think) · also [Not a Checklist](https://meddicc.com/resources/meddic-is-not-a-checklist), [Isn't One and Done](https://meddicc.com/resources/medmen-meddic-isnt-one-and-done) | Keeps the copilot from turning MEDDPICC into a checkbox exercise. |
| [forecast-confidence](meddpicc/forecast-confidence.md) | practitioner_article · P2 | MEDDICC (naming used in source title) | unknown | [Forecast Confidence](https://meddicc.com/resources/achieving-forecast-confidence-with-meddicc) | Maps forecast misses to specific MEDDPICC weaknesses. |
| [metrics-personalizing-metrics](meddpicc/metrics-personalizing-metrics.md) | practitioner_article · P2 | MEDDPICC | unknown | [Personalize Metrics](https://meddicc.com/resources/medmen-why-you-need-to-personalize-metrics) | Teaches per-stakeholder value, essential when multithreading an expansion. |
| [metrics-solution-to-inertia](meddpicc/metrics-solution-to-inertia.md) | practitioner_article · P2 | MEDDPICC | unknown | [Metrics as a Solution to Inertia](https://meddicc.com/resources/metrics-as-a-solution-to-inertia) | Frames no-decision as the main competitor and quantified value as the remedy. |
| [metrics-uncovering-more-metrics](meddpicc/metrics-uncovering-more-metrics.md) | practitioner_article · P2 | MEDDPICC | unknown | [Uncover More Metrics](https://meddicc.com/resources/medmen-uncover-more-metrics) | The Three Ps give the AM a concrete way to find metrics customers will not volunteer. |
| [pain-are-you-really-implicating](meddpicc/pain-are-you-really-implicating.md) | practitioner_article · P2 | MEDDPICC | unknown | [Are You Really Implicating the Pain?](https://meddicc.com/resources/are-you-really-implicating-the-pain) | A pipeline self-check and the warning that implications fade over time. |
| [pain-stakeholder-specific](meddpicc/pain-stakeholder-specific.md) | practitioner_article · P2 | MEDDPICC | unknown | [Pain is Stakeholder-Specific](https://meddicc.com/resources/pain-is-stakeholder-specific) | Worked example of mapping one pain across seven executive roles. |
| [paper-process-go-live-plan](meddpicc/paper-process-go-live-plan.md) | practitioner_article · P2 | MEDDPICC | 2026-08-24 | [Go-Live Plan](https://meddicc.com/resources/go-live-plan) | Mutual plan anchored on time-to-impact; transferable to expansion timelines. |
| [paper-process-mastering](meddpicc/paper-process-mastering.md) | practitioner_article · P2 | MEDDPICC | unknown | [Master the Paper Process](https://meddicc.com/resources/meddpicc-paper-process-meddicc) | Operational components of contracting that an AM can start in parallel. |
| [qualifying-out](meddpicc/qualifying-out.md) | practitioner_article · P2 | MEDDICC (naming used in source URL) | 2026-08-20 | [Nobody Regrets Qualifying Out](https://meddicc.com/resources/alexa-email-cadence-meddicc) | Permission to drop weak expansion hypotheses. |

### `spiced/` — Winning by Design (8)

| Document | Type · priority | Framework version | Published | Source | Why it is valuable to the AM Copilot |
|---|---|---|---|---|---|
| [spiced-framework](spiced/spiced-framework.md) | canonical · P1 | SPICED, current page (2025) | 2025-11-28 | [SPICED Framework](https://winningbydesign.com/spiced-framework/) · also [SPICED Operating Model](https://winningbydesign.com/design/spiced-operating-model/) | First-party SPICED definitions and its role across the lifecycle. |
| [deal-analysis-with-spiced](spiced/deal-analysis-with-spiced.md) | practitioner_article · P2 | SPICED | 2022-06-27 | [Analyzing a Deal](https://winningbydesign.com/resources/blog/deal-analysis/) | Win/loss analysis questions transferable to churn and expansion post-mortems. |
| [emotional-vs-rational-impact](spiced/emotional-vs-rational-impact.md) | practitioner_article · P2 | SPICED | 2021-11-04 | [Emotional Versus Rational Impact](https://winningbydesign.com/resources/blog/emotional-versus-rational-impact/) | Adds the emotional dimension of impact and its post-sale use in renewal and expansion. |
| [how-to-diagnose](spiced/how-to-diagnose.md) | practitioner_article · P2 | SPICED | 2022-05-09 | [How to Diagnose](https://winningbydesign.com/resources/blueprints/how-to-diagnose/) | Diagnosis-before-prescription flow for QBRs and expansion conversations (partial, gated). |
| [spiced-across-the-customer-journey](spiced/spiced-across-the-customer-journey.md) | practitioner_article · P2 | SPICED | 2022-05-09 | [SPICED Across the Customer Journey](https://winningbydesign.com/resources/blueprints/spiced-across-the-customer-journey/) | Treats SPICED as a living account record owned by CSMs and AMs (partial, gated). |
| [the-spiced-framework-blueprint](spiced/the-spiced-framework-blueprint.md) | practitioner_article · P2 | SPICED blueprint (2022) | 2022-04-15 | [The SPICED Framework blueprint](https://winningbydesign.com/resources/blueprints/the-spiced-framework/) | Takeaways on non-linear discovery and summarizing (partial, gated). |
| [operating-model-for-recurring-revenue](spiced/operating-model-for-recurring-revenue.md) | research · P3 | SPICED as defined in the 2022 research paper | unknown | [Fundamental Models of Recurring Revenue (PDF)](https://winningbydesign.com/wp-content/uploads/2022/06/Research-Paper_-The-Fundamental-Models-of-Recurring-Revenue.pdf) | The most detailed public SPICED definitions found during retrieval: conversation flow, Critical vs. compelling event, granular post-sale metrics. |
| [comparison-meddic-and-spiced-wbd-view](spiced/comparison-meddic-and-spiced-wbd-view.md) | historical · P4 | SPICED (2023); describes the six-letter MEDDIC form | 2023-09-06 | [MEDDIC and SPICED 2023](https://winningbydesign.com/resources/blog/meddic-and-spiced-2023-two-different-approaches-2/) | Winning by Design's integration steps for using both frameworks together (vendor-biased). |

### `account-management/` — Winning by Design and MEDDICC (14)

| Document | Type · priority | Framework version | Published | Source | Why it is valuable to the AM Copilot |
|---|---|---|---|---|---|
| [bowtie-model](account-management/bowtie-model.md) | canonical · P1 | Bowtie, current page (2026) | 2026-03-04 | [The Bowtie](https://winningbydesign.com/bowtie/) · also [Bowtie Standard landing page](https://winningbydesign.com/resources/research/bowtie-standard/) | The lifecycle model the AM's territory sits on. |
| [account-management-for-growth](account-management/account-management-for-growth.md) | practitioner_article · P2 | course listing current at retrieval | 2025-12-17 | [Account Management for Growth](https://winningbydesign.com/training-coaching/account-management-for-growth/) · also [Revenue Academy listing](https://winningbydesign.com/revenue-academy/course-account-management-for-growth/) | Winning by Design's own sequence for AM: diagnose, plan, earn renewal, whitespace, executives, trade, storytelling. |
| [customer-success-for-impact](account-management/customer-success-for-impact.md) | practitioner_article · P2 | course listing current at retrieval | 2025-12-16 | [Customer Success for Impact](https://winningbydesign.com/training-coaching/customer-success-for-impact/) | Vocabulary for EBRs, save plays, and First Value / Full Value. |
| [customer-success-metrics-harvesting-vs-mining](account-management/customer-success-metrics-harvesting-vs-mining.md) | practitioner_article · P2 | MEDDPICC | unknown | [Harvesting vs Mining](https://meddicc.com/resources/generating-customer-success-metrics) | How to rebuild value evidence and reset a drifted account. |
| [customer-success-operating-model](account-management/customer-success-operating-model.md) | practitioner_article · P2 | unversioned | 2022-10-03 | [CS Operating Model blueprint](https://winningbydesign.com/resources/blueprints/customer-success-operating-model/) | States that expansion is gated on achieved impact (partial, gated). |
| [first-impact](account-management/first-impact.md) | practitioner_article · P2 | unversioned | 2023-07-31 | [First Impact](https://winningbydesign.com/resources/blueprints/first-impact/) | Defines the first value milestone that renewal evidence rests on (partial, gated). |
| [joint-impact-plan](account-management/joint-impact-plan.md) | practitioner_article · P2 | unversioned | 2022-05-09 | [Joint Impact Plan](https://winningbydesign.com/resources/blueprints/create-a-joint-impact-plan/) | A 12-month co-created plan extending past renewal (partial, gated). |
| [meddic-for-customer-success-webinar](account-management/meddic-for-customer-success-webinar.md) | practitioner_article · P2 | MEDDIC (naming used in source title) | 2026-08-19 | [MEDDIC for CS Takeaways](https://meddicc.com/resources/meddic-for-customer-success-live-webinar-takeaways) | Pain amnesia, renewal decision process, and five CS plays. |
| [meddpicc-customer-lifecycle-intro](account-management/meddpicc-customer-lifecycle-intro.md) | practitioner_article · P2 | MEDDPICC | unknown | [Customer Lifecycle Framework Intro](https://meddicc.com/resources/meddpicc-customer-lifecycle-marketing-framework-introduction) | The Value / Stakeholders / Process lens for inspecting any account. |
| [meddpicc-for-customer-success](account-management/meddpicc-for-customer-success.md) | practitioner_article · P2 | MEDDPICC | unknown | [MEDDPICC for Customer Success](https://meddicc.com/resources/meddpicc-as-framework-customer-success) | What each MEDDPICC element means after the sale. |
| [meddpicc-for-revops](account-management/meddpicc-for-revops.md) | practitioner_article · P2 | MEDDPICC | unknown | [MEDDPICC for RevOps](https://meddicc.com/resources/meddpicc-as-framework-revops) | Eight pressure-test questions for renewal and expansion forecasts. |
| [customer-success-as-profit-center](account-management/customer-success-as-profit-center.md) | research · P3 | unversioned research paper (2021) | 2021-03 | [CS as a Profit Center (PDF)](https://winningbydesign.com/wp-content/uploads/2022/05/WbD-Research-Customer-Success-as-a-Profit-Center.pdf) | The economic case for in-year expansion cadence and time-based coverage. |
| [saas-roles-and-definitions](account-management/saas-roles-and-definitions.md) | historical · P4 | unversioned (2019 posts) | 2019-08-23 | [SaaS Roles Definitions](https://winningbydesign.com/resources/blog/saas-role-definitions/) · also [SaaS Definitions](https://winningbydesign.com/resources/blog/saas-definitions/) | Distinguishes AM (commercial) from CSM (adoption, retention) responsibilities. |
| [the-saas-sales-method](account-management/the-saas-sales-method.md) | historical · P4 | SaaS Sales Method (2019 post; older Bowtie stage names) | 2019-08-22 | [The SaaS Sales Method](https://winningbydesign.com/resources/blog/the-saas-sales-method-2/) | The post-sale stance: orchestrating, results, and growing instead of upselling. |

### `expansion/` — Winning by Design and MEDDICC (5)

| Document | Type · priority | Framework version | Published | Source | Why it is valuable to the AM Copilot |
|---|---|---|---|---|---|
| [expansion-and-retention-playbooks](expansion/expansion-and-retention-playbooks.md) | practitioner_article · P2 | unversioned | 2026-07-22 | [Playbooks](https://winningbydesign.com/deploy/playbooks/) | Names the components of a systematic expansion and retention motion (promotional). |
| [meddpicc-for-account-expansion](expansion/meddpicc-for-account-expansion.md) | practitioner_article · P2 | MEDDPICC | unknown | [MEDDPICC for Account Executives](https://meddicc.com/resources/meddpicc-as-framework-account-executive) | Four MEDDPICC questions for expansion, including who has veto over it. |
| [trade-instead-of-negotiate](expansion/trade-instead-of-negotiate.md) | practitioner_article · P2 | unversioned | 2021-11-08 | [How to Trade Instead of Negotiate](https://winningbydesign.com/resources/blog/how-to-trade-instead-of-negotiate/) | A step-by-step renewal and expansion commercial conversation: three core levers plus additional assets. |
| [value-based-negotiation-meddicc](expansion/value-based-negotiation-meddicc.md) | practitioner_article · P2 | MEDDPICC | unknown | [Rethinking Negotiation](https://meddicc.com/resources/rethinking-negotiation-in-sales) | Why the business case, not tactics, wins procurement conversations. |
| [bowtie-expansion-types](expansion/bowtie-expansion-types.md) | research · P3 | The Bowtie: Proposed Standard v1.0 | unknown | [The Bowtie: A Proposed Standard (PDF)](https://winningbydesign.com/wp-content/uploads/2026/02/The-Bowtie-A-Proposed-Standard.pdf) | First-party definitions of upsell, cross-sell, renewal and resell, with ownership guidance. |

### `account-planning/` — Winning by Design and MEDDICC (5)

| Document | Type · priority | Framework version | Published | Source | Why it is valuable to the AM Copilot |
|---|---|---|---|---|---|
| [mapping-relationships](account-planning/mapping-relationships.md) | practitioner_article · P2 | unversioned | 2022-05-09 | [Mapping Relationships](https://winningbydesign.com/resources/blueprints/mapping-relationships/) | Influence mapping reveals risk that stages cannot (partial, gated). |
| [multi-threading](account-planning/multi-threading.md) | practitioner_article · P2 | MEDDPICC | unknown | [What It Really Means to Multi-Thread](https://meddicc.com/resources/what-it-really-means-to-multi-thread) | Quality over contact count, and threading your own side too. |
| [sales-velocity-account-level-thinking](account-planning/sales-velocity-account-level-thinking.md) | practitioner_article · P2 | MEDDPICC | unknown | [Opportunity Obsession](https://meddicc.com/resources/your-obsession-with-opportunities-is-costing-you-revenue) | Why deal size and conversion beat opportunity count for an AM. |
| [target-account-tiering](account-planning/target-account-tiering.md) | practitioner_article · P2 | unversioned | 2022-04-15 | [Target Account List](https://winningbydesign.com/resources/blog/how-to-create-a-target-account-list-for-your-enterprise-team/) | Winning by Design's new-logo tiering logic; applying it to an existing book is project inference. |
| [the-stakeholder-meeting](account-planning/the-stakeholder-meeting.md) | practitioner_article · P2 | unversioned | 2022-05-09 | [The Stakeholder Meeting](https://winningbydesign.com/resources/blueprints/the-stakeholder-meeting/) | A three-phase structure that maps onto an expansion-focused EBR (partial, gated). |

---

## Coach playbook documents (`coach/kb/`)

Uploaded to the same knowledge base, so they are ranked under the same scheme.

| Document | Framework | Type · priority | Provenance |
|---|---|---|---|
| [01-taro.md](../../coach/kb/01-taro.md) | successcoaching | canonical · P1 | Restructured from the user-provided SuccessCOACHING playbook; model-note headings are project-authored |
| [02-lifecycle-and-value.md](../../coach/kb/02-lifecycle-and-value.md) | successcoaching | canonical · P1 | Restructured from the user-provided SuccessCOACHING playbook; model-note headings are project-authored |
| [03-health-and-churn.md](../../coach/kb/03-health-and-churn.md) | successcoaching | canonical · P1 | Restructured from the user-provided SuccessCOACHING playbook; model-note headings are project-authored |
| [04-renewals.md](../../coach/kb/04-renewals.md) | successcoaching | canonical · P1 | Restructured from the user-provided SuccessCOACHING playbook; model-note headings are project-authored |
| [05-expansion.md](../../coach/kb/05-expansion.md) | successcoaching | canonical · P1 | Restructured from the user-provided SuccessCOACHING playbook; model-note headings are project-authored |
| [06-onboarding.md](../../coach/kb/06-onboarding.md) | successcoaching | canonical · P1 | Restructured from the user-provided SuccessCOACHING playbook; model-note headings are project-authored |
| [07-cs-operations.md](../../coach/kb/07-cs-operations.md) | successcoaching | canonical · P1 | Restructured from the user-provided SuccessCOACHING playbook; model-note headings are project-authored |
| [08-revenue-operations.md](../../coach/kb/08-revenue-operations.md) | successcoaching | canonical · P1 | Restructured from the user-provided SuccessCOACHING playbook; model-note headings are project-authored |
| [09-spiced.md](../../coach/kb/09-spiced.md) | spiced | secondary · P5 | Project-authored from general knowledge; relabeled and softened in this audit |
| [10-meddpicc.md](../../coach/kb/10-meddpicc.md) | meddpicc | secondary · P5 | Project-authored from general knowledge; relabeled and softened in this audit |
| [11-framework-selection.md](../../coach/kb/11-framework-selection.md) | cross-framework | secondary · P5 | Project-authored from general knowledge; relabeled and softened in this audit |

---

## Conflicts and terminology differences

Nothing below is resolved by declaring a winner. Each item keeps the original
framework's terminology and attribution. Where the authority ranking applies, the
item says which definition takes precedence for that framework.

### Terminology — see `TERMINOLOGY.md` for side-by-side definitions

1. **Critical Event vs. Compelling Event.** Winning by Design's current SPICED page defines a Critical Event as the deadline, milestone or external force that sets when a decision must be made. Its 2022 research paper says a Critical Event has a specific deadline and a *compelling event* does not. MEDDICC defines a **Compelling Event** as explicitly time-bound. The phrase "compelling event" therefore means opposite things in the two sources.
2. **Implicate the Pain vs. Identify Pain.** MEDDICC's current term is Implicate the Pain (Identify → Indicate → Implicate). "Identify Pain" is the original MEDDIC letter. It appears in Winning by Design's 2023 comparison (historical) and was used in `coach/kb/10-meddpicc.md` until this audit relabeled it.
3. **First Impact vs. First Value (within Winning by Design).** The First Impact blueprint (2023) and the Bowtie Proposed Standard use First Impact. The Joint Impact Plan blueprint (2022) and the Customer Success for Impact course use First Value and Full Value. The public sources do not say whether these are synonyms, and the Bowtie paper distinguishes Value (a promise) from Impact (its fulfillment), so they are not treated as interchangeable. SuccessCOACHING's "first value milestone" (M3) is a separate definition.
4. **M3 (within MEDDICC).** The canonical Metrics page defines M3s as M2s validated after go-live — realized value. The MEDDIC for Customer Success webinar describes an M3 as a value goal that moves from proposal to commitment and becomes an M1 once achieved. The canonical definition takes precedence for MEDDPICC.
5. **Value Pyramid levels (within MEDDICC).** Dick Dunkel's executive selling takeaways order it corporate objectives → business strategy → initiatives → execution challenges and capabilities. The Value Pyramid with the Economic Buyer article orders it strategic initiatives → objectives → programs → solution. No public canonical version was found.
6. **SPICED Situation over time.** The 2022 research paper frames Situation as facts establishing ideal-customer-profile fit. The current canonical page frames it as context, constraints, priorities and triggers for change. The canonical page takes precedence.
7. **Bowtie stage names over time.** Current page: Awareness, Education, Selection, Commit, Onboard, Impact, Expansion. The 2019 SaaS Sales Method post (historical) uses Onboarding → First impact → Renewal → Expansion. The Bowtie Proposed Standard's post-sale sub-systems are Onboarding, Adoption and Expansion. Current canonical names take precedence.
8. **Conversion-rate numbering.** Customer Success as a Profit Center (2021) numbers Onboard CR5, Retain CR6, Expand CR7. The Bowtie Proposed Standard numbers Onboarding CR6, Retention CR7, Expansion CR8. Use stage names, not numbers.
9. **"Value" has different senses.** Winning by Design's Value (a promise of impact); MEDDICC's Value driver group (Pain, Metrics, Decision Criteria); SuccessCOACHING's value realization stages V1–V5.
10. **Trading levers.** Winning by Design's trade article names three core levers — price, contract length, payment terms — and separately lists additional assets. `expansion/trade-instead-of-negotiate.md` previously described four levers; corrected in this audit.

### Substantive tensions between claims

1. **Who owns urgency.** A MEDDICC lifecycle article says customers don't control deal timelines — sellers do. Winning by Design's How to Diagnose says urgency should come from a milestone the buyer identifies, and MEDDICC's own Compelling Event article rejects manufactured urgency. One reading — the seller drives the process while the customer owns the date — is project inference, not stated by either source.
2. **Expiration dates.** Winning by Design's trade article recommends an expiration date with consequences on negotiated terms. MEDDICC lists "this price is only good until end of quarter" as manufactured urgency. They may address different moments (terms after a decision vs. a reason to decide), but that too is inference.
3. **Economic Buyer by title.** Nick Reva says the Economic Buyer is now the CFO, and Pim Roelofsen recommends treating the CFO as the Economic Buyer by default. MEDDICC's qualification article warns against qualifying by title, and the canonical definition rests on authority, not job title. The canonical definition takes precedence; the CFO heuristics are practitioner views.
4. **Cross-sell ownership.** Winning by Design's Bowtie Proposed Standard says a cross-sell should never be handled by a CSM. MEDDICC's customer-success articles have CS managers using MEDDPICC to identify expansion. Identification vs. ownership may be the distinction.
5. **Which framework contains the other.** Winning by Design (2023, historical) says all MEDDIC elements are found within SPICED, and positions MEDDIC for sellers with 20+ years' experience. MEDDICC (2026) says SPICED lacks Champion, Paper Process and Competition equivalents. Both are vendor-biased.
6. **When onboarding is complete.** Winning by Design: when First Impact is achieved and acknowledged. SuccessCOACHING: at M5 — CSM handoff complete, success plan active, time-to-value achieved. Different frameworks; neither overrides the other.

### Source-stated statistics (attributed, not independently verified)

| Claim | Source |
|---|---|
| 60% of deals are lost to inertia | MEDDICC, canonical Decision Process page |
| 72–93% of customer lifetime value comes after the initial deal | Winning by Design, Emotional vs. Rational Impact (2021) and The SaaS Sales Method (2019) |
| A 5% retention increase yields an estimated 25–95% revenue increase | Reference cited in Winning by Design, CS as a Profit Center (2021) |
| A 10% discount leaves half the revenue after seven years | Winning by Design, How to Trade Instead of Negotiate (2021) |
| About 7 stakeholders in mid-market evaluations, about 14 in enterprise, around 22 with a board | MEDDICC, Personalize Metrics; How to Close Deals Without Being in the Room |
| Top performers who work through Champions are about 4x more successful | Richard Dufty, MEDDICC downturn takeaways |
| Executives are about 3x more likely to engage through multichannel outreach | Dick Dunkel, MEDDICC takeaways |
| 59% of sales leaders say agreement and signing take too long | Survey cited in MEDDICC's Paper Process article |
| Forecast accuracy above 98% after implementation | Vendor-reported MEDDICC case study |

### Unsupported absolute claims

**Source-stated absolutes, kept with attribution:** "No Champion, no deal"
(MEDDICC); a cross-sell "should never" be handled by a CSM (Winning by Design);
"MEDDICC is binary" (Andy Whyte); "Nobody regrets qualifying out" (MEDDICC article
title); the Economic Buyer "is now the CFO" (Nick Reva); sellers, not customers,
control timelines (MEDDICC).

**Project-authored absolutes softened in this audit:**

- `coach/kb/10-meddpicc.md`: "most commonly skipped element"; "Economic Buyers change more often than champions"; Paper Process as where renewals slip "most often"; status quo as "the most common competitor at renewal"; direct competitors as "usually the least likely"; the Known/Partial/Unknown scoring and three-Unknowns rule, now labeled model heuristics (MEDDICC's own practice is 1–10 confidence scoring)
- `coach/kb/09-spiced.md`: Situation "decays faster than any other element"; a missing Critical Event as "the single most common reason" expansion slips; "Run the five in order," which contradicted Winning by Design's point that Impact and Critical Events surface out of sequence
- `coach/kb/02`, `03`, `04`, `05`, `06`, `08`, `11`: superlatives such as "most often," "most common," "matters most," "earliest," and "will renew on goodwill or not at all"
- `account-planning/target-account-tiering.md` and `spiced/operating-model-for-recurring-revenue.md`: "the only" and "most detailed" claims now scoped to what was found during retrieval

### Duplicate and overlapping concepts

| Concept | Documents | Handling |
|---|---|---|
| Economic Buyer identification | `meddpicc/economic-buyer`, `economic-buyer-qualifying`, `economic-buyer-vs-champion` | Kept: canonical markers, the Budget Holder distinction, and title heuristics are distinct angles |
| Decision Criteria dimensions | `meddpicc/decision-criteria`, `decision-criteria-three-dimensional` | Kept: the second adds examples and qualification use |
| M1/M2/M3 | `meddpicc/metrics`, `metrics-solution-to-inertia`, `account-management/meddic-for-customer-success-webinar`, `meddpicc-for-customer-success`, `customer-success-metrics-harvesting-vs-mining` | Kept; definitional variance noted above |
| Inertia as a competitor | `meddpicc/competition`, `competition-the-wrong-competition`, `metrics-solution-to-inertia`, `decision-process` | Consistent; kept |
| Deal review practice | `meddpicc/deal-reviews`, `deal-reviews-lessons-from-implementation`, `failure-modes` | Kept: cadence, adoption lessons, and failure modes |
| Bowtie | `account-management/bowtie-model`, `expansion/bowtie-expansion-types`, `account-management/the-saas-sales-method` | Kept; stage-name history noted above |
| SPICED and MEDDPICC definitions | `coach/kb/09-spiced`, `10-meddpicc`, `11-framework-selection` vs. the sourced corpus | Kept at `secondary` / P5 as project reasoning, per earlier direction |

### Documents with unclear or limited provenance

1. **Three PDFs reached by direct link:** `spiced/operating-model-for-recurring-revenue`, `account-management/customer-success-as-profit-center`, `expansion/bowtie-expansion-types`. No license terms are stated, and the pages linking to them were not identified. Winning by Design separately offers a related "Bowtie Standard" behind a form, and how the Proposed Standard relates to it is unclear. **Confirm permission, or remove these before any external use.**
2. **Public summaries of gated assets** (`paraphrased_notes_partial`): the SPICED blueprint, SPICED Across the Customer Journey, How to Diagnose, CS Operating Model, First Impact, Joint Impact Plan, Mapping Relationships, The Stakeholder Meeting.
3. **Outlines only** (`paraphrased_notes_outline`): Account Management for Growth, Customer Success for Impact, and the playbooks page.
4. **Merged documents with mixed source types:** `meddpicc/champion` (a canonical page plus a practitioner article) and `account-management/bowtie-model` (a canonical page plus a research landing page) are ranked by their primary source.
5. **Unknown publication dates** for most MEDDICC documents (see *Publication dates*).
6. **`coach/kb/01`–`08`:** restructured from the user-provided SuccessCOACHING playbook with model elaboration. Ownership and license of that playbook are not recorded.
7. **Verification coverage.** This audit spot-checked 7 documents against the live sources. Four were accurate (`meddpicc/compelling-event`, `meddpicc/champion-closing-without-being-in-the-room`, `meddpicc/pain-are-you-really-implicating`, `meddpicc/decision-process`). Three had errors, now corrected: `account-planning/target-account-tiering` attributed a claim about existing customers that the article does not make; `expansion/trade-instead-of-negotiate` described four levers where the article names three plus additional assets; `spiced/comparison-meddic-and-spiced-wbd-view` paraphrased the seller-experience comparison imprecisely (the article says 5+ years for SPICED, 20+ for MEDDIC). **The other documents have not been re-verified line by line.**

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

