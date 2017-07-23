#Simple linear regression assumes that a linear relationship exists between the response variable and explanatory variable; it models this relationship with a linear surface called a hyperplane. A hyperplane is a subspace that has one dimension less than the ambient space that contains it. In simple linear regression, there is one dimension for the response variable and another dimension for the explanatory variable, making a total of two dimensions. The regression hyperplane therefore, has one dimension; a hyperplane with one dimension is a line.

#The sklearn.linear_model.LinearRegression class is an estimator. Estimators predict a value based on the observed data. In scikit-learn, all estimators implement the fit() and predict() methods.

#The fit method of LinearRegression learns the parameters of the following model for simple linear regression:

#y=a+bx

#Using training data to learn the values of the parameters for simple linear regression that produce the best  tting model is called ordinary least squares or linear least squares.

#Using training data to learn the values of the parameters for simple linear regression that produce the best  tting model is called ordinary least squares or linear least squares.

#A cost function, also called a loss function, is used to de ne and measure the error of a model. The differences between the prices predicted by the model and the observed prices of the pizzas in the training set are called residuals or training errors

#model  ts if the values it predicts for the response variable are close to the observed values for all of the training examples. This measure of the model's  tness is called the residual sum of squares cost function.
from sklearn.linear_model import LinearRegression
import numpy as np
X = [[6],[8],[10],[14],[18]]
Y = [[7],[9],[13],[17.5],[18]]
model = LinearRegression()
model.fit(X,Y)
print 'A 12" pizza should cose: $%.2f' % model.predict([12])[0]
print 'Residual sum of squares: %.2f' % np.mean((model.predict(X)-Y)**2)
