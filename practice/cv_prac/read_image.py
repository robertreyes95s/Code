import cv2 

image = cv2.imread('pics/city.jpg')

h, w = image.shape[:2]

print("Height = {}, width = {}".format(h, w))
