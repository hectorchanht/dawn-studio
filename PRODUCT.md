# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

dawnstudio.app is the official place Hector Chan points people to when showing Dawn Studio's work. One page serves several audiences, all arriving from a link someone shared:

- **App users** — people looking for, or sent to, one of the apps; they want to find it and open it.
- **Developers** — people looking at the `@dawn-studio/*` npm libraries and their GitHub repos.
- **Collaborators / employers** — people assessing the studio's range and the builder behind it.
- **Press / community** — people introducing or sharing the studio and its apps.

## Product Purpose

A portfolio and front door for Dawn Studio, an independent software studio. It presents the app shelf (each app solving one clear problem, usable in the browser) and the open-source libraries extracted from those apps, and sends visitors on to the right destination. Success: whoever was handed the link understands what the studio makes and reaches the app, package or contact they came for.

## Positioning

A single independent builder shipping a shelf of focused, real, working apps across very different domains (music, currency, clipboard, portfolio tracking, live Q&A, investment education, Chinese fortune-telling, script conversion, UFO archive), plus the reusable libraries pulled out of them. Breadth of shipped, usable work from one studio is the claim.

## Operating Context

- Visitors usually arrive from a shared link (shown to someone in person, sent in chat, posted, or on a CV/profile).
- Every app links out to its own site; this page does not host app functionality.
- Libraries are installed with npm; each card links to npm and GitHub.
- Contact route is hectorchan.com (per `privacy.html`).

## Capabilities and Constraints

- Current apps: OpenMusic (Web + Android), RealUFO (Web + REST API + MCP), 洛書命理 / Numerology, ZhConvert, MoneyRate, ClipBin, Holdr, OpenQ, Pennyvest.
- Current libraries: `@dawn-studio/auth`, `zh-convert`, `pronounce`, `ai-cache`, `drag-scroll`, `theme`.
- Current implementation: one self-contained static `index.html` (plus `privacy.html`, `404.html`, PWA/SEO files), no build step, deployed to Cloudflare Pages by direct upload. This is the existing setup, not a stated commitment.
- Analytics: Cloudflare Web Analytics, cookieless. The site has no accounts, forms or personal-data collection (`privacy.html`).
- **Pricing model: core features free, some features may be paid.** The current meta/OG description ("free tools for everyone — no ads, no paywalls, no sign-up walls") overstates this and should be reconciled; do not repeat "no paywalls" claims.

## Brand Commitments

- **Bilingual EN + 繁中 (Traditional Chinese) is required.** Both languages are first-class; every piece of copy ships in both.
- Name: Dawn Studio. Existing logo (`logo.png`) and favicons are current assets; the user did not mark them as binding.
- Current copy describes the studio as one person ("One builder. Useful software. No theatre.") with principles Useful first / Honest by default / Priced fairly / Built to stay simple. Not confirmed as fixed commitments.

## Evidence on Hand

- App logos in `project-logos/`; studio logo and icon set at repo root.
- Real, live apps and published npm packages listed above.
- No testimonials, user counts, press coverage or metrics are on hand. Do not invent them.

## Product Principles

1. Route fast: every audience should reach its destination (an app, a package, the builder) within a glance.
2. Show the work, not claims about it: the shipped apps and libraries are the proof.
3. Stay honest about pricing and scope; no blanket "free forever" or unverified numbers.
4. Two languages, one quality bar: nothing is English-only or Chinese-only.
