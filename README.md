# Code-role

Code-role is a local workflow template for controlling Codex-assisted software delivery.

It separates complex coding work into explicit roles, document packets, handoff manifests, status gates, and validation checks. The goal is to keep product scope, architecture, code context, implementation, testing, and review from collapsing into one chat-only process.

## Product Docs

Product requirements and current scope:

- [`docs/product/prd.zh-CN.md`](docs/product/prd.zh-CN.md)
- [`docs/product/prd.md`](docs/product/prd.md)

## Workflow Template

Copy `docs/workflow/` and optional `tests/test_workflow_*.py` into a target project when you want to configure role-based workflow locally.

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
