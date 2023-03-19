# Creates a histogram of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x ** 3 in the range [0, 10], 
# on one set of axes.

# Author = Kirstin Barnett

import numpy as np
import matplotlib.pyplot as plt

# Histogram
hist_mean = 5
hist_st_dev = 2
number_of_values = 1000

normal_data = np.random.normal(loc = hist_mean, scale = hist_st_dev, size = number_of_values)

plt.hist (normal_data)

# Power
min = 0
max = 10

xpoints = np.array(range(min,max))
ypoints = xpoints ** 3

plt.plot(xpoints, ypoints, color = 'r')

# Plot
plt.title("Weekly task 8 - histogram of a normal distribution and line of x^3")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["x to the power 3", "normal distribution",])
plt.show()