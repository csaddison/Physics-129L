import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Initializing variables
sigma = 10
rho = 32
beta = 8 / 3
x0 = 1
y0 = 2
z0 = 3
timescale = 50
dt = .01

# Defining evolution function
def f(R, t):
    x = R[0]
    y = R[1]
    z = R[2]
    f = [sigma * (y - x), (x * (rho - z)) - y, (x * y) - (beta * z)]
    return f

# Solving ODE states
R = [x0, y0, z0]
t = np.arange(0, timescale + dt, dt)
states = odeint(f, R, t)
X = states[:, 0]
Y = states[:, 1]
Z = states[:, 2]

# Adding plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(X, Y, Z)
plt.show()