import pandas as pd

data = pd.read_csv("data/data.csv", sep=";")

print(data)

print(data.head())

print(data.info())

ages = data["age"]

print(ages)

print(ages[0])

olderThan30 = data[data.age > 30]

print(olderThan30)

