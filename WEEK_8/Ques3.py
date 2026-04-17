import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
print(data)

df = df.rename(columns={
    'Name': 'name',
    'Sleep': 'sleep time'
})

print(df.head())

print(df.dtypes)

df['Age'] = df['Age'].astype('Int64')
df['Study'] = df['Study'].astype(str)
print(df.dtypes)

print(df)