#In this program, we talk about ROI(Region of Interest)
#this concept is use to find target portion from image like eyes on face.
import cv2
import numpy as np

#read image
img = cv2.imread("thor.jpg")
img = cv2.resize(img,(800,700))
#cv2.imshow("Original image==",img)
#Now extract  area of interest from an image
"""Now to know the pixels of image where we wanna cut the image either use mouseCallingFunction or open paint,resize image as here(800,700)
and select that part in rectangle and see those pixels value below there
"""
#now pass like [y1:y2,x1:x2]
roi = img[20:210,340:450]
#cv2.imshow("roi image==",roi)

#putting roi into any pixel values
#Here took these difference same in slicing,otherwise error and we want y to be same here
img[20:210,451:561] = roi   
img[20:210,562:672] = roi 
img[20:210,230:340] = roi
img[20:210,120:230] = roi

#changing y===
img[400:590,60:170] = roi
cv2.imshow("original image==",img)

#Now try to use one image data into another image

img1 = cv2.imread("one.jpg")
img1 = cv2.resize(img1,(900,600))
img1[1:191,560:670] = roi

cv2.imshow("ironman",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
