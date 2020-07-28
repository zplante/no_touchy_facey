import cv2
import winsound
from utils.no_touchy_facey_util import *
from hand_detector import *

cap = cv2.VideoCapture(0)
#cap.set(3, 1280/2)
#cap.set(4, 1024/2)
haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
HandsDetector = TSDetector()

while (True):
    ret, frame = cap.read()
    grey_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faces = haar_face_cascade.detectMultiScale(grey_frame, scaleFactor=1.1, minNeighbors=5)
    hands = HandsDetector.detect(grey_frame)
    img_detected = add_objects_to_image(grey_frame, hands)
    img_detected = add_objects_to_image(img_detected, faces, color=(0, 255, 0))
    
    cv2.destroyAllWindows()
    cv2.imshow('NO TOUCHY FACEY', cv2.cvtColor(img_detected, cv2.COLOR_RGB2BGR))
    if objects_touch(faces,hands):
        print("you did the one thing you werent suppose to")
        break
    if cv2.waitKey(1) == 27: 

            break  # esc to quit

    
cap.release()
cv2.destroyAllWindows()