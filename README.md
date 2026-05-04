# IT23836518 Playwright Test Automation

This repository contains a Python Playwright script that reads test cases from an Excel workbook, runs browser-based transliteration checks, and writes the actual output and status back into the workbook.

## Project Files

- `IT23836518_test_automation.py` - main automation script
- `IT23836518 _Test cases.xlsx` - test case workbook used by the script

## Requirements

- Python 3.10 or newer
- `playwright`
- `openpyxl`

## Installation

Install the Python packages:

```bash
pip install playwright openpyxl
```

Install the Playwright browser binaries:

```bash
python -m playwright install
```

## Running the Tests

Run the automation script from the `test_automation` folder:

```bash
python IT23836518_test_automation.py
```

If the workbook is not picked up automatically, pass it explicitly:

```bash
python IT23836518_test_automation.py --excel "IT23836518 _Test cases.xlsx"
```

By default, the script writes results back to the input workbook. You can also provide a separate output file:

```bash
python IT23836518_test_automation.py --excel "IT23836518 _Test cases.xlsx" --output "results.xlsx"
```

## Optional Settings

- Set `FRONTEND_URL` if you need to point the tests to a different site.
- Use `--headless` to run the browser without opening a visible window.
- Use `--save-every N` to save the workbook after every N processed rows.

## Notes

- The script searches for input, expected output, actual output, and status columns automatically when possible.
- Results are written into the workbook as `Actual output` and `Status` columns when they are missing.
