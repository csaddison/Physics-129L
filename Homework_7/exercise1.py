#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 7, Exercise 1

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# Loading data
txt_file = 'straightTracks.txt'
raw = np.loadtxt(txt_file)

# Separating data into tracks 0 and 1 with lists of [(xi1,xi2,xi3,xi4), (yi1,yi2,yi3,yi4)]
x = (2, 3, 5, 7)
data = []
X0 = []
Y0 = []
for r in raw:
    track0 = [x, (r[2], r[3], r[4], r[5])]
    track1 = [x, (r[6], r[7], r[8], r[9])]
    data.append([track0, track1])
    X0.append(r[0])
    Y0.append(r[1])

# Fitting curve
X1 = []
X2 = []
Xavg = []
def func(x, m, b):
    f = (m * x) + b
    return f
for trial in data:
    opt1 = optimize.curve_fit(func, trial[0][0], trial[0][1])
    X1.append(opt1[0][1])
    opt2 = optimize.curve_fit(func, trial[1][0], trial[1][1])
    X2.append(opt2[0][1])
    Xavg.append((opt1[0][1] + opt2[0][1]) / 2)

# Preparing data for histogram
x1_x0 = []
x2_x0 = []
xa_x0 = []
for i in range(len(X0)):
    x1_x0.append(X1[i] - X0[i])
    x2_x0.append(X2[i] - X0[i])
    xa_x0.append(Xavg[i] - X0[i])


# Adding plot of tracks
fig = plt.figure()
plot = fig.add_subplot(131)
for n in range(10):
    plot.plot(data[n][0][0], data[n][0][1], color = '.6')
    plot.plot(data[n][1][0], data[n][1][1], color = '.6')
plot.set(title = 'First 10 collisions')

# Adding histogram of error
hist1 = fig.add_subplot(132)
hist2 = fig.add_subplot(133)
hist1.hist((x1_x0, x2_x0), 20, stacked = True)
hist2.hist(xa_x0, 20)
hist1.set(xlim =  (-.05, .05), title = r'$(x_1/x_2 - x_0 )$')
hist2.set(xlim =  (-.05, .05), title = r'$x_a - x_0$')
plt.show()