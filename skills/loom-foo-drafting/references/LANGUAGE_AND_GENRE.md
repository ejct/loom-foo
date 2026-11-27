# Language, voice and genre · v0.1

Load this reference when multilingual adaptation, cross-cultural register, technical vocabulary, source fidelity or genre choice matters.

## Language dimensions

Do not conflate the user's chat language, source language, expected final language, locale/region (e.g. uk-UA, en-US, en-GB), explanation language and literal technical tokens (code/IDs/quoted text). If a target language is explicit, use it even when the surrounding conversation is in another language. If not explicit, infer from the user request and the intended recipient; don't over-generalize from a technical product name.

Examples of variants needing attention: UK/US spelling and punctuation for public-facing copy; polite address, case forms and euphony in Ukrainian; date and number formatting only when user authorizes locale adaptation (avoid changing quantities or legal identifiers); local industry terms vs source terms. No embedded language profile proves authoritative normative correctness. Use current primary sources or dictionaries where normative certainty is consequential. For unverified low-resource languages, state limits rather than claim fluent or standardized output.

**Ownership:** The table below describes fidelity constraints, not a routing rule. `loom-foo-translation` owns source-faithful translation and locale rendering when available; `loom-foo-translation-analysis` owns source/target comparison. Drafting owns newly authored prose, substantial authorized audience adaptation and transcreation. Translation is a fallback only if its specialist is unavailable.

## Transformation contract

| Operation | What can change | What stays invariant unless explicitly authorized |
| --- | --- | --- |
| New drafting | Rhetorical presentation | Given facts, author stance, required details, audience/medium constraints |
| Light rewrite | Word choice, rhythm, syntactic clarity | Meaning, all protected entities/figures/phrases, voice and degree of certainty |
| Structural rewrite | Paragraph ordering and transitions in requested section | Facts, responsibility, chronology when causal, important qualifiers |
| Translation | Surface language and natural grammar | Meaning, actors, negations, modality, dates, amounts, key technical identifiers |
| Localization | Idiom, register, spelling, date presentation if allowed | Core content obligations, legal/commercial promises, unchangeable names/IDs |
| Transcreation | Creative concept/tone where explicitly permitted | Brief, constraints and disclosed material departures |

Meaning preservation is context-sensitive; exact back-translation is not a universal oracle. Compare specific propositions and commitments, not just word overlap. When a source phrase is ambiguous, preserve its ambiguity or disclose the interpretation.

## Genre defaults (adapt, do not force)

- Correspondence / outreach: intended request or offer early, necessary context, respectful specificity, one natural closing; avoid spammy urgency and fake familiarity. No invented recipient identity.
- Product copy: concrete capability, user benefit tied to evidence, honest scope and status, audience terminology, clear CTA when appropriate; no invented statistics or guarantees.
- Case-study prose: describe problem, contribution, evidence, decision/trade-off and actual outcome at the level supported. The architecture belongs to Narrative Design if that's the task.
- Technical documentation: prerequisites, expected action/state, exact commands, limitations and recovery; commands and identifiers must remain precise. Language polishing cannot change runtime semantics.
- Articles/essays: clear throughline and voice, fair attribution, useful examples and uncertainty. Narrative architecture is a separate concern for complex pieces.
- Public posts: concise, voice-consistent, evidence-grounded; no mandatory hashtags/emojis/call-to-action.
- Agent prompts: preserve authority and invariants; see AGENT_ARTIFACTS.md.

## Author voice protection

Voice comprises lexical register, sentence cadence, directness, preferred terminology, humor or profanity, and level of explicit uncertainty. Preserve it when revising existing text unless the user wants a new voice. Avoid formulaic opener/closer and automatic "improvement" to neutral corporate prose. A regional or colloquial form is not automatically an error in a deliberately voiced text.
