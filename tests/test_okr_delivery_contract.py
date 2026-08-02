from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIALOGUE = ROOT / "docs" / "dialogue-control.md"
LOOP = ROOT / "docs" / "loop"
WORKFLOW = ROOT / "docs" / "workflow"
EXAMPLE = ROOT / "examples" / "minimal-goal-loop"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_delivery_krs_are_outcomes_not_process_artifacts() -> None:
    shared = read(DIALOGUE)
    minimal_pm = read(LOOP / "roles" / "project-manager.md")
    full_pm = read(WORKFLOW / "orchestrator" / "ROLE.md")

    marker = "A delivery KR must describe an observable user, business, product, or runtime outcome."
    forbidden = "Research, PRD, architecture, evaluation SOP, tests, reports, packets, and reviews are delivery methods or evidence, not delivery KRs."

    for text in (shared, minimal_pm, full_pm):
        assert marker in text
        assert forbidden in text


def test_minimal_assignments_start_from_one_failed_kr_evidence_gap() -> None:
    for filename in (
        "product-assignment.md",
        "engineering-assignment.md",
        "evaluation-assignment.md",
    ):
        assignment = read(LOOP / "templates" / filename)
        for marker in (
            "objective:",
            "target_kr:",
            "current_failed_evidence:",
            "role_deliverable:",
            "acceptance_checks:",
            "required_artifact_path:",
        ):
            assert marker in assignment
        assert "role_objective:" not in assignment
        assert "professional_question:" not in assignment
        assert "stop_condition:" not in assignment


def test_engineering_cannot_pass_with_analysis_or_plan_only() -> None:
    minimal = read(LOOP / "roles" / "engineering.md")
    full = read(WORKFLOW / "roles" / "implementer" / "ROLE.md")
    marker = (
        "Analysis, plans, documents, and implementation claims alone cannot pass "
        "a development work unit."
    )

    assert marker in minimal
    assert marker in full


def test_evaluation_reports_work_execution_and_kr_result_as_two_binary_facts() -> None:
    minimal_return = read(LOOP / "templates" / "evaluation-return.md")
    full_return = read(
        WORKFLOW / "roles" / "test-evaluator" / "templates" / "return.md"
    )

    for text in (minimal_return, full_return):
        assert "evaluation_executed: 0 | 1" in text
        assert "kr_observed_pass: 0 | 1" in text
        assert "pass_with_residual_risk" not in text


def test_milestone_board_is_current_control_not_process_history() -> None:
    board = read(LOOP / "templates" / "milestone-board.md")

    assert "Current failed evidence" in board
    assert "Accepted evidence path" in board
    assert "Decision Log" not in board
    assert "Do not append chronological workflow history" in board


def test_full_profile_roles_require_one_primary_professional_artifact() -> None:
    for role_id in (
        "researcher",
        "product-prd",
        "architect",
        "code-context",
        "implementer",
        "test-evaluator",
        "reviewer",
    ):
        role = read(WORKFLOW / "roles" / role_id / "ROLE.md")
        assignment = read(WORKFLOW / "roles" / role_id / "templates" / "assignment.md")
        role_return = read(WORKFLOW / "roles" / role_id / "templates" / "return.md")

        assert "one required primary professional artifact" in role
        assert "required_artifact_path:" in assignment
        assert "artifact_path:" in role_return
        assert "required_packet_path:" not in assignment
        assert "packet_path:" not in role_return


def test_role_prompts_forbid_process_narration_and_next_role_selection() -> None:
    minimal_roles = (
        LOOP / "roles" / "product-strategy.md",
        LOOP / "roles" / "engineering.md",
        LOOP / "roles" / "independent-evaluation.md",
    )
    full_roles = tuple(
        WORKFLOW / "roles" / role_id / "ROLE.md"
        for role_id in (
            "researcher",
            "product-prd",
            "architect",
            "code-context",
            "implementer",
            "test-evaluator",
            "reviewer",
        )
    )

    for path in (*minimal_roles, *full_roles):
        text = read(path)
        assert "Do not narrate routine" in text
        assert "Do not recommend or choose the next role" in text


def test_public_walkthrough_replays_failed_evidence_to_observed_outcome() -> None:
    engineering_assignment = read(EXAMPLE / "01-pm-engineering-assignment.md")
    evaluation_assignment = read(EXAMPLE / "03-pm-evaluation-assignment.md")
    engineering_return = read(EXAMPLE / "02-engineering-return.md")
    evaluation_return = read(EXAMPLE / "04-independent-evaluation-return.md")
    board = read(EXAMPLE / "milestone-board.md")

    for assignment in (engineering_assignment, evaluation_assignment):
        assert "current_failed_evidence:" in assignment
        assert "role_deliverable:" in assignment
        assert "acceptance_checks:" in assignment
        assert "required_artifact_path:" in assignment
        assert "role_objective:" not in assignment
        assert "stop_condition:" not in assignment

    assert "work_unit_pass: 1" in engineering_return
    assert "candidate_ready_for_independent_evaluation: 1" in engineering_return
    assert "evaluation_executed: 1" in evaluation_return
    assert "kr_observed_pass: 1" in evaluation_return
    assert "Current failed evidence" in board
    assert "Decision Log" not in board
