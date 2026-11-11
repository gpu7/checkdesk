#!/usr/bin/env bash
# OPTIONAL, UNTESTED template for uploading a Check Desk build to S3 and
# invalidating CloudFront. This script is not used by CI. Review and test it
# before relying on it.
#
# Requires the AWS CLI and credentials that can write the one bucket and
# create an invalidation on the one distribution (see docs/HOSTING-HANDOFF.md).
# Do not hardcode bucket names or distribution IDs in this file.
#
# Usage (from the repo root, after python3 site-src/build.py):
#   export CHECKDESK_BUCKET=your-bucket-name
#   export CHECKDESK_DISTRIBUTION_ID=EXXXXXXXXXXXXX
#   ./scripts/deploy.sh
#
# Optional: CHECKDESK_SRC (defaults to site-src/public)

set -euo pipefail

if [[ -z "${CHECKDESK_BUCKET:-}" || -z "${CHECKDESK_DISTRIBUTION_ID:-}" ]]; then
  echo "Set CHECKDESK_BUCKET and CHECKDESK_DISTRIBUTION_ID in the environment (do not commit them)." >&2
  exit 1
fi

SRC="${CHECKDESK_SRC:-site-src/public}"

if [[ ! -d "$SRC" ]]; then
  echo "Build output not found: $SRC (run python3 site-src/build.py first)." >&2
  exit 1
fi

if [[ ! -f "$SRC/index.html" ]]; then
  echo "Refusing to upload: $SRC/index.html is missing. Upload the contents of the build directory, with index.html at the bucket root." >&2
  exit 1
fi

# No --delete: the least-privilege example policy does not include s3:DeleteObject.
# --metadata-directive REPLACE so Content-Type and Cache-Control are applied on updates.

# 1) Fingerprinted CSS under assets/ — 1 year, immutable.
#    Only CSS is included here; add a separate sync if other asset types appear.
aws s3 sync "$SRC" "s3://${CHECKDESK_BUCKET}" \
  --exclude "*" --include "assets/*.css" --include "assets/**/*.css" \
  --content-type "text/css; charset=utf-8" \
  --cache-control "public, max-age=31536000, immutable" \
  --metadata-directive REPLACE

# 2) SVG favicon (and any other root SVGs) — 1 year, immutable.
aws s3 sync "$SRC" "s3://${CHECKDESK_BUCKET}" \
  --exclude "*" --include "*.svg" --exclude "assets/*" \
  --content-type "image/svg+xml" \
  --cache-control "public, max-age=31536000, immutable" \
  --metadata-directive REPLACE

# 3) HTML — 5 minutes.
aws s3 sync "$SRC" "s3://${CHECKDESK_BUCKET}" \
  --exclude "*" --include "*.html" \
  --content-type "text/html; charset=utf-8" \
  --cache-control "public, max-age=300" \
  --metadata-directive REPLACE

# 4) sitemap.xml — 5 minutes.
aws s3 sync "$SRC" "s3://${CHECKDESK_BUCKET}" \
  --exclude "*" --include "sitemap.xml" \
  --content-type "application/xml" \
  --cache-control "public, max-age=300" \
  --metadata-directive REPLACE

# 5) robots.txt — 5 minutes.
aws s3 sync "$SRC" "s3://${CHECKDESK_BUCKET}" \
  --exclude "*" --include "robots.txt" \
  --content-type "text/plain; charset=utf-8" \
  --cache-control "public, max-age=300" \
  --metadata-directive REPLACE

# 6) IndexNow key file at the site root (32-character hex name) — 1 day.
#    The build copies it from site-src/src/static/. Do not use this include for robots.txt.
aws s3 sync "$SRC" "s3://${CHECKDESK_BUCKET}" \
  --exclude "*" --include "*.txt" --exclude "robots.txt" \
  --content-type "text/plain; charset=utf-8" \
  --cache-control "public, max-age=86400" \
  --metadata-directive REPLACE

# 7) Clear the CloudFront edge cache.
aws cloudfront create-invalidation \
  --distribution-id "${CHECKDESK_DISTRIBUTION_ID}" \
  --paths "/*"

# After the invalidation completes, from the repo root:
#   python3 site-src/tools/indexnow_ping.py --all
# Or pass changed https://checkdesk.us/... URLs. This script does not wait for
# the invalidation, so do not run the ping from here automatically.
