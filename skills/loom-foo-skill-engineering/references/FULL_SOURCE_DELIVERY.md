# Complete source delivery through output-limited tool channels

Scope: An inner source reader successfully returned the file but an outer result channel could clip what the model receives. This is an operational fallback for a selected required source, not a universal ChatGPT SessionStart hook.

## ChatGPT Code Mode

Use a bounded range per functions.exec tool invocation, with the same exact URI. This example must be adapted to the current file and start offset:

    const URI = "skills://plugins/loom-foo/loom-foo-skill-engineering/skill.md";
    const START = 0;    // then previous output END
    const SPAN = 8500; // illustration, not a guaranteed platform limit
    const r = await tools.skills__read({uri: URI});
    const raw = r[0].content;
    const footer = raw.indexOf("\n---\nAvailable file URIs");
    const body = footer < 0 ? raw : raw.slice(0, footer);
    const end = Math.min(body.length, START + SPAN);
    if (START < 0 || START > body.length) throw Error("invalid source range");
    text("SOURCE " + URI + " [" + START + "," + end + ") / " + body.length + "\n" + body.slice(START, end));
    if (end === body.length) text("END_OF_SOURCE");

Repeat in a NEW invocation with START set to the previous END until END_OF_SOURCE is visible. If any output itself is truncated, reduce SPAN and repeat the affected range. An inner reader returning total length N does not prove the complete body was forwarded. Do not aggregate many large files in one output. For conditionally required references, read each separately and fully; the available-file index is metadata, not reference content.

## Other runtimes

Use a native paged reader and next_cursor when actually supported. Do not assume a Codex tool is available in ChatGPT. Keep source identity bound to a release/commit across pages when possible.

## Evidence boundary

Source retrieval, model-visible output delivery and compliance with the instructions are different evidence layers. Confirming contiguous emitted ranges supports delivery but cannot by itself establish model comprehension or behavior. Do not claim host-level reliability from this procedure. Keep private source bodies within the authorized execution context; do not publish them to generic logs or fixtures.
