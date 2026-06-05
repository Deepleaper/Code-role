# Code-role

Code-role is a discussion-first local workflow template for controlling Codex-assisted programming work.

Code-role 是一个 discussion-first 的本地工作流模板，用来控制 Codex 参与编程时的角色边界、上下文交接和交付质量。

It is not an automation runner. Its purpose is to make every professional step discussable, reviewable, and explicitly accepted before the next role acts.

它不是自动执行代码的工具。它的目标是让每个专业环节都先讨论、可审阅、可确认，然后再进入下一角色。

## What It Solves / 解决什么问题

Large coding tasks often drift when one Codex conversation tries to research, write PRD, design architecture, inspect code, implement, test, and review at the same time.

复杂编程任务如果在一个 Codex 对话里同时做调研、PRD、架构、代码上下文、实现、测试和审计，很容易出现目标漂移、上下文混乱和越权执行。

Code-role fixes that by splitting work into role-specific conversations:

Code-role 通过拆分独立角色对话解决这个问题：

- Workflow Orchestrator / 项目经理
- Researcher / 研究员
- Product / PRD / 产品经理
- Architect / 架构师
- Code Context / Context Engineer / 代码上下文工程师
- Implementer / 实现工程师
- Test Evaluator / 测试评估师
- Reviewer / 审计评审

Each execution role writes a versioned document packet. The next role consumes that packet as its professional input. Chat is not the source of truth.

每个执行角色产出一个版本化文档 packet。下一个角色消费这个 packet 作为专业输入。聊天记录不是事实源。

## Core Principles / 核心原则

- Discussion first, execution second.
- Every role confirms read scope, write scope, forbidden scope, and milestone alignment before writing.
- Non-Implementer roles produce documents only.
- Implementer can modify project files only after explicit user approval and exact writable scope confirmation.
- Orchestrator checks milestone alignment before routing to the next role.
- Every role completion response includes a copy-ready summary for Orchestrator / Project Manager.
- When Orchestrator routes forward, it must paste a copy-ready startup message for the next role.
- Public-source network research is allowed by default for every role when relevant to the milestone.
- Real provider APIs, authenticated/private resources, downloads, remote execution, or sending secrets/project-private data externally require separate explicit approval.
- Daily workflow is lightweight: user acceptance plus Orchestrator routing is enough.
- Strict `ready_for_next_role`, `packet.lock.json`, and `sha256` locking are optional advanced mode only.
- Target-project `code-role/` folders are local assistance, not product runtime or release artifacts.

中文规则：

- 先讨论，再执行。
- 每个角色写入前必须确认读取范围、写入范围、禁止范围和 milestone 对齐。
- 非 Implementer 角色只产出文档。
- Implementer 只有在用户明确批准并确认精确可写范围后，才能修改项目文件。
- Orchestrator / 项目经理先检查 milestone 是否漂移，再决定是否路由下一角色。
- 每个角色完成后，必须在同一条回复末尾附上给 Orchestrator 的可复制摘要。
- Orchestrator 如果允许进入下一角色，必须直接贴出可复制的下一角色启动消息。
- 每个角色默认都可以在当前 milestone 相关范围内使用公开来源联网研究。
- 调用真实 provider API、访问私有认证资源、下载或执行远程内容、向外部发送秘密或项目私有数据，都需要单独明确批准。
- 日常流程保持轻量：用户接受产出 + Orchestrator 路由即可。
- 严格 `ready_for_next_role`、`packet.lock.json`、`sha256` 只作为高级 strict handoff 模式。
- 目标项目里的 `code-role/` 是本地辅助，不是产品运行时内容，也不进入发布交付。

## Repository Contents / 仓库内容

```text
docs/product/
  prd.md
  prd.zh-CN.md
  code-role-workflow-guide.zh-CN.html

docs/workflow/
  README.md
  role-configuration-guide.md
  project-bootstrap.md
  handoff-protocol.md
  packet-schema.md
  workflow-chain-policy.md
  source-map.md
  orchestrator/
  roles/
  tools/

scripts/
  init_project_workflow.py

tests/
  test_workflow_*.py
```

Key documents / 关键文档：

- [Chinese product guide HTML](docs/product/code-role-workflow-guide.zh-CN.html)
- [Chinese PRD](docs/product/prd.zh-CN.md)
- [English PRD](docs/product/prd.md)
- [Workflow guide](docs/workflow/README.md)
- [Role configuration guide](docs/workflow/role-configuration-guide.md)
- [Project practices](docs/workflow/project-practices.md)
- [Role instance setup](docs/workflow/role-instance-setup.md)
- [Target project bootstrap](docs/workflow/project-bootstrap.md)
- [Optional state index](docs/workflow/state-index.md)
- [Git operation policy](docs/workflow/git-operation-policy.md)

Open source documents / 开源文档：

