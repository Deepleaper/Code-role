from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_MAP = ROOT / "docs" / "workflow" / "source-map.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_source_map_covers_all_eight_roles() -> None:
    text = read(SOURCE_MAP)
    for section in [
        "Orchestrator Read Scope",
        "Researcher Read Scope",
        "Product / PRD Read Scope",
        "Architect Read Scope",
        "Code Context Read Scope",
        "Implementer Read Scope",
        "Test Evaluator Read Scope",
        "Reviewer Read Scope",
    ]:
        assert section in text


def test_source_map_hardens_high_risk_roles() -> None:
    text = read(SOURCE_MAP)
    assert "The Implementer must not begin from chat-only instruction" in text
    assert "Orchestrator must approve Implementer start" in text
    assert "The Test Evaluator must not modify code or tests" in text
    assert "The Reviewer must not implement fixes" in text
    assert "The Code Context role must not modify code, tests" in text

