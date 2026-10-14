# TandemVector Labs — Organization Rename Preflight R008

> **R010 CURRENT (2026-10-14): 14 organization repositories (11 public, 3 private).** Earlier R008 (12) and R009 (13) observations remain historical; they are superseded for any rename prestate. New original public repository `AppearanceStudio-Core` has `protected=false` on `main`; 10/11 public branches show protected=true. **No organization rename or protection change has been executed.** See R010 delta below.

> **R009 current-state notice (2026-10-14):** This document retains the original R008 historical 12-repository preflight. The verified current count is **13 repositories (10 public / 3 private)**. The 12-repository references below are historical and MUST NOT be used as the current rename acceptance baseline. See the R009 delta at the end. The organization has **not** been renamed.

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

---

## R009 verified continuation — 2026-10-14

**Mutation objective:** correct the stale organization rename baseline without changing organization/repository settings, private visibility, release state or Git history. R008 evidence and 12-repository snapshot are retained above for chronology; this delta is authoritative for current pre-rename inventory.

### Live prestate and evidence

- Organization handle remains `Usefull-Skills`; the proposed `TandemVector-Labs` rename is **NOT executed**.
- **13 repositories total: 10 public + 3 private**, from the authenticated organization repository listing. Do **not** place private repository identifiers or contents in this public document. The fresh 13-item confidential ID/visibility/ref snapshot and Owner/2FA readback remain an **OPEN access-controlled gate**.
- Both linked GitHub accounts `GOD13emad` and `mohammadmohammadzadeh19960-code` authenticated. Repo-level `admin` access for each was confirmed on the private security tracker, and for the second account on the organization Browser. These permission checks do **NOT** replace organization-wide Owner/recovery, 2FA enforcement or Member privilege readbacks.
- **All eight public personal-source Fork default branches are IDENTICAL to upstream at this timestamp:** comparison returned `status=identical`, `ahead=0`, `behind=0`, with the exact upstream and fork HEAD matching. This confirms parity only for the specified default branches, not Issues, releases, tags or other refs:

| Public organization Fork | Branch | Verified identical upstream/fork HEAD |
| --- | --- | --- |
| OpenInternetGateway | main | `4c34996ef615afa7b515ac0f84e6a18b9ddcb5cf` |
| TaskbarMonitorEnhanced | main | `03e70785529354f741d75449a19d7e2538c2b81d` |
| PersianWordAgent | main | `65aa3f85a9dccc23fcc19e26e4515ef7b5928697` |
| DirectInternetMethod | main | `26ef644117ea474b487186ce5e6e61e92cd02dd4` |
| FreeNetHub | main | `e4112be36d6cce97863c59a5dbe6a5d0bcdf5786` |
| ChatGPTRemoteCommander | main | `bd4f868d3c07e95965a8e249f5191fb16902406c` |
| LTEMonitor | master | `646c05592c3497e94ec4aa576aa06c8c3c6f0edf` |
| WSAGAScript | main | `99f034ef529aa39aa008e02befe8788cb9d86b46` |

- The public `.github` governance repository and the **eight public forks** each have an active default-branch ruleset that blocks deletion and non-fast-forward changes (9 repos, 9 such rulesets). The governance repo additionally has an active CODEOWNERS/one-review PR ruleset, with no bypass actors. Its independent-review gate remains **OPEN** until an actual eligible reviewer submits approval.
- The original organization Browser has **no repository ruleset returned** by the rulesets listing. Its separate branch-protection REST read returned **403** via the installed integration; do not infer that it has no protection. On three private repositories, the rulesets listing returned GitHub's **403 plan restriction**; do not infer either rule presence or absence from that error.
- The public source for this migration behavior is GitHub's official [Renaming an organization](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization) documentation: old profile URLs and API paths are **not** redirected; repository URL redirection is conditional and should be verified. The old handle becomes available for another user to claim. No automatic rename-back is safe.

### Updated gates / exact next action

1. **PASS at this snapshot:** public default-branch Fork parity (8/8) and the 9 observed public default-branch delete/non-FF rulesets. Recheck immediately before any rename; snapshots are not permanent synchronization.
2. **OPEN:** each Owner validates working 2FA and recovery; verify and enforce the organization-level requirement via official Owner settings; re-read actual poststate. Do not expose recovery codes.
3. **OPEN:** official Organization Member privileges for repository deletion/transfer and visibility changes; read back actual persisted controls.
4. **OPEN:** access-controlled 13-repository identity/visibility/HEAD export and private repo protection alternatives; release, tags, packages, Projects, API client and App installation inventory; jointly approved rename plan and post-rename rollback/contingency.
5. **OPEN:** separate peer review of this preflight PR. Merging the documentation does not perform or prove the rename.

