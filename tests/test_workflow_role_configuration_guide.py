from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "workflow" / "role-configuration-guide.md"
README = ROOT / "docs" / "workflow" / "README.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_role_configuration_guide_exists_and_is_linked() -> None:
    assert GUIDE.exists()
    assert "role-configuration-guide.md" in read(README)


def test_role_configuration_guide_defines_eight_configured_roles() -> None:
    text = read(GUIDE)
    for role_id in [
        "workflow-orchestrator",
        "researcher",
        "product-prd",
        "architect",
        "code-context",
        "implementer",
        "test-evaluator",
        "reviewer",
    ]:
        assert f"`{role_id}`" in text
    assert "The remaining seven roles are execution roles" in text


def test_role_configuration_guide_includes_role_setup_details() -> None:
    text = read(GUIDE)
    for heading in [
        "### Goal",
        "### Reads",
        "### Writes",
        "### Must Not",
        "### Confirmation Required",
        "### Downstream Handoff",
    ]:
        assert heading in text
    assert "Shared Initialization Prompt" in text
    assert "Day-One Setup Order" in text
    assert "Role 1: Workflow Orchestrator" in text
    assert "Role 8: Reviewer" in text
    assert "Repository / Publishing Boundary" in text
    assert "keep `docs/workflow/` out of GitHub commits" in text
    assert "keep `docs/workflow/` out of release packages" in text
    assert "bootstrap `docs/workflow/` from a local template folder or local initialization script" in text
    assert "not part of the execution packet chain" in text


def test_role_configuration_guide_preserves_packet_and_boundary_rules() -> None:
    text = read(GUIDE)
    assert "handoff.manifest.json" in text
    assert "packet-vNNN" in text
    assert "latest.json" in text
    assert "Do not let a downstream role consume `draft`" in text
    assert "Chat is not the source of truth" in text
    assert "Product / PRD" in text
