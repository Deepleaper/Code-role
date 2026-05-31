# Workflow Bootstrap

This workflow is a local coordination layer by default.

It is designed to help one workspace coordinate role conversations without adding workflow control files to the product repository or release package.

## Default Boundary

Default rules:

- `docs/workflow/` is local workflow configuration.
- `docs/workflow/` is not committed to GitHub by default.
- `docs/workflow/` is not included in release packages by default.
- Workflow-only tests such as `tests/test_workflow_*.py` are local checks by default.
- Product repositories should commit product code and product docs, not local workflow control files, unless the team explicitly upgrades the workflow into a repo standard.

## Recommended Local Exclude

Use local git exclude:

```gitignore
docs/workflow/
tests/test_workflow_*.py
```

This belongs in:

```text
.git/info/exclude
```

Do not add these patterns to project `.gitignore` unless the team has agreed that the workflow is a shared repo convention.

## Bootstrap Options

Choose one:

1. Copy from a local workflow template folder into the workspace.
2. Use a local initialization script maintained outside the product repo.
3. If the team decides the workflow should be shared, explicitly promote it to a repo workflow standard and commit it intentionally.

## Promotion Rule

If a team wants to commit `docs/workflow/`, first update the boundary language:

- from `local coordination layer`
- to `repo workflow standard`

Then add repo-level CI and ownership rules intentionally.

Do not silently mix local workflow files into product release evidence.

