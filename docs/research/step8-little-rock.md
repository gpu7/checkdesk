# Step 8: Little Rock, AR (2026-11-15, America/Denver)

**Rows:** 10 (ten Post Offices). First city of the approved Arkansas batch (Little Rock, Fayetteville, Fort Smith, Springdale, Jonesboro; one city at a time). Little Rock is an incorporated city in Pulaski County (Census "Little Rock city", GEOID 0541000; county Pulaski County, GEOID 05119), not a consolidated city-county. North Little Rock is a separate incorporated city in the same county. Only addresses inside Little Rock city whose official printed city is Little Rock are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable (the press-and-hold / PerimeterX block was still in place on 2026-11-15).

**Counts:** 10 locations; 10 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 2 Open evenings, 7 Open weekends. The money-orders page lists 10. The after-hours page lists 7 (Asher, Brady, Southside, Forest Park, Industrial, Westside, and Chenal). Westside and Chenal are the two evening offices (weekday closes 18:00 and 17:30). State Capitol, Hillcrest, and Otter Creek appear on the hub and money-orders pages but not on after-hours. Otter Creek has a weekday midday closure. No check-cashing or bill-pay page (zero listings). Holds: GMF Box Section, Mabelvale, and Alexander. In-city, not listed (no money-order tags): Brady Annex and the Little Rock Post Office at 600 E Capitol Ave.

Hours are copied as published and are local Little Rock time (Central Time). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as the Arizona cities. Pass 1: 5 and 15 miles around every official Little Rock ZIP (36 codes listed for Little Rock, AR by ZIP-Codes.com from USPS data last updated 2026-11-01, including 11 North Little Rock / Sherwood codes that also appear on that page) and nearby official ZIPs for Alexander, Benton, Bryant, Cabot, Conway, England, Jacksonville, Lonoke, Mabelvale / Shannon Hills, Wrightsville, and Pine Bluff (58 ZIPs, 116 queries, 69 unique records). Pass 2: 1, 2, 3, 10, and 20 mile widenings on edge Little Rock and fringe ZIPs (70 queries, 20 added records). Total 89 records (`step8-browser/little-rock-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 89 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/little-rock-usps-2026-11-15.md`. The Arkansas five-city Census memo is at `arkansas-cities-census-2026-11-15.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 89 addresses and all 89 official locator map points on both benchmarks (`step8-browser/little-rock-usps-geocoder-2026-11-15.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (10 listed)

All ten offices have printed city Little Rock and address plus official map point in Little Rock city on both Census files. All ten list Domestic and Inquiry Money Orders.

Holds and in-city exclusions are listed in the city-page "not listed" section and in `little-rock-usps-2026-11-15.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/little-rock.csv` and `/little-rock/`, `/little-rock/money-orders/`, and `/little-rock/after-hours/` pages.
- An Arkansas heading is added on the home "Start here" list and on `/cities/`, after Arizona and before Colorado (alphabetical: Alabama, Alaska, Arizona, Arkansas, Colorado). Little Rock is the first Arkansas city on those lists. Home and `/cities/` meta descriptions now include Little Rock, Arkansas. No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
