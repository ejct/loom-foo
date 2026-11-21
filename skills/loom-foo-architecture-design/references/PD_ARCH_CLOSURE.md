# Arch Closure — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 18. Terminal states

Choose one:

### `CONVERGED`
No unresolved Critical/Major architecture findings; critical scenarios have coherent responses; invariants are compatible; material decisions have rationale; assumptions are explicit; fixes survive regression; no material framing challenge remains; empirical unknowns are bounded/handed to validation; another pass has low expected information value.

For consequential designs, two stable fresh passes are a strong default to dogfood, not an immutable law.

### `VALIDATION_REQUIRED`
A material design choice depends on empirical evidence.

### `BLOCKED`
A missing constraint, authority decision, dependency, or required evidence prevents defensible design.

### `NON_CONVERGING`
Repeated revisions expose material contradictions; reopen framing/drivers instead of patching indefinitely.
## 19. Fitness-function candidates

When a stable architecture property can be continuously checked, suggest a candidate:
- dependency/architecture test;
- contract/schema test;
- invariant/property test;
- runtime metric/SLO;
- static/policy check;
- failure-injection regression.

Do not implement without authorization.
## 20. Output

Return the latest architecture as the primary artifact.

Add compact Design Closure:
- mode;
- status;
- selected candidate/revision;
- alternatives materially considered;
- important trade-offs;
- material findings resolved;
- accepted risks;
- remaining uncertainties;
- validation step if needed;
- fitness-function candidates;
- stop reason.

Do not dump the full intermediate design-space transcript unless asked.
