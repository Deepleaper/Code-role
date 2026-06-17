import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROLES = ROOT / "docs" / "workflow" / "roles"


ROLE_EXPECTATIONS = {
    "architect": {
        "handoff_to": ["code-context"],
        "status_at_consumption": "draft",
        "documents": {
            "architecture-plan.md",
            "boundary-map.md",
            "interface-contracts.md",
            "data-flow.md",
            "test-strategy.md",
            "risk-register.md",
        },
        "input_role": "product-prd",
    },
    "code-context": {
        "handoff_to": ["implementer"],
        "status_at_consumption": "draft",
        "documents": {
            "code-map.md",
            "dependency-map.md",
            "impact-analysis.md",
            "test-map.md",
            "implementation-constraints.md",
        },
        "input_role": "architect",
    },
    "implementer": {
        "handoff_to": ["test-evaluator"],
        "status_at_consumption": "draft",
        "documents": {
            "implementation-summary.md",
            "changed-files.md",
            "verification-log.md",
            "risk-notes.md",
        },
        "input_role": "code-context",
    },
    "test-evaluator": {
        "handoff_to": ["reviewer"],
        "status_at_consumption": "draft",
        "documents": {
            "evaluation-sop.md",
            "evaluation-baseline.md",
            "test-plan.md",
            "test-results.md",
            "regression-matrix.md",
            "failure-analysis.md",
            "quality-gate.md",
            "sop-calibration.md",
        },
        "input_role": "implementer",
    },
    "reviewer": {
        "handoff_to": ["orchestrator"],
        "status_at_consumption": "draft",
        "documents": {
            "milestone-drift-audit.md",
            "review-findings.md",
            "risk-decision.md",
            "packet-chain-audit.md",
            "final-gate.md",
        },
        "input_role": "test-evaluator",
    },
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_remaining_role_folders_and_templates_exist() -> None:
    for role_id, expectation in ROLE_EXPECTATIONS.items():
        role_dir = ROLES / role_id
        assert (role_dir / "ROLE.md").exists()
        assert (role_dir / "reports" / "README.md").exists()
        assert (role_dir / "templates" / "handoff.manifest.json").exists()
        for doc in expectation["documents"]:
            assert (role_dir / "templates" / doc).exists()


def test_remaining_role_manifests_are_valid_and_chain_locked() -> None:
    for role_id, expectation in ROLE_EXPECTATIONS.items():
        manifest = json.loads((ROLES / role_id / "templates" / "handoff.manifest.json").read_text())
        document_paths = {doc["path"] for doc in manifest["documents"]}
        assert manifest["role"] == role_id
        assert manifest["status"] == "draft"
        assert manifest["handoff_to"] == expectation["handoff_to"]
        assert expectation["documents"].issubset(document_paths)
        assert manifest["input_packets"][0]["role"] == expectation["input_role"]
        assert manifest["input_packets"][0]["status_at_consumption"] == expectation["status_at_consumption"]
        assert manifest["input_packets"][0]["consumption_status"] == "accepted_as_input"


def test_high_risk_role_boundaries_are_explicit() -> None:
    architect = read(ROLES / "architect" / "ROLE.md")
    implementer = read(ROLES / "implementer" / "ROLE.md")
    evaluator = read(ROLES / "test-evaluator" / "ROLE.md")
    reviewer = read(ROLES / "reviewer" / "ROLE.md")
    code_context = read(ROLES / "code-context" / "ROLE.md")

    assert "Do not route directly from Architect to Test Evaluator" in architect
    assert "Default downstream role: Code Context / Context Engineer" in architect
    assert "Architect Output Standard" in architect
    assert "current delivery project practice, industry practice, and paper/frontier engineering practice" in architect
    assert "does not present industry practice as current project fact" in architect
    assert "does not present papers or frontier engineering practice as architecture commitment" in architect
    assert "Alias: Context Engineer" in code_context
    assert "Code Context Output Standard" in code_context
    assert "architecture intent, current project code evidence, and Context Engineer judgment or assumptions" in code_context
    assert "does not present Architect intent as current code fact" in code_context
    assert "does not present writable candidates as approved writable scope" in code_context
    assert "must not begin from chat-only instruction" in implementer
    assert "must not expand scope" in implementer
    assert "Implementer Output Standard" in implementer
    assert "writable_candidate` entries are not write authorization" in implementer
    assert "must not modify files outside exact writable scope" in implementer
    assert "must not run `git add`, `git commit`, or `git push`" in implementer
    assert "does not change code unless explicitly reassigned as Implementer" in evaluator
    assert "Test Evaluator Output Standard" in evaluator
    assert "active milestone `evaluation-sop.md`" in evaluator
    assert "code-role/workflow/evaluation/evaluation-sop.md" in evaluator
    assert "SOP Calibration Rule" in evaluator
    assert "packet-local evaluation baseline, industry or common-consensus evaluation references" in evaluator
    assert "First response baseline discussion" in evaluator
    assert "does not invent evaluation baselines without user confirmation or source evidence" in evaluator
    assert "Implementer-reported verification, evaluator-observed evidence, and evaluator quality judgment" in evaluator
    assert "does not treat Implementer-reported verification as evaluator-observed result" in evaluator
    assert "does not implement fixes" in evaluator
    assert "does not implement fixes" in reviewer
    assert "does not rewrite upstream packets" in reviewer
    assert "Reviewer Output Standard" in reviewer
    assert "audit Workflow Orchestrator state, decisions, and next-role handoff briefs against the original milestone anchor" in reviewer
    assert "code-role/workflow/orchestrator/milestone-contract.md" in reviewer
    assert "code-role/workflow/evaluation/evaluation-sop.md" in reviewer
    assert "audit each execution role's output against the original milestone anchor" in reviewer
    assert "audit whether Test Evaluator followed `code-role/workflow/evaluation/evaluation-sop.md`" in reviewer
    assert "which specific role must revise if drift exists" in reviewer
    assert "flow-wide milestone drift, evaluation baseline validity, acceptance gaps, packet-chain evidence, and final gate judgment" in reviewer
    assert "does not treat an unconfirmed evaluation mechanism or benchmark baseline as sufficient evidence" in reviewer
    assert "does not accept unsupported industry-consensus or benchmark claims" in reviewer
    assert "does not treat Test Evaluator `pass_with_residual_risk` as automatic final acceptance" in reviewer
    assert "does not ignore gaps between PRD or acceptance criteria and quality-gate conclusions" in reviewer
    assert "does not modify code" in code_context


def test_architect_output_standard_and_templates_separate_practice_tracks() -> None:
    standard = read(ROLES / "architect" / "architect-output-standard.md")
    role = read(ROLES / "architect" / "ROLE.md")
    manifest = json.loads((ROLES / "architect" / "templates" / "handoff.manifest.json").read_text())
    template_paths = [
        ROLES / "architect" / "templates" / "architecture-plan.md",
        ROLES / "architect" / "templates" / "boundary-map.md",
        ROLES / "architect" / "templates" / "interface-contracts.md",
        ROLES / "architect" / "templates" / "data-flow.md",
        ROLES / "architect" / "templates" / "test-strategy.md",
        ROLES / "architect" / "templates" / "risk-register.md",
    ]
    combined = "\n".join(read(path) for path in template_paths)

    assert "架构师输出规范" in standard
    assert "Architect Output Standard" in standard
    assert "Current Delivery Project Practice" in standard
    assert "Industry Practice" in standard
    assert "Paper And Frontier Engineering Practice" in standard
    assert "current_project_practice" in combined
    assert "industry_practice" in combined
    assert "frontier_reference" in combined
    assert "original business goal" in combined
    assert "possible drift" in combined
    assert "Code Context Verification Needs" in combined
    assert "TODO" not in combined
    assert "locks upstream Product / PRD" not in role
    assert "docs/workflow/roles/architect/architect-output-standard.md" in manifest["source_scopes"]


def test_code_context_output_standard_and_templates_ground_implementation_context() -> None:
    standard = read(ROLES / "code-context" / "code-context-output-standard.md")
    manifest = json.loads((ROLES / "code-context" / "templates" / "handoff.manifest.json").read_text())
    template_paths = [
        ROLES / "code-context" / "templates" / "code-map.md",
        ROLES / "code-context" / "templates" / "dependency-map.md",
        ROLES / "code-context" / "templates" / "impact-analysis.md",
        ROLES / "code-context" / "templates" / "test-map.md",
        ROLES / "code-context" / "templates" / "implementation-constraints.md",
    ]
    combined = "\n".join(read(path) for path in template_paths)

    assert "Code Context 输出规范" in standard
    assert "Code Context Output Standard" in standard
    assert "Architecture Intent" in standard
    assert "Current Project Code Evidence" in standard
    assert "Context Engineer Judgment Or Assumptions" in standard
    assert "architecture_intent" in combined
    assert "current_code_evidence" in combined
    assert "context_engineer_judgment" in combined
    assert "original business goal" in combined
    assert "possible drift" in combined
    assert "writable_candidate" in combined
    assert "TODO" not in combined
    assert manifest["input_packets"][0]["status_at_consumption"] == "draft"
    assert "docs/workflow/roles/code-context/code-context-output-standard.md" in manifest["source_scopes"]


def test_implementer_output_standard_and_templates_require_exact_scope_and_verification() -> None:
    standard = read(ROLES / "implementer" / "implementer-output-standard.md")
    manifest = json.loads((ROLES / "implementer" / "templates" / "handoff.manifest.json").read_text())
    template_paths = [
        ROLES / "implementer" / "templates" / "implementation-summary.md",
        ROLES / "implementer" / "templates" / "changed-files.md",
        ROLES / "implementer" / "templates" / "verification-log.md",
        ROLES / "implementer" / "templates" / "risk-notes.md",
    ]
    combined = "\n".join(read(path) for path in template_paths)

    assert "Implementer 输出规范" in standard
    assert "Implementer Output Standard" in standard
    assert "Approved Implementation Scope" in standard
    assert "Actual Project Changes" in standard
    assert "Verification Evidence And Residual Risk" in standard
    assert "implementation_start_confirmation" in combined
    assert "approved_writable_scope" in combined
    assert "actual_file_change" in combined
    assert "original business goal" in combined
    assert "possible drift" in combined
    assert "verification_evidence" in combined
    assert "Do not mark an unrun command or test as pass" in combined
    assert "TODO" not in combined
    assert manifest["input_packets"][0]["status_at_consumption"] == "draft"
    assert "docs/workflow/roles/implementer/implementer-output-standard.md" in manifest["source_scopes"]


def test_test_evaluator_output_standard_and_templates_separate_reported_and_observed_evidence() -> None:
    standard = read(ROLES / "test-evaluator" / "test-evaluator-output-standard.md")
    manifest = json.loads((ROLES / "test-evaluator" / "templates" / "handoff.manifest.json").read_text())
    template_paths = [
        ROLES / "test-evaluator" / "templates" / "evaluation-sop.md",
        ROLES / "test-evaluator" / "templates" / "evaluation-baseline.md",
        ROLES / "test-evaluator" / "templates" / "test-plan.md",
        ROLES / "test-evaluator" / "templates" / "test-results.md",
        ROLES / "test-evaluator" / "templates" / "regression-matrix.md",
        ROLES / "test-evaluator" / "templates" / "failure-analysis.md",
        ROLES / "test-evaluator" / "templates" / "quality-gate.md",
        ROLES / "test-evaluator" / "templates" / "sop-calibration.md",
    ]
    combined = "\n".join(read(path) for path in template_paths)

    assert "Test Evaluator 输出规范" in standard
    assert "Test Evaluator Output Standard" in standard
    assert "Implementer-Reported Verification" in standard
    assert "User-Confirmed Evaluation Mechanism And Baseline" in standard
    assert "Industry Or Common-Consensus Evaluation References" in standard
    assert "Evaluator-Observed Evidence" in standard
    assert "Evaluator Quality Judgment" in standard
    assert "Active Milestone Evaluation SOP" in standard
    assert "SOP Calibration Standard" in standard
    assert "evaluation-baseline.md" in standard
    assert "evaluation-sop.md" in standard
    assert "sop-calibration.md" in standard
    assert "original business goal" in combined
    assert "possible drift" in combined
    assert "evaluation_sop" in combined
    assert "sop_calibration" in combined
    assert "user_approved_eval_mechanism" in combined
    assert "industry_evaluation_reference" in combined
    assert "benchmark_dataset_reference" in combined
    assert "metric_definition" in combined
    assert "implementer_reported_verification" in combined
    assert "evaluator_observed_result" in combined
    assert "test_command_output" in combined
    assert "regression_evidence" in combined
    assert "final_acceptance" in combined
    assert "TODO" not in combined
    assert manifest["input_packets"][0]["status_at_consumption"] == "draft"
    assert "docs/workflow/roles/test-evaluator/test-evaluator-output-standard.md" in manifest["source_scopes"]
    assert "docs/workflow/evaluation-sop.md" in manifest["source_scopes"]
    assert "code-role/workflow/evaluation/evaluation-sop.md" in manifest["source_scopes"]
    assert "evaluation-sop.md" in {doc["path"] for doc in manifest["documents"]}
    assert "sop-calibration.md" in {doc["path"] for doc in manifest["documents"]}
    assert manifest["evaluation_baseline"]["sop_status"] == "draft"
    assert manifest["evaluation_baseline"]["mechanism_confirmed"] is False


def test_reviewer_output_standard_and_templates_enforce_final_gate_gap_review() -> None:
    standard = read(ROLES / "reviewer" / "reviewer-output-standard.md")
    manifest = json.loads((ROLES / "reviewer" / "templates" / "handoff.manifest.json").read_text())
    template_paths = [
        ROLES / "reviewer" / "templates" / "milestone-drift-audit.md",
        ROLES / "reviewer" / "templates" / "review-findings.md",
        ROLES / "reviewer" / "templates" / "risk-decision.md",
        ROLES / "reviewer" / "templates" / "packet-chain-audit.md",
        ROLES / "reviewer" / "templates" / "final-gate.md",
    ]
    combined = "\n".join(read(path) for path in template_paths)

    assert "Reviewer 输出规范" in standard
    assert "Reviewer Output Standard" in standard
    assert "Flow-Wide Milestone Drift Audit" in standard
    assert "Milestone Drift Audit Standard" in standard
    assert "final-packet-index.md" in standard
    assert "Evaluation SOP And Baseline Audit" in standard
    assert "milestone-contract.md" in standard
    assert "evaluation-sop.md" in standard
    assert "Acceptance Gap Check" in standard
    assert "Packet Chain Audit" in standard
    assert "Final Gate Judgment" in standard
    assert "original_milestone_anchor" in combined
    assert "milestone_contract" in combined
    assert "evaluation_sop" in combined
    assert "sop_calibration" in combined
    assert "final_packet_index" in combined
    assert "possible_drift_summary" in combined
    assert "current_final_versions_only" in combined
    assert "Role-By-Role Drift Matrix" in combined
    assert "workflow-orchestrator" in combined
    assert "orchestrator_output_evidence" in combined
    assert "Correction Routing Recommendation" in combined
    assert "correction_owner" in combined
    assert "drift_audit" in combined
    assert "milestone_goal" in combined
    assert "Evaluation SOP And Baseline Audit" in combined
    assert "evaluation_baseline_evidence" in combined
    assert "benchmark_dataset_reference" in combined
    assert "metric_definition" in combined
    assert "Acceptance Gap Check" in combined
    assert "test_evaluator_evidence" in combined
    assert "packet_chain_evidence" in combined
    assert "final_acceptance" in combined
    assert "strict_handoff_requested" in combined
    assert "TODO" not in combined
    assert manifest["input_packets"][0]["status_at_consumption"] == "draft"
    assert "docs/workflow/roles/reviewer/reviewer-output-standard.md" in manifest["source_scopes"]
    assert "docs/workflow/milestone-contract.md" in manifest["source_scopes"]
    assert "docs/workflow/evaluation-sop.md" in manifest["source_scopes"]
    assert "code-role/workflow/orchestrator/milestone-contract.md" in manifest["source_scopes"]
    assert "code-role/workflow/evaluation/evaluation-sop.md" in manifest["source_scopes"]
    assert manifest["final_packet_index"] == "docs/workflow/orchestrator/final-packet-index.md"
    assert manifest["audit_scope"] == "current_final_versions_only"
    assert "docs/workflow/orchestrator/final-packet-index.md" in manifest["source_scopes"]
    assert "original milestone anchor from Orchestrator or user input" in manifest["source_scopes"]
    assert "Orchestrator workflow-state, milestone-registry, decision-log, consumption-check outputs, and next-role handoff briefs" in manifest["source_scopes"]
    assert "all upstream role packets in selected chain" in manifest["source_scopes"]
    assert "upstream test-evaluator evaluation-sop.md" in manifest["source_scopes"]
    assert "upstream test-evaluator sop-calibration.md" in manifest["source_scopes"]
    assert manifest["evaluation_baseline_audit"]["sop_required"] is True
    assert manifest["evaluation_baseline_audit"]["sop_calibration_required"] is True
    assert manifest["evaluation_baseline_audit"]["mechanism_required"] is True
    assert manifest["evaluation_baseline_audit"]["unsupported_industry_claims_block_final_acceptance"] is True
    assert manifest["quality_gate"]["final_acceptance"] is False


def test_execution_roles_require_orchestrator_consumption_request() -> None:
    for role_id in ROLE_EXPECTATIONS:
        text = read(ROLES / role_id / "ROLE.md")
        assert "Completion Response Rule" in text, role_id
        assert "copy-ready short Orchestrator consumption-check summary" in text, role_id
        assert "same completion response" in text, role_id
        assert "must not generate the authoritative next-role startup message" in text, role_id


def test_roles_index_lists_all_execution_roles() -> None:
    index = read(ROLES / "README.md")
    for label in [
        "Researcher",
        "Product / PRD",
        "Architect",
        "Code Context",
        "Implementer",
        "Test Evaluator",
        "Reviewer",
    ]:
        assert label in index
