# Research Method — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 6. Choose the narrowest credible method family

Use `references/METHOD_ROUTING.md` when the method is not obvious.

Possible families include:
- direct source verification / inspection;
- capability probe / spike;
- measurement;
- benchmark / controlled comparison;
- simulation;
- qualitative user research;
- observational analysis;
- causal experiment;
- reproduction / replication;
- robustness / variability test;
- specialist method.

These are routing aids, not a canonical ontology.

Do not escalate to a controlled experiment when source inspection, one real-environment probe, or a small observational check can answer the actual question. When the question can be settled by a check already available to the main task owner, give that direct check and return control; this skill does not need to produce a formal Evidence Plan or interrupt authorized implementation.
## 7. Define the subject and scope of the claim

Specify only dimensions that can materially affect interpretation:
- exact subject / version / candidate;
- population or case distribution;
- environment;
- comparator / baseline;
- relevant controls;
- treatment/intervention when applicable.

Do not let a narrow sample silently license a broad population claim.

For AI/agent evaluations, read `references/AI_AGENT_EVAL_PROFILE.md` when model/harness/tool/context differences could change behavior.
## 8. Validate the measurement strategy before running

Ask:
- Does the metric, oracle, scorer, observer, or proxy actually measure the target property?
- What does it systematically miss?
- Can it be improved without improving the real outcome?
- Can the subject game it?
- Is its precision, stability, and resolution sufficient for the intended distinction?
- Does the measurement instrument itself require validation?

Use `references/VALIDITY_CHECKS.md` for consequential plans.

If the measurement strategy is not fit for the intended claim, surface the instrumentation/oracle gap instead of pretending the study is ready.
## 9. Add controls only when the claim requires them

Comparative and causal claims may require stronger controls than feasibility or descriptive claims.

When material, consider:
- fair baseline / comparator;
- randomization;
- blocking / stratification;
- correct unit of replication;
- repeated runs for stochastic behavior;
- negative controls;
- blinding or independent observation;
- fixed environment / treatment implementation;
- contamination and leakage checks.

Do not cargo-cult these mechanisms into low-risk direct checks.
## 10. Separate exploratory from confirmatory work

Exploratory work is legitimate.

If the goal is discovery:
- label it `EXPLORATORY`;
- allow findings to generate new hypotheses;
- do not present post-hoc patterns as pre-specified confirmation.

If the plan is intended to support a consequential confirmatory claim:
- pre-state the primary interpretation criteria when practical;
- fix material exclusions, stopping rules, comparison setup, and analysis choices before seeing the outcome;
- preserve any later adaptations explicitly.

Formal preregistration is optional unless the domain, risk, or external process requires it.
