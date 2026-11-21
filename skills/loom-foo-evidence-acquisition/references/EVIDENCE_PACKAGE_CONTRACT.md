# Evidence Package Contract

Status: candidate reference for `evidence-acquisition v0.1.0-candidate`.

The **Evidence Package** is the primary artifact owned by `loom-foo-evidence-acquisition`.

It records what evidence was actually acquired under a controlling Evidence Plan or equivalent bounded acquisition contract. It does not decide what the evidence ultimately means.

## 1. Artifact boundary

Input:

- current Evidence Plan / acquisition contract;
- action authority;
- subject/source locators;
- available runtime/tool capabilities.

Output:

- Evidence Package.

The package may reference external/raw artifacts rather than copy them.

Do not require a separate first-class Acquisition Record unless later evidence establishes a distinct lifecycle or consumer.

## 2. Minimum recoverable contract

When material, make recoverable:

- package status/disposition;
- controlling plan identity/version;
- acquisition subject/scope;
- execution environment and time window;
- planned evidence requirement -> acquired evidence mapping;
- evidence item identity;
- source locator/version/revision/date;
- acquisition action/method/tool;
- raw/minimally transformed result or durable/recoverable pointer;
- transformation/normalization lineage;
- acquisition outcome;
- deviation/substitution;
- failure/retry state;
- missing/not-run/excluded items;
- privacy/redaction/retention constraints;
- package-level execution/claim limits;
- stop reason.

Do not force empty fields.

## 3. Evidence item identity

Use stable evidence-item identifiers when they improve traceability.

Identity should be strong enough for the intended review/reproduction claim.

Examples:

- a URL + retrieved timestamp;
- file ID + revision/span;
- commit SHA + file/range;
- dataset/case ID;
- run ID + artifact hash;
- measurement subject + timestamp/window;
- immutable artifact pointer.

A label alone is not identity when two different underlying subjects could satisfy it.

## 4. Acquisition outcome semantics

Preserve these distinctions when applicable:

### ACQUIRED
The requested evidence was obtained.

### COMPLETE_ZERO
The acquisition completed correctly and returned no matching evidence.

### PARTIAL
Only part of the planned evidence was obtained.

### ACCESS_BLOCKED / UNAVAILABLE
The evidence target was not accessible under the current context.

### FAILED
The acquisition operation failed.

### NOT_RUN
The plan included an item that was not attempted.

### EXCLUDED
The item/source was excluded by the accepted selection rule.

### SUBSTITUTED
A planned source/method was replaced.

Representation is flexible. These are semantic distinctions, not a mandated enum schema.

## 5. Package completion

Use `EVIDENCE_PACKAGE_READY` when all material acquisition obligations in the controlling contract are resolved as one of:

- successfully acquired;
- valid complete zero;
- explicitly plan-allowed exclusion;
- another plan-defined completed state.

A package may still be ready when its evidence is surprising, contradictory, negative, or unfavorable to the target claim.

Use `PARTIAL_EVIDENCE_PACKAGE` when material planned acquisition remains unresolved, failed, unavailable, or not run but the collected evidence is still useful to review.

Do not let a partial package imply that missing items are ignorable.

## 6. Source vs observation vs transformed evidence

Keep distinguishable:

- **source/subject** — where evidence originates;
- **direct acquisition result** — what was actually observed/retrieved/measured;
- **transformed evidence** — a plan-required deterministic/model/human transformation;
- **interpretation** — what the evidence implies.

The first three may appear in an Evidence Package. Interpretation belongs downstream unless the controlling acquisition plan explicitly defines a mechanical label as part of collection.

## 7. Minimal transformation

A transformation is acceptable inside acquisition when:

- required or permitted by the controlling plan;
- its input is recoverable;
- the transformation is identified when material;
- failure/uncertainty can remain visible;
- it does not silently add stronger meaning than the source supports.

Examples:
- parse JSON;
- extract a named field;
- normalize units;
- select an exact source span;
- compute a plan-defined measurement;
- run a plan-defined classifier and preserve its output as model-derived evidence.

Do not turn a model-derived extraction into direct source evidence.

## 8. Provenance strength

Capture only provenance that materially protects:

- subject identity;
- reproducibility;
- reviewability;
- temporal validity;
- source/transform lineage;
- authority/scope;
- evidence integrity.

Runtime trace/span IDs can supplement provenance but should not become the sole durable basis for consequential evidence when the trace may expire or be inaccessible later.

## 9. Raw evidence storage

Prefer references when copying is unnecessary, disallowed, expensive, sensitive, or unstable.

Durable capture is warranted when:

- source mutation/deletion risk is material;
- exact bytes/state are part of the claim;
- downstream review cannot reliably re-fetch the source;
- reproducibility requires the captured state;
- the plan explicitly requires a frozen artifact.

Respect copyright, privacy, retention and disclosure constraints.

## 10. Claim limits

The package may carry claim limits inherited from the plan or caused by execution, such as:

- single environment only;
- one account/cohort;
- partial time window;
- inaccessible source subset;
- proxy instead of direct measurement;
- transformed/model-derived evidence;
- unresolved source drift;
- incomplete capture.

The package does not adjudicate whether those limits are acceptable for the final decision.

## 11. Fast path

For a trivial one-source check, the whole package may be:

- plan/question pointer;
- source identity;
- acquisition result;
- source/version/time;
- outcome;
- limitation.

No table/schema is required.

## 12. Anti-goals

The Evidence Package is not:

- a transcript;
- a full runtime trace;
- a generic project evidence database;
- a W3C PROV graph;
- an evidence-quality verdict;
- a decision record;
- a universal research-result schema.
