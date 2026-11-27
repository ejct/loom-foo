---
name: loom-foo-terminology
description: "Research, disambiguate, define, align and audit terms and concepts in one or more languages; build a proportionate glossary or term resource. Use when a term decision, concept/term equivalence or terminology resource is the primary result. Not routine lookup, passage translation, UI behavior/naming decisions, domain architecture or canonical persistence."
metadata:
  family: "writing"
  project: "loom-foo"
  version: "0.2.0"
compatibility: "Portable Agent Skills guidance; authorized corpora, dictionaries and termbase tools are optional."
---

# Terminology

## Result and ownership

Produce a grounded term decision, candidate term record, glossary or conflict assessment. Own the language-specific investigation of concepts, senses, definitions and terms, including monolingual work and cross-language/resource equivalence. Not ordinary glossary lookup (use supplied resource or Knowledge Retrieval), passage translation (Translation), comparative translation critique (Translation Analysis), product vocabulary choices that depend on actual UI behavior (UX Writing), behavioral specification or domain architecture, generic knowledge intake, target-text proofreading, or canon persistence. A term analysis may expose unresolved product/domain meaning; it cannot settle unapproved behavior or authoritative legal meaning.

## Critical invariants

- Distinguish concept, sense, lexical form/label, definition, usage context, evidence and term status. Shared spelling is not proof of concept identity; legitimate synonyms, contextual variants and polysemy can coexist. Do not force a universal one-term-one-meaning policy or invent a graph.
- Treat source usage and supplied glossaries as evidence; actual project/institutional authority determines accepted status. Distinguish proposed, approved, superseded and unknown; evidence confidence is not approval. Do not infer canonical status from frequency, a proposal, a stale change summary, recency or an agent decision. Resolve current resource when material.
- Scope to the user's request and available authorized sources. Do not disclose private corpora, run untrusted extractors, mutate source/native resources or publish without authority; an analysis or candidate does not authorize canon changes. No claim of professional certification, complete corpus coverage or independent review without evidence.

## Fast path

1. Identify intended outcome and relevant language(s), domain, context, actual term occurrence and existing authority. Use supplied definitions/occurrences; ask only for blocking ambiguity. Do not treat an isolated gloss as an exhaustive sense inventory.
2. Choose the smallest operation: **RESOLVE** a term/ambiguity; **BUILD** a glossary from supplied or authorized material; **ALIGN** terms or resource entries across contexts/languages; **AUDIT** a resource for conflicts, stale entries or misleading mappings. These labels are optional; don't force mode selection or create a glossary for one term.
3. Compare actual usages, definitions, concept boundaries, alternative labels and evidence. Test positive/negative examples when a definition is consequential. Split homonyms, preserve justified contextual variants, qualify cross-language mappings, and return a proposed choice or unresolved conflict. Where actual authority settles the choice, report that source, scope and version instead of inventing an approval.
4. Deliver concise term + context/meaning + relevant source/alternative/uncertainty, or a scoped resource with identifiers, statuses and coverage only as needed. Use the user's existing format and project workflow. Keep missing/unresolved terms visible; mark corpus limits. No automatic write or mandatory global schema.

**Conditional loss-aware resource transfer.** When moving an approved or proposed terminology resource into a materially different format, schema or consumer, inspect the actual target profile and determine which sense distinctions, alternative terms, constraints, statuses, provenance and language/context qualifiers it can represent. Preserve the authoritative source; report unsupported or lost properties and prefer a compatible representation, scoped resources or a separate constraint carrier where appropriate. Verify the actual output and target interpretation when feasible; do not silently flatten conflicting senses or forbidden terms, infer support from file extensions, upload private resources or claim target enforcement from an export alone. No transfer procedure for ordinary term resolution.

## Conditional specialist composition (L1)

Use `loom-foo-knowledge-retrieval` for missing current approved project terms/decisions; `loom-foo-evidence-acquisition` for exact necessary public/authorized attestations when a bounded acquisition plan or appropriate evidence request applies; `loom-foo-evidence-review` for consequential conflicts in an existing evidence package. Ordinary supplied-resource work needs none. If an exact unfamiliar-language passage is necessary to establish a concept, consult `loom-foo-translation` on that passage; if actual paired renderings disagree in a consequential property, consult `loom-foo-translation-analysis` for that bounded contrast. When Translation or Analysis is the caller, resolve the term from available evidence and return the term decision; do not re-enter the original request or create a cycle. For a product-state-dependent label, return the concept distinction to UX Writing; Specification/Architecture retain domain behavior/model authority. Knowledge Intake retains generic knowledge candidate ownership; Project Knowledge Stewardship owns separately authorized durable canon updates. Use only the specialist whose distinct output is materially needed. If absent, continue from available evidence and label limitations.

## Conditional references

- Competing senses, definitions, overlapping concepts, domain disagreement or boundary tests → [Concepts and senses](references/CONCEPTS_AND_SENSES.md).
- Building/auditing a reusable resource, progressive extraction, authority, versioning, change impact or format selection → [Resource lifecycle](references/RESOURCE_LIFECYCLE.md).
- Cross-language, cross-domain or historical equivalence, lack of direct equivalents or conflicting mappings → [Multilingual equivalence](references/MULTILINGUAL_EQUIVALENCE.md).

Do not load all references for a one-term decision. No required external service, persistent store or separate reviewer.

## Completion

All material requested terms or scoped occurrences are accounted for, concept/sense distinctions and evidence recoverable, alternatives and uncertainty explicit where consequential, no unearned approval or source change. If directly consulted, include one compact Answer Receipt with actual version/source delivery, used references, sources, checks/actions and limitations where appropriate; omit for exact machine-only results.
