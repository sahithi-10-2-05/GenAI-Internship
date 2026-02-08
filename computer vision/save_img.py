import cv2
img=cv2.imread(r"C:\Users\srisa\OneDrive\Attachments\Desktop\computer_vision_work\img\download.jpg",0)
cv2.imshow('window_name',img)
cv2.imwrite('img/new_abc.jpg',img)#imwrite to save the image
cv2.waitKey(0)
cv2.destroyAllWindows()
