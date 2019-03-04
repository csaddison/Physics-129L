#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 6, Exercise 1

import math
import numpy as np

class LVector:
    
    def __init__(self, coordinates):
        self.x0 = coordinates[0]
        self.x1 = coordinates[1]
        self.x2 = coordinates[2]
        self.x3 = coordinates[3]

    def __getitem__(self, index):
        if index == 0:
            return self.x0
        elif index == 1:
            return self.x1
        elif index == 2:
            return self.x2
        elif index == 3:
            return self.x3        
    
    def __str__(self):
        return 'x0=' + str(self.x0) + ' , x1=' + str(self.x1) + ' , x1=' + str(self.x2) + ' , x3=' + str(self.x3)

    def __add__(self, other):
        a = [self.x0 + other[0], self.x1 + other[1], self.x2 + other[2], self.x3 + other[3]]
        return a

    def __sub__(self, other):
        s = [self.x0 - other[0], self.x1 - other[1], self.x2 - other[2], self.x3 - other[3]]
        return s
    
    def __mul__(self, other):
        if isinstance(other, (int, float)) == True:
            m = [self.x0 * other, self.x1 * other, self.x2 * other, self.x3 * other]
        else:
            m = (self.x0 * other[0]) - (self.x1 * other[1]) - (self.x2 * other[2]) - (self.x3 * other[3])
        return m
    
    def __rmul__(self, other):
        return self.__mul__(other)
        
    def square(self):
        sqr = self.__mul__(self)
        return sqr
    
    def set_x0(self, x0):
        self.x0 = x0
    
    def set_x1(self, x1):
        self.x1 = x1

    def set_x2(self, x2):
        self.x2 = x2

    def set_x3(self, x3):
        self.x3 = x3
    
    def get_rlength(self):
        L3 = math.sqrt((self.x1 ** 2) + (self.x2 ** 2) + (self.x3 ** 2))
        return L3
    
    def get_rtlength(self):
        L2 = math.sqrt((self.x1 ** 2) + (self.x2 ** 2))
        return L2
    
    def get_r(self):
        R3 = np.array((self.x1, self.x2, self.x3))
        return R3
    
    def get_rt(self):
        R2 = np.array((self.x1, self.x2, 0))
        return R2
    
    def phi(self):
        p = math.atan(self.x2 / self.x1)
        return p
    
    def theta(self):
        t = math.atan(self.get_rtlength() / self.x3)
        return t
    
    def eta(self):
        e = -1 * math.log(math.tan(self.theta() / 2))
        return e
    
    def Y(self):
        y = .5 * math.log((self.x0 + self.x3) / (self.x0 - self.x3))
        return y
    
    def boost(self, beta):
        magnitude_beta = math.sqrt((beta[0] ** 2) + (beta[1] ** 2) + (beta[2] ** 2))
        gamma = 1 / math.sqrt(1 - (magnitude_beta ** 2))
        dot_product = (self.x1 * beta[0]) + (self.x2 * beta[1]) + (self.x3 * beta[2])
        r_transform = (-1 * gamma * self.x0) + (((gamma ** 2) / (1 + gamma)) * dot_product)

        x0 = gamma * (self.x0 - dot_product)
        
        self.set_x0(x0)

        x1 = self.x1 + (r_transform * self.x1)
        self.set_x1(x1)

        x2 = self.x2 + (r_transform * self.x2)
        self.set_x2(x2)

        x3 = self.x3 + (r_transform * self.x3)
        self.set_x3(x3)