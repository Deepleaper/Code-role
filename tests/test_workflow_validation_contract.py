import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "workflow"
VALIDATOR = WORKFLOW / "tools" / "validate_workflow_packet.py"
DRAFT_TEMPLATE_PACKET = WORKFLOW / "roles" / "researcher" / "templates"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_workflow_validation_doc_defines_required_checks() -> None:
    text = read(WORKFLOW / "workflow-validation.md")
    for phrase in [
        "observable user, business, product, or runtime outcome",
        "one exact current failed evidence item",
        "required_artifact_path",
        "does not require a precomputed per-file writable whitelist",
        "Exactly one primary professional artifact is required",
        "evaluation_executed=0|1",
        "kr_observed_pass=0|1",
        "Only when the user explicitly requests immutable packet provenance",
    ]:
        assert phrase in text


def test_local_validator_script_exists_and_validates_template_packet() -> None:
    assert VALIDATOR.exists()
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(DRAFT_TEMPLATE_PACKET)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    payload = json.loads(result.stdout)
    assert payload["ok"] is True
    assert payload["role"] == "researcher"
    assert payload["status"] == "draft"


def test_local_validator_allows_draft_for_lightweight_consumption() -> None:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(DRAFT_TEMPLATE_PACKET), "--for-consumption"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["ok"] is True
    assert payload["status"] == "draft"


def test_local_validator_rejects_draft_for_strict_consumption() -> None:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(DRAFT_TEMPLATE_PACKET), "--for-consumption", "--strict"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["ok"] is False
    assert "not strictly consumable" in payload["error"]
