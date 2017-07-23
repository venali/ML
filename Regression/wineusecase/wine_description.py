import pandas as pd
df = pd.read_csv('wine.csv',sep=';')
print df.describe()

