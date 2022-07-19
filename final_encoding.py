
# DBSCAN - Density-Based Spatial Clustering of Applications with Noise. Finds core samples of high density and expands clusters from them.
import pickle
import cv2
import numpy as np
from sklearn.cluster import DBSCAN
from imutils import build_montages
import os
from tqdm import tqdm

#read data from enc.picke file
data = pickle.loads(open("enc.picke", "rb").read())
#creating array from that data
data=np.array(data)

encodings=[d['encodings'] for d in data]
#Perform DBSCAN clustering from vector array or distance matrix.
# metric to calculating distance between instances in a feature array.
clt = DBSCAN(metric="euclidean", n_jobs=-1) # Euclidean Distance represents the shortest distance between two points  
# use this distance metric to measure the similarity between observations or points
clt.fit(encodings)

clt.labels_

labelIDs = np.unique(clt.labels_)
labelIDs

numUniqueFaces=len(np.where(labelIDs>-1)[0])

print("unique faces: {}".format(numUniqueFaces))


for labelID in tqdm(labelIDs):
    idxs = np.where(clt.labels_ == labelID)[0]
#     Generates a random sample from 1-D array
    idxs = np.random.choice(idxs, size=min(25, len(idxs)),replace=False)
# storing faces to face_samples/unique_name dir by indexing 
    faces = []
    path=r'face_samples/id'+str(labelID)
    if not os.path.exists(path):
        os.makedirs(path)
    for i in idxs:
        img=cv2.imread(data[i]["imgpath"])
        cv2.imwrite(path+"/"+str(i)+".jpeg",img)
    
