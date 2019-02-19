#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 4, Exercise 2

import math
import numpy as np
import matplotlib.pyplot as plt
import argparse

# The genPoisson.py script was throwing a bunch of errors for me and it seemed more difficult to debug the code than it was to start fresh

# Initializing variables
seed = 283901283
N = 100
n_counts = 1000
g_mean = 100
delta = .5
sigma = delta * g_mean
# PDF = Log Normal[mean = b, sigma = delta]

# Calculating means for background noise
np.random.seed(seed)
x = np.random.rand(N)
def CDF(x, mean, sigma):
    f_x = math.erfc((mean - math.log(x)) / (math.sqrt(2) * sigma)) / 2
    return f_x
p_means = []
for n in range(N):
    p_means.append(CDF(5 * sigma * x[n], g_mean, sigma))

# Using distributed means to generate noisy poissons
noisy_poissons = []
for n in range(N):
    noisy_poissons.append(np.random.poisson(p_means[n] * g_mean, n_counts))
poisson = np.ravel(noisy_poissons)

# Setting up figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(poisson, math.floor(max(poisson)))
ax.set(title = 'Poisson distribution with Log-Normal noise', xlabel = 'Value', ylabel = 'Count')
plt.savefig('noisypoisson.png')
plt.show()