# import required modules
import cv2, numpy, os


size = 2
#using face_cascade.xml file for recognition
haar_cascade = cv2.CascadeClassifier('face_cascade.xml')

def train_model():
#     Pre-built face recognition models

#     OpenCV supports local binary patterns histograms (or shortly LBPH), eigenface and fisherface methods. We can run them all within opencv.
    model = cv2.face.LBPHFaceRecognizer_create()
    #model = cv2.face.EigenFaceRecognizer_create()
    #model = cv2.face.FisherFaceRecognizer_create()
    fn_dir = 'face_samples2'

    (images, lables, names, id) = ([], [], {}, 0)

    for (subdirs, dirs, files) in os.walk(fn_dir):
        # Loop through each folder named 
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(fn_dir, subdir)
            # Loop through each photo in the folder
            for filename in os.listdir(subjectpath):
                # Skip non-image formates
                f_name, f_extension = os.path.splitext(filename)
                if(f_extension.lower() not in ['.png','.jpg','.jpeg','.gif','.pgm']):
                    print("Skipping "+filename+", wrong file type")
                    continue
                path = subjectpath + '/' + filename
                lable = id
                # Add to training data
                images.append(cv2.imread(path, 0))
                lables.append(int(lable))
            id += 1

    # Convert a list of images and labels to np array to train tensorflow
    (images, lables) = [numpy.array(lis) for lis in [images, lables]]
    # OpenCV trains a model from the images
    model.train(images, lables)

    return (model, names)

# function for recognition 
def recognize_face(model, frame, gray_frame, face_coords, names): 
    (img_width, img_height) = (112, 92)
    #defining two list (using list because list is mutable in python also direct access is possible)
    recognized = []
    recog_names = []

    for i in range(len(face_coords)): # face_coords is list
        face_i = face_coords[i]

        # Coordinates of face after scaling down by size
        (x, y, w, h) = [v * size for v in face_i]
        # converting this face to gray frame
        face = gray_frame[y:y + h, x:x + w]
        # resize the face
        face_resize = cv2.resize(face, (img_width, img_height))

        # Try to recognize the face
        (prediction, confidence) = model.predict(face_resize)

        # print(prediction, confidence)
        if (confidence<95 and names[prediction] not in recog_names):
            # if confidence<95 then draw a green rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # if confidence>=95 then draw a red rectangle with name
        elif (confidence >= 95):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return (frame, recognized) 

train_model()
