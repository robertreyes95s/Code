import numpy as np 
import cv2 as cv

img = cv.imread('pics/walk_the_walk.jpg')

# setup SimpleBlobDetector parameters.
params = cv.SimpleBlobDetector_Params()

# Change threshold
params.minThreshold = 10
params.maxThreshold = 200

# Filter by area
params.filterByArea = True
params.minArea =  1200

params.filterByCircularity = True
params.minCircularity = 0.1

# Create detector with ther parameters
detector = cv.SimpleBlobDetector(params)

#Detect blob
keypoints = detector.detect(img)

img_keypoints = cv.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255))

cv.imshow("Keypoints", img_keypoints)
cv.waitKey(0)