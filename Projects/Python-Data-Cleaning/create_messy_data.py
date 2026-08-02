import pandas as pd
import numpy as np

# Create a deliberately messy customer orders dataset
data = {
    'customer_id': [101, 102, 103, 104, 105, 102, 106, 107, 108, 109, 110, 999],
    'customer_name': [' John Smith', 'jane doe', 'ALICE BROWN', 'Bob White', 'Charlie Black',
                      'jane doe', 'Diana Green', 'Ethan Grey', 'fiona blue', ' George Pink ',
                      'Hannah Gold', 'Ian Silver'],
    'order_date': ['2024-01-15', '01/16/2024', '2024-01-17', '17-01-2024', '2024-01-18',
                   '01/16/2024', '2024/01/19', '2024-01-20', '2024-01-21', '2024-01-22',
                   '2024-01-23', '2024-01-24'],
    'amount': ['250.50', '99.99', '1200.00', '45.00', '78.25',
               '99.99', '15000.00', '60.00', '35.50', '89.00', '120.00', '-50.00'],
    'category': ['Electronics', 'electronics', 'Clothing', 'CLOTHING', 'Food',
                 'electronics', 'Electronics', 'Food', 'clothing', 'Food', 'Electronics', 'Food'],
    'quantity': [2, 1, 3, np.nan, 1, 1, 5, 2, np.nan, 1, 2, 1]
}

df = pd.DataFrame(data)
df.to_csv('messy_data.csv', index=False)
print("messy_data.csv created.")
print(df)
