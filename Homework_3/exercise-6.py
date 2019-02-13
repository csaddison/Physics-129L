#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 3, Exercise 6

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate
import math

np.random.seed(12373899)

# Initializing position
N = 1000000
x_pos = [0]
x = 0
y_pos = [0]
y = 0

# Generating moves
moves = np.random.randint(0, 4, N)
for i in range(N):
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
    else:
        y -= 1
        x_pos.append(x)
        y_pos.append(y)

# Setting up figure
fig = plt.figure(1)
ax1 = fig.add_subplot(111)
ax1.scatter(0, 0, c = 'red')
ax1.plot(x_pos, y_pos)
ax1.set(title = 'N = ' + str(N) + ' step Markov Chain', xlabel = 'x', ylabel = 'y')
ax1.set_xlim(min(x_pos) - 2, max(x_pos) + 2)
ax1.set_ylim(min(y_pos) - 2, max(y_pos) + 2)
plt.savefig('markov.png')
plt.show()

# Initializing an animation
anim = plt.figure(2)
ax2 = anim.add_subplot(111)
ax2.set(title = 'N = ' + str(N) + ' step Markov Chain', xlabel = 'x', ylabel = 'y')
ax2.set_xlim(min(x_pos) - 2, max(x_pos) + 2)
ax2.set_ylim(min(y_pos) - 2, max(y_pos) + 2)
ax2.scatter(0, 0, c = 'red')

# Generating update frames
watch_time = 10
frame_rate = math.floor((watch_time * 1000)/ N )
def update(frame):
    x_anim = []
    y_anim = []
    for f in range(frame):
        x_anim.append(x_pos[f])
        y_anim.append(y_pos[f])
    line = ax2.plot(x_anim, y_anim, animated = True, color = 'grey')
    return line
result = animate.FuncAnimation(anim, update, frames = N + 1, interval = frame_rate, blit = True, save_count = 50)
#result.save('markov_anim.mp4', dpi = 180)
#plt.close()
#plt.show()