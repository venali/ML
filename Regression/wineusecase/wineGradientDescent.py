#Gradient descent is only guaranteed to  nd the local minimum
#There are two varieties of gradient descent that are distinguished by the number of training instances that are used to update the model parameters in each training iteration. Batch gradient descent, which is sometimes called only gradient descent, uses all of the training instances to update the model parameters in each iteration. Stochastic Gradient Descent (SGD), in contrast, updates the parameters using only a single training instance in each iteration. 

import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import SGDRegressor
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
data = load_boston()
X_train,X_test,Y_train,Y_test = train_test_split(data.data,data.target)
X_scaler = StandardScaler()
Y_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
Y_train = Y_scaler.fit_transform(Y_train)
X_test = X_scaler.transform(X_test)
Y_test = Y_scaler.transform(Y_test)

regressor = SGDRegressor(loss='squared_loss')
scores = cross_val_score(regressor,X_train,Y_train,cv=5)
print 'Cross validation r-squared scores:' , scores
print 'Average cross validation r-squared score:', np.mean(scores)
regressor.fit_transform(X_train,Y_train)
print 'Test set r-squared score', regressor.score(X_test,Y_test) 
