#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 5, Exercise 3

import math
import numpy as np
import matplotlib.pyplot as plt
from ccHistStuff import statBox

# Loading data
txt_file = 'mass.txt'
bins = 20
data = np.loadtxt(txt_file)

# Setting up figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(data, bins)
ax.set(title = 'Mass frequency distribution', xlabel = 'Mass', ylabel = 'Frequency of value')
statBox(ax, data, data)
plt.show()