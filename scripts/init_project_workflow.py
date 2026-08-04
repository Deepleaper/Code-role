#!/usr/bin/env python3
"""Initialize the Code-role Full Profile eight-role scaffold."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DOCS = ROOT / "docs" / "workflow"

ROLE_CONFIG = {
    "workflow-orchestrator": {
        "name": "Workflow Orchestrator / 项目经理",
        "contract": WORKFLOW_DOCS / "orchestrator" / "ROLE.md",
        "output_standard": WORKFLOW_DOCS / "orchestrator" / "project-manager-output-standard.md",
    },
    "researcher": {
        "name": "Researcher / 研究员",
        "contract": WORKFLOW_DOCS / "roles" / "researcher" / "ROLE.md",
        "output_standard": WORKFLOW_DOCS / "roles" / "researcher" / "researcher-output-standard.md",
    },
    "product-prd": {
        "name": "Product / PRD / 产品经理",
        "contract": WORKFLOW_DOCS / "roles" / "product-prd" / "ROLE.md",
        "output_standard": WORKFLOW_DOCS / "roles" / "product-prd" / "product-prd-output-standard.md",
    },
    "architect": {
        "name": "Architect / 架构师",
        "contract": WORKFLOW_DOCS / "roles" / "architect" / "ROLE.md",
        "output_standard": WORKFLOW_DOCS / "roles" / "architect" / "architect-output-standard.md",
    },
    "code-context": {
        "name": "Code Context / 上下文工程师",
        "contract": WORKFLOW_DOCS / "roles" / "code-context" / "ROLE.md",
        "output_standard": WORKFLOW_DOCS / "roles" / "code-context" / "code-context-output-standard.md",
    },
    "implementer": {
        "name": "Implementer / 实现工程师",
        "contract": WORKFLOW_DOCS / "roles" / "implementer" / "ROLE.md",
        "output_standard": WORKFLOW_DOCS / "roles" / "implementer" / "implementer-output-standard.md",
    },
    "test-evaluator": {
        "name": "Test Evaluator / 测试评估师",
        "contract": WORKFLOW_DOCS / "roles" / "test-evaluator" / "ROLE.md",
        "output_standard": WORKFLOW_DOCS / "roles" / "test-evaluator" / "test-evaluator-output-standard.md",
    },
    "reviewer": {
        "name": "Reviewer / 复核审计",
        "contract": WORKFLOW_DOCS / "roles" / "reviewer" / "ROLE.md",
        "output_standard": WORKFLOW_DOCS / "roles" / "reviewer" / "reviewer-output-standard.md",
    },
}

EXECUTION_ROLES = tuple(role for role in ROLE_CONFIG if role != "workflow-orchestrator")


@dataclass(frozen=True)
class Config:
    target: Path
    project_name: str
    initial_milestone: str
    initial_chain: str
    external_research_allowed: bool
    with_state_index: bool
    force: bool
    write: bool

    @property
    def code_role(self) -> Path:
        return self.target / "code-role"

    @property
    def workflow(self) -> Path:
        return self.code_role / "workflow"


def render(text: str, config: Config) -> str:
    return (
        text.replace("{{PROJECT_NAME}}", config.project_name)
        .replace("{{PROJECT_ROOT}}", str(config.target))
        .replace("{{MILESTONE}}", config.initial_milestone)
    )


def source_text(path: Path, config: Config) -> str:
    return render(path.read_text(encoding="utf-8"), config)


def render_project_readme(config: Config) -> str:
    return f"""# {config.project_name} Code-role Full Profile

This directory is local-only role-control assistance. It is not product runtime or release content.

本目录是本地角色控制辅助，不是产品运行时或发布内容。

## Use / 使用

1. Configure the eight conversations once from `role-instance-prompts/`.
2. Open `workflow-orchestrator` and accept one complete Objective with `MKR-1...MKR-N` under `OKR-STANDARD.md`.
3. Product / PRD creates one complete `PKR-1...PKR-N` contract covering every MKR.
4. Architecture and Code Context cover the complete Product OKR when needed.
5. Implementer alone defines `EKR-1...EKR-N` and produces the complete runnable candidate.
6. Test Evaluator starts only after candidate readiness and evaluates the full MKR/PKR contract.
7. Reviewer, when required, audits the complete final chain before closure.

