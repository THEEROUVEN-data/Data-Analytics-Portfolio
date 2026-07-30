import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

print("Before cleaning:")
print("Shape:", titanic.shape)
print("Missing values:\n", titanic.isnull().sum())

titanic = titanic.drop(columns=['deck'])
titanic['age'] = titanic['age'].fillna(titanic['age'].median())
titanic['embarked'] = titanic['embarked'].fillna(titanic['embarked'].mode()[0])
titanic['embark_town'] = titanic['embark_town'].fillna(
    titanic['embark_town'].mode()[0])

print("\nAfter cleaning:")
print("Shape:", titanic.shape)
print("Missing values:\n", titanic.isnull().sum())

titanic.to_csv('titanic_cleaned.csv', index=False)
print("\nSaved cleaned data to titanic_cleaned.csv")
