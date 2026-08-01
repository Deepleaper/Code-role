import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"
SCRIPT = ROOT / "scripts" / "init_project_workflow.py"
ROLES = (
    "workflow-orchestrator",
    "researcher",
    "product-prd",
    "architect",
    "code-context",
    "implementer",
    "test-evaluator",
    "reviewer",
)
PROFESSIONAL_ROLES = ROLES[1:]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_init(target: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--target",
            str(target),
            "--project-name",
            "Target Project",
            "--write",
            *extra,
        ],
        check=False,
        text=True,
        capture_output=True,
    )


def test_project_bootstrap_docs_are_linked() -> None:
    readme = read(ROOT / "README.md")
    workflow_readme = read(WORKFLOW / "README.md")
    setup = read(WORKFLOW / "role-instance-setup.md")

    for filename in (
        "project-bootstrap.md",
        "state-index.md",
        "git-operation-policy.md",
        "milestone-contract.md",
        "role-completion-contract.md",
        "evaluation-sop.md",
    ):
        assert filename in readme
        assert filename in workflow_readme
    assert "scripts/init_project_workflow.py" in setup


def test_state_index_and_git_policy_define_local_boundaries() -> None:
    state_index = read(WORKFLOW / "state-index.md")
    git_policy = read(WORKFLOW / "git-operation-policy.md")
    assert "It is not authoritative" in state_index
    assert "Git operations are outside the Code-role role chain" in git_policy
    assert "Use the target project's normal Git process" in git_policy
    assert "code-role/` files are local workflow assistance" in git_policy


def test_full_profile_initializer_creates_eight_prompts_and_role_templates(
    tmp_path: Path,
) -> None:
    target = tmp_path / "Target Project"
    exclude = target / ".git" / "info" / "exclude"
    exclude.parent.mkdir(parents=True)
    exclude.write_text("# local excludes\n", encoding="utf-8")

    result = run_init(target)
    assert result.returncode == 0, result.stderr

    code_role = target / "code-role"
    required_control = (
        code_role / "README.md",
        code_role / "DIALOGUE-CONTROL.md",
        code_role / "project-config.md",
        code_role / "workflow" / "orchestrator" / "workflow-state.md",
        code_role / "workflow" / "orchestrator" / "milestone-contract.md",
        code_role / "workflow" / "orchestrator" / "final-packet-index.md",
        code_role / "workflow" / "evaluation" / "evaluation-sop.md",
    )
    assert all(path.exists() for path in required_control)
    assert not (code_role / "workflow" / "orchestrator" / "decision-log.md").exists()
    assert not (code_role / "workflow" / "orchestrator" / "milestone-registry.md").exists()

    for role_id in ROLES:
        prompt = read(code_role / "role-instance-prompts" / f"{role_id}.md")
        assert "Use Chinese by default" in prompt
        assert "startup acknowledgement" in prompt
        assert "narrate routine progress" in prompt or role_id == "workflow-orchestrator"
    for role_id in PROFESSIONAL_ROLES:
        assert (code_role / "templates" / f"{role_id}-assignment.md").exists()
        role_return = read(code_role / "templates" / f"{role_id}-return.md")
        assert "return_to: workflow-orchestrator" in role_return

    config = read(code_role / "project-config.md")
    assert "control_profile: full-eight-role" in config
    assert "valid_assignment_starts_immediately: true" in config
    assert "format_only_rework_allowed: false" in config
    assert "role_self_routing_allowed: false" in config
    assert "code-role/" in read(exclude)


def test_force_refresh_preserves_durable_project_memory(tmp_path: Path) -> None:
    target = tmp_path / "Target Project"
    target.mkdir()
    assert run_init(target).returncode == 0

    state = target / "code-role" / "workflow" / "orchestrator" / "workflow-state.md"
    sop = target / "code-role" / "workflow" / "evaluation" / "evaluation-sop.md"
    prompt = target / "code-role" / "role-instance-prompts" / "researcher.md"
    state.write_text("real workflow memory\n", encoding="utf-8")
    sop.write_text("frozen evaluation memory\n", encoding="utf-8")
    prompt.write_text("stale prompt\n", encoding="utf-8")

    result = run_init(target, "--force")
    assert result.returncode == 0, result.stderr
    assert read(state) == "real workflow memory\n"
    assert read(sop) == "frozen evaluation memory\n"
    assert "stale prompt" not in read(prompt)
    assert "A complete Project Manager assignment starts work immediately" in read(prompt)


def test_state_index_is_optional_and_non_authoritative(tmp_path: Path) -> None:
    target = tmp_path / "Target Project"
    target.mkdir()
    assert run_init(target, "--with-state-index").returncode == 0

    index_root = target / "code-role" / "state-index"
    assert "non-authoritative navigation index" in read(index_root / "README.md")
    for role_id in ROLES:
        role_index = read(index_root / "roles" / f"{role_id}.md")
        assert "Status: non-authoritative navigation index" in role_index
        assert "Read authoritative files directly" in role_index
