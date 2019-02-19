import math
import numpy as np
import integration

# Initializing variables

def f(x, parameters):
    b = parameters[0]
    c = parameters[1]
    f = c * (x ** b)
    return f
"""
def g(x):
    g = x
    return g
"""
# 3x^2 
seed = 123123
xmin = 0
xmax = 3
N = 10000
b = 2
c = 3
z = 2

a = integration.integrate(f, xmin, xmax, N, seed, b, c)
print(a)

"""
import matplotlib.pyplot as plt

accept = a[1]

fig = plt.figure()
ax = fig.add_subplot(111)
x = []
y =[]
for i in accept:
    x.append(i[0])
    y.append(i[1])
ax.scatter(x, y)
plt.show()
"""

