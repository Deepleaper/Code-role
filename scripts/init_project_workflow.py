#!/usr/bin/env python3
"""Initialize the Full Profile eight-role packet workflow scaffold.

Use this profile for complex, high-risk, research-heavy, or audit-intensive
milestones. The script creates navigation and role-start files only. It does
not run role work, create packets for execution roles, stage files, commit,
push, or touch business source files.
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
    with_state_index: bool
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


def role_extra_read_paths(config: BootstrapConfig, role_id: str) -> list[str]:
    common = [
        workflow_doc_path(config, "role-completion-contract.md"),
        str(config.workflow_root / "orchestrator" / "milestone-contract.md"),
    ]
    if role_id == "researcher":
        return common + [workflow_doc_path(config, "roles/researcher/researcher-output-standard.md")]
    if role_id == "product-prd":
        return common + [workflow_doc_path(config, "roles/product-prd/product-prd-output-standard.md")]
    if role_id == "architect":
        return common + [workflow_doc_path(config, "roles/architect/architect-output-standard.md")]
    if role_id == "code-context":
        return common + [workflow_doc_path(config, "roles/code-context/code-context-output-standard.md")]
    if role_id == "implementer":
        return common + [workflow_doc_path(config, "roles/implementer/implementer-output-standard.md")]
    if role_id == "test-evaluator":
        return common + [
            str(config.workflow_root / "evaluation" / "evaluation-sop.md"),
            workflow_doc_path(config, "evaluation-sop.md"),
            workflow_doc_path(config, "roles/test-evaluator/test-evaluator-output-standard.md"),
        ]
    if role_id == "reviewer":
        return common + [
            str(config.workflow_root / "evaluation" / "evaluation-sop.md"),
            workflow_doc_path(config, "roles/reviewer/reviewer-output-standard.md"),
        ]
    return common


ROLE_PROFESSIONAL_STARTUP_CHECKS = {
    "researcher": """researcher_professional_startup_check:
research_objective_understood: 1 | 0
milestone_research_question: <one sentence>
research_deliverable_target: <uncertainty this research must reduce>
expected_gap_categories: architecture_gap | implementation_gap | evidence_gap | evaluation_gap | unknown
downstream_decision_to_reduce: <Product/PRD | Architect | Code Context | Test Evaluator | Reviewer decision>""",
    "product-prd": """product_prd_professional_startup_check:
product_problem_to_define: <one sentence>
target_user_or_operator_to_define: <user/operator>
user_value_to_define: <value>
product_scope_to_define: <scope boundary>
non_goals_to_define: <non-goal boundary>
acceptance_criteria_to_define: <verification target>
architect_handoff_to_define: <what Architect must preserve or decide>""",
    "architect": """architect_professional_startup_check:
architecture_objective_understood: 1 | 0
product_commitment_to_preserve: <product commitment>
contracts_to_define: <contract list or unknown>
boundaries_to_protect: <boundary list or unknown>
code_context_uncertainty_to_reduce: <exact ambiguity>""",
    "code-context": """code_context_professional_startup_check:
code_context_objective_understood: 1 | 0
architecture_contract_to_map: <contract>
implementation_seams_to_identify: file | function | field | test | artifact
implementer_uncertainty_to_reduce: <exact ambiguity>""",
    "implementer": """implementer_professional_startup_check:
implementation_objective_understood: 1 | 0
authorized_product_architecture_context: <target>
authorized_writable_scope_present: 1 | 0
verification_target_present: 1 | 0
test_evaluator_handoff_to_produce: <commands/artifacts/claims>""",
    "test-evaluator": """test_evaluator_professional_startup_check:
evaluation_objective_understood: 1 | 0
milestone_success_criteria_to_evaluate: <criteria>
evaluation_sop_baseline_thresholds_present: 1 | 0
evaluation_mechanism_needs_user_confirmation: 1 | 0
full_independent_evaluation_to_run: <SOP layers, metrics, artifacts, blockers>""",
    "reviewer": """reviewer_professional_startup_check:
review_objective_understood: 1 | 0
original_milestone_anchor_to_audit_against: <anchor>
full_chain_audit_scope_present: 1 | 0
orchestrator_included_in_audit: 1 | 0
closure_decision_not_owned_by_reviewer: 1""",
}


ROLE_COMPLETION_BLOCKS = {
    "researcher": """researcher_completion_template_conformant: 1 | 0
