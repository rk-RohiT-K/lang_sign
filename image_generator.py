import os
import cv2
import time 
import uuid

IMAGE_PATH='Dataset'

labels=["Hello","Yes","No","Thanks","IloveYou","Please","What","Name",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
        "Q","R","S","T","U","V","W","X","Y","Z"]

number_of_images=25

for label in labels:
    img_path=os.path.join(IMAGE_PATH,label)
    if os.path.exists(img_path):
        continue
    os.makedirs(img_path)
    cap=cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(3)
    for image_number in range(number_of_images):
        ret, frame=cap.read()
        image_name=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        print(image_name)
        cv2.imwrite(image_name,frame)
        cv2.imshow('frame',frame)
        time.sleep(0.5)

        if cv2.waitKey(1) and 0xFF==ord('q'):
            break
    cap.release()

