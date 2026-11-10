# Check Desk — Step 1 site plan (planning only)

**Project:** Check Desk, a factual, verified local directory of check-cashing, money-order, and bill-pay locations, focused on unbanked/underbanked and after-hours users.  
**Owner:** Richard Casey (Fort Collins, CO; timezone America/Denver).  
**Status:** Step 2 of 8 (local repo scaffolding). Step 1 plan approved 2026-11-10. Local git repo: `/workspace/checkdesk-repo`. No GitHub remote has been created or pushed from this checkout. No listings collected. No businesses contacted. No affiliate signups. No money spent.  
**Plan date:** 2026-11-10 (America/Denver).  
**Pilot market (confirmed):** Denver / Denver metro — not Fort Collins.

This document is a proposal for human review. It does not collect or publish Denver listings. Fee figures below appear only when an official page was opened for this step, with the URL and the date it was checked. Anything else is marked TODO.

Related Step 1 research:

- [research/step1-scope.md](research/step1-scope.md) — services in and out of scope
- [research/step1-competitors.md](research/step1-competitors.md) — public competitor scan
- [schema/locations.schema.json](schema/locations.schema.json), [schema/locations.csv](schema/locations.csv), [schema/fees.schema.json](schema/fees.schema.json)

---

## 1. What already exists (Errand Desk) and what to reuse

Canonical source of truth for https://erranddesk.com:

- **Repo / builder:** `/workspace/mogul/erranddesk-repo/site-src/`
- **Built output (do not hand-edit):** `/workspace/mogul/erranddesk-repo/erranddesk-site/`
- **Deploy / AWS checklist:** `/workspace/mogul/erranddesk-repo/CHECKLIST.md` (S3 + CloudFront + Route 53; Richard performs paid AWS/domain steps)
- **Working notes / city drafts (not the live source of truth):** `/workspace/mogul/` (per-state and per-city draft folders, including `/workspace/mogul/denver/` with `facts.md` and raw fetches in `f/`). Filename hits for "errand" also appear under `/workspace/backups/`; treat those as backups, not the live tree.

**Stack.** A tiny Python 3 standard-library static generator (`build.py`). No JS framework. Pages are HTML bodies in `src/pages/` that start with `<!--meta {"title","description","nav","lastmod","schema"} -->` and are wrapped in `src/layout.html`. `site.config.json` holds `base_url`, `default_lastmod`, and an optional Cloudflare Web Analytics token. The build is deterministic: dates come from each page's `lastmod` (or the config default), never from the clock. It also writes `sitemap.xml`, `robots.txt`, and `assets/search-index.json`. Search is client-side on `/` and `/search/` only. Deploy pattern is S3 + CloudFront, documented in the repo README and CHECKLIST.

**Page types and URL scheme already in production:**

| Type | Live URL pattern |
|---|---|
| Home | `/` |
| Guides index and guides | `/guides/`, `/guides/<slug>/` (includes `/guides/money-orders/`) |
| City guides | `/<city-slug>/` (disambiguate with a state suffix when needed, e.g. `/aurora/` vs `/aurora-il/`) |
| Map, search | `/map/`, `/search/` |
| About, disclosure, privacy, contact | `/about/`, `/disclosure/`, `/privacy/`, `/contact/` |

**How listings and verification are shown.** City and guide pages are sourced prose and tables, not a row-per-location database. Every price or service claim has a numbered citation. A page-level line reads "All figures last checked \<date\>" (HTML `<time datetime>`). The Sources list repeats "(last checked \<date\>)" on each item. Franchise or single-store prices are labeled as examples, not national prices. "No national price published" is used instead of guesses. City pages carry a "Not affiliated, not legal advice" note; the money-order guide also says the page is general information, not legal or financial advice, and to confirm fees before you go.

**SEO.** Every page gets a canonical URL, Open Graph, and Twitter card tags. JSON-LD: `WebSite` on home; `Article` + `BreadcrumbList` + `FAQPage` (built from on-page `<details><summary>` FAQs) on article/city pages; `CollectionPage` on collection pages.

**Monetization placements on the live site.** Footer and about/disclosure pages state: no ads, no popups, no paid rankings. Some links are affiliate links, each marked `(paid link)` with `rel="sponsored nofollow noopener"`. Disclosure last updated Oct 26, 2026 names Notarize (Proof) and iFax as current possible commissions, plus optional Ko-fi tips. Commissions must not change facts, prices, or sort order. Check Desk's hard rules are stricter: do not sign up for affiliate programs or spend money on this project. Do not copy Errand Desk affiliate links or tip buttons onto Check Desk unless Richard later approves a separate, disclosed model.

