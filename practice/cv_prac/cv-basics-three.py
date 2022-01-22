########################### Drawing Functions ############################

########### Drawing Circles ##################
"""
-Syntax: cv2.circle(image, center_coordinates, radius, color, thickness)-
Parameters: 
image: It is the input image on which a circle is to be drawn. 
center_coordinates: It is the center coordinates of the circle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value). 
radius: It is the radius of the circle. 
color: It is the color of the border line of the circle to be drawn. We can pass a tuple For in BGR,  eg: (255, 0, 0) for blue color. 
thickness: It is the thickness of the circle border line in px. Thickness of -1 px will fill the circle shape by the specified color.
Return Value: It returns an image
"""

import numpy as np 
import cv2

img = cv2.imread('pics/people_walk.jpg', 1)
cv2.circle(img, (80, 80), 55, (255, 0, 0), -1)
#cv2.imshow('image' img) # Just circle

########### Drawing Rectangle ##################
""" 
Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)

Parameters:
image: It is the input image on which rectangle is to be drawn.
start_point: It is the starting coordinates(top left vertex) of the rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
end_point: It is the ending coordinates(bottom right) of the rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
color: It is the color of the border line of the rectangle to be drawn. We can pass a tuple For in BGR,  eg: (255, 0, 0) for blue color. 
thickness: It is the thickness of the rectangle border line in px. Thickness of -1 px will fill the rectangle shape by the specified color.

Return Value: It returns an image.
"""

cv2.rectangle(img, (12, 12), (250, 150), (23, 100, 244), 15)
#cv2.imshow('image', img) # Circle and Rectangle

########### Drawing Playlines ##################
"""
syntax: cv2.polyLine(image, arr, is_closed, color, thickness)  
Parameters:
img - It represents an image.
arr -represents the coordinates of vertices into an array of shape nx1x2 where n is number of vertices and it should be of type int32.
is_Closed - It is a flag that indicates whether the drawn polylines are closed or not.
color - Color of polylines. We can pass a tuple For in BGR,  eg: (255, 0, 0) for blue color. 
thickness - It represents the Thickness of the polyline's edges.
"""

# defining points for polyines
pts = np.array([[100, 50],[200, 300],[700, 200],[500, 100]], np.int32)
#pts = pts.reshapre((-1, 1, 2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
#cv2.imshow('image',img)


########## Write text on an image ####################
"""
Syntax: cv2.putText(img, text, org, font,fontScale, color)  
Parameters:
img: It represents the input image on which we have to write text
text: The text which we want to write on the image.
org: It denotes the Bottom-left corner of the text string on the image.So it is used to set the location of text on the image
font: the font of text.Here is the list of supported fonts.
fontScale: The scale of the font by which you can increase or decrease size
color: Represents the color. We can pass a tuple For in BGR,  eg: (255, 0, 0) for blue color. 
"""
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'People', (10,500), font, 1,(100, 200, 15), 2)
#Display the image
cv2.imshow("image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()