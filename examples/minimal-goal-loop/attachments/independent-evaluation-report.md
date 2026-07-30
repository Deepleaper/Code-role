# Independent Evaluation Report

This illustrative report represents a fresh evaluator run. No Engineering-generated output artifact was reused.

## JSON-1

- Command: `pytest -q tests/test_json_output.py -k schema`
- Exit code: `0`
- Observed: `3 passed`
- Fresh artifacts: `tmp/evaluator/a.json`, `tmp/evaluator/b.json`, `tmp/evaluator/c.json`
- Exact-key checks: `3/3 passed`

## JSON-2

- Command: `pytest -q tests/test_json_output.py -k deterministic`
- Exit code: `0`
- Observed: `3 passed`
- Independent SHA-256 pairs: `A=match`, `B=match`, `C=match`

## REG-1

- Command: `pytest -q tests/test_text_output.py`
- Exit code: `0`
- Observed: `12 passed`
- Snapshot diff: empty

## Evaluator Boundary

The evidence supports `KR-1=1`. It does not establish production readiness, performance improvement, or support for formats outside JSON.
