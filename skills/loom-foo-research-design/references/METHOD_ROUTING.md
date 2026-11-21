# Method Routing


Choose by the claim and discriminating observation, not by familiarity with a method.


This guide is intentionally lightweight. It routes to method families; it does not replace specialist methodology.


## Direct source verification / inspection
Use when the target is a current externally observable fact and a primary/authoritative source can establish it.


Examples:
- API capability;
- version/support status;
- documented constraint;
- current configuration.


Escalate to a live probe when documentation cannot establish runtime behavior.


## Capability probe / spike
Use when the main question is whether something can work at all under an exact environment.


Good for:
- browser/device capability;
- API behavior;
- implementation feasibility;
- integration viability.


Keep scope narrow. A successful probe establishes feasibility under the tested conditions, not production fitness or user value.


## Measurement
Use when the uncertainty is quantitative and the property can be directly observed.


Examples:
- latency;
- memory/cost;
- throughput;
- physical output;
- error rate.


Check measurement resolution, drift, calibration, warm-up/cache effects, and sampling window when material.


## Benchmark / controlled comparison
Use when comparing alternatives on a defined case distribution.


Need when material:
- fair baseline;
- exact treatment difference;
- same cases across arms;
- frozen environment;
- repetitions for stochastic systems;
- outcome/scorer validity.


A benchmark licenses claims only about its represented population/conditions.


## Qualitative user research
Use when the uncertainty is about meaning, comprehension, workflow, motivation, mental model, or failure mechanism that numeric product telemetry cannot identify alone.


Possible methods:
- moderated task observation;
- interview;
- think-aloud;
- contextual inquiry;
- concept/prototype test.


Do not convert a few qualitative sessions into prevalence estimates.


## Observational analysis
Use when real-world behavior/data can answer descriptive or associational questions without manipulating treatment.


Be explicit about:
- selection bias;
- confounding;
- missing data;
- measurement process;
- population scope.


Do not license causal claims from association alone.


## Causal experiment
Use when the decision specifically depends on the effect of an intervention and credible causal attribution is required.


This may require:
- randomization;
- counterfactual comparator;
- blocking/stratification;
- correct unit of assignment/analysis;
- power/sample-size expertise;
- sequential-analysis controls.


Use `NEED_SPECIALIST_METHOD` if these details materially affect validity and appropriate expertise is unavailable.


## Simulation
Use when real-world execution is costly, risky, slow, or unavailable and a model can discriminate alternatives.


The simulation itself becomes part of the measurement instrument. State its calibration/assumption limits and do not treat simulated validity as real-world validation.


## Reproduction / replication
Use **reproduction** to test whether the same data/code/method yields a consistent result.


Use **replication** to test whether a new study/new data supports the same conclusion.


Do not describe either as generalization unless the sampled contexts support that claim.


## Robustness / variability test
Use when the question is whether a result survives allowed variation.


Examples:
- prompt paraphrases;
- run-to-run randomness;
- environment differences;
- alternate reasonable analysis choices;
- device/runtime variants.


Define which variations are supposed to preserve the construct. Do not average away the spread when the spread is the property of interest.


## Specialist method
Return `NEED_SPECIALIST_METHOD` when correct design depends materially on expertise such as:
- formal power/sample-size calculation;
- complex causal inference;
- advanced DOE;
- clinical/regulated protocol;
- safety/security adversarial testing;
- survey sampling/weighting;
- psychometrics;
- scorer/judge validation;
- domain-specific measurement science.


The general skill should describe the evidence question and required specialist output, not improvise a weak method.