#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 3, Exercise 1

import numpy as np
import math
from scipy import stats

def pi_approximator(N, seed = 224567):
    # Generating random points
    np.random.seed(seed)
    points = np.random.rand(N, 2)
    x = points[:, 0]
    y = points[:, 1]
    # Determining succeses with r <= 1
    successes = []
    for i in range(len(x)):
        if math.sqrt(x[i]**2 + y[i]**2) <= 1:
            successes.append((x[i], y[i]))
    # Computing pi and accuracy
    f = len(successes) / N
    pi = 4 * f
    acc =  abs((pi - math.pi) / math.pi)
    sigma = math.sqrt((f * (1 - f)) / N)
    pull = (pi - math.pi) / sigma
    return [N, pi, acc, pull]

# Conducting 5 trials
t1 = pi_approximator(100, 224567)
t2 = pi_approximator(1000, 346789)
t3 = pi_approximator(10000, 196821)
t4 = pi_approximator(100000, 178943)
t5 = pi_approximator(1000000, 555321)
trials = [t1, t2, t3, t4, t5]
for t in trials:
    print('With N = ' + str(t[0]) + ' points, pi is approxmately ' + str(t[1]) + '. This is within ' + str(round(100 * t[2], 3)) + '% of pi with a pull of ' + str(round(t[3], 3)) + '.')

# Accuracy stats
p_squared = [t1[3]**2, t2[3]**2, t3[3]**2, t4[3]**2, t5[3]**2]
chi = math.fsum(p_squared)
prob = 1 -stats.chi2.cdf(chi, 5)
print('This leads to a chi-squared value of ' + str(round(chi, 3)) + '. The probability of a larger chi-squared value is ' + str(round(100 * prob, 3)) + '%.')