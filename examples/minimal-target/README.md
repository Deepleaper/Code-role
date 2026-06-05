# Minimal Target Project Example / 最小目标项目示例

This example shows how Code-role should be initialized in a target project.

这个示例说明如何在目标项目中初始化 Code-role。

## Command / 初始化命令

Run from the Code-role repository:

在 Code-role 仓库中执行：

```bash
python scripts/init_project_workflow.py \
  --target "/path/to/Target Project" \
  --project-name "Target Project" \
  --initial-milestone workflow-bootstrap \
  --initial-chain research-only \
  --write
```

## Expected Local Files / 预期本地文件

The target project receives local workflow assistance:

目标项目会生成本地 workflow 辅助文件：

```text
code-role/
  README.md
  project-config.md
  role-instance-prompts/
    workflow-orchestrator.md
    researcher.md
    product-prd.md
    architect.md
    code-context.md
    implementer.md
    test-evaluator.md
    reviewer.md
  workflow/
    orchestrator/
      workflow-state.md
      milestone-registry.md
      decision-log.md
      final-packet-index.md
```

## Git Boundary / Git 边界

For target projects, generated `code-role/` folders are local operator assistance by default.

对于目标项目，生成的 `code-role/` 默认只是本地操作者辅助。

Default rule:

默认规则：

- Do not commit target-project `code-role/` output by default.
- Do not package it as product runtime content.
- Do not ship it in release artifacts.
- Keep normal product Git operations unchanged.

- 默认不要提交目标项目中的 `code-role/` 产物。
- 不要把它当作产品运行时内容。
- 不要把它打包进发布产物。
- 产品代码的 Git 操作仍按原项目规则执行。

## First Conversation / 第一次对话

Open the Workflow Orchestrator conversation and paste:

打开 Workflow Orchestrator / 项目经理对话，并粘贴：

```text
项目经理，执行 startup routine，恢复当前状态
```

The Orchestrator should restore state, ask for the real milestone when needed, and generate the next role startup message.

项目经理应恢复状态，在需要时询问真实 milestone，并生成下一角色启动消息。
