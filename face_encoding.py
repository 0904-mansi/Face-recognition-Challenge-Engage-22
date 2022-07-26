
# DBSCAN - Density-Based Spatial Clustering of Applications with Noise. Finds core samples of high density and expands clusters from them. 
# DBSCAN model for clustering similar encodings
import pickle
import cv2
import numpy as np
from sklearn.cluster import DBSCAN
from imutils import build_montages
import os
from tqdm import tqdm

#read data from enc.picke file 
# load the serialized face encodings + bounding box locations from
# disk/encodings pickle file, then extract the set of encodings to so we can cluster on them
data = pickle.loads(open("enc.picke", "rb").read())
#creating array from that data
data=np.array(data)

encodings=[d['encodings'] for d in data]
# creating DBSCAN object for clustering the encodings with the metric "euclidean"
# Perform DBSCAN clustering from vector array or distance matrix.
# metric to calculating distance between instances in a feature array.
clt = DBSCAN(metric="euclidean", n_jobs=-1) # Euclidean Distance represents the shortest distance between two points  
# use this distance metric to measure the similarity between observations or points

clt.fit(encodings)

clt.labels_

# determine the total number of unique faces found in the dataset
# clt.labels_ contains the label ID for all faces in our dataset (i.e., which cluster each face belongs to).
# To find the unique faces/unique label IDs, used NumPy’s unique function.
# The result is a list of unique labelIDs
labelIDs = np.unique(clt.labels_)
labelIDs

# we count the numUniqueFaces . There could potentially be a value of -1 in labelIDs — this value corresponds
# to the “outlier” class where a 128-d embedding was too far away from any other clusters to be added to it.
# “outliers” could either be worth examining or simply discarding based on the application of face clustering.
numUniqueFaces=len(np.where(labelIDs>-1)[0])

print("unique faces: {}".format(numUniqueFaces))

# loop over the unique face integers
for labelID in tqdm(labelIDs):
    idxs = np.where(clt.labels_ == labelID)[0]
    # find all indexes into the `data` array that belong to the
	# current label ID, then randomly sample a maximum of 25 indexes
	# from the set    idxs = np.random.choice(idxs, size=min(25, len(idxs)),replace=False)
    # storing faces to face_samples/unique_name dir by indexing 
    
    # initialize the list of faces to include in the montage
	faces = []


    path=r'face_samples/id'+str(labelID)
    # os.path.exists() method in Python is used to check whether the specified path exists or not.
	# os.mkdir() method in Python is used to create a directory named path with the specified numeric mode.
    if not os.path.exists(path):
        os.makedirs(path)
    for i in idxs:
        img=cv2.imread(data[i]["imgpath"])
        # Using cv2.imwrite() method 
    	# Saving the image 
        cv2.imwrite(path+"/"+str(i)+".jpeg",img)
    
