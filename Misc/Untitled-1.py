#import math
#import numpy as np
import matplotlib.pyplot as plt
import integration
import complexplane as z

"""
#integration test
def f(x, parameters):
    b = parameters[0]
    c = parameters[1]
    f = c * (x ** b)
    return f

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
"""
c = complex(-.4, .6)

zmap = complexplane.julia(c, 400, 200, 2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(zmap, cmap = 'winter')
plt.show()
"""
c = z.cgen(8799)
print(c)
zz = z.createplane(700,700)
frac = z.julia(zz, c, True)
plot = z.fracplot(frac, 'afmhot')
#plt.show()