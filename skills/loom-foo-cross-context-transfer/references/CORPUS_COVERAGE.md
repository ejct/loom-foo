# Corpus Coverage Contract

Coverage is task-relative: guarantee completeness only against an explicitly defined corpus/surface/search protocol.

## Manifest

For each artifact track:

```yaml
source_id:
title:
path_or_url:
source_class:
version_or_revision:
authority_or_status:
included:
exclusion_reason:
coverage:
task_disposition:
notes:
```

## Coverage states

`FULL_REVIEWED | PARTIAL | METADATA_ONLY | FAILED | EXCLUDED`

Search snippets, sampled chunks, capped listings, and truncated responses are never `FULL_REVIEWED` unless followed up.

## Task dispositions

`MATERIAL | POSSIBLY_MATERIAL | NO_MATERIAL_RELEVANCE | SUPERSEDED | CONTRADICTORY | UNRESOLVED`

Every in-scope artifact needs a disposition before closure.

## Internal projects

Prefer an explicit project/document census and authority map. `EXHAUSTIVE_IN_SCOPE` requires a closed declared corpus and material-reference frontier.

## Public repositories

Declare reviewed surfaces, e.g. docs, ADRs, examples, architecture-relevant code paths, relevant tests, bounded issue/PR searches. Use `DECLARED_SURFACE_COMPLETE`.

## Research

Record search sources/databases, queries, date range, inclusion/exclusion criteria, screened set, deep-read set, and inaccessible material. Use `SEARCH_PROTOCOL_COMPLETE`.

## Mutable identity

Capture file revision/modified timestamp, repository commit/tag, publication/spec version, and retrieval date when material.

## Material-reference frontier

Follow only references that can materially change authority/currentness, rationale, evidence, failure history, supersession, or transfer conclusion.

## Target coverage

Use two passes:

1. independent target preflight;
2. concern expansion after Transfer Units exist.

Do not conclude the target lacks something without inspecting the relevant target concern.

## Closure questions

- What corpus/surfaces were in scope?
- Does every item have coverage state and task disposition?
- What remains partial/unavailable?
- Any unresolved material references?
- Which target concerns were inspected?
- What exact completeness claim is justified?
