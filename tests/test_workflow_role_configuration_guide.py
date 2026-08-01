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
    assert "The remaining seven roles are professional execution roles" in text


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
    assert "local workflow assistance" in text
    assert "out of target-project GitHub commits and release packages" in text
    assert "Code-role source repository itself tracks these templates normally" in text


def test_role_configuration_guide_preserves_packet_and_boundary_rules() -> None:
    text = read(GUIDE)
    assert "handoff.manifest.json" in text
    assert "packet-vNNN" in text
    assert "`latest.json` is deprecated" in text
    assert "Default handoff does not require readiness conversion or packet lock" in text
    assert "A complete assignment starts immediately" in text
    assert "Chat is not the source of truth" in text
    assert "Product / PRD" in text
