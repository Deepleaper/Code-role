# Decision Log / 决策日志

Product decisions must distinguish user-confirmed decisions, product proposals, assumptions, and blockers.

产品决策必须区分用户确认、产品建议、产品假设和阻塞项。

| Decision / 决策 | Status / 状态 | Source Label / 来源标签 | Evidence / 证据 | Alternatives Rejected / 被拒方案 | User Confirmation Needed / 是否需用户确认 | Downstream Impact / 下游影响 | Notes / 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <decision> | proposed | product_judgment | <evidence> | <alternative> | yes | Architect needs boundary clarity | <notes> |

## Status Values / 状态值

- `proposed`: product recommendation not yet confirmed / 产品建议，尚未确认
- `user_confirmed`: explicitly confirmed by user / 用户已明确确认
- `accepted`: accepted for this packet scope / 本 packet 范围内接受
- `rejected`: explicitly rejected / 已拒绝
- `blocked`: cannot proceed without input / 无输入无法继续
- `product_assumption`: temporary assumption, not confirmed scope / 临时假设，不是确认范围

## Source Label Values / 来源标签

- `accepted_evidence`
- `frontier_reference`
- `product_judgment`
- `user_confirmed_decision`
- `product_assumption`
- `unknown_or_blocker`

## Confirmation Rule / 确认规则

Major product judgment without user confirmation must remain `proposed` or `product_assumption`.

没有用户确认的重大产品判断，只能保持为 `proposed` 或 `product_assumption`。
