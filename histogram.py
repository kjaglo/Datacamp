from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("data/data_hist.csv", sep=";")
print(data)

# HISTOGRAM

plt.hist(data.age_f)
plt.show()

# HISTOGRAM: BINS, RANGE

nbins=20
xmin=20
xmax=70
plt.hist(data.age_f,
         bins=nbins,
         range=(xmin,xmax))
plt.show()

# HISTOGRAM: 2 HISTOGRAMS

plt.hist(data.age_f,
         label="Female")
plt.hist(data.age_m,
         label="Male")
plt.title("Age")
plt.legend()
plt.show()

# HISTOGRAM: DENSITY(NORMALIZATION)

plt.hist(data.age_f,
         label="Female",
         density=True,
         alpha=.5)
plt.hist(data.age_m,
         label="Male",
         density=True,
         alpha=.5)
plt.title("Age - normalization")
plt.legend()
plt.show()