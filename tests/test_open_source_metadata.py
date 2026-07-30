from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_open_source_metadata_is_consistent() -> None:
    readme = read(ROOT / "README.md")
    pyproject = read(ROOT / "pyproject.toml")
    license_text = read(ROOT / "LICENSE")

    assert "MIT License" in license_text
    assert "license = { file = \"LICENSE\" }" in pyproject
    assert "Code-role is released under the [MIT License](LICENSE)." in readme
    assert "No license has been declared yet" not in readme
    assert "Proprietary" not in pyproject


def test_open_source_supporting_files_exist() -> None:
    expected = [
        ROOT / "CONTRIBUTING.md",
        ROOT / "SECURITY.md",
        ROOT / ".github" / "workflows" / "tests.yml",
        ROOT / "examples" / "README.md",
        ROOT / "examples" / "minimal-target" / "README.md",
    ]
    missing = [path for path in expected if not path.exists()]
    assert not missing


def test_readme_exposes_goal_loop_diagram_and_example() -> None:
    readme = read(ROOT / "README.md")
    example = read(ROOT / "examples" / "minimal-target" / "README.md")

    assert "```mermaid" in readme
    assert "Project Manager selects one KR=0" in readme
    assert "Product Strategy" in readme
    assert "Engineering" in readme
    assert "Independent Evaluation" in readme
    assert "There is no fixed four-role chain" in readme
    assert "valid assignment starts immediately" in readme.lower()
    assert "partial_pass" in readme
    assert "manual copy-ready transport" in readme
    assert "Minimal target example" in readme
    assert "examples/minimal-target/README.md" in readme
    assert "Do not commit target-project `code-role/` output by default." in example
    assert "完整任务书即直接启动" in example
