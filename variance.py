#Variance is a measure of how far a set of values is spread out. If all of the numbers in the set are equal, the variance of the set is zero. A small variance indicates that the numbers are near the mean of the set, while a set containing numbers that are far from the mean and each other will have a large variance.


from __future__ import division
import numpy as np
xbar = (6+8+10+14+18)/5
varience = ((6 - xbar)**2 + (8 - xbar)**2 + (10 - xbar)**2 + (14 - xbar)**2 + (18 - xbar)**2 ) / 4
print varience
print np.var([6,8,10,14,18],ddof=1)


