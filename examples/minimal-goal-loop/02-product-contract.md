# Complete Product OKR / 完整产品 OKR

## Product Objective / 产品目标

Reporter CLI users can deliberately select deterministic machine-readable JSON while existing users retain the exact default text contract.

## Product Key Results / 产品关键结果

| PKR | Product outcome | Binary threshold | Source MKRs | Independent evidence |
| --- | --- | --- | --- | --- |
| PKR-1 | `--format json` is an explicit supported command mode; unsupported values fail with a stable actionable error. | 3/3 valid fixtures accepted; 3/3 frozen invalid-format cases return exit 2 and the accepted message. | MKR-1 | Fresh CLI observations. |
| PKR-2 | JSON output follows schema v1 and is deterministic for identical input. | 3/3 schema-valid; two runs per fixture have equal SHA-256. | MKR-1 | Raw output, schema result, hash pairs. |
| PKR-3 | Omitting `--format` and selecting `--format text` preserve the existing text output. | 12/12 frozen text fixtures are byte-identical. | MKR-2 | Fresh regression diff. |

## MKR-to-PKR Traceability / 映射

| MKR | Covered by | Coverage complete |
| --- | --- | ---: |
| MKR-1 | PKR-1, PKR-2 | 1 |
| MKR-2 | PKR-3 | 1 |

## Scope And Claims / 范围与声明

- In scope: CLI format selection, JSON schema v1, deterministic serialization, text compatibility, invalid-format behavior.
- Out of scope: YAML/XML, streaming output, plugin APIs, unrelated performance work.
- Allowed claim after independent pass: Reporter CLI supports deterministic JSON export while preserving the frozen text contract.
- Forbidden claim: all future report schemas or every external integration are compatible.

product_okr_complete: 1
all_mkrs_covered: 1
