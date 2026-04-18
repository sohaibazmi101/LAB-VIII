import pandas as pd
import numpy as np

data = {
    "Age": np.random.randint(18,56, 30),
    "marks": np.random.randint(50,100, 30),
    "sleep": np.random.randint(4,10, 30),
    "workout": np.random.randint(0,2, 30),
    "study": np.random.randint(0,2, 30),
}

df = pd.DataFrame(data)

# using iloc we can select specific rows and columns from the DataFrame.

avg_marks = df.iloc[:,1].mean()

print("Average marks:", avg_marks)

# Using iloc to select the first five rows of the third and fourth columns (sleep and workout) and calculate their average value.

avg_value_of_first_five_rows_of_third_and_fourth_columns = df.iloc[:5, 2:4].values.mean()
print("Average value of first five rows of third and fourth columns:", avg_value_of_first_five_rows_of_third_and_fourth_columns)

df["row_sum"] = df.sum(axis=1)
print("DataFrame with row sums:\n", df.head())

max_avg = df.mean(axis=1).max()
print("Maximum average value across rows:", max_avg)