#R-squared measures how well the observed values of the response variables are predicted by the model. More concretely, r-squared is the proportion of the variance in the response variable that is explained by the model. An r-squared score of one indicates that the response variable can be predicted without any error using the model. An r-squared score of one half indicates that half of the variance in the response variable can be predicted using the model. There are several methods to calculate r-squared. In the case of simple linear regression, r-squared is equal to the square of the Pearson product moment correlation coef cient, or Pearson's r.

from sklearn.linear_model import LinearRegression
X=[[6],[8],[10],[14],[18]]
Y=[[7],[9],[13],[17.5],[18]]
X_test = [[8],[9],[11],[16],[12]]
Y_test = [[11],[8.5],[15],[18],[11]]
model = LinearRegression()
model.fit(X,Y)
print 'R-squared: %.4f' % model.score(X_test,Y_test)
