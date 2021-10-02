#Start with Basic operations on Image
import cv2
import numpy as np

#Read an Image---
img = cv2.imread("one.jpg")
img = cv2.resize(img,(600,400))
cv2.imshow("res",img)
print("shape==",img.shape) #returns a tuple of number of rows, columns, and channels
print("no.of pixels==",img.size) #returns Total number of pixels is accessed
print("datatype==",img.dtype) #returns Image datatype is obtained like unsigned int
print("Imagetype==",type(img))#returns tyoe like array
#Now try to split an image
#split  -  return 3 channel of ur image which is blue,green,red
#print(cv2.split(img))
b,g,r = cv2.split(img)

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
"""
#Now if we want to mix the the channels then use merge
"""
mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)
mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr",mr2)
cv2.waitKey()
#Here bgr combination is the original image
cv2.destroyAllWindows()

#Working on pixel color values------
"""
img = cv2.imread("two.png")
img = cv2.resize(img,(1024,700))
cv2.imshow("Image==",img)

#access a pixel value by its row and column coordinates.
px = img[220,280] #store cordinate in variable
print("the pixel of that co-ordinates==",px) #we get the pixel value

#Now try to find selected channel value from cordinate
#We know we have three channel -   0,1,2
# accessing only blue pixel
blue = img[220,280,0]
print("the pixel having blue color==",blue)

grn = img[220,280,1] #for green pass 1
print("the pixel having grn color==",grn)
red = img[220,280,2] #for red pass 2
print("the pixel having red color==",red)

cv2.waitKey(0)
cv2.destroyAllWindows()"""
