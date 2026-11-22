# Content systems: terminology, voice, tone and patterns

Read when user asks for cross-screen or product-level content standards, not for a routine single label.

## Determine the authoritative vocabulary

Prefer an actual product glossary, established component text and accepted UX decisions. Record `concept → preferred term → forbidden/ambiguous synonyms → usage context`, and note disputed terminology. Do not silently invent a canonical term from a single screenshot. Distinguish named entities, visible UI labels, technical API terms, accessible names, and translation keys.

## Voice versus tone

Stable **voice** expresses product identity: level of directness, technicality, formality and point of view. **Tone** adapts to stakes, user task, unfamiliarity and failures without assuming feelings or using empathy scripts. Provide a small representative chart, for example:

| Moment | Voice retained | Tone shift | Avoid |
| --- | --- | --- | --- |
| Everyday task | Direct and competent | Efficient | Over-explaining or praise |
| First use | Direct and competent | More instructive | Forced excitement |
| System failure | Direct and competent | Calm, specific, recovery-focused | Blame, invented reassurance |
| Destructive action | Direct and competent | Explicit and neutral | Euphemism or pressure |

Avoid universal commands such as “always friendly”, “always 2–4 words”, or US grade-level metrics across locales and expert audiences. Use examples showing preferred and unacceptable phrasing rather than relying only on adjectives.

## Content pattern contract

For a recurring content-bearing pattern, define: `purpose`, `user task`, `trigger/state`, `component`, `message anatomy`, `string constraints`, `accessible name/status`, `localization context`, `important exceptions` and `behavior owner`. Make it proportional; don't require a component specification for a one-off toast.

## Consistency without rigid uniformity

Prefer the same term for the same concept and the same label for the same action, unless user context changes meaning. Do not force one label for different consequences just because the visual component is the same. When a new rule affects many products, identify owners, consumers and migration implications; Design Systems owns cross-consumer component governance.

Sources informing patterns: https://atlassian.design/get-started/content-design ; https://fluent2.microsoft.design/content-design ; https://shopify.dev/docs/apps/design/content

## Content operations: beyond a style guide

For an explicitly requested inventory or cross-screen content system, identify the smallest source of truth needed for reuse, change impact and localization. A useful content record may have `string_id`, `component`, `context`, `trigger/state`, `source_locale`, `source_text`, `product_object/action`, `variables and type`, `approved terms`, `sensitivity`, `owner`, `status`, `reviewed_version`, `target_locales`, and `consumer_locations`. Keep only fields actually needed; do not impose a mandatory global schema on one button.

- **Source authority:** prefer a supplied established termbase/content spec. Suggest changes as candidate rules, not automatic canonical updates.
- **Content debt:** identify duplicate meanings under different labels, a reused ID for different behaviors, ambiguous short strings, unsupported names, and strings with missing context. Treat evidence from a sampled screen as sampled, not an exhaustive inventory.
- **Change propagation:** for a rename, map actual consumer screens, accessible names, help text, notifications, search/filter labels and affected translations. Record whether old and new terms represent the same concept; a one-word change can alter behavior expectations.
- **Review surface:** for shared content patterns, include one representative success, error, restricted, and localization edge state as appropriate. Define who owns content decisions versus component behavior, but do not invent an approval bureaucracy.
- **Implementation:** source text and stable string keys are separate; do not silently rename keys. Tooling can lint deterministic invariants when data exists; a written guideline does not prove string propagation.

Sources: https://www.carbondesignsystem.com/building-blocks/foundations/content ; https://atlassian.design/foundations/content ; https://learn.microsoft.com/en-us/globalization/internationalization/contextual-metadata