## Active Control / 活跃控制

- `DIALOGUE-CONTROL.md`
- `OKR-STANDARD.md`
- `workflow/orchestrator/milestone-contract.md`
- `workflow/orchestrator/workflow-state.md`
- `workflow/evaluation/evaluation-sop.md`
- accepted primary professional artifacts and evidence

Packet manifests are optional provenance indexes. Readiness conversion and packet locks are optional strict-audit controls, not normal delivery gates.

## Git / Git 边界

Code-role follows the target project's normal Git and release process. It does not create separate add/commit/push gates.
"""


def render_project_config(config: Config) -> str:
    research = "true" if config.external_research_allowed else "false"
    return f"""# Project Config

project_name: {config.project_name}
target_project_path: {config.target}
control_profile: full-eight-role
control_model: okr-delivery-v4
tracking_policy: local-only
initial_milestone: {config.initial_milestone}
initial_chain_hint: {config.initial_chain}
external_research_allowed_default: {research}
valid_assignment_starts_immediately: true
startup_acknowledgement_required: false
format_only_rework_allowed: false
role_self_routing_allowed: false
completion_model: binary
mandatory_delivery_order: complete-milestone-okr -> complete-product-okr -> engineering-candidate -> independent-evaluation -> review-when-required

authoritative_control:
- {config.workflow / 'orchestrator' / 'milestone-contract.md'}
- {config.workflow / 'orchestrator' / 'workflow-state.md'}
- {config.workflow / 'evaluation' / 'evaluation-sop.md'}

boundary:
- code-role is local workflow assistance, not product runtime or release content
- one primary professional artifact carries each role result; short returns are transport summaries
- delivery KRs are user, business, product, or runtime outcomes; process artifacts are methods or evidence
- Workflow Orchestrator owns complete MKRs, Product / PRD owns complete PKRs, and Implementer owns EKR decomposition
- Test Evaluator cannot start before a complete runnable candidate exists
- target-project Git follows its normal process
"""


def render_workflow_state(config: Config) -> str:
    return f"""# Workflow State / 当前交付状态

project: {config.project_name}
active_milestone: {config.initial_milestone}
objective_accepted: 0
objective: unconfirmed
delivery_stage: milestone_definition
milestone_okr_accepted: 0
product_okr_accepted: 0
candidate_ready_for_independent_evaluation: 0
evaluation_executed: 0
current_evidence_owner: user
current_stage_assignment: none
accepted_product_okr_artifact: none
accepted_architecture_artifact: none
accepted_code_context_artifact: none
accepted_engineering_artifact: none
runnable_candidate_artifact: none
latest_independent_evidence: none
current_iteration: 0
iteration_limit: 3
milestone_pass: 0

pending_human_decision: accept one complete Objective and two to five MKRs

rules:
- record current accepted state only; do not append chronological workflow history
- preserve complete global contracts and mandatory stage order
- do not store Implementer EKR detail in Orchestrator state
- packet status, manifest readiness, and locks do not control routine routing
- only complete independent outcome evidence can change an MKR from 0 to 1
"""


def render_milestone_contract(config: Config) -> str:
    return f"""# Milestone Contract / 里程碑合同

milestone: {config.initial_milestone}
objective: unconfirmed
objective_accepted: 0

milestone_key_results:
| MKR | Observable outcome | Subject and scenario | Binary threshold and conditions | Required independent evidence | Claim boundary | Pass (0/1) |
| --- | --- | --- | --- | --- | --- | ---: |

non_goals:
- unconfirmed

claim_boundary:
- allowed: unconfirmed
- forbidden: unconfirmed

outcome_rule: delivery KRs describe observable user, business, product, or runtime outcomes
method_rule: research, PRD, architecture, evaluation SOP, tests, reports, packets, and reviews are methods or evidence, not delivery KRs
product_okr_required_before_engineering: 1
product_okr_path: none
candidate_required_before_evaluation: 1
runnable_candidate_path: none

evaluation_sop_required_for_evaluation: 1
evaluation_sop_path: {config.workflow / 'evaluation' / 'evaluation-sop.md'}
engineering_to_evaluation_attempt_limit: 3
accepted_time_or_cost_budget: unconfirmed

closure_rule: all accepted MKRs are 1, complete independent evaluation passes, and required review gate passes
"""


def render_evaluation_sop(config: Config) -> str:
    return f"""# Evaluation SOP / 评估 SOP

