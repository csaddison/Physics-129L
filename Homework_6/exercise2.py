#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 6, Exercise 2

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

"""
# Getting inputs
print('Enter a value for N:')
N = float(input())
print('Enter a value for mu:')
mu = float(input())
print('Enter a value for sigma:')
sigma = float(input())
"""
N, mu, sigma = 5, 3, .5

# Defining function
def f(x, y, N):
    f = np.exp(-1 * (x + y)) * (x + y) ** N
    return f

# Initializing variables
x1 = 0
x2 = 15
num_points = 100
y_trials = 1000
seed = 265748

# Generating points
x = np.linspace(x1, x2, num_points + 1)
raw = []
for i in range(len(x)):
    np.random.seed(seed + i)
    y = np.random.normal(mu, sigma, y_trials)
    y = list(y)
    for y_n in y:
        if y_n <= 0:
            y.remove(y_n)
    g = f(x[i], y, N)
    g_avg = math.fsum(g) / len(y)
    raw.append(g_avg)
norm = raw

# Normalizing by forcing sum(norm) = 1
"""
norm = []
for n in raw:
    norm.append(n / math.fsum(raw))
"""

# Calculating stats
mean, var, std = stats.bayes_mvs(norm, 0.95)
low_bound = mean[1][0]
print("")
print("----DONE----")
print('For your inputs the lower bound of the 95% confidence interval is ' + str(low_bound) + '.')
print("")

# Adding figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, norm)
ax.set_xticks(range(x1, x2 + 1, 3))
ax.set_title(r'Posterior PDF for $(N,\mu,\sigma)=($' + str(N) + ', ' + str(mu) + ', ' + str(sigma) + ')')
ax.set(xlabel = r'$S$', ylabel = r'$P(S)$')
#plt.savefig('posterior_N5.png')
#plt.show()