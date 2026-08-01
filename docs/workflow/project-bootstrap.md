# Project Bootstrap / 项目初始化

Bootstrap creates local Full Profile role-control files. It does not run roles, create professional packets, modify business files, or perform Git operations.

## Command / 命令

```bash
python scripts/init_project_workflow.py \
  --target "/path/to/Target Project" \
  --project-name "Target Project" \
  --initial-milestone workflow-bootstrap \
  --initial-chain full-chain \
  --write
```

Omit `--write` for dry run. Add `--force` to refresh generated prompts and templates. Durable milestone state and evaluation SOP files are preserved.

## Generated Files / 生成文件

```text
code-role/
  README.md
  DIALOGUE-CONTROL.md
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
  templates/
    <role>-assignment.md
    <role>-return.md
  workflow/
    orchestrator/
      workflow-state.md
      milestone-contract.md
      final-packet-index.md
    evaluation/
      evaluation-sop.md
```

Optional `--with-state-index` creates non-authoritative navigation only.

## Local Boundary / 本地边界

Generated `code-role/` is local target-project assistance, not product runtime or release content. If `.git/info/exclude` exists, bootstrap adds `code-role/` there without modifying tracked `.gitignore`.

## After Bootstrap / 初始化后

1. Configure eight conversations once from generated role prompts.
2. Open Workflow Orchestrator and accept one Objective with binary KRs.
3. Paste its first complete role-specific assignment to the selected role.
4. Continue with one assignment and one short return per role iteration.
