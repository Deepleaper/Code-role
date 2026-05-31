import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"
SCRIPT = ROOT / "scripts" / "init_project_workflow.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_project_bootstrap_docs_are_linked() -> None:
    readme = read(ROOT / "README.md")
    workflow_readme = read(WORKFLOW / "README.md")
    setup = read(WORKFLOW / "role-instance-setup.md")
    guide = read(WORKFLOW / "role-configuration-guide.md")

    for filename in [
        "project-bootstrap.md",
        "state-index.md",
        "git-operation-policy.md",
    ]:
        assert filename in readme
        assert filename in workflow_readme

    assert "scripts/init_project_workflow.py" in setup
    assert "generated role-instance prompts" in guide
    assert "non-authoritative state index" in guide


def test_state_index_and_git_policy_define_boundaries() -> None:
    state_index = read(WORKFLOW / "state-index.md")
    git_policy = read(WORKFLOW / "git-operation-policy.md")

    assert "It is not authoritative" in state_index
    assert "ROLE.md" in state_index
    assert "handoff.manifest.json" in state_index
    assert "packet.lock.json" in state_index

    assert "Git operations are not automatic workflow steps" in git_policy
    assert "Confirm each class of operation separately" in git_policy
    assert "git add" in git_policy
    assert "git commit" in git_policy
    assert "git push" in git_policy
    assert "generated template indexes" in git_policy


def test_init_project_workflow_creates_fast_setup_files(tmp_path: Path) -> None:
    target = tmp_path / "Target Project"
    target.mkdir()

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--target",
            str(target),
            "--project-name",
            "Target Project",
            "--tracking",
            "repo-tracked",
            "--write",
        ],
        check=True,
        text=True,
        capture_output=True,
    )

    assert "created/updated" in result.stdout

    expected = [
        target / "code-role" / "README.md",
        target / "code-role" / "project-config.md",
        target / "code-role" / "workflow" / "orchestrator" / "workflow-state.md",
        target / "code-role" / "workflow" / "orchestrator" / "milestone-registry.md",
        target / "code-role" / "workflow" / "orchestrator" / "decision-log.md",
        target / "code-role" / "state-index" / "README.md",
        target / "code-role" / "state-index" / "current-workflow-index.md",
        target / "code-role" / "role-instance-prompts" / "reviewer.md",
        target / "code-role" / "state-index" / "roles" / "reviewer.md",
    ]

    for path in expected:
        assert path.exists(), path

    project_config = read(target / "code-role" / "project-config.md")
    reviewer_prompt = read(target / "code-role" / "role-instance-prompts" / "reviewer.md")
    reviewer_index = read(target / "code-role" / "state-index" / "roles" / "reviewer.md")

    assert "tracking_policy: repo-tracked" in project_config
    assert "Do not run `git add`, `git commit`, or `git push`" in reviewer_prompt
    assert "non-authoritative navigation index" in reviewer_index
