# Code-role Goal Loop / Code-role 目标闭环

This is the Code-role Minimal Profile: the smallest complete milestone-control unit.

这是 Code-role 四角色最小版：能够完整控制一个软件里程碑的最小单元。

## Purpose / 目的

Code-role controls one software milestone through a bounded evidence loop:

Code-role 通过一个有边界的证据闭环控制一个软件里程碑：

1. Project Manager and user accept one complete Objective and `MKR-1...MKR-N`.
2. Product Strategy defines one complete Product OKR, `PKR-1...PKR-N`, covering every MKR.
3. Engineering decomposes the complete product contract into `EKR-1...EKR-N`, implements, integrates, and self-verifies the runnable candidate.
4. Independent Evaluation starts only after candidate readiness and evaluates the complete MKR/PKR contract.
5. Project Manager closes the milestone or returns the failed global contract owner.

1. 项目经理与用户确认一个完整 Objective 和 `MKR-1...MKR-N`。
2. 产品策略定义覆盖全部 MKR 的完整 Product OKR：`PKR-1...PKR-N`。
3. 工程把完整产品契约拆成 `EKR-1...EKR-N`，完成设计、编码、集成和自测。
4. 独立评估只在候选物就绪后启动，并评估完整 MKR/PKR 契约。
5. 项目经理关闭里程碑，或把完整失败契约退回责任角色。

## Active Workstations / 活跃工位

| Workstation | Responsibility |
| --- | --- |
| Project Manager / 项目经理 | Owns the complete Milestone OKR, stage gates, iteration budget, and closure. |
| Product Strategy / 产品策略 | Owns the complete Product OKR and MKR-to-PKR product contract. |
| Engineering / 工程 | Owns EKR decomposition, architecture/context methods, implementation, integration, tests, and the complete candidate. |
| Independent Evaluation / 独立评估 | Starts after candidate readiness and independently evaluates every MKR and PKR. |

Research is a capability inside Product Strategy and Engineering. Architecture and context engineering are modes inside Engineering. They are not mandatory routing stages.

研究是产品策略和工程工位的能力。架构和上下文工程是工程工位的工作模式，不是必须依次经过的独立角色。

A delivery KR must describe an observable user, business, product, or runtime outcome. Research, PRDs, architecture, evaluation SOPs, tests, reports, and reviews are methods or evidence. Each role writes one required primary artifact; additional attachments are optional.

交付 KR 必须描述可观测的用户、业务、产品或运行时结果。调研、PRD、架构、评估 SOP、测试、报告和审计只是方法或证据。每个角色只有一份必需的主交付物，其他附件可选。

## Canonical Files / 权威文件

- `code-role/milestone-board.md`: the only active milestone state.
- `code-role/DIALOGUE-CONTROL.md`: shared conversation and artifact-first acceptance contract.
- `code-role/OKR-STANDARD.md`: authoritative MKR/PKR/EKR definition and decomposition standard.
- `code-role/LOOP.md`: the operating contract.
- Role-specific assignment templates under `code-role/templates/`.
- Role-specific return templates under `code-role/templates/`.
- Detailed attachments under `code-role/work/<milestone>/`.

Packets, manifests, readiness transitions, locks, state indexes, and archived role prompts are not part of the Minimal Profile control model.

Packet、manifest、readiness 转换、lock、state-index 和归档角色提示词不属于四角色最小版控制模型。

## Start / 启动

```bash
python scripts/init_loop_workflow.py "/absolute/path/to/project" \
  --project-name "Project Name"
```

Update role rules without replacing the existing milestone board or work history:

只更新角色规则，不替换已有作战板和工作历史：

```bash
python scripts/init_loop_workflow.py "/absolute/path/to/project" \
  --project-name "Project Name" \
  --sync
```

Validate an initialized project:

校验已初始化项目：

```bash
python scripts/init_loop_workflow.py "/absolute/path/to/project" --check
```

The initializer adds `code-role/` to `.git/info/exclude` when the target is a Git repository. This keeps role-control material local without changing the product repository's tracked `.gitignore`.

如果目标项目是 Git 仓库，初始化器会把 `code-role/` 写入本地 `.git/info/exclude`。这样角色控制材料保持本地，不会修改产品仓库已跟踪的 `.gitignore`。

## Full Profile / 八角色完整版

The eight-role Full Profile lives under [`docs/workflow/`](../workflow/README.md). It uses the same artifact-first dialogue control while adding separate research, product, architecture, code-context, implementation, evaluation, and audit ownership with versioned packet evidence.

八角色完整版位于 [`docs/workflow/`](../workflow/README.md)。当调研、产品定义、架构、代码上下文、实现、独立评估和最终审计需要独立专业责任及版本化 packet 证据时使用它。

Neither profile is deprecated. Select one profile for a milestone and keep its control records authoritative throughout that milestone.

两套配置都不是历史遗留。每个 milestone 选择其中一套，并在该 milestone 内始终以所选配置的控制记录为权威。
