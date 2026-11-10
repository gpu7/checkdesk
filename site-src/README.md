# Check Desk site source

This folder is the source of the Check Desk static site. Preview builds go to `public/` (gitignored). Don't edit the output by hand. Edit the files here and rebuild.

The intended production domain is **checkdesk.com** (decided 2026-11-10). Registration and ownership are still Richard's step and are unconfirmed. `site.config.json` uses `https://checkdesk.com/`. You can still override it with `SITE_BASE_URL` at build time.

## Build

Requirements: Python 3.8 or newer, standard library only.

From the repo root:

```sh
python3 site-src/build.py
```

- Without `--out`, the output goes to `site-src/public/`, which is git-ignored. Preview with `python3 -m http.server 8787 --directory site-src/public`.
- The output directory is deleted and fully rebuilt on every run.
- The build is deterministic. Dates come only from each page's `"lastmod"` meta, from `default_lastmod`, or from `disclaimer_updated` in `site.config.json`, never from the clock.

The builder also writes `sitemap.xml` and `robots.txt`, and it fails if the site-wide disclaimer is missing from `layout.html` or from any output HTML file (including the static 404).

## Layout

```
build.py            the builder
site.config.json    base_url (https://checkdesk.com/), default_lastmod, disclaimer_updated, cf_analytics_token (leave empty)
src/layout.html     shared header, nav, footer, and {{disclaimer}}
src/partials/disclaimer.html   the site-wide disclaimer block
src/pages/          page bodies, each starting with <!--meta {...} -->
src/assets/         style.css (link gets ?v=<sha256 prefix> for cache-busting)
src/static/         copied to the site root (favicon, 404.html)
```

How pages map to URLs:

| Source | URL | Output file |
|---|---|---|
| `src/pages/index.html` | `/` | `public/index.html` |
| `src/pages/about.html` | `/about/` | `public/about/index.html` |
| `src/assets/*` | `/assets/*` | `public/assets/*` |
| `src/static/*` | `/*` | `public/*` |

Page `schema` values: `website` (WebSite JSON-LD), `article` (Article, BreadcrumbList, and FAQPage from on-page `<details>` FAQs), `collection`, or `page` (no JSON-LD).

## Fact rules (every page)

1. **Sourced figures only.** Every price, fee, limit or service claim comes from the provider's or agency's official page, with a citation that links to it.
2. **Last-verified dates.** Each published figure and each location row carries a last-verified date. Location rows also have a required `verification_status` (`unverified`, `policy_only_call_ahead`, `verified_official_locator`, or `verified_official_store_page`).
3. **No invented data.** If there's no published national price, write that and say why. Never estimate or average prices.
4. **Examples are labeled.** A single store is an example, never national policy. Example CSV rows set `is_example=true` and must not be published.
5. **Not financial advice.** The site-wide disclaimer appears on every page. City and guide pages also carry the longer affiliation / no-advice note.
6. **No affiliate programs** unless Richard later approves a disclosed change. No placeholder commercial links.
7. **Stable URLs.** Never change a URL after launch; add a redirect instead.

## Deploy

Hosting matches Errand Desk: a private S3 bucket served only through CloudFront, with DNS at Cloudflare in **DNS-only** (not proxied) mode. See the repo-root [CHECKLIST.md](../CHECKLIST.md) and [docs/HOSTING-HANDOFF.md](../docs/HOSTING-HANDOFF.md). Do not create AWS resources or change DNS until Richard approves those steps.

After a fresh `python3 site-src/build.py`:

1. Upload the contents of `site-src/public/` (or another `--out` directory) to the private S3 bucket with explicit Content-Type and Cache-Control. HTML, `sitemap.xml`, and `robots.txt` get 5 minutes; fingerprinted assets (`assets/*`, including `style.css` with `?v=`) and `favicon.svg` get one year, immutable.
2. Invalidate `/*` on the CloudFront distribution and wait for it to complete.

An optional, untested helper is [`scripts/deploy.sh`](../scripts/deploy.sh). It reads `CHECKDESK_BUCKET` and `CHECKDESK_DISTRIBUTION_ID` from the environment and hardcodes no IDs. Bucket names, account IDs, and distribution IDs stay out of this repository.

Optional Cloudflare Web Analytics: leave `cf_analytics_token` empty for no script. If Richard later creates a site in the Cloudflare dashboard, paste the public site token, rebuild, re-upload, and invalidate.
