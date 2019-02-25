#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 5, Exercise 5

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate

# Initializing function and variables
def f(x):
    f = x * math.cos(x)
    return f
# Point of interest
x0 = .7
# Initial margin
dx = .1
# Desired precision
dy = .0001
# Desired y-value
y = .5
# Maximum steps to prevent infinite recursion
max_steps = 30

# Initializing additional variables
c = x0
x1 = x0 - dx
x2 = x0 + dx

# Creating point to plot
x = np.arange(x1, x2, ((x0 + dx)  - (x0 - dx)) / max_steps)
fx = []
for x_i in x:
    fx.append(f(x_i))

# Adding plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, fx, color = '.5')
ax.scatter(c, f(c), color = 'r')
ax.set(title = "Bisection  method for xCos(x) = .5", xlabel = 'x', ylabel = 'y', xlim =[x1, x2], ylim = [f(x1), f(x2)])

# Begining recursion
for n in range(max_steps):
    # Checking if f(c) is within margin
    if y - dy <= f(c) <= y + dy:
        print("    ")
        print('----DONE----')
        print('f(' + str(c) + ') = ' + str(f(c)))
        print(str(n + 1) + ' iterations')
        print("    ")
        break
    elif f(c) < y - dy:
        x1 = c
    elif f(c) > y + dy:
        x2 = c
    c = (x1 + x2) / 2
    ax.scatter(c, f(c), color = 'r')
ax.plot([x0 - dx, x0 + dx], [f(c), f(c)], color = 'g')
plt.show()