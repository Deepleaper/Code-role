#!/usr/bin/env python3
"""Initialize or sync the Code-role four-workstation Minimal Profile."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "loop"

ROLE_FILES = (
    "project-manager.md",
    "product-strategy.md",
    "engineering.md",
    "independent-evaluation.md",
)

TEMPLATE_FILES = (
    "assignment.md",
    "product-return.md",
    "engineering-return.md",
    "evaluation-return.md",
    "pm-decision.md",
)

FULL_PROFILE_ROLE_FILES = (
    "workflow-orchestrator.md",
    "researcher.md",
    "product-prd.md",
    "architect.md",
    "code-context.md",
    "implementer.md",
    "test-evaluator.md",
    "reviewer.md",
)


def render(source: Path, project_name: str, project_root: Path) -> str:
    text = source.read_text(encoding="utf-8")
    return (
        text.replace("{{PROJECT_NAME}}", project_name)
        .replace("{{PROJECT_ROOT}}", str(project_root))
    )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def ensure_local_exclude(project_root: Path) -> None:
    exclude = project_root / ".git" / "info" / "exclude"
    if not exclude.parent.exists():
        return
    current = exclude.read_text(encoding="utf-8") if exclude.exists() else ""
    lines = current.splitlines()
    if any(line.strip().rstrip("/") == "code-role" for line in lines):
        return
    suffix = "" if not current or current.endswith("\n") else "\n"
    exclude.write_text(f"{current}{suffix}code-role/\n", encoding="utf-8")


def archive_full_profile_roles(code_role: Path) -> None:
    role_root = code_role / "role-instance-prompts"
    archive_root = code_role / "archive" / "full-profile-role-instance-prompts"
    for filename in FULL_PROFILE_ROLE_FILES:
        source = role_root / filename
        if not source.exists():
            continue
        archive_root.mkdir(parents=True, exist_ok=True)
        destination = archive_root / filename
        if not destination.exists():
            shutil.copy2(source, destination)
        source.unlink()


def render_project_readme(project_name: str) -> str:
    return f"""# {project_name} Code-role

This directory is local-only role-control assistance. It is not product runtime content and is excluded from the target project's Git delivery by local `.git/info/exclude`.

本目录是本地角色控制辅助，不是产品运行时代码，并通过本地 `.git/info/exclude` 排除在目标项目 Git 交付之外。

## Active Model / 当前模型

One Project Manager controls three callable professional workstations around one milestone board:

- [Project Manager / 项目经理](role-instance-prompts/project-manager.md)
- [Product Strategy / 产品策略](role-instance-prompts/product-strategy.md)
- [Engineering / 工程](role-instance-prompts/engineering.md)
- [Independent Evaluation / 独立评估](role-instance-prompts/independent-evaluation.md)

`milestone-board.md` is the only active state. `LOOP.md` defines the loop contract.

`milestone-board.md` 是唯一活跃状态，`LOOP.md` 定义闭环协议。

## Use / 使用

1. Open the Project Manager conversation.
2. Give it `role-instance-prompts/project-manager.md`.
3. Confirm the Objective and Key Results.
4. Project Manager prints one copy-ready assignment for one `KR=0`.
5. Paste it into the selected workstation conversation; a valid assignment starts immediately.
6. Paste the workstation's fixed return back to Project Manager.
7. Repeat until every accepted KR has independent evidence and equals `1`.

Only the selected workstation runs. There is no fixed four-role chain.

每轮只运行被选中的工位，不存在固定四角色链。

## History / 历史

`workflow/`, `state-index/`, and `archive/` may contain useful history. They do not route current work and cannot update milestone status.

## Git / Git 边界

Code-role follows the project's normal Git and release process. It does not create separate `git add`, `commit`, or `push` gates.
"""


def render_start_here(project_name: str) -> str:
    return f"""# Start Here / 从这里开始

Project: `{project_name}`

