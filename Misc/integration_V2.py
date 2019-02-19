import math
import numpy as np

def integrate_args(func, xmin, xmax, N = 1000, seed = 805415, *args):
    """Returns the numeric apporximation of a 1-dimensional continuous function. The function can take additional arguments but must expect them in touple form such as f(x,[params])
    
    Args:
        func    <function>: The function to integrate over
        xmin    <float>:    Lower bound of integration
        xmax    <float>:    Upper bound of integration
        N       <integer>:  Number of points generated
        seed    <integer>:  Random seed for reproducibility
        *args   <optional>: Arguments that the function expects as a touple.
        Ex: f(x, [params]) --> integrate(f, ..., param1, param2)
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
