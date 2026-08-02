import sqlite3

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS sales')
cursor.execute('''
CREATE TABLE sales (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    unit_price REAL,
    order_date TEXT,
    region TEXT
)
''')

sales_data = [
    (1, 'John Smith', 'Laptop', 'Electronics', 1, 850.00, '2024-01-05', 'North'),
    (2, 'Jane Doe', 'Mouse', 'Electronics', 2, 25.00, '2024-01-06', 'South'),
    (3, 'Alice Brown', 'Desk Chair', 'Furniture', 1, 150.00, '2024-01-07', 'North'),
    (4, 'Bob White', 'Monitor', 'Electronics', 2, 300.00, '2024-01-08', 'East'),
    (5, 'Charlie Black', 'Notebook', 'Stationery', 10, 2.50, '2024-01-09', 'West'),
    (6, 'John Smith', 'Keyboard', 'Electronics', 1, 45.00, '2024-01-10', 'North'),
    (7, 'Diana Green', 'Desk', 'Furniture', 1, 220.00, '2024-01-11', 'South'),
    (8, 'Ethan Grey', 'Pen Set', 'Stationery', 5, 8.00, '2024-01-12', 'East'),
    (9, 'Jane Doe', 'Laptop', 'Electronics', 1, 850.00, '2024-01-13', 'South'),
    (10, 'Fiona Blue', 'Bookshelf', 'Furniture', 1, 180.00, '2024-01-14', 'West'),
    (11, 'George Pink', 'Monitor', 'Electronics', 1, 300.00, '2024-01-15', 'North'),
    (12, 'Hannah Gold', 'Notebook', 'Stationery', 20, 2.50, '2024-01-16', 'East'),
]

cursor.executemany(
    'INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?, ?)', sales_data)
conn.commit()
conn.close()

print("sales.db created with", len(sales_data), "records.")
