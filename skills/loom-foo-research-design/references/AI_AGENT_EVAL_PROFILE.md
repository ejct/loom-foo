# AI / Agent Evaluation Profile


Use this profile when the subject includes an LLM, agent, tool-using system, or evaluation harness and system configuration can materially affect observed behavior.


## Subject identity


When material, bind:
- exact model/system identity;
- model/provider version or dated endpoint;
- reasoning/temperature/configuration;
- prompt/system instructions;
- harness/scaffold;
- tool manifest and permissions;
- memory/context/retrieval setup;
- environment/sandbox;
- safeguards;
- turn/token/time/cost budget;
- retry/attempt policy.


Do not report a model-level claim when the experiment actually measures a model+harness+tools+context system.


## Cases / population


State:
- case/task source;
- inclusion/exclusion rule;
- weighting if any;
- whether cases are historical, synthetic, production-derived, public benchmark, or fresh holdout;
- contamination risk.


A fresh holdout is especially useful when the skill/prompt/system was tuned on historical cases.


## Outcome vs trajectory


Distinguish:
- final outcome quality;
- intermediate tool/action correctness;
- trajectory properties;
- cost/latency;
- policy/authority behavior.


Do not treat an attractive rationale or self-report as evidence that the underlying behavior occurred.


## Stochasticity


If randomness can alter the decision:
- repeat conditions;
- preserve per-run results;
- report spread/worst-case or task-level success probability appropriate to the claim;
- avoid selecting only the best run.


No fixed K is universal. Choose enough repetition to support the intended distinction.


## Capability vs reliability


Capability question:
"Can the system do X under a credible elicitation regime?"


Reliability question:
"Does the system do X consistently under deployment-relevant variation?"


These require different summaries. Peak elicitation supports a bounded capability floor; it does not establish typical reliability.


## Harness hazards


Check when material:
- treatment not actually implemented in every arm;
- provider/serving path changes;
- cache/warm-up/rate-limit effects;
- tool availability differences;
- context leakage between conditions;
- hidden retries;
- prompt contamination;
- broken tasks or impossible graders;
- evaluator awareness;
- reward/scorer hacking;
- under-elicitation / inadequate scaffold;
- benchmark contamination.


## Scorer / judge boundary


For consequential gating, the scorer itself is a measurement instrument.


Ask:
- Is it validated against a stronger reference where necessary?
- What dangerous false acceptances does it have?
- Can polish/length/confidence/gameable tokens move the score without better behavior?
- Does scorer version remain fixed across compared runs?


If scorer validity is material and unknown, surface the gap or route to specialist validation.


## Interpretation limits


Examples:
- "System S with harness H solved 78% of this task distribution" is narrower and usually safer than "Model M has 78% capability."
- One prompt format does not establish robustness.
- Best-of-N does not estimate ordinary deployment behavior.
- Benchmark success does not establish user value unless the benchmark construct was validated against real outcomes.