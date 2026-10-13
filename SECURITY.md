# Security Policy

## Scope and supported versions

Security support is **repository- and release-specific**. The organization profile does not promise that every repository, fork, experimental branch, or preview release is maintained or supported. Check the project's README, release notes and SECURITY.md for version-specific guidance.

## Responsible vulnerability reporting

**Do not disclose an exploitable vulnerability, credential, authentication token, personally identifying information, browser session, or private configuration in a public issue or pull request.**

Use the repository's **Private vulnerability reporting / Security advisories** feature when it is enabled. If private reporting is unavailable, first request a suitable confidential contact channel through a non-sensitive message to maintainers; do not reveal exploit details in that request.

A useful private report includes the affected repo and version/commit, vulnerable component, reproduction prerequisites, minimized steps and impact, affected platforms, and suggested mitigations. Avoid testing against systems that you do not own or have permission to assess.

## Coordination and response

Project maintainers will assess reports, establish severity and affected releases, prioritize a fix, document necessary disclosure coordination, and issue versioned release/rollback guidance when a fix has been validated. There is no guaranteed response or patch SLA for experimental or archival work.

## Hardening principles

- Keep authenticated browser profiles, tokens, secret files and project-private datasets out of public repositories and CI logs.
- Use scoped GitHub permissions and least-privilege workflow tokens.
- Do not disable Chromium sandboxing or certificate validation as a workaround without a separately approved, verified threat model.
- Treat upstream Git history, licenses and third-party advisories as authoritative for imported forks.
- Verify build, runtime, security regression and user acceptance separately.

This default policy is inherited only by repositories that do not define their own security policy.
