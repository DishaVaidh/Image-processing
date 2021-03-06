#Screen Recorder ---

import pyautogui as p
import cv2 as c
import numpy as np
#Create resolution automatically according to screen size
rs = p.size()
#filename in which we store recording
fn = input("Please Enter any file name and Path")#C:\Users\Admin\Desktop\IP
#Fix the frame rate
fps = 60.0
fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)
#create recording module
c.namedWindow("Live_Recording",c.WINDOW_NORMAL)#1st parammeter is name and second is type of window
#Resize the window
c.resizeWindow("Live_Recording",(600,400))
while True:
    img = p.screenshot() #image
    f = np.array(img) #convert image into array
    f = c.cvtColor(f,c.COLOR_BGR2RGB)#in python color in bgr internally
    output.write(f)
    c.imshow("Live_Recording", f)
    if c.waitKey(1) == ord("q"):
        break
c.destroyAllWindows()
output.release()  


