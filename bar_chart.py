from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("data/data_bar.csv", sep=";")

# BAR VERTICAL
plt.bar(data.sex, data.avg_cat)
plt.xlabel("Sex")
plt.ylabel("Cat")
plt.show()

# BAR HORIZONTAL
plt.barh(data.sex, data.avg_cat)
plt.xlabel("Height")
plt.ylabel("Cat")
plt.show()

# BAR + ERROR
plt.bar(data.sex, data.avg_cat,
        yerr=data.std_cat)
plt.xlabel("Sex")
plt.ylabel("Cat")
plt.show()


# STACKED BAR
plt.bar(data.sex, data.avg_dog, label="Dog")
plt.bar(data.sex, data.avg_cat,
        bottom=data.avg_dog,
        label="Cat")
plt.xlabel("Sex")
plt.ylabel("Pet")
plt.legend()
plt.show()


