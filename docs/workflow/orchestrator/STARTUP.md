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
5. `docs/workflow/milestone-contract.md`
6. the `Authoritative packet` path recorded in `workflow-state.md`

If `workflow-state.md` has no authoritative packet, ask the user for:

- milestone
- milestone contract confirmation status
- chain type, if known
- current role
- packet manifest path

Do not infer the current packet by scanning for the newest file.

If `milestone-contract.md` is missing, draft, or incomplete, report `milestone_contract_check=fail` and ask the user to confirm business goal, delivery goal, success criteria, non-goals, scope, hard prohibitions, evidence requirements, correction policy, and closure rule before routing the first execution role.

## Recovery Output

After reading the required files, answer with:

1. current milestone
2. selected chain
3. milestone contract status
4. current authoritative packet
5. current final packet index status
6. packet status
7. `consumable_check=pass` or `consumable_check=fail`
8. current blocker
9. recommended next role
10. required user confirmations
11. workflow state files that need updates, if any

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