**Reusable for Check Desk (recommended):** the static Python builder, layout/CSS, meta + lastmod discipline, fact rules in `site-src/README.md`, JSON-LD/FAQ pattern, sitemap/robots/search, "last checked" and numbered-sources display, disclaimer tone, and the existing money-order research (USPS, Walmart, Western Union, MoneyGram) as a starting point — re-check official pages before reuse. `src/data/cities.json` already stores Census Gazetteer coordinates for Colorado places, which can seed city-page maps later. The Denver Errand Desk city page is a template for voice and source-list structure, not a source of check-cashing listings (it only covers USPS money-order fees at the national level).

**Do not blindly reuse:** affiliate/Ko-fi placements; Errand Desk brand strings and analytics token; the city-page body files (wrong niche); OSM-style third-party location dumps; any "typical fee" ranges that are not on an official page.

---

## 2. Proposed site map and URL scheme

Proposed production host is a separate site (working name Check Desk). Domain is an open question for Richard. URL patterns below follow Errand Desk: trailing slashes, stable slugs, state suffixes only when two cities would collide.

### Global and utility

| URL | Page |
|---|---|
| `/` | Home: what the site is, fee snapshot (sourced official national/max fees only), cheapest-first framing, link to Denver pilot, how we verify, disclaimer |
| `/about/` | Method: public sources only, last-verified policy, no financial advice, no business outreach |
| `/disclosure/` | How (or whether) the site makes money. At launch: no ads, no paid rankings, no affiliate programs |
| `/privacy/` | Privacy policy (reuse Errand Desk structure, new site name) |
| `/contact/` | Corrections inbox; do not use this to contact listed businesses on the user's behalf |
| `/search/` | Client-side search, same pattern as Errand Desk |
| `/map/` | Optional after the Denver dataset exists; not required for the first published pages |

### Guides (national / Colorado facts, not a store list)

| URL | Page |
|---|---|
| `/guides/` | Guide index |
| `/guides/check-cashing-fees/` | Official published fees and limits (Walmart, King Soopers/Kroger Money Services, ACE "menu board / varies", etc.). Lower-fee options first. "No national price published" where true |
| `/guides/money-orders/` | USPS, Walmart, Western Union, MoneyGram. Can start from Errand Desk's guide after a fresh official-page check |
| `/guides/bill-pay/` | In-store bill pay: what official pages say about stubs, payment methods, and fees (often "varies / ask at the desk") |
| `/guides/prepaid-reload/` | Where official pages say you can reload prepaid cards; CFPB fee-type explainer (not a product endorsement) |
| `/guides/after-hours/` | How we define after-hours, how the flag is set, and how to use the Denver after-hours view |
| `/guides/lower-fee-options/` | Side-by-side of options that official pages actually price (own bank, issuing bank *if* the bank publishes a policy — do not invent a legal duty), grocery money desks, USPS, Walmart vs stores that do not post a national fee |

### Geography (pilot first)

| URL | Page |
|---|---|
| `/denver/` | Denver metro hub: services overview, lower-fee snapshot, after-hours jump link, location list grouped by service and by brand, sources |
| `/denver/check-cashing/` | Denver-area check-cashing locations only |
| `/denver/money-orders/` | Denver-area money-order sellers |
| `/denver/bill-pay/` | Denver-area bill-pay desks |
| `/denver/after-hours/` | Locations whose published hours fall outside the after-hours definition below |
| `/aurora/`, `/lakewood/`, `/commerce-city/`, … | Add metro city pages only after the Denver hub listing set is reviewed. Reuse Errand Desk slug rules (`/aurora/` is Colorado unless a collision requires a suffix) |

Do not create thin city pages that only repeat national fees. A city page goes live when it has verified local locations (or an explicit, sourced statement that a given brand has no official locator result in that city).

### Provider pages (policy and fees, not every store)

| URL | Page |
|---|---|
| `/providers/` | Index of brands we cover |
| `/providers/usps/` | Official money-order fees, cashing rules, locator pointer |
| `/providers/walmart/` | Official check-cashing and money-order fee language; store-finder pointer |
| `/providers/king-soopers/` | Official Money Services pages (fees vary by state) |
| `/providers/western-union/` | Official "varies by location" language; location-finder pointer |
| `/providers/moneygram/` | Official US limit language; location-finder pointer |
| `/providers/ace-cash-express/` | Official "menu board, varies by state" language; locator pointer. Do not promote payday or title loans |

