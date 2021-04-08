import pandas as pd

data = pd.read_csv("data/data.csv", sep=";")

print("first 5 rows: \n", data.head())

print("basic info: \n", data.info())

print("(rows, cols): ", data.shape)

# count - non-missing values
print("statistics for numerical columns: \n", data.describe())

# 2d array of values
print("values: \n", data.values)

# column names
print("columns: \n", data.columns)

# row numbers or names
print("index: \n", data.index)

