---
name: Dawn Studio
description: Portfolio and front door for an independent software studio's app shelf and libraries.
colors:
  dawn-ember: "#E8590C"
  paper: "#f7f8f5"
  surface: "#ffffff"
  ink: "#111214"
  muted: "#555b62"
  hairline: "#c9cdd0"
  paper-dark: "#0d0e10"
  surface-dark: "#15171a"
  ink-dark: "#f4f5ef"
  muted-dark: "#b5bac0"
  hairline-dark: "#383c40"
  shelf-amber: "#f3a23b"
  shelf-coral: "#eb6048"
  shelf-blue: "#3d7df2"
  shelf-green: "#35a66f"
  shelf-violet: "#8458d8"
  shelf-teal: "#2e9c95"
  ray-red: "#E5484D"
  ray-yellow: "#FFD23F"
  ray-green: "#46A758"
  ray-blue: "#3E8EDE"
  ray-violet: "#8E4EC6"
  illustration-ink: "#101113"
  illustration-paper: "#f8f8f4"
typography:
  display:
    fontFamily: "Manrope, Noto Sans TC, sans-serif"
    fontSize: "clamp(3rem, 8.2vw, 6rem)"
    fontWeight: 700
    lineHeight: 0.88
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Manrope, Noto Sans TC, sans-serif"
    fontSize: "clamp(2.25rem, 5vw, 4.5rem)"
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: "-0.04em"
  title:
    fontFamily: "Manrope, Noto Sans TC, sans-serif"
    fontSize: "clamp(2rem, 4vw, 3.5rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.04em"
  lead:
    fontFamily: "Manrope, Noto Sans TC, sans-serif"
    fontSize: "clamp(1.125rem, 1.8vw, 1.25rem)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Manrope, Noto Sans TC, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "IBM Plex Mono, monospace"
    fontSize: "0.72rem"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0.08em"
  code:
    fontFamily: "IBM Plex Mono, monospace"
    fontSize: "0.82rem"
    fontWeight: 500
    lineHeight: 1.4
rounded:
  xs: "4px"
  sm: "6px"
  md: "8px"
  lg: "12px"
  xl: "16px"
  pill: "999px"
spacing:
  gutter: "16px"
  xs: "8px"
  sm: "12px"
  md: "18px"
  lg: "24px"
  xl: "32px"
  2xl: "44px"
  section: "64px"
  section-lg: "88px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: "48px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: "48px"
  button-secondary-hover:
    backgroundColor: "{colors.surface}"
  tag:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "8px 12px"
  lang-switch-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "5px 12px"
    height: "34px"
  library-card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.xl}"
    padding: "22px"
  install-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.code}"
    rounded: "{rounded.md}"
    padding: "8px 8px 8px 12px"
  project-visual:
    rounded: "{rounded.lg}"
    padding: "24px"
---

# Design System: Dawn Studio

## Overview

**Creative North Star: "First Light"**

The whole system hangs off the logo: a Dawn Ember sun sitting on a horizon, with rays that cycle through a spectrum. Everything else is the quiet morning around it: a cool off-white paper, near-black ink, hairline rules and monospace labels. Color is not spread across the chrome; it arrives the way light does, from one source, and lands on each app as its own hue on the shelf.

The mood is clean, direct and playful. The page itself is plain, ruled and typographic: huge tightly-tracked Manrope headlines, a mono meta line under each app name, and thin dividers that turn sections into a list. The play is concentrated in the per-app illustration cards (a spinning-feeling vinyl, a UFO over a green night sky, a Lo Shu number grid, stacked clipboard cards), each drawn in flat CSS shapes on that app's color. Components stay quiet and precise so those cards can carry the personality.

Light and dark are both first-class and follow `prefers-color-scheme`. EN and 繁中 share the same layout; Chinese gets looser line-height on display type.

**Key Characteristics:**
- One warm sun (Dawn Ember) as the only chrome accent; app hues live only on the shelf.
- Oversized, negative-tracked sans headlines over uppercase mono labels.
- Hairline-ruled sections; the page reads as a catalogue, not a grid of cards.
- Flat-shape CSS illustrations, one per app, each on its own color plate.
- Quiet, precise components: ink-filled or outlined, small radius, short eased transitions.

## Colors

A neutral paper-and-ink base lit by one ember-orange sun, with a separate set of shelf hues reserved for the apps.

