#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 5, Exercise 5

import math
import numpy as np

# Initializing functions and variables
def f(x):
    f = x * math.cos(x)
    return f
seed = 89787
x0 = .7
# Too narrow of dx makes it imposssible to find if the root is outside x0 +/- dx, too big dx and it will take too long
dx = .1
margin = .0001
# f(x)= b
b = .5

# Begining iterative bisection
c = x0
x1 = x0 - dx
x2 = x0 + dx
while f(c) < b - margin or f(c) > b + margin:
    