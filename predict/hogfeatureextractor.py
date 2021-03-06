import cv2
from skimage import color
from skimage.transform import resize
from skimage.feature import hog
from predict.featureextractor import FeatureExtractor
from scipy import misc
from scipy import ndimage

__author__ = 'Gilles'

"""

    This class contains a method to extract a HOG from an image. Which is a set of histograms which are calculated
    on macroblocks of the gradient image.

    Written by Group 16: Tim Deweert, Karsten Goossens & Gilles Vandewiele
    Commissioned by UGent, course Machine Learning

"""


class HogFeatureExtractor(FeatureExtractor):

    def __init__(self, _pixels_per_cell):
        self.pixels_per_cell = _pixels_per_cell

    def extract_feature_vector(self, image):
        """
        Extract a feature vector (using HOG) for image
        :param image: GRAY image
        :return: HOG vector
        """

        img = color.rgb2gray(image)
        return self.extract_hog(img, self.pixels_per_cell)

    def extract_hog(self, image, ppc):
        fd = hog(image, orientations=9, pixels_per_cell=(ppc, ppc), cells_per_block=(2, 2), normalise=True)
        return fd.tolist()