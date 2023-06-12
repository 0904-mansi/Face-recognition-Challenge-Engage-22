# register.py
import cv2
from face_detection import detect_faces

def registerCriminal(img, path, img_num):  
    (im_width, im_height) = (112, 92)
    # applied formula so that new image will be start from odd num
    file_num = 2*img_num - 1
    # for image 1 filenum will be one
    # for image 2 filenum will be 3
   # converting RGB to gray Because it is a one layer image from 0-255 whereas the RGB have three different layer image. 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # calling detect face function will return face
    faces = detect_faces(gray)

    if(len(faces) > 0):
        faces = sorted(faces, reverse=True)  # sort based on height of image in desc order
        face_i = faces[0]
        (x, y, w, h) = [v for v in face_i]
        face = gray[y:y + h, x:x + w]
       # resizing image according to height and width
        face = cv2.resize(face, (im_width, im_height))

        print("Saving training sample " + str(img_num)+".1")
        # Save image file in face sample directory
        cv2.imwrite('%s/%s.png' % (path, file_num), face)
        file_num += 1

        # Saving flipped image in face sample directory
        print("Saving training sample " + str(img_num)+".2")
        # flipping image horizontally
        face = cv2.flip(face, 1)
        # save the image in corresponding path
        cv2.imwrite('%s/%s.png' % (path, file_num), face)

    else:
        # No face present
        print("img %d : Face is not present" % (img_num))
        return img_num

    return None