No per-store vanity URLs in the pilot (`/denver/walmart-example-st/` is later, if needed). The city page plus a data row is enough for v1.

### After-hours definition (proposed)

A location is `after_hours=true` when *any* published service window is outside **Monday–Friday, 09:00–17:00 America/Denver** (typical bank hours), including Saturday, Sunday, or a weekday open after 17:00 or before 09:00. Also store the raw weekday hours and separate flags (`open_saturday`, `open_sunday`, `open_after_1700_weekday`) so the after-hours page can filter precisely. If hours are not published on an official or locator page, leave hours empty, set `after_hours` to unknown/null, and say so — do not guess.

---

## 3. Page templates

Mirror Errand Desk templates, with directory cards added.

**Shared chrome.** Skip link; brand + short tagline; nav (Guides, Check-cashing fees, Money orders, Bill pay, After hours, About); footer with method blurb, no-financial-advice line, disclosure/privacy/contact; optional analytics only if Richard later supplies a token.

**Home.** One-sentence purpose; disclaimer; fee snapshot table copied from official wording (not averages); last-checked dates and source links; "pilot: Denver metro"; links into guides and the Denver hub.

**Guide.** Kicker (`Guide · <topic> · All figures last checked <date>`); disclaimer box; short version; comparison table that quotes official pages; "what to bring"; FAQ as `<details>` so FAQPage JSON-LD cannot drift; numbered Sources list.

**City / after-hours.** Kicker with city name and last-checked date; disclaimer; short version that favors lower-fee options first; filters (service, after-hours, brand); location cards from `locations.csv` (name, address, public phone, services, hours, fee notes + fee source, last verified, confidence); a clearly labeled "example / not yet verified" state must never appear on a published page; sources.

**Provider.** National or chain-wide official policy; locator link; "fees may differ by store"; no invented ranges.

**Disclaimer / no-financial-advice wording (draft, for review):**

> **Not financial advice, not affiliated.** Check Desk is an independent information site. It is not a bank, money transmitter, check casher, or financial adviser, and it is not affiliated with USPS, Walmart, King Soopers, Western Union, MoneyGram, ACE Cash Express, the CFPB, the FDIC, the State of Colorado, or any business it lists. This site is general information, not financial, legal, or tax advice, and not a recommendation to use or avoid any product, loan, or account. Fees, hours, ID rules, and services change and can differ by location. Confirm with the official source or the location before you go. We do not promote payday loans, title loans, or other credit products.

**How "last verified" is displayed (draft):**

- Page kicker: `All figures last checked <time datetime="YYYY-MM-DD">Mon D, YYYY</time>`.
- Each source line: `(last checked Mon D, YYYY)` plus the official URL.
- Each location card: `Last verified YYYY-MM-DD` · `Verified by <initials or agent name>` · `Confidence: high|medium|low`.
- If a fee is a chain-wide maximum, say so ("Walmart published maximum, not this store's till").
- Proposed recheck: fees and hours at least every 90 days, or sooner if an official page changes. A build warning (not a public scare banner) should flag rows older than 90 days before publish.

**SEO (proposed, same as Errand Desk):** unique title and description; canonical; OG/Twitter; JSON-LD `WebSite` on home, `Article` + `BreadcrumbList` + `FAQPage` on guides and city pages, `LocalBusiness` or `FinancialService` only if a listing's address and hours were taken from an official locator and are not example data. Do not emit LocalBusiness markup for unverified rows.

---

## 4. Pilot market and why Denver metro

**Pilot: Denver / Denver metro**, as confirmed for this step, consistent with prior Errand Desk work.

Reasons:

- Errand Desk already has a mature Denver city page and many adjacent Colorado metro pages (Aurora, Lakewood, Thornton, Arvada, Westminster, Commerce City, Littleton, Centennial, and others), plus a reusable voice, source style, and Census coordinates.
- Official chain pages relevant to this metro were available to cite without any outreach: Walmart, King Soopers Money Services (Kroger family; King Soopers is the Colorado banner), USPS, Western Union, MoneyGram, ACE Cash Express.
- A denser mix of grocery money desks, supercenters, post offices, and after-hours storefronts makes a lower-fee vs after-hours comparison meaningful in one market.
- Richard is in Northern Colorado (America/Denver), so rechecks and spot-checks of public pages can happen in-zone. Fort Collins can be a later city, not the first dataset.

**Proposed first-publish geography (for review, no listings yet):**

