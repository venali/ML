#Stemming and lemmatization are two strategies to condense in ected and derived forms of a word into a single feature.
#Lemmatization is the process of determining the lemma, or the morphological root, of an in ected word based on its context. Lemmas are the base forms of words that are used to key the word in a dictionary. Stemming has a similar goal to lemmatization, but it does not attempt to produce the morphological roots of words. Instead, stemmin removes all patterns of characters that appear to be af xes, resulting in a token that is not necessarily a valid word.

import nltk
from sklearn.feature_extraction.text import CountVectorizer
corpus = [
	'He ate the sandwiches',
	'Every sandwich was eaten by him'
]
vectorizer = CountVectorizer(binary=True, stop_words='english')
print vectorizer.fit_transform(corpus).todense()
print vectorizer.vocabulary_



print 'lemmetization'
corpus = [
	'I am gathering ingredients for the sandwich.',
	'There were many wizards at the gathering.'
]

from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print 'gathering:'
print lemmatizer.lemmatize('gathering','v')
print lemmatizer.lemmatize('gathering','n')

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print stemmer.stem('gathering')




from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
wordnet_tags = ['n','v']
corpus = [
	'He ate the sandwiches',
	'Every sandwich was eaten by him'
]
stemmer = PorterStemmer()
print 'Stemmed:', [[stemmer.stem(token) for token in word_tokenize(document)] for document in corpus]
def lemmatize(token,tag):
	if tag[0].lower() in ['n','v']:
		return lemmatizer.lemmatize(token,tag[0].lower())
	return token
lemmatizer = WordNetLemmatizer()
tagged_corpus = [pos_tag(word_tokenize(document)) for document in corpus]
print 'Lemmatized:' , [[lemmatize(token,tag) for token, tag in document] for document in tagged_corpus]

