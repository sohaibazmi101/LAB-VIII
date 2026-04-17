import pandas as pd

data = pd.read_csv('data.csv')

print(data.isnull())
print(data.isnull().sum())

print(data.isnull().sum().sum())

print(data.isna().sum())