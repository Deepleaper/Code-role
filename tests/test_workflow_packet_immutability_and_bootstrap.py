from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_packet_schema_keeps_immutability_in_optional_strict_mode() -> None:
    text = read(WORKFLOW / "packet-schema.md")
    assert "Optional Packet Schema" in text
    assert "must not become a routine delivery gate" in text
    assert "Only when the user explicitly requests immutable audit handoff" in text
    assert "A locked packet is immutable" in text
    assert "changes require `packet-v002`" in text
    assert "cannot change a delivery KR without substantive outcome evidence" in text


def test_workflow_bootstrap_documents_local_boundary() -> None:
    text = read(WORKFLOW / "bootstrap.md")
    assert "local coordination layer" in text
    assert "`docs/workflow/` is not committed to GitHub by default" in text
    assert "`docs/workflow/` is not included in release packages by default" in text
    assert ".git/info/exclude" in text
    assert "repo workflow standard" in text
