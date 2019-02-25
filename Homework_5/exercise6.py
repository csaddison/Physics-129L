#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 5, Exercise 6

import math
import numpy as np
import matplotlib.pyplot as plt

# Initializing variables
print("Enter a R-C time constant:")
tau = float(input())
# You can enter an input value for tau or use the cutoff frequency which sets the RC accordingly
# Very steady when fc >> fv, where fv is the frequency of V_in. At that point the low pass filter just passes all of the band
cutoff_freq = .3
time_range = 100
step_size = .001
graph_cut_time = 10
RC = 1 / (2 * math.pi * cutoff_freq)
# Note: fc = .3 --> tau = .53

# Defining function for differential equation dV/dt = f(t,V)
def f(t, Vout, tau):
    # Frequency and amplitude of 1. Since we're dealing in microseconds, our frequency is actually 1Mhz
    if math.ceil(t) % 2 == 0:
        V_in = -1
    else:
        V_in = 1
    d = (V_in - Vout) / tau
    return d

# Setting up points
x = np.arange(0, time_range + step_size, step_size)
y = [0]

# Runge-Kutta method
h = step_size
for n in range(len(x) - 1):
    k1 = h * f(x[n], y[n], tau)
    k2 = h * f(x[n] + (h / 2), y[n] + (k1 / 2), tau)
    k3 = h * f(x[n] + (h / 2), y[n] + (k2 / 2), tau)
    k4 = h * f(x[n] + h, y[n] + k3, tau)
    y_n = y[n] + ((k1 + (2 * k2) + (2 * k3) + k4) / 6)
    y.append(y_n)

# Splitting 0-10us data and 10-100us data
index = int(graph_cut_time / step_size)
xlow = x[0:index + 1]
ylow = y[0:index + 1]
xhigh = x[index:]
yhigh = y[index:]

# Simulating RC falloff
e = []
for i in xlow:
    e.append(math.exp(-i / tau))

# Plotting curves
fig = plt.figure(figsize = (10, 8))
up = fig.add_subplot(211)
low = fig.add_subplot(212)
plt.subplots_adjust(hspace = .7)
up.plot(xlow, ylow, color = 'b')
up.plot(xlow, e, color = 'g', linestyle = '--')
up.set(title = r"$\tau=$" + str(tau) + r" low-pass filter with $e^{-t / RC}$ falloff, 0-" + str(graph_cut_time) + r"$\mu s$", xlabel = r"Time, $\mu s$", ylabel = "Voltage")
low.plot(xhigh, yhigh, color = 'b')
low.set(title = r"$\tau=$" + str(tau) + r" low-pass filter steady state, " + str(graph_cut_time) + "-" + str(time_range) + r"$\mu s$", xlabel = r"Time, $\mu s$", ylabel = "Voltage")
plt.show()