1. Start or refresh the Project Manager conversation with `role-instance-prompts/project-manager.md`.
2. The Project Manager reads `LOOP.md` and `milestone-board.md`.
3. Confirm one Objective and no more than five binary Key Results.
4. Copy the Project Manager's single `PM Assignment` into the selected workstation conversation.
5. A complete assignment starts work immediately; do not add a separate `开始` step.
6. Copy the fixed workstation return back to Project Manager.
7. Project Manager updates the board from accepted evidence and selects the next `KR=0`.

Only Objective/KR changes, evaluation-threshold changes, budget expansion, and irreversible external actions require an additional human gate.

只有 Objective/KR 变更、评估阈值变更、预算扩展和不可逆外部操作需要额外人工确认。
"""


def render_project_config(project_name: str, project_root: Path) -> str:
    return f"""# Project Config

project_name: {project_name}
target_project_path: {project_root}
tracking_policy: local-only
control_model: goal-loop-v2
authoritative_control_record: {project_root / "code-role" / "milestone-board.md"}
loop_contract: {project_root / "code-role" / "LOOP.md"}
active_role_root: {project_root / "code-role" / "role-instance-prompts"}
active_roles:
- project-manager
- product-strategy
- engineering
- independent-evaluation
transport_model: manual-copy-ready-assignment-and-return
valid_assignment_starts_immediately: true
fixed_role_chain: false
completion_model: binary-key-results
default_iteration_limit_per_kr: 3
external_research_allowed_default: true

## Boundary

- `code-role/` is local-only assistance, not product runtime content.
- `milestone-board.md` is the only active control state.
- Full Profile packets and state indexes may remain as history, but they do not control a project while the Minimal Profile is active.
- Product attachments carry professional content; Project Manager references them instead of rewriting them.
- Code-role does not own the target project's Git or release process.
"""


def render_role_readme() -> str:
    return """# Active Role Prompts / 活跃角色提示词

Exactly four prompts are active:

- `project-manager.md`
- `product-strategy.md`
- `engineering.md`
- `independent-evaluation.md`

The Project Manager is always the controller. The other three workstations are called dynamically for one selected `KR=0`; they are not a fixed chain.

项目经理始终是控制器。其他三个工位围绕一个被选中的 `KR=0` 动态调用，不构成固定链路。

Full Profile prompt filenames are archived under `code-role/archive/` during sync so the active prompt directory contains exactly four Minimal Profile workstations.
"""


def render_work_readme() -> str:
    return """# Professional Attachments / 专业附件

Store detailed work under:

`code-role/work/<milestone>/`

Recommended filenames:

- Product Strategy: `product-decision-<assignment-id>.md`
- Engineering: `engineering-report-<assignment-id>.md`
- Independent Evaluation baseline: `evaluation-sop-<assignment-id>.md`
- Independent Evaluation result: `evaluation-report-<assignment-id>.md`