research_objective_answered: 1 | 0
gap_table_complete: 1 | 0
confirmed_unconfirmed_unknown_separated: 1 | 0
downstream_owner_map_complete: 1 | 0
source_log_complete: 1 | 0""",
    "product-prd": """product_prd_completion_template_conformant: 1 | 0
product_problem_defined: 1 | 0
target_user_defined: 1 | 0
user_value_defined: 1 | 0
scope_defined: 1 | 0
non_goals_defined: 1 | 0
acceptance_criteria_binary: 1 | 0
claim_boundary_defined: 1 | 0
architect_handoff_constraints_defined: 1 | 0""",
    "architect": """architect_completion_template_conformant: 1 | 0
product_commitment_preserved: 1 | 0
architecture_contracts_defined: 1 | 0
boundary_map_defined: 1 | 0
state_and_data_flow_defined: 1 | 0
schema_or_artifact_expectations_defined: 1 | 0
risk_register_defined: 1 | 0
code_context_handoff_defined: 1 | 0""",
    "code-context": """code_context_completion_template_conformant: 1 | 0
architecture_contract_mapped: 1 | 0
file_function_field_seams_complete: 1 | 0
artifact_field_map_complete: 1 | 0
test_surface_map_complete: 1 | 0
writable_and_readonly_surfaces_separated: 1 | 0
implementation_contract_defined: 1 | 0
stop_conditions_defined: 1 | 0""",
    "implementer": """implementer_completion_template_conformant: 1 | 0
authorized_scope_respected: 1 | 0
changed_files_exact: 1 | 0
changed_files_mapped_to_requirements: 1 | 0
tests_or_no_test_reason_recorded: 1 | 0
verification_commands_recorded: 1 | 0
runtime_boundary_proof_recorded: 1 | 0
test_evaluator_handoff_complete: 1 | 0""",
    "test-evaluator": """test_evaluator_completion_template_conformant: 1 | 0
evaluation_scope_basis_confirmed: 1 | 0
sop_layers_evaluated_or_marked_not_run: 1 | 0
each_gate_has_metric_expected_observed_evidence: 1 | 0
commands_and_artifacts_recorded: 1 | 0
unsupported_claims_rejected: 1 | 0
binary_route_field_present: 1 | 0
milestone_impact_recorded: 1 | 0""",
    "reviewer": """reviewer_completion_template_conformant: 1 | 0
original_milestone_anchor_audited: 1 | 0
orchestrator_audited: 1 | 0
role_by_role_drift_matrix_complete: 1 | 0
acceptance_gap_checked: 1 | 0
evaluation_sop_baseline_checked: 1 | 0
packet_chain_audited: 1 | 0
final_gate_binary: 1 | 0
return_role_or_closure_discussion_route_defined: 1 | 0""",
}


def role_completion_conformant_field(role_id: str) -> str:
    return f"{role_id.replace('-', '_')}_completion_template_conformant"


def render_professional_objective_section(role_id: str) -> str:
    if role_id == "workflow-orchestrator":
        return """Role-specific professional completion gate / 分角色专业完成门:

When checking a completed role, Orchestrator must require that role's `*_completion_template_conformant=1`. Missing or `0` means the output is not consumable, even if files exist and manifest JSON is valid.

检查角色产出时，项目经理必须要求对应角色的 `*_completion_template_conformant=1`。缺失或为 `0` 时，即使文件存在、manifest 合法，也不可消费。

```text
researcher requires researcher_completion_template_conformant=1
product-prd requires product_prd_completion_template_conformant=1
architect requires architect_completion_template_conformant=1
code-context requires code_context_completion_template_conformant=1
implementer requires implementer_completion_template_conformant=1
test-evaluator requires test_evaluator_completion_template_conformant=1
reviewer requires reviewer_completion_template_conformant=1
```

Professional fields must be checked before process fields. A role output fails if it mostly reports read/write/forbidden scope but does not prove its professional completion fields.

必须先检查专业字段，再检查流程字段。如果角色主要汇报读取/写入/禁止范围，却没有证明专业完成字段，则产出失败.
"""
    return """Professional objective first / 专业目标优先:

- Your first response must start from this role's professional objective for the current milestone, before read/write/forbidden scope. / 首次回复必须先确认本角色对当前 milestone 的专业目标，再写读取、写入和禁止范围。
- Process boundaries are required, but they are not the main deliverable. / 流程边界必须写，但不是本角色主交付。
- If the professional objective is unclear, set `assignment_issue_detected=1`, set packet/formal execution permission to `0`, and ask for the missing milestone/product/evidence fields. / 如果专业目标不清楚，标记任务问题，禁止写 packet/正式执行，并索要缺失字段。
"""


def render_first_response_section(role_id: str) -> str:
    if role_id == "workflow-orchestrator":
        return """First response / 首次回复:

