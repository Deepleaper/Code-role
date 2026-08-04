import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"
PRODUCT = WORKFLOW / "roles" / "product-prd"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_product_prd_role_files_exist() -> None:
    expected = [
        PRODUCT / "ROLE.md",
        PRODUCT / "product-prd-output-standard.md",
        PRODUCT / "reports" / "README.md",
        PRODUCT / "templates" / "product-brief.md",
        PRODUCT / "templates" / "prd.md",
        PRODUCT / "templates" / "acceptance-criteria.md",
        PRODUCT / "templates" / "non-goals.md",
        PRODUCT / "templates" / "decision-log.md",
        PRODUCT / "templates" / "handoff.manifest.json",
    ]
    missing = [path for path in expected if not path.exists()]
    assert not missing


def test_product_prd_role_consumes_assignment_named_evidence() -> None:
    role = read(PRODUCT / "ROLE.md")
    manifest = json.loads((PRODUCT / "templates" / "handoff.manifest.json").read_text(encoding="utf-8"))

    assert "complete Product / PRD Assignment" in role
    assert "accepted Researcher artifacts and user decisions" in role
    assert "A complete assignment starts work immediately" in role
    assert "Do not recommend or choose the next role" in role
    assert manifest["role"] == "product-prd"
    assert manifest["return_to"] == "workflow-orchestrator"
    assert manifest["input_packets"] == []
    assert "assignment-named upstream artifacts" in manifest["source_scopes"]


def test_product_prd_boundaries_are_documented() -> None:
    role = read(PRODUCT / "ROLE.md")
    source_map = read(WORKFLOW / "source-map.md")

    assert "implementation architecture, STEP phases, code, tests, evaluation verdicts" in role
    assert "Do not invent implementation details as product facts" in role
    assert "Do not silently change an accepted Objective" in role
    assert "docs/workflow/roles/product-prd/reports/<milestone>/packet-vNNN/" in source_map
    assert "Must not write architecture implementation, code, tests" in source_map


def test_product_prd_output_standard_defines_product_commitment_quality() -> None:
    standard = read(PRODUCT / "product-prd-output-standard.md")
    assert "产品经理输出规范" in standard
    assert "Product PRD Output Standard" in standard
    assert "Product / PRD owns product commitment, not product imagination" in standard
    assert "frontier_reference" in standard
    assert "must not become committed scope directly" in standard
    assert "A requirement without acceptance criteria cannot enter committed scope" in standard
    assert "Acceptance Criteria Standard" in standard
    assert "Architect Handoff Standard" in standard


def test_product_prd_templates_are_listed_in_manifest() -> None:
    manifest = json.loads((PRODUCT / "templates" / "handoff.manifest.json").read_text(encoding="utf-8"))
    document_paths = {doc["path"] for doc in manifest["documents"]}

    assert {
        "product-brief.md",
        "prd.md",
        "acceptance-criteria.md",
        "non-goals.md",
        "decision-log.md",
    }.issubset(document_paths)


def test_product_prd_templates_enforce_evidence_scope_and_acceptance() -> None:
    product_brief = read(PRODUCT / "templates" / "product-brief.md")
    prd = read(PRODUCT / "templates" / "prd.md")
    acceptance = read(PRODUCT / "templates" / "acceptance-criteria.md")
    non_goals = read(PRODUCT / "templates" / "non-goals.md")
    decision_log = read(PRODUCT / "templates" / "decision-log.md")

    assert "Frontier Reference Boundary" in product_brief
    assert "Committed Scope" in product_brief
    assert "Proposed Scope Or Assumptions" in product_brief
    assert "original business goal" in product_brief
    assert "possible drift" in product_brief
    assert "Acceptance Link" in prd
    assert "Architect Handoff" in prd
    assert "Observable Behavior" in acceptance
    assert "Non-Regression Boundary" in acceptance
    assert "Downstream Misuse Risk" in non_goals
    assert "frontier references" in non_goals
    assert "User Confirmation Needed" in decision_log
    assert "product_assumption" in decision_log
