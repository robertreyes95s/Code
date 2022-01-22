########################## Resizing Image ##############################
"""
Syntax: cv2.resize(s, size,fx,fy,interpolation)  
Parameters:
s - input image (required).
size - desired size for the output image after resizing (required)
fx - Scale factor along the horizontal axis.(optional)
fy - Scale factor along the vertical axis.
Interpolation(optional) - This flag uses following methods:
 INTER_NEAREST – a nearest-neighbor interpolation
 INTER_LINEAR – a bilinear interpolation (used by default) 
 INTER_AREA – resampling using pixel area relation. It may be a preferred method for    image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
 INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood 
 INTER_LANCZOS4 – a Lanczos interpolation over 8×8 pixel neighborhood
"""
import cv2 
import numpy as np 

img = cv2.imread('pics/sf_people.jpg', 1)
#print(img.shape)

img_resize=cv2.resize(img, (780, 540), interpolation = cv2.INTER_NEAREST)

cv2.imshow('Resized', img_resize)

########################### Image Rotation #################################
"""
 Syntax: cv2.rotate( src, rotateCode[, dst] )
Parameters:
src: It is the image to be rotated.
rotateCode: It is an enum to specify how to rotate the array.Here are some of the possible values :
cv2.cv2.ROTATE_90_CLOCKWISE
cv2.ROTATE_180
cv2.ROTATE_90_COUNTERCLOCKWISE
"""

image = cv2.rotate(img_resize, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Rotated', image)

#################### RotationMatrix2d  ##################
"""
syntax:cv2.getRotationMatrix2D(center, angle, scale)
cv2.warpAffine(Img, M, (W, H))
center: center of the image (the point about which rotation has to happen)
angle: angle by which image has to be rotated in the anti-clockwise direction.
scale: scales the image by the value provided,1.0 means the shape is preserved.
H:height of image
W: width of the image.
M: affine matrix returned by cv2.getRotationMatrix2D
Img:image to be rotated.
"""
emg = cv2.imread('pics/people_walk.jpg', 1)

(h, w) = emg.shape[:2] # Get image height, width
center = (w / 2, h / 2) # Calculate the center of the image
# >> (600, 400)

scale = 1.0

# Perform the counter clockwwise roration holding at the center 
# 45 degress
M = cv2.getRotationMatrix2D(center, 45, scale)
print(M)
rotated45 = cv2.warpAffine(emg, M, (h, w))

# 110 Degree Rotation 
M = cv2.getRotationMatrix2D(center, 110, scale)
print(M)
rotated110 = cv2.warpAffine(emg, M, (h, w))

# 150 degree rotation
M = cv2.getRotationMatrix2D(center, 150, scale)
print(M)
rotated150 = cv2.warpAffine(emg, M, (h, w))


cv2.imshow('45 Degree Rotation', rotated45)
cv2.imshow('110 Degree Rotation', rotated110)
cv2.imshow('150 Degree Rotation', rotated150)


cv2.waitKey(0)
cv2.destroyAllWindows()


