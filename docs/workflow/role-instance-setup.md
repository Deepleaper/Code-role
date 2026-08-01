# Role Instance Setup / 角色对话配置

## Two Projects / 两个项目

- **Role-configuration project:** this Code-role repository supplies contracts and templates.
- **Target code project:** the product repository receives local `code-role/` prompts, state, and work artifacts.

Do not run the Full Profile by switching roles inside one conversation. Create one configured Codex role instance per role.

## Initialize / 初始化

```bash
python scripts/init_project_workflow.py \
  --target "/absolute/path/to/project" \
  --project-name "Project Name" \
  --initial-milestone workflow-bootstrap \
  --initial-chain full-chain \
  --write
```

The initializer writes eight prompts under `code-role/role-instance-prompts/` and role-specific assignment/return templates under `code-role/templates/`.

## Configure Once / 一次配置

For each conversation, paste the matching role-instance prompt once. Do not require the role to restate its identity or boundary after every assignment.

## Run / 运行

1. Workflow Orchestrator defines and obtains acceptance for Objective and binary KRs.
2. It prints one complete role-specific assignment.
3. The user pastes the assignment to the selected configured role conversation.
4. The role starts immediately, writes its professional artifact, and returns one short result.
5. The user pastes the short result to Workflow Orchestrator.
6. Workflow Orchestrator reads the artifact and routes the substantive blocker owner.

No separate `开始`, readiness conversion, packet lock, or Git confirmation is part of normal role flow.

## Refresh / 刷新

Rerun the initializer with `--force --write` to refresh generated prompts and templates. Existing milestone contract, workflow state, final-output index, evaluation SOP, and professional packet reports are preserved.
