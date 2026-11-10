# Security Policy

## Scope

This repository holds the static website for Check Desk (domain not yet chosen; `site.config.json` uses a placeholder base URL): HTML, CSS, icons, and AWS deploy helpers (S3 + CloudFront). It has no server-side code, user accounts, or stored user data.

When the GitHub remote exists, enable GitHub secret scanning (with push protection), Dependabot alerts, and CodeQL code scanning, matching the Errand Desk practice documented in that project's SECURITY.md.

## Reporting a Vulnerability

**Please do not report security issues through public GitHub issues.**

Once the remote repository `gpu7/checkdesk` exists, report privately through GitHub:

https://github.com/gpu7/checkdesk/security/advisories/new

Please include a description, steps to reproduce, and the affected URL or file.

- We aim to acknowledge reports within **48 hours**.
- We aim to provide a full response within **7 business days**.

Please give us reasonable time to fix an issue before disclosing it publicly.

## Practices

- Never commit AWS credentials, account IDs, `.env` files, or private keys (see `.gitignore`).
- Use placeholders (`YOUR_BUCKET_NAME`, `YOUR_ACCOUNT_ID`, `YOUR_DISTRIBUTION_ID`, `YOUR_DOMAIN`) in deploy templates. Fill them only in the AWS console or in a local untracked file, never in a commit.
- The S3 bucket should be private and served only through CloudFront (Origin Access Control).
- This project does not sign up for affiliate programs. Do not add affiliate IDs, tip-service IDs, or analytics tokens unless Richard later approves them and they stay out of git until configured locally or via a documented, non-secret public site token.
