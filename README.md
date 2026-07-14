# WorkflowPro-QA (scaffold)

This repository contains a simple scaffold for UI tests using Playwright and pytest.

## Quick start (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install
python -m pytest -q
```

Files:
- `tests/` — test files
- `pages/` — page objects
- `utils/` — helper modules
- `testdata/` — test data JSON files
- `reports/` — test reports
