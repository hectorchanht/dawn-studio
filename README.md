# Dawn Studio

The portfolio site for [dawnstudio.app](https://dawnstudio.app) — Dawn Studio, an independent software studio.

A single self-contained static site: `index.html` plus its icons, PWA and SEO files. No build step.

## Structure

- `index.html` — the whole site (EN / 繁中）
- `privacy.html`, `404.html`
- `sw.js`, `site.webmanifest`, `robots.txt`, `sitemap.xml` — PWA + SEO
- `logo.png`, favicons, `icon-maskable-*`, `android-chrome-*` — brand icons
- `project-logos/` — logos for the apps in the shelf

## Deployment

Deployed to Cloudflare Pages (project `dawn-studio`) by direct upload — pushing this repo does not deploy the site. The deployed file set is exactly the files in this repo root (plus `project-logos/`).
