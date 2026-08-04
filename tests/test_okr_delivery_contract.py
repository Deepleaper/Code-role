from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OKR = ROOT / "docs" / "okr-standard.md"
LOOP = ROOT / "docs" / "loop"
WORKFLOW = ROOT / "docs" / "workflow"
EXAMPLE = ROOT / "examples" / "minimal-goal-loop"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_three_okr_layers_have_distinct_owners_and_authority() -> None:
    standard = read(OKR)

    for marker in (
        "Milestone OKR | Project Manager + user",
        "Product OKR | Product Strategy / Product PRD",
        "Engineering Execution KRs | Engineering / Implementer",
        "`MKR-1...MKR-N`",
        "`PKR-1...PKR-N`",
        "`EKR-1...EKR-N`",
        "A passed EKR never implies a passed PKR or MKR",
    ):
        assert marker in standard


def test_project_manager_and_product_work_on_complete_global_contracts() -> None:
    minimal_pm = read(LOOP / "roles" / "project-manager.md")
    minimal_product = read(LOOP / "roles" / "product-strategy.md")
    full_pm = read(WORKFLOW / "orchestrator" / "ROLE.md")
    full_product = read(WORKFLOW / "roles" / "product-prd" / "ROLE.md")

    for text in (minimal_pm, full_pm):
        assert "complete Milestone OKR" in text
        assert "Do not send Product" in text
        assert "one MKR at a time" in text
    for text in (minimal_product, full_product):
        assert "complete Product OKR" in text
        assert "every accepted MKR" in text
        assert "EKR" in text


def test_stage_assignments_preserve_global_scope_and_candidate_gate() -> None:
    product = read(LOOP / "templates" / "product-assignment.md")
    engineering = read(LOOP / "templates" / "engineering-assignment.md")
    evaluation = read(LOOP / "templates" / "evaluation-assignment.md")

    assert "delivery_stage: product_definition" in product
    assert "milestone_okr_scope: all_accepted_mkrs" in product
    assert "role_deliverable: complete_product_okr_and_product_contract" in product

    assert "delivery_stage: engineering_delivery" in engineering
    assert "product_okr_accepted: 1" in engineering
    assert "engineering_objective: produce_the_complete_runnable_candidate" in engineering

    assert "delivery_stage: independent_evaluation" in evaluation
    assert "candidate_ready_for_independent_evaluation: 1" in evaluation
    assert "candidate_artifact_path:" in evaluation
    assert "evaluation_scope: complete_mkr_and_pkr_contract" in evaluation


def test_engineering_alone_decomposes_ekrs_and_cannot_self_pass_mkrs() -> None:
    minimal = read(LOOP / "roles" / "engineering.md")
    full = read(WORKFLOW / "roles" / "implementer" / "ROLE.md")

    for text in (minimal, full):
        assert "`EKR-1...EKR-N`" in text
        assert "partial EKR completion" in text
        assert "cannot pass the Engineering stage" in text
        assert "cannot" in text and "MKR" in text


def test_evaluation_is_post_candidate_and_reports_every_mkr() -> None:
    minimal_role = read(LOOP / "roles" / "independent-evaluation.md")
    full_role = read(WORKFLOW / "roles" / "test-evaluator" / "ROLE.md")
    minimal_return = read(LOOP / "templates" / "evaluation-return.md")
    full_return = read(WORKFLOW / "roles" / "test-evaluator" / "templates" / "return.md")

    for text in (minimal_role, full_role):
        assert "candidate_ready_for_independent_evaluation=1" in text
        assert "complete runnable candidate" in text
        assert "latest diff" in text
    for text in (minimal_return, full_return):
        assert "evaluation_executed: 0 | 1" in text
        assert "mkr_results:" in text
        assert "milestone_observed_pass: 0 | 1" in text
        assert "pass_with_residual_risk" not in text


def test_milestone_board_tracks_global_stage_not_ekr_activity() -> None:
    board = read(LOOP / "templates" / "milestone-board.md")

    for marker in (
        "Delivery stage",
        "Milestone OKR accepted",
        "Product OKR accepted",
            "Candidate ready for independent evaluation",
        "Independent evaluation executed",
        "Accepted Product OKR",
        "Current blocking contract",
    ):
        assert marker in board
    assert "Target KR" not in board
    assert "Current failed evidence" not in board
    assert "Decision Log" not in board
    assert "Do not append process history" in board


def test_full_profile_roles_keep_one_primary_artifact_contract() -> None:
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

        assert "primary" in role.lower() and "artifact" in role.lower()
        assert "required_artifact_path:" in assignment
        assert "artifact_path:" in role_return
        assert "required_packet_path:" not in assignment
        assert "packet_path:" not in role_return


def test_public_walkthrough_proves_product_engineering_evaluation_order() -> None:
    product_assignment = read(EXAMPLE / "01-pm-product-assignment.md")
    product_contract = read(EXAMPLE / "02-product-contract.md")
    engineering_assignment = read(EXAMPLE / "04-pm-engineering-assignment.md")
    engineering_return = read(EXAMPLE / "06-engineering-return.md")
    evaluation_assignment = read(EXAMPLE / "07-pm-evaluation-assignment.md")
    evaluation_return = read(EXAMPLE / "09-independent-evaluation-return.md")
    decision = read(EXAMPLE / "10-pm-decision.md")

    assert "milestone_okr_scope: all_accepted_mkrs" in product_assignment
    assert "PKR-1" in product_contract and "PKR-3" in product_contract
    assert "product_okr_accepted: 1" in engineering_assignment
    assert "candidate_ready_for_independent_evaluation: 1" in engineering_return
    assert "candidate_ready_for_independent_evaluation: 1" in evaluation_assignment
    assert "MKR-1" in evaluation_return and "MKR-2" in evaluation_return
    assert "evaluation_executed: 1" in evaluation_return
    assert "milestone_pass: 1" in decision
