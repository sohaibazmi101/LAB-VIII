import pandas as pd

data = pd.read_csv('data.csv')

print("Top 5 rows of the data frame: \n", data.head())
print("Top bottom rows of the data frame: \n", data.tail())
print("Data Information: \n", data.info())
