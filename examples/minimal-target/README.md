# Minimal Target Project Example / 最小目标项目示例

This example initializes the four-workstation goal loop in a target project.

这个示例在目标项目中初始化四工位目标闭环。

## Command / 初始化命令

Run from the Code-role repository:

在 Code-role 仓库中执行：

```bash
python scripts/init_loop_workflow.py "/path/to/Target Project" \
  --project-name "Target Project"
```

## Expected Local Files / 预期本地文件

```text
code-role/
  README.md
  START-HERE.md
  LOOP.md
  milestone-board.md
  project-config.md
  role-instance-prompts/
    project-manager.md
    product-strategy.md
    engineering.md
    independent-evaluation.md
  templates/
    assignment.md
    product-return.md
    engineering-return.md
    evaluation-return.md
    pm-decision.md
  work/
    README.md
```

## Git Boundary / Git 边界

For target projects, generated `code-role/` folders are local operator assistance by default.

对于目标项目，生成的 `code-role/` 默认只是本地操作者辅助。

- Do not commit target-project `code-role/` output by default.
- Do not package it as product runtime content.
- Do not ship it in release artifacts.
- Keep normal product Git operations unchanged.

The initializer records `code-role/` in local `.git/info/exclude`; it does not change the tracked `.gitignore`.

初始化器把 `code-role/` 写入本地 `.git/info/exclude`，不会修改仓库跟踪的 `.gitignore`。

## First Conversation / 第一次对话

Open a Project Manager conversation and use:

打开项目经理对话并使用：

```text
请读取 code-role/role-instance-prompts/project-manager.md，
然后根据 code-role/milestone-board.md 定义或恢复当前里程碑 OKR。
```

After the user accepts the OKR, Project Manager selects one exact failed evidence item keeping a KR at `0` and prints one copy-ready assignment. Paste that assignment into the selected workstation conversation. A valid assignment starts immediately.

用户确认 OKR 后，项目经理选择一个导致 KR 仍为 `0` 的精确失败证据，并输出一份可复制任务书。把任务书贴入对应工位对话，完整任务书即直接启动。
