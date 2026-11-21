# Support and Uncertainty

Status: candidate reference for `evidence-review v0.1.0-candidate`.

## Support is scoped

Avoid claims like “the evidence proves X” without the relevant scope.

Prefer:
- supported for candidate/version V under environment E;
- contradicted in the tested population/window;
- mixed across environments A/B;
- insufficient for a general claim beyond the observed cases.

## Not-supported vs contradicted

`INSUFFICIENT` means the current evidence cannot establish the claim to the required strength.

`CONTRADICTED_WITHIN_SCOPE` requires material evidence inconsistent with the claim in the tested scope.

Absence of support is not itself counterevidence.

## Non-discrimination

Use `NON_DISCRIMINATING` when the evidence is valid but cannot distinguish the live alternatives strongly enough.

Examples:
- test resolution too weak to distinguish the required difference;
- both alternatives predict the observed result;
- null result has confidence/precision interval too wide for the meaningful threshold;
- only a surrogate was measured while the alternatives differ on the target property.

## Evidence of absence/equivalence

A null/zero result can support absence/equivalence only when:
- the acquisition completed correctly;
- the design/measurement could detect a meaningful alternative;
- uncertainty is sufficiently bounded;
- the scoped absence/equivalence threshold is defined when needed;
- no material validity failure defeats the inference.

Otherwise do not convert zero into proof of absence.

## Contradictions

Do not average contradictions away automatically.

First determine whether evidence differs by:
- population;
- environment;
- version/time;
- method;
- measurement semantics;
- source lineage.

If no defensible reconciliation exists, use `MIXED` and preserve the unresolved condition.

## Confidence discipline

Qualitative confidence may be useful when it explains assessment robustness.

Confidence should fall when material uncertainty comes from:
- incomplete acquisition;
- weak measurement validity;
- imprecision;
- indirectness;
- correlated evidence presented as corroboration;
- unexplained contradiction;
- temporal mismatch;
- scope extrapolation.

Do not lower confidence merely because the result is unfavorable.

## Unknown discipline

Prefer a specific unknown over a generic caveat.

Good:
> The package establishes behavior on macOS 26.1 / Chromium 153 only; behavior on Windows is untested.

Weak:
> Results may vary.

## Specialist methods

When a claim depends on a specialist statistical/scientific evidentiary standard, do not improvise a generic threshold. Use the controlling specialist method or return the corresponding context/specialist boundary.
