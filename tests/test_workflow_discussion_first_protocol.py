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

    assert "discussion-first, not automation-first" in protocol
    assert "Every role conversation must point to that role's explicit output" in protocol
    assert "Except for Implementer after explicit approval" in protocol
    assert "discussion-first-protocol.md" in readme


def test_every_role_has_prompt_contract_and_scope_correction() -> None:
    for role_file in ROLE_FILES:
        text = read(role_file)
        assert "## Prompt Contract" in text, role_file
        assert "This role does:" in text, role_file
        assert "Inputs:" in text, role_file
        assert "Outputs:" in text, role_file
        assert "May write:" in text, role_file
        assert "Must not write:" in text, role_file
        assert "Conversation scope:" in text, role_file
        assert "All communication with this role must point" in text, role_file
        assert "outside" in text and "scope" in text, role_file
        assert "return to" in text, role_file


def test_non_implementer_roles_document_only_boundary() -> None:
    for role_file in NON_IMPLEMENTER_ROLE_FILES:
        text = read(role_file)
        assert "code" in text, role_file
        assert "Must not write:" in text, role_file

    workflow_readme = read(WORKFLOW / "README.md")
    assert "Every non-Implementer role produces documents only and does not change code" in workflow_readme
    assert "Implementer is the only role that may change approved project files" in workflow_readme


def test_implementer_requires_user_confirmed_start() -> None:
    implementer = read(WORKFLOW / "roles" / "implementer" / "ROLE.md")
    protocol = read(WORKFLOW / "discussion-first-protocol.md")

    assert "Orchestrator confirmation that implementation may start" in implementer
    assert "Stop for user confirmation before implementation start" in implementer
    assert "Implementer is the only role that may write approved project files" in protocol