1. Confirm this conversation is the `workflow-orchestrator` role. / 确认本对话是 `workflow-orchestrator` 角色。
2. State `role_activation_status=active`. / 明确写出 `role_activation_status=active`。
3. State which Orchestrator state, milestone, index, and upstream packet files you will read. / 说明将读取哪些 Orchestrator 状态、milestone、索引和上游 packet 文件。
4. State what Orchestrator state files you may update, if any. / 说明可能更新哪些 Orchestrator 状态文件，如有。
5. State forbidden scope. / 说明禁止范围。
6. For role routing, state the role's milestone target, completion definition, required output, and exact next-role message source. / 如果要路由角色，说明该角色的 milestone 目标、完成定义、所需产出和精确下一角色消息来源。
7. Wait for user confirmation before writing Orchestrator state. / 等用户确认后再写 Orchestrator 状态。
"""

    return f"""First response / 首次回复:

1. Confirm this conversation is the `{role_id}` role. / 确认本对话是 `{role_id}` 角色。
2. State `role_activation_status=active`. / 明确写出 `role_activation_status=active`。
3. State the professional startup check first: / 先写专业启动检查：

```text
{ROLE_PROFESSIONAL_STARTUP_CHECKS[role_id]}
```
4. State `assignment_issue_detected=0|1` and list missing or conflicting task fields. / 明确写出任务问题和缺失字段。
5. State `packet_write_allowed=1|0` for packet creation/write execution. / 明确写出是否允许写 packet。
6. State exact read scope. / 说明精确读取范围。
7. State exact write scope, if any. / 说明精确写入范围。
8. State forbidden scope. / 说明禁止范围。
9. State blockers or questions, if any; blockers do not cancel role activation. / 如有 blocker 或问题，明确列出。
10. Wait for user confirmation before writing. / 等用户确认后再写入。
"""


def render_completion_response_section(role_id: str, config: BootstrapConfig) -> str:
    if role_id == "workflow-orchestrator":
        return ""
    return f"""Completion response / 完成回复:

The final response after writing the packet must include this structured block before the Orchestrator check request. Free-form summaries cannot replace it.

写完 packet 后的最终回复必须先包含本结构化块，再附 Orchestrator 检查请求；自由文本总结不能替代。

```text
{ROLE_COMPLETION_BLOCKS[role_id]}
role_completion_status: 1 | 0
assigned_completion_conditions_total: <integer>
assigned_completion_conditions_met: <integer>
unmet_completion_conditions: none | <condition ids>
completion_evidence:
- condition_id: <id>
  evidence: <file path | artifact path | command/result | source reference | explicit inspected field>
forbidden_completion_claim_used: true | false
orchestrator_next_check_request: <copy-ready lightweight consumption check summary from {workflow_doc_path(config, "orchestrator/consumption-check-request-template.md")}>
```

If any required professional field is missing, set `{role_completion_conformant_field(role_id)}=0`, set `role_completion_status=0`, list the missing fields, and do not recommend route-forward as a completed handoff.

如果缺少任一专业字段，必须把 `{role_completion_conformant_field(role_id)}` 置为 `0`，`role_completion_status=0`，列出缺失字段，不得建议完成态路由。
"""


def render_project_readme(config: BootstrapConfig) -> str:
    return f"""# Code-role Full Profile Project Configuration

This directory configures the eight-role Code-role Full Profile for `{config.project_name}`.

This folder is local-only workflow assistance. It is not product runtime content, is not part of the target project's delivery, and should not be committed or pushed with the target project.

## Authoritative Sources

- `workflow/orchestrator/workflow-state.md`
- `workflow/orchestrator/milestone-registry.md`
- `workflow/orchestrator/decision-log.md`
- `workflow/orchestrator/final-packet-index.md`
- `workflow/orchestrator/milestone-contract.md`
- `workflow/evaluation/evaluation-sop.md`
- Code-role `docs/workflow/role-completion-contract.md`
- role packet `handoff.manifest.json` files
- strict handoff `packet.lock.json` files, only when explicitly requested

