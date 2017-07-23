from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
df = pd.read_csv('wine.csv',sep=';')
X = df[list(df.columns)[:-1]]
print X
Y = df['quality']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y)
regressor = LinearRegression()
regressor.fit(X_train,Y_train)
y_predictions = regressor.predict(X_test)
print 'R-squared:', regressor.score(X_test,Y_test)
