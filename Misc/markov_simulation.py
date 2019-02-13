import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate
import math
from mpl_toolkits.mplot3d import Axes3D 

np.random.seed(224567)

def random_walk(dimension = 2, N = 1000, seed = 224567):
    # Checking dimension
    assert 1 <= dimension <= 3, "Enter a dimension less than or equal to 3"
    # Initializing position
    np.random.seed(seed)
    x_pos = [0]
    x = 0
    y_pos = [0]
    y = 0
    z_pos = [0]
    z = 0
    # Generating moves
    moves = np.random.randint(0, 2 * dimension, N)
    # 1-Dimension
    if dimension == 1:
        for i in range(N):
            y_pos.append(0)
            z_pos.append(0)
            if moves[i] == 0:
                x += 1
                x_pos.append(x)
            elif moves[i] == 1:
                x -= 1
                x_pos.append(x)
    # 2-Dimension
    elif dimension == 2:
        for i in range(N):
            z_pos.append(0)
            if moves[i] == 0:
                x += 1
                x_pos.append(x)
                y_pos.append(y)
            elif moves[i] == 1:
                x -= 1
                x_pos.append(x)
                y_pos.append(y)
            elif moves[i] == 2:
                y += 1
                x_pos.append(x)
                y_pos.append(y)
            elif moves[i] == 3:
                y -= 1
                x_pos.append(x)
                y_pos.append(y)
    # 3-Dimension
    elif dimension == 3:
        for i in range(N):
            if moves[i] == 0:
                x += 1
                x_pos.append(x)
                y_pos.append(y)
                z_pos.append(z)
            elif moves[i] == 1:
                x -= 1
                x_pos.append(x)
                y_pos.append(y)
                z_pos.append(z)
            elif moves[i] == 2:
                y += 1
                x_pos.append(x)
                y_pos.append(y)
                z_pos.append(z)
            elif moves[i] == 3:
                y -= 1
                x_pos.append(x)
                y_pos.append(y)
                z_pos.append(z)
            elif moves[i] == 4:
                z += 1
                x_pos.append(x)
                y_pos.append(y)
                z_pos.append(z)
            elif moves[i] == 5:
                z -= 1
                x_pos.append(x)
                y_pos.append(y)
                z_pos.append(z)
    return [x_pos, y_pos, z_pos]

# Setting up figure and running program to generate data
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
trials = 50
N = 75
dimensions = 3
seeds = np.random.randint(10000, 999999, trials)
data = []
for t in range(trials):
    results = random_walk(dimensions, N, seeds[t])
    data.append(results)
    ax.plot(results[0], results[1], results[2], c = 'goldenrod')
ax.scatter(0, 0, 0, c = 'magenta')
plt.show()

""" # Histogram of results
x_hist = []
y_hist = []
z_base = []
for trial in data:
    for xloc in trial[0]:
        x_hist.append(xloc)
    for yloc in trial[1]:
        y_hist.append(yloc)
    for z in trial[2]:
        z_base.append(z)
xbin = max(x_hist) - min(x_hist)
ybin = max(y_hist) - min(y_hist)

z_height = np.histogram2d(x_hist, y_hist, [xbin, ybin])
xx, yy = np.meshgrid(x_hist, y_hist)
zz, w = np.meshgrid(z_base, z_base)

his = plt.figure(2)
hist = his.add_subplot(111
, projection = '3d'
)
x_val = np.ravel(xx)
y_val = np.ravel(yy)
z_val = np.ravel(zz)
count = np.ravel(z_height)
#hist.hist(x_hist, bins)
hist.bar3d(x_val, y_val, z_val, 1, 1, count)
plt.show()
 """
