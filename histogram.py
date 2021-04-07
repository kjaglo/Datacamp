from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("data/data_hist.csv", sep=";")


# HISTOGRAM

plt.hist(data.age_f)
plt.show()

# HISTOGRAM: BINS, RANGE

nbins=20
xmin=20
xmax=70

plt.hist(data.age_f,
         bins=nbins,
         range=(xmin, xmax))

plt.show()

# HISTOGRAM: 2 HISTOGRAMS

plt.hist(data.age_f,
         alpha=.5,
         label="Female")
plt.hist(data.age_m,
         alpha=.5,
         label="Male")
plt.title("Age")
plt.xlabel("Years")
plt.legend()
plt.show()

# HISTOGRAM: 2 HISTOGRAMS + DENSITY(NORMALIZTION)

plt.hist(data.age_f,
         alpha=.5,
         label="Female",
         density=True)
plt.hist(data.age_m,
         alpha=.5,
         label="Male",
         density=True)
plt.title("Age - normalization")
plt.xlabel("Years")
plt.legend()
plt.show()

