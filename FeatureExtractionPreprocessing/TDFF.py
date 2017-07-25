# TfdfTransformer smoothes the raw counts and applies L2 normalization. The smoothed, normalized term frequencies are given by the following equation:
#t f (t,d)= f (t,d)+1 /x

# In addition to normalizing raw term counts, we can improve our feature vectors by calculating logarithmically scaled term frequencies, which scale the counts to a more limited range, or augmented term frequencies, which further mitigates the bias for longer documents. Logarithmically scaled term frequencies are given by the following equation:
#t f (t,d)=log(f (t,d)+1)

# The inverse document frequency (IDF) is a measure of how rare or common a word is in a corpus. The inverse document frequency is given by the following equation:
#id f (t,D)=log N 1+ | d E D:t E d |

from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
	'The dog ate a sandwich and I ate a sandwich',
	'The wizard transfigured a sandwich'
]
vectorizer = TfidfVectorizer(stop_words='english')
print vectorizer.fit_transform(corpus).todense()
