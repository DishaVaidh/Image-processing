import cv2
vd = cv2.VideoCapture("video.MP4")#object created

#Here infinite loop for multiple images in video
while(True):
    ret,frame = vd.read()# here retension is a boolean flag to check our video source exists or not,frame is a image object(if ret false then frame is none)
    if ret==True:
        frame = cv2.resize(frame,(300,200))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Original video",frame)
        cv2.imshow("Gray scale video",gray)
        close = cv2.waitKey(25)#25 ms standard for video speed
        if close == ord('q'):
            break #in normal close it will conflict because loop is infinite and video is play until it finish
vd.release() #for extra ram not 
cv2.destroyAllWindows()
