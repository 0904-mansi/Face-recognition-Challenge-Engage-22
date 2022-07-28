# register.py
import cv2
from facerec import detect_faces

def registerCriminal(img, path, img_num):
    # initializing with 2 because 1 image will be stored 2 times
    size = 2
    (im_width, im_height) = (112, 92)
    # applied formulaa so that new image will be start from odd num
    file_num = 2*img_num - 1
   # converting RGB to gray Because it is a one layer image from 0-255 whereas the RGB have three different layer image. 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # calling detect face function will return face
    faces = detect_faces(gray)

    if(len(faces) > 0):
        # Taking the largest face detected
        faces = sorted(faces, key=lambda x: x[3], reverse=True)  # sort based on height of image
        face_i = faces[0]# taking first image
        (x, y, w, h) = [v * size for v in face_i]

        face = gray[y:y + h, x:x + w]
        face = cv2.resize(face, (im_width, im_height))

        print("Saving training sample " + str(img_num)+".1")
        # Save image file in face sample directory
        cv2.imwrite('%s/%s.png' % (path, file_num), face)
        file_num += 1

        # Saving flipped image in face sample directory
        print("Saving training sample " + str(img_num)+".2")
        face = cv2.flip(face, 1, 0)
        cv2.imwrite('%s/%s.png' % (path, file_num), face)

    else:
        # No face present
        print("img %d : Face is not present" % (img_num))
        return img_num

    return None
