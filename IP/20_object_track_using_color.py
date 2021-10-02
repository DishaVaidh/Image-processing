#HSV -  Hue saturation value
#Hsv is use to separate image information on the basis of color luminous or intensity.
#We use Hsv where we perform operation on the basis of color.
#HSV related to hexaon color model
# H - hue - use to select color from 360 portion 
#saturation is amount of color  which is selected in hue.(color shades)[intensity]
#V  -  value which is brightness of the color.

import cv2
import numpy as np

frame = cv2.imread('one.jpg')#take color balls images for better understanding
while True:
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#convert to hsv image
    
   
    l_v = np.array([110,50,50])#take this color from color picker,this is lower color value
    u_v = np.array([130,235,225])#higher value
    
    #Creating Mask
    mask = cv2.inRange(hsv, l_v, u_v)
    #filter mask with image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
"""

frame = cv2.imread('H:\\Data\\color_balls.jpg')
frame = cv2.resize(frame,(600,400))
#Binding Color Trackbars with image
def nothing(x):
    pass

cv2.namedWindow("Color Adjustments")
cv2.createTrackbar("Lower_H", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_S", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_V", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Upper_H", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_S", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_V", "Color Adjustments", 255, 255, nothing)


while True:
    
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustments")
    l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustments")
    l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustments")

    u_h = cv2.getTrackbarPos("Upper_H", "Color Adjustments")
    u_s = cv2.getTrackbarPos("Upper_S", "Color Adjustments")
    u_v = cv2.getTrackbarPos("Upper_V", "Color Adjustments")
    
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    
    #Creating Mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    #filter mask with image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()"""
