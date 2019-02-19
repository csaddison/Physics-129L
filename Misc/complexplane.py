#
# 2/19/19
# ------------------------------------- COMPLEXPLANE.PY -------------------------------------

import math
import numpy as np
import matplotlib.pyplot as plt

# Applies a given function over complex plane and returns z-map
def complexplane(func, x_res, y_res, domain, *args):
  x = np.linspace(-1 * x_range, x_range, xsize)
  y = np.linspace(-1 * y_range, y_range, ysize)
  xx, yy = np.meshgrid(x, y)
  zz = np.zeros((ysize, xsize))
  return xx, yy, zz


def julia(c, x_res, y_res, x_range):
 
  # Determining size of image
  aspect_ratio = x_res / y_res
  y_range = x_range / aspect_ratio 
  
  # Defining the quadratic julia generating function f(z)
  def f(x, y, m):
    z = complex(x, y)
    f = z ** 2 + m
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
            z_n = f(z.real, z.imag, c)
            z = complex(z_n.real, z_n.imag)
            n += 1
        zz[y_i, x_i] = n
        
   # Returns array of z-map  
   return zz
