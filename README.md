[![CI](https://github.com/OMKAR40111/Testing_Automation_Bynry/actions/workflows/ci.yml/badge.svg)](https://github.com/OMKAR40111/Testing_Automation_Bynry/actions/workflows/ci.yml)

# Project

This project is a small test framework that uses Playwright and pytest to run browser tests.

## Installation

Follow these steps on Windows PowerShell to set up the project:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install
```

## How to run tests

Run all tests:

```powershell
python -m pytest -q
```

Run a single test file:

```powershell
python -m pytest tests/login_test.py -q
```

## Framework

- Tests: `pytest`
- Browser automation: `playwright`
- HTTP requests: `requests`

## Folder structure

- `tests/` - test files (examples are `login_test.py`, `project_test.py`)
- `pages/` - page object placeholders (e.g. `login_page.py`)
- `utils/` - small helpers (e.g. `config.py`)
- `testdata/` - local test pages and data (`login.html`, `dashboard.html`, `users.json`)
- `reports/` - test output and reports
- `requirements.txt` - pinned Python packages
- `pytest.ini` - pytest config

## Assumptions

- You have Python 3 installed.
- You will run tests on Windows PowerShell (commands above).
- Tests use local HTML files by default for examples.

## Tools used

- Python, pip
- Playwright (for browser automation)
- pytest (test runner)
- Git and GitHub Actions (CI)

## Known issues

- Playwright downloads browser binaries (this can be large).
- On CI, Playwright may need extra setup on some runners.
- If tests fail locally, try re-running `python -m playwright install`.

If you want, I can add a CI status badge to this file.
