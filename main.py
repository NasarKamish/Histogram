import numpy as np
import matplotlib.pyplot as plt

# x values
nums = [0.5, 0.7, 1., 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

plt.hist(nums, bins, color="crimson")
plt.xlabel("Bins")
plt.ylabel("Nums")
plt.title("Histogram of nums against bins")
plt.show()
