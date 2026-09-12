# CS Operations

## Capacity

```
Max supportable ARR = (number of CSMs) × (ARR per CSM target)
```

Alert thresholds on headroom:

| Level | Headroom | Action |
|---|---|---|
| **Critical** | Below 0% — over capacity | Immediate coverage triage |
| **High** | 0–10% | Flag for hiring now |
| **Medium** | 10–25% | Limited headroom; plan ahead |
| **Healthy** | Above 25% | No action |

Capacity problems present as quality problems. Before diagnosing a CSM
performance issue, check whether the book size makes the expected motion
impossible.

---

## Segmentation

Your coverage model determines which accounts get high-touch, tech-touch, or
pooled coverage.

**Segment drift** — an account growing above or below its segment threshold —
requires proactive reassignment planning. Drift handled late means either an
enterprise account receiving pooled coverage, or a CSM spending high-touch hours
on an account that no longer warrants it.

Review drift on a set cadence rather than discovering it at renewal.

---

## Data quality

**Authority by system:**

- **CRM** is authoritative for ARR, renewal dates, and account ownership
- **CS platform** is authoritative for health scores, success plan status, and CTAs
- **Product analytics** is authoritative for feature usage, seat activation, and
  adoption metrics

**Conflicts between systems must be resolved at the source, not papered over in
analysis.** A report that reconciles two disagreeing systems hides a data problem
that will resurface in every future report.

When numbers disagree, the discrepancy is the finding. Say which system you are
quoting and when it was last verified.
