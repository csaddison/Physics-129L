#
# 2/17/19
# ------------------------------------- INTEGRATION.PY -------------------------------------
"""
A callable module who's main function returns the numeric integral of a 1-dimensional function. Function should be contiuous and finite. Has three methods:
    .integrate():       returns the numeric approcimation
    .point_plot():      returns an array of good vs bad integration points
    .differentiate():  returns the numeric derivative of f(x) at a given x
"""
# Change log:
    # 2/18/19: added support for passing additional *args to function inside integral
    # 2/22/19: added differentiation support
# ---------------------------------------------------------------------------------------------------------------

import math
import numpy as np


# .integrate module
def integrate(func, xmin, xmax, N = 1000, seed = 805415, *args):
    """
    Returns the numeric apporximation of a 1-dimensional continuous function. The function can take additional arguments but must expect them in touple form such as f(x,[params])
    
    Args:
        func    <function>: The function to integrate over
        xmin    <float>:    Lower bound of integration
        xmax    <float>:    Upper bound of integration
        N       <integer>:  Optional, number of points generated
        seed    <integer>:  Optional, seed for reproducibility
        *args   <optional>: Optional, arguments that func() needs
        
    If *args for func() are given then func() must expect a touple, ex:
        f(x, [params])  ---)  integrate(f, ..., param1, param2)
    """
    # Creating random points for M.C. method
    np.random.seed(seed)
    x = np.random.rand(N)
    np.random.seed(seed + 1)
    y = np.random.rand(N)
    # Scaling x points
    for i in range(N):
        x[i] = (xmax - xmin) * x[i] + xmin
    # Determining if the function takes any additional *args and generating curve
    y_vals = []
    if len(args) == 0:
        for i in range(N):
            y_val = func(x[i])
            y_vals.append(y_val)
    else:
        for i in range(N):
            y_val = func(x[i], args)
            y_vals.append(y_val)
    # Finding max[f(x)] and scaling y to y_i < y_max
    ymax = max(y_vals)
    for i in range(N):
        y[i] = (ymax) * y[i]
    # Checking if point is under curve (acceptable)
    accept = []
    for i in range(N):
        if y[i] <= y_vals[i]:
            accept.append((x[i], y[i]))
    # Returning area under curve where area == delta_x * delta_y * success rate
    n = len(accept)
    area = (xmax - xmin) * ymax * (n / N)
    return area


# .point_plot module
def point_plot(function, xmin, xmax, N, seed = 805415, *args):
    """
    Same as .integrate but returns an array whose first element is a list of n succesful points and second is (N - =n) attempted points.
    """
    # Creating random points for M.C. method
    np.random.seed(seed)
    x = np.random.rand(N)
    np.random.seed(seed + 1)
    y = np.random.rand(N)
    # Scaling x points
    for i in range(N):
        x[i] = (xmax - xmin) * x[i] + xmin
    # Determining if the function takes any additional *args and generating curve
    y_vals = []
    if len(args) == 0:
        for i in range(N):
            y_val = func(x[i])
            y_vals.append(y_val)
    else:
        for i in range(N):
            y_val = func(x[i], args)
            y_vals.append(y_val)
    # Finding max[f(x)] and scaling y to y_i < y_max
    ymax = max(y_vals)
    for i in range(N):
        y[i] = (ymax) * y[i]
    # Checking if point is under curve (acceptable)
    succesful = []
    unsuccesful = []
    for i in range(N):
        if y[i] <= y_vals[i]:
            succesful.append((x[i], y[i]))
        else:
            unsuccesful.append((x[i], y[i]))
    # Returning array of succesful and unsuccesful points
    points = [succesful, unsuccesful]
    return points


# .differentiate module
def differentiate(func, x, h = .001):
    """
    Returns numerical approximation of the function at a given x.
    """
    assert h > .0000000001, print("Interval too small")
    fprime = (func(x + h) - func(x - h)) / (2 * h)
    return fprime