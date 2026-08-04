# Engineering Delivery / 工程交付

## Engineering Execution KRs / 工程执行 KR

| EKR | Source PKRs | Dependency | Binary engineering result | Verification | Pass |
| --- | --- | --- | --- | --- | ---: |
| EKR-1 | PKR-1 | none | CLI accepts `text|json` and rejects other values with the accepted error. | 6 CLI contract cases. | 1 |
| EKR-2 | PKR-2 | EKR-1 | Schema-v1 serializer emits stable key order and normalized values. | 3 schema checks and repeated hashes. | 1 |
| EKR-3 | PKR-3 | EKR-1, EKR-2 | Integrated candidate preserves all frozen text fixtures and packages evaluator instructions. | 12 text regressions and clean candidate install. | 1 |

## Candidate / 候选物

- Candidate artifact: `dist/reporter-cli-candidate`
- Environment: Python 3.12, Linux or macOS, no network dependency.
- Run instructions: `dist/reporter-cli-candidate/bin/reporter --fixture <id> --format <text|json>`
- Engineering verification: CLI contract 6/6; JSON schema 3/3; repeated hash 3/3; text regression 12/12.

These results establish candidate readiness only. They do not pass MKR-1 or MKR-2.

all_required_ekrs_pass: 1
candidate_ready_for_independent_evaluation: 1
