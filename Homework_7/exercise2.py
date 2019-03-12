#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 7, Exercise 2

# Importing 
import numpy as np
import matplotlib.pyplot as plt
import math
import ccHistStuff as cc

# Initializing data and variables
data_path = 'dataSet.npy'
nbins = 40
cutoff = 20
N = 25
iter_max = 9
p = [10000, .5]

# Setting up figure & generating data
print("")
print("-------------------- INITIAL GUESS (IN RED) --------------------")
print("p = " + str(p))
print("")
fig = plt.figure()
ax = fig.add_subplot(111)
data = np.load(data_path)
bins  = np.linspace(0, cutoff, nbins + 1)
bin_centers = [(bins[1] - bins[0]) / 2 + bin for bin in bins]
bin_centers.pop()
n, bins, patches = ax.hist(data, bins, color = 'grey')


# Defining fit, chi, and diff equations
def exponential_fit(x, p):
    f = p[0] * math.e ** (-p[1] * x)
    return f
def chiSquared(y, y0):
    c = math.fsum(((y0 - y) ** 2) / y0)
    return c
def dydp(i, x, p):
    if i == 1:
        d = math.e ** (-p[1] * x)
    elif i == 2:
        d = -p[0] * x * math.e ** (-p[1] * x)
    return d

# Static matrices
y0 = n[0 : N]
x = np.array(bin_centers[0 : N])
sigma = []
for i in y0:
    sigma.append(math.sqrt(i))
sigma = np.array(sigma)
W = np.diag(1 / sigma)
y_init = np.array([exponential_fit(i, p) for i in x])
ax.plot(x, y_init, color = 'r')

# Iterating fit
for j in range(iter_max):

    # Matricies    
    y = np.array([exponential_fit(i, p) for i in x])
    At = np.array([dydp(1, x, p), dydp(2, x, p)])
    A  = (At.T).copy()
    dy = (np.array([(y - y0)])).T 

    # Multiplying
    step1  = np.matmul(At, W)
    step2 = np.matmul(step1, A)
    step3 = np.linalg.inv(step2)
    step4 = np.matmul(step3, At)
    step5 = np.matmul(step4, W)
    dp  = np.matmul(step5, dy)

    # Reassigning guess, must have lost negative sign somewhere because this only works with the minus
    p[0] -= dp[0][0]
    p[1] -= dp[1][0]
    print(f"---------- ITERATION {j + 1} ----------")
    print(f"    p = {p}")
    print("")

# Printing results
print("")
print("-------------------- FINAL RESULTS (BLUE) --------------------")
print(f"p = {p}")

y_f = np.array([exponential_fit(i, p) for i in x])
chi = chiSquared(y_f, y0)
print(f"Chi squared = {chi}")
print("")

# Finishing fig
ax.set_yscale('log')
ax.set(title = 'Log data fit, Gaussian regime', xlabel = 'X', ylabel = 'Count', xlim = (bin_centers[0], bin_centers[N - 1]))
cc.statBox(ax, x, bins)
ax.plot(x, y, color = 'b')
#plt.savefig('chifit.png')
plt.show()