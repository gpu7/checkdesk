#!/usr/bin/env python3
"""Tiny static builder for Check Desk: wraps src/pages/**.html in src/layout.html -> public/ (or --out DIR).

Each page starts with <!--meta {json} --> (title, description, nav, optional lastmod, optional noindex,
optional schema: "website" | "article" | "collection" | "page").
URL scheme: src/pages/index.html -> /, src/pages/about.html -> /about/.
Config: site.config.json (base_url, default_lastmod, disclaimer_updated, optional cf_analytics_token).
Env SITE_BASE_URL overrides base_url.
Also writes public/sitemap.xml and public/robots.txt, and copies src/static/* to the site root.

The site-wide disclaimer in src/partials/disclaimer.html is injected into every built page
via the {{disclaimer}} token in src/layout.html. The build fails if that token is missing
or if any output page lacks the required disclaimer sentence.
"""
import argparse, calendar, hashlib, html as htmlmod, json, os, re, shutil, sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(description="Build the Check Desk static site.")
ap.add_argument("--out", help="output directory (default: public/ next to build.py). It is deleted and rebuilt.")
args = ap.parse_args()
SRC = ROOT / "src"
OUT = Path(args.out).resolve() if args.out else ROOT / "public"
if OUT in (ROOT, SRC) or OUT in ROOT.parents:
    raise SystemExit(f"refusing to use {OUT} as output dir")

cfg = json.loads((ROOT / "site.config.json").read_text())
BASE = os.environ.get("SITE_BASE_URL", cfg["base_url"]).rstrip("/") + "/"
CF_TOKEN = cfg.get("cf_analytics_token", "").strip()
if CF_TOKEN and not re.fullmatch(r"[A-Za-z0-9]+", CF_TOKEN):
    raise SystemExit("cf_analytics_token looks malformed")
# Cloudflare Web Analytics (cookie-free). Emitted only when a token is configured; otherwise nothing.
ANALYTICS = (
    f"<script defer src=\"https://static.cloudflareinsights.com/beacon.min.js\" "
    f"data-cf-beacon='{{\"token\": \"{CF_TOKEN}\"}}'></script>\n"
    if CF_TOKEN else ""
)

DISCLAIMER_SENTENCE = "Policies and fees change. Call the location before you go. Check Desk is an information directory, not financial advice."

def format_disclaimer_date(iso):
    """Turn YYYY-MM-DD into 'Mon D, YYYY' (e.g. 2026-11-10 -> Nov 10, 2026)."""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", iso):
        raise SystemExit(f"disclaimer_updated must be YYYY-MM-DD, got {iso!r}")
    y, m, d = (int(p) for p in iso.split("-"))
    return f"{calendar.month_abbr[m]} {d}, {y}"

def load_disclaimer():
    path = SRC / "partials" / "disclaimer.html"
    text = path.read_text()
    updated = cfg.get("disclaimer_updated", cfg["default_lastmod"])
    label = format_disclaimer_date(updated)
    text = (text.replace("{{disclaimer_updated}}", updated)
                .replace("{{disclaimer_updated_label}}", label))
    leftover = re.findall(r"\{\{[^}]+\}\}", text)
    if leftover:
        raise SystemExit(f"unreplaced token in disclaimer partial: {leftover}")
    if DISCLAIMER_SENTENCE not in text:
        raise SystemExit("disclaimer partial is missing the required sentence")
    return text

layout = (SRC / "layout.html").read_text()
if "{{disclaimer}}" not in layout:
    raise SystemExit("src/layout.html must contain {{disclaimer}} so every page gets the site-wide disclaimer")
CSS_V = hashlib.sha256((SRC / "assets" / "style.css").read_bytes()).hexdigest()[:10]
layout = layout.replace('href="/assets/style.css"', f'href="/assets/style.css?v={CSS_V}"')
DISCLAIMER = load_disclaimer()
layout = layout.replace("{{disclaimer}}", DISCLAIMER)
# 404.html is copied from static/ and is not wrapped by this layout; keep its wording in sync by hand.

SITE_NAME = "Check Desk"
HAS_OG_IMAGE = (SRC / "static" / "og-image.png").is_file()
OG_IMAGE = BASE + "og-image.png"
OG_ALT = "Check Desk: sourced, dated check cashing, money order, and bill-pay information"
ORG = {"@type": "Organization", "name": SITE_NAME, "url": BASE}


def attr(v):
    return htmlmod.escape(v, quote=True)


def social_tags(meta, url):
    kind = "article" if meta.get("schema") == "article" else "website"
    t, d = attr(meta["title"]), attr(meta["description"])
    tags = [
        f'<meta property="og:type" content="{kind}">',
        f'<meta property="og:site_name" content="{SITE_NAME}">',
        f'<meta property="og:title" content="{t}">',
        f'<meta property="og:description" content="{d}">',
        f'<meta property="og:url" content="{url}">',
        '<meta property="og:locale" content="en_US">',
    ]
    if HAS_OG_IMAGE:
        tags[5:5] = [
            f'<meta property="og:image" content="{OG_IMAGE}">',
            '<meta property="og:image:type" content="image/png">',
            '<meta property="og:image:width" content="1200">',
            '<meta property="og:image:height" content="630">',
            f'<meta property="og:image:alt" content="{attr(OG_ALT)}">',
        ]
        tags += [
            '<meta name="twitter:card" content="summary_large_image">',
            f'<meta name="twitter:title" content="{t}">',
            f'<meta name="twitter:description" content="{d}">',
            f'<meta name="twitter:image" content="{OG_IMAGE}">',
            f'<meta name="twitter:image:alt" content="{attr(OG_ALT)}">',
        ]
    else:
        tags += [
            '<meta name="twitter:card" content="summary">',
            f'<meta name="twitter:title" content="{t}">',
            f'<meta name="twitter:description" content="{d}">',
        ]
    return "\n".join(tags) + "\n"


