# Security Policy / 安全策略

## Scope / 范围

Code-role is a local workflow template and documentation system. It does not provide hosted services, production APIs, or automatic code execution.

Code-role 是本地工作流模板和文档系统，不提供托管服务、生产 API 或自动代码执行。

## Do Not Submit / 不要提交

Do not submit:

- API keys, tokens, credentials, or secrets;
- private customer data;
- confidential source code from a target project;
- private workflow packets from a target project;
- provider credentials or authenticated resource URLs;
- logs that contain prompts, secrets, or proprietary project context.

请不要提交 API key、token、凭证、客户隐私数据、目标项目私有源码、目标项目私有 workflow packet、provider 凭证或包含敏感上下文的日志。

## Target Project Boundary / 目标项目边界

Generated target-project `code-role/` folders are local assistance by default. They should not be committed, pushed, packaged, indexed, or shipped unless the target project explicitly promotes Code-role into its standard workflow.

目标项目中生成的 `code-role/` 默认是本地辅助内容。除非目标项目明确决定纳入标准工作流，否则不应提交、推送、打包、索引或发布。

## Reporting / 报告问题

If you find a security issue in Code-role itself, open a GitHub issue only when the report does not include sensitive details. For sensitive reports, contact the repository owner privately.

如果发现 Code-role 自身的安全问题，且报告不包含敏感细节，可以提交 GitHub issue。包含敏感细节的问题请私下联系仓库所有者。
