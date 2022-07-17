# importing required module
import numpy as np 
import cv2

def detect(path):
#  using haarcascade_frontalface_default.xml file for face-detection
    facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(path)
    sampleNum = 0


    while(True):
        ret,img = cam.read()
        # convert from RGB to grayscale
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#        The detectMultiScale method is the one that will perform the detection for us. It takes the following parameters: scaleFactor & minNeighbors
#        The detectMultiScale method returns a numpy array with dimensions and positions of the rectangles containing the faces.

        faces = facedetect.detectMultiScale(gray,1.3,5)
#       x,y — position of the top left corner of the rectangle and w, h — width and height of the rectangle
        for(x,y,w,h) in faces:
            sampleNum+=1
            # storing image into dataset folder
            cv2.imwrite('dataset/'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])
             # draw a rectangle with these dimensions in green color (0, 255, 0) (BGR color code) with the border thickness = 2
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(1)
        cv2.imshow('face',img)
        cv2.waitKey(1)
        if(sampleNum>100):
            break

    # closing window automatically
    cv2.destroyAllWindows()
