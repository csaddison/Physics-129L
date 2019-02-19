#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 4, Exercise 3

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Initializing variables
def f(x, y):
    f = (x**2) + (3 * x * y) + (2 * y**2)
    return f
seed = 123123
xmin = 0
xmax = 1
ymin = 2
ymax = 4
N = 10000

# Generating points
np.random.seed(seed)
x = np.random.rand(N)
np.random.seed(seed + 1)
y = np.random.rand(N)
np.random.seed(seed + 2)
z = np.random.rand(N)

# Scaling x and y points
for i in range(N):
    x[i] = (xmax - xmin) * x[i] + xmin
    y[i] = (ymax - ymin) * y[i] + ymin

# Finding max[f(x,y)]
z_vals = []
for i in range(N):
    z_val = f(x[i], y[i])
    z_vals.append(z_val)
zmax = max(z_vals)

# Scaling z points
for i in range(N):
    z[i] = (zmax) * z[i]

# Checking if point is under curve (acceptable)
accept = []
for i in range(N):
    if z[i] <= z_vals[i]:
        accept.append((x[i], y[i], z[i]))

# Printing volume where vol = area * height * success rate= dx * dy * zmax * (n/N)
n = len(accept)
vol = (xmax - xmin) * (ymax - ymin) * zmax * (n / N)
print('With ' + str(N) + ' points the volume of f(x,y) is approximately ' + str(vol))

# Adding figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for point in accept:
    if point[2] >= f(point[0], point[1]) - 2:
        ax.scatter(point[0], point[1], point[2], c = 'orange')
ax.set(title = 'Surface of f(x,y)', xlabel = 'x', ylabel = 'y', zlabel = 'z')
plt.savefig('doubleintegral.png')
#plt.show()