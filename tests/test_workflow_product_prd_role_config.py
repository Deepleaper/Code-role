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


def test_product_prd_role_consumes_researcher_packet() -> None:
    role = read(PRODUCT / "ROLE.md")
    manifest = json.loads((PRODUCT / "templates" / "handoff.manifest.json").read_text(encoding="utf-8"))

    assert "accepted Researcher packets" in role
    assert "read the upstream `handoff.manifest.json` first" in role
    assert "Product PRD Output Standard" in role
    assert "owns product commitment, not product imagination" in role
    assert "must not become committed scope" in role
    assert "records the exact Researcher packet consumed as input" in role
    assert "locks the Researcher packet" not in role
    assert manifest["role"] == "product-prd"
    assert manifest["handoff_to"] == ["architect"]
    assert manifest["input_packets"][0]["role"] == "researcher"
    assert manifest["input_packets"][0]["status_at_consumption"] == "draft"
    assert manifest["input_packets"][0]["consumption_status"] == "accepted_as_input"


def test_product_prd_boundaries_are_documented() -> None:
    role = read(PRODUCT / "ROLE.md")
    source_map = read(WORKFLOW / "source-map.md")

    assert "does not write implementation code" in role
    assert "does not change tests" in role
    assert "does not make architecture decisions" in role
    assert "does not edit release docs" in role
    assert "does not turn external frontier research directly into committed scope" in role
    assert "does not present unconfirmed product judgment as user decision" in role
    assert "does not write requirements without acceptance criteria" in role
    assert "docs/workflow/roles/product-prd/reports/<milestone>/packet-vNNN/" in source_map
    assert "must not write product source docs, architecture docs, release docs, code, or tests" in source_map


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
