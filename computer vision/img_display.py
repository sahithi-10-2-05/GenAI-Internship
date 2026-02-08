import cv2
img=cv2.imread(r"C:\Users\srisa\OneDrive\Attachments\Desktop\computer_vision_work\img\download.jpg",-1)
#imread will take 2 parameters: image path and flag.
#flag has 0,1,-1
print(img)
cv2.imshow('window_name',img)
#imshow will display an image or video . it takes 2 parameters as input- window name and variable of image
cv2.waitKey(0)
#-215 assertion error in image means image is not read properly
#if there is unicode error place'r' before file path
cv2.destroyAllWindows()#used to closes the window properly it takes the window name as parameter
