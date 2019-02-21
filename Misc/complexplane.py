#
# 2/19/19
# ------------------------------------- COMPLEXPLANE.PY -------------------------------------
"""
Create and plot fractals and complex functions. Contains three methods:

    .createplane:   Creates an xy grid and a null array zmap
    .cgen:          Generates random values of c for julia set
    .julia:         Generates Julia set fractals for a given c
    .complexfunc:   Returns a map of f(z) over the complex plane
    .fracplot:      Plots a colormap of a given zmap
"""
# ---------------------------------------------------------------------------------------------------------------

import math
import numpy as np
import matplotlib.pyplot as plt


# Returns the quadratic julia set for a given c
def julia(plane, c, smooth = False):
    # Defining the quadratic julia generating function f(z)
    def f(z, c):
        f = z ** 2 + c
        return f
    # Importing plane
    xx = plane[0]
    yy = plane[1]
    zmap = plane[2]
    xsize = len(xx[0])
    ysize = len(yy)
    # Resursion on each pixel. Reassigns z and n each iteration until abs(z) >= 2 or n == 255
    for x_i in range(xsize):
        for y_i in range(ysize):
            z = complex(xx[y_i, x_i], yy[y_i, x_i])
            n = 0
            # Checking if smooth is enabled
            if smooth == False:
                while abs(z) < 2 and n < 255:
                    z_n = f(z, c)
                    z = complex(z_n.real, z_n.imag)
                    n += 1
                zmap[y_i, x_i] = n 
            elif smooth == True:
                # Smoothing subtracts fractional amount from iteration count
                while abs(z) <= 2 and n < 255:
                    z_n = f(z, c)
                    z = complex(z_n.real, z_n.imag)
                    n += 1
                zmap[y_i, x_i] = n - math.log(abs(z), 2)
    # Returns array of zmap  
    return zmap


# Applies a given function over complex plane and returns z-map
def complexfunc(plane, func, *args):
    # Importing plane
    xx = plane[0]
    yy = plane[1]
    zmap = plane[2]
    xsize = len(xx[0])
    ysize = len(yy)
    # Applies func() to complex plane
    for x_i in range(xsize):
        for y_i in range(ysize):
            z = complex(xx[y_i, x_i], yy[y_i, x_i])
            # Checking if func() takes additional parameters
            if len(args) == 0:
                z_0 = func(z)
            else:
                z_0 = func(z, args)
            # Appending value |z| to array
            zmap[y_i, x_i] = abs(z_0)  
    # Returns array of z-map  
    return zmap

  
# Creates and returns complex xy plane and empty zmap. Domain is x-distance +/- from the center. Center expects a touple and defaults to (0,0)
def createplane(x_res, y_res, domain = 2, center = (0, 0)):
    # Determining size of image
    aspect_ratio = x_res / y_res
    y_range = domain / aspect_ratio
    # Assigning coordinates to each pixel
    # Note: array indexing goes array[row,col] == array[y,x]
    x = np.linspace(center[0] - domain, center[0] + domain, x_res)
    y = np.linspace(center[1] - y_range, center[1] + y_range, y_res)
    xx, yy = np.meshgrid(x, y)
    zz = np.zeros((y_res, x_res))
    return [xx, yy, zz]


# Automatically plots the fractal or function as a colormap
def fracplot(zmap, colormap = 'plasma', show = True):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(zmap, cmap = colormap)
    # Checks if user wants the plot returned for additional manipulation
    if show == False:
        return ax
    else:
        plt.show()


# Generates random values of c for julia set
def cgen(seed, xlim = 1.5, ylim = 1):
    np.random.seed(seed)
    choice = np.random.rand(4)
    x = choice[0] * xlim
    y = choice[1] * ylim
    if choice[2] >= .5:
        x = -x
    if choice[3] >= .5:
        y = -y
    return complex(x, y)