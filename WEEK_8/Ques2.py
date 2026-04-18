import pandas as pd

data = pd.read_csv('data.csv')

print(data.isna())

print(data.isna().sum())
print(data.isna().sum().sum())

df = pd.DataFrame(data)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].median())
df['Sleep'] = df['Sleep'].fillna(df['Sleep'].mean())
df['Study'] = df['Study'].fillna(df['Study'].mean())
df['Workout Filled'] = df["Workout"].fillna(df['Workout'].mean())
print(df)
df.dropna(inplace=True, axis=1)
print(df)
print("Total Empty cell: ",df.isna().sum().sum())