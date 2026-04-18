import pandas as pd

data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

# using describe() method we can see statistical summary

print(df.describe())