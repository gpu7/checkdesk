# Check Desk — Step 3 seed content plan

**Date:** 2026-11-10 (America/Denver).  
**Status:** Step 3 of 8. This file is a content and URL plan only. It does not collect Denver listings and does not draft full page copy.  
**Repo:** `/workspace/checkdesk-repo` (site is its own property; production domain is **checkdesk.us**, registered at Cloudflare Registrar on 2026-11-10).  
**Related:** [PLAN.md](PLAN.md), [research/step1-scope.md](research/step1-scope.md), [research/step1-competitors.md](research/step1-competitors.md), [../data/schema/locations.schema.json](../data/schema/locations.schema.json).

Do not start Step 4 (opening locators and filling location rows) or Step 5 (full page drafts) until Richard approves this plan.

## Decisions in force

- **Domain:** production host is **checkdesk.us**, registered at Cloudflare Registrar on 2026-11-10. Nameservers are already Cloudflare's. No AWS resources have been created and no site DNS records have been added from this repo.
- **Pilot:** Denver metro, Denver proper first. Inner-ring cities later: Aurora, Lakewood, Commerce City, Englewood, Wheat Ridge, Federal Heights.
- **Payday / title-loan storefronts:** omitted from the directory for now.
- **Fees:** only published official figures. If a provider does not publish a price, the cell is **Not published, call ahead**. Never estimate or average.
- **Hours labels (decided 2026-11-10):** the site displays two labels, not a single after-hours badge.
  - **Open evenings** (`open_after_1700_weekday`): published hours are open after 17:00 America/Denver on at least one weekday (Monday–Friday).
  - **Open weekends** (`open_weekends`): published hours on Saturday or Sunday.
  If hours are not published, leave hours empty and leave the corresponding flag null. Do not guess. The `after_hours` field is still computed for internal use (true when any published service window is outside Monday–Friday 09:00–17:00 America/Denver, including Saturday, Sunday, weekday evenings after 17:00, or weekday mornings before 09:00). It is not displayed on the site.
- **Location rows:** `last_verified` (YYYY-MM-DD) and `verification_status` are required.
- **Disclaimer:** the site-wide block in `site-src/src/partials/disclaimer.html` already appears on every built page. City and guide pages also get the longer "not affiliated / not financial advice" note from PLAN.md.
- **No affiliate links** in this seed. No outreach, no paid tools.

Fee figures below are included only when an official page was opened in Step 1 (2026-11-10) and the wording is quoted or closely paraphrased with the URL. Everything else is marked **TODO** for Step 4.

## First ship set

Ship these **two** pages first, in this order, once Step 4 data for them has been reviewed:

1. **`/guides/money-orders/`** — National money-order comparison. Step 1 already opened official fee pages for USPS and Walmart, and official "varies / no national price" language for Western Union, MoneyGram, and King Soopers-related FAQs. This is the fastest honest comparison we can publish.
2. **`/denver/`** — Denver proper hub. A short, sourced overview that points at lower-fee published options and at the service sub-pages, even if the first public location list is still short (official-locator rows only).

Same wave, immediately after those two (not a substitute for them): **`/guides/check-cashing-fees/`** (Walmart published maximums already sourced; King Soopers official page does not publish a dollar fee). Among city sub-pages, **`/denver/check-cashing/`** is the first to follow the hub.

Do not wait to invent a large store list before shipping the money-order guide. Do not ship a Denver sub-page that only repeats national fees with no verified local rows.

---

## 1. URL tree

Trailing slashes, stable slugs, Errand Desk-style paths. Status **seed** means the page is in the first content wave (Step 4–5). Status **later** means it is specified here but is not in the first wave.

### 1.1 Utility pages

| URL | Title (proposed) | H1 (proposed) | Intent / audience question | Sections | Data | Sources | Links | JSON-LD | Status |
|---|---|---|---|---|---|---|---|---|---|
| `/` | Check Desk: sourced check cashing, money orders, and bill pay | Plain, sourced answers for check cashing, money orders, and bill pay | "Where can I cash a check / buy a money order without a bank?" | Draft notice until launch; disclaimer; what the site is; fee snapshot copied only from reviewed official wording; Denver jump link; method | Snapshot table (same columns as the fee-table template, subset) | Only figures already reviewed or added in Step 4 | `/guides/*`, `/denver/`, `/about/` | `WebSite` | seed (already a DRAFT stub; fill after the two ship-first pages) |
| `/about/` | About Check Desk and how we check facts | About this site and how we check facts | "Can I trust these fees?" | Method; last-verified and `verification_status`; not financial advice; corrections | None | Method only | `/disclosure/`, `/privacy/` | `page` (no JSON-LD) | seed (stub exists) |
| `/disclosure/` | Disclosure \| Check Desk | Disclosure: how this site makes money | "Do you get paid to list these places?" | No ads / no paid rankings / no affiliates at this time; what money would not change | None | — | `/about/` | `page` | seed (stub exists) |
| `/privacy/` | Privacy Policy \| Check Desk | Privacy policy | "What data do you collect?" | No accounts; no analytics token now; future hosting logs if S3/CloudFront is used | None | — | `/about/` | `page` | seed (stub exists) |
| `/contact/` | Contact Check Desk | Contact | "How do I send a correction?" | Corrections process; no email until Richard publishes one | None | — | `/about/` | `page` | later |
| `/search/` | Search \| Check Desk | Search | Site search | Client-side search, Errand Desk pattern | Search index of public pages | — | Home | `page` | later |
| `/map/` | — | — | — | **No map in v1** (see §3). Official locator links instead. | — | — | — | — | later, only if a later decision adds one |

