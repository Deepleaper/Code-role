# Complete Product Contract / 完整产品契约

Authority: the Project Objective and `KR-1`, `KR-2` in `milestone-board.md`. This document adds product detail to those KRs and creates no additional Objective or KR.

权威目标来自 `milestone-board.md` 中的 Project Objective、`KR-1` 和 `KR-2`。本文只补充产品定义，不创建第二套 Objective 或 KR。

## Product Definition By Existing KR / 按现有 KR 补充产品定义

| KR | User and trigger | Observable behavior | Failure behavior | Binary product acceptance | Independent evidence |
| --- | --- | --- | --- | --- | --- |
| KR-1 | Reporter CLI user supplies fixture A, B, or C with `--format json`. | CLI emits schema-v1 JSON with stable key order and normalized values; two identical runs produce equal SHA-256. | Unsupported `--format` values return exit 2 and the accepted actionable message without partial output. | 3/3 valid fixtures pass schema; two runs per fixture have equal SHA-256; 3/3 frozen invalid-format cases pass. | Raw CLI output, schema results, hash pairs, and invalid-case log. |
| KR-2 | Existing user omits `--format` or selects `--format text`. | CLI emits the exact frozen text output. | JSON support does not alter default selection, text formatting, exit status, or stderr behavior. | 12/12 frozen text fixtures are byte-identical. | Fresh evaluator regression diff. |

## User Flow And State Rules / 用户流程与状态规则

1. Parse `--format`; omission resolves to `text`.
2. Reject unsupported values before report serialization.
3. Serialize valid `json` requests with schema v1; serialize `text` through the unchanged text path.
4. Return one complete output or one actionable error; never mix partial JSON with an error.

## KR Product Coverage / KR 产品覆盖

| KR | Product definition complete | Evidence executable by Engineering and Evaluation |
| --- | ---: | ---: |
| KR-1 | 1 | 1 |
| KR-2 | 1 | 1 |

## Scope And Claims / 范围与声明

- In scope: CLI format selection, JSON schema v1, deterministic serialization, text compatibility, invalid-format behavior.
- Out of scope: YAML/XML, streaming output, plugin APIs, unrelated performance work.
- Allowed claim after independent pass: Reporter CLI supports deterministic JSON export while preserving the frozen text contract.
- Forbidden claim: all future report schemas or every external integration are compatible.

product_contract_complete: 1
all_krs_covered: 1
