# Adaptation and Failures

Status: candidate reference for `evidence-acquisition v0.1.0-candidate`.

This reference governs retries, substitutions, stale plans, partial acquisition and escalation.

## 1. Operational recovery vs method change

Recover autonomously from ordinary execution friction when the evidence semantics remain the same.

Examples normally safe when authorized:

- retry after transient timeout;
- use another HTTP/browser/search transport to fetch the same source;
- use another parser that returns the same defined field;
- resolve a moved file/repository path to the same exact subject;
- resume pagination from a checkpoint;
- write the same captured bytes to a different local storage format.

A change is method-level when it can materially alter the evidence population, measurement, comparison, fidelity or interpretation.

## 2. Material adaptation gate

Return `PLAN_REVISION_REQUIRED` when continuation requires materially changing:

- subject or candidate identity;
- population/case set/sample;
- source universe or selection rule;
- inclusion/exclusion rule;
- comparator/control;
- intervention/treatment;
- metric/oracle;
- direct/proxy evidence class;
- environment required by the claim;
- confirmatory stopping rule after outcomes are visible;
- analysis/extraction rule when it changes what counts as evidence.

Do not bury these changes as "tool substitutions."

## 3. Stale plan handling

A plan can remain methodologically valid while its locator is stale.

### Execution-binding repair
Allowed when:
- the same exact semantic subject can be identified;
- only the locator/path/transport changed;
- evidence scope/meaning is preserved.

### Plan-level drift
Escalate when:
- version/candidate changed;
- source universe materially changed;
- expected interface/property no longer exists;
- comparator changed;
- time window no longer matches;
- acquisition would answer a different question.

## 4. Retry semantics

A retry is a new attempt when attempt identity matters.

Record retries when they affect:

- rate-limit interpretation;
- reproducibility;
- cost;
- completeness;
- stochastic behavior;
- error diagnosis;
- stop/adaptation rules.

Do not log every low-value internal retry in a trivial check.

## 5. Failure distinctions

Preserve at least the semantic difference between:

- complete successful result;
- complete zero;
- partial result;
- access/permission failure;
- rate limit;
- timeout;
- transport/tool failure;
- parser/transformation failure;
- abort/cancel;
- not run;
- unknown.

Domain-specific workflows may use richer states.

## 6. Partial acquisition

A partial package is legitimate when:

- some evidence is useful and attributable;
- the exact missing plan obligations are visible;
- downstream review can avoid assuming completeness.

Do not stretch the plan or lower the completeness criterion merely to return READY.

## 7. Authority failures

If a plan requires an action that is not authorized:

- do not execute it;
- do not replace it with weaker evidence unless the plan permits that substitution;
- identify the exact blocked item;
- continue independent authorized acquisition when useful;
- return PARTIAL or BLOCKED with the authority gap visible.

A runtime approval prompt does not replace project/user authority for a stronger external transition.

## 8. Capability failures

If the current runtime cannot perform a planned step:

1. check reasonable lower-friction authorized alternatives;
2. determine whether an equivalent runtime/tool can satisfy the same evidence property;
3. if yes, switch and record it when material;
4. if not, identify the natural/specialist executor or required capability;
5. return PARTIAL/BLOCKED rather than inventing evidence.

## 9. Conflicting or surprising results

Do not redesign acquisition simply because results are surprising or unfavorable.

Complete the plan unless:
- a stop rule triggers;
- continuing is unsafe/unauthorized;
- the result exposes a plan-invalidating defect;
- the plan explicitly allows adaptive acquisition.

Interpretation belongs downstream.

## 10. Cost and budget boundaries

Respect explicit spend/time/query/runtime budgets.

A budget limit is not permission to silently change method quality.

When a budget is exhausted:
- preserve completed evidence;
- mark remaining obligations;
- state whether the result is PARTIAL or the plan-defined stop was legitimately reached.

## 11. External/human execution

When a natural executor performs a step:

- preserve the requested procedure/contract;
- capture the returned artifact/result;
- record executor/source identity only to the level needed for provenance;
- preserve deviations reported by that executor;
- do not claim direct machine observation if the evidence is human-reported.

## 12. Stop rule

Stop acquisition when one of these holds:

- all required acquisition obligations are resolved;
- a plan-defined stop rule fires;
- material plan revision is required;
- an irreducible capability/authority/safety boundary blocks the remaining plan;
- the user/project explicitly stops the run.

Do not continue exploratory source collection after the controlling acquisition contract has ended.
