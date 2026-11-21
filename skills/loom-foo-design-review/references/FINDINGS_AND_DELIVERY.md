# Design Review — usable findings, not generic judgments

For a simple case, prose with annotated reference points is enough. For complex reviews, use a few structured findings:

- **Location / state:** page, component, text span, frame or pixel size actually viewed.
- **Finding:** observable difference or specific suspected problem, without accusation.
- **Evidence class:** OBSERVED / SOURCE_CHECKED / INFERRED / HYPOTHESIS / PREFERENCE / UNVERIFIED.
- **Impact / priority:** why the issue matters to the intended task, with severity only when justified.
- **Proposal:** concrete correction or test and what acceptable quality should look like.
- **Trade-off:** what might worsen when fixing it, if material.

Begin with the most consequential overall assessment tied to the actual supplied version/medium. If the artifact is strong, state the relevant strengths; use `NO_MATERIAL_ISSUES_FOUND` when warranted.

Separate changes the user may authorize from changes actually performed. Review-only -> findings, **no edits**. Do not declare formal WCAG/production conformance unless the required checks actually ran at the necessary fidelity. Do not cite invented sources, user feedback, brand constraints, web analytics or expert consensus.

Keep the output proportionate: no obligatory executive report for a favicon, no list of 20 speculative issues for an unproblematic poster. A concrete before/after sketch may be useful as a suggestion but must not be presented as an already modified source file.
