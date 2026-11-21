# Design Review — substantive critique method

## Judge against intent before style

Reconstruct the task: audience, job, intended first impression, core action/reading path, constraints, accessibility/technical medium and known design decisions. Where this is unknown, analyze defensibly visible relations and mark anything about user behavior as hypothesis.

Review design as a system of trade-offs. A visually bold feature is not inherently a problem; a minimal interface is not inherently better; a deviation from a grid may be intentional. Ask: what information/action does this feature advance or obstruct under the specified use conditions?

## Hypothesis challenge

For a meaningful finding:

1. **Observation:** specific location, state, dimension and appearance; quote protected copy exactly.
2. **Possible cause:** composition, affordance, hierarchy, mismatch, missing context, implementation state, artifact defect.
3. **Consequence:** task friction, mistaken reading, lack of trust, exclusion, technical risk, or aesthetic incoherence — stated as observed or hypothesized.
4. **Rival explanation:** intent, audience knowledge, branding, technical constraints, unobserved state. Do not accuse a designer of an error simply because an intent is unknown.
5. **Correction:** smallest concrete change that addresses the mechanism; specify what to keep.
6. **Validation:** how to see if the fix helped (artifact render, source check, simulated state, user test, production proof). No need for a formal study for a one-line defect.

## Priority without theatrical scoring

- **Critical:** demonstrably blocks central user action or loses required content, or an applicable hard constraint is violated. Requires proof at relevant fidelity.
- **Major:** materially weakens intended reading, accessibility, comprehension or coherent function under supplied conditions.
- **Minor:** noticeable craft/consistency issue with bounded local impact.
- **Observation / preference:** a legitimate alternate creative direction or hypothesis needing evidence, not a defect.

Do not assign criticality when only a low-fidelity screenshot suggests it. Do not produce a percentage quality score, rank creators' talent or enforce one taste.

## Comparisons

Use identical tasks/context across alternatives. Identify what improves and regresses, including typographic clarity, screen real estate, information ordering, contrast, brand distinctiveness, implementation effort and flexibility. Choose a default only when trade-offs support it. Preserve acceptable unusual solutions.

## Independent review semantics

Consulting Review instructions after creating the design in the **same conversation** remains self-check; no new independence arises from a label. If an independent evaluator is available and warranted, pass a frozen artifact plus brief without the author's justification or a prewritten verdict where practicable. Record actual reviewer, context and evidence rather than implying a separate agent ran.

## Sources

- NN/g heuristic evaluation guidance: https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/
- W3C WCAG 2.2 interpretation: https://www.w3.org/WAI/WCAG22/Understanding/
- Agent Skills spec (source packaging, not review quality): https://agentskills.io/specification
