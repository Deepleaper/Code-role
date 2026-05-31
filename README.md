# Code-role

Code-role is a discussion-first local role-configuration project for controlling Codex-assisted programming work.

It separates complex coding work into explicit roles, document packets, handoff manifests, status gates, and validation checks. The goal is to discuss and confirm each professional step before execution advances, instead of letting Codex run an automated code pipeline from chat-only instruction.

Except for Implementer after explicit approval, roles produce documents only. Each role's document packet becomes the next role's input.

## Product Docs

Product requirements and current scope:

- [`docs/product/prd.zh-CN.md`](docs/product/prd.zh-CN.md)
- [`docs/product/prd.md`](docs/product/prd.md)
- [`docs/product/code-role-workflow-guide.zh-CN.html`](docs/product/code-role-workflow-guide.zh-CN.html)

## Usage Model

Recommended current usage:

```text
Code-role project = role configuration, workflow protocol, packet outputs
Target code project = product code being discussed or changed
```

Create one configured Codex role instance per role. Do not run the whole workflow by switching roles inside one conversation.

Configured roles:

1. Workflow Orchestrator
2. Researcher
3. Product / PRD
4. Architect
5. Code Context
6. Implementer
7. Test Evaluator
8. Reviewer

Default boundary:

- local coordination layer
- not product repo content by default
- not release/package content by default
- add `docs/workflow/` and `tests/test_workflow_*.py` to the target project `.git/info/exclude`

Core workflow rule:

- every role conversation must point to that role's explicit output
- unrelated requests must be corrected and routed to the proper role
- non-Implementer roles do not change code
- Implementer starts only after the packet chain and user confirmation allow implementation
- upstream packet manifests must be passed between role instances explicitly

Alternative embedded usage:

- copy `docs/workflow/` and optional `tests/test_workflow_*.py` into a target project
- add them to `.git/info/exclude` if they should remain local workflow files

See [`docs/workflow/role-instance-setup.md`](docs/workflow/role-instance-setup.md).

Fast target-project bootstrap:

```bash
python scripts/init_project_workflow.py \
  --target "/path/to/Target Project" \
  --project-name "Target Project" \
  --tracking repo-tracked \
  --write
```

This creates `code-role/` project config, role-instance prompts, Orchestrator state, and a non-authoritative `state-index/`. It does not create execution packets or run Git operations.

See [`docs/workflow/project-bootstrap.md`](docs/workflow/project-bootstrap.md), [`docs/workflow/state-index.md`](docs/workflow/state-index.md), and [`docs/workflow/git-operation-policy.md`](docs/workflow/git-operation-policy.md).

## Start

Start in a target project with the Orchestrator command:

```text
项目经理，执行 startup routine，恢复当前状态
```

## Local Validation

Install test dependencies, then run:

```bash
python -m pytest -q
```

Validate a packet template:

```bash
python docs/workflow/tools/validate_workflow_packet.py docs/workflow/roles/researcher/templates
```
