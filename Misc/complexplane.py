#
# 2/19/19
# ------------------------------------- COMPLEXPLANE.PY -------------------------------------

import math
import numpy as np
import matplotlib.pyplot as plt

# Returns the quadratic julia set for a given c
def julia(c, x_res, y_res, x_range):
  # Determining size of image
  aspect_ratio = x_res / y_res
  y_range = x_range / aspect_ratio
  # Defining the quadratic julia generating function f(z)
  def f(z, c):
    f = z ** 2 + c
    return f
  # Assigning coordinates to each pixel
  # Note: array indexing goes array[row,col] == array[y,x]
  x = np.linspace(-1 * x_range, x_range, x_res)
  y = np.linspace(-1 * y_range, y_range, y_res)
  xx, yy = np.meshgrid(x, y)
  zz = np.zeros((y_res, x_res))
  # Resursion on each pixel. Reassigns z and n each iteration until abs(z) >= 2 or n == 255
  for x_i in range(x_res):
     for y_i in range(y_res):
        z = complex(xx[y_i, x_i], yy[y_i, x_i])
        n = 0
        while abs(z) < 2 and n < 255:
            z_n = f(z, c)
            z = complex(z_n.real, z_n.imag)
            n += 1
        zz[y_i, x_i] = n  
   # Returns array of z-map  
   return zz
  
  
# Applies a given function over complex plane and returns z-map
def complexfunc(func, x_res, y_res, domain, *args):
  # Determining size of image
  aspect_ratio = x_res / y_res
  y_range = x_range / aspect_ratio
  # Assigning coordinates to each pixel
  # Note: array indexing goes array[row,col] == array[y,x]
  x = np.linspace(-1 * x_range, x_range, xsize)
  y = np.linspace(-1 * y_range, y_range, ysize)
  xx, yy = np.meshgrid(x, y)
  zz = np.zeros((ysize, xsize))
  # Applies func() to complex plane
  for x_i in range(x_res):
     for y_i in range(y_res):
        z = complex(xx[y_i, x_i], yy[y_i, x_i])
        # Checking if func() takes additional parameters
        if len(args) == 0:
          z_0 = func(z)
        else:
          z_0 = func(z, args)
        # Appending value |z| to array
        zz[y_i, x_i] = abs(z_0)  
   # Returns array of z-map  
   return zz

  
# Creates and returns complex xy plane to manipulate outside module
def createplane(x_res, y_res, domain):
  # Determining size of image
  aspect_ratio = x_res / y_res
  y_range = x_range / aspect_ratio
  # Assigning coordinates to each pixel
  # Note: array indexing goes array[row,col] == array[y,x]
  x = np.linspace(-1 * x_range, x_range, xsize)
  y = np.linspace(-1 * y_range, y_range, ysize)
  xx, yy = np.meshgrid(x, y)
  zz = np.zeros((ysize, xsize))
  return [xx, yy, zz]