1. City and County of Denver (the `/denver/` hub).
2. Inner-ring cities that official locators often return alongside Denver and that Errand Desk already treats as Front Range cities: Aurora, Lakewood, Commerce City, Englewood, Wheat Ridge, Federal Heights. Other metro cities (Arvada, Westminster, Thornton, Littleton, Centennial, Boulder, etc.) wait until the first set is reviewed.

Colorado-level sources (DORA Division of Banking, money-transmitter rules, CFPB, FDIC) apply to the whole pilot, not only Denver addresses.

---

## 5. Public data sources by provider

Only public pages. Never call or email a store to collect data. Never create accounts or join affiliate programs. If a locator is JavaScript-heavy, record the official locator URL, the search parameters used, and the date, and copy only what the locator actually shows.

### Official fee and policy pages (opened for this step unless noted)

| Provider / topic | What the official page is for | URL | Checked | What we may state now |
|---|---|---|---|---|
| USPS money orders | National fees, limits, how to buy/cash, replacement fee | https://www.usps.com/shop/money-orders.htm | 2026-11-10 | Domestic fees: $2.65 for $0.01–$500.00; $3.75 for $500.01–$1,000.00; Postal Military Money Orders $0.85. Limit $1,000 per domestic money order. Pay with cash or debit card; "You cannot pay with a credit card." Cashable free at a Post Office with a primary photo ID; sign at the counter. Replacement processing fee $23.00. Domestic money orders never expire. |
| Walmart check cashing | National published maximum fees and limits | https://www.walmart.com/cp/check-cashing/632047 | 2026-11-10 | Official FAQ wording: "In most states the check-cashing limit is $5,000, though we increase this limit to $7,500 between January & April of each year. Check-cashing fees have a $4 maximum for pre-printed checks up to $1,000. For pre-printed checks above $1,000, the maximum fee is $8. Two-party personal checks are limited to $200 & have a maximum fee of $6." Present endorsed check at a Money Service Center or Customer Service desk with valid identification. No registration required. |
| Walmart money orders | Published maximum fee and how to pay | https://www.walmart.com/cp/money-orders/5791922 | 2026-11-10 | Official wording: "$1 maximum fee" and "Exact charges vary by location, but they won't be over $1." "Use cash or your debit card at any Walmart Money Center or Customer Service Desk." |
| King Soopers check cashing | Colorado Kroger-family Money Services policy | https://www.kingsoopers.com/o/money-services/check-cashing | 2026-11-10 | No dollar fee is published on this page: "Fees and limits vary by state so check your local Money Services Desk." Accepts checks "up to the value of up to $5,000." Requires SSN or TIN plus a listed photo ID. No bank account required. "We are generally open from 8am-8pm, but operating hours may vary depending on your location"; many stores "open seven days a week." List accepted check types only as the page lists them. |
| Kroger Money Services FAQ | ID, Sunday hours, bill-pay requirements, prepaid, money orders | https://www.kroger.com/i/money-services-faq | 2026-11-10 | ID required (same ID list). Loyalty cards not required for bill pay, "however fee discounts are offered when you use your card." Bill pay needs the biller stub and cash or debit (checks only for limited billers, payable to the biller; fees paid with cash or debit). No specific dollar fees on this page. |
| King Soopers bill pay | What can be paid and how | https://www.kingsoopers.com/o/money-services/bill-pay | 2026-11-10 | In-person bill pay with cash or debit; bring stub and enough funds for the bill plus fees. Page does not publish a dollar fee. "Over 20,000 billers" is the page's claim; do not invent a Denver biller list from the national examples (several examples are not Colorado utilities). |
| Western Union money orders | Official "varies" language | https://www.westernunion.com/us/en/money-order.html | 2026-11-10 | "A nominal fee may be charged … with the amount varying by location." Some locations may limit the maximum amount. Payment methods "depending on the policies of your local Western Union location." Not every WU location cashes money orders. No expiration, but a non-refundable service charge may apply in some states after one to three years. Use WU's location finder (linked from this page) later; exact finder URL TODO if it is not obvious from the page chrome. |
| MoneyGram money-order limits | US limit | https://www.moneygram.com/blog/money-order-limits-what-you-need-to-know | 2026-11-10 (article dated July 1, 2026) | "For MoneyGram money orders in the US, the current limit is $1,000." Limits "may vary slightly" by state and location. Available at participating retail locations; the article names Walmart and CVS as examples. No national fee published on this page. Location finder is referenced; exact finder URL TODO at listing time. |
| ACE Cash Express check cashing | Official fee-disclosure practice | https://www.acecashexpress.com/check-cashing/ | 2026-11-10 | No national fee published. "Each of our locations has a menu board that lists competitive check cashing fees for different check types. Because these rates vary by state and may change, it's best to visit a store near you to ask about fees." Valid government-issued photo ID required; no credit check. Official locator: https://www.acecashexpress.com/locations/ (URL from the official site's locations section; listings themselves are not collected in this step). ACE's broader site also markets payday and title loans — out of scope to promote. |
| CFPB prepaid card fees | Fee types, not a price list | https://www.consumerfinance.gov/ask-cfpb/what-types-of-fees-do-prepaid-cards-typically-charge-en-2053/ | 2026-11-10 (page "last reviewed: OCT 31, 2024") | Explains activation, monthly, ATM, cash reload, bill payment, and other fee types. Use as consumer-education context only, not as a Denver fee table. |
| FDIC Household Survey (2023) | Audience context | https://www.fdic.gov/household-survey | 2026-11-10 (page last updated November 14, 2024) | Official key findings: 4.2% of U.S. households (about 5.6 million) were unbanked in 2023; 14.2% (about 19.0 million) were underbanked. 8.0% of all households used nonbank money orders, 2.7% used nonbank check cashing, 6.6% used nonbank money transfer services. Use for "why this site exists," not as location data. |
| Colorado DORA Division of Banking — money transmitters | State licensing of money transmitters | https://banking.colorado.gov/industry/money-transmitters | 2026-11-10 | Official industry page for Colorado money-transmitter licensing, forms, and a note about "HB-25-1201 Update to Colorado's Money Transmitter Act." TODO in a later research pass: read the update and the statutes before describing current agent rules. |
| Colorado DORA — what the Division regulates | Scope of state banking regulation | https://banking.colorado.gov/consumers/what-we-regulate | 2026-11-10 | "The Division of Banking regulates only state-chartered commercial banks and trust companies, and state-licensed money transmitters. We do not regulate national banks or credit unions." Institution search is described on this page. **TODO:** this page does not say whether standalone check cashers are licensed or fee-capped in Colorado. Do not claim "no license required" until an official statute or DORA page is opened and quoted. |

