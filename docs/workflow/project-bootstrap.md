# Project Bootstrap

Project bootstrap turns a target repository into a Code-role-controlled workspace without manually writing every role prompt and state file.

Bootstrap creates configuration and navigation files only. It does not run any role, create execution packets, stage Git files, commit, push, or modify business source files.

## Inputs

Required inputs:

- target project path
- project name
- tracking policy: `repo-tracked` or `local-only`
- initial milestone
- initial chain
- external research default

The tracking policy is required because workflow files have a release boundary:

- `repo-tracked` means `code-role/` is repository governance infrastructure.
- `local-only` means `code-role/` is local coordination scratch space.

Both modes keep `code-role/` out of product runtime content and release artifacts unless explicitly approved.

## Fast Path

From the Code-role repository:

```bash
python scripts/init_project_workflow.py \
  --target "/path/to/Target Project" \
  --project-name "Target Project" \
  --tracking repo-tracked \
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

If `code-role/` is later staged, committed, or pushed, that is a separate Git operation requiring explicit user confirmation.
