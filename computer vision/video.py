import cv2
cam=cv2.VideoCapture(0)#camera device mean i.e. no.of camera
while True:
   ret,frame=cam.read()#ret is used to return frame to camera
   cv2.circle(frame, (100, 100), 50, (0, 0, 255), -1)
   cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 3)
   cv2.rectangle(frame, (50, 50), (150, 150), (0, 255, 0), 3)#square
   cv2.putText(frame, 'Hello World!', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
   cv2.imshow('camera',frame)
   if cv2.waitKey(1) & 0xFF==ord('q'):
       break
cam.release()
cv2.destroyAllWindows()