### Official locators and other public sources to use in later listing steps (URLs to collect from; no listings now)

- USPS Post Office / money-order locations: official USPS location tools (exact locator URL TODO at collection time; policy page above already says any Post Office can sell or cash postal money orders).
- Walmart store finder (official walmart.com store locator; confirm URL at collection time).
- King Soopers store locator, linked from the Money Services pages above.
- Western Union location finder, linked from the money-order page above; filter to money-order / bill-pay services if the finder allows it.
- MoneyGram location finder, referenced from the limits article above.
- ACE Cash Express locator: https://www.acecashexpress.com/locations/
- Other brands only if an official locator or official store directory exists (examples to confirm later, all TODO until an official page is opened): Safeway/Albertsons money services, MoneyTree, Check Into Cash, Speedy Cash, 7-Eleven / Western Union agent pages.
- Do **not** treat OpenStreetMap, CitySquares, Yelp, or Google Maps as a fee source. OSM or a search index may be a *lead* to then confirm on an official locator. Errand Desk's fact rules still apply: if the official page does not publish it, say so.

### Sources that are not sufficient on their own

Aggregator directories, Bankrate/NerdWallet/MoneyPantry fee tables, and "typical 1.5%–5%" ranges must not be copied into Check Desk as facts. They can appear in the competitor research memo only.

---


## 6. Data fields (brief)

Two datasets, both requiring `source_url` (or `source_urls`) and `last_verified` (YYYY-MM-DD) on every fact.

**Locations** (`data/schema/locations.schema.json`, header + example-only rows in `data/schema/locations.csv`): `id`, `name`, `brand`, address fields, `lat`/`lng`, public `phone` only, service booleans (`check_cashing`, `money_orders`, `bill_pay`, `prepaid_reload`), per-day hours, `after_hours`, `open_saturday`, `open_sunday`, `open_after_1700_weekday`, `fee_notes`, `fee_source_url`, `id_requirements`, `source_urls`, **`last_verified` (required on every row)**, **`verification_status` (required)**, `verified_by`, `confidence` (`high`/`medium`/`low`), `notes`, `is_example`. Example rows are labeled and must never be published.

`last_verified` is the America/Denver calendar date the cited sources were last opened, even when the store itself has not been individually verified. A row that is only a chain policy still needs this date (the date the official policy or locator page was checked).

