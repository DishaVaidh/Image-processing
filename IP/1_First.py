import cv2
img = cv2.imread("one.jpg")#In second argument,1 means original image,0 means gray scale image and -1 means saturated image
print(img)
cv2.imshow("Original Image",img)

img1 = cv2.imread("one.jpg",0)#In second argument,1 means original image,0 means gray scale image and -1 means saturated image
print(img1)
cv2.imshow("Black and white Image",img1)

img2 = cv2.imread("one.jpg",-1)#In second argument,1 means original image,0 means gray scale image and -1 means saturated image
print(img2)
cv2.imshow("Saturated Image",img2)

"Resize the image"
img3 = cv2.imread("one.jpg")#In second argument,1 means original image,0 means gray scale image and -1 means saturated image
print(img3)
img3 = cv2.resize(img3,(1000,200))
cv2.imshow("Resize Image",img3)

"Rotate the image"
img4 = cv2.imread("one.jpg")#In second argument,1 means original image,0 means gray scale image and -1 means saturated image
print(img4)
img4 = cv2.flip(img4,1)#Second arg can be 0,1,-1
cv2.imshow("Rotate Image",img4)

cv2.waitKey(0)#It defines how much time in ms the image show and 0 means infinte time and it also takes input
cv2.destroyAllWindows()
