import cv2
img=cv2.imread(r"C:\Users\srisa\OneDrive\Attachments\Desktop\computer_vision_work\img\download1.jpg",-1)
img1=cv2.imread(r"C:\Users\srisa\OneDrive\Attachments\Desktop\computer_vision_work\img\download1.jpg",0)
add_img=img+img1
print(add_img)
cv2.imshow('window_name',add_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
