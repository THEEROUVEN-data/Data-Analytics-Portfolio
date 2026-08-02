# Excel Sales Dashboard

Interactive sales dashboard built in Excel using PivotTables and PivotCharts.

## Objective
Analyze 6 months of sample sales data (90 records) across products, categories, regions, and time, and present findings in a single-page dashboard.

## Files
- `generate_data.py` — generates the sample dataset (`sales_data.csv`)
- `sales_dashboard.xlsx` — Excel workbook with raw data, PivotTables, and Dashboard sheet

## Dashboard Structure
- **sales_data** — raw data as an Excel Table, with a calculated `revenue` column (quantity × unit_price)
- **Revenue_by_Category** — PivotTable + column chart
- **Revenue_by_Region** — PivotTable + column chart
- **Revenue_by_Month** — PivotTable + line chart (trend over time)
- **Dashboard** — all 3 charts combined on one summary sheet

## Skills Demonstrated
- Excel Tables
- PivotTables (Rows, Values, Sum aggregation)
- PivotCharts (column, line)
- Calculated fields
- Dashboard layout/design

## How to Regenerate the Data
```
python generate_data.py
```