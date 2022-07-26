# import modules
import glob 
# face_recognition library
import face_recognition
# argument parser
import argparse
# pickle to save the encodings
import pickle
# opencv
import cv2
# operating system
import os

imagepaths=[]
# grab the paths to the input images in our dataset, then initialize out data list
for name in glob.glob("dataset/*"):
    imagepaths.append(name)

# vectorizing the features of video frames & serializing it in a enc.picke file (a binary format file)
data=[]
# loop over the image paths
for (i,img) in enumerate(imagepaths):
    print("img {}/{} ".format(i+1,len(imagepaths)))
    # loading image to BGR
    imgg=cv2.imread(img)
#   load the input image and convert it from BGR (OpenCV ordering) to dlib ordering (RGB)
    rgb=cv2.cvtColor(imgg,cv2.COLOR_BGR2RGB)
   # detect the (x, y)-coordinates of the bounding boxes
	# corresponding to each face in the input image
    boxes=face_recognition.face_locations(rgb)
   # compute the facial embedding for the face
    encodings=face_recognition.face_encodings(rgb,boxes)
    # build a dictionary of the image path, bounding box location,
	# and facial encodings for the current image
    d=[{"imgpath":img,"box":box,"encodings":enc} for (box,enc) in zip(boxes,encodings)]
    data.extend(d)

f=open("enc.picke","wb")
# dump() function store the object data to the file. pickle
f.write(pickle.dumps(data))
f.close()
