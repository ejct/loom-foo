# Requirement Quality


Use this reference when a Specification is consequential, stateful, externally visible, compatibility-sensitive, or still ambiguous after the core pass.


The checks below protect semantic quality. They are not a mandatory visible checklist.


## 1. Necessary


Every material obligation should have a legitimate reason to exist.


Ask:
- Which accepted intent, decision, standard, constraint, or derived implication requires it?
- Would removing it violate an established goal or contract?


Warning signs:
- requirement appears only because one implementation already works that way;
- reviewer preference promoted to product truth;
- speculative future need;
- generic "best practice" with no local consequence.


Unsupported obligations should be removed, downgraded to assumptions/options, or escalated for authority.


## 2. Singular


Prefer one independently checkable obligation per statement.


Weak:
"The system validates the token, logs the event, notifies the user, and expires the session."


This may hide four independently decidable obligations.


Keep combined wording only when the behaviors form one inseparable semantic rule.


## 3. Unambiguous


Challenge words that can support materially different implementations:
- fast;
- robust;
- intuitive;
- secure;
- timely;
- reliable;
- seamless;
- near-real-time;
- appropriate;
- minimal;
- gracefully.


Operationalize them only when their precision matters.


Do not invent a number merely to remove vagueness. If the threshold is an unresolved product or empirical decision, surface it.


## 4. Observable / verifiable


A requirement should permit a conceptual conformity judgment.


Ask:
- What observable state or behavior would count as satisfied?
- What observation would clearly violate it?
- Is the requirement only an aspiration with no conformance meaning?


If a requirement cannot be verified because the desired property itself is undefined, repair the requirement first.


If the property is defined but the method of proving it is non-trivial, route evidence design separately.


## 5. Complete enough


Completeness is contextual, not maximal.


For stateful behavior, consider:
- initial state;
- normal transition;
- repeated action / idempotence;
- invalid input;
- cancellation/interruption;
- timeout/expiry;
- partial failure;
- retry;
- concurrent/conflicting action;
- terminal state;
- recovery;
- compatibility with prior state.


For access/permission behavior, consider:
- authorized path;
- unauthorized path;
- revocation;
- stale credential/token;
- inheritance/delegation;
- information leakage through errors/metadata.


For data transformation, consider:
- null/empty;
- malformed;
- unknown value;
- ordering;
- duplicates;
- precision/loss;
- reversibility;
- partial processing.


Do not cargo-cult every category.


## 6. Consistent


Check:
- requirement vs requirement;
- requirement vs accepted constraint;
- current delta vs unaffected baseline;
- scenario vs normative rule;
- interface/schema vs prose;
- invariant vs allowed transition.


When two authoritative sources conflict, do not repair the conflict by interpretation alone. Surface authority resolution.


## 7. Solution-independent where possible


A requirement should preserve legitimate solution space.


Warning signs:
- names a database, framework, queue, service topology, library, model, UI widget, or file layout without authority;
- dictates internal decomposition;
- prescribes algorithm where only outcome matters.


Keep the detail when it is itself required by:
- compatibility;
- deployment environment;
- regulator/platform;
- accepted architecture constraint;
- migration contract;
- interoperability.


## 8. Feasible enough to specify


Do not require proof of implementation feasibility before writing any requirement.


But do challenge obligations that appear physically, technically, legally, or economically impossible under accepted constraints.


If feasibility is genuinely uncertain:
- preserve the intended semantic target when useful;
- mark the uncertainty;
- return `VALIDATION_REQUIRED` when evidence is needed before the contract can be accepted downstream.


## 9. Bounded


Define scope where omission would create semantic ambiguity.


Examples:
- which users/actors;
- which lifecycle phases;
- which data classes;
- which environments;
- which compatibility versions;
- which temporal window.


Do not add artificial scope metadata that no downstream consumer needs.


## 10. Stable referenceability


A material obligation should be referenceable without relying on paragraph position.


Prefer semantic names.


Avoid identities such as:
- "the third bullet";
- "requirement above";
- line-number-only references.


## 11. Acceptance quality


Acceptance conditions should be:
- tied to the obligation;
- observable;
- strong enough to reject an invalid implementation;
- not secretly weaker than the normative statement;
- not overfitted to one implementation.


A scenario is evidence of intended behavior, not necessarily the entire rule.


## 12. Overconstraint


Ask:
- Does this rule exclude a solution that would satisfy all authoritative intent?
- Is the excluded behavior actually harmful?
- Is the restriction inherited from an old implementation rather than an accepted contract?


Overconstraint increases downstream design cost and should require a legitimate reason.


## 13. Derived requirements


A requirement may be derived from another accepted obligation.


When derivation is non-obvious:
- retain the parent/source;
- state the logical or constraint-based reason;
- distinguish derivation from new stakeholder intent.


Architecture-discovered constraints must not silently become product semantics; they require explicit acceptance at the correct authority boundary.


## 14. Anti-patterns


Repair these before `SPEC_READY`:
- vague adjective used as acceptance criterion;
- implementation detail posed as a requirement without authority;
- requirement with no legitimate provenance;
- several behaviors hidden in one sentence;
- happy-path-only stateful specification;
- scenario contradicts normative prose;
- delta rewrites unrelated behavior;
- test procedure confused with required behavior;
- user story used as the only semantic contract;
- exhaustive documentation added without decision value;
- numeric threshold invented solely to sound precise;
- "should" used where requirement strength is materially unclear;
- current implementation treated as normative by default.