`state-index/` is optional non-authoritative navigation. It is generated only with `--with-state-index`.

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
control_profile: full-eight-role
tracking_policy: {config.tracking}
external_research_allowed_default: {external}

## Boundary

- `code-role/` is local-only workflow assistance, not product runtime content.
- `code-role/` should not be committed or pushed with this target project.
- `code-role/state-index/` is optional non-authoritative navigation when generated.
- Orchestrator state and packet manifests remain authoritative. Packet locks are authoritative only in strict handoff mode.
- `workflow/orchestrator/milestone-contract.md` is the hard goal anchor for the active milestone.
- Code-role `docs/workflow/role-completion-contract.md` defines the binary role completion gate.
- `workflow/evaluation/evaluation-sop.md` is the hard evaluation anchor for Test Evaluator and Reviewer.
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


def render_milestone_contract(config: BootstrapConfig) -> str:
    return f"""# Milestone Contract

status: draft
confirmed_by: unknown
confirmed_at: unknown

milestone_name:
{config.initial_milestone}

business_goal:
unknown

delivery_goal:
unknown

success_criteria:
- unknown

role_completion_conditions:
- id: unknown
  role: unknown
  required: true
  condition: unknown
  evidence_required: unknown

non_goals:
- unknown

in_scope:
- unknown

out_of_scope:
- unknown

hard_prohibitions:
- No execution role may start until this contract is confirmed by the user.
- Do not change the milestone goal silently.
- Do not route forward when role output drifts from this contract.

required_roles:
- workflow-orchestrator
- researcher: unknown
- product-prd: unknown
- architect: unknown
- code-context: unknown
- implementer: unknown
- test-evaluator: unknown
- reviewer: unknown

allowed_chain:
{config.initial_chain}

evidence_requirements:
- Each role completion summary must include `role_completion_status`.
- `role_completion_status=1` is valid only when all assigned completion conditions are met with concrete evidence.
- If any assigned condition is missing, unverifiable, or only qualitatively described, `role_completion_status` must be `0`.
- Orchestrator must check this contract before packet structure or routing convenience.

drift_detection_questions:
- Does this output answer the milestone business goal?
- Are all assigned role completion conditions met with concrete evidence?
- Is `role_completion_status` exactly `1` or `0`?
- Is `assigned_completion_conditions_met` equal to `assigned_completion_conditions_total`?
- Is `unmet_completion_conditions` equal to `none`?
- Did it introduce any out-of-scope claim?
- Did it touch any hard prohibition?
- Did it use forbidden completion language such as "mostly complete", "closer to completion", or "pass_with_residual_risk" as completion?

correction_policy:
- If role output drifts: return to the same role for revision.
- If the milestone itself should change: ask the user to revise this contract first.
- If evidence is missing: return to the role responsible for that evidence.
- If scope is unclear: hold routing.

closure_rule:
Reviewer may recommend closure only after final role outputs align with this contract, required evidence is present, and the user accepts residual risk or confirms final acceptance.
"""


def render_evaluation_sop(config: BootstrapConfig) -> str:
    return f"""# Evaluation SOP

status: draft
confirmed_by: unknown
confirmed_at: unknown
milestone: {config.initial_milestone}

evaluation_subject:
unknown

evaluation_objective:
unknown

required_layers:
- evaluation_baseline
- evidence_integrity
- acceptance_mapping
- independent_evaluation
- regression_and_risk
- claim_boundary
- final_quality_gate
- sop_calibration

baseline_sources:
- user_confirmed_baseline: unknown
- product_acceptance: unknown
- architecture_test_strategy: unknown
- code_context_test_map: unknown
- industry_or_benchmark_reference: unknown

metrics:
- unknown: unknown

thresholds:
- unknown: unknown

commands_or_checks:
- unknown: blocked

artifact_requirements:
- unknown

not_run_policy:
- Required checks marked `not_run` block unconditional pass.
- Optional checks marked `not_run` must be listed as residual risk or not applicable.
- Implementer-reported verification is input only; it is not final evaluation evidence.

claim_boundary:
- allowed_claims:
  - unknown
- forbidden_claims:
  - production-ready unless explicitly proven and approved
  - release-ready unless explicitly proven and approved
  - benchmark-leading unless benchmark evidence exists
  - business-complete unless business acceptance evidence exists
- unknown_claims:
  - unknown

final_acceptance_rule:
`final_acceptance=true` may be recommended only when the SOP is confirmed, required evidence is sufficient, required checks are not `not_run`, no unresolved P0/P1 remains, and claim boundaries are respected.

sop_calibration_rule:
- After evaluation, state whether this SOP remains valid.
- Record every SOP change in the Test Evaluator packet.
- Do not silently change evaluation standards between packets.
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


def render_final_packet_index(config: BootstrapConfig) -> str:
    return f"""# Final Packet Index

