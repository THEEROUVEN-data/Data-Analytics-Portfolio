import seaborn as sns
import pandas as pd

# Load the Titanic dataset (built into seaborn — no download needed)
titanic = sns.load_dataset('titanic')

# Always start by looking at the shape and first few rows
print("Shape (rows, columns):", titanic.shape)
print("\nFirst 5 rows:")
print(titanic.head())

# Check data types and missing values — this tells you what needs cleaning
print("\nData info:")
print(titanic.info())

print("\nMissing values per column:")
print(titanic.isnull().sum())
