#The Euclidean distance between two vectors is equal to the Euclidean norm, or L2 norm, of the difference between the two vectors

#d= x0 - x1
#the Euclidean norm of a vector is equal to the vector's magnitude, which is given by the following equation:
#x = sqrt(x2+x2+...+x2)

from sklearn.metrics.pairwise import euclidean_distances
counts = [
    [0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
]
print 'Distance between 1st and 2nd documents:',euclidean_distances(counts[0],counts[1])
print 'Distance between 1st and 3nd documents:',euclidean_distances(counts[0],counts[2])
print 'Distance between 2st and 3nd documents:',euclidean_distances(counts[1],counts[2])

