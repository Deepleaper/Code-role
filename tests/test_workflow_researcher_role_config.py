import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"
RESEARCHER = WORKFLOW / "roles" / "researcher"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_researcher_workflow_files_exist() -> None:
    expected = [
        WORKFLOW / "README.md",
        WORKFLOW / "handoff-protocol.md",
        WORKFLOW / "packet-schema.md",
        WORKFLOW / "source-map.md",
        RESEARCHER / "ROLE.md",
        RESEARCHER / "reports" / "README.md",
        RESEARCHER / "templates" / "research-brief.md",
        RESEARCHER / "templates" / "evidence-map.md",
        RESEARCHER / "templates" / "risk-register.md",
        RESEARCHER / "templates" / "open-questions.md",
        RESEARCHER / "templates" / "source-log.md",
        RESEARCHER / "templates" / "handoff.manifest.json",
        RESEARCHER / "templates" / "latest.json",
    ]
    missing = [path for path in expected if not path.exists()]
    assert not missing


def test_packet_protocol_versions_and_handoff_are_explicit() -> None:
    protocol = read(WORKFLOW / "handoff-protocol.md")
    schema = read(WORKFLOW / "packet-schema.md")

    assert "packet-vNNN" in protocol
    assert "latest.json" in protocol
    assert "handoff.manifest.json" in protocol
    assert "Downstream roles must record the exact upstream packet version" in protocol
    assert "ready_for_next_role" in protocol
    assert "packet-v001" in schema
    assert "input_packets" in schema


def test_researcher_read_write_boundaries_are_documented() -> None:
    role = read(RESEARCHER / "ROLE.md")
    source_map = read(WORKFLOW / "source-map.md")

    assert "does not write PRD" in role
    assert "does not write code" in role
    assert "does not change tests" in role
    assert "does not use external research unless explicitly approved" in role
    assert "docs/workflow/roles/researcher/reports/<milestone>/packet-vNNN/" in source_map
    assert "must not write outside its reports folder without explicit user confirmation" in source_map


def test_researcher_manifest_template_is_machine_readable() -> None:
    manifest_path = RESEARCHER / "templates" / "handoff.manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    document_paths = {doc["path"] for doc in manifest["documents"]}
    assert manifest["schema_version"] == "0.1"
    assert manifest["role"] == "researcher"
    assert manifest["status"] == "draft"
    assert manifest["handoff_to"] == ["product"]
    assert {
        "research-brief.md",
        "evidence-map.md",
        "risk-register.md",
        "open-questions.md",
        "source-log.md",
    }.issubset(document_paths)
