#!/usr/bin/env python3
"""Initialize a target project's Code-role workflow scaffold.

The script creates navigation and role-start files only. It does not run role
work, create packets for execution roles, stage files, commit, push, or touch
business source files.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


ROLE_IDS = [
    "workflow-orchestrator",
    "researcher",
    "product-prd",
    "architect",
    "code-context",
    "implementer",
    "test-evaluator",
    "reviewer",
]

EXECUTION_ROLES = [role for role in ROLE_IDS if role != "workflow-orchestrator"]


@dataclass(frozen=True)
class BootstrapConfig:
    target: Path
    project_name: str
    code_role_root: Path
    tracking: str
    initial_milestone: str
    initial_chain: str
    external_research_allowed: bool
    force: bool
    write: bool

    @property
    def workflow_root(self) -> Path:
        return self.target / "code-role" / "workflow"

    @property
    def project_config_root(self) -> Path:
        return self.target / "code-role"


def workflow_doc_path(config: BootstrapConfig, relative: str) -> str:
    return str(config.code_role_root / "docs" / "workflow" / relative)


def role_contract_path(config: BootstrapConfig, role_id: str) -> str:
    if role_id == "workflow-orchestrator":
        return workflow_doc_path(config, "orchestrator/ROLE.md")
    return workflow_doc_path(config, f"roles/{role_id}/ROLE.md")


def render_project_readme(config: BootstrapConfig) -> str:
    return f"""# Code-role Project Configuration

This directory configures Code-role for `{config.project_name}`.

This folder is local-only workflow assistance. It is not product runtime content, is not part of the target project's delivery, and should not be committed or pushed with the target project.

## Authoritative Sources

- `workflow/orchestrator/workflow-state.md`
- `workflow/orchestrator/milestone-registry.md`
- `workflow/orchestrator/decision-log.md`
- role packet `handoff.manifest.json` files
- ready packet `packet.lock.json` files

`state-index/` is only a non-authoritative navigation index for role onboarding.

## Role Instances

Start each Codex role in its own conversation. Use the matching prompt in `role-instance-prompts/`.

## Git Boundary

Code-role does not own the target project's Git workflow.

Use the project's normal Git process for product changes. Role conversations may report Git-related facts, but they must not create workflow gates for `git add`, `git commit`, or `git push`.
"""


def render_project_config(config: BootstrapConfig) -> str:
    external = "true" if config.external_research_allowed else "false"
    return f"""# Project Config

project_name: {config.project_name}
target_project_path: {config.target}
workflow_root: {config.workflow_root}
tracking_policy: {config.tracking}
external_research_allowed_default: {external}

## Boundary

- `code-role/` is local-only workflow assistance, not product runtime content.
- `code-role/` should not be committed or pushed with this target project.
- `code-role/state-index/` is a non-authoritative navigation index.
- Orchestrator state, packet manifests, and packet locks remain authoritative.
- Product release artifacts must exclude `code-role/`.

## Git Boundary

Code-role does not own the target project's Git workflow. Use the project's normal Git process for product changes.

Role conversations may report changed files or untracked workflow files, but they must not require Orchestrator or Reviewer gates for normal `git add`, `git commit`, or `git push`.

## Initial State

initial_milestone: {config.initial_milestone}
initial_chain: {config.initial_chain}
"""


def render_orchestrator_state(config: BootstrapConfig) -> str:
    return f"""# Workflow State

project: {config.project_name}
target_project_path: {config.target}
workflow_root: {config.workflow_root}

current_milestone: {config.initial_milestone}
selected_chain: {config.initial_chain}
current_authoritative_packet: none
packet_status: none
consumable_check: fail
workflow_status: initialized

current_blocker: First real milestone and next role require user confirmation.
recommended_next_role: workflow-orchestrator

authoritative_note: This file is Orchestrator state. Role state indexes are non-authoritative navigation only.
"""


def render_milestone_registry(config: BootstrapConfig) -> str:
    return f"""# Milestone Registry

## {config.initial_milestone}

- chain: {config.initial_chain}
- status: initialized
- authoritative_packet: none
- next_required_confirmation: Confirm first real milestone, chain, and role start.
"""


def render_decision_log(config: BootstrapConfig) -> str:
    return f"""# Decision Log

## 2026-05-31 - Bootstrap project workflow

