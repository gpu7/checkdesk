# Security Policy

## Scope

This repository holds the static website for Check Desk (production domain: checkdesk.us, registered at Cloudflare Registrar on 2026-11-10): HTML, CSS, icons, and deploy helpers (private S3 + CloudFront, with DNS hosted at Cloudflare in DNS-only / not-proxied mode). It has no server-side code, user accounts, or stored user data.

GitHub secret scanning (with push protection), Dependabot alerts, and CodeQL code scanning are enabled on [gpu7/checkdesk](https://github.com/gpu7/checkdesk), matching the Errand Desk practice.

## Reporting a Vulnerability

**Please do not report security issues through public GitHub issues.**

Report privately through GitHub:

https://github.com/gpu7/checkdesk/security/advisories/new

Please include a description, steps to reproduce, and the affected URL or file.

- We aim to acknowledge reports within **48 hours**.
- We aim to provide a full response within **7 business days**.

Please give us reasonable time to fix an issue before disclosing it publicly.

## Practices

- Never commit AWS credentials, account IDs, `.env` files, Cloudflare API tokens, or private keys (see `.gitignore`).
- Use placeholders (`YOUR_BUCKET_NAME`, `YOUR_ACCOUNT_ID`, `YOUR_DISTRIBUTION_ID`) in deploy templates. Fill them only in the AWS or Cloudflare console, or in a local untracked file, never in a commit. The public hostname `checkdesk.us` is intended site configuration, not a secret.
- The S3 bucket should be private and served only through CloudFront (Origin Access Control). DNS for the site should be hosted at Cloudflare as **DNS-only** (grey cloud, not proxied) records pointing at the CloudFront distribution domain. Do not put Cloudflare in front of CloudFront as a proxy.
- This project does not sign up for affiliate programs. Do not add affiliate IDs, tip-service IDs, or analytics tokens unless Richard later approves them and they stay out of git until configured locally or via a documented, non-secret public site token (the optional Cloudflare Web Analytics site token in `site.config.json`).