### Primary
- **Dawn Ember** (`dawn-ember`): the sun in the logo, the accent word in display headlines ("Real life.", "No theatre."), the focus ring, and link hover color. The same value in light and dark.

### Secondary
- **Shelf hues** (`shelf-amber`, `shelf-coral`, `shelf-blue`, `shelf-green`, `shelf-violet`, `shelf-teal`): one per app, applied as `--project-color`: the plate behind the app's illustration, the dot in its meta label, and accents inside the illustration. Dark mode uses brighter versions (amber `#ffb34d`, coral `#ff715b`, blue `#6b9cff`, green `#52c28c`, violet `#aa84f2`, teal `#55bdb5`). A few apps use one-off values (`#3ddc84` for OpenMusic, `#c9563c`).

### Tertiary
- **Ray spectrum** (`ray-red`, `dawn-ember`, `ray-yellow`, `ray-green`, `ray-blue`, `ray-violet`): used only for the logo rays, which step through these colors on a 7s loop.

### Neutral
- **Paper** (`paper` / `paper-dark`): page background; also the `theme-color`.
- **Surface** (`surface` / `surface-dark`): raised fills: library cards, tags, the language switch track.
- **Ink** (`ink` / `ink-dark`): body text, primary buttons, strong rules (`--line-strong` is ink).
- **Muted** (`muted` / `muted-dark`): supporting copy, labels, meta lines.
- **Hairline** (`hairline` / `hairline-dark`): soft dividers, tag and card borders.
- **Illustration ink / paper** (`illustration-ink`, `illustration-paper`): fixed near-black and warm white used inside the app illustrations so they read the same in both themes.

### Named Rules
**The One Sun Rule.** Dawn Ember is the only accent in the page chrome. App hues stay on the shelf and never color navigation, buttons or section headings.

## Typography

**Display Font:** Manrope (with Noto Sans TC, sans-serif)
**Body Font:** Manrope (with Noto Sans TC, sans-serif)
**Label/Mono Font:** IBM Plex Mono (with monospace)

**Character:** A geometric-humanist sans set very large and very tight for headlines, against a small uppercase mono that labels and counts things like a catalogue.

### Hierarchy
- **Display** (700, `clamp(3rem, 8.2vw, 6rem)`, 0.88): hero and product-page h1. Tracking −0.04em. One accent phrase may take Dawn Ember.
- **Headline** (700, `clamp(2.25rem, 5vw, 4.5rem)`, 0.95): section heads ("The app shelf"). The studio note runs larger, up to 6rem.
- **Title** (700, `clamp(2rem, 4vw, 3.5rem)`, 1): app names, paired with a 44px app logo.
- **Lead** (400, `clamp(1.125rem, 1.8vw, 1.25rem)`, 1.55): hero and product pitch, muted, max ~610px.
- **Body** (400, 1rem, 1.55): app descriptions, max ~580px, muted.
- **Label** (500, 0.72rem, 0.08em, uppercase, mono): utility note, the app meta line set directly under the app name, sun label.
- **Code** (500–600, 0.82–0.95rem, mono): package names and install commands.

### Named Rules
**The Tight Display Rule.** Headlines track at −0.04em (the floor; never tighter) with line-height under 1 in English. In 繁中, display line-height opens to 1.08 and headlines to 1.15 so characters do not collide.

**The Mono Labels Rule.** Anything that labels, counts or categorises (meta lines under titles, numbers in illustrations) is IBM Plex Mono uppercase with wide tracking. Prose is never mono.

## Layout

A single centered column, `min(100% − 32px, 1180px)`, keeping a 16px gutter at every width. Sections are stacked full-width and separated by rules instead of boxes: a strong ink rule under the hero and section heads, hairline rules between apps.

- **Hero:** two columns (copy 1.15fr, sun 0.85fr), min-height 610px, 80px/64px vertical padding.
- **App shelf:** each app is a two-column row (copy + illustration, 1.08fr / 0.92fr), min-height 360px, alternating sides on even rows.
- **Libraries:** auto-fill grid, min column 300px, 18px gap.
- **Studio note:** headline beside a ruled principles list, 88px vertical padding.
- **Product route:** a hash-routed detail view per app that reuses the hero/illustration pattern.

Breakpoints: at 900px everything collapses to one column (illustration below copy); at 620px buttons go full width, the hero tightens and type clamps down. Vertical rhythm steps roughly 12 / 18 / 24 / 32 / 44 / 64 / 88px.

## Elevation & Depth

