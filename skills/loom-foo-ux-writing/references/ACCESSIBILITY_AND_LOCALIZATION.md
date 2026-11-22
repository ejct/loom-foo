# Accessibility and localization for product copy

Read when accessible names/status messages, form errors, localization, or specific languages affect the decision. A well-written sentence does not by itself prove accessibility conformance.

## Accessibility checks tied to actual criteria

- **WCAG 2.2 2.5.3 Label in Name (A):** when a control has a visible text label, its accessible name includes that visible text. Check actual implementation, not a proposed copy string alone.
- **WCAG 2.2 3.3.1 Error Identification (A):** if an input error is automatically detected, identify the item and describe the error in text.
- **WCAG 2.2 3.3.2 Labels or Instructions (A):** provide labels/instructions for required input.
- **WCAG 2.2 3.3.3 Error Suggestion (AA):** provide known corrections, except where security or purpose would be jeopardized.
- **WCAG 2.2 3.2.4 Consistent Identification (AA):** identify repeated functionality consistently.
- **WCAG 2.2 4.1.2 Name, Role, Value (A):** programmatic labels/roles are an implementation condition, not achieved by copy alone.

Prefer descriptive link names, visible form labels, accurate alt text for informative images and textual state identification; don't rely only on icon/color/position. Identify when screen-reader announcement timing, focus management, or live regions need actual UI/engineering validation. Do not assert that an arbitrary message is WCAG-compliant from heuristic inspection.

## Localization-safe source copy

- Keep the actual target locale (`uk-UA`, `en-US`, `en-GB`, etc.) explicit when it matters. Source language and response language can differ.
- Avoid string concatenation, ambiguous placeholders and interpolations without semantic context. Provide translator comments for variable meaning, plural and gender agreement, and whether the phrase is a button, title or message.
- Confirm date/time/number/currency/measurement formatting expectations; don't invent a universal date format.
- Account for expansion/contraction, morphology, string order and bidirectional/Unicode scripts when applicable. Don't truncate meaningful warnings to meet English character limits; suggest layout adjustments if needed.
- Avoid idioms, culturally obscure jokes and grammatical assumptions baked into source strings; preserve genuine domain terminology when the audience uses it.
- For Ukrainian: do not translate English interface jargon word-for-word. Use natural Ukrainian grammatical case and verb aspect based on task; note uncertainties and consult authoritative language resources or the project's termbase when a disputed form matters. Do not present invented spelling rules as official norms.
- For English: follow the actual product/platform voice and locale, rather than treating `en-US` conventions as obligatory for all products.

## Handoff

When delivering a localized string set, keep stable provided keys and placeholders byte-for-byte; supply `source`, `locale`, `target`, `UI context`, `variable definitions` and `uncertainty` as needed. Actual rendering and assistive-technology tests belong to the implementation/runtime owner.

Sources: https://www.w3.org/TR/WCAG22/ ; https://www.w3.org/International/questions/qa-i18n/qa-i18n.uk.php ; https://learn.microsoft.com/en-us/globalization/methodology/software-internationalization

## Additional content-related WCAG 2.2 criteria to consider

- **3.3.4 Error Prevention (Legal, Financial, Data), AA:** for applicable consequential submissions, an implementation must provide reversibility, checking, or confirmation as specified by the criterion. Accurate confirmation copy is necessary but cannot establish the criterion on its own.
- **3.3.7 Redundant Entry, A:** avoid requiring information already entered in the same process except allowed cases; copy cannot excuse a redundant interaction.
- **4.1.3 Status Messages, AA:** relevant status messages must be programmatically determinable without receiving focus; text alone does not establish the announcement mechanism.
- **1.4.1 Use of Color, A / 2.5.3 Label in Name, A:** meaning and accessible-name requirements need layout and DOM checks.

Do not treat every explanatory design suggestion as a WCAG requirement. Distinguish normative success criteria, informative W3C Understanding documents and a product's own more stringent policy.

## Localization contract: context is as important as grammar

For ambiguous UI strings, supply a translator note describing `user intent`, `screen/state`, `referenced noun and grammatical number`, `placeholder names and examples`, `allowed ordering`, `tone`, `protected terms`, `max visible space if genuinely constrained`, and screenshots or component context when accessible. Reordering is often necessary; avoid concatenation of natural-language fragments.

Plural/grammatical variation must be handled by the **actual runtime message formatter** (for example ICU-style plural/select where supported), not a manually assembled string. Do not guess exact CLDR rules or write pseudo-ICU as if runnable without verifying the project's parser, locale and variables. If Ukrainian singular/plural cases, gender agreement or grammatical case are material, author multiple candidate examples and flag implementation integration for native-speaker/runtime verification.

Prefer pseudolocalization to find clipping, encoding and missing-resource defects; this is a **test to run on a real UI**, not a claim that copy alone passed. Date and time require correct locale and timezone; warn against hidden UTC/local-clock assumptions.

Sources: https://www.w3.org/TR/WCAG22/ ; https://learn.microsoft.com/en-us/globalization/internationalization/contextual-metadata ; https://learn.microsoft.com/en-us/globalization/internationalization/pluralization ; https://learn.microsoft.com/en-us/globalization/methodology/pseudolocalization ; https://www.w3.org/TR/international-specs/
