# R006 — Current public-fork reconciliation (2026-10-14)

**New accepted state:** `Usefull-Skills/FreeNetHub:main` and `GOD13emad/FreeNetHub:main` now both point to `e41b3f669a894b1df5f0e84884eeb8600e747224` (exact 40-character GitHub API readback). The earlier R005 `f65da9c8...` head is **SUPERSEDED AS CURRENT**, retained below for lineage. The fork only advanced by two commits; GitHub compare returned `ahead_by=2`, `behind_by=0`, merge base equal to old fork `f65da9c8...`. No force push or branch/tag deletion occurred.

**Mutation preflight and cause:** Repo ID `1418018228`, parent `GOD13emad/FreeNetHub`, exact two HEADs, non-fast-forward guard, source CI [38488479939](https://github.com/GOD13emad/FreeNetHub/actions/runs/38488479939) **10/10 jobs SUCCESS**, and zero in-progress target runs were checked before `gh repo sync Usefull-Skills/FreeNetHub --branch main`. The operation result delivery flagged a shell time boundary despite writing a `...SYNC_PASS` receipt; **independent direct GitHub source and fork HEAD readback** independently confirmed success. Do not rerun based on the transport timeout alone.

**Change surface:** `.github/workflows/ci.yml` (+29), `PUBLIC_MANIFEST.json` (updated file hashes), `tests/test_lifecycle_safety.py` (+23), `windows/installer/FreeNetHub.iss` (+44). The installer change introduces a **fail-closed conflicting-install-root guard** to prevent silent split installation; the existing source CI was accepted before mirror advancement. No release/tag publication is implied.

**Downstream exact-head acceptance:** New organization CI [38490448851](https://github.com/Usefull-Skills/FreeNetHub/actions/runs/38490448851) was `queued` on first post-sync check. **CI gate remains OPEN** until this exact-head run is `completed/success` and all jobs pass. Existing R005 CI [38487571483](https://github.com/Usefull-Skills/FreeNetHub/actions/runs/38487571483) is PASS for **its older exact SHA only**.

**TaskbarMonitorEnhanced:** Fork divergence remains **intentional**: org `main=a24d2328f0b70780bd4ebbe25f29c6d3f44cf4a6`, upstream personal `main=86db0d17c438a255a19dbcfb94c5942922712ecd`; fork exact-head Windows native A/B CI PASS, original product remains separate. Upstream [PR #66](https://github.com/GOD13emad/TaskbarMonitorEnhanced/pull/66) is now `READY FOR REVIEW`, `OPEN`, `merged=false`, one CI test script changed. Upstream PR-hosted Build on exact head [38488705989](https://github.com/GOD13emad/TaskbarMonitorEnhanced/actions/runs/38488705989) PASS. **Do not auto-merge or re-release** without separately accepted upstream promotion gates.

**Whole portfolio FINAL remains OPEN**: external Owner secure-2FA readiness, official organization-handle migration and API/package regression, member privileges, privately scoped repo transfer, GH Projects access, unpatched OIG toolchain advisories, cross-product release/owner acceptance. Public controls must not disclose private repository filenames, content, staging paths or personal account 2FA specifics.

---

## Prior R005/R004/R003 control snapshots — retained as evidence (CURRENT claims superseded above)

## R005.1 — Taskbar upstream review proposal (2026-10-14)

**CURRENT:** Organization Fork R163 main CI remains PASS, and upstream personal [Draft PR #66](https://github.com/GOD13emad/TaskbarMonitorEnhanced/pull/66) was opened **without merging**. Exact PR base `86db0d17c438a255a19dbcfb94c5942922712ecd`, head `Usefull-Skills:main=a24d2328f0b70780bd4ebbe25f29c6d3f44cf4a6`; GitHub returned `draft=true`, `merged=false`, `changed_files=1` (`build/Test-Native-Presentation-R155.ps1`). No executable/installer release was changed. The separate **upstream review/CI/owner acceptance gate** is OPEN; personal main remains the reference for product releases. This is not permission to auto-merge a draft.

# R005 acceptance delta — 2026-10-14

**CURRENT: FreeNetHub Fork sync + exact-head CI = PASS.** The previously OPEN/RUNNING FreeNetHub CI gate documented in the R004 section below has now completed and is **SUPERSEDED FOR CURRENT STATUS**.

- GitHub [run 38487571483](https://github.com/Usefull-Skills/FreeNetHub/actions/runs/38487571483) finished `status=completed, conclusion=success` at exact organization-fork `main=f65da9c8ff2ca9e6207aecc3c7e67b6b935ee6eb`. Independent GitHub Jobs readback: **10/10 SUCCESS** (`ios-static`, `linux-static`, `android-build`, `windows-installer-fresh`, `console-virtual-e2e`, `windows-unit`, `windows-virtual-signing`, `ios-simulator-runtime`, `android-emulator-runtime`, `virtual-acceptance`); none failed.
- Main source and organization-fork ref reads match at full SHA `f65da9c8ff2ca9e6207aecc3c7e67b6b935ee6eb`. The change was fast-forward-only and removed a legacy automatic Linux release-publisher job; no forced push, branch/tag deletion or release publication occurred.
- **Scope of PASS:** Git mirror target main-head parity and exact-head hosted GitHub Actions regression; **not** evidence of production installation/owner acceptance, a signed public stable release, or all historical branch/tag service-data parity.
- **TaskbarMonitorEnhanced:** Fork-only PR1 main R163 and exact-head native A+B CI remain ACCEPTED/PASS (see prior R004 delta); personal upstream deliberately remains separate.
- **Remaining critical gates:** two-owner secure 2FA and org enforcement; official handle rename/URL/API/package regression; member privileges/review requirement; consented private-repository scope; GitHub Projects read scope; two unpatched OIG dev-chain GHSA risks and release/owner validation. **Portfolio FINAL remains OPEN.**

---

## R004 previous acceptance snapshot — superseded only where explicitly noted

# Current reconciliation — R004 (2026-10-14)

**CURRENT / CONFIRMED:** Public-fork default branches have **7/8 exact upstream SHA parity** after reconciliation. The one exception is **intentional and tested fork-specific divergence** in TaskbarMonitorEnhanced, not an unsynchronized stale fork. Historic R003 snapshot below is preserved as provenance and is **SUPERSEDED FOR CURRENT STATUS**.

- **FreeNetHub main Fast-forward: PASS.** Upstream and organization fork both point to `f65da9c8ff2ca9e6207aecc3c7e67b6b935ee6eb`. Exact prestate source `f65da9c8...`, fork `cab6139d...`, compare `ahead_by=2, behind_by=0`; `gh repo sync --branch main` succeeded without force; independent GitHub ref readback matched. The new `PUBLIC_MANIFEST.json` matches the updated CI file. The two commits removed a **legacy automatic Linux release-publication job** rather than adding automatic release behavior. No fork-only historical refs were deleted.
- **FreeNetHub exact-head CI: OPEN/RUNNING** in [workflow run 38487571483](https://github.com/Usefull-Skills/FreeNetHub/actions/runs/38487571483). Initial job evidence: iOS static, Linux static, Android build, Windows fresh installer, console virtual E2E, Windows unit, and Windows virtual signing all SUCCESS; mobile iOS simulator and Android emulator acceptance jobs were still running at the last check. Do not call the whole CI PASS until the run completes with SUCCESS.
- **TaskbarMonitorEnhanced fork-specific main acceptance: PASS.** Organization fork `main=a24d2328f0b70780bd4ebbe25f29c6d3f44cf4a6` is 3 commits ahead of personal upstream `main=86db0d17c438a255a19dbcfb94c5942922712ecd` by **intentional R163 diagnostic/paint-readiness changes**. Fork PR #1 merged; [main-head build 38485471888](https://github.com/Usefull-Skills/TaskbarMonitorEnhanced/actions/runs/38485471888) and [native A+B acceptance 38485471910](https://github.com/Usefull-Skills/TaskbarMonitorEnhanced/actions/runs/38485471910) both SUCCESS. [Upstream CI-specific Issue #65](https://github.com/GOD13emad/TaskbarMonitorEnhanced/issues/65) was closed with completion evidence. Preserve the original upstream release and the fork's validated changes; **DO NOT RESET/SYNC AWAY** this fork-specific delta without upstream promotion authority.
- All other first-party and legacy public fork default branches were SHA-matched in the R004 readback. A default-head check is not exhaustive branch/tag parity, so continue per-ref verification when required.
- Organization URL remains `Usefull-Skills`; displayed brand `TandemVector Labs`. Shared ownership, 2FA enforcement, private replication and rename acceptance are separate critical gates, not closed by code parity.

**Accepted gate outcomes:** `FNH-FAST-FORWARD=PASS`, `TASKBAR-ORG-FORK-MAIN-CI=PASS`; `FNH-EXACT-HEAD-CI=OPEN`, `TASKBAR-PRODUCTION-RELEASE=OPEN`, `WHOLE-ORGANIZATION-FINAL=OPEN`. 

---

## R003 historical snapshot — SUPERSEDED FOR CURRENT STATUS (retained verbatim)

# Public Fork Synchronization Control — TandemVector Labs

**Audit date:** 2026-10-14  
**Status:** PARTIAL / NOT CONTINUOUSLY SYNCHRONIZED  
**Original source owner:** `GOD13emad`  
**Organization owner/namespace:** `Usefull-Skills` (displayed brand: TandemVector Labs)

This document records GitHub **read-only evidence and a safe synchronization rule**; it does not itself synchronize repositories, transfer Issues or create releases.

## Verified default-branch snapshot

| Public repository | Authoritative personal head | Organization-fork head | Gate |
| --- | --- | --- | --- |
| ChatGPTRemoteCommander | `6f52f93cbc04ba30354b35cd144ffc96aaa20aba` | same | SHA MATCH |
| DirectInternetMethod | `26ef644117ea474b487186ce5e6e61e92cd02dd4` | same | SHA MATCH |
| FreeNetHub | `f65da9c8ff2ca9e6207aecc3c7e67b6b935ee6eb` | `cab6139d32c149b08ef69bc60a0d58c3c18e6f14` | **OPEN — FORK BEHIND** |
| OpenInternetGateway | `23f4fe514698102c7ecb735c7843fe25c594c8af` | same | SHA MATCH |
| TaskbarMonitorEnhanced | `86db0d17c438a255a19dbcfb94c5942922712ecd` | same | SHA MATCH |
| PersianWordAgent | `65aa3f85a9dccc23fcc19e26e4515ef7b5928697` | same | SHA MATCH |
| LTEMonitor (master) | `646c05592c3497e94ec4aa576aa06c8c3c6f0edf` | same | SHA MATCH |
| WSAGAScript | `99f034ef529aa39aa008e02befe8788cb9d86b46` | same | SHA MATCH |

**Evidence:** GitHub REST `git/ref/heads/{main|master}` read-back on both owners; full 40-character SHA checked in the same audit.

## FreeNetHub — critical sync delta

GitHub compare using base `cab6139d32c149b08ef69bc60a0d58c3c18e6f14` and head `f65da9c8ff2ca9e6207aecc3c7e67b6b935ee6eb` returned **status=ahead, ahead_by=2, behind_by=0**, with two changed files:

- `.github/workflows/ci.yml`: 51 removed lines (must verify CI gate semantics, not blindly assume equivalent coverage).
- `PUBLIC_MANIFEST.json`: checksum/metadata changes (validate exact affected source and manifest consistency before accepting promotion).

**Current source branch count: 2; fork branch count: 10.** The fork has eight additional historical branch refs that no longer exist in the personal repository. These must **not** be auto-deleted just to make counts equal. Classify each as historical retained evidence, superseded work, or unknown before any removal.

**Allowed mutation:** one non-force, fast-forward-only update of `Usefull-Skills/FreeNetHub:main`, guarded by **exact** source/destination head SHA and compare status ahead/behind. STOP if either head changed or downstream branch protection/rules are incompatible. Re-read both 40-character heads and inspect exact-head CI + `PUBLIC_MANIFEST.json` after update. Preserve former fork commit as immutable Git history. Do not modify the personal source.

**Current result:** no synchronization was performed in this audit. `FreeNetHub` parity remains OPEN.

## Rules for all public forks

1. The named personal upstream is the code/release authority unless a documented project decision promotes another source; do not silently switch remotes.
2. Record source/target repository IDs and exact SHA before any branch change; an HTTP success code alone is insufficient.
3. Synchronize only fast-forward-compatible branches. Never force push, blindly recreate unrelated tags, mirror-delete branches, squash history, or overwrite a divergent fork.
4. Recheck complete branch/tag refs with pagination; compare names and SHAs. `main` equality alone is not complete Git ref parity.
5. Preserve Issues, pull requests, Releases, Wiki, packages, CI environment and authentication boundaries: **GitHub Fork is not full GitHub service migration**.
6. Do not label an untested downstream CI/release gate PASS based on upstream tests.
7. Update the cumulative Project Brain and the [central acceptance issue](https://github.com/Usefull-Skills/.github/issues/1) after verified milestones.

## Additional downstream gates

- [TaskbarMonitorEnhanced fork native-GUI failure](https://github.com/GOD13emad/TaskbarMonitorEnhanced/issues/65): fork-hosted Windows lane A still fails physical UI acceptance despite upstream build PASS. Do not release-promote from failed fork tests.
- [OpenInternetGateway npm advisory assessment](https://github.com/GOD13emad/OpenInternetGateway/issues/6): two build-toolchain transitive advisories need independent mitigation and acceptance; no fixed version was listed by GitHub advisories as of this audit.
- GitHub App/CLI authorizations and organization owner 2FA must remain inside approved privilege boundaries.

**Definition of Done:** an independently reproduced, read-back-confirmed ref parity snapshot; verified branch-rule continuity; no secrets/visibility changes; no deleted history; applicable exact-head CI/packaging regression acceptance; cumulative Brain updated. Until these pass, **FINAL=OPEN**.
