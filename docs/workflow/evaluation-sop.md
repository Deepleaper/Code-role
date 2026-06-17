# Evaluation SOP / 评估 SOP

The Evaluation SOP is the hard evaluation anchor for a milestone.

评估 SOP 是一个 milestone 的硬评估锚点。

It exists because evaluation quality cannot rely on a different ad-hoc rubric every time. Test Evaluator proposes or confirms the SOP before evaluation. Reviewer audits whether the SOP was followed.

它存在的原因是：评估质量不能每次都依赖临时口径。Test Evaluator 在评估前提出或确认 SOP，Reviewer 审计该 SOP 是否被遵守。

## Authority / 权威性

In a target project, the active SOP lives at:

```text
code-role/workflow/evaluation/evaluation-sop.md
```

在目标项目中，当前有效 SOP 位于：

```text
code-role/workflow/evaluation/evaluation-sop.md
```

Test Evaluator owns the SOP content for the active milestone. The user confirms it. Reviewer audits it. Orchestrator routes based on it.

Test Evaluator 负责当前 milestone 的 SOP 内容；用户确认；Reviewer 审计；Orchestrator 基于它路由。

## Required Fields / 必填字段

```text
evaluation_subject:
evaluation_objective:
required_layers:
baseline_sources:
metrics:
thresholds:
commands_or_checks:
artifact_requirements:
not_run_policy:
claim_boundary:
final_acceptance_rule:
sop_calibration_rule:
```

## Hard Rules / 硬规则

- Test Evaluator must not start final evaluation until the SOP is confirmed or explicitly marked partial/blocked.
- If the SOP is missing or unconfirmed, `quality-gate.md` must not be `pass`.
- `not_run` never counts as `pass`.
- Implementer-reported verification is input only; it is not final evaluation evidence.
- If public-source research is used to define an industry benchmark or common practice, sources must be recorded.
- If no benchmark or common-practice source exists, mark it `unknown` or `not_found`; do not invent consensus.
- Every complete evaluation must include SOP calibration: keep, amend, or block.
- SOP changes must be recorded in the Test Evaluator packet; evaluation standards must not drift silently.

- SOP 缺失或未确认时，Test Evaluator 不得开始最终评估，除非明确标记 partial/blocked。
- SOP 缺失或未确认时，`quality-gate.md` 不得为 `pass`。
- `not_run` 永远不能算作 `pass`。
- Implementer 自证只是输入，不是最终评估证据。
- 如果用公开来源研究定义行业 benchmark 或通用实践，必须记录来源。
- 如果没有 benchmark 或通用实践来源，标记 `unknown` 或 `not_found`，不得编造共识。
- 每次完整评估必须包含 SOP calibration：保持、修订或阻塞。
- SOP 变更必须记录在 Test Evaluator packet 中；评估标准不得静默漂移。

## Default Layer Order / 默认分层顺序

Use the following layer order when the milestone scope does not define a narrower SOP.

当 milestone 没有定义更窄 SOP 时，使用以下默认分层顺序。

1. **Evaluation Baseline Gate / 评估基线门**
   - evaluation subject
   - objective
   - baseline source
   - metrics
   - thresholds
   - accepted evidence

2. **Evidence Integrity Gate / 证据完整性门**
   - artifact existence
   - source path validity
   - command output or inspection result
   - same-run or version consistency when relevant
   - fixture/synthetic/manual evidence disclosure

3. **Acceptance Mapping Gate / 验收映射门**
   - Product / PRD acceptance criteria
   - Architect test strategy
   - Code Context test map
   - Implementer changed files and verification log

4. **Independent Evaluation Gate / 独立评估门**
   - evaluator-observed evidence
   - commands actually run
   - files actually inspected
   - gaps, failures, and not-run checks

5. **Regression And Risk Gate / 回归与风险门**
   - regression coverage
   - unresolved P0/P1/P2
   - side effects and forbidden actions
   - safety, privacy, permission, or claim-boundary risks

6. **Claim Boundary Gate / 结论边界门**
   - what may be claimed
   - what must remain unknown
   - what needs Reviewer or user confirmation
   - what cannot be called production-ready, release-ready, benchmark-leading, or business-complete

7. **Final Quality Gate / 最终质量门**
   - `pass`
   - `pass_with_residual_risk`
   - `fail`
   - `blocked`
   - `partial`

8. **SOP Calibration / SOP 校准**
   - keep SOP unchanged
   - amend SOP with recorded reason
   - block because SOP is insufficient

## Template / 模板

```text
# Evaluation SOP

status: draft | confirmed | partial | blocked | superseded
confirmed_by: user | unknown
confirmed_at: YYYY-MM-DD | unknown
milestone:

evaluation_subject:
<what is being evaluated>

evaluation_objective:
<what decision this evaluation must support>

required_layers:
- evaluation_baseline
- evidence_integrity
- acceptance_mapping
- independent_evaluation
- regression_and_risk
- claim_boundary
- final_quality_gate
- sop_calibration

baseline_sources:
- user_confirmed_baseline: <path or summary>
- product_acceptance: <path or summary>
- architecture_test_strategy: <path or summary>
- code_context_test_map: <path or summary>
- industry_or_benchmark_reference: <source or unknown>

metrics:
- <metric name>: <definition>

thresholds:
- <metric name>: <pass/fail threshold>

commands_or_checks:
- <command or inspection>: required | optional | blocked

artifact_requirements:
- <artifact, packet, source file, command output, or inspection evidence>

not_run_policy:
- Required checks marked `not_run` block unconditional pass.
- Optional checks marked `not_run` must be listed as residual risk or not applicable.

claim_boundary:
- allowed_claims:
  - <claim>
- forbidden_claims:
  - <claim>
- unknown_claims:
  - <claim>

final_acceptance_rule:
<what must be true before final_acceptance=true may be recommended>

sop_calibration_rule:
- After evaluation, state whether this SOP remains valid.
- Record every SOP change in the Test Evaluator packet.
```

