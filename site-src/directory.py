"""Data-driven blocks for Check Desk pages (standard library only).

Pages can embed these comments; build.py replaces them at build time:

  <!--locations {"city": "denver", "service": "money_orders"} -->   location table for one service
  <!--locations {"city": "denver", "service": "any"} -->            every public row (hub)
  <!--locations {"city": "denver", "view": "evenings_weekends"} --> rows with Open evenings or Open weekends
  <!--count {"city": "denver", "service": "check_cashing"} -->      number of public rows (same filters)
  <!--count {"city": "denver", "label": "open_evenings"} -->        number of public rows with that label

Rules enforced here (see docs/CONTENT-PLAN.md section 3):
  * Only rows with verification_status verified_official_locator or verified_official_store_page,
    is_example=false, and a last_verified date are shown. Everything else is dropped.
  * Payday / title-loan brands never appear in a city list; the build fails if one is in the data.
  * Labels are "Open evenings" (open_after_1700_weekday) and "Open weekends" (open_weekends).
    The internal after_hours field is never displayed.
  * Fees come only from data/providers/fees.csv through site-src/fee-display.json. A brand/service
    pair with no published figure shows "Not published, call ahead". Nothing is estimated.
  * Sort: published fee lower first, then Open evenings, then Open weekends, then name A-Z.
"""
import csv, datetime, html, io, json, re
from pathlib import Path

PUBLIC_STATUSES = {"verified_official_locator", "verified_official_store_page"}
EXCLUDED_BRANDS = {"ace_cash_express", "check_into_cash", "speedy_cash", "moneytree", "advance_america"}
SERVICES = ("check_cashing", "money_orders", "bill_pay", "prepaid_reload")
SERVICE_LABEL = {"check_cashing": "Check cashing", "money_orders": "Money orders",
                 "bill_pay": "Bill pay", "prepaid_reload": "Prepaid reload (load and unload)"}
STATUS_LABEL = {"verified_official_store_page": "Checked on the official store page",
                "verified_official_locator": "Checked on the official USPS location page"}
DAYS = (("mon", "Mon"), ("tue", "Tue"), ("wed", "Wed"), ("thu", "Thu"), ("fri", "Fri"),
        ("sat", "Sat"), ("sun", "Sun"))
STALE_DAYS = 90
NOT_PUBLISHED = "Not published, call ahead"

esc = lambda s: html.escape(s or "", quote=True)


def _read_csv(path):
    lines = [l for l in path.read_text(encoding="utf-8").splitlines() if not l.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines))))


