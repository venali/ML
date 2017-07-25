#Scale-Invariant Feature Transform (SIFT) is a method for extracting features from an image that is less sensitive to the scale, rotation, and illumination of the image
#Each SIFT feature, or descriptor, is a vector that describes edges and corners in a region of an image.
#Speeded-Up Robust Features (SURF) is another method of extracting interesting points of an image and creating descriptions that are invariant of the image's scale, orientation, and illumination.

import mahotas as mh
from mahotas.features import surf
image = mh.imread('/Users/venali.sonone/Documents/gitworkspace/PythonDir/ML/FeatureExtractionPreprocessing/zipper.jpg', as_grey=True)
print 'The first SURF descriptor:\n', surf.surf(image)[0]
print 'Extracted %s SURF descriptors' % len(surf.surf(image))
