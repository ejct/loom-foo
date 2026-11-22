# First-use evaluation and actual scope

**Fixture status:** The cases in `cases.jsonl` are candidate prompts/oracles, not executed model runs. `PRV-INITIAL-` identifies original `PROBES.jsonl` scenarios; `PRV-REPORT-` identifies the later model-only report. Same numeric suffixes across these prefixes denote different cases.

## When an appropriate agent runtime is available

1. Freeze the exact installed version/hash of `loom-foo-editorial-review` and its enabled environment.
2. For each selected case, send the prompt as real conversation turn(s); multi-turn tests must be **separate actual messages**, not a simulated joined paragraph. Preserve all output unedited.
3. Keep the test's expected behavior out of the executing agent's prompt (blind where meaningful); evaluate afterwards against an expert-reviewed oracle.
4. Record: `case ID | runtime | model/skill version | date | real input/turns | raw output | PASS/FAIL/MIXED | violated invariant | uncertainties`.
5. Run adjacent negative routing checks: new essay from scratch → drafting; reorganize argumentative arc → narrative design; review spelling/style of existing text → editorial review. Observe actual skill selection; fixture labels alone do not measure discovery.
6. For exact URL/code/quoted strings use `scripts/check_invariants.py` against the **actual output**. For JSON parse with a real JSON parser, and check semantic preservation separately. Check meaningful language decisions with a competent normative oracle; do not equate substring matching with correctness.

## Scope limits of this local candidate

Static test suite validates formatting, unique fixture IDs, internal contracts and a deterministic helper with both passing and deliberately failing mutations. It does not call the original GPT, invoke ChatGPT's plugin router, independently evaluate language quality, test a separate agent context, or prove a comparative benefit. First-use observations performed manually within the authoring context must be recorded as `SAME_CONTEXT_DOGFOOD` and are not automatic routing tests.