This file records the current final packet for each role in `{config.project_name}`.

The Orchestrator owns this file. Reviewer uses it as the authoritative index for final-version milestone drift audit.

It is not a history log. A role output may become the current final output only when `role_completion_status=1` and the user accepts it for this milestone.

## Current Milestone Anchor

| Field | Value |
| --- | --- |
| Milestone | {config.initial_milestone} |
| Original business goal | unknown |
| Original delivery goal | unknown |
| Success criteria | unknown |
| Non-goals | unknown |
| Anchor source | unknown |

## Final Role Outputs

| Role | Current final output | Status | Accepted for milestone audit | Notes |
| --- | --- | --- | --- | --- |
| workflow-orchestrator | workflow-state.md, milestone-registry.md, decision-log.md, final-packet-index.md | initialized | yes | Orchestrator output is audited by Reviewer for milestone drift. |
| researcher | none | not_started | no | Update after user accepts Researcher final packet. |
| product-prd | none | not_started | no | Update after user accepts Product / PRD final packet. |
| architect | none | not_started | no | Update after user accepts Architect final packet. |
| code-context | none | not_started | no | Update after user accepts Code Context final packet. |
| implementer | none | not_started | no | Update after user accepts Implementer final packet. |
| test-evaluator | none | not_started | no | Update after user accepts Test Evaluator final packet. |
| reviewer | none | not_started | no | Reviewer fills current packet during final audit. |

## Update Rule

- Update this file only after `role_completion_status=1` and the user accepts a role output as the current final version for this milestone.
- Do not list every historical packet version here.
- Do not scan for newest files to infer final versions.
- If a role output is revised, point the role row to the new accepted packet.
- If a role is skipped by chain type, set status to `not_applicable` and explain why in Notes.
"""


def render_role_prompt(config: BootstrapConfig, role_id: str) -> str:
    index_path = config.project_config_root / "state-index" / "roles" / f"{role_id}.md"
    state_index_read = f"- {index_path}\n" if config.with_state_index else ""
    if role_id == "workflow-orchestrator":
        role_name = "workflow-orchestrator"
        output_boundary = "Only update Orchestrator state files after user-confirmed routing decisions. / 只在用户确认路由决策后更新 Orchestrator 状态文件。"
        upstream = "none unless explicitly provided"
        orchestrator_reads = (
            f"- {workflow_doc_path(config, 'orchestrator/project-manager-output-standard.md')}\n"
            f"- {workflow_doc_path(config, 'orchestrator/next-role-message-template.md')}\n"
            f"- {config.workflow_root / 'orchestrator' / 'final-packet-index.md'}\n"
        )
    else:
        role_name = role_id
        output_boundary = f"Only write this role's packet under `code-role/workflow/roles/{role_id}/reports/<milestone>/packet-vNNN/`. / 只把本角色 packet 写入该路径。"
        upstream = "<paste exact upstream handoff.manifest.json path>"
        orchestrator_reads = ""
    extra_reads = "\n".join(f"- {path}" for path in role_extra_read_paths(config, role_id))

    return f"""# Start {role_name} / 启动 {role_name}

You are the `{role_name}` role for `{config.project_name}`.
你是 `{config.project_name}` 项目的 `{role_name}` 角色。

Read first / 请先读取:

- {workflow_doc_path(config, "README.md")}
- {workflow_doc_path(config, "discussion-first-protocol.md")}
- {workflow_doc_path(config, "role-instance-setup.md")}
- {workflow_doc_path(config, "handoff-protocol.md")}
- {workflow_doc_path(config, "packet-schema.md")}
- {workflow_doc_path(config, "source-map.md")}
- {role_contract_path(config, role_id)}
{orchestrator_reads.rstrip()}
{extra_reads}
{state_index_read.rstrip()}

Target project / 目标项目:

```text
{config.target}
```

Current upstream input / 当前上游输入:

```text
{upstream}
```

Rules / 规则:

