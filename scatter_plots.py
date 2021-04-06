from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv", sep=";")

# PLOT SCATTER: ALPHA
plt.scatter(data.age, data.weight,
            color="red",
            marker="*",
            alpha=0.5)

plt.xlabel("Age [in years]")
plt.ylabel("Weight [in kg]")

plt.show()
