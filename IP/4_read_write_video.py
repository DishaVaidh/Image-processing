#How to read Video from any folder using opencv

import cv2

#Here with the help of videoCapture fucntion we easily ready any video.

cap = cv2.VideoCapture("video.mp4")   #Here parameter is a path of any video
while True:
    ret, frame = cap.read()   #here read the frame
    #get height and width of frame
    print("Width ==>",cv2.CAP_PROP_FRAME_WIDTH)
    print("Height==>",cv2.CAP_PROP_FRAME_HEIGHT)
    
    frame = cv2.resize(frame,(300,250))
    gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,-1) 
    cv2.imshow('Colorframe',frame)
    cv2.imshow("Gray Frame",gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):   #press to exit
        break
   
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()