milestone: {config.initial_milestone}
sop_version: unassigned_until_candidate_ready
sop_confirmed: 0
confirmed_by: none

candidate_gate_required: 1
candidate_ready_for_independent_evaluation: 0
candidate_artifact_path: none

evaluation_subject: unconfirmed
evaluation_objective: unconfirmed
datasets: []
graders: []
environment: []

required_checks:
| Check ID | Expected observation | Command or method | Required evidence | Pass threshold |
| --- | --- | --- | --- | --- |

required_regressions: []
positive_cases: []
negative_cases: []

claim_boundary:
- allowed: unconfirmed
- forbidden: unconfirmed

accepted_time_or_cost_budget: unconfirmed

purpose_rule: this SOP is recorded after candidate readiness and before candidate results are inspected; it is not a delivery KR
binary_rule: evaluation_executed is 1 only when the complete MKR/PKR evaluation ran; milestone_observed_pass is 1 only when every MKR independently passes
sop_change_rule: post-candidate change requires user approval, new SOP version, and affected-evidence rerun
"""


def render_final_packet_index(config: Config) -> str:
    rows = "\n".join(
        f"| {role} | none | 0 | none |" for role in ROLE_CONFIG
    )
    return f"""# Accepted Final Outputs / 已接受最终产出

project: {config.project_name}
milestone: {config.initial_milestone}

This is a pointer table, not a completion gate. Workflow Orchestrator updates it after substantive primary-artifact acceptance.

| Role | Accepted primary artifact | Work-unit pass (0/1) | Evidence note |
| --- | --- | ---: | --- |
{rows}
"""


def render_role_prompt(config: Config, role_id: str) -> str:
    role = ROLE_CONFIG[role_id]
    dialogue = config.code_role / "DIALOGUE-CONTROL.md"
    okr_standard = config.code_role / "OKR-STANDARD.md"
    contract = role["contract"]
    standard = role["output_standard"]
    state = config.workflow / "orchestrator" / "workflow-state.md"
    milestone = config.workflow / "orchestrator" / "milestone-contract.md"
    sop = config.workflow / "evaluation" / "evaluation-sop.md"

    if role_id == "workflow-orchestrator":
        return f"""# {role['name']}

You are the Workflow Orchestrator for `{config.project_name}`.

Read silently on every turn:

- {dialogue}
- {okr_standard}
- {contract}
- {standard}
- {milestone}
- {state}
- {sop}
- accepted primary professional artifacts named by workflow state

Respond to the user's actual request with exactly one OKR proposal, role-specific assignment, artifact decision, consolidated user-decision request, or milestone-closure decision.

Do not send a startup acknowledgement or recovery report. Do not narrate reads or consumption checks. Do not write professional role conclusions. Read primary artifacts directly; return formatting, draft status, and optional locks are not substantive gates. Every professional role returns here, and you advance or repair the current global delivery stage.

Use Chinese by default.
"""

    assignment = config.code_role / "templates" / f"{role_id}-assignment.md"
    result = config.code_role / "templates" / f"{role_id}-return.md"
    return f"""# {role['name']}

You are the `{role_id}` role for `{config.project_name}`.

Read once when configured or refreshed:

- {dialogue}
- {okr_standard}
- {contract}
- {standard}
- {milestone}
- {state}
{f'- {sop}' if role_id in {'test-evaluator', 'reviewer'} else ''}
- assignment template: {assignment}
- return template: {result}

A complete Project Manager assignment starts work immediately. Do not send a startup acknowledgement, repeat read/write/forbidden boundaries, ask for `开始`, or narrate routine progress. Ask one consolidated blocker question only when a substantive user-owned decision is missing.

Write the assignment's one required primary professional artifact and then send the short role-specific return. Optional packet metadata or evidence annexes do not become extra completion gates. Do not recommend or choose the next role. Return to Workflow Orchestrator. The primary artifact carries professional truth; the short return is only a pointer.

Public-source research is allowed when relevant. Explicit approval is required only for authenticated/private resources, paid provider execution outside accepted budget, private-data external transfer, or irreversible external actions.

Use Chinese by default.
"""


def render_state_index(config: Config, role_id: str) -> str:
    return f"""# {role_id} State Index

