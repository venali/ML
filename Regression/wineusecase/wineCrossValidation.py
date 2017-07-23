import pandas as pd
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LinearRegression
df = pd.read_csv('wine.csv',sep=';')
X = df[list(df.columns)[:-1]]
Y = df['quality']
regressor = LinearRegression()
scores = cross_val_score(regressor,X,Y,cv=5)
print scores.mean(),scores
