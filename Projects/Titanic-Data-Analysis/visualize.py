import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv('titanic_cleaned.csv')

plt.figure()
sns.countplot(data=titanic, x='survived')
plt.title('Survival Count (0 = Died, 1 = Survived)')
plt.savefig('chart_survival_count.png')

plt.figure()
sns.barplot(data=titanic, x='sex', y='survived')
plt.title('Survival Rate by Sex')
plt.savefig('chart_survival_by_sex.png')

plt.figure()
sns.barplot(data=titanic, x='pclass', y='survived')
plt.title('Survival Rate by Class')
plt.savefig('chart_survival_by_class.png')

plt.figure()
sns.barplot(data=titanic, x='pclass', y='survived', hue='sex')
plt.title('Survival Rate by Class and Sex')
plt.savefig('chart_survival_by_class_and_sex.png')

print("Charts saved as PNG files.")
