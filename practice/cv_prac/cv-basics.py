import cv2 
import numpy 

#Create a windows freedom of dimension
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

# Reads disered image 
img = cv2.imread('pics/sf_people.jpg', 1)

#Resize image to desired dimensions 
imgS = cv2.resize(img, (1600, 940))

# This is to display the image
cv2.imshow('image', imgS)

# Save image to directed path and as sf_peopleS.jpg
##status = cv2.imwrite(r'pics/sf_peopleS.jpg', imgS)
# Relay status of save, will print 'True' if successull 
##print("Image written success? : ", status)

cv2.waitKey() # This is necessary to be required

################### Access Pixel Value and Modyfing them #####################################

# Select a certian pixel in image
px = imgS[100, 100]  # Gives a list of cointing lsit value fro RGB Ex. [23, 12, 23]

#access blue channel 
blue = img[100, 100, 0]

#  to modify we need to acess and overwrite
img[100, 100] = [255, 255, 255] 
##print(img[100,100]) 
#output: [255, 255, 255]

# Accessing red value
img.item(10,10,2)
# >> 59

#$mod red value 
img.itemset((10,10,2),100)
img.item(10,10,2)
# >> 100

####################### Access Image Properties ##################################

# Gives you dimensions of pictures/item
img.shape
# >> (2399, 3600, 3) # rows, columns, channels

img.size
# >> 25909200

#Gives image type
img.dtype
# >> uint8

##################### Splitting and Mergin Image Channels  ############################

# This is how to split image channels  
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2] 

# Set all calues in red channel to zero 
img [:,:,2] = 0

# It will run continuosliy until the key press 
cv2.destroyAllWindows()