def plain(fragment):
    """Visible text of an HTML fragment, minus citation markers (<sup>...</sup>)."""
    x = re.sub(r"<sup>.*?</sup>", "", fragment, flags=re.S)
    x = htmlmod.unescape(re.sub(r"<[^>]+>", "", x))
    x = re.sub(r"\s+", " ", x).strip()
    return re.sub(r"\s+([.,;:])", r"\1", x)


def faq_pairs(body):
    """Question disclosures only. A <details> list that is not a question is not an FAQ."""
    pairs, seen = [], set()
    for q, a in re.findall(r"<details><summary>(.*?)</summary>(.*?)</details>", body, re.S):
        question, answer = plain(q), plain(a)
        if not question.endswith("?"):
            continue
        if not answer:
            raise SystemExit(f"FAQ question has an empty answer: {question}")
        key = question.casefold()
        if key in seen:
            raise SystemExit(f"duplicate FAQ question: {question}")
        seen.add(key)
        pairs.append((q, a))
    return pairs


def jsonld(meta, body, url, lastmod):
    graph, kind = [], meta.get("schema")
    if kind == "website":
        graph.append({"@type": "WebSite", "name": SITE_NAME, "url": BASE, "description": meta["description"],
                      "inLanguage": "en-US", "publisher": ORG})
    elif kind == "article":
        h1 = plain(re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S).group(1))
        node = {"@type": "Article", "headline": h1, "description": meta["description"], "url": url,
                "mainEntityOfPage": url, "dateModified": lastmod,
                "inLanguage": "en-US", "author": ORG, "publisher": ORG}
        if HAS_OG_IMAGE:
            node["image"] = OG_IMAGE
        graph.append(node)
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": h1, "item": url}]})
        faqs = faq_pairs(body)
        if faqs:
            graph.append({"@type": "FAQPage", "url": url, "mainEntity": [
                {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                for q, a in faqs]})
    elif kind == "collection":
        h1 = plain(re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S).group(1))
        graph.append({"@type": "CollectionPage", "name": h1, "description": meta["description"], "url": url,
                      "dateModified": lastmod, "inLanguage": "en-US", "publisher": ORG})
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": h1, "item": url}]})
    if not graph:
        return ""
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    data = data.replace("</", "<\\/")  # never close the script element early
    return f'<script type="application/ld+json">\n{data}\n</script>\n'


def page_path(page):
    rel = page.relative_to(SRC / "pages").with_suffix("")
    if str(rel) == "index":
        return ""
    if rel.name == "index":
        return f"{rel.parent.as_posix()}/"
    return f"{rel.as_posix()}/"


if OUT.exists():
    shutil.rmtree(OUT)
shutil.copytree(SRC / "assets", OUT / "assets")
static = SRC / "static"
if static.exists():
    for f in static.glob("*"):
        shutil.copy(f, OUT / f.name)

pages = []
for page in sorted((SRC / "pages").rglob("*.html")):
    raw = page.read_text()
    m = re.match(r"\s*<!--meta\s*(\{.*?\})\s*-->", raw, re.S)
    if not m:
        raise SystemExit(f"missing <!--meta {{...}} --> in {page}")
    meta = json.loads(m.group(1))
    body = raw[m.end():].strip()
    pages.append((page_path(page), meta, body))

NAV_KEYS = ("about", "disclosure", "privacy")
urls = []
for path, meta, body in pages:
    dest = OUT / path / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    url, lastmod = BASE + path, meta.get("lastmod", cfg["default_lastmod"])
    html = (layout.replace("{{title}}", meta["title"])
            .replace("{{description}}", attr(meta["description"]))
            .replace("{{canonical}}", url)
            .replace("{{social}}", social_tags(meta, url))
            .replace("{{jsonld}}", jsonld(meta, body, url, lastmod)))
    for key in NAV_KEYS:
        token = "{{nav_" + key + "}}"
        html = html.replace(token, ' aria-current="page"' if meta.get("nav") == key else "")
    html = html.replace("{{analytics}}", ANALYTICS).replace("{{content}}", body)
    leftover = [tok for tok in re.findall(r"\{\{[^}]+\}\}", html)]
    if leftover:
        raise SystemExit(f"unreplaced layout tokens on {path or '/'}: {leftover}")
    if DISCLAIMER_SENTENCE not in html:
        raise SystemExit(f"disclaimer missing from built page {path or '/'}")
    dest.write_text(html)
    print("built", dest.relative_to(OUT))
    if not meta.get("noindex"):
        urls.append((url, lastmod))

# Confirm every HTML file in the output, including the static 404, carries the sentence.
missing = []
for html_path in OUT.rglob("*.html"):
    text = html_path.read_text()
    if DISCLAIMER_SENTENCE not in text:
        missing.append(str(html_path.relative_to(OUT)))
if missing:
    raise SystemExit("disclaimer sentence missing from: " + ", ".join(missing))

sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"  <url><loc>{escape(u)}</loc><lastmod>{d}</lastmod></url>" for u, d in urls]
sm.append("</urlset>")
(OUT / "sitemap.xml").write_text("\n".join(sm) + "\n")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
print(f"built sitemap.xml ({len(urls)} urls) and robots.txt, base {BASE}")
print(f"disclaimer present on {sum(1 for _ in OUT.rglob('*.html'))} HTML files")
