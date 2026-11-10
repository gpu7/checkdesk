# Check Desk: launch checklist (Cloudflare DNS + AWS hosting)

This checklist matches how [erranddesk.com](https://erranddesk.com) was verified live on **2026-11-10** (America/Denver). It replaces the earlier draft that assumed Route 53 for DNS.

The intended domain is **checkdesk.com** (decided 2026-11-10). Registration and ownership of that domain are still Richard's step and are unconfirmed. **Do not run these steps until Richard gives a go-ahead to create resources.** Hosting and any AWS or registrar charges are Richard's decisions. Pax must not spend money, register a domain, create AWS resources, or change DNS as part of writing or reviewing this document.

Replace every remaining `YOUR_*` placeholder (`YOUR_BUCKET_NAME`, `YOUR_ACCOUNT_ID`, `YOUR_DISTRIBUTION_ID`) with values from the AWS or Cloudflare consoles. Never commit the filled-in account ID, bucket name, distribution ID, or API tokens. The hostname `checkdesk.com` is intended site configuration, not a secret.

## Target architecture (verified for Errand Desk, 2026-11-10)

- **Hosting:** a private S3 bucket (Block Public Access ON, default encryption SSE-S3, no static website hosting) served only through CloudFront with Origin Access Control (OAC).
- **Edge:** a CloudFront Function (runtime `cloudfront-js-2.0`, viewer request) from `cloudfront-function-index-rewrite.js`. With `APEX` set to `checkdesk.com`, it rewrites folder URLs to `index.html` and 301-redirects `www` to the apex.
- **TLS:** a free ACM public certificate in **us-east-1** for the apex and `www`, DNS-validated.
- **DNS:** the zone is hosted at Cloudflare (nameservers on Cloudflare). Records are **DNS-only** (grey cloud, **not** proxied). The apex uses a CNAME to `d….cloudfront.net`; Cloudflare flattens that apex CNAME, so public resolvers see CloudFront IPs as A records. `www` is also a DNS-only CNAME to the same distribution domain.
- **Analytics (optional):** Cloudflare Web Analytics. The public site token lives in `site-src/site.config.json` as `cf_analytics_token`. Leave it empty so the build emits no script.

Live Errand Desk response headers on 2026-11-10 showed `server: AmazonS3` and `via: … cloudfront.net`, with no `cf-ray`. That is the intended result: DNS points at CloudFront, and Cloudflare does not proxy the traffic.

## Who does each step

Every step is marked **Richard (console login)** or **Pax (after access granted)**. Until Richard grants scoped access (see [docs/HOSTING-HANDOFF.md](docs/HOSTING-HANDOFF.md)), Pax can only edit this repo, open pull requests, and build the site locally. Pax cannot create AWS resources or change DNS.

💲 marks a step that can cost money. Confirm current prices in the vendor console or on the vendor's pricing page at the time you do the work. Cost notes below are reused only where Errand Desk already sourced them; do not treat them as current quotes.

---

## 0. Prerequisites and decisions

**Who:** Richard (console login) for account, registration, and ownership. Pax does not buy or register the domain.

Before any console work, settle these:

1. **Domain name (`checkdesk.com`).** Decided 2026-11-10 as the intended production domain. `site-src/site.config.json` `base_url` is `https://checkdesk.com/`, and `cloudfront-function-index-rewrite.js` sets `APEX` to `checkdesk.com`. **Registration and ownership are still Richard's step and are unconfirmed.** This decision does not mean the domain has been purchased, transferred, or pointed at Cloudflare. You can still override `base_url` with `SITE_BASE_URL` at build time if needed.
2. **Registrar.** Either:
   - Register `checkdesk.com` with **Cloudflare Registrar**, which requires Cloudflare nameservers, or
   - Register (or keep) the domain at **another registrar** and point its nameservers at the Cloudflare zone you create in section B.
   - Do **not** use Route 53 as the authoritative DNS for this site. Errand Desk's original checklist assumed Route 53; the live site uses Cloudflare DNS instead. You do not need a Route 53 hosted zone, and you will not attach one to a CloudFront plan.
3. **Accounts.** Richard's AWS account (console access) and a Cloudflare account that can create a zone on the Free plan.
4. **Region rule.** Put the S3 bucket and the ACM certificate in **US East (N. Virginia) `us-east-1`**. CloudFront requires the certificate in that region.
5. **Plan eligibility (if you want CloudFront's flat-rate Free plan).** Errand Desk's checklist recorded that AWS's flat-rate plan documentation said accounts are not eligible for flat-rate plans while "Your account is using AWS Free Tier." In **Billing and Cost Management → Free Tier**, check whether the account is on the AWS Free Tier "free plan." If it is, either change plans first, or skip the flat-rate option in section F and use pay-as-you-go. Confirm the current rule in the console. Errand Desk's "about $0.50/month" pay-as-you-go estimate was mostly a Route 53 hosted zone, which this setup does not use.

---

## A. Cost safety net (AWS Budgets)

**Who:** Richard (console login)

This is the same $5 monthly safety net Errand Desk used, with the same source.

1. **Billing and Cost Management → Budgets → Create budget.**
   - Choose **Customize (advanced)** → **Cost budget** → Next. Name: `checkdesk-monthly`. Period: **Monthly**. Budget renewal: **Recurring**. Budgeting method: **Fixed**. Amount: **5.00** USD. Scope: all AWS services → Next.
   - **Add alert threshold:** 80% of budgeted amount, trigger **Actual**. Email: your address.
   - **Add alert threshold:** 100% of budgeted amount, trigger **Forecasted**. Email: your address.
   - Don't add budget "actions." Next → Create budget.
   - Cost: $0 per Errand Desk's source. AWS says "You can monitor and receive notifications on your budgets free of charge." Only action-enabled budgets beyond the first two ($0.10/day each) and Budgets Reports ($0.01 per report) cost money. Source: [AWS Budgets pricing](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/). Confirm on that page when you do the work.

---

## B. Cloudflare zone

**Who:** Richard (console login)

2. In the Cloudflare dashboard, **Add a site** (or add a zone) for `checkdesk.com`. Choose the **Free** plan.
3. Cloudflare will show two nameservers. If the domain is already at Cloudflare Registrar, nameservers should already be Cloudflare's. If the domain is at another registrar, change the domain's nameservers there to the two Cloudflare nameservers. Do not leave Route 53 or the registrar's default nameservers authoritative.
4. Wait until the Cloudflare zone status is **Active**. Do not create the apex/`www` CloudFront records yet (those come in section H, after the distribution exists). Do not orange-cloud / proxy any records you add later.

---

## C. ACM certificate (us-east-1, DNS validation in Cloudflare)

**Who:** Richard (console login) for the ACM request and for adding the validation records in Cloudflare. **Pax (after access granted)** could add the validation CNAMEs only if Richard later issues a Cloudflare API token scoped to DNS edit on this one zone; that access is optional and is not in place now.

5. In the AWS console, switch the region to **us-east-1**. Go to **Certificate Manager (ACM) → Request → Request a public certificate.**
   - Fully qualified domain names: `checkdesk.com`, then **Add another name**: `www.checkdesk.com`.
   - Validation: **DNS validation**. Key algorithm: default (RSA 2048) → Request.
   - Public certificates used with CloudFront are documented by AWS as no cost. Confirm if needed on [ACM pricing](https://aws.amazon.com/certificate-manager/pricing/). Don't create two certificates for the same names.
6. ACM will show one CNAME validation record per hostname. **There is no "Create records in Route 53" step for this setup.** Copy each CNAME name and value from ACM and add them **manually** in Cloudflare DNS:
   - Type: **CNAME**
   - Name and target: exactly as ACM shows (Cloudflare may display the name without the zone suffix)
   - Proxy status: **DNS only** (grey cloud). Do not proxy validation records; proxying can prevent ACM from seeing the CNAME and the certificate may never issue.
7. Wait until the certificate status is **Issued**. This is often minutes; it can take longer if the zone has only just become Active.

---

## D. S3 bucket

**Who:** Richard (console login)

8. **S3 → Create bucket** (region **us-east-1**). Type: General purpose. Name: a unique name you write down as `YOUR_BUCKET_NAME` (do not commit it).
   - Object Ownership: **ACLs disabled**. **Block all public access: ON** (leave all 4 boxes checked).
   - Versioning off, default encryption **SSE-S3** → Create bucket.
   - Do **not** enable "Static website hosting." CloudFront, not the S3 website endpoint, is what serves the site.
9. You can upload a first build now or wait until section I. If you upload early, still redo section I after the distribution and bucket policy are in place so cache headers and the invalidation are correct.

---

## E. CloudFront Function

**Who:** Richard (console login)

10. **CloudFront → Functions → Create function.** Name: `checkdesk-viewer-request`. Runtime: **cloudfront-js-2.0** → Create.
    - In **Build**, replace the code with the full contents of `cloudfront-function-index-rewrite.js` (the repo file already sets `APEX` to `checkdesk.com`) → **Save changes**.
    - **Test** tab, event type Viewer request:
      - Path `/about/`, host `checkdesk.com` → output URI should be `/about/index.html`.
      - Host `www.checkdesk.com` → 301 to `https://checkdesk.com/...` (path and query preserved).
    - **Publish** tab → **Publish function**.
    - Don't share this function with another distribution if your CloudFront plan forbids it.

---

## F. CloudFront distribution

**Who:** Richard (console login)

This follows the same CloudFront and WAF choices Errand Desk's checklist used, except you **do not** attach a Route 53 hosted zone.

11. **CloudFront → Distributions → Create distribution.**
    - If the wizard offers a plan, Errand Desk chose **Free ($0/month)** (the flat-rate Free plan), subject to the eligibility check in section 0. Confirm current plan names, limits, and prices in the console and on [CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/).
    - Distribution name: something like `checkdesk`. Type: **Single website or app**.
    - **Domain:** if offered, enter `checkdesk.com`, then add `www`.
12. **Origin:** Origin type **Amazon S3** → choose your bucket. Use **recommended origin settings**, which set up **Origin Access Control (OAC)**.
13. **Security:** if you are on a flat-rate plan, keep the AWS WAF protections the wizard offers. Errand Desk's checklist recorded that a WAF web ACL is required for flat-rate plans and is included at no extra cost, with the Free plan allowing up to 5 rules. Confirm current plan rules and cost. If you use pay-as-you-go instead, decide whether to keep WAF; it may not be included.
14. **TLS certificate:** choose the **Issued** ACM certificate from section C (covers both names) → create the distribution.
    - Write down `YOUR_DISTRIBUTION_ID` and the distribution domain name (`d….cloudfront.net`) in a local untracked note, not in git.
15. **Finish settings.** Open the distribution → **General → Settings → Edit**:
    - Alternate domain names (CNAMEs): `checkdesk.com` and `www.checkdesk.com`.
    - Custom SSL certificate: the section C certificate.
    - **Default root object:** `index.html`.
    - IPv6: **On**.
    - Save.
    - Then **Behaviors** → Default (*) → Edit:
      - Viewer protocol policy: **Redirect HTTP to HTTPS**.
      - Allowed HTTP methods: **GET, HEAD**.
      - Cache policy: **CachingOptimized** (keep what the wizard set, if present).
      - **Function associations → Viewer request:** Function type **CloudFront Functions**, function `checkdesk-viewer-request`.
      - Save.
16. **Custom error response (recommended, so the 404 page actually appears):** Error pages → create responses that map HTTP 403 and 404 to `/404.html` and return status 404. With OAC, a missing object is often a 403 from S3 unless you add this.
17. **Do not attach a Route 53 hosted zone** to the CloudFront plan. Errand Desk's original checklist did that to cover a $0.50/month hosted-zone fee. Check Desk's DNS is at Cloudflare, so that attachment does not apply.

---

## G. Bucket policy (from the template)

**Who:** Richard (console login)

18. CloudFront usually writes an OAC bucket policy when you use the recommended origin settings. Check **S3 → bucket → Permissions → Bucket policy**.
    - If it's empty or different, paste `s3-bucket-policy.json` with `YOUR_BUCKET_NAME`, `YOUR_ACCOUNT_ID` (12 digits, top-right account menu), and `YOUR_DISTRIBUTION_ID` filled in → Save. Fill those values only in the console (or a local untracked file), never in a commit.
    - **Block all public access** stays **ON**. The bucket must be reachable only through this CloudFront distribution.

---

## H. Cloudflare DNS records (DNS only)

**Who:** Richard (console login). **Pax (after access granted)** could create or update these records only with a later, optional Cloudflare API token scoped to DNS edit on this one zone.

19. In the Cloudflare DNS tab for `checkdesk.com`, wait until the CloudFront distribution is deployed, then create two records pointing at the distribution domain (`d….cloudfront.net`), **not** at individual CloudFront IPs (those IPs can change):

    | Name | Type | Target | Proxy status |
    |---|---|---|---|
    | `@` (apex) | CNAME | `d….cloudfront.net` | **DNS only** (grey cloud) |
    | `www` | CNAME | `d….cloudfront.net` | **DNS only** (grey cloud) |

    Cloudflare [flattens CNAME records at the zone apex](https://developers.cloudflare.com/dns/cname-flattening/), which is why an apex CNAME is allowed here. Public lookups of the apex may then show A (and possibly AAAA) records resolving to CloudFront IPs; that is expected.

20. **Warning: leave both records DNS only (grey cloud). Do not turn the Cloudflare proxy on (orange cloud).** Proxying would send visitors through Cloudflare instead of straight to CloudFront. That breaks this intended setup: TLS may no longer use the ACM certificate on CloudFront as designed, the `www` → apex function and HTTP → HTTPS redirects can misbehave, and responses would typically show a `cf-ray` header. Errand Desk's live, intended configuration is DNS-only.

    Also keep the ACM validation CNAMEs from section C on **DNS only**. Do not delete them while the certificate must stay issued.

---

## I. Upload the site and invalidate CloudFront

**Who:** Richard (console login). **Pax (after access granted)** could run the upload and invalidation with a later, optional IAM user or role limited to this one bucket and this one distribution (see [docs/HOSTING-HANDOFF.md](docs/HOSTING-HANDOFF.md)). There is no AWS CLI and no AWS credentials on the shared box as of 2026-11-10.

21. Build from the repo root: `python3 site-src/build.py`. Upload the **contents** of `site-src/public/` (or another `--out` directory), not the folder name itself. `index.html` must sit at the bucket root. Include `about/`, `disclosure/`, `privacy/`, `assets/`, `sitemap.xml`, `robots.txt`, `favicon.svg`, and `404.html`.
22. Set **Content-Type** and **Cache-Control** explicitly on every object:

    | Files | Content-Type | Cache-Control |
    |---|---|---|
    | `*.html` | `text/html; charset=utf-8` | `public, max-age=300` (5 minutes) |
    | `sitemap.xml` | `application/xml` | `public, max-age=300` |
    | `robots.txt` | `text/plain; charset=utf-8` | `public, max-age=300` |
    | Fingerprinted assets (`assets/*`, including `style.css` with the build's `?v=` query) | `text/css` for CSS | `public, max-age=31536000, immutable` (1 year) |
    | `favicon.svg` | `image/svg+xml` | `public, max-age=31536000, immutable` |

    The CSS link is cache-busted with `?v=<sha256 prefix>`, so the long cache is safe for that file.

23. Create a CloudFront invalidation for `/*` and wait until it completes.
24. An optional, **untested**, CI-free template is [`scripts/deploy.sh`](scripts/deploy.sh). It reads `CHECKDESK_BUCKET` and `CHECKDESK_DISTRIBUTION_ID` from the environment and does not hardcode IDs. It does not use `aws s3 sync --delete`. Richard should review and test it before relying on it. Do not put the env values in git.

---

## J. Verification

**Who:** Richard (console login) should confirm in a private window. Pax can run the public `curl` checks once the domain resolves, with no AWS or Cloudflare credentials.

25. After DNS has propagated, check:

    ```sh
    # Hosting path: CloudFront in front of S3, not Cloudflare-proxied.
    curl -sI https://checkdesk.com/
    # Expect: server: AmazonS3 (or similar S3/CloudFront server header)
    #         via: … cloudfront.net (or a Via header that names CloudFront)
    #         no cf-ray header

    curl -sI https://YOUR_BUCKET_NAME.s3.amazonaws.com/index.html
    # Expect: Access Denied (bucket is private)

    curl -sI https://www.checkdesk.com/about/
    # Expect: 301 Location: https://checkdesk.com/about/

    curl -sI http://checkdesk.com/
    # Expect: redirect to https://checkdesk.com/ (or https on the same path)

    curl -sI https://checkdesk.com/about/
    curl -sI https://checkdesk.com/about
    # Both should succeed (function rewrites to /about/index.html)

    curl -sI https://checkdesk.com/this-path-should-not-exist
    # Expect: 404 (if the custom error response in section F is set), body is 404.html

    curl -s https://checkdesk.com/ | grep -i disclaimer
    curl -s https://checkdesk.com/about/ | grep -i disclaimer
    # Site-wide disclaimer must be present
    ```

    Also open in a private window: `https://checkdesk.com/`, `/about/`, `/disclosure/`, `/privacy/`, `/sitemap.xml`, `/robots.txt`, and `/favicon.svg`. Confirm the padlock, the disclaimer on each HTML page, and that page canonicals and sitemap URLs use `https://checkdesk.com/`.

---

## K. Optional: Cloudflare Web Analytics

**Who:** Richard (console login) creates the analytics site and token. Pax can paste a token Richard provides, rebuild, and (after access granted) re-upload; until then, Richard does the upload and invalidation.

26. Only if Richard wants analytics: in the Cloudflare dashboard, create a **Web Analytics** site for `checkdesk.com`. This works on a site that is not proxied through Cloudflare (beacon JavaScript only).
27. Paste the public site token into `cf_analytics_token` in `site-src/site.config.json`. Leave the field empty to emit no script. This token is a public site token (it will appear in page HTML once enabled); still do not commit Cloudflare API tokens or other secrets.
28. Rebuild (`python3 site-src/build.py`), re-upload with the same Content-Type and Cache-Control rules as section I, and invalidate `/*`.

---

## L. What never goes in git

Do not commit any of the following (see also `.gitignore` and [SECURITY.md](SECURITY.md)):

- AWS access keys, secret keys, session tokens, or `.env` files
- `YOUR_ACCOUNT_ID`, `YOUR_BUCKET_NAME`, or `YOUR_DISTRIBUTION_ID` (including a filled-in `s3-bucket-policy.json`)
- Cloudflare API tokens, Global API keys, or origin CA keys
- Private keys, `.pem` files, or ACM certificate private material (ACM keeps the cert key; you should not have one to commit)
- A `scripts/deploy.sh` (or shell history) with real bucket or distribution values hardcoded
- Registrar or Cloudflare login cookies, and any local `aws.doc` notes that contain IDs or credentials

The public Cloudflare Web Analytics site token may be stored in `site.config.json` after Richard approves it. Filled-in infrastructure identifiers still stay out.

The chosen domain (`checkdesk.com`) is already set in `base_url` and in the CloudFront function. That is expected site configuration, not a secret. Still keep account, bucket, and distribution IDs out of the repo.
