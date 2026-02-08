#model_training
import cv2
import os
import numpy as np
faces=[] #image face numerical
labels=[] #label

for folder in os.listdir('dataset'):
    label=int(folder.split('_')[1])

    for img in os.listdir(f'dataset/{folder}'):
        image=cv2.imread(f'dataset/{folder}/{img}',0)
        faces.append(image)
        labels.append(label)
faces =np.array(faces)
labels =np.array(labels)

model =cv2.face.LBPHFaceRecognizer_create()#local binary patent histogram(picture understanding)
model.train(faces,labels)
model.save('face_model.yml')
print('Training Completed')
