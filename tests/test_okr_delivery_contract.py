from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OKR = ROOT / "docs" / "okr-standard.md"
LOOP = ROOT / "docs" / "loop"
WORKFLOW = ROOT / "docs" / "workflow"
EXAMPLE = ROOT / "examples" / "minimal-goal-loop"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_one_project_okr_has_distinct_delivery_responsibilities() -> None:
    standard = read(OKR)

    for marker in (
        "One milestone has exactly one Project OKR",
        "Define and govern the Project OKR | Project Manager + user",
        "Make every KR product-complete | Product Strategy / Product PRD",
        "Build the complete candidate | Engineering / Implementer",
        "`KR-1...KR-N`",
        "`STEP-1...STEP-N`",
        "A passed step never implies a passed KR",
        "Product, Engineering, and Evaluation do not create their own Objectives or KRs",
    ):
        assert marker in standard


def test_project_manager_and_product_work_on_complete_global_contracts() -> None:
    minimal_pm = read(LOOP / "roles" / "project-manager.md")
    minimal_product = read(LOOP / "roles" / "product-strategy.md")
    full_pm = read(WORKFLOW / "orchestrator" / "ROLE.md")
    full_product = read(WORKFLOW / "roles" / "product-prd" / "ROLE.md")

    for text in (minimal_pm, full_pm):
        assert "complete Project OKR" in text
        assert "Do not send Product" in text
        assert "one KR at a time" in text
    for text in (minimal_product, full_product):
        assert "complete Product Contract" in text
        assert "every accepted KR" in text
        assert "STEP" in text


def test_stage_assignments_preserve_global_scope_and_candidate_gate() -> None:
    product = read(LOOP / "templates" / "product-assignment.md")
    engineering = read(LOOP / "templates" / "engineering-assignment.md")
    evaluation = read(LOOP / "templates" / "evaluation-assignment.md")

    assert "delivery_stage: product_definition" in product
    assert "project_okr_scope: all_accepted_krs" in product
    assert "role_deliverable: complete_product_contract_for_existing_krs" in product
    assert "PRODUCT-CONTRACT" in product

    assert "delivery_stage: engineering_delivery" in engineering
    assert "product_contract_accepted: 1" in engineering
    assert "engineering_objective: produce_the_complete_runnable_candidate" in engineering

    assert "delivery_stage: independent_evaluation" in evaluation
    assert "candidate_ready_for_independent_evaluation: 1" in evaluation
    assert "candidate_artifact_path:" in evaluation
    assert "evaluation_scope: complete_project_okr" in evaluation


def test_engineering_alone_decomposes_steps_and_cannot_self_pass_krs() -> None:
    minimal = read(LOOP / "roles" / "engineering.md")
    full = read(WORKFLOW / "roles" / "implementer" / "ROLE.md")

    for text in (minimal, full):
        assert "`STEP-1...STEP-N`" in text
        assert "partial STEP completion" in text
        assert "cannot pass the Engineering stage" in text
        assert "cannot" in text and "KR" in text


def test_evaluation_is_post_candidate_and_reports_every_kr() -> None:
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
        assert "kr_results:" in text
        assert "milestone_observed_pass: 0 | 1" in text
        assert "pass_with_residual_risk" not in text


def test_milestone_board_tracks_global_stage_not_step_activity() -> None:
    board = read(LOOP / "templates" / "milestone-board.md")

    for marker in (
        "Delivery stage",
        "Project OKR accepted",
        "Product Contract accepted",
            "Candidate ready for independent evaluation",
        "Independent evaluation executed",
        "Accepted Product Contract",
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

    assert "project_okr_scope: all_accepted_krs" in product_assignment
    assert "KR-1" in product_contract and "KR-2" in product_contract
    assert "KR-3" not in product_contract
    assert "creates no additional Objective or KR" in product_contract
    assert "product_contract_accepted: 1" in engineering_assignment
    assert "candidate_ready_for_independent_evaluation: 1" in engineering_return
    assert "candidate_ready_for_independent_evaluation: 1" in evaluation_assignment
    assert "KR-1" in evaluation_return and "KR-2" in evaluation_return
    assert "evaluation_executed: 1" in evaluation_return
    assert "milestone_pass: 1" in decision


def test_public_contracts_do_not_reintroduce_role_specific_okr_namespaces() -> None:
    roots = (
        ROOT / "README.md",
        ROOT / "CHANGELOG.md",
        ROOT / "ROADMAP.md",
        ROOT / "docs",
        ROOT / "examples",
        ROOT / "scripts",
    )
    files: list[Path] = []
    for root in roots:
        if root.is_file():
            files.append(root)
        else:
            files.extend(
                path
                for path in root.rglob("*")
                if path.is_file() and path.suffix in {".md", ".py", ".html", ".json"}
            )

    legacy = ("MKR", "PKR", "EKR")
    for path in files:
        text = read(path)
        for term in legacy:
            assert term not in text, f"{path} reintroduced {term}"

    standard = read(OKR)
    assert "No role may create a second Objective or KR set" in standard
