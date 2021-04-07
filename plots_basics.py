from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("data/data.csv", sep=";")

# 1 PLOT

plt.plot(data.age, data.weight, 'o')
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Plot", fontsize=20, color="Gray")
plt.text(3, 5, "Text")
plt.show()


# 2 PLOT LINESTYLE, COLOR, LABEL, LINEWIDTH

#linestyle="-" - regular line
plt.plot(data.id, data.age, label="Age", color="Yellow", linewidth=5, linestyle="-.")
plt.plot(data.id, data.weight, label="Weight", linestyle="--")
plt.plot(data.id, data.shoe_size, label="Shoe size", linestyle=":")
plt.title("Plot 2")
plt.legend()
plt.show()



x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [1/2, 2/2, 3/2, 4/2, 5/2]
y3 = [1/3, 2/3, 3/3, 4/3, 5/3]
y4 = [1/4, 2/4, 3/4, 4/4, 5/4]
y5 = [1/5, 2/5, 3/5, 4/5, 5/5]
y6 = [1/6, 2/6, 3/6, 4/6, 5/6]


# 3 PLOT STYLE
# plt.style.use("fivethirtyeight")
# plt.style.use("ggplot")
# plt.style.use("seaborn")
# plt.style.use("default")
plt.style.use("Solarize_Light2")

# 3 PLOT MARKER

plt.plot(x, y1, label="x", marker="x")  # x-s
plt.plot(x, y2, label="s", marker="s")  # squares
plt.plot(x, y3, label="d", marker="d")  # diamonds
plt.plot(x, y4, label="*", marker="*")  # stars
plt.plot(x, y5, label="o", marker="o")  # circles
plt.plot(x, y6, label="h", marker="h")  # hexagons
plt.legend()
plt.title("Markers")
plt.show()

# print(plt.style.available)  # View all styles


