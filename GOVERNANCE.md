# Organization Governance — TandemVector Labs

**Scope:** Shared GitHub portfolio and collaboration standards, not a representation of registered company name, legal ownership, shareholding or authority over externally owned projects.

## Joint stewardship

This organization is managed as a **joint technical collaboration**, not the personal brand of one contributor. Both current owners retain equal GitHub Owner-role standing; this document does not grant one the right to unilaterally reassign the other's organization ownership.

Major decisions (organization handle, ownership, member permissions, private repository access, destructive operations, licensing changes, dependency publication, project ownership transfers and public release promotion) should be recorded with a review by the relevant stakeholders. If a second reviewer has not approved a sensitive change, mark the gate **OPEN** instead of calling it final.

## Source authority and release status

**Personal-first source policy (2026-11-25).** For first-party projects with a verified personal upstream, the personal repository is the canonical source-development and existing publication/updater authority. The matching organization fork is the shared collaboration, review, integration QA and coordination surface. The earlier organization-first direction dated 2026-10-15 is retained in Git history as provenance, not the default for new work. Preserve already-active organization branches and unique commits, and reconcile them by reviewed ancestry-preserving PRs; do not recreate repositories, change ownership, transfer private material or change release endpoints under this policy alone. For organization-origin projects or other ownership arrangements, confirm the accepted project-specific source authority before any migration. Third-party projects retain their original license, maintainers and upstream routing. A matching Git commit proves code parity at that commit, not service-data or product acceptance parity.

Never claim stable release status based solely on a successful build, GitHub workflow run or copied tag. Keep each project's raw test evidence, Project Brain, release notes, licenses and version history authoritative for that project.

## Security and accountability

- Preserve visibility boundaries: **private must remain private**; verify actual audience before any transfer or copy.
- Keep two-person owner recovery viable; require owners to enable 2FA before enforcing organization-wide 2FA, to prevent involuntary access lockout.
- Prefer reviewable PRs, appropriately scoped permissions, verified status checks, secret scanning and documented rollback.
- Never silently rewrite provenance, force-push, disable security controls or automatically promote candidate builds.
- Route new issues to the project-specific accepted tracker; existing organization issue intake for the six first-party forks remains available for shared coordination, with links to the canonical personal source issue or PR where applicable. Do not duplicate or silently move issue history.

## Changes and evidence

Record reason, affected namespace/repositories, old and new values, SHA/commit identifiers, checks, risk, restoration path and unresolved gates. After significant governance changes, update the portable organization Project Brain.

**This file describes intended operating policy. It does not certify that all GitHub UI/branch/security controls are enabled.**