- [Contributing guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [MIT License](LICENSE)

## Fast Start In A Target Project / 在目标项目中快速启动

Run from this Code-role repository:

在 Code-role 仓库里执行：

```bash
python scripts/init_project_workflow.py \
  --target "/path/to/Target Project" \
  --project-name "Target Project" \
  --initial-milestone workflow-bootstrap \
  --initial-chain research-only \
  --write
```

This creates local workflow assistance in the target project:

它会在目标项目中创建本地辅助配置：

```text
code-role/
  README.md
  project-config.md
  role-instance-prompts/
  workflow/
    orchestrator/
      workflow-state.md
      milestone-registry.md
      decision-log.md
      final-packet-index.md
```

By default, it does not generate `state-index/`. Add `--with-state-index` only when optional navigation files are useful.

默认不会生成 `state-index/`。只有确实需要可选导航文件时，才加 `--with-state-index`。

If the target is a Git repository, the script adds `code-role/` to `.git/info/exclude`. That keeps workflow assistance local and out of the target project's Git history.

如果目标项目是 Git 仓库，初始化脚本会把 `code-role/` 写入 `.git/info/exclude`。这样 workflow 辅助文件保留在本地，不进入目标项目 Git 历史。

## How To Run The Workflow / 如何运行流程

1. Open the Workflow Orchestrator conversation.
2. Paste `code-role/role-instance-prompts/workflow-orchestrator.md`.
3. Ask Orchestrator to restore state:

```text
项目经理，执行 startup routine，恢复当前状态
```

4. Confirm the real milestone and chain.
5. Orchestrator routes to the next role and pastes a copy-ready startup message.
6. Open that role in a separate Codex conversation.
7. Paste the generated role prompt and Orchestrator startup message.
8. The role confirms scope first.
9. Reply `开始` only after the scope is correct.
10. After completion, copy the role's Orchestrator summary back to the Orchestrator conversation.

Create one configured Codex role instance per role. Do not run the whole workflow by switching roles inside one conversation.

中文步骤：

1. 打开 Workflow Orchestrator / 项目经理对话。
2. 粘贴 `code-role/role-instance-prompts/workflow-orchestrator.md`。
3. 让项目经理恢复状态：

```text
项目经理，执行 startup routine，恢复当前状态
```

4. 确认真实 milestone 和 chain。
5. Orchestrator 路由下一角色，并直接贴出可复制启动消息。
6. 为该角色打开单独 Codex 对话。
7. 粘贴生成的角色 prompt 和 Orchestrator 启动消息。
8. 角色先确认范围。
9. 范围正确后，回复 `开始`。
10. 角色完成后，把它末尾的 Orchestrator 摘要复制回项目经理对话。

## Role Chain / 角色链路

Typical full chain:

典型完整链路：

```text
Workflow Orchestrator
  -> Researcher
  -> Product / PRD
  -> Architect
  -> Code Context
  -> Implementer
  -> Test Evaluator
  -> Reviewer
  -> Workflow Orchestrator closeout
```

Supported chain types:

支持的链路类型：

- `full-chain`: high-risk or full lifecycle work.
- `mini-chain`: scope is mostly known, but architecture/context/testing/review are still needed.
- `patch-chain`: narrow implementation follow-up with known scope.
- `docs-only-chain`: documentation-only work.
- `research-only`: research that stops before PRD or implementation.

## Validation / 校验

Run tests:

运行测试：

```bash
.venv/bin/python -m pytest -q
```

Validate a packet template:

校验 packet 模板：

```bash
python docs/workflow/tools/validate_workflow_packet.py docs/workflow/roles/researcher/templates
```

## Git And Release Boundary / Git 与发布边界

For this repository, Code-role itself is committed and published as a workflow template.

对于本仓库，Code-role 本身会作为工作流模板提交和发布。

For target projects, generated `code-role/` folders are local operator assistance by default. They should not be committed, pushed, packaged, indexed, or shipped as product release artifacts unless a team explicitly decides to promote Code-role into that repository's standard workflow.

对于目标项目，初始化生成的 `code-role/` 默认只是本地操作者辅助。除非团队明确决定把 Code-role 升级为该项目的标准工作流，否则它不应被提交、推送、打包、索引或作为产品发布内容交付。

Normal Git operations for product code remain normal Git operations. Code-role can report Git facts, but it does not own or gate normal project commits.

产品代码的 Git 操作仍按项目原有方式执行。Code-role 可以报告 Git 状态，但不接管也不阻断正常项目提交。

## Status / 当前状态

Current template status:

当前模板状态：

- Eight roles are defined.
- Role output standards are defined for professional deliverables.
- Orchestrator milestone-alignment checks are defined.
- Lightweight handoff is the default.
- Strict packet locking is optional.
- Target-project bootstrap is available.
- Tests cover workflow rules, role boundaries, packet templates, and bootstrap behavior.

## License / 许可

Code-role is released under the [MIT License](LICENSE).

Code-role 使用 [MIT License](LICENSE) 开源。
