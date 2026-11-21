# Source Intake handoff (optional, compact)

This is a lightweight source-context note passed to an analysis skill, not a mandatory persistent schema or new global object.

```yaml
source_identity:
  canonical_url: "https://www.youtube.com/watch?v=EXAMPLE0000"
  source_type: youtube_video
  title: null             # fill only when verified
  creator: null           # fill only when verified
acquisition:
  method: "connected transcript provider"  # observed, not assumed
  retrieved_at: null      # UTC timestamp if needed
  content_kind: transcript
  source_track: auto_captions
  language: uk
coverage:
  text: FULL_TRANSCRIPT  # or PARTIAL_TRANSCRIPT/METADATA_ONLY/UNAVAILABLE
  visual: NOT_INSPECTED
  failures: []
result:
  content_ref: null       # bounded text or actually accessible pointer
  requested_task: summarize
  source_timestamps: []
permissions:
  external_transfer_permitted: false
  persistence_permitted: false
```

## Status mapping from historical link-intake proposal

Retain historical display statuses `FULL_TRANSCRIPT`, `PARTIAL_TRANSCRIPT`, `METADATA_ONLY`, `UNAVAILABLE` for backward-compatible YouTube summaries, but do not confuse them with complete multimedia evidence. Add an orthogonal visual coverage indicator. Underlying classification must distinguish provider blocked, video not found, no captions, and untested status.

## Routing examples

- Bare YouTube watch URL → identify exact video, retrieve subtitles if viable, provide bounded useful overview; mark visual coverage.
- "Analyze architecture in this product demo" + URL → transcript as one evidence layer; visual inspection needed or warn explicitly.
- A supplied full transcript → no link-intake; direct analysis.
- A user-uploaded .m4a → `loom-foo-audio-transcription` owns execution only when separately installed; otherwise mark transcription unavailable and preserve the supplied file/source without uploading it elsewhere.
- Private Google Doc URL → connected Google Drive/Docs action rather than public scraping.
- "Add insights from this video to knowledge index" → acquire source here; knowledge index intake owns bounded admission/authority after source acquisition.
- A video URL with `list=` + `v=` → the individual video is the primary referent, not the whole playlist.
- A playlist URL → scoped collection; no unapproved wholesale processing.
