# Check Desk hosting hand-off

Prepared **2026-11-10** (America/Denver). This is a planning document. **No AWS resources were created, no DNS was changed, and no AWS or Cloudflare CLI was installed or authenticated** as part of writing it.

The intended setup is the one in [CHECKLIST.md](../CHECKLIST.md): a private S3 bucket served only through CloudFront, DNS at Cloudflare (DNS-only, not proxied), a free ACM public certificate in `us-east-1`, and optional Cloudflare Web Analytics. It matches how erranddesk.com was verified live on 2026-11-10.

The production domain is **checkdesk.us**, registered at Cloudflare Registrar on 2026-11-10. This document does not create AWS resources or change DNS.

---

## 1. What Pax can do now (as of 2026-11-10)

Checked on the shared box on 2026-11-10:

- **GitHub:** `gh` is signed in as `gpu7`. Pax can edit, commit, open pull requests, and merge in [gpu7/checkdesk](https://github.com/gpu7/checkdesk) (branch protection on `main` requires a pull request; required approvals are 0).
- **Site build:** Pax can run `python3 site-src/build.py` locally and preview the output. No cloud credentials are required for that.
- **AWS:** the AWS CLI is **not** installed. There is no `~/.aws` directory and no `AWS_*` environment variables on the box.
- **Cloudflare:** there are no Cloudflare credentials, config directory, or API tokens on the box. No Cloudflare CLI is in use.
- Pax can run **public** `curl` checks against a live domain once DNS points at CloudFront. That does not need AWS or Cloudflare access.

Pax **cannot**, with current access: create or change AWS resources, upload to S3, create a CloudFront invalidation, add or edit Cloudflare DNS records, request or validate an ACM certificate, register a domain, or turn on analytics in the Cloudflare dashboard.

---

## 2. What Pax could do if Richard later grants scoped access (optional)

Nothing in this section is requested or enabled today. If Richard wants Pax to run later deploys or help with DNS records, grant **least privilege** and only for Check Desk. Do not hand over the root AWS user, a wide IAM policy, or a Cloudflare Global API key.

### Optional: IAM user or role for deploys only

Limit it to the one bucket and the one distribution, for example:

- `s3:ListBucket` on `arn:aws:s3:::YOUR_BUCKET_NAME`
- `s3:PutObject` (and, for `aws s3 sync`, typically also `s3:GetObject`) on `arn:aws:s3:::YOUR_BUCKET_NAME/*`
- `cloudfront:CreateInvalidation` on `arn:aws:cloudfront::YOUR_ACCOUNT_ID:distribution/YOUR_DISTRIBUTION_ID`

Do **not** include `s3:DeleteObject` unless you later decide the deploy process should delete objects. The template `scripts/deploy.sh` does not use `--delete`. Do not include permissions to create buckets, distributions, functions, certificates, hosted zones, or to change bucket policies or public-access blocks.

Example policy (placeholders only; never commit the filled-in ARNs):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListTheOneBucket",
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME"
    },
    {
      "Sid": "WriteObjectsInTheOneBucket",
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject"],
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    },
    {
      "Sid": "InvalidateTheOneDistribution",
      "Effect": "Allow",
      "Action": ["cloudfront:CreateInvalidation"],
      "Resource": "arn:aws:cloudfront::YOUR_ACCOUNT_ID:distribution/YOUR_DISTRIBUTION_ID"
    }
  ]
}
```

`s3:GetObject` is included because `aws s3 sync` usually needs it to compare existing objects. If you omit it, PutObject and ListBucket still match a strict reading of "upload," but the template script may fail or re-upload everything. Optional extras you might add later, if you want Pax to wait on an invalidation: `cloudfront:GetInvalidation` and `cloudfront:ListInvalidations` on the same distribution ARN.

If this access is granted, Pax could run (after a local build) the untested `scripts/deploy.sh` with `CHECKDESK_BUCKET` and `CHECKDESK_DISTRIBUTION_ID` set in the environment, not in git. Richard would still create the bucket, distribution, certificate, budget, and DNS zone himself unless he separately expands that access.

### Optional: Cloudflare API token for DNS edit on one zone

A custom token scoped to **Zone → DNS → Edit**, and only the one `checkdesk.us` zone (not all zones; not Zone settings, analytics, or registrar). That would let Pax add or update the ACM validation CNAMEs and the apex/`www` CNAMEs described in the checklist, still as **DNS-only** records.

It would **not** let Pax change nameservers at the registrar, turn the proxy on, or create the zone in the first place, and it should not be used to orange-cloud the CloudFront records.

---

## 3. Richard's steps, in order

The production domain is **checkdesk.us**, registered at Cloudflare Registrar on 2026-11-10. Nameservers are already Cloudflare's; there is no nameserver-change step. Do not start creating AWS or DNS resources until you give a go-ahead. Detailed console clicks are in [CHECKLIST.md](../CHECKLIST.md). Short version:

1. **Domain: `checkdesk.us` (registered 2026-11-10 at Cloudflare Registrar).** Nameservers are already Cloudflare's. Do not use Route 53 as authoritative DNS.
2. **Create the $5 AWS Budget** `checkdesk-monthly` (80% actual and 100% forecasted email alerts; no budget actions). Confirm current [Budgets pricing](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/).
3. **Confirm the Cloudflare zone** for `checkdesk.us` is on the Free plan and **Active**. There is no nameserver-change step.
4. **Request the ACM public certificate** in **us-east-1** for `checkdesk.us` and `www.checkdesk.us`, DNS validation. Add the ACM CNAME records **manually** in Cloudflare as **DNS only**. Wait until the certificate is **Issued**.
5. **Create the private S3 bucket** in `us-east-1`: Block Public Access ON, SSE-S3, ACLs disabled, no static website hosting. Write down `YOUR_BUCKET_NAME` locally; do not commit it.
6. **Create and publish** the CloudFront Function `checkdesk-viewer-request` (runtime `cloudfront-js-2.0`) from `cloudfront-function-index-rewrite.js`. The repo file already sets `APEX` to `checkdesk.us`; confirm that when you publish the function.
7. **Create the CloudFront distribution:** S3 origin with OAC, alternate domain names apex + `www`, the Issued ACM certificate, default root object `index.html`, HTTP → HTTPS redirect, cache policy CachingOptimized, viewer-request function association. If you use the flat-rate Free plan (subject to eligibility), keep the wizard WAF as Errand Desk did. **Do not attach a Route 53 hosted zone.** Recommended: map 403/404 to `/404.html`. Write down `YOUR_DISTRIBUTION_ID` and `d….cloudfront.net` locally.
8. **Confirm or paste the OAC bucket policy** from `s3-bucket-policy.json` (filled in only in the console). Block Public Access stays ON.
9. **In Cloudflare DNS**, create the apex CNAME and the `www` CNAME to `d….cloudfront.net`, both **DNS only (grey cloud)**. Do not proxy them. Do not point at raw CloudFront IPs.
10. **Build and upload** `site-src/public/` with explicit Content-Type and Cache-Control (HTML, sitemap, and `robots.txt` at 5 minutes; fingerprinted assets and the SVG favicon at 1 year immutable). Invalidate CloudFront `/*`.
11. **Verify** with the `curl` checks in checklist section J (CloudFront/`via` headers and no `cf-ray`, bucket URL Access Denied, `www` 301, HTTP → HTTPS, folder URLs, 404 page, disclaimer present).
12. **Optional:** create a Cloudflare Web Analytics site, put the public token in `cf_analytics_token`, rebuild, re-upload, and invalidate.
13. **Optional, later:** if you want Pax to deploy updates, create the scoped IAM user or role (and, if you want help with DNS records, the scoped Cloudflare token) described in section 2, and store those credentials off-box from git.

Pax will not perform steps 2–10 until you approve them and, where needed, grant the matching access.
