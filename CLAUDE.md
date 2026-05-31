# Figma Design Project — Rask · Record & Polish

- **Figma file:** https://www.figma.com/design/atkrZzP4H5zld4zrzO9yV3/Rask.ai?node-id=0-1
- **Target page/node:** `0:1` — create new frames here, do NOT modify existing designs on the page.
- **Source of truth:** the local prototype `index.html` in this repo (open via the preview server on :4599). It is the exact spec — match its light theme, layout, and states.
- **Fonts:** [leave blank — Preflight auto-populates from Design System Variables]
- **Session goal:** Transfer the Record & Polish editor — *all states* — into the file as clean, on-spec frames bound to the Rask design system.

## Rules (claude2figma harness)

1. Every visual value must bind to a Style or Variable. Never hardcode colors, font sizes, or spacing.
2. Always search connected libraries before building any component from scratch (library-first).
3. Never start designing before the Design Brief is confirmed.
4. Build one frame (state) at a time; pause for review before the next.

## Brand tokens already extracted from this file (use as the binding target)

- Primary/brand blue `#0B0BCF`, secondary `#3D3DE9`, deep `#0909A2`, muted bg `#F5F5FF`
- Text `#101828` / `#344054` / `#667085`; borders `#EAECF0` / `#D0D5DD`; red `#FF384C`
- Font: Inter (Medium 500 / Semi Bold 600); button radius 12px
- (Confirm/replace with the file's real Styles & Variables during preflight.)

## States to build (each = its own frame, 1440×900 desktop)

1. **Editor — default** (light theme, "After" mode, transcript panel open, an auto-zoom active on a click target, running word-highlight in transcript).
2. **Before vs After** — raw recording (greyed waveform, removed regions visible, 3:12) vs polished (2:25). Two frames or a variant pair.
3. **Smart zoom — manual** — a custom zoom added at the playhead: per-zoom editor (Zoom level / Duration), draggable focus-point dot on the preview, manual block on the timeline.
4. **Retake review (inline in transcript)** — 3 sub-states: (a) pending candidate ("⟳ 1st / 2nd / both" pill, NEEDS REVIEW), (b) removed (false start struck, REMOVED, timeline cut), (c) kept both.
5. **Transcript navigation** — Loom-style: per-line timecode gutter, hover-time tooltip on a word, current-word highlight.
6. **Design notes overlay ON** — the 5 annotated rationale callouts over a dimmed canvas.
7. **Aspect ratios** — canvas reframed to 16:9 / 9:16 / 1:1 ("ship anywhere").
8. **Transcript collapsed** — preview at full width, Polish panel only.

## Prototype reference assets

- `index.html` — full implementation (CSS variables at top map 1:1 to the tokens above).
- Live screenshots can be captured from the preview server (`.claude/launch.json` → `rask-concept`, port 4599).
