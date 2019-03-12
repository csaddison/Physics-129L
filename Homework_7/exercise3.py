#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 7, Exercise 3

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import ccHistStuff as cc
import itertools as it

# Loading data
txt_file = 'straightTracks.txt'
raw = np.loadtxt(txt_file)

# Organizing data into a contrained track
# Flipping x-y so that we find 
x = (2, 3, 5, 7)
data = []
X0 = []
Y0 = []
for r in raw:
    contrained_track = [(x, x), ((r[2], r[3], r[4], r[5]), (r[6], r[7], r[8], r[9]))]
    data.append(contrained_track)
    X0.append(r[0])
    Y0.append(r[1])

# Fitting curve
Xf = []
def func(vars, m, n, b):
    x1, x2 = vars
    f1 = (m * x1) + b
    f2 = (-n * x2) + b
    return int(str(f1) + str(f2))
    
for trial in data:
    opt = optimize.curve_fit(func, trial[0], trial[1])
    print