#How to use android device camera as webcam in OPencv.

#Download Ip webcam in mobile->start server->and then that ip address given in mobile is provided here
import cv2
camera = "http://100.68.9.166:8080/video"
#connect your laptop and android device with same network either wifi or hotspot
cap = cv2.VideoCapture(0)   #Here parameter 0 is a path of any video use for webcam
cap.open(camera)
print("check===",cap.isOpened())
#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    if ret == True:
    
        frame = cv2.resize(frame,(700,700))
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    
 
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()
