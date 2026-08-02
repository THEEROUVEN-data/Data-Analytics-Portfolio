import csv
import random

random.seed(42)

products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor',
            'Desk Chair', 'Notebook', 'Pen Set', 'Bookshelf']
categories = {'Laptop': 'Electronics', 'Mouse': 'Electronics', 'Keyboard': 'Electronics',
              'Monitor': 'Electronics', 'Desk Chair': 'Furniture', 'Notebook': 'Stationery',
              'Pen Set': 'Stationery', 'Bookshelf': 'Furniture'}
regions = ['North', 'South', 'East', 'West']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

rows = []
order_id = 1
for month in months:
    for _ in range(15):
        product = random.choice(products)
        rows.append([
            order_id, month, product, categories[product],
            random.choice(regions), random.randint(1, 10),
            round(random.uniform(10, 900), 2)
        ])
        order_id += 1

with open('sales_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['order_id', 'month', 'product',
                    'category', 'region', 'quantity', 'unit_price'])
    writer.writerows(rows)

print(f"sales_data.csv created with {len(rows)} rows.")
