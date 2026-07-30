import pandas as pd

titanic = pd.read_csv('titanic_cleaned.csv')

print("Survival counts:")
print(titanic['survived'].value_counts())

print("\nSurvival rate by sex:")
print(titanic.groupby('sex')['survived'].mean())

print("\nSurvival rate by class:")
print(titanic.groupby('pclass')['survived'].mean())

print("\nSurvival rate by sex and class:")
print(titanic.groupby(['sex', 'pclass'])['survived'].mean())
