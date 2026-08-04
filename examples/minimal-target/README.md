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
  DIALOGUE-CONTROL.md
  OKR-STANDARD.md
  LOOP.md
  milestone-board.md
  project-config.md
  role-instance-prompts/
    project-manager.md
    product-strategy.md
    engineering.md
    independent-evaluation.md
  templates/
    product-assignment.md
    engineering-assignment.md
    evaluation-assignment.md
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
然后根据 code-role/milestone-board.md 定义或恢复当前项目 OKR。
```

After the user accepts the complete Project OKR, Project Manager sends the same KR set to Product Strategy. Product Strategy adds one complete Product Contract under those KRs without creating another OKR. Project Manager then sends the accepted Project OKR and Product Contract to Engineering. Engineering alone decomposes implementation into STEP stages and produces the complete runnable candidate. Independent Evaluation starts only after that candidate gate passes.

用户确认完整项目 OKR 后，项目经理把同一组 KR 交给产品策略；产品策略在这些 KR 下补全产品契约，不创建第二套 OKR；项目经理再把已接受的项目 OKR 与 Product Contract 交给工程；只有工程可以拆分 STEP 并产出完整可运行候选物。候选物门禁通过后才能启动独立评估。
