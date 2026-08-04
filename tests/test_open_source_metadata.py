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
        ROOT / "ROADMAP.md",
        ROOT / "CHANGELOG.md",
        ROOT / ".github" / "workflows" / "tests.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "bug-report.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "workflow-feedback.yml",
        ROOT / "examples" / "README.md",
        ROOT / "examples" / "minimal-target" / "README.md",
        ROOT / "examples" / "minimal-goal-loop" / "README.md",
        ROOT / "assets" / "code-role-social-preview.svg",
        ROOT / "assets" / "code-role-social-preview.png",
        ROOT / "docs" / "promotion" / "LAUNCH-KIT.md",
        ROOT / "docs" / "promotion" / "STAR-GROWTH-PLAN.md",
        ROOT / "docs" / "promotion" / "TWO-CASE-LAUNCH-STORY.md",
        ROOT / "docs" / "case-studies" / "README.md",
        ROOT / "docs" / "case-studies" / "deepbrain.md",
        ROOT / "docs" / "case-studies" / "leaper-agent.md",
    ]
    missing = [path for path in expected if not path.exists()]
    assert not missing


def test_public_entry_points_are_actionable() -> None:
    readme = read(ROOT / "README.md")
    social_preview = read(ROOT / "assets" / "code-role-social-preview.svg")
    walkthrough = read(ROOT / "examples" / "minimal-goal-loop" / "README.md")
    launch_kit = read(ROOT / "docs" / "promotion" / "LAUNCH-KIT.md")
    growth_plan = read(ROOT / "docs" / "promotion" / "STAR-GROWTH-PLAN.md")

    assert "60-Second Start / 60 秒启动" in readme
    assert "What Makes It Different / 核心差异" in readme
    assert "GitHub Discussions" in readme
    assert "Complete Minimal Goal Loop / 四工位完整闭环示例" in walkthrough
    assert 'width="1280"' in social_preview
    assert 'height="640"' in social_preview
    assert "Show HN" in launch_kit
    assert "Product Hunt" in launch_kit
    assert "Never buy stars." in growth_plan


def test_real_cases_preserve_private_project_claim_boundaries() -> None:
    readme = read(ROOT / "README.md")
    deepbrain = read(ROOT / "docs" / "case-studies" / "deepbrain.md")
    leaper_agent = read(ROOT / "docs" / "case-studies" / "leaper-agent.md")
    case_index = read(ROOT / "docs" / "case-studies" / "README.md")

    assert "Real Project Cases / 真实项目案例" in readme
    assert "DeepBrain memory runtime" in readme
    assert "Leaper Agent enterprise runtime" in readme
    assert "Both source repositories are private." in case_index
    assert "Milestone pass | `0`" in deepbrain
    assert "Reviewer route allowed | `0`" in deepbrain
    assert "production ready = 0" in deepbrain
    assert "Historical target pass | `0`" in leaper_agent
    assert "Current-model interpretation" in leaper_agent
    assert "current code-role standard does not route test evaluator before a runnable candidate" in leaper_agent.lower()
    assert "does not claim that Leaper Agent already beats Hermes" in leaper_agent


def test_social_preview_png_meets_github_dimensions() -> None:
    preview = ROOT / "assets" / "code-role-social-preview.png"
    data = preview.read_bytes()

    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    assert (width, height) == (1280, 640)
    assert len(data) < 1_000_000


def test_readme_exposes_both_supported_profiles() -> None:
    readme = read(ROOT / "README.md")
    example = read(ROOT / "examples" / "minimal-target" / "README.md")

    assert "```mermaid" in readme
    assert "Minimal Profile / 四角色最小版" in readme
    assert "Full Profile / 八角色完整版" in readme
    assert "Neither profile is deprecated" in readme
    assert "scripts/init_loop_workflow.py" in readme
    assert "scripts/init_project_workflow.py" in readme
    assert "one Objective and one KR set" in readme
    assert "Product Contract for every existing KR" in readme
    assert "only Engineering decomposes `STEP-1...STEP-N` execution stages" in readme
    assert "Product Strategy" in readme
    assert "Engineering" in readme
    assert "Independent Evaluation" in readme
    assert "Software delivery uses a fixed dependency order" in readme
    assert "Workflow Orchestrator" in readme
    assert "Researcher" in readme
    assert "Architect" in readme
    assert "Code Context" in readme
    assert "Implementer" in readme
    assert "Test Evaluator" in readme
    assert "Reviewer" in readme
    assert "partial_pass" in readme
    assert "Minimal target example" in readme
    assert "examples/minimal-target/README.md" in readme
    assert "Do not commit target-project `code-role/` output by default." in example
    assert "完整项目 OKR" in example
    assert "只有工程可以拆分 STEP" in example


def test_product_docs_define_minimal_and_full_profiles() -> None:
    english_prd = read(ROOT / "docs" / "product" / "prd.md")
    chinese_prd = read(ROOT / "docs" / "product" / "prd.zh-CN.md")
    html = read(
        ROOT / "docs" / "product" / "code-role-workflow-guide.zh-CN.html"
    )
    full_profile = read(ROOT / "docs" / "workflow" / "README.md")

    assert "Minimal Profile" in english_prd
    assert "Full Profile" in english_prd
    assert "四角色最小版" in chinese_prd
    assert "八角色完整版" in chinese_prd
    assert "四角色最小版" in html
    assert "八角色完整版" in html
    assert "Full Profile: Eight-Role Workflow" in full_profile
    assert "Legacy Eight-Role Profile" not in read(ROOT / "README.md")
    assert "本八角色 packet 工作流仅为兼容" not in full_profile
