# import modules
import glob 
import face_recognition
import argparse
import pickle
import cv2
import os

imagepaths=[]

for name in glob.glob("dataset/*"):
    imagepaths.append(name)

# vectorizing the features of video frames & serializing it in a enc.picke file (a binary format file)
data=[]
for (i,img) in enumerate(imagepaths):
    print("img {}/{} ".format(i+1,len(imagepaths)))
    imgg=cv2.imread(img)
    rgb=cv2.cvtColor(imgg,cv2.COLOR_BGR2RGB)
    boxes=face_recognition.face_locations(rgb)
    encodings=face_recognition.face_encodings(rgb,boxes)
    d=[{"imgpath":img,"box":box,"encodings":enc} for (box,enc) in zip(boxes,encodings)]
    data.extend(d)

f=open("enc.picke","wb")
# dump() function store the object data to the file. pickle
f.write(pickle.dumps(data))
f.close()
