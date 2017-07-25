#High-dimensional feature vectors that have many zero-valued elements are called sparse vectors.
#high-dimensional vectors require more memory than smaller vectors.
#The second problem is known as the curse of dimensionality, or the Hughes effect. As the feature space's dimensionality increases, more training data is required to ensure that there are enough training instances with each combination of the feature's values. If there are insuf cient training instances for a feature, the algorithm may over t noise in the training data and fail to generalize.

from sklearn.feature_extraction.text import CountVectorizer
corpus = [
	'UNC played Duke in basketball',
	'Duke lost the basketball game',
	'I ate a sandwich'
]
vectorizer = CountVectorizer(stop_words='english')
print vectorizer.fit_transform(corpus).todense()
print vectorizer.vocabulary_
