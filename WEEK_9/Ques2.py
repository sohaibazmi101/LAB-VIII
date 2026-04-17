import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

corr = df.corr(numeric_only=True)
print("Correlation:")
print(corr)

upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))

threshold = 0.8

to_drop = [col for col in upper.columns if any(upper[col] > threshold)]

clean_df = df.drop(columns=to_drop)

print("Clean DF: ")

print(clean_df)

print("Columns Dropped: ", to_drop)