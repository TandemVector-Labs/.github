# Shared GitHub development home

**Effective scope (2026-10-15):** TandemVector Labs operates the GitHub organization
[`TandemVector-Labs`](https://github.com/TandemVector-Labs) with two equal, active **organization Owners**:
[`GOD13emad`](https://github.com/GOD13emad) and
[`mohammadmohammadzadeh19960-code`](https://github.com/mohammadmohammadzadeh19960-code).
Each has repository **Admin** authority throughout the organization's public and private repositories.
This does **not** confer ownership of repositories hosted in someone's personal account.

## Where to collaborate

| Project | Shared organization collaboration and QA | Organization issue intake | Existing personal releases / updater source |
| --- | --- | --- | --- |
| OpenInternetGateway | [Org code and PRs](https://github.com/TandemVector-Labs/OpenInternetGateway) | [Org Issues](https://github.com/TandemVector-Labs/OpenInternetGateway/issues) | [Personal original releases](https://github.com/GOD13emad/OpenInternetGateway/releases) |
| ChatGPTRemoteCommander | [Org code and PRs](https://github.com/TandemVector-Labs/ChatGPTRemoteCommander) | [Org Issues](https://github.com/TandemVector-Labs/ChatGPTRemoteCommander/issues) | [Personal original releases](https://github.com/GOD13emad/ChatGPTRemoteCommander/releases) |
| DirectInternetMethod | [Org code and PRs](https://github.com/TandemVector-Labs/DirectInternetMethod) | [Org Issues](https://github.com/TandemVector-Labs/DirectInternetMethod/issues) | [Personal original releases](https://github.com/GOD13emad/DirectInternetMethod/releases) |
| FreeNetHub | [Org code and PRs](https://github.com/TandemVector-Labs/FreeNetHub) | [Org Issues](https://github.com/TandemVector-Labs/FreeNetHub/issues) | [Personal original releases](https://github.com/GOD13emad/FreeNetHub/releases) |
| TaskbarMonitorEnhanced | [Org code and PRs](https://github.com/TandemVector-Labs/TaskbarMonitorEnhanced) | [Org Issues](https://github.com/TandemVector-Labs/TaskbarMonitorEnhanced/issues) | [Personal original releases](https://github.com/GOD13emad/TaskbarMonitorEnhanced/releases) |
| PersianWordAgent | [Binary distribution coordination](https://github.com/TandemVector-Labs/PersianWordAgent) | [Org Issues](https://github.com/TandemVector-Labs/PersianWordAgent/issues) | [Personal binary releases](https://github.com/GOD13emad/PersianWordAgent/releases) |

**Binary-only exception:** PersianWordAgent is distributed through published binaries; its public repositories do not provide source code for source-level pull requests. Use the existing organization issue tracker for distribution questions and coordination, and do not treat the organization repository as a source-code PR destination.

**Current routing proposal (2026-11-25):** Where source is published, the personal upstream is the canonical source-development and existing release/updater authority. For a binary-only distribution such as PersianWordAgent, the personal repository remains the distribution/release authority and does not expose source for code contributions. The organization repositories remain shared collaboration, review, integration QA and issue-coordination surfaces. The table preserves the existing organization issue entry points and personal release URLs; it does not transfer issues, repositories or release authority. The former organization-first development rule is historical. For additional first-party repositories, verify actual source ownership, fork lineage and project-specific acceptance before applying this routing.

For the two legacy third-party fork chains (LTEMonitor and WSAGAScript), continue following [the project catalog](PROJECT_CATALOG.md) and that project's own maintainer guidance; a generic policy must not claim transfer of third-party ownership, licensing or release authority. Private repositories are **not cataloged publicly** and must remain private.

## Safe two-owner workflow

1. Propose new first-party source changes in the verified canonical personal upstream by default. Keep existing organization work and candidate branches intact; reconcile accepted source changes to the fork via reviewed PRs, with explicit ancestry and exact-head checks. No direct protected-main write is authorized.
2. Either organization Owner can administer the organization projects. For sensitive changes, the **other actual human Owner** reviews; do not substitute a second login or automated approval for independent judgment.
3. Validate at the **exact candidate SHA**. A green CodeQL PR scan does not close an alert on protected `main`; prove closure after the accepted merge and a new main scan.
4. Preserve personal-source provenance and existing publication URLs. Fork reconciliation must use explicit SHA/ancestry and approved non-force syncing, **not** overwriting organization-only PRs or release assets.
5. Treat migration of releases, workflows, secrets, existing Issues/PRs, tags, notifications and package registries as separate gated work. Document original and destination identifiers, compatibility, backup/rollback, and reviewer decision. Personal-source repo transfer, deletion, archival, visibility changes and billing changes are **not authorized by this document**.

## Verified boundaries and open decisions

- **Organization collaboration access:** both active Owners and Admin permissions, verified via authenticated GitHub Owner and repository permission readbacks.
- **Org issue intake for all six first-party projects:** `has_issues=true` confirmed via GitHub REST after an authorized, reversible setting change. Historic issues in the personal repos are **not migrated**.
- **Upstream relationship:** all six org repositories remain public GitHub forks of `GOD13emad` originals; their protected default-branch SHA values matched the parent default-branch SHAs at the 2026-10-15 readback. This is **not** a detached independent upstream.
- **Code delivery:** personal source and organization integration each require their applicable exact-head tests and genuine independent review. A successful fork QA run is not a source merge or a published release.
- **Release migration:** still **OPEN**. The current applications and release automation reference personal GitHub namespaces; no release endpoint, artifact, tag or GitHub ownership transfer was changed.
- **Policy publication:** edits in this document require accepted organization branch protection and authorized review to become effective on the default branch. Until then, any PR containing this text is a candidate proposal, not an already published governance policy.

For details of repository provenance and per-project support, see [Project catalog](PROJECT_CATALOG.md), [Governance](GOVERNANCE.md), [Fork synchronization](FORK_SYNC_CONTROL.md) and [Contributing](CONTRIBUTING.md).
