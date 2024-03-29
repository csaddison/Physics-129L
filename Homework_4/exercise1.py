#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 4, Exercise 1

import numpy as np
import matplotlib.pyplot as plt
import math as m
from ccHistStuff import statBox

# Loading data
x = np.load('dataSet.npy')

# Setting up figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_yscale('log')
ax.set(title = 'Data set array frequency, semi-log', xlabel = 'Value of x', ylabel = 'Frequency of value, log scale')

# Finishing fig
ax.hist(x, m.floor(max(x) * 3))
statBox(ax, x, x)
plt.savefig('datavis.png')
plt.show()
