#Many machine learning problems have categorical, or nominal, rather than continuous features. Categorical variables are commonly encoded using one-of-K or one-hot encoding, in which the explanatory variable is encoded using one binary feature for each of the variable's possible values.

from sklearn.feature_extraction import DictVectorizer
onehot_encoder = DictVectorizer()
instances = [
     {'city': 'New York'},
     {'city': 'San Francisco'},
     {'city': 'Chapel Hill'}
 ]
print onehot_encoder.fit_transform(instances).toarray()
