# Behavioral Patterns


Use these patterns only when they make a semantic contract clearer. They are representation tools, not mandatory specification syntax.


## 1. Plain normative prose


Best for compact stable obligations.


Pattern:


`<subject> must <required behavior> [under <condition>] [within <semantic bound>].`


Example:


`A revoked grant must not authorize a new access attempt.`


Prefer direct wording over ceremony.


## 2. Event / condition / response


Useful for reactive behavior.


Pattern:


`When <trigger> while <precondition>, the system must <response>.`


Example:


`When the owner revokes an active grant, future access attempts using that grant must be denied.`


This separates:
- state/precondition;
- event;
- required response.


Do not force an event form onto static invariants.


## 3. Given / When / Then scenarios


Use scenarios to clarify concrete paths, especially where examples expose ambiguity.


Example:


`Given an active grant`
`When the owner revokes it`
`Then a later access attempt using that grant is denied.`


A scenario is not automatically the whole rule. Keep a normative obligation when broader behavior exists beyond the example.


## 4. State-transition representation


Prefer a state model when correctness depends on lifecycle.


Recover at minimum:
- meaningful states;
- transition triggers;
- allowed transitions;
- forbidden transitions;
- terminal states;
- invariants across states.


Common stateful omissions:
- repeated action;
- cancellation;
- retry;
- timeout/expiry;
- replacement/supersession;
- partial failure;
- stale state;
- concurrent conflict.


Use a table when it is clearer than prose:


State | Trigger | Next state | Required effect | Invalid/edge behavior


Do not create a state machine for essentially stateless behavior.


## 5. Invariants / properties


Use when a property must hold across many transitions or implementations.


Examples:
- "A revoked credential never authorizes a new request."
- "Accepted history entries are never silently mutated."
- "A public response never reveals private payload content."


Separate:
- safety invariant: something bad must never happen;
- liveness obligation: something good must eventually happen;
- bounded temporal rule: something must happen within a defined semantic interval.


Do not invent timing bounds if authority has not established them.


## 6. Interface and schema contracts


Use structured interface representation when semantics depend on exchanged data.


Specify only what is semantically required:
- required/optional fields;
- value domains;
- null/unknown behavior;
- compatibility/version rules;
- error semantics;
- ordering/duplication guarantees;
- idempotence where material.


OpenAPI, JSON Schema, protobuf, typed schemas, or similar can be projections when the interface warrants them.


Do not let a schema silently substitute for behavioral rules that it cannot express.


## 7. Data transformation contracts


For transformations, define:
- accepted input domain;
- output semantics;
- preservation/loss rules;
- ordering;
- duplicates;
- invalid/unknown values;
- precision/rounding;
- determinism/equivalence expectations;
- partial failure.


Prefer properties over example-only coverage when the transformation is broad.


## 8. Async / long-running operations


When an operation is not instantaneous, consider:
- initiation acknowledgment;
- in-progress semantics;
- completion;
- cancellation;
- timeout;
- retry;
- duplicate initiation;
- replacement/supersession;
- partial completion;
- progress visibility only if required.


Do not assume cancellation means rollback unless the contract requires it.


## 9. Permission and privacy behavior


Consider:
- who may initiate;
- who may observe;
- what data becomes visible;
- grant;
- revoke;
- stale authorization;
- delegated/indirect access;
- error-message leakage;
- metadata leakage;
- retention after permission changes.


Separate access-control mechanism from required visibility semantics.


## 10. Compatibility contracts


Use when old/new versions or external consumers matter.


Specify:
- supported versions;
- accepted input from older/newer peers;
- unknown-field behavior;
- downgrade/upgrade semantics;
- migration coexistence;
- removed/deprecated behavior;
- preservation requirements.


Do not infer backward compatibility by default.


## 11. Agent/AI behavior


For agentic or stochastic systems, specify semantic obligations separately from evaluation methodology.


Useful dimensions:
- allowed tools/actions;
- authority boundaries;
- required refusal/block behavior;
- state/context preservation;
- deterministic invariants;
- semantic equivalence where exact text may vary;
- escalation conditions;
- provenance requirements;
- uncertainty disclosure.


Avoid impossible exact-output requirements when variation is legitimate.


If conformity requires repeated stochastic evaluation, keep the semantic requirement here and route the measurement design to `loom-foo-research-design`.


## 12. Examples and counterexamples


A small positive and negative example can disambiguate a rule.


Use examples when:
- boundary cases are hard to describe;
- terminology is overloaded;
- equivalent outputs are allowed;
- invalid behavior is subtle.


Examples must not contradict the normative contract or silently narrow it.


## 13. Formalization escalation


Consider stronger formalization when:
- state/concurrency interactions create hidden contradictions;
- safety/security consequence is high;
- compatibility rules are combinatorial;
- invariants are central;
- ordinary prose repeatedly fails to remove ambiguity.


Possible tools:
- property-based representation;
- temporal/state models;
- model checking;
- formal schemas.


Escalation should protect a real risk. Formal notation is not a quality signal by itself.


## 14. Choosing a representation


Prefer the least formal representation that:
- expresses the required semantics without material ambiguity;
- preserves stable referenceability;
- supports downstream architecture and verification;
- remains understandable by the intended users/agents.


Use multiple representations only when they establish different useful properties.