`verification_status` allowed values:

| Value | Meaning |
|---|---|
| `unverified` | Not yet checked against an official source. Do not publish. |
| `policy_only_call_ahead` | Chain or official policy for the brand is known (fees, ID rules, or services from a policy page), but this store has not been individually verified. The public card must tell the reader to call ahead. |
| `verified_official_locator` | Address, published hours, and listed services were confirmed on the brand's official store locator (or an official store directory) on `last_verified`. |
| `verified_official_store_page` | Confirmed on that location's own official page (not only a chain policy or a multi-store locator result). |

**Fees** (`data/schema/fees.schema.json`): provider-level facts — `provider`, `service`, amount or range, unit, conditions, geography, `source_url`, `last_verified`, `verified_by`, `confidence`, verbatim official wording when possible. Prefer one row per published figure (e.g. USPS $2.65 tier separately from the $3.75 tier).

### Site-wide disclaimer (Step 2 refinement)

Every built page includes a short disclaimer from `site-src/src/partials/disclaimer.html`, injected by `build.py` into `src/layout.html` (token `{{disclaimer}}`). 404.html, which is copied as a static file and not wrapped by the builder, contains the same wording by hand. Draft text:

> Policies and fees change. Call the location before you go. Check Desk is an information directory, not financial advice. Last updated <date>.

The date comes from `disclaimer_updated` in `site.config.json`. This block is in addition to, not a replacement for, the longer "not financial advice / not affiliated" note on city and guide pages.

---

## 7. Proposed 8-step sequence and human-review pauses

This is formally **Step 1 of 8**. Later steps are a proposal; do not start them until Richard signs off on this plan. Do not create a GitHub repo in Step 1. Do not collect Denver listings in Step 1.

| Step | Work | Human-review pause (required before the next step) |
|---|---|---|
| **1. Plan (this step)** | Scope, competitor scan, site map, schemas, source list, pilot-market decision | Richard reviews this plan, scope, and competitor memo; confirms domain/branding questions and metro boundary |
| **2. Repo and scaffolding** | Create the Check Desk GitHub repo; copy the Errand Desk static-builder pattern (not the city bodies); layout, fact-rule README, empty data files, CI lint for schema/CSV | Richard reviews repo settings, license, branch protection, and that no Errand Desk secrets, analytics tokens, or affiliate/Ko-fi code were copied. **No listings yet.** |
| **3. Provider fee facts** | Fill `fees` data only from official pages already listed (and any additional official pages found). Re-check every URL. Mark missing fees TODO, never estimate | Richard reviews the fee table and official quotations before any public-facing guide is written |
| **4. Denver listing collection** | Collect locations for the approved metro boundary from official locators only. Record source URL + date on every row. No outreach, no paid tools, no affiliate signups | Richard reviews the raw CSV (brands included, hours completeness, payday-storefront policy, confidence tags) before copy is drafted |
| **5. Draft pages** | Write home, disclaimers, guides, `/denver/` and service/after-hours views from reviewed data only | Richard reviews tone, lower-fee ordering, disclaimer text, and that no unsourced fee appears |
| **6. Verification pass** | Re-open sources; align last-verified dates; reject stale or unsourced rows; check phones/hours against the same official locators | Richard signs off on the verified dataset and any drop/keep decisions |
| **7. Hardening** | SEO/JSON-LD, accessibility, sitemap, link checks, "not financial advice" on every template, no indexing of example data | Richard reviews a preview build (local or staging). No paid ads, no affiliate join |
| **8. Pilot publish** | Deploy only after Richard approves going live (hosting/domain are his, as with Errand Desk). Recheck cadence starts | Richard gives an explicit go-live. Post-launch corrections follow the contact page; still no outreach to businesses to "verify" listings |

---

## 8. Hard rules (carry into every later step)

- Public sources only. Never contact businesses. Never sign up for affiliate programs or spend project money.
- Never present content as financial, legal, or tax advice. Never promote payday loans, title loans, or other credit products.
- Favor lower-fee options and honest comparisons. If a provider does not publish a fee, write that — do not invent a range.
- Every data point needs a source URL and a last-verified date.
- Do not invent facts.

---

## 9. Open questions for Richard

See the Step 1 report; the three questions are: (1) separate domain vs a section of Errand Desk; (2) exact Denver metro boundary for the first listing pass; (3) whether payday/title-loan storefronts that also cash checks may appear as check-cashing locations with a non-promotional label, or should be omitted.
