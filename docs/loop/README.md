# Code-role Goal Loop / Code-role 目标闭环

This is the default Code-role operating model.

这是 Code-role 的默认运行模式。

## Purpose / 目的

Code-role controls one software milestone through a bounded evidence loop:

Code-role 通过一个有边界的证据闭环控制一个软件里程碑：

1. Project Manager freezes one Objective and binary Key Results.
2. Project Manager selects exactly one accepted `KR=0`.
3. Product Strategy removes product uncertainty only when needed.
4. Engineering produces a candidate implementation and evidence.
5. Independent Evaluation reruns the frozen milestone SOP.
6. Project Manager updates the board from independent evidence.
7. The loop repeats until every accepted KR is `1`, or a stop condition is reached.

1. 项目经理冻结一个 Objective 和一组二值 Key Results。
2. 项目经理每轮只选择一个已确认的 `KR=0`。
3. 只有存在产品不确定性时才调用产品策略。
4. 工程工位产出候选实现和证据。
5. 独立评估按照冻结的 milestone SOP 重新执行。
6. 项目经理依据独立证据更新作战板。
7. 所有已确认 KR 都为 `1`，或触发停止条件前，持续循环。

## Active Workstations / 活跃工位

| Workstation | Responsibility |
| --- | --- |
| Project Manager / 项目经理 | Owns Objective, KR definitions, current KR, routing, iteration budget, and milestone closure. |
| Product Strategy / 产品策略 | Resolves user value, behavior, scope, threshold, and claim-boundary uncertainty. |
| Engineering / 工程 | Researches engineering practice, designs when necessary, implements, tests, and produces candidate evidence. |
| Independent Evaluation / 独立评估 | Freezes or consumes the evaluation SOP, independently evaluates the complete required scope, and reports binary evidence. |

Research is a capability inside Product Strategy and Engineering. Architecture and context engineering are modes inside Engineering. They are not mandatory routing stages.

研究是产品策略和工程工位的能力。架构和上下文工程是工程工位的工作模式，不是必须依次经过的独立角色。

## Canonical Files / 权威文件

- `code-role/milestone-board.md`: the only active milestone state.
- `code-role/LOOP.md`: the operating contract.
- `code-role/templates/assignment.md`: the only PM-to-workstation task format.
- Role-specific return templates under `code-role/templates/`.
- Detailed attachments under `code-role/work/<milestone>/`.

Packets, manifests, readiness transitions, locks, state indexes, and archived role prompts are not part of the default loop.

Packet、manifest、readiness 转换、lock、state-index 和归档角色提示词不属于默认闭环。

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

## Legacy Profile / 历史模式

The previous eight-role packet workflow remains under [`docs/workflow/`](../workflow/README.md) for compatibility and audit history. It is not the default initialization path.

之前的八角色 packet 工作流仍保留在 [`docs/workflow/`](../workflow/README.md)，仅用于兼容和历史审计，不是默认初始化路径。
