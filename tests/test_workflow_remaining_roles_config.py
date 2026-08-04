import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROLES = ROOT / "docs" / "workflow" / "roles"

ROLE_DOCUMENTS = {
    "architect": {
        "architecture-plan.md",
        "boundary-map.md",
        "interface-contracts.md",
        "data-flow.md",
        "test-strategy.md",
        "risk-register.md",
    },
    "code-context": {
        "code-map.md",
        "dependency-map.md",
        "impact-analysis.md",
        "test-map.md",
        "implementation-constraints.md",
    },
    "implementer": {
        "implementation-summary.md",
        "changed-files.md",
        "verification-log.md",
        "risk-notes.md",
    },
    "test-evaluator": {
        "evaluation-sop.md",
        "evaluation-baseline.md",
        "test-plan.md",
        "test-results.md",
        "regression-matrix.md",
        "failure-analysis.md",
        "quality-gate.md",
        "sop-calibration.md",
    },
    "reviewer": {
        "milestone-drift-audit.md",
        "review-findings.md",
        "risk-decision.md",
        "packet-chain-audit.md",
        "final-gate.md",
    },
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def manifest(role_id: str) -> dict:
    return json.loads(
        read(ROLES / role_id / "templates" / "handoff.manifest.json")
    )


def test_role_folders_professional_templates_and_transport_contracts_exist() -> None:
    for role_id, documents in ROLE_DOCUMENTS.items():
        role_dir = ROLES / role_id
        assert (role_dir / "ROLE.md").exists()
        assert (role_dir / "reports" / "README.md").exists()
        assert (role_dir / "templates" / "assignment.md").exists()
        assert (role_dir / "templates" / "return.md").exists()
        for document in documents:
            assert (role_dir / "templates" / document).exists()


def test_manifests_index_documents_without_hard_coding_role_chain() -> None:
    for role_id, documents in ROLE_DOCUMENTS.items():
        data = manifest(role_id)
        document_paths = {document["path"] for document in data["documents"]}
        assert data["role"] == role_id
        assert data["status"] == "draft"
        assert data["return_to"] == "workflow-orchestrator"
        assert data["input_packets"] == []
        assert documents.issubset(document_paths)
        assert "handoff_to" not in data


def test_every_role_starts_from_complete_assignment_and_does_not_self_route() -> None:
    for role_id in ROLE_DOCUMENTS:
        role = read(ROLES / role_id / "ROLE.md")
        assert "A complete assignment starts" in role
        assert "Do not send a startup acknowledgement" in role
        assert "Do not recommend or choose the next role" in role
        assert "Use Chinese by default" in role
        role_return = read(ROLES / role_id / "templates" / "return.md")
        assert "return_to: workflow-orchestrator" in role_return


def test_architect_preserves_three_practice_tracks() -> None:
    standard = read(ROLES / "architect" / "architect-output-standard.md")
    combined = "\n".join(
        read(ROLES / "architect" / "templates" / name)
        for name in ROLE_DOCUMENTS["architect"]
    )
    assert "Current Delivery Project Practice" in standard
    assert "Industry Practice" in standard
    assert "Paper And Frontier Engineering Practice" in standard
    assert "current_project_practice" in combined
    assert "industry_practice" in combined
    assert "frontier_reference" in combined
    assert "Code Context Verification Needs" in combined


def test_code_context_grounds_architecture_in_repository_seams() -> None:
    standard = read(ROLES / "code-context" / "code-context-output-standard.md")
    combined = "\n".join(
        read(ROLES / "code-context" / "templates" / name)
        for name in ROLE_DOCUMENTS["code-context"]
    )
    assert "Architecture Intent" in standard
    assert "Current Project Code Evidence" in standard
    assert "Context Engineer Judgment Or Assumptions" in standard
    assert "architecture_intent" in combined
    assert "current_code_evidence" in combined
    assert "context_engineer_judgment" in combined
    assert "writable_candidate" in combined
    assert "likely change seam candidates" in combined


def test_implementer_uses_sufficient_scope_and_reproducible_evidence() -> None:
    standard = read(ROLES / "implementer" / "implementer-output-standard.md")
    assignment = read(ROLES / "implementer" / "templates" / "assignment.md")
    combined = "\n".join(
        read(ROLES / "implementer" / "templates" / name)
        for name in ROLE_DOCUMENTS["implementer"]
    )
    assert "A valid assignment is the start authorization" in standard
    assert "does not need to predict every file" in standard
    assert "required_artifact_path:" in assignment
    assert "writable_scope:" not in assignment
    assert "task_specific_exclusions:" in assignment
    assert "EKR-1...EKR-N" in standard
    assert "complete MKR/PKR contracts" in standard
    assert "repo_evidence" in combined
    assert "actual_file_change" in combined
    assert "verification_evidence" in combined
    assert "Do not mark an unrun command or test as pass" in combined


def test_test_evaluator_records_sop_after_candidate_gate_and_reports_binary_gate() -> None:
    standard = read(ROLES / "test-evaluator" / "test-evaluator-output-standard.md")
    role = read(ROLES / "test-evaluator" / "ROLE.md")
    data = manifest("test-evaluator")
    combined = "\n".join(
        read(ROLES / "test-evaluator" / "templates" / name)
        for name in ROLE_DOCUMENTS["test-evaluator"]
    )
    assert "Implementer-Reported Verification" in standard
    assert "Evaluator-Observed Evidence" in standard
    assert "Active Milestone Evaluation SOP" in standard
    assert "SOP Calibration Standard" in standard
    assert "candidate_ready_for_independent_evaluation=1" in role
    assert "complete runnable candidate" in role
    assert "Before inspecting candidate results" in role
    assert "evaluation_executed: 0 | 1" in combined
    assert "milestone_observed_pass: 0 | 1" in combined
    assert "mkr_results:" in combined
    assert data["quality_gate"]["evaluation_executed"] == 0
    assert data["quality_gate"]["candidate_gate_valid"] == 0
    assert data["quality_gate"]["milestone_observed_pass"] == 0
    assert data["quality_gate"]["mkr_results"] == []
    assert data["quality_gate"]["allowed_values"] == [0, 1]


def test_reviewer_audits_full_flow_and_reports_binary_gate() -> None:
    standard = read(ROLES / "reviewer" / "reviewer-output-standard.md")
    role = read(ROLES / "reviewer" / "ROLE.md")
    data = manifest("reviewer")
    combined = "\n".join(
        read(ROLES / "reviewer" / "templates" / name)
        for name in ROLE_DOCUMENTS["reviewer"]
    )
    assert "Flow-Wide Milestone Drift Audit" in standard
    assert "Evaluation SOP And Baseline Audit" in standard
    assert "Acceptance Gap Check" in standard
    assert "Packet Chain Audit" in standard
    assert "Final Gate Judgment" in standard
    assert "current final output of Workflow Orchestrator and every professional role" in role
    assert "review_gate_pass: 0 | 1" in combined
    assert "Role-By-Role Drift Matrix" in combined
    assert "correction_owner" in combined
    assert data["quality_gate"]["review_gate_pass"] == 0
    assert data["quality_gate"]["allowed_values"] == [0, 1]
    assert data["evaluation_baseline_audit"][
        "unsupported_industry_claims_fail_required_check"
    ] is True


def test_roles_index_lists_all_execution_roles() -> None:
    index = read(ROLES / "README.md")
    for label in (
        "Researcher",
        "Product / PRD",
        "Architect",
        "Code Context",
        "Implementer",
        "Test Evaluator",
        "Reviewer",
    ):
        assert label in index
