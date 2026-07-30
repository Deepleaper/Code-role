# Engineering Candidate Evidence

This illustrative attachment records candidate evidence only. It cannot change milestone state.

## JSON-1

- Command: `pytest -q tests/test_json_output.py -k schema`
- Exit code: `0`
- Observed: `3 passed`
- Candidate artifacts: `tmp/candidate/a.json`, `tmp/candidate/b.json`, `tmp/candidate/c.json`

## JSON-2

- Command: `pytest -q tests/test_json_output.py -k deterministic`
- Exit code: `0`
- Observed: `3 passed`
- SHA-256 pairs: `A=match`, `B=match`, `C=match`

## REG-1

- Command: `pytest -q tests/test_text_output.py`
- Exit code: `0`
- Observed: `12 passed`
- Snapshot changes: `0`
