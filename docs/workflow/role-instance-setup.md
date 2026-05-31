# Role Instance Setup

Code-role is intended to be used as a role-configuration project.

The recommended current setup is:

```text
Code-role project
  -> stores workflow protocol files
  -> stores role definitions
  -> stores role packet outputs
  -> hosts one configured conversation per role

Target code project
  -> contains the product code being discussed or changed
  -> is read by research / architecture / code-context roles only within approved scope
  -> is written only by Implementer after explicit approval
```

Do not run the full workflow by switching roles inside one conversation. Each role should be configured and used as a separate role instance.

## Role Instance

A role instance is one configured Codex conversation dedicated to exactly one role.

Examples:

- `workflow-orchestrator` instance
- `researcher` instance
- `product-prd` instance
- `architect` instance
- `code-context` instance
- `implementer` instance
- `test-evaluator` instance
- `reviewer` instance

Each instance reads its own `ROLE.md` and follows only that role's prompt contract.

## Required Per-Role Configuration

Each role instance should be configured with:

- the role's `ROLE.md`
- `docs/workflow/README.md`
- `docs/workflow/discussion-first-protocol.md`
- `docs/workflow/handoff-protocol.md`
- `docs/workflow/packet-schema.md`
- `docs/workflow/source-map.md`
- any upstream `handoff.manifest.json` explicitly provided for the milestone
- the target project path, when that role needs to inspect or modify the product project

The role instance must not infer upstream input from chat memory or by scanning for the newest packet.

## Conversation Rule

Each role instance has one job: produce that role's explicit output.

If the conversation moves away from that output, the role must correct it:

1. State that the request is outside the current role's scope.
2. Name the role that should handle the request.
3. Return to the current role's expected output.

## Suggested Setup Flow

1. Clone `Deepleaper/Code-role` into a local Code-role project.
2. Bootstrap the target project with `scripts/init_project_workflow.py`.
3. Create one Codex role instance for `workflow-orchestrator`.
4. Paste `code-role/role-instance-prompts/workflow-orchestrator.md` into that instance.
5. Create each execution role instance only when Orchestrator routes to it.
6. Paste that role's generated prompt from `code-role/role-instance-prompts/`.
7. Let the role read its `code-role/state-index/roles/<role>.md` entry and the explicit upstream manifest.
8. Let each role write only its own packet output.
9. Let Implementer write target project files only after the packet chain and user confirmation allow implementation.

The generated prompts reduce setup friction. They do not replace role `ROLE.md` files, packet manifests, or Orchestrator routing.

## Fast Bootstrap

Use the bootstrap script from the Code-role repository:

```bash
python scripts/init_project_workflow.py \
  --target "/path/to/Target Project" \
  --project-name "Target Project" \
  --write
```

Omit `--write` to preview the files. The script creates local-only project config, role-instance prompts, Orchestrator state files, and a non-authoritative state index. It also adds `code-role/` to `.git/info/exclude` when that target file exists. It does not create execution packets, mark readiness, stage files, commit, or push.

See `project-bootstrap.md`, `state-index.md`, and `git-operation-policy.md`.

## Target Project Handling

The target project should be provided as an explicit path in the milestone or role prompt.

Non-Implementer roles may inspect target project files only within source-map and packet-approved scope.

Implementer may modify target project files only when:

- Orchestrator confirms implementation may start
- upstream packets are consumable
- the target project path is explicit
- the approved file scope is explicit
- the user confirms implementation start

## Embedded Workflow Alternative

Some teams may choose to copy `docs/workflow/` into the target code project.

That is allowed, but it is not the only supported model. If embedded in the target project, follow `bootstrap.md` and decide whether workflow files stay local-only or become a committed repo standard.

For the current Code-role usage model, prefer the separate role-configuration project.
