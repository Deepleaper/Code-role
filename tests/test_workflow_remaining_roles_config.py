import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROLES = ROOT / "docs" / "workflow" / "roles"


ROLE_EXPECTATIONS = {
    "architect": {
        "handoff_to": ["code-context"],
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
        "documents": {
            "test-plan.md",
            "test-results.md",
            "regression-matrix.md",
            "failure-analysis.md",
            "quality-gate.md",
        },
        "input_role": "implementer",
    },
    "reviewer": {
        "handoff_to": ["orchestrator"],
        "documents": {
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
        assert (role_dir / "templates" / "latest.json").exists()
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
        assert manifest["input_packets"][0]["status_at_consumption"] == "ready_for_next_role"
        assert manifest["input_packets"][0]["consumption_status"] == "accepted_as_input"


def test_high_risk_role_boundaries_are_explicit() -> None:
    implementer = read(ROLES / "implementer" / "ROLE.md")
    evaluator = read(ROLES / "test-evaluator" / "ROLE.md")
    reviewer = read(ROLES / "reviewer" / "ROLE.md")
    code_context = read(ROLES / "code-context" / "ROLE.md")

    assert "must not begin from chat-only instruction" in implementer
    assert "must not expand scope" in implementer
    assert "does not change code unless explicitly reassigned as Implementer" in evaluator
    assert "does not implement fixes" in reviewer
    assert "does not rewrite upstream packets" in reviewer
    assert "does not modify code" in code_context


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

