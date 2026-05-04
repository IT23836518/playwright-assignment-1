# IT23836518 Playwright Test Automation

This repository contains a Playwright test project built with Python and pytest.

## Project Files

- `requirements.txt` - Python dependencies
- `pytest.ini` - pytest configuration
- `conftest.py` - shared Playwright fixtures
- `tests/test_example.py` - sample Playwright test

## Requirements

- Python 3.10 or newer
- `pip`

## Installation

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Install the Playwright browser binaries:

```bash
python -m playwright install
```

## Running the Tests

Run all tests:

```bash
pytest
```

You can also run a single test file:

```bash
pytest tests/test_example.py
```

## Project Structure

- `tests/` contains the Playwright test files.
- `conftest.py` provides a reusable browser fixture.
- `pytest.ini` keeps pytest focused on the `tests` folder.

## Notes

- This repository is now Python-based, so the JavaScript Playwright files were replaced.
- Add more test files inside `tests/` as needed.
