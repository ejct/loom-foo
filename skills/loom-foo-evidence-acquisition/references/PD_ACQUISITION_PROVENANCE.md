# evidence-acquisition — detailed conditional method (PD_ACQUISITION_PROVENANCE.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 5. Map planned acquisition obligations

Create the smallest internal map needed to answer:

- Which planned evidence items/steps are required?
- What counts as completing each acquisition obligation?
- Which source/subject does each item target?
- Which stop/adaptation rule governs it?

Prefer stable plan pointers over copying research rationale.

One Evidence Plan may legitimately contain multiple acquisition methods. Do not split it merely because several tools or sources are involved.
## 9. Keep raw and transformed evidence distinguishable

Evidence acquisition may perform transformations required by the plan, including deterministic parsing, unit conversion, format normalization, exact span extraction, or plan-specified model extraction/classification.

When transformed evidence is material:

- preserve a raw/recoverable source pointer;
- record the transformation/tool/version when it can affect meaning;
- distinguish direct capture from derived/transformed output;
- preserve uncertainty or parser/model failure rather than inventing a value.

Do not add unsupported interpretation, causal explanation, or evaluative judgment merely to make the package easier to read.
## 10. Preserve minimum useful provenance

Provenance should be sufficient to recover what evidence came from where and how it was acquired when that matters.

Prefer references over duplication.

Depending on the claim, useful provenance may include:

- source locator;
- source/version/revision/date;
- acquisition timestamp/window;
- query/request/input;
- runtime/tool/version;
- artifact/hash/run/trace pointer;
- transformation lineage;
- actor/executor role;
- relevant access/environment scope.

Do not require a W3C PROV graph, global EvidenceRecord ontology, persistent registry, or full runtime trace.

Runtime traces are optional supporting provenance, not automatic durable project truth.
## 11. Validate acquisition integrity, not evidentiary meaning

Before packaging, perform an author-owned mechanical/fidelity check:

- required acquisition obligations are mapped;
- obtained evidence points to the correct subject/source;
- complete-zero is distinguishable from failure;
- material retries/deviations/substitutions are visible;
- raw/transformed lineage is recoverable when material;
- missing/unavailable/not-run items are explicit;
- package claim/execution limits match the actual run.

This does **not** assess whether the evidence is credible enough to accept a claim or decision. That belongs to `loom-foo-evidence-review`.
## 12. Emit the Evidence Package

The Evidence Package is one logical artifact. It may be tiny or may reference several raw artifacts.

For the artifact contract, read `references/EVIDENCE_PACKAGE_CONTRACT.md`.

When material, the package should make recoverable:

- controlling plan/acquisition-contract identity;
- subject and scope;
- execution environment/time window;
- plan-item -> evidence-item/attempt mapping;
- evidence source and acquisition provenance;
- raw/minimally transformed evidence or durable pointer;
- acquisition outcome;
- deviations/substitutions;
- gaps/failures/not-run items;
- privacy/redaction/retention constraints;
- package-level limits;
- stop reason;
- skill-local disposition.

Do not duplicate large raw evidence when a stable, reviewable pointer is sufficient.
