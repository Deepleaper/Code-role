# Orchestrator 下一角色交接模板 / Next Role Handoff Template

Orchestrator 使用这个模板启动下一角色。只要 Orchestrator 明确判断可以进入下一角色，就必须在回复里直接贴出这段可复制文本。

The Orchestrator uses this template when starting the next role. When Orchestrator explicitly allows the next role to start, it must paste this copy-ready message directly in its response.

这是一份 milestone handoff brief，不是 workflow 教程，也不是专业任务重写。

This message is a milestone handoff brief, not a workflow tutorial and not a rewrite of the professional task.

目标角色自己的 prompt、`ROLE.md` 和 output standard 已经定义了专业职责、边界和输出格式。

The target role's own prompt, `ROLE.md`, and output standard already define professional responsibility, boundaries, and output format.

Orchestrator 只说明：当前 milestone、项目经理审阅结论、权威上游输入、边界和启动方式。

The Orchestrator states only the current milestone, project-manager review result, authoritative upstream input, boundaries, and start protocol.

专业内容以上游 packet 为准，不以 Orchestrator 本消息为准。

Professional content comes from the upstream packet, not from this Orchestrator message.

```text
你是 {PROJECT_NAME} 项目的 {NEXT_ROLE} 角色。
You are the {NEXT_ROLE} role for {PROJECT_NAME}.

请先读取你的 role-instance prompt 和 workflow protocol。
First read your role-instance prompt and workflow protocol.

这些文件已经定义了你的职责、边界和输出格式。
Those files already define your responsibility, boundary, and output format.

本消息只提供项目经理审阅结论、权威上游输入和本轮边界。
This message provides only the project-manager review result, authoritative upstream input, and this round's boundaries.

一、当前 milestone / Current Milestone

milestone:
{MILESTONE_NAME}

chain:
{CHAIN_TYPE}

本 milestone 的业务目标 / Milestone business goal:
{MILESTONE_BUSINESS_GOAL}

本 milestone 的交付目标 / Milestone delivery goal:
{MILESTONE_DELIVERY_GOAL}

本 milestone 的成功标准 / Milestone success criteria:
{MILESTONE_SUCCESS_CRITERIA}

明确不做 / Non-goals:
{MILESTONE_NON_GOALS}

硬禁止项 / Hard prohibitions:
{MILESTONE_HARD_PROHIBITIONS}

milestone contract / 里程碑契约:
{MILESTONE_CONTRACT_PATH}

二、项目经理审阅结论 / Project Manager Review Result

上游角色 / Upstream role:
{UPSTREAM_ROLE}

上游产出审阅结论 / Upstream output review result:
{UPSTREAM_REVIEW_RESULT}

milestone 对齐结果 / Milestone alignment result:
{MILESTONE_ALIGNMENT_RESULT}

上游角色完成状态 / Upstream role completion status:
{UPSTREAM_ROLE_COMPLETION_STATUS_1_OR_0}

上游完成条件计数 / Upstream completion condition count:
{UPSTREAM_COMPLETION_CONDITIONS_MET}/{UPSTREAM_COMPLETION_CONDITIONS_TOTAL}

上游未满足完成条件 / Upstream unmet completion conditions:
{UPSTREAM_UNMET_COMPLETION_CONDITIONS_OR_NONE}

如有残余风险 / Residual risk, if any:
{RESIDUAL_RISK_OR_NONE}

是否允许进入本角色 / Whether this role may start:
{HANDOFF_DECISION}

路由规则 / Routing rule:

- 只有当上游 `role_completion_status=1`、完成条件计数相等、未满足条件为 `none` 时，才能把上游产出作为完成态交给本角色。
- 如果上游 `role_completion_status=0`，本角色不能把它当作完成输入；必须记录阻塞并回到 Orchestrator。

- The upstream packet may be consumed as completed input only when `role_completion_status=1`, completion counts match, and unmet conditions are `none`.
- If upstream `role_completion_status=0`, this role must not treat it as completed input. Record the blocker and return to Orchestrator.

三、权威上游输入 / Authoritative Upstream Input

请消费以下上游 packet / Consume this upstream packet:
{AUTHORITATIVE_UPSTREAM_PACKET}

上游输入状态 / Upstream status:
{UPSTREAM_STATUS}

用户已接受该上游输入用于本轮轻量交接 / User accepted this upstream input for lightweight handoff:
{USER_ACCEPTED_UPSTREAM_FOR_HANDOFF}

权威规则 / Authority rule:

- 专业判断、事实、范围和风险以上游 packet 及其列出的文档为准。
- 本消息只提供路由和边界，不替代上游专业产出。
- 如果本消息与上游 packet 冲突，先记录冲突并请 Orchestrator 澄清。

- Professional judgment, facts, scope, and risks come from the upstream packet and its listed documents.
- This message provides routing and boundaries only. It does not replace the upstream professional output.
- If this message conflicts with the upstream packet, record the conflict and ask Orchestrator to clarify.

如果你发现上游输入不足，请只记录缺口，不要切换角色，不要自行补做其他角色工作。
If upstream input is insufficient, record the gap only. Do not switch roles or complete another role's work yourself.

四、你这个角色的执行要求 / Execution Requirement For This Role

请按你自己的 `ROLE.md` 和 output standard 消费上游 packet，并产出本角色 packet。

Use your own `ROLE.md` and output standard to consume the upstream packet and produce this role's packet.

你需要自己从上游 packet 中提取本角色应回答的专业问题。

You must derive this role's professional questions from the upstream packet yourself.

不要让 Orchestrator 的简短 handoff brief 替代上游专业内容。

Do not let the Orchestrator's short handoff brief replace the upstream professional content.

五、本轮产出 / Expected Output

产出路径 / Output packet path:
{OUTPUT_PACKET_PATH}

产出文件 / Output files:

按你的 `ROLE.md` 和 output standard 要求创建。

Create the files required by your `ROLE.md` and output standard.

如果因为 milestone 或上游输入不足无法产出，请只创建本角色允许的 blocked / draft packet 或向用户说明阻塞，不能写其他角色产物。

If the milestone or upstream input is insufficient, create only the blocked / draft packet allowed by this role or explain the blocker to the user. Do not write another role's output.

六、milestone 对齐要求 / Milestone Alignment Requirement

你的所有结论都必须回答：
All your conclusions must answer:

这个产出如何帮助当前 milestone 达成业务目标？
How does this output help the current milestone achieve its business goal?

这个产出覆盖了 milestone contract 中哪些 success criteria？
Which success criteria in the milestone contract does this output cover?

这个产出是否触碰 non-goals 或 hard prohibitions？
Does this output touch any non-goal or hard prohibition?

如果发现任务目标开始偏离 milestone，请停止扩展，明确写出：
If the task starts drifting away from the milestone, stop expanding scope and state:

- 偏离点是什么 / what the drift point is
- 是否需要 Orchestrator 调整 milestone / whether Orchestrator should adjust the milestone
- 是否需要当前角色修正输出 / whether this role should revise its output
- 是否需要先更新 milestone contract / whether the milestone contract must be updated first

七、边界 / Boundaries

允许读取 / Allowed read scope:
{ALLOWED_READ_SCOPE}

允许写入 / Allowed write scope:
{ALLOWED_WRITE_SCOPE}

禁止 / Forbidden:
- 不切换到其他角色 / Do not switch roles.
- 不修改上游 packet / Do not modify upstream packets.
- 不修改业务文件，除非你是 Implementer 且用户明确批准 / Do not modify business files unless you are Implementer and the user explicitly approved it.
- 不执行 git add / git commit / git push / Do not run git add, git commit, or git push.
- 默认允许为当前 milestone 使用公开来源联网研究，但首次回复必须说明联网目的和来源类型 / Public-source network research is allowed by default when relevant to the milestone, but the first response must state the network purpose and source types.
- 未经用户单独批准，不调用真实 provider API、不访问需认证或私有资源、不下载或执行远程内容、不向外部发送秘密或项目私有数据 / Do not call real provider APIs, access authenticated/private resources, download or execute remote content, or send secrets/project-private data externally unless separately approved.
- 不做 strict handoff，除非用户明确要求 / Do not perform strict handoff unless the user explicitly requests it.

八、开始方式 / Start Protocol

你的第一次回复不要直接写 packet。
Do not write the packet in your first response.

请先确认 / First confirm:

1. 你理解的 milestone 目标 / your understanding of the milestone goal
2. 你这个角色负责什么 / what this role is responsible for
3. 你会读取什么 / what you will read
4. 你会写入什么 / what you will write
5. 你不会做什么 / what you will not do
6. 是否存在阻塞或目标漂移风险 / whether there is any blocker or goal-drift risk

等用户回复“开始”后再执行。
Wait for the user to reply "开始" before execution.

九、完成后的回复格式 / Completion Response Format

完成后请输出：
After completion, output:

role_completion_status:
1 | 0

assigned_completion_conditions_total:
<integer>

assigned_completion_conditions_met:
<integer>

unmet_completion_conditions:
none | <condition id list>

completion_evidence:
- condition_id: <id>
  met: 1 | 0
  evidence: <concrete evidence>

forbidden_completion_claim_used:
true | false

然后列出 / Then list:

1. 本角色完成条件是否全部满足 / whether every role completion condition is met
2. 产出路径 / output path
3. 关键结论 / key conclusions
4. 这些结论如何服务 milestone / how these conclusions serve the milestone
5. 是否存在目标漂移 / whether goal drift exists
6. 哪些结论来自上游输入，哪些是你的判断 / which conclusions come from upstream input and which are your judgment
7. 是否存在阻塞 / blockers, if any
8. 建议给 Orchestrator 的路由判断 / routing recommendation for Orchestrator
9. 给 Orchestrator 的轻量交接检查块 / lightweight handoff check block for Orchestrator
```

## 规则 / Rules

- 除非用户要求 strict handoff，不要加入 readiness conversion 指令 / Do not include readiness conversion instructions unless the user requested strict handoff.
- 默认轻量流程里，不要求 `packet.lock.json` 或 `sha256` / Do not ask for `packet.lock.json` or `sha256` in the default lightweight flow.
- 让角色聚焦 milestone 产出，而不是流程管控 / Keep the role focused on milestone output, not process control.
- 完成状态只能是 `role_completion_status=1` 或 `role_completion_status=0` / Completion status can only be `role_completion_status=1` or `role_completion_status=0`.
- 不要让 Orchestrator 编写专业问题、专业背景、专业结论或专业输出清单 / Do not let Orchestrator write professional questions, background, conclusions, or output lists.
- 下一角色的专业问题必须由该角色从上游 packet 中提取 / The next role's professional questions must be derived by that role from the upstream packet.
- 如果 Orchestrator 已允许进入下一角色，必须输出完整可复制启动消息 / If Orchestrator has allowed the next role to start, output the full copy-ready startup message.
- 不要只写“推荐下一角色” / Do not only write "recommended next role".
