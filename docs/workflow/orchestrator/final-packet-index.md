# Accepted Final Outputs / 已接受最终产物

This optional pointer table records each role's current accepted primary artifact for the active milestone. The historical filename is retained for compatibility; this is not a packet-readiness gate or history log.

本可选指针表记录当前 milestone 中每个角色已接受的主交付物。文件名仅为兼容保留，它不是 packet readiness 门禁，也不是历史日志。

## Current Milestone Anchor / 当前里程碑锚点

| Field | Value |
| --- | --- |
| Milestone | TBD |
| Objective | TBD |
| Complete MKR set | TBD |
| Complete PKR set | TBD |
| Non-goals | TBD |
| Claim boundary | TBD |
| Anchor source | user_input / milestone_contract / unknown |

## Accepted Primary Artifacts / 已接受主产物

| Role | Accepted primary artifact | Work-unit pass (0/1) | Evidence note |
| --- | --- | ---: | --- |
| workflow-orchestrator | milestone-contract.md, workflow-state.md, applicable evaluation contract | 0 | current control artifacts |
| researcher | none | 0 | none |
| product-prd | none | 0 | none |
| architect | none | 0 | none |
| code-context | none | 0 | none |
| implementer | none | 0 | none |
| test-evaluator | none | 0 | none |
| reviewer | none | 0 | none |

## Update Rule / 更新规则

- Update a row only after Workflow Orchestrator reads the primary artifact and applies the assignment's binary acceptance checks.
- Replace the pointer when a newer artifact is accepted; do not append chronology.
- A role not needed for the milestone remains `none`; no chain status is required.
- Missing chat fields, manifest readiness, or packet locks do not invalidate sufficient evidence.
- This index cannot change an MKR, PKR, delivery stage, or milestone status.

Reviewer, when required, audits the current accepted artifacts listed here, MKR-to-PKR-to-EKR traceability, mandatory stage order, and the compact Orchestrator state against the original milestone contract.
