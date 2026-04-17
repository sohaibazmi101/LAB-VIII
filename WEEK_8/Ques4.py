import pandas as pd

data = pd.read_csv("data.csv")

df = pd.DataFrame(data)

# clean_df = df.dropna()

# clean_df = df[df['Marks'].notna()]

# clean_df = df[df['Marks'] >= 50]

# clean_df = df[(df['Marks'] > 50) & (df['Age'] < 23)]

clean_df = df.drop(columns='Workout')

print(clean_df)