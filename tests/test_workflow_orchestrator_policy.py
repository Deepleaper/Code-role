from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"
ORCH = WORKFLOW / "orchestrator"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_orchestrator_files_exist() -> None:
    expected = [
        ORCH / "ROLE.md",
        ORCH / "STARTUP.md",
        ORCH / "workflow-state.md",
        ORCH / "milestone-registry.md",
        ORCH / "decision-log.md",
        ORCH / "final-packet-index.md",
        WORKFLOW / "evaluation-sop.md",
        WORKFLOW / "milestone-contract.md",
        WORKFLOW / "workflow-chain-policy.md",
        WORKFLOW / "orchestrator" / "consumption-check-request-template.md",
        WORKFLOW / "orchestrator" / "project-manager-output-standard.md",
        WORKFLOW / "orchestrator" / "next-role-message-template.md",
    ]
    missing = [path for path in expected if not path.exists()]
    assert not missing


def test_orchestrator_is_process_control_not_execution_role() -> None:
    role = read(ORCH / "ROLE.md")
    assert "workflow control plane" in role
    assert "not part of the execution packet chain" in role
    assert "must not:" in role
    assert "write PRD" in role
    assert "write code" in role
    assert "write tests" in role
    assert "does not produce `packet-vNNN` outputs" in role
    assert "consumable_check=pass" in role
    assert "consumable_check=fail" in role
    assert "项目经理，执行 startup routine，恢复当前状态" in role
    assert "must not infer the current packet by scanning for the newest file" in role
    assert "mark a role packet `ready_for_next_role` without user confirmation" in role
    assert "allow Implementer to start without explicit user approval and exact writable scope" in role
    assert "primary project-manager check is milestone alignment" in role
    assert "role output drifts from the milestone" in role
    assert "Project Manager Output Standard" in role
    assert "final packet index" in role
    assert "milestone-contract.md" in role
    assert "milestone_contract_check=fail" in role


def test_chain_policy_defines_allowed_chains_and_gates() -> None:
    policy = read(WORKFLOW / "workflow-chain-policy.md")
    for chain in ["full-chain", "mini-chain", "patch-chain", "docs-only-chain", "research-only"]:
        assert f"`{chain}`" in policy
    assert "Chain Type Matrix" in policy
    assert "`architect -> code-context -> implementer -> test-evaluator -> reviewer`" in policy
    assert "`code-context -> implementer -> test-evaluator -> reviewer`" in policy
    assert "`product-prd or architect -> reviewer`" in policy
    assert "Architect must not hand off directly to Test Evaluator" in policy
    assert "Architecture packets first go to Code Context / Context Engineer" in policy
    assert "Downstream roles may consume the current role's completed output after the user accepts it" in policy
    assert "Do not route a role back for readiness conversion by default" in policy
    assert "Strict handoff" in policy
    assert "Implementer must not begin work from chat-only instruction" in policy
    assert "Reviewer must audit the full workflow against the original milestone" in policy
    assert "Orchestrator `final-packet-index.md` exists" in policy
    assert "Reviewer identifies `correction_owner`" in policy


def test_workflow_docs_link_orchestrator_and_policy() -> None:
    readme = read(WORKFLOW / "README.md")
    root_readme = read(ROOT / "README.md")
    handoff = read(WORKFLOW / "handoff-protocol.md")
    guide = read(WORKFLOW / "role-configuration-guide.md")
    source_map = read(WORKFLOW / "source-map.md")

    assert "orchestrator/ROLE.md" in readme
    assert "orchestrator/STARTUP.md" in readme
    assert "bootstrap.md" in readme
    assert "workflow-chain-policy.md" in readme
    assert "milestone-contract.md" in readme
    assert "evaluation-sop.md" in readme
    assert "The user may accept a role's completed output for the next role" in handoff
    assert "Role 1: Workflow Orchestrator" in guide
    assert "Orchestrator Write Scope" in source_map
    assert "consumption-check-request-template.md" in readme
    assert "project-practices.md" in readme
    assert "docs/workflow/project-practices.md" in root_readme
    assert "docs/workflow/milestone-contract.md" in root_readme
    assert "docs/workflow/evaluation-sop.md" in root_readme


