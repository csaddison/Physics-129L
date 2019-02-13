#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 3, Exercise 2

def f(x):
    y = (1 - x) * x **2
    return y

def derivitive(function_plus, function_minus, interval):
    i = (function_plus - function_minus)/interval
    return i

