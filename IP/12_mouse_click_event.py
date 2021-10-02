import numpy as np
import cv2


"""
# mouse callback function
def draw(event,x,y,flags,param):#here xy represnt the point where our mouse is
    
    if event == cv2.EVENT_LBUTTONDBLCLK:#left button double click
        
        cv2.circle(img,(x,y),100,(125,0,255),5)
        
    if event == cv2.EVENT_RBUTTONDBLCLK:
        
        cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2)
        #rectangle start from x,y point 
cv2.namedWindow(winname = "res")    
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)#black image draw of width and height 512 with 3 channels
cv2.setMouseCallback("res",draw)#here window link with function

while True:
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0xFF == 27:#Here 27 means esc
        break

cv2.destroyAllWindows()"""




#Create a fucntion which help to find cordinate of any pixel and its color



def mouse_event(event, x, y, flg, param):
    print("event==",event)#Event shows if we click or not
    print("x==",x)#Here x shows where our mouse in x direction is
    print("y==",y)
    print("flg==",flg)
    print("param==",param)
    font = cv2.FONT_HERSHEY_PLAIN 
    if event == cv2.EVENT_LBUTTONDOWN:#left button single click
        print(x,', ' ,y)
           
        cord = ". "+str(x) + ', '+ str(y)
        cv2.putText(img, cord, (x, y), font, 1, (155,125 ,100), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b= img[y, x, 0] #for blue channel is 0
        g = img[y, x, 1] #for green channel is 1
        r = img[y, x, 2] #for red channel is 2
        
        color_bgr = ". "+str(b) + ', '+ str(g)+ ', '+ str(r)
        cv2.putText(img, color_bgr, (x, y), font, 1, (152, 255, 130), 2)
        cv2.imshow('image', img)
#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('one.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

