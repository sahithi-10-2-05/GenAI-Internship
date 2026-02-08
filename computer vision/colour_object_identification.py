#YOLO is famous in object identifiction.Training is done using LBPH algorithm.
#h=0-255-colour,s=0-255-shade,value=0-255,v-brightness
import cv2
import numpy as np
cam=cv2.VideoCapture(0)
while True:
    ret, frame=cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([20, 100, 100])#yellow
    upper_blue=np.array([40, 255, 255])#yellow
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('window',result)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
cam.release()
cv2.destroyAllWindows
    