class Directory:
    def __init__(self, repo_root, site_root):
        self.repo = Path(repo_root)
        self.fees = {r["id"]: r for r in _read_csv(self.repo / "data" / "providers" / "fees.csv")}
        self.display = json.loads((Path(site_root) / "fee-display.json").read_text())
        self.display.pop("_notes", None)
        self.cities = {}
        self.warnings = []
        for svc, brands in self.display.items():
            if svc not in SERVICES:
                raise SystemExit(f"fee-display.json: unknown service {svc!r}")
            for brand, d in brands.items():
                for fid in [d.get("sort_fee_id")] + d.get("fee_ids", []):
                    if fid and fid not in self.fees:
                        raise SystemExit(f"fee-display.json: {svc}/{brand} cites unknown fee id {fid!r}")
                if d.get("sort_fee_id") is None and NOT_PUBLISHED not in d["text"]:
                    raise SystemExit(f"fee-display.json: {svc}/{brand} has no published fee, so its text must say '{NOT_PUBLISHED}'")

    # ---------- data ----------
    def rows(self, city):
        if city not in self.cities:
            path = self.repo / "data" / "locations" / f"{city}.csv"
            out = []
            for r in _read_csv(path):
                if r["brand"] in EXCLUDED_BRANDS:
                    raise SystemExit(f"{path}: payday/title-loan brand {r['brand']} must not be in a city list ({r['id']})")
                if (r["is_example"].lower() != "false" or r["verification_status"] not in PUBLIC_STATUSES
                        or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["last_verified"])):
                    continue
                out.append(r)
            self.cities[city] = out
        return self.cities[city]

    def fee_entry(self, service, brand):
        return self.display.get(service, {}).get(brand)

    def sort_fee(self, row, service):
        services = SERVICES if service == "any" else (service,)
        best = None
        for s in services:
            if row[s] != "true":
                continue
            d = self.fee_entry(s, row["brand"])
            if not d or not d.get("sort_fee_id"):
                continue
            f = self.fees[d["sort_fee_id"]]
            if f["fee_unit"] not in ("usd_flat", "usd_maximum", "usd_range"):
                raise SystemExit(f"sort fee {f['id']} must be a dollar figure, not {f['fee_unit']}")
            v = float(f["fee_amount_max"] or f["fee_amount_min"])
            best = v if best is None else min(best, v)
        return best

    def select(self, city, service=None, view=None, label=None):
        rows = self.rows(city)
        if service and service != "any":
            rows = [r for r in rows if r[service] == "true"]
        if view == "evenings_weekends":
            rows = [r for r in rows if (r["open_after_1700_weekday"] == "true" or r["open_weekends"] == "true")
                    and any(r[s] == "true" for s in SERVICES)]
        if label == "open_evenings":
            rows = [r for r in rows if r["open_after_1700_weekday"] == "true"]
        if label == "open_weekends":
            rows = [r for r in rows if r["open_weekends"] == "true"]
        key_service = service or "any"

        def key(r):
            fee = self.sort_fee(r, key_service)
            k = [fee is None, fee if fee is not None else 0,
                 r["open_after_1700_weekday"] != "true", r["open_weekends"] != "true"]
            if view == "evenings_weekends":
                k.append(-latest_weekday_close(r))
            k.append(r["name"].casefold())
            return k
        return sorted(rows, key=key)

    def check_stale(self, rows, lastmod, page):
        ref = datetime.date.fromisoformat(lastmod)
        for r in rows:
            age = (ref - datetime.date.fromisoformat(r["last_verified"])).days
            if age > STALE_DAYS:
                self.warnings.append(f"WARNING {page}: {r['id']} last_verified {r['last_verified']} is {age} days older than the page lastmod")

    # ---------- rendering ----------
    def render_table(self, opts, lastmod, page):
        rows = self.select(opts["city"], opts.get("service"), opts.get("view"))
        if not rows:
            raise SystemExit(f"{page}: locations block {opts} matched no public rows; do not publish an empty list")
        self.check_stale(rows, lastmod, page)
        service = opts.get("service") or "any"
        out = ['<div class="table-scroll">', '<table class="locations">',
               '<thead><tr><th scope="col">Location</th><th scope="col">Services listed on the official page</th>'
               '<th scope="col">Published hours</th><th scope="col">Published fee (chain policy)</th>'
               '<th scope="col">Last verified</th></tr></thead>', "<tbody>"]
        for r in rows:
            out.append(self._row(r, service))
        out += ["</tbody>", "</table>", "</div>",
                f'<p class="small">{len(rows)} location{"s" if len(rows) != 1 else ""} shown. Sorted by published fee '
                '(lower first; locations whose brand does not publish a fee come last), then Open evenings, '
                'then Open weekends, then name.'
                + (" Within that, later weekday closing time comes first." if opts.get("view") == "evenings_weekends" else "")
                + "</p>"]
        return "\n".join(out)

    def _row(self, r, service):
        addr = f'{esc(r["address"])}, {esc(r["city"])}, {esc(r["state"])} {esc(r["zip"])}'
        phone = f'<br><span class="small">Phone (from the official page): {esc(r["phone"])}</span>' if r["phone"] else ""
        loc = f'<th scope="row">{esc(r["name"])}<br><span class="addr">{addr}</span>{phone}</th>'
        offered = [s for s in SERVICES if r[s] == "true"]
        if offered:
            svc = ", ".join(SERVICE_LABEL[s] for s in offered)
        else:
            svc = ("<span class=\"unk\">The official store page lists a Money Services desk but does not list "
                   "which services. Call ahead.</span>")
        labels = []
        if r["open_after_1700_weekday"] == "true":
            labels.append('<span class="label">Open evenings</span>')
        if r["open_weekends"] == "true":
            labels.append('<span class="label">Open weekends</span>')
        hours = format_hours(r)
        hours_cell = f'{hours}<br>{" ".join(labels)}' if labels else hours
        desk = ""
        if r["brand"] in ("walmart", "king_soopers"):
            desk = '<br><span class="small">Store hours. Money desk hours are not published; call ahead.</span>'
        fee = self._fee_cell(r, service, offered)
        verified = (f'<time datetime="{esc(r["last_verified"])}">{esc(r["last_verified"])}</time><br>'
                    f'<span class="small">{esc(STATUS_LABEL[r["verification_status"]])}: '
                    f'<a href="{esc(first_url(r["source_urls"]))}">source</a></span>')
        return (f"<tr>{loc}<td>{svc}</td><td>{hours_cell}{desk}</td><td>{fee}</td><td>{verified}</td></tr>")

    def _fee_cell(self, r, service, offered):
        services = offered if service == "any" else [service]
        if not services:
            return NOT_PUBLISHED + "."
        parts = []
        for s in services:
            d = self.fee_entry(s, r["brand"])
            if d is None:
                raise SystemExit(f"fee-display.json has no entry for {s}/{r['brand']} (row {r['id']})")
            fid = d.get("sort_fee_id") or d["fee_ids"][0]
            src = self.fees[fid]["source_url"]
            text = d["short"] if service == "any" else d["text"]
            prefix = f"{SERVICE_LABEL[s]}: " if service == "any" else ""
            parts.append(f'{prefix}{esc(text)} <a class="small" href="{esc(src)}">official page</a>')
        return "<br>".join(parts)

    def count(self, opts):
        return str(len(self.select(opts["city"], opts.get("service"), opts.get("view"), opts.get("label"))))

    def expand(self, body, lastmod, page):
        def loc(m):
            return self.render_table(json.loads(m.group(1)), lastmod, page)

        def cnt(m):
            return self.count(json.loads(m.group(1)))
        body = re.sub(r"<!--locations\s*(\{.*?\})\s*-->", loc, body, flags=re.S)
        body = re.sub(r"<!--count\s*(\{.*?\})\s*-->", cnt, body, flags=re.S)
        return body


