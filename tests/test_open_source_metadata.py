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


def test_readme_exposes_workflow_diagram_and_example() -> None:
    readme = read(ROOT / "README.md")
    example = read(ROOT / "examples" / "minimal-target" / "README.md")

    assert "```mermaid" in readme
    assert "Workflow Orchestrator / 项目经理" in readme
    assert "R --> O" in readme
    assert "P --> O" in readme
    assert "A --> O" in readme
    assert "C --> O" in readme
    assert "I --> O" in readme
    assert "T --> O" in readme
    assert "V --> O" in readme
    assert "O --> R --> P --> A --> C --> I --> T --> V --> O" not in readme
    assert "Every professional role returns its binary completion block and packet to the Orchestrator." in readme
    assert "role_completion_status" in readme
    assert "Researcher -> Workflow Orchestrator review" in readme
    assert "Minimal target example" in readme
    assert "examples/minimal-target/README.md" in readme
    assert "Do not commit target-project `code-role/` output by default." in example
    assert "项目经理，执行 startup routine，恢复当前状态" in example
