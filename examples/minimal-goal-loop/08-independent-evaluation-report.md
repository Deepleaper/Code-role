# Independent Evaluation Report / 独立评估报告

## Recorded SOP / 已记录 SOP

Recorded before candidate outputs were inspected: run frozen valid and invalid CLI cases, validate three JSON fixtures against schema v1, compare two-run SHA-256 for each fixture, and diff all 12 frozen text fixtures byte-for-byte.

## Independent Observations / 独立观察

| Check | Observed | Evidence | Pass |
| --- | --- | --- | ---: |
| PKR-1 CLI contract | valid JSON mode 3/3; invalid format 3/3 returned exit 2 and accepted message | `evidence/cli-contract.log` | 1 |
| PKR-2 schema | fixture A/B/C schema-valid | `evidence/schema-results.json` | 1 |
| PKR-2 determinism | repeated SHA-256 equal for A/B/C | `evidence/hash-pairs.txt` | 1 |
| PKR-3 compatibility | 12/12 text outputs byte-identical | `evidence/text-regression.diff` | 1 |

## MKR Results / MKR 结果

| MKR | Observed result | Pass |
| --- | --- | ---: |
| MKR-1 | All JSON behavior, schema, and determinism thresholds passed. | 1 |
| MKR-2 | All frozen text compatibility thresholds passed. | 1 |

evaluation_executed: 1
product_contract_pass: 1
milestone_observed_pass: 1
