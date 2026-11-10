# Check Desk — Step 4 data-collection notes

**Date opened / last_verified:** 2026-11-10 (America/Denver).  
**Branch intent:** `step4-data` (PR #2, merged). Hours-label follow-up (`hours-labels`) records the 2026-11-10 decision to display **Open evenings** and **Open weekends** instead of a single after-hours badge.  
**What this is:** official policy facts plus verified Denver-proper location rows collected from official store pages and the official USPS locator in a browser on 2026-11-10. This is not Step 5 page copy.

Related files: [../CONTENT-PLAN.md](../CONTENT-PLAN.md), [../../data/providers/fees.csv](../../data/providers/fees.csv), [../../data/locations/denver.csv](../../data/locations/denver.csv), [../../tools/validate_data.py](../../tools/validate_data.py), and the browser collection notes in [step4-browser/](step4-browser/).

`python3 tools/validate_data.py` was run after this pass: **38 fee rows OK; 32 Denver location rows OK**.

## What was collected

- **Provider policy tables** are in `data/providers/fees.csv` (38 rows, `is_example=false`, `verification_status=policy_only_call_ahead`, `last_verified=2026-11-10`). Unpublished prices are stored as `fee_unit=unpublished` and `published_fee=Not published, call ahead`. No estimated or “typical” ranges were invented.
- **Walmart national fees** were re-verified in a browser on 2026-11-10 from official Walmart pages. The earlier `STEP4_REVERIFY_BLOCKED` flag is gone. Confirmed figures: $4 maximum for pre-printed checks up to $1,000; $8 maximum above $1,000; two-party personal checks limited to $200 with a $6 maximum fee; limit in most states $5,000, increased to $7,500 January–April; money orders $1 maximum, with the maximum money-order amount **not published**; bill pay “starts at just $1” (varies by biller and speed); load/unload $0–$3.74 per transaction ($20–$1,000, up to 3 per day); card cashing $3.74 per transaction, $1,000 per transaction, 3 cards per day. Official pages: [check cashing](https://www.walmart.com/cp/check-cashing/632047), [money orders](https://www.walmart.com/cp/money-orders/5791922), [bill pay](https://www.walmart.com/cp/bill-pay/8721209), [load and unload](https://www.walmart.com/cp/deposit-and-withdraw/8401365).
- **King Soopers** check cashing, money orders, and bill pay remain unpublished (“Fees and limits vary by state”). The official check-cashing ID list and the Denver-proper store-number list are in the fee-row notes. Prepaid reload table figures were already recorded from the official prepaid page.
- **Denver proper locations** are in `data/locations/denver.csv` (**32 data rows**): 3 Walmart Supercenters, 13 King Soopers, and 16 USPS Post Offices. Every row has `last_verified=2026-11-10`. Walmart and King Soopers use `verification_status=verified_official_store_page`. USPS uses `verified_official_locator`. Payday / title-loan storefronts, including ACE, stay out of this city file.
- **Online / app options:** Ingo Money official fee page was immediately fetchable, so those published tiers were recorded. Cash App, PayPal, Venmo, and prepaid mobile-deposit pages were **not** hunted further (the approved plan: collect only if cheap, else skip).

Browser collection notes (verbatim extracts from official pages opened 2026-11-10):

- [step4-browser/walmart-2026-11-10.md](step4-browser/walmart-2026-11-10.md)
- [step4-browser/kingsoopers-2026-11-10.md](step4-browser/kingsoopers-2026-11-10.md)
- [step4-browser/usps-2026-11-10.md](step4-browser/usps-2026-11-10.md)

## Denver row counts

| Brand | Included rows | Source | Notes |
|---|---|---|---|
| Walmart | 3 | Official store pages | Supercenters 5676, 3533, and 3566 only |
| King Soopers | 13 | Official store pages | All Denver-address stores except Federal Heights 00034 |
| USPS | 16 | Official USPS locator detail pages | Retail Post Offices with listed money-order services |
| **Total** | **32** | | `open_weekends=true` on all 32 rows; `open_after_1700_weekday=true` on 26 rows (the 6 exceptions are USPS offices that close at 17:00 on weekdays) |

Service flags on the 32 rows (true only when that location’s official page listed the service):

- `check_cashing=true`: 4 (3 Walmart Supercenters + King Soopers Virginia Village 00150)
- `money_orders=true`: 30 (3 Walmart, 11 King Soopers, 16 USPS)
- `bill_pay=true`: 3 (Walmart Supercenters only)
- `prepaid_reload=true`: 1 (Walmart 5676, which listed load/unload)

Display labels (decided 2026-11-10): **Open evenings** = `open_after_1700_weekday` (published hours open after 17:00 America/Denver on at least one weekday, Monday–Friday); **Open weekends** = `open_weekends` (published hours on Saturday or Sunday). All 32 rows have `open_weekends=true` (every included location publishes Saturday retail hours; all 16 Walmart and King Soopers rows also publish Sunday hours). 26 of 32 rows have `open_after_1700_weekday=true`. The 6 false rows are USPS offices whose weekday retail hours end at 17:00 (Mile High, Cherry Creek, Park Hill, Wellshire, Stockyards, and Westwood). The internal `after_hours` field remains true on all 32 rows because every included location publishes at least one window outside Monday–Friday 09:00–17:00 America/Denver (for every USPS office, Saturday retail hours; and, at many offices, weekday hours that start before 09:00 or end after 17:00). It is not displayed.

## Exclusions and why

- **Walmart Neighborhood Markets 3128 (S Parker Rd) and 3127 (Chambers Rd).** Official store pages did not list money services. Mentioned here and in the Walmart 5676 row notes; not added as location rows.
- **King Soopers Federal Heights 00034** (1575 W 84th Ave, mailing address Denver, CO 80260). Physically in Federal Heights, Adams County. Held for the inner-ring wave.
- **USPS Capitol Hill Annex (1356950)** (1551 N Downing St). Official locator showed no hours and no services; excluded.
- **USPS North Pecos (1375398)** (1411 Cortez St, Denver, CO 80221). ZIP 80221 is likely outside Denver city limits; excluded and held for the inner-ring wave.
- **USPS GMF Finance (1439607)** (7550 E 53rd Pl, Denver, CO 80217). The locator notes it as a mail processing facility. It is not plainly a retail Post Office on the collected page, so it is excluded by the default rule (include only if plainly a retail Post Office). Flagged here for review. If included later, it would be a 17th USPS row; hours on the locator were Mon–Fri 7:30am–9:30pm and Sat 8:00am–10:00pm.
- **ACE, Check Into Cash, Speedy Cash, and other payday-or-title storefronts.** Omitted from `denver.csv` by decision. ACE keeps a national check-cashing-only policy page that may link ACE’s official locator; no loan promotion; no ACE store rows in the city file.
- **Western Union and MoneyGram agent pins.** Not listed as their own Denver rows. Many such agents sit inside already-listed chains (Walmart Money Centers, King Soopers Money Services desks, and similar). Official WU and MoneyGram locators were not used to add standalone agent rows in this pass.

## Gaps that remain

- **No Money Center or Money Services desk hours published.** Walmart and King Soopers location hours in `denver.csv` are published *store* or *retail* hours. No official store page in this collection published separate desk hours. Rows say to call ahead. Walmart 3566 mentions a Money Center “from 6am” but does not publish a desk closing time.
- **USPS ZIP sweeps incomplete.** Locator searches for ZIPs 80202, 80205, 80222, and 80239 were not run. There may be missed retail Post Offices near DIA or in 80225. The 16 included offices came from the collected locator set, not from a complete ZIP-by-ZIP census.
- **King Soopers service tags are incomplete on most store pages.** All 13 included stores tag a Money Services desk. Only Virginia Village (00150) tags check cashing. Eleven stores tag money orders; Union Station (00115) and Central Park (00123) do not. Bill pay and prepaid reload were not tagged on these store pages and were **not inferred** from the chain policy page, so those flags are false even though the chain offers those services at Money Services desks in general. Union Station and Central Park therefore have all four service flags set false; they are still listed because the official store page tags a Money Services desk. Confidence is `medium` on 12 King Soopers rows for that reason (`high` only for Virginia Village).
- **Walmart prepaid reload** is marked true only at Supercenter 5676, where load/unload was explicitly listed in the collection notes. Stores 3533 and 3566 are marked `prepaid_reload=false` because that service was not enumerated for those pages in the notes, even though both Supercenters list money services.
- **No latitude or longitude.** Coordinates were not recorded from the official pages and were left blank (null).
- **Western Union and MoneyGram stand-alone agent locations** were not collected as Denver pins (see Exclusions).
- **Inner-ring cities** (Aurora, Lakewood, Commerce City, Englewood, Wheat Ridge, Federal Heights) are not in this file.

## Decisions applied

- ACE: check-cashing-only national policy row is included and may point at ACE’s official locator URL. No ACE store rows in `denver.csv`. No loan products described or promoted.
- Hours labels (decided 2026-11-10) are computed only from published per-day hours. **Open evenings** is true when a weekday window is open after 17:00 America/Denver. **Open weekends** is true when Saturday or Sunday hours are published as an open window. The internal `after_hours` field is still computed (any published window outside Monday–Friday 09:00–17:00 America/Denver, including Saturday, Sunday, weekday evenings after 17:00, or weekday mornings before 09:00) but is not displayed. If hours had been missing, the flags would have been left null. No hours were missing on the 32 included rows.
- Service flags are copied only from what that location’s official page or official locator lists. A chain policy page is not enough to mark a specific desk.
- King Soopers national biller examples include non-Colorado names (for example City of Houston). Those are not a Denver biller list.
- USPS `check_cashing` is false. Locator pages in this collection list Domestic Money Orders and Inquiry Money Orders, not general check cashing. Cashing a *postal* money order at a Post Office is a money-order service (and is free, per the national policy page), not a reason to set `check_cashing=true`.

## Earlier blocked-source list (resolved for Walmart, King Soopers, and USPS Denver)

The first Step 4 pass could not read official locators or store pages in this environment (bot wall, timeout, or JS-only shells). Those pages were later opened in a browser on 2026-11-10, which is what filled `denver.csv` and re-verified Walmart fees. The earlier blocked-URL table is kept only as history:

| Source | Official URL | First-pass result | Status after browser pass |
|---|---|---|---|
| Walmart check cashing (policy) | https://www.walmart.com/cp/check-cashing/632047 | Bot wall / timeout | Re-verified 2026-11-10 |
| Walmart money orders (policy) | https://www.walmart.com/cp/money-orders/5791922 | Bot wall / timeout | Re-verified 2026-11-10 |
| Walmart store finder / store pages | https://www.walmart.com/store-directory/co and `/store/{id}-denver-co` | Bot wall | Three Supercenters added; two Neighborhood Markets excluded |
| King Soopers store search and store pages | https://www.kingsoopers.com/stores/search?searchText=Denver%2C%20CO | Timeout / HTTP 500 | 13 Denver-proper stores added; 00034 excluded |
| USPS Location Finder | https://tools.usps.com/locations/ | JS shell with no results in fetched HTML | 16 retail Post Offices added from official detail pages |
| Western Union location finder | https://location.westernunion.com/global-services/find-locations?WUCountry=us&WULanguage=en | JS app; no Denver results in fetched HTML | No stand-alone WU agent rows added (by decision) |
| MoneyGram location finder | https://www.moneygram.com/locations/us/en | JS “Loading”; no Denver results | No stand-alone MoneyGram agent rows added (by decision) |
| ACE store locator | https://www.acecashexpress.com/locations/ | JS page; no Denver results | Still omitted from `denver.csv` by decision |

King Soopers and Kroger **policy** pages (`/o/money-services/*` and `/i/money-services-faq`) had already been opened in the first pass.

## Uncertainties that still apply

1. **USPS coverage may be incomplete** because ZIP sweeps for 80202, 80205, 80222, and 80239 were not run (see Gaps). This replaces the earlier “zero Denver pins” item.

2. **GMF Finance (1439607)** was excluded by the default rule. Confirm if it should be treated as a retail Post Office on a later pass.

3. **MoneyGram $1,000 limit source.** The official product page (https://www.moneygram.com/us/en/services/money-orders) publishes neither a purchase fee nor a dollar limit. The $1,000 US limit is from the official blog article dated **July 1, 2026** (https://www.moneygram.com/blog/money-order-limits-what-you-need-to-know), which also says limits may vary slightly by state and retail location. Confidence is medium for that reason.

4. **PayNearMe range vs till price.** The official Support Center article (updated August 07, 2026 21:17; timezone not stated) publishes a **range** of $0–$5.99 that varies by biller and payment option. That is not a single Denver till fee.

5. **CheckFreePay has no official consumer fee page we could open.** King Soopers’ bill-pay page says payments are “Powered By” CheckFreePay Corporation and Western Union in a **Texas Finance Code** sentence. We did not treat that as a Colorado licensing statement, and we did not copy third-party biller pages (SiEnergy, APS, and similar) that mention CheckFreePay or Walmart bill-pay prices.

Other notes, not listed as a top decision unless needed:

- USPS military money-order fee ($0.85, issued by military facilities) is recorded for completeness; it is not a civilian Denver Post Office fee.
- Western Union purchase fees remain unpublished; refund processing fees ($0 / $5 / $15 by amount tier) **are** published on the official FAQ and are stored as `money_order_replacement`, not as a purchase fee. The FAQ also mentions a $15 administrative fee for a copy of a cashed money order (not given its own row).
- King Soopers prepaid FAQ still says there is “normally a small fee” to activate and reload, while the same official page publishes a fee table (including cash reload $3.95 for NetSpend and “Up to $4.95” for listed Green Dot / GO2bank cards). The table is the more specific official figure. This is not a card recommendation.
- Colorado DORA “What We Regulate” (https://banking.colorado.gov/consumers/what-we-regulate, opened in Step 4) states that the Division regulates state-chartered commercial banks and trust companies, and state-licensed money transmitters, and does not regulate national banks or credit unions. It still does **not** state a check-casher licensing rule. No license claim was added to the data.
- CFPB prepaid fee-types page was re-opened (https://www.consumerfinance.gov/ask-cfpb/what-types-of-fees-do-prepaid-cards-typically-charge-en-2053/); still last reviewed **Oct 31, 2024**. It lists fee *types*, not retailer dollar fees, so it is not a `fees.csv` row.
- Ingo official tiers were recorded from https://ingomoney.com/benefits-fees/. That guide is still scheduled to ship after the first wave is reviewed. No affiliate links.

## Open questions already decided (do not relitigate)

- ACE national policy page may link the official locator; city lists still omit those stores.
- `/guides/online-check-options/` ships after the first wave is reviewed; Ingo data is on file if that later guide needs it.
