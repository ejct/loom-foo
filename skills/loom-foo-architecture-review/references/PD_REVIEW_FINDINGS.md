# architecture-review — detailed conditional method (PD_REVIEW_FINDINGS.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 11. Findings

For each material finding maintain:
- `id`;
- `severity`: CRITICAL | MAJOR | MODERATE | MINOR;
- `confidence`: HIGH | MEDIUM | LOW;
- `category`;
- `scope`;
- `claim`;
- `evidence`;
- `affected_driver_or_scenario`;
- `consequence`;
- `failure_or_cost_path`;
- `resolution_criterion`;
- `validation_method`;
- `sensitivity`;
- `tradeoff`;
- `fitness_function_candidate`;
- `status`: OPEN | RESOLVED | REJECTED | ACCEPTED_RISK.

Equivalent findings keep stable identity.

Severity is consequence. Confidence is evidence strength. Never collapse them into a score.
## 12. Findings are not redesign commands

Prefer:
"Canonical ownership is ambiguous between X and Y; recovery can produce conflicting state. Resolution requires one canonical owner or explicit consistency semantics."

Avoid:
"Add StateCoordinator service."

A review may mention plausible directions to clarify a trade-off, but does not own redesign.

The **resolution criterion is normative; implementation suggestions are illustrative**. In review-only mode, do not emit a coherent replacement architecture. If a concrete alternative is useful for explaining a finding, label it as an example and keep the finding valid even if that example is rejected.
## 13. Non-risks

Record material `NON_RISK` conclusions when evidence supports them.

Review quality is not measured by criticism count.
## 14. Sensitivity and trade-offs

A sensitivity point is a decision/parameter whose small change materially changes a quality outcome.

A trade-off point improves one driver while degrading another.

Surface these when they govern evolution or candidate selection.
## 15. Implementation conformance

In IMPLEMENTATION_REVIEW distinguish:
- accepted design;
- observed behavior/structure;
- known temporary deviations;
- real architecture drift;
- stale docs.

Do not call every discrepancy a violation.

When a property can be executable, propose a fitness-function candidate.
## 16. Empirical boundary

If a conclusion depends on measurement or real behavior—throughput, latency, contention, failover time, model/provider behavior—do not invent certainty.

Return:
- hypothesis;
- smallest probe;
- measurement;
- pass/fail or discriminating boundary;
- architecture consequence.

Use `VALIDATION_REQUIRED` when needed to close review.
## 17. Reviewer independence

Use a separate context/agent/model when genuinely available and proportionate.

If the same context performs review, call it a **fresh adversarial self-review**, not independent review.

Never fabricate independence.
