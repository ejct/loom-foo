# Proposal Refinement — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 8. Challenge consequential claims when warranted

When consequential claims affect a material decision, read [claim challenge](./CONSEQUENTIAL_CLAIM_CHALLENGE.md). Routine proposals do not require audit or benchmark campaigns.
## 9. Record findings

When a separate consequential audit needs traceable resolution, give material findings a stable identity with:

- `id`;
- `severity`;
- `dimension`;
- `claim`;
- `evidence`;
- `consequence`;
- `resolution_criterion`;
- `introduced_in`;
- `status`;
- `resolved_in` when applicable;
- `disposition`.

Statuses are `OPEN`, `RESOLVED`, `REJECTED`, or `ACCEPTED_RISK`.

Equivalent findings expressed with different wording retain the same identity. Do not inflate novelty by paraphrasing an existing issue.

Severity means consequence:

- **CRITICAL** — invalidates the proposal, creates unacceptable risk, or prevents the primary objective;
- **MAJOR** — proposal remains viable but has a material architectural, product, operational, evidentiary, or integration weakness;
- **MODERATE** — bounded but meaningful weakness worth addressing when proportionate;
- **MINOR** — polish, documentation quality, or low-risk refinement.
## 10. Adjudicate before revising

Treat audit findings as hypotheses, not commands.

For each material finding:

1. decide whether it is valid;
2. if valid, fix the underlying problem;
3. if partially valid, address the real weakness without mechanically adopting the auditor's suggested implementation;
4. if invalid, reject it with a reason;
5. if inherent and acceptable, mark it `ACCEPTED_RISK` and keep it visible;
6. check whether the response introduces new assumptions, dependencies, complexity, or regressions.

Do not silently leave a CRITICAL finding unresolved.

A MAJOR finding that cannot be resolved through reasoning should normally lead to `BLOCKED` or `VALIDATION_REQUIRED`, depending on whether a decision/input or empirical evidence is missing.

If an early audit repeatedly finds a defect that the Proposal Quality Contract was supposed to prevent, treat that as a construction failure as well as a proposal finding. Repair the proposal first; consider strengthening the construction rule only after recurrence across real cases rather than mutating the skill ad hoc during one run.
## 11. Produce a coherent revision

Create the next proposal version as a coherent artifact rather than a patch list.

If another consequential review is warranted, check previously material CRITICAL, MAJOR and design-changing MODERATE findings for regression.

A finding is `RESOLVED` only when its resolution criterion actually holds. If an earlier defect returns in another form, reopen its existing identity.
## 12. Repeat only on new material evidence

If material changes justify another review, check for genuinely new defects and relevant regressions, then stop when the next pass has low expected information value. No fixed audit-pass count is required; never stop because a pass quota was met or continue to fill one.

### Record material proposal review passes for Answer Receipt

For actual repeated proposal review, correction or verification, carry a small internal sequence of **observed semantic stages** (`PROPOSE1 → REVIEW1 → REVISE1 → REVIEW2 ...`) and their material outcomes. Bind a proposal revision to an actual identifiable version only when one exists; an in-context edit is not a saved document. Distinguish self-review from a genuinely separate reviewer. Render the sequence in the final Answer Receipt's `Process Trail` when material, without making additional review passes mandatory or replacing the primary proposal with an audit transcript. A later stage may summarize a finding as resolved only after the affected criterion was actually rechecked.
