# Milestone Board / 里程碑作战板

<!-- Current accepted state only. No chronological workflow history. -->

## Milestone / 里程碑

| Field | Value |
| --- | --- |
| Project | `Reporter CLI` |
| Milestone | `deterministic-json-export` |
| Objective accepted | `1` |
| Delivery stage | `milestone_decision` |
| Project OKR accepted | `1` |
| Product Contract accepted | `1` |
| Runnable candidate ready | `1` |
| Independent evaluation executed | `1` |
| Milestone pass | `1` |

## Objective / 目标

Users can export a report as stable JSON without changing the existing text-output contract.

## Milestone Key Results / 里程碑关键结果

| KR | Observable delivered outcome | Binary threshold | Measurement | Required independent evidence | Accepted evidence path | Pass |
| --- | --- | --- | --- | --- | --- | ---: |
| KR-1 | Users can export fixtures A, B, and C as valid deterministic JSON. | 3/3 fixtures pass schema and repeated-run SHA-256 equality. | Fresh evaluator run against the candidate. | Raw JSON, schema output, and hash pairs. | `08-independent-evaluation-report.md` | 1 |
| KR-2 | Existing text-output users observe no contract change. | 12/12 frozen text regressions are byte-identical. | Fresh evaluator regression run against the candidate. | Command log and fixture diff output. | `08-independent-evaluation-report.md` | 1 |

## Accepted Global Artifacts / 已接受全局产物

| Field | Value |
| --- | --- |
| Current owner | `project-manager` |
| Milestone contract | `milestone-board.md#milestone-key-results--里程碑关键结果` |
| Product contract | `02-product-contract.md` |
| Engineering delivery | `05-engineering-delivery.md` |
| Runnable candidate | `dist/reporter-cli-candidate` |
| Independent evidence | `08-independent-evaluation-report.md` |
| Current blocking contract | `none` |
| Human decision required | `release decision` |

## Non-Goals / 非目标

- YAML or XML output.
- Streaming export.
- A new plugin API.
- Performance optimization beyond the existing command timeout.
