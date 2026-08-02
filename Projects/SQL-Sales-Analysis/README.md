# SQL Sales Analysis

Sales data analysis using SQL (SQLite) and Python, focused on writing real SQL queries to answer business questions.

## Objective
Build a small sales database and use SQL to extract insights: revenue by category, top customers, regional performance, and high-value orders.

## Files
- `create_database.py` — creates `sales.db` (SQLite) with a sample `sales` table (12 records)
- `run_queries.py` — runs SQL queries against the database and prints results

## Queries Implemented
1. Total revenue by category (GROUP BY, SUM, ORDER BY)
2. Top customers by total spend (GROUP BY, SUM, ORDER BY)
3. Sales count and revenue by region (GROUP BY, COUNT, SUM)
4. High-value orders over $200 (WHERE, calculated column)

## Key Findings
- Jane Doe and John Smith are the top spenders (~$900 and ~$895)
- North region generates the highest revenue ($1,345 across 4 orders)
- 5 orders exceed $200, with two $850 laptop purchases as the largest single orders

## How to Run
1. `python -m venv venv`
2. `venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. `python create_database.py`
5. `python run_queries.py`

## Note
`sales.db` is excluded from version control (`.gitignore`) since it's a generated binary file — running `create_database.py` recreates it locally.