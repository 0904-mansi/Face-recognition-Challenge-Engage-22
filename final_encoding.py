
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

clt = DBSCAN(metric="euclidean", n_jobs=-1)
clt.fit(encodings)

clt.labels_

labelIDs = np.unique(clt.labels_)
labelIDs

numUniqueFaces=len(np.where(labelIDs>-1)[0])

print("unique faces: {}".format(numUniqueFaces))


for labelID in tqdm(labelIDs):
    idxs = np.where(clt.labels_ == labelID)[0]
    idxs = np.random.choice(idxs, size=min(25, len(idxs)),replace=False)
    faces = []
    path=r'face_samples/id'+str(labelID)
    if not os.path.exists(path):
        os.makedirs(path)
    for i in idxs:
        img=cv2.imread(data[i]["imgpath"])
        cv2.imwrite(path+"/"+str(i)+".jpeg",img)
    
