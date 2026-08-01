from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_status_transition_protocol_exists_and_separates_acceptance() -> None:
    text = read(WORKFLOW / "status-transition-protocol.md")
    assert "Packet status is owned by the role that owns the packet" in text
    assert "Downstream roles must not rewrite upstream packet manifests" in text
    assert "`accepted` is not a valid upstream packet manifest status" in text
    assert "accepted_as_input" in text
    assert "packet.lock.json" in text


def test_packet_schema_uses_accepted_as_input_not_manifest_accepted() -> None:
    text = read(WORKFLOW / "packet-schema.md")
    assert "Valid packet manifest statuses" in text
    assert "`accepted` is not a packet manifest status for new packets" in text
    assert "\"consumption_status\": \"accepted_as_input\"" in text
    assert "downstream acceptance must not mutate the upstream manifest" in text


def test_handoff_protocol_forbids_upstream_acceptance_rewrite() -> None:
    text = read(WORKFLOW / "handoff-protocol.md")
    assert "Downstream consumption is recorded as `accepted_as_input`" in text
    assert "Default Handoff" in text
    assert "Do not ask the owning role to perform readiness conversion" in text
    assert "Downstream roles must not mutate upstream packet manifests" in text
