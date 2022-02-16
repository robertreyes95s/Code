# Loading an image using OpenCV
import cv2

# colored image 
Img = cv2.imread("pics/city.jpg")

# Black and White (grey scale)
img_one = cv2.imread("pics/city.jpg")

# Image Shape/Resolution
print(Img.shape)

cv2.imshow("City", Img)
# Displaying the image;
cv2.waitKey(0)