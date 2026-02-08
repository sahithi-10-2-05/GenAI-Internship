import cv2
img=cv2.imread(r"C:\Users\srisa\OneDrive\Attachments\Desktop\computer_vision_work\img\download.jpg",0)
cv2.circle(img, (400, 300), 100, (255,0,0), -1)
cv2.putText(img, 'Hello World!', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)#image, text, coordinates,font style, thickness,bgr code,thickness,line style
cv2.imshow('window_name',img)
cv2.imwrite('img/new_abc.jpg',img)#imwrite to save the image
cv2.waitKey(0)
cv2.destroyAllWindows()
