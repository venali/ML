#Where simple linear regression uses a single explanatory variable with a single coef cient, multiple linear regression uses a coef cient for each of an arbitrary number of explanatory variables

from sklearn.linear_model import LinearRegression
X = [[6,2],[8,1],[10,0],[14,2],[18,0]]
Y = [[7],[9],[13],[17.5],[18]]
model = LinearRegression()
model.fit(X,Y)
X_test = [[8,2],[9,0],[11,2],[16,2],[12,0]]
Y_test = [[11],[8.5],[15],[18],[11]]
predictions = model.predict(X_test)
for i, prediction in enumerate(predictions):
	print 'Predicted: %s,Target: %s' % (prediction,Y_test[i])
print 'R-squared: %.2f' % model.score(X_test, Y_test)
