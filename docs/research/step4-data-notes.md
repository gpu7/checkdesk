# Check Desk — Step 4 data-collection notes

**Date opened / last_verified:** 2026-11-10 (America/Denver).  
**Branch intent:** `step4-data` (do not merge until Richard reviews).  
**What this is:** official policy facts plus an honest report of blocked locators. This is not a complete Denver store census and not Step 5 page copy.

Related files: [../CONTENT-PLAN.md](../CONTENT-PLAN.md), [../../data/providers/fees.csv](../../data/providers/fees.csv), [../../data/locations/denver.csv](../../data/locations/denver.csv), [../../tools/validate_data.py](../../tools/validate_data.py).

`python3 tools/validate_data.py` was run on both CSVs in this step (35 fee rows OK; 0 Denver location rows OK).

## What was collected

- **Provider policy tables** are in `data/providers/fees.csv` (35 rows, `is_example=false`, `verification_status=policy_only_call_ahead`, `last_verified=2026-11-10`). Unpublished prices are stored as `fee_unit=unpublished` and `published_fee=Not published, call ahead`. No estimated or “typical” ranges were invented.
- **Denver proper locations** are in `data/locations/denver.csv` with a header and **zero data rows**. Official locators and official store pages could not be read here (see Blocked sources). Payday / title-loan storefronts, including ACE, stay out of this city file even when a locator later works.
- **Online / app options:** Ingo Money official fee page was immediately fetchable, so those published tiers were recorded. Cash App, PayPal, Venmo, and prepaid mobile-deposit pages were **not** hunted further (the approved plan: collect only if cheap, else skip).

## Decisions applied

- ACE: check-cashing-only national policy row is included and may point at ACE’s official locator URL. No ACE store rows in `denver.csv`. No loan products described or promoted.
- After-hours flags are computed only from published per-day hours. With no store hours collected, no location is flagged after-hours.
- King Soopers national biller examples include non-Colorado names (for example City of Houston). Those are not a Denver biller list.

## Blocked sources (need a browser)

Automated fetching did not return usable store-level Denver data. Per the plan, these were **not** worked around with unofficial APIs, OSM/Yelp/Google, or a headed browser session. Please open the official pages below in a browser and, if they show Denver proper places, we can add `verified_official_locator` or `verified_official_store_page` rows in a later pass.

| Source | Official URL | What happened | Why it matters |
|---|---|---|---|
| Walmart check cashing (policy) | https://www.walmart.com/cp/check-cashing/632047 | curl redirected to `walmart.com/blocked` (“Robot or human?”). WebFetch timed out. | Step 4 could not re-open the official FAQ. CSV rows use Step 1 same-day official HTML wording and are flagged `STEP4_REVERIFY_BLOCKED` with `confidence=medium`. |
| Walmart money orders (policy) | https://www.walmart.com/cp/money-orders/5791922 | Same bot wall / WebFetch timeout. | Same as above. Confirm the $1 maximum language and whether a purchase limit or ID rule is also published. |
| Walmart store finder | https://www.walmart.com/store-finder | Bot wall. | Needed for a Denver Supercenter / Neighborhood Market list and Money Center flags. |
| Walmart official store page (example) | https://www.walmart.com/store/3533-denver-co | Bot wall. | Search indexed additional official URLs that were **not** successfully opened: `/store/5676-denver-co`, `/store/3127-denver-co`, `/store/3566-denver-co`. Addresses seen only in search snippets must not be copied into `denver.csv` until the official store page is opened. |
| King Soopers store search | https://www.kingsoopers.com/stores/search | curl timed out (0 bytes). | Needed to list Denver Money Services desks. |
| King Soopers official store pages | https://www.kingsoopers.com/stores/details/620/00134 (also `/620/00139`, `/620/00039`, and `/097/00305` which may not be a King Soopers banner) | WebFetch returned HTTP 500. curl timed out. | Do not invent addresses or hours from third-party directories. Confirm city = Denver (not an inner-ring city) and whether the page states Money Services. |
| USPS Location Finder | https://tools.usps.com/locations/ and https://tools.usps.com/find-location.htm (redirects to `/locations/home.htm`) | HTTP 200, but a JS locator shell with **no Denver results** in the fetched HTML. | Policy page says any Post Office can sell or cash postal money orders, but we still need official locator or official location-page hours before adding pins. Individual `?location=` URLs exist; we did not have a confirmed Denver location ID from a readable official index, so none were fetched at random. |
| Western Union locations marketing page | https://www.westernunion.com/us/en/locations.html | HTTP 200; no store list or Denver results. | Policy/marketing only. |
| Western Union location finder | https://location.westernunion.com/global-services/find-locations?WUCountry=us&WULanguage=en | HTTP 200 JS app (`__NEXT_DATA__` present) with no Denver agent results in the fetched HTML (a city search was not executed in a browser). | Needed for money-order / bill-pay agent rows. 7-Eleven filter candidate: the same finder with `agentName=7-eleven` (linked from the official 7-Eleven WU page). |
| MoneyGram location finder | https://www.moneygram.com/locations/us/en | HTTP 200 JS page (“Loading”); no Denver results in the fetched HTML. | Needed for money-order / bill-pay agent rows. |
| ACE store locator | https://www.acecashexpress.com/locations/ | HTTP 200 JS page; no Denver results in the fetched HTML. | May be linked from the national ACE check-cashing policy page (approved). Still **do not** add ACE rows to `denver.csv`. |

