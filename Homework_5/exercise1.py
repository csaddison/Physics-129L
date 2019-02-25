#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 5, Exercise 1

import math as m
import matplotlib.pyplot as plt
import integration
from scipy import special
import numpy as np

# Initializing variables. Alpha given in degrees but the function converts inside to radians
alpha_deg = 90
N = 10000
step = 1
seed = 232455
L = 1
g = 9.806
T_0 = (2 * m.pi) * (m.sqrt(L / g))
xmin = 0
xmax = m.pi / 2

# Initializing function
def T(beta, parameters):
    alpha = parameters[0]
    T_0 = parameters[1]
    alpha_rad = alpha * m.pi / 180
    k = m.sin(alpha_rad / 2)
    T = (2 * T_0) / (m.pi * m.sqrt(1 - ((k ** 2) * (m.sin(beta)) ** 2)))
    return T

# Calculating integral to find relative period for each step of alpha
period_plot = []
domain = np.arange(0, alpha_deg + step, step)
for degree in domain:
    period = integration.integrate(T, xmin, xmax, N, seed, degree, T_0)
    period_plot.append(period / T_0)

# Setting up figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(domain, period_plot, c = 'purple')
ax.set_xlim([0,alpha_deg])
ax.set_title(r'Period ratio $T/T_0$ as function of $\alpha$', fontsize = 13)
ax.set_xlabel(r'Maximum swing angle $\alpha$', fontsize = 11)
ax.set_ylabel(r'$\frac{T(\alpha)}{T_0}$', rotation = 0, labelpad = 12, fontsize = 14)
plt.show()