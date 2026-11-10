# Creating the GitHub remote for Check Desk

The local repository is at `/workspace/checkdesk-repo` on the shared box, branch `main`. This checkout is **not** connected to GitHub. The box `gh` CLI is not logged in. Nobody should run `gh auth login` from an agent session unless Richard does that himself.

The intended remote is an empty **private** repository: `https://github.com/gpu7/checkdesk`.

## 1. Create an empty private repo on GitHub

In the GitHub UI, signed in as `gpu7`:

1. **New repository**.
2. Name: `checkdesk`. Owner: `gpu7`.
3. Visibility: **Private**.
4. **Do not** add a README, license, or `.gitignore`. An initial commit on GitHub would conflict with the local history.
5. Create the repository.

## 2. Push this local history (HTTPS)

On the shared box:

```sh
cd /workspace/checkdesk-repo
git remote add origin https://github.com/gpu7/checkdesk.git
git push -u origin main
```

If GitHub asks for credentials, use an account Richard controls (a personal access token or the GitHub CLI, not a committed secret).

## 3. Alternative: GitHub CLI

Only after Richard authenticates the CLI himself:

```sh
gh auth login
gh repo create gpu7/checkdesk --private --source=/workspace/checkdesk-repo --push
```

`--source` plus `--push` creates the empty private repo and pushes `main`. Do not pass `--add-readme`. If `origin` already exists, drop `--source` and use the commands in section 2 instead.

## 4. Recommended repository settings

These recommendations come only from files in the Errand Desk repo (`https://github.com/gpu7/erranddesk`) and from that project's `SECURITY.md`. GitHub-only settings such as branch protection are **not** stored in the Errand Desk tree, so they are recommended practice, not a copy of a rule I could read.

From Errand Desk files you can copy as-is in spirit (already in this repo):

- **CODEOWNERS** — default owner `@gpu7`, with extra ownership on `.github/`, `SECURITY.md`, and the deploy templates.
- **Dependabot** — weekly `github-actions` updates (`.github/dependabot.yml`). In the GitHub UI, also turn on Dependabot alerts (and security updates if you want them).
- **CodeQL** — workflow at `.github/workflows/codeql.yml` (this copy also analyzes Python, because Check Desk's builder is Python). Enable code scanning in the repo's Security settings if a private repo does not pick the workflow up automatically.
- **Secret scanning with push protection** — Errand Desk's `SECURITY.md` states these are enabled there. Turn them on for `gpu7/checkdesk` in **Settings → Code security and analysis**.
- **Security advisories** — the reporting URL in `SECURITY.md` is `https://github.com/gpu7/checkdesk/security/advisories/new`.

Recommended, but **not visible as a file in the Errand Desk repo** (confirm in the Errand Desk GitHub UI if you want a exact match):

- Protect `main`: no force-pushes, no deletions, require a pull request before merge if you want a review gate. CODEOWNERS says reviews are not enforced as required reviews on Errand Desk, so you can keep that lighter rule if you prefer.

After the first push, confirm the default branch is `main`.
