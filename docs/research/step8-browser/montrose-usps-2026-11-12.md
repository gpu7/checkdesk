# Montrose, CO: USPS locator research (2026-11-12, America/Denver)

Research only. Nothing was built, committed, or deployed. No business was contacted. No browser was used. last_verified: 2026-11-12. Official locator pages that were actually fetched are marked verification_status `verified_official_locator`.

This work did not start Louisville or any other city, and it did not touch other cities' files or worktrees (including site-src, data/locations, /workspace/step8jt, /workspace/step8ev, /workspace/step8fn, and the Erie/Northglenn/Lafayette/Fountain/Evans/Johnstown build worktrees). Existing Montrose Walmart/King Soopers research files under `/workspace/checkdesk/research/` were left unmodified.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl, the same way as Johnstown, Evans, Lafayette, Erie, and Fountain. First-pass searches ran at 5 and 15 miles around 81401 (Montrose), 81403 (Montrose; see ZIP note below), 81402 (Montrose PO Box ZIP), 81425 (Olathe), 81416 (Delta), 81432 (Ridgway), 81427 (Ouray), 81220 (Cimarron), 81415 (Crawford), 81419 (Hotchkiss), 81428 (Paonia), 81230 (Gunnison), plus other close official ZIPs confirmed from the Census 2025 ZCTA gazetteer and/or a successful locator query: 81410 (Austin), 81418 (Eckert), 81413 (Cedaredge), 81430 (Placerville), 81424 (Nucla), 81243 (Powderhorn), 81423 (Norwood), and 81527 (Whitewater). That first pass returned **34 unique Post Office records**. Because 81401 at 5 miles returned only 2 offices, a spot-check of 81401 at 10 miles (2 offices) and 20 miles (4 offices) was run; neither added a new office. A second pass at 5 and 15 miles around additional official nearby ZIPs 81431 (Redvale), 81435 (Telluride), 81434 (Somerset), 81426 (Ophir), 81235 (Lake City), 81646 (Molina), 81422 (Naturita), 81643 (Mesa), 81624 (Collbran), 81526 (Palisade), 81433 (Silverton), 81429 (Paradox), 81414 (Cory), 81420 (Lazear), 81210 (Almont), 81239 (Parlin), 81332 (Rico), 81224 and 81225 (Crested Butte area), 81522 (Gateway), 81411 (Bedrock), 81323 (Dolores), 81325 (Egnar), and 81248 (Sargents) added 19 farther offices. Grand Junction ZIPs were not given a dedicated widened pass: Grand Junction, Clifton, Fruitvale, Palisade, and the Grand Junction Carrier Annex already appeared in the first pass (Whitewater 81527 at 15 miles), and the second pass added nothing closer to Montrose. All **90** locator queries returned JSON (`sweep.out`); together they returned **53 unique Post Office records**. Raw data: `/workspace/step8mt/usps_all.json` (first pass also saved as `usps_all_pass1.json`). One-line summary: `usps_summ.txt`. Scripts: `sweep.py`, `sweep_pass2.py`.
- **Official Montrose ZIPs:** The USPS city/ZIP lookup tool was in outage during this research (HTTP 302 to USPS's apology page), so 81403 was confirmed from public official sources that did respond: it is a Census 2025 ZCTA (GEOID 81403), and the official USPS locator accepts 81403 and returns the Montrose-printed offices. 81402 has no ZCTA (PO Box ZIP) but is accepted by the locator, which centers it on the 321 S 1st St Montrose Post Office (0.03 miles).
- **Official pages:** `https://tools.usps.com/locations/details/<id>` was fetched with curl at about 3:50 PM MT for 1373677 Montrose, 1373668 Montrose Annex, 1375997 Olathe, 1360641 Delta, 1379328 Ridgway, and 1358060 Cimarron. All six returned HTTP 200 on the first try (`http.txt`, `d<id>.html`). Hours and services come from the official locator record that these pages display. "Retail hours" means the `BUSINESS` hours block only.
- **City limits:** all 53 records checked with the U.S. Census Geocoder address endpoint, Public_AR_Current / Current_Current, Incorporated Places, CDPs, and Counties layers (`usps_geo.jsonl`). Every official USPS locator map point was also checked against the current benchmark (`coord.jsonl`). For both Montrose-printed addresses and every current-file no-match, one-line lookups were run against the Census 2020 file and the current file (`fbr.jsonl`). No other-city office had a map point inside Montrose city, so no extra 2020 pass was needed for that reason. Joined view: `joined.txt`.
- **Structured output:** `/workspace/step8mt/montrose_usps_records.csv` / `.json` cover all 53 records (same core fields as Johnstown and Evans, plus `verification_status` set to `verified_official_locator` on the six official pages that were fetched). Built by `build.py`.

## Candidate include (1)

| Office | Address | Phone | Services | Retail hours | Geocoder |
|---|---|---|---|---|---|
| Montrose (1373677) | 321 S 1st St, Montrose 81401 | 970-249-6654 | Money orders, Domestic and Inquiry (MONEYORDERSDOM, MONEYORDERSINQ) | Mon-Fri 08:00-17:00, Sat 10:00-12:00, Sun closed | Current file: 321 S 1ST ST, MONTROSE, CO, 81401, **Montrose city**, Montrose County. The 2020 file agrees (Montrose city), and so does the official locator point (38.47857, -107.876618 → Montrose city, Montrose County). |

- Official URL: https://tools.usps.com/locations/details/1373677 — HTTP 200 on the first try; `verified_official_locator`.
- Open evenings: **no** (weekday retail closes at 17:00, not after 17:00).
- Open weekends: **yes** (Saturday 10:00-12:00).
- Money orders: **yes**.

## Left out, not a hold: Montrose Annex

- **Montrose Annex (1373668)**, 3025 Woodgate Rd, Montrose 81401, 970-252-7246. Official URL: https://tools.usps.com/locations/details/1373668 — HTTP 200 on the first try; `verified_official_locator`. Official printed city is Montrose. The current address file did not match this street. The 2020 file did: 3025 WOODGATE RD, MONTROSE, CO, 81401, **Montrose city**. The official locator point (38.451995, -107.86379) is also in **Montrose city**, Montrose County. The office has no `BUSINESS` (retail) hours and no money orders. It is a carrier/delivery unit (CARRIER, DELIVERYUNIT) with lobby, PO Box access, and hold-mail/pickup windows, not a retail office. Left out, not a hold. It does not share a building with the 321 S 1st St retail office.

## Holds

- None. No Montrose-printed office geocodes outside the City of Montrose, and no other-city-printed office has an address match or official map point inside the City of Montrose.

## Left-out nearby offices (not holds)

Printed with another city (or an unincorporated place name), and both the address geocode (where matched) and the locator point agree it is outside the City of Montrose. Nearest/most relevant:

- **Olathe (1375997)**, 215 N US Highway 50 Business Loop, Olathe 81425, 970-323-5936: Olathe town, Montrose County (address + point). The only other office in the 81401 15-mile search; a close miss, not a hold. Money orders; Mon-Fri 09:00-16:30, Sat 09:30-12:00. HTTP 200.
- **Delta (1360641)**, 360 Meeker St, Delta 81416, 970-874-2652: Delta city, Delta County (address + point). Money orders; Mon-Fri 09:00-17:00, Sat 10:00-12:00. HTTP 200.
- **Ridgway (1379328)**, 485 Clinton St, Ridgway 81432, 970-626-5576: address no match on the current or 2020 file; official locator point is in Ridgway town, Ouray County. Money orders; Mon-Fri 08:30-16:30, Sat 09:00-12:00. HTTP 200.
- **Cimarron (1358060)**, 82111 E US Highway 50, Cimarron 81220, 970-252-8366: address no match on the current or 2020 file; official locator point is in no incorporated place and no CDP (unincorporated Montrose County). Unincorporated places stay off the include list. Money orders; Mon-Fri 09:30-13:30, Sat 10:00-12:00. HTTP 200. The 81401 20-mile spot-check returned 4 offices and 0 new to the sweep; Cimarron is the nearest office east of town and was already found via 81220 in the first pass.
- **Ouray (1376452)**, 620 Main St, Ouray 81427: Ouray city (address + point). Money orders; Mon-Fri 08:45-16:15, Sat 09:00-11:30.
- **Crawford (1359758)**, 295 Highway 92, Crawford 81415: Crawford town (address + point). Money orders; Mon-Fri 08:30-12:00 and 12:30-16:00, Sat 09:00-12:00.
- Cedaredge (1357401, Cedaredge town), Hotchkiss (1367461, Hotchkiss town), Paonia (1376738, Paonia town), Austin (1353727; printed Austin, address + point in Orchard City town), Eckert (1362011; printed Eckert, address + point in Orchard City town): all outside Montrose city.
- Cory (1359343; address no match, point in Orchard City town) and Lazear (1370017; address no match, point in Lazear CDP): no retail `BUSINESS` hours and no money orders. Left out, not holds; neither is in Montrose city.
- Nucla (1375663, Nucla town), Naturita (1374469, Naturita town), Norwood (1375629, Norwood town), Redvale (1379005, Redvale CDP), all in or near western Montrose County but outside the City of Montrose.
- Farther records (Telluride, Ophir, Placerville, Silverton, Somerset, Gunnison, Almont, Parlin, Powderhorn, Whitewater, Palisade, Clifton, Fruitvale, Grand Junction, Grand Junction Carrier Annex, Lake City, Crested Butte, Molina, Mesa, Collbran, De Beque, Paradox, Bedrock, Pitkin, Rico, Gateway, Dolores, Lewis, Cortez, Yellow Jacket, Mancos, Egnar, Dove Creek, Sargents): outside the City of Montrose; see CSV.
- Carrier annexes / no-retail records in the sweep besides Montrose Annex: Grand Junction Carrier Annex 1469994 (Grand Junction city; no retail hours, no money orders), Cory 1359343, Lazear 1370017, and Powderhorn 1378272 (unincorporated Gunnison County; no `BUSINESS` hours, no money orders). None of these is a Montrose hold.
- No shared-building pairs in the sweep.
- Minor geocoder notes (not Montrose-include issues): Austin and Eckert print those place names but geocode (address + point) to Orchard City town. Ophir 1376191 matched the current address file but with no incorporated place; its locator point is also in no place (unincorporated San Miguel County). Current-file address no-matches were 13 of 53: Montrose Annex (resolved by the 2020 file and the official map point, both in Montrose city, and left out as a non-retail annex), plus Cory, Lazear, Ridgway, Cimarron, Almont, Parlin, Powderhorn, Paradox, Pitkin, Lewis, Yellow Jacket, and Dove Creek, all resolved by the official map point (and, for Yellow Jacket, by a 2020 match in unincorporated Montezuma County) and all outside the City of Montrose.

## Fetch failures

- None. All 90 locator queries returned JSON; all 6 detail pages returned HTTP 200 on the first try. Census geocoder: 40/53 current-file address matches; the 13 no-matches were resolved by the official locator map point and, where the 2020 file matched, by that file.