- decision: Initialized Code-role workflow scaffold for `{config.project_name}`.
- tracking_policy: {config.tracking}
- initial_milestone: {config.initial_milestone}
- initial_chain: {config.initial_chain}
- boundary: No execution-role packet has been created by bootstrap.
- next_confirmation: User must confirm the first real milestone and role start.
"""


def render_role_prompt(config: BootstrapConfig, role_id: str) -> str:
    index_path = config.project_config_root / "state-index" / "roles" / f"{role_id}.md"
    if role_id == "workflow-orchestrator":
        role_name = "workflow-orchestrator"
        output_boundary = "Only update Orchestrator state files after user-confirmed routing decisions."
        upstream = "none unless explicitly provided"
    else:
        role_name = role_id
        output_boundary = f"Only write this role's packet under `code-role/workflow/roles/{role_id}/reports/<milestone>/packet-vNNN/`."
        upstream = "<paste exact upstream handoff.manifest.json path>"

    return f"""# Start {role_name}

You are the `{role_name}` role for `{config.project_name}`.

Read first:

- {workflow_doc_path(config, "README.md")}
- {workflow_doc_path(config, "discussion-first-protocol.md")}
- {workflow_doc_path(config, "role-instance-setup.md")}
- {workflow_doc_path(config, "handoff-protocol.md")}
- {workflow_doc_path(config, "packet-schema.md")}
- {workflow_doc_path(config, "source-map.md")}
- {role_contract_path(config, role_id)}
- {index_path}

Target project:

```text
{config.target}
```

Current upstream input:

```text
{upstream}
```

Rules:

- Do not switch roles inside this conversation.
- Confirm read and write boundaries before creating output.
- {output_boundary}
- Do not modify upstream packets.
- Do not run network calls unless explicitly allowed.
- Do not run `git add`, `git commit`, or `git push`.
- Do not mark a draft packet `ready_for_next_role` unless the user explicitly requests strict handoff.
- When you finish a draft or ready packet, end your response with an Orchestrator consumption-check request block using the template at `{workflow_doc_path(config, "orchestrator/consumption-check-request-template.md")}`.
- You may recommend a downstream role, but you must not generate the authoritative next-role startup message. Orchestrator owns consumable checks, chain routing, and next-role startup message generation.

First response:

1. State which files you will read.
2. State what you will write, if anything.
3. State forbidden scope.
4. Wait for user confirmation before writing.
"""


def render_state_index_readme(config: BootstrapConfig) -> str:
    return f"""# State Index

This directory is a non-authoritative navigation index for Code-role role onboarding in `{config.project_name}`.

It does not replace:

- Orchestrator state files
- role `handoff.manifest.json` files
- ready packet `packet.lock.json` files

Use this directory to find the current role entry point faster. If any conflict exists, trust the authoritative packet chain and Orchestrator state, not this index.

This index is not product runtime content and must be excluded from release artifacts.
"""


def render_current_workflow_index(config: BootstrapConfig) -> str:
    return f"""# Current Workflow Index

Status: initialized

This is a non-authoritative navigation index.

## Current State

- project: {config.project_name}
- target_project_path: `{config.target}`
- workflow_root: `{config.workflow_root}`
- current milestone: `{config.initial_milestone}`
- selected chain: `{config.initial_chain}`
- authoritative packet: none
- current gate: initialized
- final_acceptance: false

## Completed Packet Chain

None yet.

## Residual Risks

- No execution packet exists yet.
- `code-role/` is local-only and should remain outside the target project's Git history.

## Recommended Next Step

Start Orchestrator, confirm the first real milestone and selected chain, then route to the first execution role.
"""


def render_role_index(config: BootstrapConfig, role_id: str) -> str:
    upstream = "none" if role_id in {"workflow-orchestrator", "researcher"} else "pending Orchestrator routing"
    status = "current-authoritative" if role_id == "workflow-orchestrator" else "not-started"
    return f"""# Role State Index: {role_id}

This file is a non-authoritative navigation index. It helps this role start faster, but it does not replace ROLE.md, Orchestrator state, handoff manifests, or packet locks.

## Role Responsibility

Read the role contract:

```text
{role_contract_path(config, role_id)}
```

Do not infer role duties from this index alone.

## Current Status In This Project

- status: {status}
- current milestone: `{config.initial_milestone}`
- selected chain: `{config.initial_chain}`
- official upstream manifest: {upstream}
- traceability manifests: none

## Must-Read Files

- `{workflow_doc_path(config, "README.md")}`
- `{workflow_doc_path(config, "discussion-first-protocol.md")}`
- `{workflow_doc_path(config, "role-instance-setup.md")}`
- `{workflow_doc_path(config, "handoff-protocol.md")}`
- `{workflow_doc_path(config, "packet-schema.md")}`
- `{workflow_doc_path(config, "source-map.md")}`
- `{role_contract_path(config, role_id)}`
- `{config.workflow_root / "orchestrator" / "workflow-state.md"}`
- `{config.workflow_root / "orchestrator" / "milestone-registry.md"}`
- `{config.workflow_root / "orchestrator" / "decision-log.md"}`