**No changes to branch protections, organization settings, account credentials, private visibility, publication, or releases were made by this R009 evidence update.** Code scanning findings and release-product acceptance are tracked separately and are not implied PASS by these infrastructure controls.

---

## R010 new public repository onboarding — 2026-10-14

**Mutation objective:** update governance/namespace migration preflight after an independent public repo appeared; preserve R008/R009 historical evidence. Do not mistake documentation for policy enforcement.

- Live authenticated `Usefull-Skills` listing: **14 repositories = 11 public + 3 private**. New public original (not a fork) [AppearanceStudio-Core](https://github.com/Usefull-Skills/AppearanceStudio-Core), GitHub repository numeric ID `1419340924`, created `2026-10-14T16:00:04Z`. Default `main` HEAD `8f56fe7f2ec16d1a563eae049ea6b6a1e6221382`. Public marketing/attribution is Appearance Studio Core / Arclenor Technologies; its published notice is all-rights-reserved with installation/use permission, not blanket open-source redistribution permission. No private repository identity is disclosed here.
- Default branch `protected` readback for all 14: **10 of 11 public protected**, the new AppearanceStudio-Core public `main` is **unprotected**; all three private default branches are also `protected=false` (GitHub Free organization plan-gated for private branch protection/rulesets). AppearanceStudio-Core rulesets list `[]`; this is a real protection gap, not a CodeQL exploit finding. Public-rule action requires authenticated Repository Administration(write) / supported Owner UI. This GitHub connection has no ruleset-create action; no false PASS, manual direct API token escalation or substitute `CODEOWNERS`-only claim.
- [AppearanceStudio-Core v0.9.0-rc1](https://github.com/Usefull-Skills/AppearanceStudio-Core/releases/tag/v0.9.0-rc1) is a **public prerelease**; git tag points to the same SHA as `main`. GitHub release asset `AppearanceStudio-Core-v0.9.0-rc1.zip` (42,451 bytes), SHA-256 `cfc28a4ba734eb7150e18895b10890d6d0ff60ac38a8825dd1938ba2cd12f4f0`. Independent Linux verification from this exact published asset: ZIP CRC PASS, no duplicate, symlink or path-escaping entries, all 27 manifest-declared files byte-size/SHA match, 16 Python AST files parse, zero unexpected files; included regression scripts `tests/test_engine_transaction.py` and `tests/test_system_monitor_model.py` both returned PASS in an isolated audit directory without running the installer or activating any desktop service. The manifest itself explicitly states `full_product_final=false`; this is distribution-integrity QA only, **not GNOME visual/soak or v1 product acceptance**.
- Core's GitHub Actions CI success was observed on exact commit `8f56fe7f2ec16d1a563eae049ea6b6a1e6221382` (run [38594803171](https://github.com/Usefull-Skills/AppearanceStudio-Core/actions/runs/38594803171)). Existing eight public organization Forks remain separate from this new original repo; most recent FreeNetHub personal/organization `main` compared IDENTICAL at `03318fa00ba56d625f6178aed517fbaba65d55a4` with organization CI SUCCESS ([38600623571](https://github.com/Usefull-Skills/FreeNetHub/actions/runs/38600623571)).

### Updated rename preflight / exact next actions

1. **PASS:** 14-repository inventory (11 public, 3 private) at this timestamp and bounded public release-archive integrity. The older 12/13 counts are retained as history only.
2. **OPEN:** protect the new public repository's default branch using an active ruleset restricting deletion and non-fast-forward updates with no unintended bypass; verify live `protected=true` and rule details. Current GitHub docs: [ruleset API requires Administration(write)](https://docs.github.com/en/rest/repos/rules#create-a-repository-ruleset); [GitHub Free public rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets).
3. **OPEN:** org-wide 2FA enforcement, member privileges, three private repositories' protection plan decision, second-owner review, and an access-controlled 14-repo ID/head/visibility/integrations snapshot. Brand/provenance and current links for new AppearanceStudio-Core must be included before any namespace rename.
4. **OPEN:** actual rename UI, post-rename project URLs/API, app integrations, releases, package references and private access regression. Original owner-approved stable assets and private repos remain untouched.

**Change boundary:** documentation branch PR #2 only. No repo rules, user tokens, private visibility, product runtime, release, or organization handle changed by this update.
