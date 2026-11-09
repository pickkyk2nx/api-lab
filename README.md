# API lab

This repository contains a pytest suite for the QuickPizza API used in the ITCS386 API testing lab. The tests cover the guided basics, login and ownership checks, and the boundary-value and input-space-partitioning checks from Part A.

## Setup

1. Create and activate a virtual environment.
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
2. Install the requirements.
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Run the suite.
   ```bash
   pytest -v
   ```
4. Save the full HTML report.
   ```bash
   pytest -v --html=report.html --self-contained-html
   ```

## Input domain model for POST /api/ratings

| Characteristic | Blocks | Example values in the test suite | Covered by |
| --- | --- | --- | --- |
| C1 value of stars | below 1, 1 to 5, above 5 | 0, 3, 6 | test_stars_out_of_range[0], test_base_choice_is_saved, test_stars_out_of_range[6] |
| C2 type of stars | whole number, decimal, text, missing | 3, 3.5, "3", no field | test_base_choice_is_saved, test_stars_decimal_is_rejected, test_stars_text_is_rejected, test_missing_stars_is_rejected |
| C3 pizza exists | yes, no | pizza_id, 999999999 | test_base_choice_is_saved, test_unknown_pizza_is_rejected |
| C4 token | valid, none, wrong length | auth, no header, short token | test_base_choice_is_saved, test_rating_without_token_is_rejected, test_rating_with_short_token_is_rejected |

## Repository layout

- conftest.py: shared session and fixtures
- test_names.py, test_tools.py, test_pizza.py: guided API basics
- test_users.py, test_ratings.py, test_refused.py: login, rating lifecycle and refusal checks
- test_excluded_tools.py: excluded-tools coverage and the known defect marked with xfail
- test_create_rating.py, test_update_rating.py, test_rating_owner.py: Part A checks
- RESULTS.md: recorded outputs and reflection notes
- report.html: generated HTML report from the full pytest run
