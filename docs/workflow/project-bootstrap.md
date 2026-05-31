# Project Bootstrap

Project bootstrap turns a target repository into a Code-role-controlled workspace without manually writing every role prompt and state file.

Bootstrap creates local configuration and navigation files only. It does not run any role, create execution packets, stage Git files, commit, push, or modify business source files.

Generated `code-role/` files are local-only target-project assistance. They are not part of the target project's product delivery and should not be committed or pushed with that project.

## Inputs

Required inputs:

- target project path
- project name
- initial milestone
- initial chain
- external research default

The tracking policy is fixed as `local-only`. If the target project is a Git repository, bootstrap adds `code-role/` to `.git/info/exclude` so the helper files remain available locally without entering the target project's Git history.

## Fast Path

From the Code-role repository:

```bash
python scripts/init_project_workflow.py \
  --target "/path/to/Target Project" \
  --project-name "Target Project" \
  --initial-milestone workflow-bootstrap \
  --initial-chain research-only \
  --write
```

Omit `--write` for a dry run.

## Files Created

Bootstrap creates:

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
  state-index/
    README.md
    current-workflow-index.md
    roles/
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
```

It intentionally does not create execution-role packet reports. Those must be created by the corresponding role instance after user confirmation.

When `.git/info/exclude` exists, bootstrap appends:

```text
code-role/
```

This keeps Code-role state local to the operator's workspace.

## After Bootstrap

1. Open the Workflow Orchestrator role instance.
2. Paste `code-role/role-instance-prompts/workflow-orchestrator.md`.
3. Confirm the first real milestone and selected chain.
4. Let Orchestrator route to the next role.
5. Open that role in a separate conversation and paste its role-instance prompt.

## Boundary

Bootstrap must not:

- infer a milestone from chat memory
- scan for the newest packet and treat it as authoritative
- create Researcher, Product / PRD, Architect, Code Context, Implementer, Test Evaluator, or Reviewer packets
- mark any packet `ready_for_next_role`
- run tests
- run Git staging, commit, or push
- modify product source files

Git operations remain normal project maintenance outside the role chain. Code-role may report Git-related facts, but it does not own or gate the target project's Git workflow.
