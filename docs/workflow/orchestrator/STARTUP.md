# Orchestrator Startup Routine

Trigger phrase:

```text
项目经理，执行 startup routine，恢复当前状态
```

When the user sends this phrase, the Orchestrator must recover state from files before answering.

## Required Reads

Read these files in order:

1. `docs/workflow/orchestrator/workflow-state.md`
2. `docs/workflow/orchestrator/milestone-registry.md`
3. `docs/workflow/orchestrator/decision-log.md`
4. `docs/workflow/orchestrator/final-packet-index.md`
5. the `Authoritative packet` path recorded in `workflow-state.md`

If `workflow-state.md` has no authoritative packet, ask the user for:

- milestone
- chain type, if known
- current role
- packet manifest path

Do not infer the current packet by scanning for the newest file.

## Recovery Output

After reading the required files, answer with:

1. current milestone
2. selected chain
3. current authoritative packet
4. current final packet index status
5. packet status
6. `consumable_check=pass` or `consumable_check=fail`
7. current blocker
8. recommended next role
9. required user confirmations
10. workflow state files that need updates, if any

## Boundaries

The startup routine must not:

- write research
- write PRD
- write architecture
- write code
- write tests
- rewrite upstream packet manifests
- approve state transitions for the user
- start Implementer
- call provider APIs, authenticated/private resources, or external services that mutate state
- use network research without declaring purpose and source types first

The startup routine is a recovery step, not an execution step.
