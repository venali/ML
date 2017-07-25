#A long document that contains one occurrence of a word may discuss an entirely different topic than a document that contains many occurrences of the same word.

#create feature vectors that encode the frequencies of words

#Instead of using a binary value for each element in the feature vector, we will now use an integer that represents the number of times that the words appeared in the document

from sklearn.feature_extraction.text import CountVectorizer
corpus = ['The dog ate a sandwich, the wizard transfigured a sandwich, and I ate a sandwich']
vectorizer = CountVectorizer(stop_words = 'english')
print vectorizer.fit_transform(corpus).todense()
print vectorizer.vocabulary_
