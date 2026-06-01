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
        WORKFLOW / "workflow-chain-policy.md",
        WORKFLOW / "orchestrator" / "consumption-check-request-template.md",
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
    assert "Reviewer must audit the packet chain" in policy


def test_workflow_docs_link_orchestrator_and_policy() -> None:
    readme = read(WORKFLOW / "README.md")
    handoff = read(WORKFLOW / "handoff-protocol.md")
    guide = read(WORKFLOW / "role-configuration-guide.md")
    source_map = read(WORKFLOW / "source-map.md")

    assert "orchestrator/ROLE.md" in readme
    assert "orchestrator/STARTUP.md" in readme
    assert "bootstrap.md" in readme
    assert "workflow-chain-policy.md" in readme
    assert "The user may accept a role's completed output for the next role" in handoff
    assert "Role 1: Workflow Orchestrator" in guide
    assert "Orchestrator Write Scope" in source_map
    assert "consumption-check-request-template.md" in readme


def test_consumption_check_request_template_keeps_routing_with_orchestrator() -> None:
    template = read(WORKFLOW / "orchestrator" / "consumption-check-request-template.md")
    assert "当前完成角色" in template
    assert "handoff manifest" in template
    assert "用户是否接受该角色产出进入下一角色" in template
    assert "严格交接只在用户明确要求时检查" in template
    assert "The current role may recommend a downstream role" in template
    assert "must not generate the authoritative next-role startup message" in template


def test_orchestrator_startup_routine_is_file_based() -> None:
    startup = read(ORCH / "STARTUP.md")
    assert "项目经理，执行 startup routine，恢复当前状态" in startup
    assert "workflow-state.md" in startup
    assert "milestone-registry.md" in startup
    assert "decision-log.md" in startup
    assert "Authoritative packet" in startup
    assert "Do not infer the current packet by scanning for the newest file" in startup
