# GitHub organization handle rename — executed 2026-10-20; follow-up verification OPEN

**Live organization:** [TandemVector-Labs](https://github.com/TandemVector-Labs) (current GitHub display name: TandemVector-Labs; shared prose brand: TandemVector Labs)
**Current GitHub handle:** TandemVector-Labs
**Former GitHub handle:** Usefull-Skills (historical provenance, no longer a valid organization REST API endpoint)
**Organization identity:** stable GitHub organization ID 334108004, both active Owners, 17 repositories (11 public, 6 private)
**Accepted operation:** official GitHub Owner Settings > General > Rename organization; live URL, organization blog and MMZ profile link independently read back
**Outstanding follow-up:** update checked-in current links and relevant remote URLs; inventory executable workflows, packages, webhooks, third-party integrations and external references. Preserve historical SHA/audit records without inventing compatibility. Independent governance review and product acceptance remain separate gates.

For canonical current acceptance and remaining work, see [portfolio Issue #1](https://github.com/TandemVector-Labs/.github/issues/1). GitHub redirects existing repository web/Git URLs, but does not redirect the former organization profile page or old REST API path. Do not use legacy endpoints for new automation.

## Historical pre-rename plan (preserved exactly below; its PREPARED status is not current)

**Status: PREPARED / NOT EXECUTED**  
**Brand (display name):** TandemVector Labs  
**Current GitHub handle:** `Usefull-Skills`  
**Proposed handle:** `TandemVector-Labs` (availability must be reconfirmed in the GitHub rename UI)  
**Organization ID:** `334108004` (immutable identity check)

This document is a reversible-as-far-as-possible migration **plan**, not evidence that the organization handle has changed. Changing the display name alone does not rename the handle.

## Why rename carefully

GitHub states that an organization rename redirects most repository web and Git URLs, but **does not redirect** the old organization profile page or old organization API endpoint paths. GitHub Packages and container consumers, references in workflow action paths, external download links, project badges and third-party integrations require independent checking. The old handle may become available to others, so reverting may not always be possible.

Official reference: https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization

## Hard preconditions — must be VERIFIED before rename

- [ ] Both organization owners have reviewed the new shared identity and can access GitHub with working secure 2FA and recovery methods; do not impair the other owner's access.
- [ ] Exact proposed handle is accepted by GitHub and has no known trademark/brand conflict (account availability is **not** legal clearance).
- [ ] Record current organization ID, both owner roles, all repository names/IDs, default branch SHAs, visibility, tags, active releases, GitHub App installations and branch policies.
- [ ] Inventory every **current executable/reference** to `Usefull-Skills` across checked-in workflows, automation, CODEOWNERS, documentation, public profiles, package metadata, container/image references, webhooks and external services. Classify historical provenance separately; never globally rewrite historical evidence.
- [ ] Confirm no active Release, deployment, GitHub Actions run or package publication depends on a hard-coded old API path; define safe maintenance window and rollback decision point.
- [ ] Prepare scoped post-rename edits for the organization profile, personal profile, README URLs and third-party service settings without publishing secrets.
- [ ] Confirm ownership continuity; no private repository or active Git history is being transferred, deleted or made public by this operation.

## Approved execution route

The documented GitHub path is **Organization Settings → Danger zone → Rename organization**. The organization Owner completes GitHub's confirmation screens. REST `PATCH /orgs/{org}` changed the display `name` but has **not** been treated as proof of handle rename. Do not create a replacement organization as a shortcut or assume that an unknown REST field will rename the account.

## Post-rename validation / acceptance

- [ ] New URL `https://github.com/TandemVector-Labs` resolves to the **same organization ID** `334108004`.
- [ ] All expected repositories resolve under the new namespace with the **same repository IDs**, visibility, default branch SHA, tags and release assets.
- [ ] Owners, GitHub App installation permissions, teams, security settings, organization membership and repository access remain intact.
- [ ] Active CI, package/registry/container pulls, install/update mechanisms, webhooks, repo references and documented external links pass an **end-to-end check**; old API paths are not relied on.
- [ ] Current profile/README/automation references use the new namespace; historical/provenance references remain unchanged and labeled where needed.
- [ ] Record validation receipts and the new authoritative path in the cumulative Project Brain, with exact failures, regression gates, and updated rollback assessment.

## Recovery policy

If any prerequisite is missing, **STOP** with existing handle and display name intact. After a rename, first preserve evidence and inspect the concrete failing link/service. Correct scoped references one at a time. Do not blindly rename back, force-push or republish releases; the old handle may be claimed and package/third-party systems may require their own recovery.

**Final gate:** HANDLE-RENAME remains **OPEN** until exact new-handle identity, reference regression, both-owner access and external integration checks have evidence.
