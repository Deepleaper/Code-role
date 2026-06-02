# Packet Chain Audit

## Chain Summary / 链路摘要

- selected_chain / 选定链路: {{chain}} [packet_chain_evidence]
- official_upstream_packet / 官方上游 packet: {{manifest_path}} [packet_chain_evidence]
- strict_handoff_requested / 是否要求严格交接: true | false [packet_chain_evidence]
- chain_supports_review / 链路是否支持 Reviewer 判断: true | false [reviewer_judgment]

## Packet Consumption Audit / Packet 消费审计

| Role / 角色 | Packet / Packet | Status At Consumption / 消费时状态 | Consumption Status / 消费状态 | Lock State / 锁定状态 | Drift Check / 漂移检查 |
| --- | --- | --- | --- | --- | --- |
| {{role}} | {{manifest_path}} [packet_chain_evidence] | draft / ready_for_next_role / unknown [packet_chain_evidence] | accepted_as_input / traceability_only / rejected / unknown [packet_chain_evidence] | locked / draft_unlocked / not_required / unknown [packet_chain_evidence] | none / minor / major / unknown [reviewer_judgment] |

## Source Scope Consistency / Source Scope 一致性

| Source Scope / 来源范围 | Used By Reviewer / Reviewer 是否使用 | Consistency Result / 一致性结果 | Notes / 说明 |
| --- | --- | --- | --- |
| {{source_scope}} [packet_chain_evidence] | yes / no [reviewer_judgment] | consistent / partial / inconsistent / unknown [reviewer_judgment] | {{notes}} |

## Strict Handoff Status / 严格交接状态

- strict_handoff_check / 严格交接检查: not_requested | pass | fail | blocked [packet_chain_evidence]
- lock_requirement_reason / lock 要求理由: {{reason}} [packet_chain_evidence]
- structural_blocker / 结构性阻断: true | false [reviewer_judgment]

默认情况下，draft packet 经用户接受即可作为下游输入；只有用户明确要求 strict handoff 时，才要求 `ready_for_next_role=true` 和 `packet.lock.json`。

By default, a draft packet may be accepted by the user as downstream input. `ready_for_next_role=true` and `packet.lock.json` are required only when the user explicitly requests strict handoff.
