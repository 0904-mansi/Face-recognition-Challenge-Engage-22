# import required modules
# The OS module in Python provides functions for interacting with the operating system. 
import cv2, numpy, os

#using face_cascade.xml file for recognition
haar_cascade = cv2.CascadeClassifier('face_cascade.xml')

def train_model():
#     Pre-built face recognition models
#     OpenCV supports local binary patterns histograms (or shortly LBPH), eigenface and fisherface methods. We can run them all within opencv.
    model = cv2.face.LBPHFaceRecognizer_create()
    #model = cv2.face.EigenFaceRecognizer_create()
    #model = cv2.face.FisherFaceRecognizer_create()
    fn_dir = 'face_samples'

    (images, lables, names, id) = ([], [], {}, 0)
    #  it yields a 3-tuple (dirpath, dirnames, filenames).
    for (subdirs, dirs, files) in os.walk(fn_dir):
        # Loop through each folder named 
        for subdir in dirs:
            names[id] = subdir
            #names[0] = first name will be 1st subdir
            subjectpath = os.path.join(fn_dir, subdir) # face-sample/1st name
            # Loop through each photo in the folder
            # os. listdir() method in python is used to get the list of all files and directories in the specified directory.
            for filename in os.listdir(subjectpath):
                
                f_name, f_extension = os.path.splitext(filename)
                # Skip non-image formates
                if(f_extension.lower() not in ['.png','.jpg','.jpeg','.pgm']):
                    print("Skipping "+filename+", wrong file type")
                    continue
                path = subjectpath + '/' + filename # face-sample/1st name/1.png
                lable = id # 0 1 2 3  
                # Add to training data
                images.append(cv2.imread(path))# will returnn matrix of pixels
                lables.append(int(lable))
            id += 1

    # Convert a list of images and labels to np array to train model
    (images, lables) = [numpy.array(lis) for lis in [images, lables]]
    # OpenCV trains a model from the images
    model.train(images, lables)

    return (model, names)

# function for recognition 
def recognize_face(model, frame, gray_frame, face_coords, names): 
    (img_width, img_height) = (112, 92)
    size = 2
    #defining two list (using list because list is mutable in python also direct access is possible)
    recognized = []
    recog_names = []

     for i in range(len(face_coords)):
        face_i = face_coords[i]

        # Coordinates of face after scaling back by `size`
        (x, y, w, h) = [v / size for v in face_i] # each coordinate will be treated as v/2  ex. x/2, y/2
        face = gray_frame[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (img_width, img_height))

    # Try to recognize the face
        (prediction, confidence) = model.predict(gray_frame) # return list of integer values

    # print(prediction, confidence)
        if (confidence<95 and names[prediction] not in recog_names):
            # if confidence<95 then draw a green rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # adding name to recog_names
            recog_names.append(names[prediction])
            # also into recognized list
            recognized.append((names[prediction].capitalize(), confidence))
        # if confidence>=95 then draw a red rectangle with name
        elif (confidence >= 95):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return (frame, recognized) 

train_model()
