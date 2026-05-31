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


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_role_instance_setup_doc_exists_and_defines_two_project_model() -> None:
    setup = read(WORKFLOW / "role-instance-setup.md")
    readme = read(ROOT / "README.md")
    workflow_readme = read(WORKFLOW / "README.md")

    assert "role-configuration project" in setup
    assert "Target code project" in setup
    assert "Do not run the full workflow by switching roles inside one conversation" in setup
    assert "one configured Codex role instance per role" in readme
    assert "role-instance-setup.md" in readme
    assert "Role Instance Setup" in workflow_readme


def test_every_role_declares_separate_role_instance_boundary() -> None:
    for role_file in ROLE_FILES:
        text = read(role_file)
        assert "configured as its own role instance" in text, role_file
        assert "Do not switch roles inside this conversation" in text, role_file
        assert "route the user to the correct role instance" in text, role_file


def test_product_docs_describe_role_instance_usage_model() -> None:
    zh_prd = read(ROOT / "docs" / "product" / "prd.zh-CN.md")
    en_prd = read(ROOT / "docs" / "product" / "prd.md")

    assert "每个角色分别配置一个独立角色实例" in zh_prd
    assert "不做一个对话内的多角色自动切换" in zh_prd
    assert "separate configured role instances" in en_prd
    assert "Switching through multiple roles inside one conversation" in en_prd