King Soopers and Kroger **policy** pages (`/o/money-services/*` and `/i/money-services-faq`) did open via WebFetch even though curl timed out. Those policy facts are in `fees.csv`.

## Uncertainties and conflicts (for Richard)

1. **Walmart re-verification.** Step 4 could not re-open the official Walmart pages. The Walmart fee rows in `fees.csv` quote official wording from the Step 1 HTML open on 2026-11-10 (America/Denver), earlier the same calendar day, and are marked medium confidence. Please confirm in a browser before those figures are treated as Step 4-verified.

2. **Zero Denver pins.** The ship-first `/denver/` hub and `/denver/check-cashing/` page will have no verified location cards until official locator or official store pages are collected in a browser. We did not fill the gap from unofficial directories.

3. **MoneyGram $1,000 limit source.** The official product page (https://www.moneygram.com/us/en/services/money-orders) publishes neither a purchase fee nor a dollar limit. The $1,000 US limit is from the official blog article dated **July 1, 2026** (https://www.moneygram.com/blog/money-order-limits-what-you-need-to-know), which also says limits may vary slightly by state and retail location. Confidence is medium for that reason.

4. **PayNearMe range vs till price.** The official Support Center article (updated August 07, 2026 21:17; timezone not stated) publishes a **range** of $0–$5.99 that varies by biller and payment option. That is not a single Denver till fee.

5. **CheckFreePay has no official consumer fee page we could open.** King Soopers’ bill-pay page says payments are “Powered By” CheckFreePay Corporation and Western Union in a **Texas Finance Code** sentence. We did not treat that as a Colorado licensing statement, and we did not copy third-party biller pages (SiEnergy, APS, and similar) that mention CheckFreePay or Walmart bill-pay prices.

Other notes, not listed as a top-five decision unless needed:

- USPS military money-order fee ($0.85, issued by military facilities) is recorded for completeness; it is not a civilian Denver Post Office fee.
- Western Union purchase fees remain unpublished; refund processing fees ($0 / $5 / $15 by amount tier) **are** published on the official FAQ and are stored as `money_order_replacement`, not as a purchase fee. The FAQ also mentions a $15 administrative fee for a copy of a cashed money order (not given its own row).
- King Soopers prepaid FAQ still says there is “normally a small fee” to activate and reload, while the same official page publishes a fee table (including cash reload $3.95 for NetSpend and “Up to $4.95” for listed Green Dot / GO2bank cards). The table is the more specific official figure. This is not a card recommendation.
- Colorado DORA “What We Regulate” (https://banking.colorado.gov/consumers/what-we-regulate, opened in Step 4) states that the Division regulates state-chartered commercial banks and trust companies, and state-licensed money transmitters, and does not regulate national banks or credit unions. It still does **not** state a check-casher licensing rule. No license claim was added to the data.
- CFPB prepaid fee-types page was re-opened (https://www.consumerfinance.gov/ask-cfpb/what-types-of-fees-do-prepaid-cards-typically-charge-en-2053/); still last reviewed **Oct 31, 2024**. It lists fee *types*, not retailer dollar fees, so it is not a `fees.csv` row.
- Walmart in-store bill pay and Walmart MoneyCard / reload official pages were not successfully opened (bot wall / no confirmed official bill-pay URL fetched). No Walmart bill-pay or prepaid-reload fee rows were added. A 2011 Walmart corporate announcement with old starting prices was not used.
- Ingo official tiers were recorded from https://ingomoney.com/benefits-fees/. That guide is still scheduled to ship after the first wave is reviewed. No affiliate links.

## Service-flag rule for a later Denver pass

When official store or locator pages are collected in a browser:

- Copy only what that official page states (name, address, public phone, per-day hours, services).
- Set `check_cashing` / `money_orders` / `bill_pay` / `prepaid_reload` true only when the official page or official locator says that store offers the service. A chain policy page is not enough to mark a specific desk.
- Compute `after_hours` only from published hours vs Monday–Friday 09:00–17:00 America/Denver. If hours are missing, leave the flag null.
- Keep `last_verified=YYYY-MM-DD` and `verification_status` of `verified_official_locator` or `verified_official_store_page`.
- City must be Denver proper, not Aurora, Lakewood, Commerce City, Englewood, Wheat Ridge, or Federal Heights (those are later pages).
- Do not add ACE / Check Into Cash / Speedy Cash / other payday-or-title storefronts to `denver.csv`.

## Open questions already decided (do not relitigate)

- ACE national policy page may link the official locator; city lists still omit those stores.
- `/guides/online-check-options/` ships after the first wave is reviewed; Ingo data is on file if that later guide needs it.
