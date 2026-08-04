import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIALOGUE = ROOT / "docs" / "dialogue-control.md"
LOOP = ROOT / "docs" / "loop"
WORKFLOW = ROOT / "docs" / "workflow"
FULL_ROLES = (
    "researcher",
    "product-prd",
    "architect",
    "code-context",
    "implementer",
    "test-evaluator",
    "reviewer",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_historical_failure_artifact_passes_even_when_chat_return_is_imperfect() -> None:
    shared = read(DIALOGUE)
    minimal_pm = read(LOOP / "roles" / "project-manager.md")
    full_pm = read(WORKFLOW / "orchestrator" / "ROLE.md")

    assert "A missing or imperfect chat return is not a substantive blocker" in shared
    assert "Missing return fields or field order are not blockers" in minimal_pm
    assert "Return formatting, draft status" in full_pm
    assert "format-only rework: `0`" in shared


def test_historical_failure_evaluator_failure_evidence_is_routed_by_substance() -> None:
    shared = read(DIALOGUE)
    full_contract = read(WORKFLOW / "role-completion-contract.md")
    evaluator_return = read(
        WORKFLOW / "roles" / "test-evaluator" / "templates" / "return.md"
    )

    assert "accept the failure evidence and route the substantive blocker owner" in shared
    assert "An incomplete stage returns to the substantive contract owner" in full_contract
    assert "failed_contract_owner:" in evaluator_return
    assert "return_to: workflow-orchestrator" in evaluator_return


def test_historical_failure_missing_prerequisites_are_collected_once_before_assignment() -> None:
    shared = read(DIALOGUE)
    minimal_pm = read(LOOP / "roles" / "project-manager.md")
    full_pm = read(WORKFLOW / "orchestrator" / "project-manager-output-standard.md")

    assert "ask once for the complete decision set" in shared
    assert "ask for all missing decisions once" in minimal_pm
    assert "ask once for the full missing decision set" in full_pm


def test_historical_failure_complete_assignment_does_not_create_startup_turn() -> None:
    shared = read(DIALOGUE)
    assert "startup acknowledgement messages: `0`" in shared
    assert "process-narration messages: `0`" in shared

    for role_id in FULL_ROLES:
        role = read(WORKFLOW / "roles" / role_id / "ROLE.md")
        assert "A complete assignment starts" in role
        assert "Do not send a startup acknowledgement" in role
        assert "ask for `开始`" in role


def test_historical_failure_post_candidate_sop_change_invalidates_evidence() -> None:
    shared = read(DIALOGUE)
    minimal_evaluator = read(LOOP / "roles" / "independent-evaluation.md")
    full_evaluator = read(WORKFLOW / "roles" / "test-evaluator" / "ROLE.md")

    required = ("explicit user approval", "new SOP version", "rerun")
    for text in (shared, minimal_evaluator, full_evaluator):
        for marker in required:
            assert marker in text


def test_historical_failure_orchestrator_emits_one_decision_not_read_logs() -> None:
    shared = read(DIALOGUE)
    startup = read(WORKFLOW / "orchestrator" / "STARTUP.md")
    standard = read(WORKFLOW / "orchestrator" / "project-manager-output-standard.md")

    assert "emit one final decision, not narrated progress checkpoints" in shared
    assert "silently read" in startup
    assert "exactly one of" in startup
    assert "Routine recovery, file reads, packet checks, and state updates are internal work" in standard


def test_both_profiles_forbid_role_self_routing() -> None:
    for name in ("product-return.md", "engineering-return.md", "evaluation-return.md"):
        role_return = read(LOOP / "templates" / name)
        assert "return_to: project-manager" in role_return
        assert "next_role" not in role_return

    for role_id in FULL_ROLES:
        role_return = read(WORKFLOW / "roles" / role_id / "templates" / "return.md")
        manifest = json.loads(
            read(WORKFLOW / "roles" / role_id / "templates" / "handoff.manifest.json")
        )
        assert "return_to: workflow-orchestrator" in role_return
        assert manifest["return_to"] == "workflow-orchestrator"
        assert "handoff_to" not in manifest


def test_evaluation_and_review_gates_are_binary_in_both_profiles() -> None:
    minimal_evaluation = read(LOOP / "templates" / "evaluation-return.md")
    full_evaluation = json.loads(
        read(WORKFLOW / "roles" / "test-evaluator" / "templates" / "handoff.manifest.json")
    )
    full_review = json.loads(
        read(WORKFLOW / "roles" / "reviewer" / "templates" / "handoff.manifest.json")
    )

    assert "evaluation_executed: 0 | 1" in minimal_evaluation
    assert "mkr_results:" in minimal_evaluation
    assert "milestone_observed_pass: 0 | 1" in minimal_evaluation
    assert full_evaluation["quality_gate"]["allowed_values"] == [0, 1]
    assert full_review["quality_gate"]["allowed_values"] == [0, 1]
    assert "final_acceptance" not in full_review["quality_gate"]
