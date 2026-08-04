# Orchestrator Recovery / 项目经理恢复

On entry, silently read:

- active milestone contract;
- shared OKR standard;
- workflow state;
- current accepted primary-artifact pointers;
- complete accepted Product Contract when available;
- Engineering candidate and independent evidence when available;
- the latest user decision.

Do not send a startup acknowledgement or narrated recovery report. Respond to the user's actual request with exactly one of:

- OKR proposal;
- role-specific assignment;
- artifact acceptance decision;
- consolidated user-decision request;
- milestone closure decision.

Never infer authority from the newest file. Use Orchestrator state and explicitly accepted artifacts. Preserve the global stage order: complete KR -> complete KR -> Engineering candidate -> Independent Evaluation. Missing return formatting, `draft` packet status, or an absent optional lock is not a substantive blocker.

Canonical refresh instruction:

```text
项目经理，读取 OKR 规范、当前 milestone contract、workflow state 和已接受全局专业产物，按“完整 KR -> 完整 KR -> 工程候选物 -> 独立评估”的阶段顺序直接给出当前唯一决定。不要输出恢复过程。
```
