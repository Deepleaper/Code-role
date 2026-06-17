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
        "milestone-contract.md",
        "role-completion-contract.md",
        "evaluation-sop.md",
    ]:
        assert filename in readme
        assert filename in workflow_readme

    assert "scripts/init_project_workflow.py" in setup
    assert "generated role-instance prompts" in guide
    assert "state index can be generated only when useful for onboarding" in guide


def test_state_index_and_git_policy_define_boundaries() -> None:
    state_index = read(WORKFLOW / "state-index.md")
    git_policy = read(WORKFLOW / "git-operation-policy.md")

    assert "It is not authoritative" in state_index
    assert "ROLE.md" in state_index
    assert "handoff.manifest.json" in state_index
    assert "strict handoff `packet.lock.json`" in state_index

    assert "Git operations are outside the Code-role role chain" in git_policy
    assert "Use the target project's normal Git process" in git_policy
    assert "git add" in git_policy
    assert "git commit" in git_policy
    assert "git push" in git_policy
    assert "code-role/` files are local workflow assistance" in git_policy


def test_init_project_workflow_creates_fast_setup_files(tmp_path: Path) -> None:
    target = tmp_path / "Target Project"
    target.mkdir()
    exclude = target / ".git" / "info" / "exclude"
    exclude.parent.mkdir(parents=True)
    exclude.write_text("# local excludes\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--target",
            str(target),
            "--project-name",
            "Target Project",
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
        target / "code-role" / "workflow" / "orchestrator" / "final-packet-index.md",
        target / "code-role" / "workflow" / "orchestrator" / "milestone-contract.md",
        target / "code-role" / "workflow" / "evaluation" / "evaluation-sop.md",
        target / "code-role" / "role-instance-prompts" / "workflow-orchestrator.md",
        target / "code-role" / "role-instance-prompts" / "researcher.md",
        target / "code-role" / "role-instance-prompts" / "product-prd.md",
        target / "code-role" / "role-instance-prompts" / "reviewer.md",
    ]

    for path in expected:
        assert path.exists(), path

    project_config = read(target / "code-role" / "project-config.md")
    project_readme = read(target / "code-role" / "README.md")
    orchestrator_prompt = read(target / "code-role" / "role-instance-prompts" / "workflow-orchestrator.md")
    final_packet_index = read(target / "code-role" / "workflow" / "orchestrator" / "final-packet-index.md")
    researcher_prompt = read(target / "code-role" / "role-instance-prompts" / "researcher.md")
    product_prompt = read(target / "code-role" / "role-instance-prompts" / "product-prd.md")
    reviewer_prompt = read(target / "code-role" / "role-instance-prompts" / "reviewer.md")
    milestone_contract = read(target / "code-role" / "workflow" / "orchestrator" / "milestone-contract.md")
    evaluation_sop = read(target / "code-role" / "workflow" / "evaluation" / "evaluation-sop.md")
    assert "tracking_policy: local-only" in project_config
    for generated in [project_config, project_readme]:
        assert "local-only workflow assistance" in generated
        assert "not product runtime content" in generated
        assert "should not be committed or pushed" in generated
        assert "Code-role does not own the target project's Git workflow" in generated
        assert "milestone-contract.md" in generated
        assert "role-completion-contract.md" in generated
        assert "evaluation-sop.md" in generated
    assert "status: draft" in milestone_contract
    assert "business_goal:" in milestone_contract
    assert "success_criteria:" in milestone_contract
    assert "role_completion_conditions:" in milestone_contract
    assert "role_completion_status=1" in milestone_contract
    assert "role_completion_status` must be `0" in milestone_contract
    assert "No execution role may start until this contract is confirmed" in milestone_contract
    assert "status: draft" in evaluation_sop
    assert "required_layers:" in evaluation_sop
    assert "not_run" in evaluation_sop
    assert "sop_calibration" in evaluation_sop
    assert "Do not run `git add`, `git commit`, or `git push`" in reviewer_prompt
    assert "orchestrator/project-manager-output-standard.md" in orchestrator_prompt
    assert "orchestrator/next-role-message-template.md" in orchestrator_prompt
    assert "final-packet-index.md" in orchestrator_prompt
    assert "Final Packet Index" in final_packet_index
    assert "Reviewer uses it as the authoritative index" in final_packet_index
    assert "workflow-orchestrator" in final_packet_index
    assert "roles/researcher/researcher-output-standard.md" in researcher_prompt
    assert "roles/product-prd/product-prd-output-standard.md" in product_prompt
    assert "roles/architect/architect-output-standard.md" in read(target / "code-role" / "role-instance-prompts" / "architect.md")
    assert "roles/code-context/code-context-output-standard.md" in read(target / "code-role" / "role-instance-prompts" / "code-context.md")
    assert "roles/implementer/implementer-output-standard.md" in read(target / "code-role" / "role-instance-prompts" / "implementer.md")
    assert "roles/test-evaluator/test-evaluator-output-standard.md" in read(target / "code-role" / "role-instance-prompts" / "test-evaluator.md")
    assert "workflow/orchestrator/milestone-contract.md" in read(target / "code-role" / "role-instance-prompts" / "test-evaluator.md")
    assert "docs/workflow/role-completion-contract.md" in read(target / "code-role" / "role-instance-prompts" / "test-evaluator.md")
    assert "workflow/evaluation/evaluation-sop.md" in read(target / "code-role" / "role-instance-prompts" / "test-evaluator.md")
    assert "roles/reviewer/reviewer-output-standard.md" in reviewer_prompt
    assert "workflow/orchestrator/milestone-contract.md" in reviewer_prompt
    assert "docs/workflow/role-completion-contract.md" in reviewer_prompt
    assert "workflow/evaluation/evaluation-sop.md" in reviewer_prompt
    assert "copy-ready short Orchestrator consumption-check summary" in reviewer_prompt
    assert "role_completion_status=1" in reviewer_prompt
    assert "role_completion_status=0" in reviewer_prompt
    assert "must not generate the authoritative next-role startup message" in reviewer_prompt
    assert not (target / "code-role" / "state-index").exists()
    assert "code-role/" in read(exclude)


def test_init_project_workflow_can_optionally_create_state_index(tmp_path: Path) -> None:
    target = tmp_path / "Target Project"
    target.mkdir()

    subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--target",
            str(target),
            "--project-name",
            "Target Project",
            "--write",
            "--with-state-index",
        ],
        check=True,
        text=True,
        capture_output=True,
    )

    expected = [
        target / "code-role" / "state-index" / "README.md",
        target / "code-role" / "state-index" / "current-workflow-index.md",
        target / "code-role" / "state-index" / "roles" / "researcher.md",
        target / "code-role" / "state-index" / "roles" / "product-prd.md",
        target / "code-role" / "state-index" / "roles" / "reviewer.md",
    ]

    for path in expected:
        assert path.exists(), path

    reviewer_index = read(target / "code-role" / "state-index" / "roles" / "reviewer.md")
    assert "roles/reviewer/reviewer-output-standard.md" in reviewer_index
    assert "non-authoritative navigation index" in reviewer_index
