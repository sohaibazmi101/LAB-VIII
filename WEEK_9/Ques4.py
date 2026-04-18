import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())

print("\nShape:", df.shape)
print("\nColumns:", df.columns)

print("\nData Types:\n", df.dtypes)
print("\nInfo:\n")
print(df.info())

print("\nMissing Values:\n", df.isnull().sum())

print("\nStatistical Summary:\n", df.describe())

print("\nDuplicate Rows:", df.duplicated().sum())

corr = df.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", corr)

plt.figure()
plt.matshow(corr)
plt.title("Correlation Matrix")
plt.colorbar()
plt.show()

plt.figure()
df.boxplot(column=["Age", "Salary", "Hours_Studied", "Sleep_Hours"])
plt.title("Boxplot (Original Data)")
plt.show()

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

outliers = df[((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
print("\nOutliers:\n", outliers)

df_clean = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

print("\nCleaned Shape:", df_clean.shape)

plt.figure()
df_clean.boxplot(column=["Age", "Salary", "Hours_Studied", "Sleep_Hours"])
plt.title("Boxplot After Removing Outliers")
plt.show()

df.hist(figsize=(10, 6))
plt.suptitle("Feature Distributions")
plt.show()

plt.figure()
plt.scatter(df["Hours_Studied"], df["Salary"])
plt.xlabel("Hours Studied")
plt.ylabel("Salary")
plt.title("Hours Studied vs Salary")
plt.show()

df_clean.to_csv("clean_students.csv", index=False)