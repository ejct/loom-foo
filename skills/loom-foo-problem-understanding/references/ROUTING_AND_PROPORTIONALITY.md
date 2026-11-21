# Routing and Proportionality

## Primary-output precedence

Problem Understanding is not a universal first stage.

If a stronger primary-output owner can already operate safely, route directly.

| Situation | Preferred owner |
| --- | --- |
| decision-ready project delta requested | proposal-refinement |
| new/changed architecture requested | architecture-design |
| frozen architecture evaluation | architecture-review |
| bounded empirical uncertainty | research-design |
| acquired evidence body | evidence-review |
| bounded alternatives/action synthesis | decision-reconciliation |
| specification obligations | specification-design |
| bounded implementation/change review | change-review |
| exact factual/source uncertainty | direct verification/retrieval |

## When explicit output is still not enough

A user may ask for a proposal or research plan while the framing is materially unstable.

Use Problem Understanding only if the ambiguity would otherwise cause the downstream owner to optimize the wrong question.

Then hand off as soon as the blocking ambiguity is resolved.

## Cheap-check rule

Prefer a direct check when one accessible observation can discriminate the live alternatives.

Examples:

- current version/API behavior;
- whether a file/setting exists;
- exact repository state;
- a deterministic calculation;
- one bounded runtime probe.

Do not build an Understanding Model around a fact that can simply be checked.

## Reversible-probe rule

If a small safe experiment is cheaper and more informative than extended framing analysis, identify the probe and route/execute under the appropriate owner/authority.

## Ordinary explanation exclusion

Do not activate merely because a user says "help me understand X."

If X is a stable, well-formed concept and the task is ordinary explanation/teaching, answer normally.

Activation requires material framing ambiguity that affects the conclusion or next action.
