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
        RESEARCHER / "researcher-output-standard.md",
        RESEARCHER / "reports" / "README.md",
        RESEARCHER / "templates" / "research-brief.md",
        RESEARCHER / "templates" / "evidence-map.md",
        RESEARCHER / "templates" / "risk-register.md",
        RESEARCHER / "templates" / "open-questions.md",
        RESEARCHER / "templates" / "source-log.md",
        RESEARCHER / "templates" / "handoff.manifest.json",
    ]
    missing = [path for path in expected if not path.exists()]
    assert not missing


def test_packet_protocol_versions_and_handoff_are_explicit() -> None:
    protocol = read(WORKFLOW / "handoff-protocol.md")
    schema = read(WORKFLOW / "packet-schema.md")

    assert "packet-vNNN" in protocol
    assert "final-packet-index.md" in schema
    assert "handoff.manifest.json" in protocol
    assert "records the exact assignment-named upstream artifact versions" in protocol
    assert "Strict Handoff" in protocol
    assert "packet-v001" in schema
    assert "input_packets" in schema


def test_researcher_read_write_boundaries_are_documented() -> None:
    role = read(RESEARCHER / "ROLE.md")
    source_map = read(WORKFLOW / "source-map.md")

    assert "PRD, architecture commitments, code, tests, evaluation verdicts" in role
    assert "Public-source network research is allowed by default" in role
    assert "Separate approval is required for authenticated/private resources" in role
    assert "Researcher Output Standard" in role
    assert "separate current-project facts from papers, industry practice, and inference" in role
    assert "Do not recommend or choose the next role" in role
    assert "docs/workflow/roles/researcher/reports/<milestone>/packet-vNNN/" in source_map
    assert "Must not write PRD commitments" in source_map


def test_researcher_output_standard_separates_project_and_frontier_research() -> None:
    standard = read(RESEARCHER / "researcher-output-standard.md")
    assert "研究员输出规范" in standard
    assert "Researcher Output Standard" in standard
    assert "当前项目研究" in standard
    assert "Current Project Research" in standard
    assert "前沿研究与工程实践" in standard
    assert "Frontier Research And Engineering Practice" in standard
    assert "If current project research and frontier research are not separated" in standard
    assert "external papers or engineering practices as current project facts" in standard
    assert "applicable" in standard
    assert "partially_applicable" in standard
    assert "not_applicable" in standard


def test_researcher_manifest_template_is_machine_readable() -> None:
    manifest_path = RESEARCHER / "templates" / "handoff.manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    document_paths = {doc["path"] for doc in manifest["documents"]}
    assert manifest["schema_version"] == "0.1"
    assert manifest["role"] == "researcher"
    assert manifest["status"] == "draft"
    assert manifest["return_to"] == "workflow-orchestrator"
    assert "docs/workflow/roles/researcher/researcher-output-standard.md" in manifest["source_scopes"]
    assert {
        "research-brief.md",
        "evidence-map.md",
        "risk-register.md",
        "open-questions.md",
        "source-log.md",
    }.issubset(document_paths)


def test_researcher_templates_are_professional_and_not_todo_scaffolds() -> None:
    template_paths = [
        RESEARCHER / "templates" / "research-brief.md",
        RESEARCHER / "templates" / "evidence-map.md",
        RESEARCHER / "templates" / "risk-register.md",
        RESEARCHER / "templates" / "open-questions.md",
        RESEARCHER / "templates" / "source-log.md",
    ]
    combined = "\n".join(read(path) for path in template_paths)

    assert "TODO" not in combined
    assert "Current Project Research" in combined
    assert "Frontier Research" in combined
    assert "original business goal" in combined
    assert "possible drift" in combined
    assert "repo_evidence" in combined
    assert "external_source" in combined
    assert "Downstream Use" in combined
