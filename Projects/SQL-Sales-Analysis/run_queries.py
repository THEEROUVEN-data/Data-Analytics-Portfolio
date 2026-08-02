import sqlite3
import pandas as pd

conn = sqlite3.connect('sales.db')

# Query 1: Total revenue per category
print("Total revenue by category:")
q1 = """
SELECT category, SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC
"""
print(pd.read_sql_query(q1, conn))

# Query 2: Top customers by total spend
print("\nTop customers by total spend:")
q2 = """
SELECT customer_name, SUM(quantity * unit_price) AS total_spent
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC
"""
print(pd.read_sql_query(q2, conn))

# Query 3: Sales by region
print("\nSales count and revenue by region:")
q3 = """
SELECT region, COUNT(*) AS num_orders, SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC
"""
print(pd.read_sql_query(q3, conn))

# Query 4: Orders above a certain amount
print("\nHigh-value orders (over $200):")
q4 = """
SELECT order_id, customer_name, product, (quantity * unit_price) AS order_total
FROM sales
WHERE (quantity * unit_price) > 200
ORDER BY order_total DESC
"""
print(pd.read_sql_query(q4, conn))

conn.close()