def test_project_practices_document_defines_adopted_practices() -> None:
    practices = read(WORKFLOW / "project-practices.md")
    for required in [
        "ADR / RFC Style Decisions",
        "Definition Of Done",
        "Claim Ledger",
        "Golden Path Example",
        "Migration / Upgrade Policy",
        "Policy As Tests",
        "Release Boundary",
        "Network Research Boundary",
        "Practices Not Adopted",
        "Every role may use public-source network research",
        "Do not overwrite by default",
        "code-role/",
    ]:
        assert required in practices


def test_consumption_check_request_template_keeps_routing_with_orchestrator() -> None:
    template = read(WORKFLOW / "orchestrator" / "consumption-check-request-template.md")
    assert "轻量消费检查摘要" in template
    assert "lightweight consumption check" in template
    assert "completed_role" in template
    assert "handoff manifest" in template
    assert "milestone_alignment" in template
    assert "possible_drift" in template
    assert "recommended_routing" in template
    assert "same completion response" in template
    assert "copy-ready next-role startup message" in template
    assert "该产出是否仍服务当前 milestone" in template
    assert "不检查 ready_for_next_role / packet.lock.json / sha256" in template
    assert "The current role may recommend a downstream role" in template
    assert "must not generate the authoritative next-role startup message" in template
    assert "milestone-contract.md" in template
    assert "success_criteria_covered" in template
    assert "non_goals_or_hard_prohibitions_touched" in template


def test_next_role_message_template_focuses_on_milestone_not_process() -> None:
    template = read(WORKFLOW / "orchestrator" / "next-role-message-template.md")
    assert "下一角色交接模板" in template
    assert "This message is a milestone handoff brief, not a workflow tutorial" in template
    assert "Professional content comes from the upstream packet" in template
    assert "本 milestone 的业务目标" in template
    assert "Milestone business goal" in template
    assert "milestone contract" in template
    assert "Hard prohibitions" in template
    assert "项目经理审阅结论" in template
    assert "Project Manager Review Result" in template
    assert "你需要自己从上游 packet 中提取本角色应回答的专业问题" in template
    assert "milestone 对齐要求" in template
    assert "Milestone Alignment Requirement" in template
    assert "是否存在目标漂移" in template
    assert "Keep the role focused on milestone output, not process control" in template
    assert "Do not let Orchestrator write professional questions" in template
    assert "Do not include readiness conversion instructions unless the user requested strict handoff" in template
    assert "paste this copy-ready message directly" in template
    assert "Do not only write \"recommended next role\"" in template


def test_project_manager_output_standard_defines_professional_outputs() -> None:
    standard = read(WORKFLOW / "orchestrator" / "project-manager-output-standard.md")
    assert "项目经理输出规范" in standard
    assert "Core Quality Bar" in standard
    assert "核心质量标准" in standard
    assert "Workflow State Summary" in standard
    assert "流程状态摘要" in standard
    assert "Consumption Check Result" in standard
    assert "消费检查结果" in standard
    assert "Next Role Handoff Brief" in standard
    assert "下一角色交接 brief" in standard
    assert "Blocker / Confirmation Request" in standard
    assert "阻塞或确认请求" in standard
    assert "Decision Log Entry" in standard
    assert "决策日志条目" in standard
    assert "Final Packet Index" in standard
    assert "final-packet-index.md" in standard
    assert "milestone-contract.md" in standard
    assert "Drift Review Standard" in standard
    assert "目标漂移审查标准" in standard
    assert "milestone_drift: detected" in standard
    assert "The handoff brief is not a workflow tutorial" in standard
    assert "交接 brief 不是 workflow 教程" in standard
    assert "The Orchestrator does not redefine the next role's professional questions" in standard
    assert "include the copy-ready next-role startup message directly" in standard
    assert "Do not only output a next-role recommendation without copy-ready text" in standard


def test_orchestrator_startup_routine_is_file_based() -> None:
    startup = read(ORCH / "STARTUP.md")
    assert "项目经理，执行 startup routine，恢复当前状态" in startup
    assert "workflow-state.md" in startup
    assert "milestone-registry.md" in startup
    assert "decision-log.md" in startup
    assert "final-packet-index.md" in startup
    assert "Authoritative packet" in startup
    assert "Do not infer the current packet by scanning for the newest file" in startup
