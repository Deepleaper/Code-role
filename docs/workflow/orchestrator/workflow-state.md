# Workflow State / 当前交付状态

Workflow Orchestrator owns this compact current-state board. It is a pointer to accepted work, not a chronological workflow log.

项目经理维护这份精简的当前状态板。它指向已接受的工作和当前阻塞，不是流程流水账。

## Current Milestone / 当前里程碑

| Field | Value |
| --- | --- |
| Milestone | TBD |
| Objective accepted (0/1) | 0 |
| Objective | TBD |
| Delivery stage | milestone_definition |
| Complete Milestone OKR accepted (0/1) | 0 |
| Complete MKR table | none |
| Complete Product OKR accepted (0/1) | 0 |
| Accepted Product OKR | none |
| Accepted architecture contract | none |
| Accepted code-context map | none |
| Accepted Engineering plan | none |
| Runnable candidate | none |
| Candidate ready for independent evaluation (0/1) | 0 |
| Independent evaluation executed (0/1) | 0 |
| Latest independent evidence | none |
| Current blocking contract | complete Milestone OKR |
| Current stage owner | workflow-orchestrator |
| Candidate iteration / limit | 0 / TBD |
| Milestone pass (0/1) | 0 |

## Pending Human Decision / 待用户决策

| Decision | Why human input is required | Status |
| --- | --- | --- |
| none | none | none |

## Rules / 规则

- Record only current accepted state. **Do not append chronological workflow history.**
- `Delivery stage` is the only default routing input. Allowed software-delivery stages are `milestone_definition`, `research_and_product_definition`, `architecture_and_code_context`, `engineering_delivery`, `independent_evaluation`, `review_when_required`, and `closure`.
- `Current blocking contract` names the substantive global contract that keeps the current stage from passing.
- Product, Architecture, and Code Context pointers represent complete accepted global artifacts, not one-MKR slices.
- Engineering owns EKR detail; do not duplicate `EKR-*` activity in this state.
- `Candidate ready for independent evaluation` can become `1` only when the complete runnable candidate and reproducibility evidence exist.
- Independent Evaluation cannot become the active stage before candidate readiness is `1`.
- Packet status, manifest readiness, and lock state are optional audit metadata and do not control routine routing.
- Do not infer current state by scanning for the newest file.
- Only independent evidence can change an MKR from `0` to `1`.
