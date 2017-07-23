import matplotlib.pylab as plt
import pandas as pd
df = pd.read_csv('wine.csv',sep=';')
#print df.describe()
plt.scatter(df['alcohol'],df['quality'])
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.title('Alcohol Against Quality')
plt.show()
print df.corr()