Status: non-authoritative navigation index

- project: {config.project_name}
- milestone: {config.initial_milestone}
- role prompt: {config.code_role / 'role-instance-prompts' / f'{role_id}.md'}
- workflow state: {config.workflow / 'orchestrator' / 'workflow-state.md'}
- milestone contract: {config.workflow / 'orchestrator' / 'milestone-contract.md'}

Read authoritative files directly before acting. This index cannot update KR or routing state.
"""


def planned_files(config: Config) -> dict[Path, str]:
    files = {
        config.code_role / "README.md": render_project_readme(config),
        config.code_role / "DIALOGUE-CONTROL.md": source_text(ROOT / "docs" / "dialogue-control.md", config),
        config.code_role / "OKR-STANDARD.md": source_text(ROOT / "docs" / "okr-standard.md", config),
        config.code_role / "project-config.md": render_project_config(config),
        config.workflow / "orchestrator" / "workflow-state.md": render_workflow_state(config),
        config.workflow / "orchestrator" / "milestone-contract.md": render_milestone_contract(config),
        config.workflow / "orchestrator" / "final-packet-index.md": render_final_packet_index(config),
        config.workflow / "evaluation" / "evaluation-sop.md": render_evaluation_sop(config),
    }

    for role_id in ROLE_CONFIG:
        files[config.code_role / "role-instance-prompts" / f"{role_id}.md"] = render_role_prompt(config, role_id)

    for role_id in EXECUTION_ROLES:
        role_templates = WORKFLOW_DOCS / "roles" / role_id / "templates"
        files[config.code_role / "templates" / f"{role_id}-assignment.md"] = source_text(role_templates / "assignment.md", config)
        files[config.code_role / "templates" / f"{role_id}-return.md"] = source_text(role_templates / "return.md", config)

    if config.with_state_index:
        files[config.code_role / "state-index" / "README.md"] = "# State Index\n\nStatus: non-authoritative navigation index\n"
        for role_id in ROLE_CONFIG:
            files[config.code_role / "state-index" / "roles" / f"{role_id}.md"] = render_state_index(config, role_id)

    return files


def write_files(config: Config) -> list[Path]:
    durable_state = {
        config.workflow / "orchestrator" / "workflow-state.md",
        config.workflow / "orchestrator" / "milestone-contract.md",
        config.workflow / "orchestrator" / "final-packet-index.md",
        config.workflow / "evaluation" / "evaluation-sop.md",
    }
    changed: list[Path] = []
    for path, content in planned_files(config).items():
        if path.exists() and (path in durable_state or not config.force):
            continue
        if config.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        changed.append(path)
    return changed


def ensure_local_git_exclude(config: Config) -> bool:
    exclude = config.target / ".git" / "info" / "exclude"
    if not exclude.parent.exists():
        return False
    current = exclude.read_text(encoding="utf-8") if exclude.exists() else ""
    if any(line.strip().rstrip("/") == "code-role" for line in current.splitlines()):
        return False
    if config.write:
        suffix = "" if not current or current.endswith("\n") else "\n"
        exclude.write_text(f"{current}{suffix}code-role/\n", encoding="utf-8")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--project-name")
    parser.add_argument("--tracking", default="local-only", choices=["local-only"])
    parser.add_argument("--initial-milestone", default="workflow-bootstrap")
    parser.add_argument("--initial-chain", default="full-chain")
    parser.add_argument("--external-research-allowed", dest="external_research_allowed", action="store_true", default=True)
    parser.add_argument("--no-external-research", dest="external_research_allowed", action="store_false")
    parser.add_argument("--with-state-index", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()
    config = Config(
        target=target,
        project_name=args.project_name or target.name,
        initial_milestone=args.initial_milestone,
        initial_chain=args.initial_chain,
        external_research_allowed=args.external_research_allowed,
        with_state_index=args.with_state_index,
        force=args.force,
        write=args.write,
    )

    files = write_files(config)
    exclude_changed = ensure_local_git_exclude(config)
    action = "created/updated" if config.write else "would create/update"
    for path in files:
        print(f"{action}: {path}")
    if exclude_changed:
        print(f"{action}: {target / '.git' / 'info' / 'exclude'}")
    if not config.write:
        print("dry-run only; rerun with --write to create files")
    if not files and not exclude_changed:
        print("no files changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
