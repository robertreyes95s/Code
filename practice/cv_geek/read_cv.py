import cv2 as cv 
import numpy as np

img = cv.imread('pics/city.jpg', 1)
cv.imshow('SF City People', img)
cv.waitKey()

cv.destroyAllWindows()
