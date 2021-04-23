# SUBSETTING

print(" 'age' \n", data["age"])

print(" 'age' and 'sex' \n", data[["age", "sex"]])

print(" is 'age' > 40 \n", data["age"] > 40)

print(" 'age' > 40 \n", data[data["age"] > 40])

print(" K \n", data[data["sex"] == "K"])

#date too: sth > "YYYY-MM-DD"

print(" K \n", data[data["sex"] == "K"])

