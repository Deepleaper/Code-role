# Orchestrator Consumption Check Request Template

Execution roles must include this block at the end of their completion response.

The block is for the user to copy into the Workflow Orchestrator role instance. It does not authorize the Orchestrator to modify the role packet, create downstream packets, run Git commands, or change business files.

```text
请执行 Orchestrator 消费检查。

当前完成角色:
{CURRENT_ROLE}

milestone:
{MILESTONE}

packet:
{CURRENT_PACKET_PATH}

handoff manifest:
{CURRENT_MANIFEST_PATH}

packet status reported by role:
{PACKET_STATUS}

ready_for_next_role:
{READY_FOR_NEXT_ROLE}

角色完成汇报:
{ROLE_COMPLETION_SUMMARY}

请检查:
1. manifest JSON 是否有效
2. manifest documents 是否存在
3. input_packets 是否正确记录上游输入
4. packet status / ready_for_next_role
5. blocked / external_research.used
6. 是否存在 packet.lock.json
7. 当前 packet 是否可被下游正式消费
8. 如果不可消费，下一步应回到哪个角色做 readiness 状态转换
9. 如果可消费，当前 chain 的下一角色是谁
10. 如果可以进入下一角色，请使用 Orchestrator next-role-message-template 生成下一角色完整首条消息

边界:
- 只更新 Orchestrator 状态文件
- 不修改当前角色 packet
- 不创建下游 packet
- 不执行 git add / git commit / git push
- 不修改业务文件
```

## Role Boundary

The current role may recommend a downstream role in its packet or summary, but it must not generate the authoritative next-role startup message. The Orchestrator owns chain position, consumable checks, routing, and the final next-role startup message.
