import pandas as pd

data = pd.read_csv("data/data.csv", sep=";")

# SORTING

print("sorted by column 'age' \n", data.sort_values("age"))

print("sorted by column 'age': descending \n", data.sort_values("age", ascending=False))

print("sorted by column 'age', 'weight' \n", data.sort_values(["age", "weight"]))

print("sorted by column 'age', 'weight': asc, desc \n", data.sort_values(["age", "weight"], ascending=[True, False]))
