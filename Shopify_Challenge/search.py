from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2
import numpy
from sklearn import datasets, svm, metrics
import tensorflow==2.0


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
# initialize
cd = ColorDescriptor((8, 12, 3))

query = cv2.imread(args["query"]) # load query image and describe it
features = cd.describe(query)

searcher = Searcher(args["index"]) # perform the search process
results = searcher.search(features)
cv2.imshow("Query", query) # display query

for (score, resultID) in results:
	result = cv2.imread(args["result_path"] + "/" + resultID) 	# load the result 
	cv2.imshow("Result", result) # display it
	cv2.waitKey(0)
