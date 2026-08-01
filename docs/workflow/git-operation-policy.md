# Git Boundary Policy

Git operations are outside the Code-role role chain.

Code-role controls role collaboration and delivery quality. It does not own the target project's Git workflow.

## Default Rule

Use the target project's normal Git process.

Roles may report Git-related facts, such as:

- changed files
- untracked files
- unrelated dirty files
- whether generated local workflow files are present

Roles must not require an Orchestrator or Reviewer gate for normal `git add`, `git commit`, or `git push`.

## Local-Only Workflow Files

Target-project `code-role/` files are local workflow assistance by default. They are not product source, not product runtime content, and not delivery artifacts.

Project bootstrap should add `code-role/` to the target repository's `.git/info/exclude` when that file exists.

## Direct User Requests

If the user directly asks Codex to run a Git command, handle it as a normal project maintenance request:

- inspect current status
- avoid unrelated dirty files
- stage only the requested scope
- do not push unless the user asks for push

This is not a Code-role packet transition and does not require a new role milestone.

## Forbidden Defaults

Roles must not:

- treat uncommitted `code-role/` files as a blocker for business work
- create a Git milestone just to run normal Git commands
- require Reviewer approval for ordinary staging or pushing
- include local `code-role/` files in product release artifacts
- treat `review_gate_pass=0` as milestone closure

`review_gate_pass=0` means the role chain has not closed milestone acceptance. It does not mean ordinary target-project Git work is blocked.
