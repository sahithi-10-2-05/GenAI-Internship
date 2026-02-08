#face detection
#haarcascade is a xml file. xml file helps to keep the size minimum. haarcascade is a machine learning based object detection by opencv.
#it works by using haar-like features(edges,lines)
#trained with +ve and -ve images
#uses cascade classifier method for rejections. Used by cpu
#minneighbours-confirmation with neighbours based on true or false; minsize-fixed size for traversal


import cv2
face_cascade=cv2.CascadeClassifier(r"C:\Users\srisa\OneDrive\Attachments\Desktop\computer_vision_work\data\haarcascade_frontalface_default.xml")
img=cv2.imread(r"C:\Users\srisa\OneDrive\Attachments\Desktop\computer_vision_work\img\61+bHcQ0waL._AC_UF894,1000_QL80_.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,22,0),2)
cv2.imshow("faces",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
