#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 3, Exercise 4

import numpy as np
import math
from math import sin as sin
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mathtext

# Setting up psi
def psi(n_x, n_y, L, x, y):
    k = math.pi / L
    psi = sin(n_x * k * x) * sin(n_y * k * y)
    return psi

# Generating points to feed into psi
L = 1
sample_rate = 200
x = np.linspace(0, L, sample_rate + 1)
y = x
xx, yy = np.meshgrid(x, y)

# Caalculating Z = psi(x,y)
z = []
for j in y:
    l = []
    for i in x:
        a = psi(2, 5, L, i, j)
        l.append(a)
    z.append(l)
zz = np.array(z)

# Setting up the figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.contourf(xx, yy, zz, cmap = cm.coolwarm)
ax.set(title = 'P.D.F. for ' + r'$\Psi (x,y)$' + ' [Red = Positive, Blue = Negative]', xlabel = 'x', ylabel = 'y')
plt.savefig('psi.png')
plt.show()