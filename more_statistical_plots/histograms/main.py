import matplotlib.pyplot as plt
import numpy as np

size = 1000
normal_sample = np.random.normal(size=size)

# Create a probabilty density function approximation using a histogram
plt.hist(normal_sample, bins=1 + int(np.log2(len(normal_sample))), density=True)

plt.show()

