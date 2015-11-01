import os
import math
import numpy
import skimage
from sklearn.cross_validation import KFold
from inout.fileparser import FileParser
from skimage.io import imread

from predict.benchmark import BenchmarkPredictor
from predict.colorfeatureextractor import ColorFeatureExtractor
from predict.prediction import Prediction

__author__ = 'Group16'

"""
    Main class of our project.
    Written by Group 16: Tim Deweert, Karsten Goossens & Gilles Vandewiele
    Commissioned by UGent, course Machine Learning
"""

"""
=======

>>>>>>> gilles
def get_results(train_images_dir):
        results = []
        for shapesDirectory in os.listdir(train_images_dir):
            os.listdir(os.path.join(train_images_dir, shapesDirectory))
            for signDirectory in os.listdir(os.path.join(train_images_dir, shapesDirectory)):
                results.extend([signDirectory]*len(os.listdir(os.path.join(train_images_dir, shapesDirectory, signDirectory))))
        return results
# Directory of our training data (it's a mess in python...)
train_images_dir = os.path.join(os.path.dirname(__file__), "train")
test_images_dir = os.path.join(os.path.dirname(__file__), "test")
# Get the results of the training data & a list of all images
results = get_results(train_images_dir)
train_images = []
for root, subFolders, files in os.walk(train_images_dir):
    for file in files:
        train_images.append(os.path.join(root, file))
test_images = []
for root, subFolders, files in os.walk(test_images_dir):
    for file in files:
        test_images.append(os.path.join(root, file))
# Decide on indices of training and validation data using k-fold cross validation
k = 2
number_images = len(train_images)
kf = KFold(100, n_folds=k, shuffle=True, random_state=1337)
<<<<<<< HEAD
"""
"""
=======

>>>>>>> gilles
# Benchmark predictor
pred = BenchmarkPredictor()
avg_logloss = 0
for train, validation in kf:
    train_set = [train_images[i] for i in train]
    validation_set = [train_images[i] for i in validation]
    train_set_results = [results[i] for i in train]
    validation_set_results = [results[i] for i in validation]
    prediction_object = Prediction()
    pred.train(train_set, train_set_results)
    for elt in validation_set:
        prediction_object.addPrediction(pred.predict(elt), True)
    # Evaluate and add to logloss
    avg_logloss += prediction_object.evaluate(validation_set_results)
print("Average logloss score of the benchmark predictor using ", k, " folds: ", avg_logloss/k)
<<<<<<< HEAD
"""
"""
=======



>>>>>>> gilles
train_images = train_images[0:100]
results = results[0:100]
# Color predictor
pred = ColorPredictor()
avg_logloss = 0
for train, validation in kf:
    train_set = [train_images[i] for i in train]
    validation_set = [train_images[i] for i in validation]
    train_set_results = [results[i] for i in train]
    validation_set_results = [results[i] for i in validation]
    prediction_object = Prediction()
    pred.train(train_set, train_set_results)
    print(pred.histograms)
    for elt in validation_set:
        prediction_object.addPrediction(pred.predict(elt))
    # Evaluate and add to logloss
    avg_logloss += prediction_object.evaluate(validation_set_results)
print("Average logloss score of the color predictor using ", k, " folds: ", avg_logloss/k)
<<<<<<< HEAD
"""

"""
pred = ColorPredictor()
pred.extract_hue_histogram(os.path.join(os.path.dirname(__file__), "test.png"))
pred.extract_hue_histogram(os.path.join(os.path.dirname(__file__), "00917_11555.png"))
"""


# Run it on the test set and write out the output in the required format
"""
pred = ColorPredictor()
pred.train(train_images, results)
prediction_object = Prediction()
for elt in test_images:
    prediction_object.addPrediction(pred.predict(elt))
FileParser.write_CSV("color_chances.xlsx", prediction_object)
prediction_object.adapt_probabilities()
FileParser.write_CSV("color_nochances.xlsx", prediction_object)
"""
"""
import numpy as np
X = np.array([[-1, -1, 1], [-2, -1, 1], [1, 1, -1], [2, 1, -1]])
y = np.array(["B5", "B5", "A1", "A1"])
from sklearn.svm import SVC
# We use C-SVM with a linear kernel and want to predict probabilities
# max_iter = -1 for no limit on iterations (tol is our stopping criterion)
# Put verbose off for some output and don't use the shrinking heuristic (needs some testing)
# Allocate 1 GB of memory for our kernel
# We are using seed 1337 to always get the same results (can be put on None for testing)
clf = SVC(C=1.0, cache_size=1000, class_weight=None, kernel='linear', max_iter=-1, probability=True,
          random_state=1337, shrinking=False, tol=0.001, verbose=False)
clf.fit(X, y)
print(clf.predict_proba([[-0.8, -1, 1]]))
pred = ColorFeatureExtractor()
pred.extract_hue(os.path.join(os.path.dirname(__file__), "01856_06592.png"))
"""

x = 2250
percent = 0.95
fault = 0.0005
p1 = math.log(max(min(fault, 1-pow(10, -15)), pow(10, -15)))
p2 = math.log(max(min(1-(80*fault), 1-pow(10, -15)), pow(10, -15)))
print(p1)
print(p2)
print(p1*(1-percent) + p2*(percent))
