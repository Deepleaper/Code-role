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
        PRODUCT / "reports" / "README.md",
        PRODUCT / "templates" / "product-brief.md",
        PRODUCT / "templates" / "prd.md",
        PRODUCT / "templates" / "acceptance-criteria.md",
        PRODUCT / "templates" / "non-goals.md",
        PRODUCT / "templates" / "decision-log.md",
        PRODUCT / "templates" / "handoff.manifest.json",
        PRODUCT / "templates" / "latest.json",
    ]
    missing = [path for path in expected if not path.exists()]
    assert not missing


def test_product_prd_role_consumes_researcher_packet() -> None:
    role = read(PRODUCT / "ROLE.md")
    manifest = json.loads((PRODUCT / "templates" / "handoff.manifest.json").read_text(encoding="utf-8"))

    assert "approved Researcher packets" in role
    assert "read the upstream `handoff.manifest.json` first" in role
    assert manifest["role"] == "product-prd"
    assert manifest["handoff_to"] == ["architect"]
    assert manifest["input_packets"][0]["role"] == "researcher"
    assert manifest["input_packets"][0]["status_at_consumption"] == "ready_for_next_role"


def test_product_prd_boundaries_are_documented() -> None:
    role = read(PRODUCT / "ROLE.md")
    source_map = read(WORKFLOW / "source-map.md")

    assert "does not write implementation code" in role
    assert "does not change tests" in role
    assert "does not make architecture decisions" in role
    assert "does not edit release docs" in role
    assert "docs/workflow/roles/product-prd/reports/<milestone>/packet-vNNN/" in source_map
    assert "must not write product source docs, architecture docs, release docs, code, or tests" in source_map


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