### 1.2 Guides (`/guides/`)

Each guide is an `Article` with `BreadcrumbList`. Add `FAQPage` only from on-page `<details>` questions whose answers are sourced on the same page. Internal links should include the Denver hub, relevant `/providers/<brand>/` pages, and `/about/`. Every guide starts with the long disclaimer note plus the site-wide banner.

Required sections on every national comparison guide, unless noted: kicker with last-checked date; short version (lower published fees first); comparison table; "what to bring"; what the official page does not say; FAQ; numbered Sources with last-verified dates.

#### `/guides/` — Guides index

- **Title:** Check Desk guides: check cashing, money orders, bill pay, after hours
- **H1:** All guides
- **Intent:** "check cashing fees" / "money order cost" (browse)
- **Question:** "What guides do you have?"
- **Sections:** Short method line; list of live guides with one-sentence descriptions; later guides marked coming, not fake-launched
- **Data tables:** None
- **Sources:** None required beyond links to child pages
- **Links:** Each live guide, `/denver/`, `/providers/`
- **JSON-LD:** `CollectionPage` + `BreadcrumbList`
- **Status:** seed

#### `/guides/check-cashing-fees/` — Check-cashing fee comparison

- **Title:** Check-cashing fees: published prices and what isn't posted (2026)
- **H1:** What check cashing costs, using official pages only
- **Intent:** "check cashing fees," "Walmart check cashing fee," "cheapest place to cash a check"
- **Question:** "What will I pay to cash this check, and who actually publishes a price?"
- **Sections:** Lower-fee published options first (Walmart official maximums; King Soopers/Kroger "fees vary by state"); grocery vs supercenter vs dedicated casher; accepted check types and ID rules as published; **online/app options** summarized here and linked to `/guides/online-check-options/`; dedicated cashers (see payday rule in §5); "Not published, call ahead" rows; what we do not guess (including any legal claim about banks cashing checks for non-customers)
- **Data tables:** National fee table (template in §2). One row per published figure or official "not published" statement, not a typical range
- **Sources (Step 1, opened 2026-11-10):** [Walmart check cashing](https://www.walmart.com/cp/check-cashing/632047) (published maximums and limits — see quote in PLAN.md); [King Soopers check cashing](https://www.kingsoopers.com/o/money-services/check-cashing) (no dollar fee; "Fees and limits vary by state"; checks up to $5,000; ID + SSN/TIN list; general 8am–8pm, hours may vary); [Kroger Money Services FAQ](https://www.kroger.com/i/money-services-faq); [ACE check cashing](https://www.acecashexpress.com/check-cashing/) (no national fee; menu board / varies by state). **TODO in Step 4:** any additional official grocery/supercenter pages if we add brands; official pages for online options (see that guide); do not copy Bankrate/NerdWallet/MoneyPantry ranges
- **Links:** `/providers/walmart/`, `/providers/king-soopers/`, `/denver/check-cashing/`, `/guides/online-check-options/`, `/guides/after-hours/`
- **JSON-LD:** `Article` + `BreadcrumbList` + `FAQPage` if FAQs exist
- **Status:** seed (same wave, right after the two ship-first pages)

#### `/guides/money-orders/` — Money order fees

- **Title:** Money order fees and limits: USPS, Walmart, and others (2026)
- **H1:** Where to get a money order and what official pages say it costs
- **Intent:** "money order cost," "USPS money order fee," "Walmart money order"
- **Question:** "Where can I buy a money order, what is the fee, and what is the limit?"
- **Sections:** Short version; comparison table; how to pay (cash vs debit vs credit, only if the official page says); ID rules for larger amounts if published; cashing vs buying; tracking/replacement only when official pages state a fee or rule; convenience stores and agents (7-Eleven / Western Union: official page **TODO** in Step 4); "Not published, call ahead"
- **Data tables:** National fee table (§2), service = money orders
- **Sources (Step 1, opened 2026-11-10):** [USPS Money Orders](https://www.usps.com/shop/money-orders.htm) ($2.65 for $0.01–$500.00; $3.75 for $500.01–$1,000.00; Postal Military $0.85; $1,000 domestic limit; cash or debit, not credit; cash free at a Post Office with photo ID; $23.00 replacement processing fee; never expire); [Walmart Money Orders](https://www.walmart.com/cp/money-orders/5791922) ("$1 maximum fee"; "Exact charges vary by location, but they won't be over $1"; cash or debit at a Money Center or Customer Service Desk); [Western Union money orders](https://www.westernunion.com/us/en/money-order.html) (nominal fee "varying by location"; not every agent cashes them); [MoneyGram limits article](https://www.moneygram.com/blog/money-order-limits-what-you-need-to-know) (US limit $1,000; no national fee on that page; article dated July 1, 2026). King Soopers/Kroger FAQ mentions money orders but publishes no dollar fee. **TODO in Step 4:** re-open all of the above; official King Soopers or Kroger money-order page if one exists; official 7-Eleven / Western Union location or money-order page (candidate, not opened for Check Desk Step 1: `https://www.westernunion.com/us/en/locations/7-eleven.html`); MoneyGram help/fee pages if any publish a national fee
- **Links:** `/providers/usps/`, `/providers/walmart/`, `/providers/western-union/`, `/providers/moneygram/`, `/denver/money-orders/`
- **JSON-LD:** `Article` + `BreadcrumbList` + `FAQPage` if FAQs exist
- **Status:** seed — **ships first**

#### `/guides/bill-pay/` — Walk-in bill pay

- **Title:** Paying a bill in person with cash or debit: what official pages say
- **H1:** Walk-in bill pay, from official pages only
- **Intent:** "pay bill with cash," "Walmart bill pay," "pay utility bill in person"
- **Question:** "Where can I pay a utility, rent, or phone bill in cash, and is the fee published?"
- **Sections:** How walk-in bill pay works (stub, cash or debit, confirmation number) only as official pages describe it; comparison table; networks vs store desks (PayNearMe, Walmart, CheckFreePay / Western Union as named on official retailer pages); what is not a Denver biller list (King Soopers' national biller examples include non-Colorado names — do not treat them as local); "Not published, call ahead"
- **Data tables:** National fee table, service = bill pay
- **Sources (Step 1, opened 2026-11-10):** [King Soopers bill pay](https://www.kingsoopers.com/o/money-services/bill-pay) (cash or debit; stub; fees mentioned but no dollar amount; "over 20,000 billers" is the page's claim); [Kroger Money Services FAQ](https://www.kroger.com/i/money-services-faq) (loyalty card not required; fee discounts with card; checks only for limited billers, payable to the biller). The King Soopers bill-pay page says payments are "Powered By" CheckFreePay Corporation and Western Union (that sentence appeared in a Texas-law context on the fetched page — quote carefully, do not generalize beyond the page). **TODO in Step 4:** official Walmart bill-pay page; official PayNearMe page; official CheckFreePay consumer page if any; Western Union bill-pay page if distinct from money orders
- **Links:** `/providers/king-soopers/`, `/providers/walmart/`, `/denver/bill-pay/`
- **JSON-LD:** `Article` + `BreadcrumbList` + `FAQPage` if FAQs exist
- **Status:** seed

#### `/guides/prepaid-reload/` — Prepaid reload

- **Title:** Reloading a prepaid card in a store: published rules and fee types
- **H1:** Prepaid card reloads, from official and CFPB pages
- **Intent:** "reload prepaid card," "prepaid card reload fee"
- **Question:** "Where can I add cash to a prepaid card, and what kinds of fees should I look for?"
- **Sections:** This is not a ranked "best card" list and not an endorsement; CFPB fee-*type* explainer (activation, monthly, cash reload, bill payment, etc.); retailer reload desks only where official pages say they offer reload; "Not published, call ahead" for dollar amounts unless an official page publishes one
- **Data tables:** National fee table, service = prepaid reload, plus a non-price "fee types" list sourced to CFPB
- **Sources (Step 1, opened 2026-11-10):** [CFPB prepaid fee types](https://www.consumerfinance.gov/ask-cfpb/what-types-of-fees-do-prepaid-cards-typically-charge-en-2053/) (last reviewed Oct 31, 2024 — re-open in Step 4; no locator, no Denver fees). Kroger FAQ mentions prepaid cards and "a small fee" without a dollar amount. **TODO in Step 4:** official Walmart MoneyCard / reload pages; other official reload-network pages we decide to include; no affiliate card links
- **Links:** `/guides/bill-pay/`, `/denver/` (if any verified reload rows exist), CFPB as external
- **JSON-LD:** `Article` + `BreadcrumbList` + `FAQPage` if FAQs exist
- **Status:** seed

#### `/guides/after-hours/` — After-hours options

- **Title:** After-hours check cashing, money orders, and bill pay
- **H1:** Finding a desk open outside bank hours
- **Intent:** "check cashing open late," "cash a check on Sunday," "money order Saturday"
- **Question:** "Where is a desk open after 5 p.m. or on the weekend, and which of those actually publish a fee?"
- **Sections:** Display rule (decided 2026-11-10): **Open evenings** means published hours are open after 17:00 America/Denver on at least one weekday (Monday–Friday); **Open weekends** means published hours on Saturday or Sunday. Both labels are computed from published hours only. Mention that the older single after-hours flag is internal and not shown. National patterns only when official pages state them (e.g. King Soopers: many stores seven days, "generally open from 8am-8pm, but operating hours may vary"); link to `/denver/after-hours/`; reminder that hours change and must be confirmed
- **Data tables:** No national store list. A small definition table (label, meaning) for Open evenings and Open weekends. Denver rows with either label live on the city sub-page
- **Sources:** Same official hours-language pages as above; location hours only from official locators, collected in Step 4
- **Links:** `/denver/after-hours/`, `/guides/check-cashing-fees/`, `/guides/money-orders/`
- **JSON-LD:** `Article` + `BreadcrumbList` + `FAQPage` if FAQs exist
- **Status:** seed

#### `/guides/online-check-options/` — Online / app options

- **Title:** Mobile check deposit and app check cashing, from official pages
- **H1:** Cashing or depositing a check with an app (official wording only)
- **Intent:** "cash a check with an app," "Ingo check cashing," "Cash App check deposit"
- **Question:** "Can I cash a check on my phone, and what fee does the official page publish?"
- **Sections:** Factual descriptions of official products only (mobile deposit to a bank, credit union, neobank, or prepaid account; Ingo-type instant check cashing if an official page is opened); published fees, holds, and limits; ID or account requirements; this is not a recommendation to open an account and not a "best app" ranking; **no affiliate links**; "Not published, call ahead" / "not stated on the official page" where needed
- **Data tables:** National fee table, with provider = the official app or program name and service = check_cashing (or a note if it is a deposit, not cash)
- **Sources:** **All TODO in Step 4.** Do not use Step 1 competitor articles as the fee source. Candidates to open (confirm the official URL in Step 4): the provider's own help or price page for Cash App, PayPal, Venmo, Ingo Money, and any prepaid official check-deposit page (e.g. a Walmart MoneyCard page if it exists). CFPB/FDIC only for context, not for a specific app's fee
- **Links:** `/guides/check-cashing-fees/`, `/about/`
- **JSON-LD:** `Article` + `BreadcrumbList` + `FAQPage` if FAQs exist
- **Status:** seed (copy after official pages are opened; may ship slightly after the two ship-first pages)

#### `/guides/lower-fee-options/`

- **Status:** **later.** The check-cashing and money-order guides already put published lower fees first. A separate "cheaper than a store" guide would duplicate them. Revisit only if those two guides become too long.

### 1.3 Denver pages

Public city lists include only rows with `verification_status` of `verified_official_locator` or `verified_official_store_page`, a real `last_verified` date, and `is_example` false. See §3 for cards, sort, grouping, map, and `policy_only_call_ahead`.

#### `/denver/` — Denver hub (ships first among city pages)

- **Title:** Check cashing, money orders, and bill pay in Denver, CO
- **H1:** Denver check cashing, money orders, and bill pay
- **Intent:** "check cashing Denver," "money order Denver," "pay bill in cash Denver"
- **Question:** "Where in Denver can I cash a check, buy a money order, or pay a bill today, and what is actually published about fees and hours?"
- **Sections:** Long disclaimer; short version that favors published lower-fee options; last-verified kicker; jump links to sub-pages; a compact lower-fee snapshot (national or chain published figures, clearly labeled as chain policy, not a store till price); verified Denver-proper location list (or a clear "we're still verifying official locator rows" note if the first ship has few rows); after-hours jump; inner-ring cities listed as coming later, not as empty pages; Sources
- **Data tables:** Location cards/table (§3). Snapshot may reuse the national fee-table columns for a few reviewed chain facts
- **Sources:** Official locators and policy pages listed in §6, opened in Step 4. Step 1 did not collect Denver store rows
- **Links:** `/denver/check-cashing/`, `/denver/money-orders/`, `/denver/bill-pay/`, `/denver/after-hours/`, `/guides/money-orders/`, `/guides/check-cashing-fees/`, matching `/providers/<brand>/`
- **JSON-LD:** `Article` + `BreadcrumbList` + `FAQPage` if FAQs exist. `LocalBusiness` / `FinancialService` markup only for a row whose address and hours came from an official locator (PLAN.md rule)
- **Status:** seed — **ships first among city pages** (second page in the overall first ship set)

#### `/denver/check-cashing/`

- **Title:** Check cashing in Denver, CO
- **H1:** Where to cash a check in Denver
- **Intent:** "check cashing near me Denver," "cash a paycheck Denver"
- **Question:** "Which verified Denver locations cash checks, what fee is published, and which are open after bank hours?"
- **Sections:** Disclaimer; short version; sort explanation; verified location list (check_cashing = true); chain policy notes; Sources
- **Data tables:** Location table, check-cashing subset
- **Sources:** Official locators + fee policy pages, Step 4
- **Links:** `/denver/`, `/denver/after-hours/`, `/guides/check-cashing-fees/`, `/guides/online-check-options/`
- **JSON-LD:** `Article` + `BreadcrumbList` + optional `FAQPage`
- **Status:** seed — first city *sub-page* after the hub

#### `/denver/money-orders/`

- **Title:** Money orders in Denver, CO
- **H1:** Where to buy a money order in Denver
- **Intent:** "money order near me Denver," "USPS money order Denver"
- **Question:** "Where in Denver can I buy a money order, and which official fees apply?"
- **Sections:** Same pattern; USPS national fees clearly labeled national; Walmart maximum labeled as a published cap, not a till price; agent locations "Not published, call ahead" if no official fee
- **Data tables:** Location table, money_orders = true
- **Sources:** USPS / Walmart / WU / MoneyGram official pages (Step 1 quotes, re-checked) + official locators in Step 4
- **Links:** `/denver/`, `/guides/money-orders/`, `/providers/usps/`, `/providers/walmart/`
- **JSON-LD:** `Article` + `BreadcrumbList` + optional `FAQPage`
- **Status:** seed (after the hub and check-cashing sub-page)

#### `/denver/bill-pay/`

- **Title:** Walk-in bill pay in Denver, CO
- **H1:** Paying a bill in person in Denver
- **Intent:** "pay utility bill in person Denver," "pay Xcel bill cash Denver" (only list a named Denver biller if an official page or the desk's official materials say so — otherwise stay generic)
- **Question:** "Where can I pay a bill with cash in Denver, and is the fee published?"
- **Sections:** Same pattern; do not invent a local biller roster from national example lists
- **Data tables:** Location table, bill_pay = true
- **Sources:** King Soopers / Kroger official bill-pay pages; other official bill-pay pages opened in Step 4; locators
- **Links:** `/denver/`, `/guides/bill-pay/`
- **JSON-LD:** `Article` + `BreadcrumbList` + optional `FAQPage`
- **Status:** seed (after the hub and check-cashing sub-page)

#### `/denver/after-hours/`

- **Title:** After-hours check cashing, money orders, and bill pay in Denver
- **H1:** Denver desks open evenings or weekends
- **Intent:** "check cashing open Sunday Denver," "cash a check at night Denver"
- **Question:** "Which verified Denver locations are open after 5 p.m. on a weekday, or open on Saturday or Sunday?"
- **Sections:** Repeat the two display labels (Open evenings / Open weekends, decided 2026-11-10); list only rows with `open_after_1700_weekday` or `open_weekends` true and hours from an official locator or official store page; if a store is missing hours, it does not appear here. Do not use the internal `after_hours` field as the display filter.
- **Data tables:** Location table of rows with either label, showing per-day hours and the Open evenings / Open weekends labels
- **Sources:** Official locator hours, Step 4
- **Links:** `/denver/`, `/guides/after-hours/`
- **JSON-LD:** `Article` + `BreadcrumbList` + optional `FAQPage`
- **Status:** seed (after the hub and check-cashing sub-page)

#### Inner-ring city pages (`/aurora/`, `/lakewood/`, `/commerce-city/`, `/englewood/`, `/wheat-ridge/`, `/federal-heights/`)

- **Status:** **later.** Same template as `/denver/`, created only when official-locator rows for that city have been reviewed. Do not publish empty city shells. The Denver hub may name these cities as "next," with no fake counts.

### 1.4 Provider pages (`/providers/<brand>/`)

See §4 for the template and initial brand list.

- `/providers/` — index, `CollectionPage`, **seed**
- Each brand page: `Article` + `BreadcrumbList` + optional `FAQPage`, **seed** or **later** as listed in §4
- No per-store vanity URLs in the pilot

---

## 2. National comparison pages and fee-table template

The guides in §1.2 are the national comparison pages. Shared rules:

- Sort rows so **published lower fees come first**. Rows whose official page does not publish a price come after, labeled **Not published, call ahead** — never filled with a "typical 1.5%–5%" figure from another website.
- Quote official wording in a column or footnote when the fee is a maximum, a range, or "varies by location."
- One table row per distinct official figure (for example, USPS $2.65 and $3.75 are two rows, or one row with both tiers clearly stated).
- Dedicated cashers that also sell payday or title loans: **do not add their storefronts to any directory list.** They may appear on a *national* fee table only as a policy row ("official page does not publish a national fee; menu board at the store") and only with a visible note that Check Desk does not list those stores because the chain also offers payday or title loans. See §5 for the proposed provider-page treatment (flagged for Richard).

### Standard fee-table template

Use these columns on national comparison guides (and on the home snapshot, in shortened form):

| Column | What it holds |
|---|---|
| Provider | Brand or official program name |
| Service | `check_cashing`, `money_orders`, `bill_pay`, or `prepaid_reload` (written in plain language on the page) |
| Published fee | Exact official figure, official maximum, or **Not published, call ahead** |
| Limits | Amount caps, count caps, or "not stated on the official page" |
| Accepted check types / product notes | Only what the official page lists (or "not stated") |
| ID rules | Only what the official page lists (or "not stated") |
| Hours note | Official national or chain hours language, clearly labeled as not a specific store's hours; otherwise "see the official locator" |
| Source | Official URL |
| last_verified | YYYY-MM-DD |
| verification_status | For a *policy* row this is usually `policy_only_call_ahead` (chain policy, not a store). Do not use `verified_official_locator` on a national policy row that is not a place |

Example of how a *reviewed* policy row would look after Step 4 re-check (figures from Step 1, not a live table to ship unchanged):

- Walmart / check cashing / "$4 maximum" for pre-printed checks up to $1,000; "$8 maximum" above $1,000; two-party personal checks limited to $200 with a "$6 maximum" / most-states limit $5,000, $7,500 January–April / types as listed on the Walmart FAQ / "valid identification" / desk: Money Service Center or Customer Service / `https://www.walmart.com/cp/check-cashing/632047` / last_verified 2026-11-10 / `policy_only_call_ahead` until a specific store is locator-verified.

Unpublished example (King Soopers check cashing): Published fee = **Not published, call ahead**; official page says fees and limits vary by state; limit up to $5,000 as published; ID list + SSN/TIN; generally 8am–8pm, hours may vary, many stores seven days / `https://www.kingsoopers.com/o/money-services/check-cashing`.

---

## 3. Pilot city pages

### What a location row shows

On `/denver/` and its sub-pages, each public card or table row shows:

- Name and brand
- Address, city, state, ZIP (from the official locator or official store page)
- Public phone only if the official locator or official page publishes one
- Services offered (check cashing, money orders, bill pay, prepaid reload) as the official source states them
- Published hours by day, or "Hours not published"
- **Open evenings** and/or **Open weekends** labels when the corresponding flags are true (decided 2026-11-10). Do not display a single after-hours badge.
- Fee notes: official chain or store wording, or **Not published, call ahead**, plus the fee source URL
- ID requirements when published
- `last_verified` (visible date)
- `verification_status` in plain language (see below)
- Link to the official source (and to `/providers/<brand>/` when that page exists)

Never show example CSV rows (`is_example=true`). Never show `unverified` rows on a public page.

### How `policy_only_call_ahead` is displayed

- **On public *city* lists:** do not include a store card whose status is `policy_only_call_ahead` or `unverified`. A public Denver pin means the place was confirmed on an official locator or official store page (`verified_official_locator` or `verified_official_store_page`).
- **Fee text on a verified store card may still be chain-level.** If the official *store* page does not publish a till price, the card quotes the official chain policy (including "maximum" language) or says **Not published, call ahead**, and it visually labels that fee as "chain policy — call the store to confirm." That does not downgrade the row's `verification_status` for address and hours.
- **`policy_only_call_ahead` is for national policy tables, provider pages, and internal/draft rows** (for example, "King Soopers Money Services desks cash checks; fees vary by state"). If a policy-only mention appears in prose on the Denver hub, it is a sentence with a source, not a fake pin.

### Sort order

1. Published fee, **lower first** (use the official dollar or official maximum when one exists; a published maximum still sorts as a published fee).
2. Then locations labeled **Open evenings** before those that are not, then **Open weekends** before those that are not (among rows with the same published-fee band, or among all "Not published, call ahead" rows).
3. Then name, A–Z.

The `/denver/after-hours/` sub-page lists rows with either label, uses the same fee sort, then latest published weekday closing time when hours exist, then name. Do not invent a fee in order to sort.

### Neighborhood grouping

For the Denver proper pilot, **do not invent neighborhood names**. Group only by data we have from the official address:

- v1: **one list for the City and County of Denver**, sorted as above.
- Optional secondary grouping later: ZIP code, if it helps a long list.
- Inner-ring cities are separate later pages, not mixed into the Denver-proper list. The hub may say that official locators also return nearby cities, and that those pages will come later.

### Map / no map

**No map on v1.** A map that is not built from verified official-locator coordinates would repeat a weakness we already saw in a competitor (a generic map that does not match the list). Link "View on the official locator" instead. Revisit a map only after a reviewed set of official coordinates exists.

### Which city pages ship first

1. `/denver/` (hub) — second page in the overall first ship set, first city page.
2. `/denver/check-cashing/` — first service sub-page.

`/denver/money-orders/`, `/denver/bill-pay/`, and `/denver/after-hours/` follow in the same seed wave once those location subsets exist.

---

## 4. `/providers/<brand>/` template and initial brand list

### Index: `/providers/`

- **Title:** Check cashing and money-service brands we cover
- **H1:** Brands
- **Question:** "Do you have a page about Walmart / USPS / King Soopers?"
- **Sections:** Plain list of brands in the seed set, one line each, no ranking by popularity or by commission (there are no commissions)
- **JSON-LD:** `CollectionPage` + `BreadcrumbList`
- **Status:** seed

### Brand page template

Every `/providers/<brand>/` page uses the same skeleton:

1. Kicker and last-checked date
2. Long disclaimer (not affiliated, not financial advice, not a loan offer)
3. What official pages say this brand offers (in-scope services only)
4. Published fees and limits, or **Not published, call ahead**
5. ID and payment-method rules as published
6. Hours language as published (labeled chain-level unless it is a specific official store page)
7. Link to the official store locator (not a scraped list)
8. Link to Denver pages that include *verified* stores of this brand (omit this section if we are not listing that brand's storefronts — see payday rule)
9. Numbered Sources

**JSON-LD:** `Article` + `BreadcrumbList` + optional `FAQPage`.  
**Data:** provider-level rows from `fees` data, not a paste of every city row.

### Initial brand list

| Slug | Brand | Status | Notes |
|---|---|---|---|
| `usps` | USPS | seed | Official national money-order fees already opened in Step 1 |
| `walmart` | Walmart | seed | Official check-cashing maximums and money-order cap opened in Step 1. Bill pay / prepaid **TODO** official pages in Step 4 |
| `king-soopers` | King Soopers (Kroger family) | seed | Official pages opened; dollar fees not published. Colorado banner for the pilot |
| `western-union` | Western Union | seed | Official money-order page opened; fee varies by location. Locator **TODO** exact URL in Step 4 |
| `moneygram` | MoneyGram | seed | Official US $1,000 limit language opened; no national fee on that page. Locator **TODO** exact URL in Step 4 |
| `ace-cash-express` | ACE Cash Express | seed, **policy only** | Official check-cashing page opened (no national fee). **No Denver store list** under the payday-omission rule. See §5 (flagged) |
| `paynearme` | PayNearMe | later | Candidate bill-pay network; official page **TODO** in Step 4 before a brand page is added |

Not in the initial list (later or omit): Check Into Cash, Speedy Cash, MoneyTree, 7-Eleven as its own brand (cover under Western Union / the money-order guide if an official page is opened), individual banks, and any payday-primary brand. A 7-Eleven section can live on the money-order guide without a `/providers/7-eleven/` page until we need one.

---

## 5. Editorial rules

### Tone

Plain, direct, and specific. Write for someone who may be cashing a paycheck today and may not have a bank account. Short sentences. No slang that talks down to the reader. No "best," "you should open," or "avoid this store" advice-voice. Favor lower published fees by **order and clarity**, not by scolding.

### Not financial advice

The site-wide disclaimer is already on every page. Guides and city pages also include the longer note from PLAN.md: Check Desk is not a bank, money transmitter, check casher, or adviser; it is not affiliated with the brands or agencies it names; this is general information, not financial, legal, or tax advice; confirm with the official source or the location before you go; we do not promote payday loans, title loans, or other credit products.

### Honest comparisons

- Quote official wording, including "maximum," "starting at," "vary by location," and "vary by state."
- If two official pages disagree (for example, competitor guides disagree about whether a bank must cash its own check for a non-customer), **do not pick a side** until official rule text is opened and quoted. Until then, say the official pages we have do not settle it.
- Do not use another publisher's "typical" percentage as our number.
- Label examples and chain-wide maximums so they cannot be read as this store's till price.

### Chains that also sell payday or title loans (proposal, flagged for Richard)

**Directory (decided):** ACE, Check Into Cash, Speedy Cash, and similar storefronts are **omitted** from `/denver/` and all city lists for now, even if they also cash checks.

**National guides and provider pages (proposed, please confirm):**

- A national fee table may include a **policy row** for a chain that publishes (or explicitly declines to publish) a check-cashing fee, so a reader who already knows the name can see "Not published, call ahead" rather than a guessed percentage.
- A `/providers/ace-cash-express/` page (and only if we later add others) may describe **check-cashing policy only**, with a short, plain sentence that Check Desk does not list these stores because the chain also offers payday or title loans, and that we do not describe or promote those loans.
- Do not add store locators as "find a store near you" calls to action for these chains on city pages. A provider page may link the official check-cashing policy page; linking the official locator is the open question below.
- Do not show ACE (or similar) reviews, loan APRs, or "other services" lists.

This is proposed, not decided. See open questions.

### Refresh cadence (proposed)

| Data type | Recheck at least | What to do if stale |
|---|---|---|
| National published fees and official "not published" statements | Every **90 days**, or sooner if we learn the official page changed | Build warning; do not silently ship a last_verified older than 90 days on a newly published or newly edited page |
| Location hours, phones, service flags from official locators | Every **90 days** | Same warning; drop from the Open evenings or Open weekends lists if hours disappear or no longer qualify |
| Open evenings / Open weekends flags (and the internal `after_hours` field) | Recompute whenever hours are re-verified | — |
| Regulatory / CFPB / FDIC / DORA context | When the official page is updated, and at least **annually** | Label the official "last reviewed" date if the agency prints one |
| Online app fees | Every **90 days** (these change often; tighten to 60 days if Step 4 shows frequent changes) | Same as national fees |

`last_verified` is always the date *we* opened the official source, not the date the provider last edited the page (that date, if shown, can appear in the source line).

---

## 6. Step 4 data-collection checklist

Step 4 opens official pages and fills `fees` (and, for Denver proper only first, `locations` from official locators). It does not draft full city/guide prose (Step 5). No outreach. No payday storefront rows.

Re-open every Step 1 source even if we already quoted it, and record a new `last_verified` date.

### A. National / chain policy pages (fees data)

- [ ] USPS money orders — https://www.usps.com/shop/money-orders.htm
- [ ] Walmart check cashing — https://www.walmart.com/cp/check-cashing/632047
- [ ] Walmart money orders — https://www.walmart.com/cp/money-orders/5791922
- [ ] Walmart bill pay — official page **TODO** (find and open the official Walmart bill-pay URL)
- [ ] Walmart prepaid / MoneyCard / reload — official page **TODO**
- [ ] King Soopers check cashing — https://www.kingsoopers.com/o/money-services/check-cashing
- [ ] King Soopers bill pay — https://www.kingsoopers.com/o/money-services/bill-pay
- [ ] Kroger Money Services FAQ — https://www.kroger.com/i/money-services-faq
- [ ] King Soopers or Kroger official money-order page, if one exists — **TODO**
- [ ] Western Union money orders — https://www.westernunion.com/us/en/money-order.html
- [ ] Western Union bill pay, if a distinct official page exists — **TODO**
- [ ] Western Union / 7-Eleven official page (candidate only, confirm in Step 4) — https://www.westernunion.com/us/en/locations/7-eleven.html
- [ ] MoneyGram money-order limits — https://www.moneygram.com/blog/money-order-limits-what-you-need-to-know
- [ ] MoneyGram official fee or help page, if it publishes a national fee — **TODO**
- [ ] ACE check-cashing *policy* page only (no store rows) — https://www.acecashexpress.com/check-cashing/
- [ ] PayNearMe official consumer/fee page — **TODO**
- [ ] CheckFreePay official consumer page, if any — **TODO**
- [ ] CFPB prepaid fee types — https://www.consumerfinance.gov/ask-cfpb/what-types-of-fees-do-prepaid-cards-typically-charge-en-2053/
- [ ] Official app / mobile-deposit fee pages to be identified in Step 4: Cash App, PayPal, Venmo, Ingo Money, and any official prepaid check-deposit page we include — all **TODO**, official URL only
- [ ] FDIC Household Survey (context only, not a fee) — https://www.fdic.gov/household-survey
- [ ] Colorado DORA money transmitters / what the Division regulates (context; do not claim a check-casher license rule the page does not state) — https://banking.colorado.gov/industry/money-transmitters and https://banking.colorado.gov/consumers/what-we-regulate

### B. Official locators (Denver proper locations only in this first collection pass)

Record source URL, search parameters, and date. Copy only what the locator shows. No ACE / Check Into Cash / Speedy Cash / other payday-or-title storefronts.

- [ ] USPS official location tool (exact URL **TODO** if not obvious from the money-order page; policy page already says any Post Office can sell or cash postal money orders)
- [ ] Walmart official store finder (exact URL **TODO**; confirm Money Center / customer-service services if the finder exposes them)
- [ ] King Soopers official store locator, linked from the Money Services pages
- [ ] Western Union official location finder, linked from the money-order page; filter to money orders / bill pay if the finder allows it (exact URL **TODO**)
- [ ] MoneyGram official location finder (exact URL **TODO**, referenced from the limits article)
- [ ] PayNearMe or other official bill-pay locator, only if we have approved that brand and an official locator exists — **TODO**

Do not use OSM, Google Maps, CitySquares, or Yelp as a fee source or as the sole source of a public row. A search index may be a lead only, then confirmed on an official locator.

### C. Row-quality gates before Step 5

- [ ] Every fees row has `source_url`, `last_verified`, and official wording or **Not published, call ahead**
- [ ] Every public location row has `last_verified`, `verification_status` in `{verified_official_locator, verified_official_store_page}`, `is_example=false`, and a public `source_urls` value
- [ ] `open_after_1700_weekday` (**Open evenings**) and `open_weekends` (**Open weekends**) are computed only from published hours: Open evenings = open after 17:00 America/Denver on at least one weekday (Monday–Friday); Open weekends = published hours on Saturday or Sunday. The internal `after_hours` field is still computed (any published window outside Monday–Friday 09:00–17:00 America/Denver) but is not displayed. Leave flags null when hours are not published.
- [ ] No payday/title-loan storefronts
- [ ] Phones are public-only
- [ ] Human review pause (PLAN.md Step 4) before any full page draft

---

## Open questions for Richard (3)

1. **Payday-chain provider pages:** Is the proposal in §5 acceptable — omit all such storefronts from city lists, but allow a national policy row and a check-cashing-only `/providers/ace-cash-express/` page that does not promote loans? And may that provider page link the official ACE *locator*, or only the official policy page?
2. **Online / app guide in the first wave:** Should `/guides/online-check-options/` ship in the same wave as the money-order guide and Denver hub, or wait until after those two and the check-cashing fee guide are reviewed?
3. **ACE locator exception:** If an official ACE locator is the only way to verify that a specific Denver address still cashes checks, we still will not list it under the current omission rule. Confirm there is no exception for "check-cashing desk only" ACE stores in Denver proper for v1.
