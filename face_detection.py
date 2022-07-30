# importing required modules
import numpy as np 
import cv2


# detect face from image
def detect_faces(gray_frame):
    global size, haar_cascade # using cascade file

    # Resize to speed up detection (optional, change size above)
    mini_frame = cv2.resize(gray_frame, (int(gray_frame.shape[1] / size), int(gray_frame.shape[0] / size)))

    # Detect faces and loop through each one It lists coordinates (x, y, w,h) of bounding boxes around the detected object.
    faces = haar_cascade.detectMultiScale(mini_frame)
    # draw a rectangle on face
      for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return faces

# detect face from video
def detect(path):
    facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(path)
    sampleNum = 0

# while video is playing read faces
    while(True):
        
#     ret is a boolean variable that returns true if the frame is available.
#     frame is an image array vector captured based on the default frames per second defined explicitly or implicitly

        ret,frame = cam.read()
         # Resize the Frame to improve speed
        frame = imutils.resize(frame, width=450)
        # converting face into grayScale 
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # detecting gray image using detectscale function
          faces = facedetect.detectMultiScale(
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
    if cv2.waitKey(1):
        break
    
# When everything is done, release the Capture
cam.release()
cv2.destroyAllWindows()
