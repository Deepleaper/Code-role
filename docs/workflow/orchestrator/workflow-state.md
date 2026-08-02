# Workflow State / 当前交付状态

Workflow Orchestrator owns this compact current-state board. It is a pointer to accepted work, not a chronological workflow log.

项目经理维护这份精简的当前状态板。它指向已接受的工作和当前阻塞，不是流程流水账。

## Current Milestone / 当前里程碑

| Field | Value |
| --- | --- |
| Milestone | TBD |
| Objective accepted (0/1) | 0 |
| Objective | TBD |
| Target KR | TBD |
| Target KR pass (0/1) | 0 |
| Current failed evidence | TBD |
| Current evidence owner | TBD |
| Current work unit | TBD |
| Accepted primary artifact | none |
| Latest independent evidence | none |
| Current iteration / limit | 0 / TBD |
| Milestone pass (0/1) | 0 |

## Pending Human Decision / 待用户决策

| Decision | Why human input is required | Status |
| --- | --- | --- |
| none | none | none |

## Rules / 规则

- Record only current accepted state. **Do not append chronological workflow history.**
- `Current failed evidence` is the only default routing input.
- `Current evidence owner` is the professional role best able to repair or decide that evidence gap.
- `Accepted primary artifact` points to the latest substantive accepted deliverable, not a chat summary.
- Packet status, manifest readiness, and lock state are optional audit metadata and do not control routine routing.
- Do not infer current state by scanning for the newest file.
- Only independent evidence can change a delivery KR from `0` to `1`.
