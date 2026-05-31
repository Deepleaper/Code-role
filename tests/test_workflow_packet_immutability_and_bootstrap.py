from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_packet_schema_defines_immutability_rules() -> None:
    text = read(WORKFLOW / "packet-schema.md")
    assert "Packet Immutability Rules" in text
    assert "`packet-v001` may be edited only while its manifest status is `draft`" in text
    assert "Once a packet status becomes `ready_for_next_role`, do not edit" in text
    assert "`accepted` is not a packet manifest status for new packets" in text
    assert "create the next version" in text
    assert "Historical packets must remain immutable" in text


def test_workflow_bootstrap_documents_local_boundary() -> None:
    text = read(WORKFLOW / "bootstrap.md")
    assert "local coordination layer" in text
    assert "`docs/workflow/` is not committed to GitHub by default" in text
    assert "`docs/workflow/` is not included in release packages by default" in text
    assert ".git/info/exclude" in text
    assert "repo workflow standard" in text
