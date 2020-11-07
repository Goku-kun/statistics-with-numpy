# Plotting a normal distribution curve using Histogram

# It will be a unimodal symmetric histogram with center=0 and std=1 as mentioned in np.random.normal method as arguments
import numpy as np
from matplotlib import pyplot as plt

data = np.random.normal(0, 1, size=10000)
plt.hist(data)
plt.show()