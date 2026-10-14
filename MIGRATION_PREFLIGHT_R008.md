# TandemVector Labs — Organization Rename Preflight R008

**Status: REVIEW REQUIRED / NOT RENAMED**  
**Current handle:** `Usefull-Skills`  
**Proposed handle:** `TandemVector-Labs` (the actual GitHub rename form must reconfirm availability)  
**Organization identity:** numeric ID `334108004` must remain identical  
**Display brand:** TandemVector Labs (jointly operated, not the personal name of either owner)  
**Plan at preflight:** GitHub Free  
**Source of evidence:** authenticated owner GitHub CLI/REST, organization GitHub repository and issue #1, 2026-10-14

## Access/continuity checkpoint

- [x] Two active GitHub Owner/admin memberships verified (separate accounts).
- [x] GitHub `2fa_disabled` member filter returned no members.
- [ ] **Organization 2FA requirement** is currently **OFF**. Enable via official authenticated Owner UI, confirm no outside collaborators are removed, then read back `two_factor_requirement_enabled=true` and both Owner roles/permissions.
- [ ] Member-privileges settings still permit repository deletion/transfer and visibility changes by eligible repository admins. Restrict through official Owner UI, re-read both flags as false, and confirm private visibility unchanged.
- [x] New repository creation by ordinary members is disabled; both Owners retain administrative control.
- [x] Public `.github` branch requires CODEOWNERS/PR review and prevents delete/force push.
- [ ] Each Owner must confirm a working recovery method, including access to their own 2FA recovery information (do not copy recovery codes into a repository or issue).

## Repository/asset prestate

At preflight the organization had **12 repositories: 10 public and 2 private**. Private repository names, release assets, source paths and personal secrets are **intentionally excluded from this public record**. Before any rename, the authorized Owner must export an access-controlled 12-repository ID/visibility/default-head snapshot into the private Project Brain. Compare it after the rename; never publish the private part of the snapshot.

Public repository names/roles:

| Repository | Type | Authoritative context |
| --- | --- | --- |
| [remote-commander-browser](https://github.com/Usefull-Skills/remote-commander-browser) | Original organization project | Browser releases and workflows here |
| [.github](https://github.com/Usefull-Skills/.github) | Organization controls | Shared profile, governance, policy |
| [ChatGPTRemoteCommander](https://github.com/Usefull-Skills/ChatGPTRemoteCommander) | Personal-source Fork | [Personal upstream](https://github.com/GOD13emad/ChatGPTRemoteCommander) |
| [DirectInternetMethod](https://github.com/Usefull-Skills/DirectInternetMethod) | Personal-source Fork | [Personal upstream](https://github.com/GOD13emad/DirectInternetMethod) |
| [FreeNetHub](https://github.com/Usefull-Skills/FreeNetHub) | Personal-source Fork | [Personal upstream](https://github.com/GOD13emad/FreeNetHub) |
| [OpenInternetGateway](https://github.com/Usefull-Skills/OpenInternetGateway) | Personal-source Fork | [Personal upstream](https://github.com/GOD13emad/OpenInternetGateway) |
| [TaskbarMonitorEnhanced](https://github.com/Usefull-Skills/TaskbarMonitorEnhanced) | Personal-source Fork | [Personal upstream](https://github.com/GOD13emad/TaskbarMonitorEnhanced) |
| [PersianWordAgent](https://github.com/Usefull-Skills/PersianWordAgent) | Personal-source Fork | [Personal upstream](https://github.com/GOD13emad/PersianWordAgent) |
| [LTEMonitor](https://github.com/Usefull-Skills/LTEMonitor) | Historical third-party fork lineage | Preserve original upstream attribution |
| [WSAGAScript](https://github.com/Usefull-Skills/WSAGAScript) | Historical third-party fork lineage | Preserve original upstream attribution |

At the last same-turn snapshot, each of the eight public personal-origin Fork default-branch SHAs matched its personal upstream; FreeNetHub and TaskbarMonitorEnhanced also had exact-head organization Actions **SUCCESS**. This is a **snapshot**, not perpetual synchronization, production release approval or GitHub Issues/Releases parity.

The original organization browser repository has **10 GitHub Release objects** in its present history, including previews. Preserve its numeric repository ID, tags, assets, release digests and CI dependencies; do not reissue any release simply because the namespace changes.

## Integrations / links to revalidate

- [x] Organization GitHub App inventory endpoint returned **one installed app**, `chatgpt-codex-connector`, with repository selection `all`. This is an installation inventory, **not** proof that renaming preserves tokens, app installation routing or permission checks. Verify installation access to representative public and private repos after the rename without disclosing private contents.
- [ ] GitHub Projects (v2) data is **not inventoried**; CLI token lacks `read:project`. Restore this capability only after explicitly authorized OAuth scope approval.
- [ ] GitHub Packages, GHCR/container tags, GitHub Pages, webhooks, GitHub App callbacks and external updaters/install scripts are **not fully enumerated**. Do not mark them PASS by inference from successful Git redirects.
- [ ] Update **current** links in the organization profile and project directory, personal profile README, installation/update docs, build workflows and third-party references after the rename. Preserve immutable tags, historical PRs, legal attribution and provenance text.
- [ ] Recheck all current API paths: the old organization path is **not automatically redirected** by GitHub. The old organization profile URL likewise will not reliably redirect. Validate each representative Git clone/fetch, release asset URL and a CI runner download **after** the rename.
- [ ] Public code search returning zero hits does **not** constitute a full dependency audit; index coverage, private repos and untracked local integrations remain unknown.

## Sequence / rollback

1. Receive both-Owner review of this preflight and verify security/access gates above. Do not transfer/rename personal or private projects as a side-effect.
2. Snapshot current numeric organization and repository IDs, visibility, public tag names/SHAs, critical release asset SHA/digests, browser app installation and both owner roles, in access-controlled Project Brain.
3. Confirm maintenance window and approved new handle availability in GitHub's authenticated **Organization Settings → Danger zone → Rename organization** interface. Do not attempt renaming by PATCHing the organization's display `name`.
4. Complete the UI confirmation, then **immediately verify** new organization URL and numeric ID `334108004`, both owners, 12 original repository identities and private visibility, and the GitHub App installation.
5. Regress old/new Git transport URLs, current API integrations, workflows, packages and release downloads; apply narrowly scoped fixes to live references only.
6. Record exact pass/fail checks, rollback feasibility and known unresolved URLs in a new cumulative Brain revision. If any issue threatens access, **STOP** and preserve evidence; an automatic rename-back is unsafe because the old handle may become available to others.

**Acceptance gate: OPEN until real UI rename + all poststate and integration checks PASS.** A Pull Request that approves this plan is not authorization to claim the rename completed.

Official references: [Renaming an organization](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization), [2FA requirements](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization), [Member privileges](https://docs.github.com/en/organizations/managing-organization-settings/setting-permissions-for-deleting-or-transferring-repositories).