## Allowed Read Scope

- This role's workflow protocol files and ROLE.md.
- Exact upstream manifests explicitly provided by Orchestrator or the user.
- Files listed by accepted upstream manifests.
- Target project files only inside explicitly approved source-map scope.

## Forbidden Scope

- Do not modify upstream packets.
- Do not modify Orchestrator state unless this is the Orchestrator role.
- Do not modify business files unless this is an approved Implementer step with exact writable scope.
- Do not run `git add`, `git commit`, or `git push`.
- Do not include `code-role/` in target-project commits or product release artifacts.

## Current Gate / Status

- gate: initialized
- ready_for_next_role: false
- final_acceptance: false

## Residual Risks

- No execution packet exists yet.
- Current authoritative state must be refreshed from Orchestrator before this role starts.

## Next Required Confirmation

Orchestrator and user must confirm whether this role should start and which exact upstream manifest it should consume.

## Authoritative Sources

- ROLE contract above
- Orchestrator state files under `{config.workflow_root / "orchestrator"}`
- Any exact upstream manifest later provided by Orchestrator
"""


def planned_files(config: BootstrapConfig) -> dict[Path, str]:
    root = config.project_config_root
    files = {
        root / "README.md": render_project_readme(config),
        root / "project-config.md": render_project_config(config),
        config.workflow_root / "orchestrator" / "workflow-state.md": render_orchestrator_state(config),
        config.workflow_root / "orchestrator" / "milestone-registry.md": render_milestone_registry(config),
        config.workflow_root / "orchestrator" / "decision-log.md": render_decision_log(config),
        root / "state-index" / "README.md": render_state_index_readme(config),
        root / "state-index" / "current-workflow-index.md": render_current_workflow_index(config),
    }
    for role_id in ROLE_IDS:
        files[root / "role-instance-prompts" / f"{role_id}.md"] = render_role_prompt(config, role_id)
        files[root / "state-index" / "roles" / f"{role_id}.md"] = render_role_index(config, role_id)
    return files


def write_files(config: BootstrapConfig) -> list[Path]:
    written: list[Path] = []
    for path, content in planned_files(config).items():
        if path.exists() and not config.force:
            continue
        if config.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        written.append(path)
    return written


def ensure_local_git_exclude(config: BootstrapConfig) -> bool:
    exclude_path = config.target / ".git" / "info" / "exclude"
    if not exclude_path.exists():
        return False

    text = exclude_path.read_text(encoding="utf-8")
    patterns = [line.strip() for line in text.splitlines()]
    if "code-role/" in patterns:
        return False

    suffix = "" if text.endswith("\n") or not text else "\n"
    if config.write:
        exclude_path.write_text(f"{text}{suffix}code-role/\n", encoding="utf-8")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path, help="Target project path.")
    parser.add_argument("--project-name", help="Project display name. Defaults to target folder name.")
    parser.add_argument(
        "--tracking",
        default="local-only",
        choices=["local-only"],
        help="Generated code-role files are local-only target-project workflow assistance.",
    )
    parser.add_argument("--initial-milestone", default="workflow-bootstrap")
    parser.add_argument("--initial-chain", default="research-only")
    parser.add_argument("--external-research-allowed", action="store_true")
    parser.add_argument("--force", action="store_true", help="Overwrite existing scaffold files.")
    parser.add_argument("--write", action="store_true", help="Write files. Omit for dry-run.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    code_role_root = Path(__file__).resolve().parents[1]
    target = args.target.expanduser().resolve()
    config = BootstrapConfig(
        target=target,
        project_name=args.project_name or target.name,
        code_role_root=code_role_root,
        tracking=args.tracking,
        initial_milestone=args.initial_milestone,
        initial_chain=args.initial_chain,
        external_research_allowed=args.external_research_allowed,
        force=args.force,
        write=args.write,
    )

    files = write_files(config)
    exclude_updated = ensure_local_git_exclude(config)
    action = "created/updated" if config.write else "would create/update"
    for path in files:
        print(f"{action}: {path}")
    if exclude_updated:
        exclude_action = "updated" if config.write else "would update"
        print(f"{exclude_action}: {config.target / '.git' / 'info' / 'exclude'}")
    if not files:
        print("no files changed")
    if not config.write:
        print("dry-run only; rerun with --write to create files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
