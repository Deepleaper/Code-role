# Handoff Protocol / 交接协议

## Default Handoff / 默认交接

The default Full Profile handoff has four steps:

1. Workflow Orchestrator issues one complete role-specific assignment.
2. The role starts immediately and writes the assignment's one primary professional artifact.
3. The role sends one short role-specific return.
4. Workflow Orchestrator reads the packet, applies the required checks, and issues one decision.

默认交接不包含启动确认、等待“开始”、readiness 转换或 packet lock。

Versioned `packet-vNNN/` directories remain available for provenance. `handoff.manifest.json` may record the exact assignment-named upstream artifact versions actually consumed; it does not prescribe a fixed predecessor, successor, or multi-file completion checklist.

Downstream consumption is recorded as `accepted_as_input` in the downstream manifest. Downstream roles must not mutate upstream packet manifests.

## Professional Authority / 专业权威

The assignment-named primary professional artifact and its referenced evidence are authoritative. `handoff.manifest.json` is optional provenance metadata. The short return is navigation only.

Workflow Orchestrator must not reject sufficient evidence solely because:

- return fields are missing or reordered;
- packet status is `draft`;
- `ready_for_next_role` is false;
- `packet.lock.json` is absent;
- the role did not recommend a next role.

## Acceptance / 验收

Project Manager checks milestone alignment and every assigned substantive check. It records `work_unit_pass=0|1`, the one current failed evidence item, its evidence, and its owner.

An incomplete assignment routes to the owner of the failed check. It does not automatically return to the same role.

## Strict Handoff / 严格交接

When the user explicitly requests immutable audit handoff, packet status transition and lock rules from [Status Transition Protocol](status-transition-protocol.md) apply. Strict handoff must not be introduced during ordinary delivery or used to delay a substantive next step.

Do not ask the owning role to perform readiness conversion in default handoff.

## Human Gates / 人工闸门

No user confirmation is required between ordinary role handoffs after Objective, KRs, and current assignment scope are accepted. Ask the user only for decisions defined by the shared dialogue-control contract.

## Forbidden Handoff Work / 禁止交接工作

- format-only revision;
- readiness-only revision;
- lock-only revision;
- repeated read/write/forbidden recitation;
- role-generated next-role startup message;
- Orchestrator rewriting upstream professional conclusions;
- treating Git add/commit/push as Code-role gates.
