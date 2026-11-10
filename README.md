# Check Desk

A factual, verified local directory of check-cashing, money-order, bill-pay, and prepaid-reload locations, written for unbanked and underbanked users and for people who need service after typical bank hours.

This repository is the source of truth for the site. **Step 2 (scaffolding) is in progress.** Pages are marked DRAFT. No Denver listings have been collected yet. The GitHub remote is not connected from this checkout; see [docs/REMOTE-SETUP.md](docs/REMOTE-SETUP.md).

Owner: Richard Casey. Hard rules: use only public sources; never contact businesses; never sign up for affiliate programs or spend project money; never present content as financial advice; every data point needs a source URL and a last-verified date.

## Layout

```
site-src/             static site generator (Python 3, standard library only)
  build.py
  site.config.json    placeholder base URL; no analytics token
  src/layout.html     shared chrome, including the site-wide disclaimer
  src/partials/       disclaimer.html (injected into every built page)
  src/pages/          page bodies (DRAFT placeholders)
  src/assets/         CSS
  src/static/         favicon and 404.html
docs/                 PLAN.md, research, remote-setup notes
data/schema/          locations and fees schemas, plus an example-only CSV
CHECKLIST.md          future S3 + CloudFront deploy steps (placeholders only)
```

## Build

From the repo root:

```sh
python3 site-src/build.py
```

Preview output goes to `site-src/public/` (gitignored). To write somewhere else:

```sh
python3 site-src/build.py --out /tmp/checkdesk-preview
```

Then: `python3 -m http.server 8787 --directory site-src/public`

`site.config.json` uses the placeholder base URL `https://checkdesk.example/`. Override it with `SITE_BASE_URL` when a real domain exists. Leave `cf_analytics_token` empty unless Richard later adds a public analytics token.

## Related

Planning from Step 1, plus Step 2 refinements, lives in [docs/PLAN.md](docs/PLAN.md). Working notes from the planning pass also remain at `/workspace/checkdesk/` on the shared box.
