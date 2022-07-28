import numpy as np 
import cv2

def detect(path):
    facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(path)
    sampleNum = 0

# while video is playing read faces
    while(True):
        ret,frame = cam.read()
         # Resize the Frame to improve speed
        frame = imutils.resize(frame, width=450)
        # converting face into grayScale 
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # detecting gray image using detectscale function
          faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1, # This tells how much the object’s size is reduced in each image.
                    minNeighbors=5, # This parameter tells how many neighbours each rectangle candidate should consider.
                    minSize=(25, 25) # This signifies the minimum possible size of an object to be detected. An object smaller than minSize would be ignored.
                )

        
       # Draw a rectangle around the Faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting Frame
    cv2.imshow('Video', frame)
# waitkey() function of Python OpenCV allows users to display a window for given milliseconds or until any key is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything is done, release the Capture
cam.release()
cv2.destroyAllWindows()
