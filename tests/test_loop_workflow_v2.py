import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "init_loop_workflow.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_init(target: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            str(target),
            "--project-name",
            "Example Project",
            *extra,
        ],
        text=True,
        capture_output=True,
        check=False,
    )


def test_goal_loop_initializes_exactly_four_active_roles(tmp_path: Path) -> None:
    target = tmp_path / "target"
    (target / ".git" / "info").mkdir(parents=True)

    result = run_init(target)

    assert result.returncode == 0, result.stderr
    role_root = target / "code-role" / "role-instance-prompts"
    active = sorted(
        path.name for path in role_root.glob("*.md") if path.name != "README.md"
    )
    assert active == [
        "engineering.md",
        "independent-evaluation.md",
        "product-strategy.md",
        "project-manager.md",
    ]
    project_config = read(target / "code-role" / "project-config.md")
    assert "control_model: okr-delivery-v4" in project_config
    assert "default_engineering_evaluation_attempt_limit: 3" in project_config
    assert "default_iteration_limit_per_kr" not in project_config
    assert "active_roles:" in project_config
    assert (target / "code-role" / "OKR-STANDARD.md").exists()
    assert "code-role/" in read(target / ".git" / "info" / "exclude")


def test_goal_loop_has_three_layer_okr_and_mandatory_stage_contract(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()
    assert run_init(target).returncode == 0

    loop = read(target / "code-role" / "LOOP.md")
    engineering_assignment = read(
        target / "code-role" / "templates" / "engineering-assignment.md"
    )
    product_assignment = read(
        target / "code-role" / "templates" / "product-assignment.md"
    )
    evaluation_assignment = read(
        target / "code-role" / "templates" / "evaluation-assignment.md"
    )
    evaluator = read(
        target
        / "code-role"
        / "role-instance-prompts"
        / "independent-evaluation.md"
    )

    okr_standard = read(target / "code-role" / "OKR-STANDARD.md")

    assert "Three OKR Layers" in loop
    assert "Mandatory Delivery Stages" in loop
    assert "Engineering Execution Loop" in loop
    assert "There is no `partial_pass`" in loop
    assert "three failed Engineering-to-Evaluation attempts" in loop
    assert "Milestone OKR | Project Manager + user" in okr_standard
    assert "Product OKR | Product Strategy / Product PRD" in okr_standard
    assert "Engineering Execution KRs | Engineering / Implementer" in okr_standard

    for assignment in (engineering_assignment, product_assignment, evaluation_assignment):
        assert "role_prompt_path:" in assignment
        assert "acceptance_checks:" in assignment
        assert "required_artifact_path:" in assignment
    assert "milestone_okr_scope: all_accepted_mkrs" in product_assignment
    assert "product_okr_accepted: 1" in engineering_assignment
    assert "engineering_objective: produce_the_complete_runnable_candidate" in engineering_assignment
    assert "task_specific_exclusions:" in engineering_assignment
    assert "candidate_ready_for_independent_evaluation: 1" in evaluation_assignment
    assert "evaluation_scope: complete_mkr_and_pkr_contract" in evaluation_assignment
    board = read(target / "code-role" / "milestone-board.md")
    assert "Delivery stage" in board
    assert "Product OKR accepted" in board
    assert "Candidate ready for independent evaluation" in board
    assert "Decision Log" not in board
    assert "Do not evaluate before a runnable candidate exists" in evaluator
    assert "Required missing, inferred, unsupported, contradictory, or unrun checks are `0`" in evaluator
    assert "latest diff" in evaluator


def test_sync_archives_full_profile_prompts_and_preserves_board(tmp_path: Path) -> None:
    target = tmp_path / "target"
    old_role_root = target / "code-role" / "role-instance-prompts"
    old_role_root.mkdir(parents=True)
    for filename in (
        "workflow-orchestrator.md",
        "researcher.md",
        "product-prd.md",
        "architect.md",
        "code-context.md",
        "implementer.md",
        "test-evaluator.md",
        "reviewer.md",
    ):
        (old_role_root / filename).write_text(filename, encoding="utf-8")
    board = target / "code-role" / "milestone-board.md"
    board.write_text("existing business state\n", encoding="utf-8")

    result = run_init(target, "--sync")

    assert result.returncode == 0, result.stderr
    assert read(board) == "existing business state\n"
    for filename in (
        "workflow-orchestrator.md",
        "researcher.md",
        "product-prd.md",
        "architect.md",
        "code-context.md",
        "implementer.md",
        "test-evaluator.md",
        "reviewer.md",
    ):
        assert not (old_role_root / filename).exists()
        assert (
            target
            / "code-role"
            / "archive"
            / "full-profile-role-instance-prompts"
            / filename
        ).exists()
    active = sorted(
        path.name for path in old_role_root.glob("*.md") if path.name != "README.md"
    )
    assert active == [
        "engineering.md",
        "independent-evaluation.md",
        "product-strategy.md",
        "project-manager.md",
    ]


def test_check_mode_accepts_generated_project(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()
    assert run_init(target).returncode == 0

    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(target), "--check"],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "goal-loop validation passed" in result.stdout
