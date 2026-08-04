from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"
ORCH = WORKFLOW / "orchestrator"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_orchestrator_control_files_exist() -> None:
    expected = [
        ORCH / "ROLE.md",
        ORCH / "STARTUP.md",
        ORCH / "workflow-state.md",
        ORCH / "final-packet-index.md",
        WORKFLOW / "evaluation-sop.md",
        WORKFLOW / "milestone-contract.md",
        WORKFLOW / "role-completion-contract.md",
        WORKFLOW / "workflow-chain-policy.md",
        ORCH / "consumption-check-request-template.md",
        ORCH / "project-manager-output-standard.md",
        ORCH / "next-role-message-template.md",
    ]
    assert not [path for path in expected if not path.exists()]


def test_orchestrator_owns_result_control_not_professional_execution() -> None:
    role = read(ORCH / "ROLE.md")
    assert "owns the complete accepted milestone result" in role
    assert "It is not an execution role" in role
    assert "complete Project OKR" in role
    assert "completes one Product Contract" in role
    assert "Implementer alone creates and manages `STEP-1...STEP-N`" in role
    assert "Test Evaluator starts only when" in role
    assert "Read the primary professional artifact and evidence directly" in role
    assert "only you choose the next role" not in role
    assert "Do not write research, product, architecture, code-context, implementation, evaluation, or review conclusions" in role
    assert "Do not create a second Git approval process" in role


def test_chain_names_preserve_mandatory_software_stage_order() -> None:
    policy = read(WORKFLOW / "workflow-chain-policy.md")
    for chain in (
        "full-chain",
        "mini-chain",
        "patch-chain",
        "docs-only-chain",
        "research-only",
    ):
        assert f"`{chain}`" in policy
    assert "Mandatory Stage Order" in policy
    assert "complete Product Contract for every existing `KR-1...KR-N`" in policy
    assert "Test Evaluator must not start before a complete runnable candidate exists" in policy
    assert "Every selected role returns to Workflow Orchestrator" in policy


def test_assignment_acceptance_is_binary_and_artifact_first() -> None:
    contract = read(WORKFLOW / "role-completion-contract.md")
    assert "work_unit_pass = 1" in contract
    assert "work_unit_pass = 0" in contract
    assert "Primary Artifact Is Authoritative" in contract
    assert "Missing return fields" in contract
    assert "Only missing or failed professional checks justify rework" in contract
    assert "evaluation_executed: 0|1" in contract
    assert "one binary result for every `KR-*`" in contract
    assert "milestone_observed_pass: 0|1" in contract
    assert "review_gate_pass: 0|1" in contract


def test_orchestrator_uses_role_specific_assignments_and_short_returns() -> None:
    assignment = read(ORCH / "next-role-message-template.md")
    role_return = read(ORCH / "consumption-check-request-template.md")
    standard = read(ORCH / "project-manager-output-standard.md")

    for role_id in (
        "researcher",
        "product-prd",
        "architect",
        "code-context",
        "implementer",
        "test-evaluator",
        "reviewer",
    ):
        assert f"roles/{role_id}/templates/assignment.md" in assignment
    for field in (
        "milestone:",
        "delivery_stage:",
        "project_okr_path:",
        "role_deliverable:",
        "acceptance_checks:",
        "required_artifact_path:",
    ):
        assert field in assignment
    assert "one complete professional delivery stage" in assignment
    assert "work_unit_pass: 0 | 1" in role_return
    assert "artifact_path:" in role_return
    assert "Do not include a next-role recommendation" in role_return
    assert "Artifact Review" in standard
    assert "Format-only rework is forbidden" in standard


def test_orchestrator_recovers_silently_and_emits_one_decision() -> None:
    startup = read(ORCH / "STARTUP.md")
    assert "silently read" in startup
    assert "Do not send a startup acknowledgement or narrated recovery report" in startup
    assert "exactly one of" in startup
    assert "不要输出恢复过程" in startup


def test_workflow_docs_link_the_active_controls() -> None:
    readme = read(WORKFLOW / "README.md")
    root_readme = read(ROOT / "README.md")
    for link in (
        "orchestrator/ROLE.md",
        "workflow-chain-policy.md",
        "milestone-contract.md",
        "role-completion-contract.md",
        "evaluation-sop.md",
        "project-bootstrap.md",
        "project-practices.md",
    ):
        assert link in readme
    assert "docs/workflow/project-practices.md" in root_readme
    assert "docs/workflow/milestone-contract.md" in root_readme


def test_project_practices_preserve_state_and_allow_public_research() -> None:
    practices = read(WORKFLOW / "project-practices.md")
    for required in (
        "ADR / RFC Style Decisions",
        "Definition Of Done",
        "Claim Ledger",
        "Migration / Upgrade Policy",
        "Policy As Tests",
        "Every role may use public-source network research",
        "Do not overwrite by default",
        "code-role/workflow/orchestrator/workflow-state.md",
    ):
        assert required in practices
