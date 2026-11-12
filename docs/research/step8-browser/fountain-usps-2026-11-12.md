# Fountain, CO: USPS locator research (2026-11-12, America/Denver)

Research only. Nothing was built, committed, or deployed. No business was contacted. No browser was used. last_verified: 2026-11-12.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl, the same way as Northglenn and Erie. Searches ran at 5 and 15 miles around 80817 (Fountain), 80911 (Security-Widefield), 80906, 80910, 80916, 80913 (Fort Carson), 80925, 80929, 80840, 80908, 80926, 80902, 80809, 80864, 80808, 80915, 80909, 80903, 80905, 80914, 80930 (`sweep.py`, `sweep.out`), plus a second pass over 80918, 80920, 80922, 80923, 80927, 80938, 80939, 80951, 80907, 80904, 80919, 80831, 80921, 80917, 81008, 80928 (only 81008 added new records: 4 Pueblo offices). Together they returned **38 unique Post Office records**; every query returned JSON. Raw: `/workspace/step8fn/usps_all.json` (pass 1 only: `usps_all_pass1.json`); summary `usps_summ.txt`. A spot check of 80817 at 1/10/20/50 miles found no additional nearby record (the 50-mile list only adds distant towns past Pueblo/Canon City/Castle Rock).
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl at 15:39 MT: 1363906 Fountain, 1381131 Security, 1363752 Fort Carson, all HTTP 200 first try (`http.txt`, `d*.html`). Hours/services come from the official locator record those pages display. "Retail hours" = `BUSINESS` block only.
- **City limits:** all 38 addresses geocoded with the Census Geocoder address endpoint, Public_AR_Current / Current_Current, Incorporated Places + CDPs + Counties (`usps_geo.jsonl`); every USPS locator map point checked against the current benchmark (`coord.jsonl`); one-line 2020 + current checks for Fountain, Security, Fort Carson, and the GMF (`fbr.jsonl`). Joined view: `joined.txt`.
- **Structured output:** `/workspace/step8fn/fountain_usps_records.csv` / `.json` (all 38 records; ID, name, address, phone, URL, retail hours, money orders, HTTP status, geocode, map-point place, classification, shared-building IDs). Built by `build.py`.

## Candidate include (1)

| Office | Address | Phone | Services | Retail hours | Geocoder |
|---|---|---|---|---|---|
| Fountain (1363906) | 101 S Santa Fe Ave, Fountain 80817 | 719-382-4623 | Money orders, Domestic and Inquiry (MONEYORDERSDOM, MONEYORDERSINQ) | Mon-Fri 08:00-17:00, Sat 09:00-13:00, Sun closed | Current file: 101 S SANTA FE AVE, FOUNTAIN, CO, 80817, **Fountain city**, El Paso County. 2020 file agrees (Fountain city); official locator point (38.682837, -104.705178) → Fountain city, El Paso County. |

- URL: https://tools.usps.com/locations/details/1363906 (HTTP 200). verification_status: verified_official_locator.
- Open Saturdays. Weekday retail closes at **17:00**, so it is **not** open evenings (`open_after_1700_weekday` = false), same as Erie/Windsor. Window service hours match retail. Lobby and PO box access listed 00:01-23:59 daily (not retail). Last collection Mon-Fri 17:00, Sat 15:15.
- Other listed services (not Check Desk tracked): parcel lockers, general delivery, PO boxes, burial flags, duck stamps, greeting cards. No passport service and no self-service kiosk listed. No fax on the record.
- No duplicate, annex, or SDC record at 101 S Santa Fe Ave; no Fountain carrier annex appears in the locator.

## Holds

- **None.** The only Fountain-printed record geocodes inside Fountain city. No record printed with another city falls inside Fountain city by address geocode or by locator map point.

## Left out (not holds)

- **Security (1381131)**, 5755 Kittery Dr, printed Colorado Springs 80911, 719-390-3192; money orders, passports; Mon-Fri 09:00-17:00, Sat 08:00-14:00. Current and 2020 files: **Security-Widefield CDP** (unincorporated El Paso County); locator point agrees. Printed another city and outside Fountain → left out.
- **Fort Carson (1363752)**, 1611 McDonald St, printed Colorado Springs 80913, 719-579-9617; money orders; Mon-Fri 09:00-16:30, Sat 09:30-12:00. Current and 2020 files: **Fort Carson CDP**; locator point agrees. Left out.
- **General Mail Facility (1364595)**, 3655 E Fountain Blvd Ste 106, Colorado Springs 80910 (money orders, Mon-Fri to 18:00). No address match in current or 2020 file; locator point in Colorado Springs city. Left out (the street name "Fountain Blvd" is not the city).
- **West End Carrier Annex (1443285)**, 2410 Robinson St, Colorado Springs 80904: no BUSINESS (retail) hours and no money orders; Colorado Springs city. Left out. It does not share a building with West End 1439639 (204 S 25th St).
- Other Colorado Springs-printed offices (all money orders, all Colorado Springs city unless noted): Cimarron Hills 1440232 (Cimarron Hills CDP), Cheyenne Mountain 1357895, Antares 1353145, Colorado Springs main 1439566, North End 1375306, West End 1439639, Templeton 1384416, Rockrimmon 1379690, Briargate 1355790.
- Farther towns, each in its own municipality/CDP/unincorporated area: Manitou Springs, Cascade (Cascade-Chipita Park CDP), USAF Academy and Cadet (Air Force Academy CDP), Green Mountain Falls, Peyton (CDP), Monument, Palmer Lake, Woodland Park and Tamarac, Elbert (CDP), Larkspur, Victor, Penrose (CDP), Cripple Creek, Divide/Yoder/Rush (matched, unincorporated), Calhan, Ramah, and Pueblo/Belmont/Midtown/Sunset (Pueblo city; Midtown had no address match, locator point in Pueblo city).
- No shared-building or SDC duplicates were found among the 38 records.
- USPS contract postal units and Approved Postal Providers were not collected, same as earlier cities.

## Fetch failures

- None. All locator queries returned JSON; all three detail pages returned HTTP 200 on first try. No current-file address match for 2 records (General Mail Facility 1364595, Midtown 1373010); official locator points used, both outside Fountain.
