# importing required modules
import numpy as np 
import cv2
import imutils # functions to make basic image processing functions like resizing


# detect face from image
def detect_faces(gray_frame):
    global haar_cascade # using cascade file
    size = 2

    # Resize to speed up detection (optional, change size above)
                                         # width                          # height   
    mini_frame = cv2.resize(gray_frame, (int(gray_frame.shape[1] / size), int(gray_frame.shape[0] / size)))

    # returns a list of face co-ordinates
    faces = haar_cascade.detectMultiScale(mini_frame)
    # draw a rectangle on face co-ordinates
      for (x, y, w, h) in faces:
       # cv2.rectangle(image, start_point, end_point, color, thickness)
        cv2.rectangle(mini_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return faces

# detect face from video
def detect(path):
    facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(path)

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
        
#         detectMultiScale function is used to detect the faces. This function will return a rectangle with coordinates(x,y,w,h) around the detected face.
#     It takes 3 common arguments — the input image, scaleFactor, and minNeighbours. 
          faces = facedetect.detectMultiScale(
                    gray,
                    minNeighbors=5, # This parameter tells how many neighbours each rectangle candidate should consider.
                    minSize=(30, 30) # This signifies the minimum possible size of an object to be detected. An object smaller than minSize would be ignored.
                )
          for(x,y,w,h) in faces:
             cv2.rectangle(faces,(x,y),(x+w,y+h),(0,255,0),2)
             cv2.waitKey(1)
    # Display the image in a window named 'face'
    cv2.imshow('face', faces)
# waitkey() function of Python OpenCV allows users to display a window for given milliseconds or until any key is pressed.
    cv2.waitKey(1)
   
# When everything is done, release the cam and close all the windows
cam.release()
cv2.destroyAllWindows()
