# Check Desk: AWS launch checklist (Richard does each step in the AWS console)

This is a future deploy checklist, adapted from Errand Desk. **Do not run these steps as part of Step 2.** Domain, hosting, and any AWS charges are Richard's decisions. The agent must not spend money or create paid resources.

Replace every `YOUR_*` placeholder with values from the AWS console. Never commit the filled-in account ID, bucket name, or distribution ID.

Region rule: put the S3 bucket and the ACM certificate in **US East (N. Virginia) `us-east-1`**. CloudFront requires the certificate in that region.

💲 marks a step that can cost money. Confirm current AWS prices in the console or on AWS's pricing pages at the time you do the work; do not rely on remembered figures.

**Before you start, check plan eligibility.** If the account is still on the AWS Free Tier "free plan," a flat-rate CloudFront plan may not be available until you change plans, or you can stay on pay-as-you-go. Check **Billing and Cost Management → Free Tier**.

### A. Cost safety net
1. **Billing and Cost Management → Budgets → Create budget.**
   - Customize (advanced) → Cost budget. Name: `checkdesk-monthly`. Period: Monthly, recurring, fixed. Amount: a limit you choose (Errand Desk used 5.00 USD as a small safety net). Scope: all AWS services.
   - Alert at 80% actual and 100% forecasted, emailed to you.
   - Don't add budget "actions."
   - Standard budget notifications are described by AWS as free; confirm on the current [AWS Budgets pricing](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/) page.

### B. Domain
2. 💲 Register the domain you chose (if it is not already yours). If you use Route 53: **Route 53 → Domains → Register domains**. Use **1 year**, **auto-renew ON**, **privacy protection ON**. Confirm the current price in checkout. AWS credits typically cannot pay for domain registration. Complete the registrant-contact verification email.
3. **Hosted zone:** confirm a single hosted zone for `YOUR_DOMAIN`. Don't create a second one. **Don't enable DNSSEC** unless you have checked the extra KMS cost.

### C. Certificate
4. Region **us-east-1**. **Certificate Manager → Request a public certificate.**
   - Names: `YOUR_DOMAIN` and `www.YOUR_DOMAIN`.
   - DNS validation. Create the records in Route 53. Wait until status is **Issued**.
   - Public certificates for CloudFront are documented by AWS as no cost; confirm if needed.
   - Don't create two certificates for the same names.

### D. Storage
5. **S3 → Create bucket** (region **us-east-1**). General purpose. Name: a unique name you write down as `YOUR_BUCKET_NAME` (do not commit it).
   - Object Ownership: ACLs disabled. **Block all public access: ON** (all 4 boxes).
   - Versioning off, default encryption SSE-S3. Do **not** enable "Static website hosting."
6. **Upload the site.** Build first (`python3 site-src/build.py`), then upload the **contents** of `site-src/public/` (or another `--out` directory): `index.html`, `about/`, `disclosure/`, `privacy/`, `assets/`, `sitemap.xml`, `robots.txt`, icons. `index.html` must sit at the bucket root.
   - Suggested cache: HTML, sitemap, and `robots.txt` for about 5 minutes; fingerprinted CSS and icons can use a long cache.

### E. Edge function
7. **CloudFront → Functions → Create function.** Name: `checkdesk-viewer-request`. Runtime: **cloudfront-js-2.0**.
   - Paste `cloudfront-function-index-rewrite.js` after replacing `YOUR_DOMAIN` with the apex hostname (no protocol, no `www`).
   - Test a viewer-request for `/about/` → `/about/index.html`. Test `www.YOUR_DOMAIN` → 301 to `https://YOUR_DOMAIN/...`.
   - Publish the function. Don't share this function with another distribution if your plan forbids it.

### F. CloudFront distribution
8. **CloudFront → Distributions → Create distribution.** Name something like `checkdesk`. Single website or app. Domain: `YOUR_DOMAIN` and `www`.
9. **Origin:** Amazon S3 → your bucket. Use recommended origin settings (**Origin Access Control**).
10. **Security:** keep the wizard's WAF settings if you are on a plan that requires them; confirm current plan rules and cost.
11. **TLS certificate:** the Issued ACM certificate from step 4. Write down `YOUR_DISTRIBUTION_ID` and the `d….cloudfront.net` domain in a local untracked note, not in git.
12. **Finish settings.**
    - Alternate domain names: `YOUR_DOMAIN` and `www.YOUR_DOMAIN`.
    - Custom SSL certificate: the step-4 certificate.
    - Default root object: `index.html`. IPv6 on.
    - Default behavior: Redirect HTTP to HTTPS; methods GET, HEAD; Viewer request function `checkdesk-viewer-request`.
13. If you use a CloudFront plan that covers a Route 53 hosted zone, attach the `YOUR_DOMAIN` zone as the plan docs describe.
14. **Bucket policy.** If CloudFront did not write one, paste `s3-bucket-policy.json` with `YOUR_BUCKET_NAME`, `YOUR_ACCOUNT_ID`, and `YOUR_DISTRIBUTION_ID` filled in. Block Public Access stays **ON**.

### G. DNS
15. In the `YOUR_DOMAIN` hosted zone, create alias A and AAAA records for the apex and for `www`, pointing at the CloudFront distribution.
16. Wait until the distribution is deployed.

### H. Test (private window)
17. Check:
    - `https://YOUR_DOMAIN/` (home loads, padlock shown)
    - `https://YOUR_DOMAIN/about/`, `/disclosure/`, `/privacy/`
    - `https://YOUR_DOMAIN/about` (no trailing slash) still loads
    - The site-wide disclaimer is visible on each of those pages
    - `https://YOUR_DOMAIN/sitemap.xml` and `/robots.txt`
    - `https://YOUR_DOMAIN/favicon.svg`
    - `http://YOUR_DOMAIN/` redirects to https
    - `https://www.YOUR_DOMAIN/about/` 301s to `https://YOUR_DOMAIN/about/`
    - `https://YOUR_BUCKET_NAME.s3.amazonaws.com/index.html` is **Access Denied**

### I. Later (not in this checklist's launch pass)
- Analytics only if Richard approves a token and it is configured without committing secrets.
- Search Console / Bing sitemap submission, after the live check and approval.
- Denver listings: only after Step 3–7 review and an explicit go-live (Step 8).