def first_url(s):
    return re.split(r"[\s;|]+", s.strip())[0]


def _t(hhmm):
    h, m = (int(x) for x in hhmm.split(":"))
    suffix = "a.m." if h < 12 or h == 24 else "p.m."
    h12 = h % 12 or 12
    return f"{h12}:{m:02d} {suffix}" if m else f"{h12} {suffix}"


def _span(v):
    v = (v or "").strip()
    if not v:
        return "not published"
    if v == "closed":
        return "closed"
    spans = []
    for part in v.split(","):  # split windows, e.g. a published midday closure
        a, b = part.split("-")
        spans.append(f"{_t(a)}–{_t(b)}")
    return ", ".join(spans)


def format_hours(r):
    vals = [(lab, r[f"hours_{d}"]) for d, lab in DAYS]
    if all(v == vals[0][1] for _, v in vals):
        return f"Daily {_span(vals[0][1])}"
    groups = []
    for lab, v in vals:
        if groups and groups[-1][2] == v:
            groups[-1][1] = lab
        else:
            groups.append([lab, lab, v])
    return "; ".join((f"{a}–{b}" if a != b else a) + f" {_span(v)}" for a, b, v in groups)


def latest_weekday_close(r):
    best = 0
    for d in ("mon", "tue", "wed", "thu", "fri"):
        v = r[f"hours_{d}"]
        if v and v != "closed":
            h, m = (int(x) for x in v.split(",")[-1].split("-")[1].split(":"))
            best = max(best, h * 60 + m)
    return best
