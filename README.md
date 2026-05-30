# Rask · Record & Polish — Editor Prototype

Interactive high-fidelity concept for the **Record & Polish** feature — a new creation mode for [Rask.ai](https://rask.ai).

## What is this

A single-page interactive prototype of the main editor screen showing how AI-powered screen recording polish would live inside the Rask platform.

**Live demo:** open `index.html` in any browser (no build step, no dependencies).

## Feature concept

**Record & Polish** lets users record their screen via a Chrome extension and automatically get:
- 🎬 **Smart zoom** — auto-zooms on click targets using DOM bounding boxes
- ✂️ **Speech cleanup** — removes filler words ("um", "uh"), shortens pauses, detects retakes
- 💬 **Auto-captions** — transcript generated during cleanup, ready for localization
- 🌍 **One-click localize** — bridge to Rask's core dubbing pipeline (30 languages)

## Editor layout

```
┌─────────────────────────────────────────────────────────────────┐
│  Topbar: Rask logo · project name · aspect ratio · Before/After │
├──────────────────────┬──────────────┬──────────────────────────┤
│                      │              │                          │
│   Video preview      │  Transcript  │   Polish settings panel  │
│   (cinematic frame   │  (edit by    │   - Review summary       │
│    with auto-zoom    │   text, live │   - Speech cleanup       │
│    animation)        │   highlight) │   - Smart zoom           │
│                      │              │   - Cursor               │
│                      │              │   - Style & background   │
│                      │              │   - Captions             │
├──────────────────────┴──────────────┴──────────────────────────┤
│  Timeline: single track · waveform · zoom blocks · cut seams   │
└─────────────────────────────────────────────────────────────────┘
```

## Interactive features

| Feature | How to use |
|---------|-----------|
| Auto-zoom loop | Press Play — cursor animates to each click target with spring zoom |
| Before / After | Toggle in topbar — shows raw vs polished video + waveform |
| Zoom moments | Click any row in Smart zoom list or block on timeline to seek |
| Transcript sync | Active phrase highlights live during playback |
| Accordion sections | Click any section header in the Polish panel |
| Toggles | Speech cleanup / Smart zoom / Cursor — affect preview live |
| Aspect ratio | 16:9 / 9:16 / 1:1 — reframes canvas |
| Background presets | Style & background section |
| Design notes | "Show design notes" button bottom-right — 5 annotated rationales |

## Design decisions

1. **Auto-polish as "review", not silent magic** — we show exactly what was removed + time saved, with one-tap Undo. Builds trust before control.
2. **Retakes are opt-in** — fillers/pauses are safe to auto-cut; false-starts are riskier, flagged "needs review", off by default.
3. **Transcript in the panel, not the timeline** — editing by text is a sibling to AI settings, not a timeline operation. Keeps the single-track timeline simple.
4. **One lightweight timeline track** — audience = founders/marketers, not editors. No multi-track/layers.
5. **Bridge to Rask's core** — transcript already exists after cleanup → 30-language localization is one click. Two user streams meet at the artifact.
6. **Ship anywhere** — aspect-ratio switcher reframes the same declarative document to 16:9 / 9:16 / 1:1.

## Brand tokens (from Figma)

| Token | Value | Usage |
|-------|-------|-------|
| Primary blue | `#0B0BCF` | CTA buttons, toggles, accent |
| Secondary blue | `#3D3DE9` | Gradient, hover states |
| Muted blue bg | `#F5F5FF` | Active states, review card |
| Main text | `#101828` | All primary text |
| Secondary text | `#344054` | Labels, descriptions |
| Muted text | `#667085` | Hints, counts |
| Border light | `#EAECF0` | Panel dividers |
| Border medium | `#D0D5DD` | Input borders |
| Red | `#FF384C` | Danger, retake indicator |
| Font | Inter 400/500/600 | All UI text |
| Button radius | `12px` | Primary/secondary buttons |

## Context

This is a test assignment for a **Senior Product Designer** role at Rask.ai, implemented as a ShapeUp pitch + interactive prototype. Built in a single HTML file with vanilla CSS/JS and no external dependencies (except Google Fonts).

**Appetite:** 3-week cycle, one team, hypothesis validation (not final product).

**Target audience:** founder-marketer / growth generalist — record once, ship anywhere.
