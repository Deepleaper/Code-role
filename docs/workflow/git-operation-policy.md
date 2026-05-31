# Git Operation Policy

Git operations are not automatic workflow steps.

The Code-role workflow may recommend staging, committing, or pushing, but it must not perform those operations without explicit user confirmation.

## Decision Rights

The project owner decides whether to run Git operations.

The Orchestrator may:

- prepare a staging plan
- identify exact paths to include and exclude
- record user authorization
- route to an approved Git operation step

The Reviewer may:

- evaluate whether the packet chain supports moving to Git operations
- record residual risks
- recommend `approve`, `request_changes`, or `pass_with_residual_risk`

The executor may run Git commands only after the user explicitly approves the exact operation.

## Separate Confirmation Gates

Confirm each class of operation separately:

1. `git add`
2. `git commit`
3. `git push`

Do not combine all three into one broad approval.

Target-project bootstrap files must repeat this rule in `code-role/README.md` and `code-role/project-config.md`. The rule needs to be visible at the project entry point, not only in the upstream Code-role template documentation.

## Staging Plan Requirements

Before `git add`, produce a staging plan that lists:

- exact paths to stage
- exact dirty files to exclude
- whether workflow packet history is included
- whether generated files are included
- whether release artifacts are affected
- the command that would be run

The staging plan should prefer explicit file and directory whitelists over broad commands such as `git add .`.

## Release Boundary

Workflow governance files may be committed as repository history when explicitly approved. That does not make them product release content.

Unless explicitly approved, exclude workflow governance from:

- generated template indexes
- customer delivery bundles
- CLI template payloads
- runtime package artifacts
- public release evidence

Recommended policy text:

```text
code-role/ is repo-tracked governance infrastructure.
It is not product runtime content.
It must be excluded from generated template indexes, customer delivery bundles, CLI template payloads, and release artifacts unless explicitly approved.
```

## Forbidden Defaults

Roles must not:

- stage unrelated dirty files
- stage broad repository state without a plan
- run `git commit` before staged diff review
- run `git push` before commit review
- treat `pass_with_residual_risk` as final acceptance
- treat `final_acceptance=false` as closed
