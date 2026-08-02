import pandas as pd

df = pd.read_csv('messy_data.csv')

print("BEFORE CLEANING")
print("Shape:", df.shape)
print(df)

# 1. Remove exact duplicate rows
df = df.drop_duplicates()

# 2. Clean customer_name: strip whitespace, standardize to Title Case
df['customer_name'] = df['customer_name'].str.strip().str.title()

# 3. Standardize category text case
df['category'] = df['category'].str.strip().str.title()

# 4. Convert amount to numeric (it's currently text)
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# 5. Convert order_date to a single consistent datetime format
df['order_date'] = pd.to_datetime(
    df['order_date'], format='mixed', dayfirst=False)

# 6. Fill missing quantity with median quantity
df['quantity'] = df['quantity'].fillna(df['quantity'].median())

# 7. Flag/remove invalid amounts (negative values are data errors here)
df = df[df['amount'] >= 0]

print("\nAFTER CLEANING")
print("Shape:", df.shape)
print(df)

df.to_csv('cleaned_data.csv', index=False)
print("\nSaved cleaned_data.csv")
