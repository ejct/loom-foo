# Acquisition Fidelity

Status: candidate reference for `evidence-acquisition v0.1.0-candidate`.

Use these rules to preserve the distinction between the evidence the plan asked for and the evidence the executor happened to obtain.

## 1. Fidelity dimensions

Check only dimensions material to the planned claim:

- subject identity;
- source identity;
- version/revision;
- time/recency/window;
- environment;
- population/case set;
- comparator/control;
- measurement/oracle;
- direct vs proxy evidence;
- selection/exclusion rule;
- acquisition completeness;
- transformation lineage.

A change in a material dimension can turn a convenient substitute into different evidence.

## 2. Plan item mapping

Each material evidence item should be traceable to the plan obligation it satisfies.

Do not require one-to-one mapping when one acquisition legitimately satisfies several obligations or one obligation requires multiple artifacts.

The mapping exists to prevent:

- accidental omission;
- unsupported substitution;
- duplicate counting;
- post-hoc redefinition of what was collected.

## 3. Direct evidence vs proxy

If the plan asks for direct evidence, do not silently replace it with:

- documentation;
- model memory;
- secondary reporting;
- a mock;
- a screenshot when physical behavior is the target;
- a synthetic fixture when production behavior is the target.

A proxy may be useful but must remain labeled and may require plan revision.

## 4. Complete zero

A zero-result acquisition is evidence only when the acquisition itself completed credibly within the planned scope.

Before labeling `COMPLETE_ZERO`, distinguish it from:

- authentication/access failure;
- parser failure;
- timeout;
- rate limiting;
- truncated pagination;
- stale/incorrect query;
- wrong environment;
- unsupported endpoint;
- incomplete source universe.

Do not infer absence from acquisition failure.

## 5. Source freshness

Capture date/version/revision only when the property can drift enough to affect interpretation.

For mutable web/runtime/product behavior, current observation may be essential.

For stable historical/static material, exact version may be unnecessary unless the claim depends on it.

## 6. Dynamic evidence

When evidence can change during acquisition:

- define/carry the plan's relevant time window;
- capture retrieval/observation time;
- freeze exact state when required;
- record pagination/window boundaries;
- avoid merging observations from materially different states without provenance.

## 7. Transformation fidelity

For any non-trivial transformation:

- retain or reference the input;
- name the transformation;
- record version/configuration when material;
- preserve failures/unknowns;
- do not upgrade transformed output into direct evidence.

If a model extracts/classifies evidence, record it as model-derived unless the plan defines a different evidence role.

## 8. Mechanical integrity checks

The acquisition owner may verify:

- artifact exists;
- hash/version matches;
- expected fields/rows/records were captured;
- source pointer resolves;
- run completed;
- requested cases executed;
- files are readable;
- tool returned success/error.

These checks establish execution integrity, not evidentiary credibility.

## 9. Independence claims

Do not call evidence or acquisition independent merely because:

- different tools were used;
- two agents ran under the same orchestrator/context;
- two sources copied the same upstream source;
- two endpoints expose the same underlying dataset.

Preserve provenance needed for later reviewers to assess independence.

## 10. Privacy and minimization

Do not retain unrelated private material merely for reproducibility.

Capture the smallest evidence sufficient for:

- the planned claim;
- downstream review;
- material provenance.

Prefer bounded excerpts, hashes, IDs, or references when full content is unnecessary.

## 11. Stop at material sufficiency for acquisition

Stop when the controlling plan's acquisition obligations have reached their execution boundary and further collection is outside the plan or unlikely to change package completeness.

Do not independently expand the research question because a new interesting source appears.
