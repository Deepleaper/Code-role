# PRD / 产品需求文档

## Background / 背景

- upstream input / 上游输入:
- milestone / 里程碑:
- current project context / 当前项目上下文:
- frontier references, if any / 外部前沿参考，如有:

## Milestone Alignment / 里程碑对齐

- business goal / 业务目标:
- product contribution / 产品贡献:
- success criteria / 成功标准:

## Users And Scenarios / 用户与场景

| User / 用户 | Scenario / 场景 | Problem / 问题 | Evidence Label / 证据标签 |
| --- | --- | --- | --- |
| <user> | <scenario> | <problem> | accepted_evidence |

## Goals / 目标

| Goal ID | Goal / 目标 | Source Label / 来源标签 | Confirmation / 确认状态 |
| --- | --- | --- | --- |
| G-001 | <goal> | user_confirmed_decision | confirmed |

## Product Scope / 产品范围

### Committed Scope / 当前承诺范围

| Scope ID | Scope Item / 范围项 | Evidence / 证据 | Acceptance Link / 验收链接 |
| --- | --- | --- | --- |
| S-001 | <scope item> | <accepted evidence> | AC-001 |

### Proposed Scope / 建议范围

| Scope ID | Scope Item / 范围项 | Source Label / 来源标签 | Confirmation Needed / 需确认 |
| --- | --- | --- | --- |
| S-PROP-001 | <scope item> | product_assumption | <user decision needed> |

## Functional Requirements / 功能需求

| Requirement ID | Requirement / 需求 | Linked Scope / 范围 | Acceptance Link / 验收 | Source Label / 来源标签 |
| --- | --- | --- | --- | --- |
| FR-001 | <requirement> | S-001 | AC-001 | accepted_evidence |

## Non-Functional Requirements / 非功能需求

| Requirement ID | Requirement / 需求 | Verification / 验证方式 | Source Label / 来源标签 |
| --- | --- | --- | --- |
| NFR-001 | <requirement> | <verification> | product_judgment |

## Dependencies And Constraints / 依赖与约束

- product dependencies / 产品依赖:
- project constraints / 项目约束:
- user-confirmed constraints / 用户确认约束:
- assumptions / 假设:

## Out Of Scope / 不做范围

See `non-goals.md`.

## Acceptance Mapping / 验收映射

Every committed functional requirement must link to an acceptance criterion.

每个 committed functional requirement 必须链接一个验收标准。

| Requirement ID | Acceptance ID | Verification Owner / 验证角色 |
| --- | --- | --- |
| FR-001 | AC-001 | Test Evaluator |

## Architect Handoff / 架构交接

- committed product boundaries / 已承诺产品边界:
- assumptions Architect must preserve / 架构师必须保留的假设:
- requirements Architect must not expand / 架构师不能擅自扩大的需求:
- open questions for Architect / 给架构师的问题:
