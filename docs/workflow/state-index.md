# State Index

The state index is an optional role onboarding shortcut. It helps a new role conversation find the current project state without relying on chat memory.

It is not authoritative.

Authoritative sources remain:

- Orchestrator state files
- role `handoff.manifest.json` files
- strict handoff `packet.lock.json` files, only when strict handoff was requested
- packet documents listed by manifests

If the state index conflicts with a manifest, strict lock, or Orchestrator state file, the authoritative source wins.

## Optional Location

In a target project:

```text
code-role/state-index/
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
```

## Role Index Contract

Each role index answers one question:

```text
If this role starts now, what should it read, what should it do, what must it not do, and what confirmation is still required?
```

Each role index must include:

- role responsibility from that role's `ROLE.md`
- current status in this project
- official upstream manifest, or the reason this role should not start
- traceability manifests
- must-read files with exact paths
- allowed read scope
- forbidden scope
- current gate / status
- residual risks
- next required confirmation
- authoritative sources

The role responsibility must come from `ROLE.md`, not from packet inference.

## Current Workflow Index

`current-workflow-index.md` summarizes:

- current milestone
- selected chain
- current authoritative packet
- completed packet chain
- current gate
- `quality_gate.status`, when available
- `final_acceptance`, when available
- residual risks
- recommended next confirmation

It should not introduce new conclusions. Every status, risk, or next step must be traceable to an Orchestrator state file or packet source.

## Refresh Rule

If generated, refresh the state index after:

- Orchestrator changes the active milestone or authoritative packet
- a role output is accepted as the current final version
- Reviewer produces a final gate

Refreshing the index is a documentation operation. It must not modify upstream packets or Orchestrator state.

## Release Boundary

`state-index/` is governance navigation. It is not product runtime content.

Do not include it in template indexes, customer delivery bundles, CLI payloads, or release artifacts.
