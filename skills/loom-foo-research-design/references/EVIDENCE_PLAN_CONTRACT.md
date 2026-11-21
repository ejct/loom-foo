# Evidence Plan Contract


An Evidence Plan is a pre-evidence decision artifact. It specifies what evidence is worth acquiring, why it can discriminate the live alternatives, and how the result will be interpreted without overclaiming.


The contract is semantic, not a fixed output template. Omit fields that are immaterial to a small case.


## Core dimensions


### 1. Decision / intended use
State the concrete decision, transition, or claim the evidence can affect.


Bad:
- "learn more about the problem"


Better:
- "decide whether architecture A may rely on capability X"
- "decide whether candidate B warrants another implementation iteration"
- "decide whether a UX issue is caused by discoverability rather than task complexity"


If no plausible result can change anything material, use `NO_NEW_EVIDENCE_NEEDED`.


### 2. Current uncertainty
State the smallest material unknown.


Examples:
- capability unknown;
- magnitude unknown;
- causal mechanism uncertain;
- result may be unstable;
- user value unknown;
- measurement/oracle may be invalid;
- generality beyond the observed context unknown.


Do not substitute the whole project problem for the uncertainty.


### 3. Live alternatives / intended claim
State only alternatives that genuinely compete.


A hypothesis is useful when it makes a discriminating prediction. It is not mandatory for descriptive/source-verification tasks.


### 4. Evidence-value gate
Record the qualitative judgment:
- why new evidence can change the decision;
- why current evidence is insufficient;
- whether a cheaper check exists;
- why the expected information justifies the cost/risk.


A numeric score is not required.


### 5. Identifiability / discriminating observation
Name the observation that would separate the alternatives.


If the same likely result is compatible with every live explanation, the plan is not discriminating enough.


### 6. Method family
Choose the narrowest credible method. Method names do not create validity by themselves.


### 7. Subject / population / environment
Bind the claim to the actual thing being observed.


When material, include:
- exact version / candidate / commit / model;
- sample/case population and weighting;
- environment/runtime;
- treatment implementation;
- time window.


### 8. Comparator / baseline / controls
Required only when the intended claim depends on comparison or causal attribution.


A baseline should be fair enough that beating it means something.


### 9. Measures / oracles
For each consequential signal, make clear:
- what it is evidence of;
- what it can miss;
- likely shortcut/gaming path;
- whether measurement noise/stability/resolution matters.


Do not use process-compliance evidence as a substitute for outcome evidence unless the process itself is the target property.


### 10. Validity hazards
Include only hazards capable of changing the interpretation.


Typical classes:
- confounding;
- selection/sampling bias;
- contamination/leakage;
- instrumentation drift;
- unstable environment;
- treatment not actually delivered;
- broken cases;
- scorer/proxy gaming;
- evaluator dependence;
- under-elicitation;
- optional stopping / outcome switching.


### 11. Interpretation contract
Where practical before execution, specify:
- `supports` — what result strengthens the intended claim;
- `weakens/refutes` — what result argues against it;
- `inconclusive` — what result fails to discriminate;
- `unsupported_claims` — claims this plan never licenses.


For exploratory work, the interpretation contract may instead state discovery outputs and the required confirmatory follow-up.


### 12. Stop / adaptation rule
State when to:
- stop;
- repeat;
- expand;
- redesign;
- escalate to a stronger method.


Avoid fixed run counts when the exact count is not decision-relevant. When stochasticity matters, define repetitions or sequential stopping sufficient for the intended claim.


### 13. Execution handoff
State the natural executor and minimum inputs it needs.


Do not encode unnecessary runtime choreography here. A separate task-design workflow can compile an executable task later.


### 14. Claim limits
End with the narrowest defensible claim surface.


Examples:
- observed capability in environment E, not all environments;
- requirement verification, not user validation;
- association, not causal effect;
- stable under tested variants, not universally robust;
- can perform under elicitation regime R, not typical deployment behavior.


## Compact fast-path example


```text
status: EVIDENCE_PLAN_READY
decision: Can architecture rely on API capability X in the current supported version?
uncertainty: Current docs are ambiguous about X.
method: Check current primary docs; if ambiguous, run one live capability probe against the exact version.
supports: X is documented or directly observed under the exact current version.
inconclusive: access/runtime prevents the probe and docs remain ambiguous.
stop: once current capability is established.
claim_limits: says nothing about throughput, reliability at scale, or future versions.
execution: direct verification / small probe.
```