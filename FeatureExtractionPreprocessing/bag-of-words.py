#The most common representation of text is the bag-of-words model
#Bag-of-words can be thought of as an extension to one-hot encoding. It creates one feature for each word of interest in the text. 
#A collection of documents is called a corpus.
#The corpus's unique words comprise its vocabulary
#The number of elements that comprise a feature vector is called the vector's dimension. A dictionary maps the vocabulary to indices in the feature vector.
#The meanings of the  rst two documents are more similar to each other than they are to the third document, and their corresponding feature vectors are more similar to each other than they are to the third document's feature vector when using a metric such as Euclidean distance. The Euclidean distance between two vectors is equal to the Euclidean norm, or L2 norm, of the difference between the two vectors



#d= x0 - x1
#the Euclidean norm of a vector is equal to the vector's magnitude, which is given by the following equation:
#x = sqrt(x2+x2+...+x2)


from sklearn.feature_extraction.text import CountVectorizer
corpus = [
     'UNC played Duke in basketball',
     'Duke lost the basketball game',
     'I ate a sandwich'	
]
vectorizer = CountVectorizer()
print vectorizer.fit_transform(corpus).todense()
print vectorizer.vocabulary_
