import pandas as pd

list = [1,2,3,4,5,6,7,8,9,10]

dictionary = {
    "name": ["Sohaib", "Abid", "Mishal", "Nayef"],
    "age": [25, 30, 35, 40],
    "marks": [85, 90, 78, 92]
}

series = pd.Series(list)
df = pd.DataFrame(dictionary)

print("Series: \n", series)
print("Data Frame: \n", df)