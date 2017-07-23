#Covariance is a measure of how much two variables change together. If the value of the variables increase together, their covariance is positive. If one variable tends to increase while the other decreases, their covariance is negative. If there is no linear relationship between the two variables, their covariance will be equal to zero; the variables are linearly uncorrelated but not necessarily independent.

xbar = (6+8+10+14+18)/5
ybar = (7+9+13+17.5+18)/5
cov = ((6-xbar)*(7-ybar)+(8-xbar)*(9-ybar)+(10-xbar)*(13-ybar)+(14-xbar)*(17.5-ybar) + (18-xbar)*(18-ybar)) /4
print cov

import numpy as np
print np.cov([6,8,10,14,18],[7,9,13,17.5,18])[0][1]
