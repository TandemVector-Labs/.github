# Contributing to TandemVector Labs projects

Thank you for helping improve an engineering or software project in this organization.

## Choose the authoritative repository

Every repository has its own status, license, support policy, and release process. For first-party projects with a verified personal upstream, submit source changes to that canonical personal repository by default when source is published. For binary-only distributions (currently PersianWordAgent), use the published issue/report path; do not assume source is available for code contributions. Use the matching organization fork for joint review, integration QA and shared coordination where source and repository policy permit. Preserve existing organization issue intake and cross-link the canonical source issue or PR instead of duplicating or moving history. Existing publication/updater authority and private visibility remain unchanged. Organization-origin and other projects require their own accepted source authority. Legacy third-party fork chains (LTEMonitor, WSAGAScript) continue to follow their original maintainers and licenses. See [Shared development home](COLLABORATION_HOME.md) and [Governance](GOVERNANCE.md).

Read the destination repository's README, existing contribution guidance, security policy and build instructions. **Repository-specific policies override this default.**

## Bug reports

Before filing, search for an existing report. Include:
- Exact repository, release/tag/commit, OS/architecture, and relevant versioned dependencies
- Expected behavior, observed behavior and reproducible steps
- Minimal sanitized logs, error messages and environment information
- Whether the behavior is reproducible on a clean, isolated setup
- Evidence of regression if applicable

Never post credentials, session data, tokens, personally identifying data, or private project files.

## Pull requests

Keep each PR focused on one problem. Explain the reason for the change, affected components, testing performed, observed results, known limitations and rollback approach. Preserve compatibility unless an intentional breaking change is documented. Add or update tests for a bug fix. Do not claim **PASS**, **released** or **final** merely because code compiles or CI starts.

Retain copyright, source provenance, upstream acknowledgments and third-party licenses. Do not introduce dependencies or code whose licensing status is unknown. Automated changes must state their source and must be reviewed by an authorized maintainer.

## Review and merge

Owners or explicitly authorized maintainers review changes. Changes to security boundaries, release assets, deployment, credentials, public visibility, and repository history require additional review proportional to risk.

**Important:** These are contribution guidelines, not a statement that GitHub enforces two-person approval on every repository. Check actual branch rules and status checks before merging.

## Language

English and Persian contributions are welcome. Use English for portable command and API examples, and preserve correct formatting for Persian RTL text.
