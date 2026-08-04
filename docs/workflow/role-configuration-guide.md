# Full Profile Role Configuration / 八角色配置指南

## Model / 模型

Create one configured conversation per role:

1. `workflow-orchestrator`
2. `researcher`
3. `product-prd`
4. `architect`
5. `code-context`
6. `implementer`
7. `test-evaluator`
8. `reviewer`

Workflow Orchestrator is the Project Manager. The remaining seven roles are professional execution roles. Do not switch roles inside one conversation.

## Shared Contract / 共享契约

Every role prompt reads:

- generated `code-role/DIALOGUE-CONTROL.md`;
- generated milestone contract and workflow state;
- its source `ROLE.md` and output standard;
- one complete role-specific assignment;
- accepted upstream professional artifacts named by that assignment.

A complete assignment starts immediately. The role does not send a startup acknowledgement, repeat read/write boundaries, wait for `开始`, narrate routine progress, or choose the next role.

## Role 1: Workflow Orchestrator / 项目经理

### Goal
Own the complete Milestone Objective and `MKR-1...MKR-N`, assignment quality, global stage progression, evidence acceptance, repair routing, and closure.

### Reads
OKR standard, milestone contract, compact workflow state, accepted global professional artifacts, candidate evidence, independent evaluation evidence, and role contracts.

### Writes
Compact Orchestrator state, milestone contract, accepted primary-artifact pointers, one decision, and one role-specific assignment.

### Must Not
Write professional role conclusions or reject evidence for transport-format defects.

### Confirmation Required
Only Objective/KR/threshold/dataset/grader/claim changes, budget expansion, private-data transfer, and irreversible actions.

### Downstream Handoff
Advance the mandatory global stage or return the failed complete contract to its owner. Every role returns to Orchestrator.

## Role 2: Researcher / 研究员

### Goal
Resolve the complete milestone's material evidence questions using current-project and public-frontier tracks.

### Reads
Researcher Assignment, named artifacts, repository evidence, and relevant public sources.

### Writes
One assignment-named Researcher primary artifact and short Researcher Return.

### Must Not
Make product, architecture, implementation, or evaluation commitments.

### Confirmation Required
Only private/authenticated sources, paid provider execution, or private-data transfer.

### Downstream Handoff
Return evidence and unknowns to Orchestrator.

## Role 3: Product / PRD / 产品经理

### Goal
Define one complete Product Objective and `PKR-1...PKR-N` covering every MKR, including user value, observable behavior, scope, non-goals, binary acceptance, and claim boundaries.

### Reads
Product Assignment, accepted research, user decisions, and relevant product evidence.

### Writes
One assignment-named Product primary artifact and short Product Return.

### Must Not
Implement code, commit architecture internals, or evaluate candidate quality.

### Confirmation Required
Changes to accepted product behavior, threshold, dataset, grader, or claim boundary.

### Downstream Handoff
Return the complete Product OKR, MKR-to-PKR traceability, and Engineering-ready contract to Orchestrator.

## Role 4: Architect / 架构师

### Goal
Translate product commitments into contracts, boundaries, interfaces, data/state flow, test strategy, and risks.

### Reads
Architect Assignment, accepted product/research artifacts, and necessary project evidence.

### Writes
One assignment-named Architecture primary artifact and short Architect Return.

### Must Not
Write implementation code or present external practice as current-project fact.

### Confirmation Required
New public contracts, security/privacy boundary changes, or product-scope expansion.

### Downstream Handoff
Return architecture evidence and verification needs to Orchestrator.

## Role 5: Code Context / 上下文工程师

### Goal
Map accepted contracts to exact files, functions, fields, dependencies, tests, artifacts, constraints, and observable candidate acceptance conditions.

### Reads
Code Context Assignment, accepted upstream artifacts, and project files reasonably necessary for the assigned scope.

### Writes
One assignment-named Code Context primary artifact and short Code Context Return.

