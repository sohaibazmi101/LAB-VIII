import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students.csv')

# Boxplot
plt.figure()
df.boxplot(column=["Age", "Salary", "Hours_Studied", "Sleep_Hours"])
plt.title("Boxplot of Dataset")
plt.savefig("plot.png")
plt.show()

# IQR calculation
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[((df < lower) | (df > upper)).any(axis=1)]
print("Outliers:\n", outliers)

clean_df = df[~((df < lower) | (df > upper)).any(axis=1)]

print("\nClean Data:\n", clean_df)

plt.figure()
clean_df.boxplot(column=["Age", "Hours_Studied", "Sleep_Hours"])
plt.title("Boxplot After Removing Outliers")
plt.savefig("plot2.png")
plt.show()