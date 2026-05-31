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
    assert "allow Implementer to start from a `draft` packet without explicit user approval" in role


def test_chain_policy_defines_allowed_chains_and_gates() -> None:
    policy = read(WORKFLOW / "workflow-chain-policy.md")
    for chain in ["full-chain", "mini-chain", "patch-chain", "docs-only-chain", "research-only"]:
        assert f"`{chain}`" in policy
    assert "Chain Type Matrix" in policy
    assert "`architect -> code-context -> implementer -> test-evaluator -> reviewer`" in policy
    assert "`code-context -> implementer -> test-evaluator -> reviewer`" in policy
    assert "`product-prd or architect -> reviewer`" in policy
    assert "Downstream roles consume only `ready_for_next_role` or `accepted` packets" in policy
    assert "Draft consumption must be recorded" in policy
    assert "consumable_check=fail" in policy
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
    assert "allowing a downstream role to consume a `draft` packet" in handoff
    assert "Role 1: Workflow Orchestrator" in guide
    assert "Orchestrator Write Scope" in source_map


def test_orchestrator_startup_routine_is_file_based() -> None:
    startup = read(ORCH / "STARTUP.md")
    assert "项目经理，执行 startup routine，恢复当前状态" in startup
    assert "workflow-state.md" in startup
    assert "milestone-registry.md" in startup
    assert "decision-log.md" in startup
    assert "Authoritative packet" in startup
    assert "Do not infer the current packet by scanning for the newest file" in startup
