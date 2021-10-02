"Save black and white image in another image"
import cv2
img = cv2.imread("one.jpg",0)#In second argument,1 means original image,0 means gray scale image and -1 means saturated image
print(img)
cv2.imshow("Gray Scale Image",img)


x=cv2.waitKey(0)#It defines how much time in ms the image show and 0 means infinte time
if(x==ord('s')):
    cv2.imwrite("one_grayscale.jpg",img)
elif(x==ord('q')):
    cv2.destroyAllWindows()
