from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_MAP = ROOT / "docs" / "workflow" / "source-map.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_source_map_covers_all_eight_roles() -> None:
    text = read(SOURCE_MAP)
    for section in [
        "Workflow Orchestrator",
        "Researcher",
        "Product / PRD",
        "Architect",
        "Code Context",
        "Implementer",
        "Test Evaluator",
        "Reviewer",
    ]:
        assert section in text


def test_source_map_hardens_high_risk_roles() -> None:
    text = read(SOURCE_MAP)
    assert "Historical packet scopes never accumulate into permanent restrictions" in text
    assert "does not need to predict every changed file" in text
    assert "Must not repair the candidate" in text
    assert "Must not implement fixes" in text
    assert "Must not implement fixes, change tests" in text
