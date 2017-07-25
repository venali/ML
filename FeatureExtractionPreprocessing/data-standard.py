#Standardized data has zero mean and unit variance. An explanatory variable with zero mean is centered about the origin; its average value is zero. A feature vector has unit variance when the variances of its features are all of the same order of magnitude. For example, assume that a feature vector encodes two explanatory variables. The  rst values of the  rst variable range from zero to one. The values of the second explanatory variable range from zero to 100,000. The second feature must be scaled to a range closer to {0,1} for the data to have unit variance. If a feature's variance is orders of magnitude greater than the variances of the other features, that feature may dominate the learning algorithm and prevent it from learning from the other variables.
from sklearn import preprocessing
import numpy as np
X = np.array([
        [0., 0., 5., 13., 9., 1.],
        [0., 0., 13., 15., 10., 15.],
        [0., 3., 15., 2., 0., 11.]
    ])
print preprocessing.scale(X) 
