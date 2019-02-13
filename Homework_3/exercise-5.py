#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 3, Exercise 5

import numpy as np
import math
import matplotlib.pyplot as plt

np.random.seed(223789)
N = 10000

def x_R(R):
    x = .25 * (math.sqrt(24 * R + 1) - 1)
    return x

x_list = []
points = np.random.rand(N).tolist()
for n in points:
    y = x_R(n)
    x_list.append(y)

# Checking the PDF
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(points, x_list)
ax.set(title = 'PDF distributed points', xlabel = 'x', ylabel = 'F(x)')
plt.savefig('pdf.png')
plt.show()