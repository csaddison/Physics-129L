#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 5, Exercise 2

import math
import numpy as np
import matplotlib.pyplot as plt

# Setting image size and initializing variables
xsize = 640
ysize = 400
x_range = 1.6
c = -.79 + .56j
aspect_ratio = xsize / ysize
y_range = x_range / aspect_ratio 

# Defining f(z)
def f(x, y, c):
    z = complex(x, y)
    f = z ** 2 + c
    return f

# Assigning coordinates to each pixel
# Note: array indexing goes array[row,col] == array[y,x]
x = np.linspace(-1 * x_range, x_range, xsize)
y = np.linspace(-1 * y_range, y_range, ysize)
xx, yy = np.meshgrid(x, y)
z_0 = np.zeros((ysize, xsize))

# Resursion on each pixel. Reassigns z and n each iteration until abs(z) >= 2 or n == 255
for x_i in range(xsize):
    for y_i in range(ysize):
        z = complex(xx[y_i, x_i], yy[y_i, x_i])
        n = 0
        while abs(z) < 2 and n < 255:
            z_n = f(z.real, z.imag, c)
            z = complex(z_n.real, z_n.imag)
            n += 1
        z_0[y_i, x_i] = n

# Setting up figure
dpi = 72
fig = plt.figure(figsize = (xsize / dpi, ysize / dpi))
ax = fig.add_subplot(111)
ax.imshow(z_0, cmap = 'afmhot')
ax.set(title = 'Julia set for c = ' + str(c), xlabel = 'X pixels from -' + str(x_range) + ' to ' + str(x_range), ylabel = 'Y pixels from -' + str(y_range) + ' to ' + str(y_range))
plt.savefig('juliaset.png')
plt.show()