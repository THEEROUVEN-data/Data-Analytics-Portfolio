# Python Data Cleaning

Hands-on data cleaning project using Python and Pandas, focused on fixing common real-world data quality issues.

## Objective
Take a deliberately messy dataset and apply standard cleaning techniques to make it analysis-ready.

## Issues Addressed
- Duplicate rows
- Inconsistent text casing and extra whitespace (names, categories)
- Mixed date formats (YYYY-MM-DD, MM/DD/YYYY, DD-MM-YYYY)
- Numeric values stored as text
- Missing values (filled with median)
- Invalid data (negative amounts)

## Files
- `create_messy_data.py` — generates the raw, messy dataset (`messy_data.csv`)
- `clean_messy_data.py` — applies cleaning steps, outputs `cleaned_data.csv`

## Key Cleaning Steps
1. Removed exact duplicate rows
2. Standardized text casing (Title Case) and stripped whitespace
3. Converted `amount` from text to numeric
4. Parsed `order_date` into a consistent datetime format
5. Filled missing `quantity` values with the median
6. Removed rows with invalid (negative) amounts

## Result
Reduced from 12 rows (raw) to 10 rows (cleaned), with consistent formatting across all columns.

## How to Run
1. `python -m venv venv`
2. `venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. `python create_messy_data.py`
5. `python clean_messy_data.py`