- Do not switch roles inside this conversation. / 不要在本对话中切换角色。
- Confirm read and write boundaries before creating output. / 创建产出前先确认读取和写入边界。
- {output_boundary}
- Do not modify upstream packets. / 不修改上游 packets。
- Network research is allowed by default for public sources when relevant to the milestone. In the first response, state the network purpose and source types you may use. / 默认允许为当前 milestone 使用公开来源联网研究；首次回复需说明联网目的和可能使用的来源类型。
- Do not call real provider APIs, access authenticated/private resources, download or execute remote content, or send secrets/project-private data externally unless the user separately approves that exact action. / 未经用户单独批准，不调用真实 provider API、不访问需认证或私有资源、不下载或执行远程内容、不向外部发送秘密或项目私有数据。
- Do not run `git add`, `git commit`, or `git push`. / 不执行 `git add`、`git commit` 或 `git push`。
- Do not mark a draft packet `ready_for_next_role` unless the user explicitly requests strict handoff. / 除非用户明确要求严格交接，不把 draft packet 标记为 `ready_for_next_role`。
- Completion status is binary. Include `role_completion_status=1` only when every assigned completion condition has concrete evidence; otherwise use `role_completion_status=0`. / 完成状态是二值。只有每个指定完成条件都有具体证据时才写 `role_completion_status=1`；否则写 `role_completion_status=0`。
- When you finish a packet, end the same completion response with the copy-ready short Orchestrator consumption-check summary from `{workflow_doc_path(config, "orchestrator/consumption-check-request-template.md")}`. / 完成 packet 后，在同一条完成回复末尾追加该模板中的可复制短版 Orchestrator 消费检查摘要，供用户发回项目经理。
- You may recommend a downstream role, but you must not generate the authoritative next-role startup message. Orchestrator owns consumable checks, chain routing, and next-role startup message generation. / 你可以建议下游角色，但不能生成权威的下一角色启动消息；Orchestrator 负责消费检查、链路路由和下一角色启动消息。

Milestone alignment rule / 里程碑对齐规则:

- Keep this role focused on the current milestone output. / 保持本角色聚焦当前 milestone 产出。
- Completion reports must include condition count, met count, unmet conditions, concrete evidence, and forbidden completion language flag. / 完成汇报必须包含条件总数、满足数、未满足项、具体证据和禁用完成表述标记。
- If `role_completion_status=0`, do not recommend starting the next role as a completed handoff. / 如果 `role_completion_status=0`，不要建议把它作为完成态交接给下一角色。

{render_professional_objective_section(role_id).rstrip()}

{render_first_response_section(role_id).rstrip()}

{render_completion_response_section(role_id, config).rstrip()}
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
    extra_reads = "\n".join(f"- `{path}`" for path in role_extra_read_paths(config, role_id))
    return f"""# Role State Index: {role_id}

This optional file is a non-authoritative navigation index. It helps this role start faster, but it does not replace ROLE.md, Orchestrator state, or handoff manifests.

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
{extra_reads}
- `{config.workflow_root / "orchestrator" / "workflow-state.md"}`
- `{config.workflow_root / "orchestrator" / "milestone-registry.md"}`
- `{config.workflow_root / "orchestrator" / "decision-log.md"}`
- `{config.workflow_root / "orchestrator" / "final-packet-index.md"}`

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
- Final packet index under `{config.workflow_root / "orchestrator" / "final-packet-index.md"}`
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
        config.workflow_root / "orchestrator" / "final-packet-index.md": render_final_packet_index(config),
        config.workflow_root / "orchestrator" / "milestone-contract.md": render_milestone_contract(config),
        config.workflow_root / "evaluation" / "evaluation-sop.md": render_evaluation_sop(config),
    }
    for role_id in ROLE_IDS:
        files[root / "role-instance-prompts" / f"{role_id}.md"] = render_role_prompt(config, role_id)
    if config.with_state_index:
        files[root / "state-index" / "README.md"] = render_state_index_readme(config)
        files[root / "state-index" / "current-workflow-index.md"] = render_current_workflow_index(config)
        for role_id in ROLE_IDS:
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
    parser.add_argument(
        "--external-research-allowed",
        dest="external_research_allowed",
        action="store_true",
        default=True,
        help="Allow public-source network research in generated role prompts. This is the default.",
    )
    parser.add_argument(
        "--no-external-research",
        dest="external_research_allowed",
        action="store_false",
        help="Disable public-source network research by default for this target project.",
    )
    parser.add_argument("--with-state-index", action="store_true", help="Also generate optional non-authoritative state-index navigation files.")
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
        with_state_index=args.with_state_index,
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
