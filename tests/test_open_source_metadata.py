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
    ]
    missing = [path for path in expected if not path.exists()]
    assert not missing
