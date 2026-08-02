from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"
ROLE_FILES = [
    WORKFLOW / "orchestrator" / "ROLE.md",
    WORKFLOW / "roles" / "researcher" / "ROLE.md",
    WORKFLOW / "roles" / "product-prd" / "ROLE.md",
    WORKFLOW / "roles" / "architect" / "ROLE.md",
    WORKFLOW / "roles" / "code-context" / "ROLE.md",
    WORKFLOW / "roles" / "implementer" / "ROLE.md",
    WORKFLOW / "roles" / "test-evaluator" / "ROLE.md",
    WORKFLOW / "roles" / "reviewer" / "ROLE.md",
]


NON_IMPLEMENTER_ROLE_FILES = [
    path for path in ROLE_FILES if "implementer" not in path.parts
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_discussion_first_protocol_exists_and_is_linked() -> None:
    protocol = read(WORKFLOW / "discussion-first-protocol.md")
    readme = read(WORKFLOW / "README.md")

    assert "It is not confirmation-first" in protocol
    assert "the role starts immediately" in protocol
    assert "no startup acknowledgement is sent" in protocol
    assert "discussion-first-protocol.md" in readme


def test_every_role_has_result_contract_and_role_boundary() -> None:
    for role_file in ROLE_FILES:
        text = read(role_file)
        assert "## Mission" in text, role_file
        assert "configured as its own role instance" in text, role_file
        assert "Do not switch roles inside this conversation" in text, role_file

    for role_file in ROLE_FILES[1:]:
        text = read(role_file)
        assert "## Result Contract" in text, role_file
        assert "one required primary professional artifact" in text, role_file
        assert "## Boundaries" in text, role_file
        assert "Do not narrate routine" in text, role_file
        assert "Do not recommend or choose the next role" in text, role_file


def test_non_implementer_roles_document_only_boundary() -> None:
    for role_file in NON_IMPLEMENTER_ROLE_FILES:
        text = read(role_file)
        assert "## Boundaries" in text, role_file

    workflow_readme = read(WORKFLOW / "README.md")
    assert "All non-Implementer roles produce governance or professional documents only" in workflow_readme
    assert "Implementer is the only role that changes target-project code under a valid assignment" in workflow_readme


def test_implementer_starts_from_complete_assignment_without_second_gate() -> None:
    implementer = read(WORKFLOW / "roles" / "implementer" / "ROLE.md")
    protocol = read(WORKFLOW / "discussion-first-protocol.md")

    assert "A complete assignment starts work immediately" in implementer
    assert "Do not send a startup acknowledgement" in implementer
    assert "Routine role routing, packet writing, local implementation" in protocol
    assert "do not require another Code-role confirmation" in protocol
