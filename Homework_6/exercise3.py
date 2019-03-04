#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 6, Exercise 3

import math
import numpy as np


# Getting inputs
print('Enter a value for N:')
N = float(input())
print('Enter a value for mu:')
mu = float(input())
print('Enter a value for sigma:')
sigma = float(input())

# Initializing variables
n_counts = 1000
x1 = 0
x2 = 15
dx = .01
seed = 2143544
x = np.arange(x1, x2, dx)

# Creating lam=S+B for each S
B = []
k = 0
while len(B) != len(range(n_counts)):
    np.random.seed(seed + k)
    b = np.random.normal(mu, sigma)
    if b > 0:
        B.append(b)
        k += 1
    else:
        k += 1

# Getting fraction from poisson
S = []
for i in range(len(x)):
    n_picks = []
    n_accept = []
    for n in range(len(B)):
        p = np.random.poisson(x[i] + B[n])
        n_picks.append(p)
        if p < N:
            n_accept.append(p)
    S.append(len(n_accept) / len(n_picks))

# Checking answer
for j in range(len(x)):
    if S[j] < 0.05:
        print("")
        print("----DONE----")
        print("The 95% confidence interval's lower bound starts at S=" + str(x[j]) + '.')
        print("")
        break