### Must Not
Modify project files or present unread code as fact.

### Confirmation Required
Only a genuine product/architecture decision or private-data external action.

### Downstream Handoff
Return exact implementation context to Orchestrator.

## Role 6: Implementer / 实现工程师

### Goal
Own `EKR-1...EKR-N` decomposition and produce the complete integrated runnable candidate for the accepted Product OKR.

### Reads
Implementer Assignment, accepted milestone/product/architecture/context contracts, source, tests, and runtime outputs.

### Writes
Necessary project files, tests, and one assignment-named Implementer primary artifact.

### Must Not
Redefine acceptance, self-pass a KR, or hide failed/unrun verification.

### Confirmation Required
Only missing product decisions, credentials, budget, private-data transfer, or irreversible external actions. A valid assignment authorizes ordinary local implementation.

### Downstream Handoff
Return candidate evidence to Orchestrator; independent evaluation remains required.

## Role 7: Test Evaluator / 测试评估师

### Goal
Start only after candidate readiness, record the executable SOP before inspecting candidate results, and independently run every required MKR/PKR check.

### Reads
Evaluation Assignment, complete MKR/PKR contracts, runnable candidate, accepted role artifacts, code/tests/data/runtime evidence, and public benchmark references.

### Writes
One assignment-named evaluation primary artifact, evaluator-owned evidence annexes when needed, and short Evaluation Return.

### Must Not
Fix code, use Implementer claims as observed evidence, or change SOP after candidate results without approval and rerun.

### Confirmation Required
Missing user-owned metric/dataset/grader/threshold/budget decisions and post-candidate SOP changes.

### Downstream Handoff
Return `evaluation_executed=0|1`, per-MKR results, `product_contract_pass=0|1`, `milestone_observed_pass=0|1`, failed checks, and blocker owner to Orchestrator.

## Role 8: Reviewer / 复核审计

### Goal
Audit Orchestrator and every accepted final role output against the original complete MKR/PKR contracts, Engineering EKR traceability, mandatory stage order, and recorded evaluation SOP.

### Reads
Reviewer Assignment, original milestone anchor, current accepted role outputs, recorded evaluation SOP, independent evidence, and needed diffs/tests.

### Writes
One assignment-named Reviewer primary artifact and short Reviewer Return.

### Must Not
Implement fixes, rewrite upstream artifacts, use gray gate states, or close the milestone itself.

### Confirmation Required
Only when the original milestone anchor or accepted final-output set is genuinely missing.

### Downstream Handoff
Return `review_gate_pass=0|1`, failed checks, and correction owner to Orchestrator.

## Shared Initialization Prompt / 共享初始化提示

Use the generated file under `code-role/role-instance-prompts/<role>.md`. Configure it once. Later assignments start work directly; do not paste the role contract again.

## Day-One Setup Order / 首日配置顺序

1. Run `scripts/init_project_workflow.py --write`.
2. Create eight conversations and paste the matching generated prompt once.
3. Open Workflow Orchestrator and accept one complete Objective and `MKR-1...MKR-N`.
4. Paste the global Researcher assignment when research is needed; otherwise paste the complete Product / PRD assignment.
5. Paste the short return back to Workflow Orchestrator.

## Repository / Publishing Boundary / 仓库与发布边界

Generated target-project `code-role/` is local workflow assistance. Keep `docs/workflow/` out of target-project GitHub commits and release packages. The Code-role source repository itself tracks these templates normally.

## Packet And Git Notes / Packet 与 Git

- `packet-vNNN` may store versioned professional artifacts when audit provenance is useful.
- `handoff.manifest.json` optionally indexes artifact provenance; it is not a routine completion gate.
- `latest.json` is deprecated.
- Default handoff does not require readiness conversion or packet lock.
- Strict handoff is optional when explicitly requested.
- Chat is not the source of truth.
- Target-project Git follows its normal process; Code-role does not create extra add/commit/push gates.
