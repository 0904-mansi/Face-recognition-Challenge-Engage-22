# register.py
import cv2
from facerec2 import detect_faces
# function for registering a person
def registerPerson(img, path, img_num):
    size = 2
    (im_width, im_height) = (112, 92)
    file_num = 2*img_num - 1

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#   calling detect_face function for image after converting it to grayscale
    faces = detect_faces(gray)
#   multiple face can also be detected
    if(len(faces) > 0):
# sorts faces based on the value of key as applied to each element of the list
        faces = sorted(faces, key=lambda x: x[3], reverse=True)  # sort based on height of image
#     Taking the largest face detected
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]
# converting RGB to gray Because it is a one layer image from 0-255 whereas the RGB have three different layer image. 
        face = gray[y:y + h, x:x + w]
        face = cv2.resize(face, (im_width, im_height))

        print("Saving training sample " + str(img_num)+".1")
        # Save image file in face sample directory
        cv2.imwrite('%s/%s.png' % (path, file_num), face)
        file_num += 1

        # Saveing flipped image in face sample directory
        print("Saving training sample " + str(img_num)+".2")
        face = cv2.flip(face, 1, 0)
        cv2.imwrite('%s/%s.png' % (path, file_num), face)

    else:
        # No face present return error
        print("img %d : Face is not present" % (img_num))
        return img_num

    return None
