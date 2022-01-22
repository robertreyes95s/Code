########################## OpenCV Blob Detection #############################
# Blob = Binary large Object -  a group of connected pixels which we 
# can find in an image and all of these pixels have some common property
# use SimpleBlobDetector() to detect blobs
import sys
sys.settrace

import cv2 
import numpy as np 

img = cv2.imread(r'pics/walk_the_walk.jpg', cv2.IMREAD_GRAYSCALE) # _GRAYSCALE loads imafe in gray scale modd
# Set up the detector with default parameters
detector = cv2.SimpleBlobDetector()

# Detecing blobs
keypoints = detector.detect(img)

# Draw detected blobs as red circles
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob 
im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Keypoints', im_with_keypoints)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""Go to basics-five for blob location syntax/examples"""