The page is flat: paper, surfaces and rules, no ambient shadows on chrome. Depth appears only in the illustration layer. App illustration cards carry a hard, unblurred offset shadow (8px 8px, ink at 22%), and the small paper objects inside them (clip cards, docs, queue rows) use smaller hard offsets of their own. Soft blurred shadows show up only inside illustrations to model physical objects (the vinyl, the UFO disc). This describes the current implementation, not a fixed rule.

### Shadow Vocabulary
- **Plate offset** (`box-shadow: 8px 8px 0 color-mix(in srgb, var(--ink) 22%, transparent)`): app illustration cards.
- **Object offset** (`box-shadow: 6px 6px 0 rgba(17,18,20,.15)` / `3px 3px 0 rgba(17,18,20,.13)`): paper objects inside illustrations.
- **Object lift** (`box-shadow: 0 14px 28px rgba(17,18,20,.16)`): mock windows inside illustrations.

## Shapes

Small, consistent radii on interactive pieces and larger radii on containers: 6px on buttons, 8px on the install bar and skip link, 12px on illustration plates and app logos, 16px on library cards, full pill on tags and the language switch. Borders are 1px (1.5px inside illustrations). Illustration content is built from circles, pills and rounded rectangles in CSS, with no raster art beyond the logos.

## Components

### Buttons
Quiet and precise.
- **Shape:** gently rounded (6px), 48px tall, 1px ink border.
- **Primary:** ink fill, paper text, weight 600.
- **Secondary:** transparent with ink border; fills with surface on hover.
- **Hover / Active:** lifts 2px on hover (0.5s ease-out-quint); scales to 0.98 on press.
- **Focus:** 2px Dawn Ember outline, 3px offset.

### Chips (tags)
- **Style:** pill, surface fill, hairline border, 0.75rem weight 600.
- **State:** static labels only; not interactive.

### Cards / Containers
- **Library card:** 16px radius, surface fill, hairline border, 22px padding; border goes to ink and the card lifts 2px on hover.
- **Install bar:** ink bar with paper mono text and a 32px ghost copy button (55% opacity, 100% on hover, turns green when copied).

### Navigation
- **Utility bar:** 64px tall, brand mark (40px logo, 12px radius) on the left, uppercase mono note, EN / 繁中 pill switch on the right. The active language is an ink-filled pill.
- **Links:** text links use a 1px bottom rule in currentColor; hover turns them Dawn Ember or lowers opacity. The "Open app" link's arrow nudges up-right on hover.

### App Illustration Plate (signature)
Each app on the shelf gets a plate: a 12px-radius card filled with the app's shelf hue, a 1px ink border and the plate offset shadow, holding a flat CSS illustration of what the app does (a vinyl and tonearm, a UFO over stars, a 3×3 Lo Shu grid, 简⇄繁 documents, currency rows, stacked clips, a holdings chart, an upvote queue, a fund ring). Illustration internals use the fixed illustration ink and paper so they look the same in both themes.

### Hero Sun (signature)
An enlarged inline-SVG logo: a static Dawn Ember sun on a horizon line, with rays whose stroke steps through the ray spectrum one color per second in a clockwise wave. Because the change is color only, it keeps running under reduced motion.

## Do's and Don'ts

### Do:
- **Do** keep Dawn Ember as the single chrome accent: the headline accent word, the focus ring, link hover.
- **Do** give every new app a shelf hue, a mono meta line with a matching dot, and a flat CSS illustration plate.
- **Do** separate sections with rules (strong ink under section heads, hairline between items) instead of wrapping them in boxes.
- **Do** ship every string in EN and 繁中, and check the 繁中 line-heights on display type.
- **Do** define colors as tokens with dark-mode counterparts; illustration internals use the fixed illustration ink and paper.
- **Do** honor `prefers-reduced-motion`: scroll reveals and transitions turn off, and only the color-only ray cycle keeps running.

### Don't:
- **Don't** put a label or eyebrow above a heading; category and platform lines go under the title.
- **Don't** number list items (01, 02…) unless the order carries meaning.
- **Don't** use app shelf hues on navigation, buttons or section headings.
- **Don't** set prose in IBM Plex Mono or set labels in Manrope.
- **Don't** draw the sun's rays as alternating red-and-white bands radiating to the edges. Keep them as short spectrum strokes above the horizon.
- **Don't** add soft blurred shadows to page chrome; depth stays in the illustrations.
