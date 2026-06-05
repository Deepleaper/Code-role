# Contributing / 贡献指南

Thanks for your interest in Code-role.

Code-role is a discussion-first local workflow template for controlling Codex-assisted software delivery. Contributions should strengthen role boundaries, milestone alignment, handoff quality, validation, documentation clarity, or target-project setup.

Code-role 是一个 discussion-first 的本地角色工作流模板。贡献应服务于角色边界、里程碑对齐、交接质量、校验能力、文档清晰度或目标项目初始化体验。

## Good Contributions / 推荐贡献

- Improve role instructions without making them more process-heavy.
- Make Orchestrator handoffs clearer and more milestone-focused.
- Improve packet templates, output standards, or validation tests.
- Improve bootstrap scripts and target-project setup.
- Clarify Git, network, release, and local-assistance boundaries.
- Add tests for workflow rules that must not regress.

## Out Of Scope / 不建议贡献

- Turning Code-role into an automatic code execution runner.
- Making strict packet locking the daily default.
- Adding speculative roles without a clear workflow need.
- Letting Orchestrator write professional conclusions for downstream roles.
- Making target-project `code-role/` folders product runtime or release artifacts by default.

## Pull Request Standard / PR 标准

Before submitting a pull request:

1. Keep the change narrow.
2. Explain the workflow problem being solved.
3. Preserve discussion-first execution.
4. Do not loosen Implementer write-scope rules.
5. Do not remove milestone-drift checks.
6. Run tests:

```bash
.venv/bin/python -m pytest -q
```

If you do not use a virtual environment, install test dependencies with:

```bash
python -m pip install -e ".[test]"
python -m pytest -q
```

## Language / 语言

English and Chinese are both acceptable. For user-facing workflow rules, bilingual wording is preferred when practical.