Attachments contain professional detail and evidence. They do not route work or update KR status. The fixed role return points to the attachment, and Project Manager decides whether to accept it.
"""


def initialize(project_root: Path, project_name: str, sync: bool) -> list[Path]:
    project_root = project_root.resolve()
    code_role = project_root / "code-role"
    if code_role.exists() and not sync:
        raise RuntimeError(
            f"{code_role} already exists; rerun with --sync to update role rules."
        )

    code_role.mkdir(parents=True, exist_ok=True)
    if sync:
        archive_full_profile_roles(code_role)

    generated: dict[Path, str] = {
        code_role / "README.md": render_project_readme(project_name),
        code_role / "START-HERE.md": render_start_here(project_name),
        code_role / "project-config.md": render_project_config(project_name, project_root),
        code_role / "LOOP.md": render(SOURCE / "LOOP.md", project_name, project_root),
        code_role / "role-instance-prompts" / "README.md": render_role_readme(),
        code_role / "work" / "README.md": render_work_readme(),
    }

    for filename in ROLE_FILES:
        generated[code_role / "role-instance-prompts" / filename] = render(
            SOURCE / "roles" / filename, project_name, project_root
        )
    for filename in TEMPLATE_FILES:
        generated[code_role / "templates" / filename] = render(
            SOURCE / "templates" / filename, project_name, project_root
        )

    milestone_board = code_role / "milestone-board.md"
    if not milestone_board.exists():
        generated[milestone_board] = render(
            SOURCE / "templates" / "milestone-board.md", project_name, project_root
        )

    for path, text in generated.items():
        write_text(path, text)

    ensure_local_exclude(project_root)
    return sorted(generated)


def validate(project_root: Path) -> list[str]:
    project_root = project_root.resolve()
    code_role = project_root / "code-role"
    errors: list[str] = []

    required = [
        code_role / "LOOP.md",
        code_role / "milestone-board.md",
        code_role / "templates" / "assignment.md",
        code_role / "templates" / "pm-decision.md",
    ]
    required.extend(code_role / "role-instance-prompts" / name for name in ROLE_FILES)
    for path in required:
        if not path.exists():
            errors.append(f"missing: {path}")

    if errors:
        return errors

    loop = (code_role / "LOOP.md").read_text(encoding="utf-8")
    required_loop_markers = (
        "One KR Per Iteration",
        "Valid Assignment Starts Work",
        "Evaluation Before Pass",
        "three failed Engineering-to-Evaluation attempts",
        "There is no `partial_pass`",
    )
    for marker in required_loop_markers:
        if marker not in loop:
            errors.append(f"LOOP.md missing marker: {marker}")

    role_root = code_role / "role-instance-prompts"
    active_markdown = {
        path.name for path in role_root.glob("*.md") if path.name != "README.md"
    }
    if active_markdown != set(ROLE_FILES):
        errors.append(
            "active role prompts must be exactly: " + ", ".join(ROLE_FILES)
        )

    combined_roles = "\n".join(
        (role_root / name).read_text(encoding="utf-8") for name in ROLE_FILES
    )
    forbidden_markers = (
        "ready_for_next_role",
        "packet.lock.json",
        "自动创建产品策略",
    )
    for marker in forbidden_markers:
        if marker in combined_roles:
            errors.append(f"active Minimal Profile prompts contain packet-profile marker: {marker}")

    assignment = (code_role / "templates" / "assignment.md").read_text(
        encoding="utf-8"
    )
    for marker in (
        "current_kr_status: 0",
        "iteration:",
        "role_prompt_path:",
        "frozen_pass_conditions:",
        "stop_conditions:",
    ):
        if marker not in assignment:
            errors.append(f"assignment template missing marker: {marker}")

    board = (code_role / "milestone-board.md").read_text(encoding="utf-8")
    for marker in (
        "Evaluation SOP frozen",
        "Current KR",
        "Current iteration",
        "Milestone pass",
    ):
        if marker not in board:
            errors.append(f"milestone board missing marker: {marker}")
    if "自动派发" in board:
        errors.append("milestone board must not claim automatic dispatch")

    project_manager = (role_root / "project-manager.md").read_text(
        encoding="utf-8"
    )
    for marker in (
        "manual transport",
        "Do not claim automatic dispatch",
        "exactly one accepted `KR=0` per iteration",
    ):
        if marker not in project_manager:
            errors.append(f"project manager prompt missing marker: {marker}")

    evaluator = (role_root / "independent-evaluation.md").read_text(
        encoding="utf-8"
    )
    for marker in (
        "baseline_freeze",
        "full_evaluation",
        "Every required unrun check is `0`",
        "not only the latest diff",
        "Do not use `partial_pass` or `pass_with_residual_risk`",
    ):
        if marker not in evaluator:
            errors.append(f"evaluator prompt missing marker: {marker}")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path, help="Target project path.")
    parser.add_argument("--project-name", help="Project display name.")
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Refresh Minimal Profile rules while preserving milestone state and work.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate an initialized Minimal Profile without writing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = args.project_root.resolve()
    if args.check:
        errors = validate(project_root)
        if errors:
            for error in errors:
                print(error, file=sys.stderr)
            return 1
        print(f"goal-loop validation passed: {project_root}")
        return 0

    project_name = args.project_name or project_root.name
    try:
        paths = initialize(project_root, project_name, args.sync)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
