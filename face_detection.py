import numpy as np 
import cv2

def detect(path):
    facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(path)
    sampleNum = 0

# while video is playing read faces
    while(True):
        ret,img = cam.read()
        # converting face into grayScale 
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # detecting gray image using detectscale function
        faces = facedetect.detectMultiScale(gray,1.3,5)
       # for crooping face we need to draw a rectangle using these coordinates
        for(x,y,w,h) in faces:
            sampleNum+=1# increasing samplenum
            cv2.imwrite('dataset/'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w]) # storing file in dataset folder
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(1)
            # show rectangle on face
        cv2.imshow('face',img)
        cv2.waitKey(1)
        # we are storing only 100 images
        if(sampleNum>100):
            break

    cam.release()
    cv2.destroyAllWindows()
