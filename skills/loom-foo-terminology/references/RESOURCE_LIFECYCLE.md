# Terminology resources and lifecycle

Use for a reusable glossary/termbase, term extraction, resource audit, explicit approval/version constraints or changes across affected documents. Use smallest sufficient resource; no mandatory registry, graph, format conversion or project file writes.

## Resource choice and coverage

A simple glossary may suffice for a short project. A concept-oriented termbase helps when definitions, senses, multiple languages, mappings, relations and authority must be tracked. Lexical resources record forms and senses; translation memory/parallel text records actual or candidate translated occurrences, not concept identity. Native CAT, project Markdown/TSV, TBX or another existing resource may be appropriate. Use actual version/profile and tooling where necessary, not a generic universal schema. Extraction/ranking may assist candidate discovery on authorized corpora; it is not an approval or semantic oracle.

Declare requested corpus/segment and record actual covered portions when building/auditing. Group candidates from observed occurrences with locators. Deduplicate true duplicates without collapsing different concepts or separate source records. Support upfront, concurrent, delegated or minimal glossary work according to actual project. Preserve unresolved terms and revisit dependent text; an explicit project prerequisite is distinct from a mandatory default approval gate.

## Proportionate record

A one-term result can simply contain term, context, definition/meaning, source/locator, alternative(s) and uncertainty. For a reusable resource add only needed stable local concept/sense identity, language/locale, definition, terms and usage constraints, mapping/relations, source authority/version, proposed/approved/unknown/superseded status, reviewer/owner and affected usages. Evidence confidence and acceptance are independent. Never invent review provenance. If resource already has an approved model, preserve it.

## Review and update

Compare current authoritative resource and actual candidate entries, not merely an issue summary or planned change. Resolve same-concept conflicts, distinct sense overlaps, stale definitions, invalid mappings and real missing coverage; preserve contextual variants and negative evidence. Mark draft/proposed vs accepted and applied vs pending changes. Propose the smallest change, explain effects on translations, code/UI or documents as appropriate, preserve unaffected entries. Verify final exact artifact if an authorized update occurred; native parsing/schema checks do not prove semantic quality. Respect real scope, permissions and authority. No automatic canonical promotion, external upload or mass rewriting. If data is incomplete, identify uncovered material rather than claiming a complete glossary.
