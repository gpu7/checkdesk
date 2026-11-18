# Santa Fe, New Mexico USPS research (2026-11-17, America/Denver)

Fourth New Mexico city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Santa Fe city, GEOID 3570500, population 89,837, in Santa Fe County (GEOID 35049). Official listed pages print Santa Fe, NM. This is not Tesuque, not Eldorado at Santa Fe, not Agua Fria, and not Española. Hours are Mountain Time (49 CFR 71.8; the 71.7 Central–Mountain boundary follows the Texas–New Mexico line; the 71.9 Mountain–Pacific boundary does not enter New Mexico). OpenStreetMap was not used. Raw data: `/workspace/step8nm/`. Classification: `/workspace/checkdesk/research/new-mexico-geocode-classify-2026-11-17.md`. Address retries: `/workspace/step8nm/retry_nomatch.jsonl`. Locator passes and official pages are the shared New Mexico sweep (292 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (4)

- Coronado (1359309, 2071 S PACHECO ST, SANTA FE 87505). Lists money orders. All four Census legs are in Santa Fe city. BUSINESS hours: weekdays 8:30 a.m. to 5:30 p.m., Saturday 9:00 a.m. to 3:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- De Vargas (1360767, 534 N GUADALUPE ST, SANTA FE 87501). Lists money orders. All four Census legs are in Santa Fe city. BUSINESS hours: weekdays 10:00 a.m. to 4:00 p.m., Saturday 10:00 a.m. to 3:00 p.m., Sunday closed. Labeled Open weekends.
- Santa Fe (1380752, 120 S FEDERAL PL STE 101, SANTA FE 87501). Lists money orders. All four Census legs are in Santa Fe city. BUSINESS hours: weekdays 8:30 a.m. to 5:30 p.m., Saturday 9:00 a.m. to 3:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- Santa Fe Place (1385970, 4250 CERRILLOS RD STE 1250, SANTA FE 87507). Weekdays 11:00 a.m. to 1:00 p.m. and 1:30 p.m. to 5:00 p.m.; Saturday 11:00 a.m. to 3:00 p.m. A 5:00 p.m. close does not count as Open evenings. Labeled Open weekends. Map-point fallback (see below).

### Santa Fe Place (1385970, 4250 CERRILLOS RD STE 1250, SANTA FE 87507)

The official page already prints Santa Fe, NM, and lists money orders. The address 4250 Cerrillos Rd Ste 1250, Santa Fe, NM 87507 did not match on the current Census file and did not match on the 2020 Census file. 48 street-name, city, and ZIP variants were tried on both vintages (official street forms such as 4250 CERRILLOS RD STE 1250, 4250 CERRILLOS RD, 4250 CERRILLOS ROAD, 4250 Cerrillos Rd Ste 1250, and 4250 CERRILLOS RD STE 1250; cities Santa Fe and SANTA FE; ZIPs 87507 and blank). None matched, and none snapped to a different address near the official map point. The official USPS locator map point (35.636024, -106.014372) places it in Santa Fe city, Santa Fe County, on both the current and 2020 benchmarks. Map-point fallback is allowed because the printed city already matches and the official point is inside the city. Raw: `/workspace/step8nm/retry_nomatch.jsonl`.

## Held

- Santa Fe Main (1442408, 120 S FEDERAL PL STE 101, SANTA FE 87501). Prints Santa Fe, NM, and all four Census legs are in Santa Fe city, but the official page does not list money orders and has no BUSINESS hours block. This is the same street address as the listed Santa Fe office at 120 S Federal Pl Ste 101.

No other office in the New Mexico locator sweep geocodes into Santa Fe city. Offices in Arizona, Colorado, Texas, Oklahoma, and Utah appear in the sweep but stay off this list. Albuquerque, Las Cruces, Rio Rancho, and Roswell stay on separate lists.

## Result

4 listed Post Offices, all with money orders, including 1 map-point fallback (Santa Fe Place). 2 Open evenings (Coronado and Santa Fe, until 5:30 p.m.). 4 Open weekends, Saturday only. Hours labeled Mountain Time. 1 hold (Santa Fe Main, no money orders, same address as the listed Santa Fe office).

## Site changes in this PR

- New `data/locations/santa-fe.csv` and `/santa-fe/`, `/santa-fe/money-orders/`, and `/santa-fe/after-hours/` pages.
- Santa Fe is inserted under the existing New Mexico section after Rio Rancho on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/santa-fe/` slug is new and does not collide with an existing page.
