import cv2
import numpy as np
from shapely.geometry import Polygon


def add_objects_to_image(img_, objects, color=(255, 0, 0)):
    img = np.copy(img_)
    for (x, y, w, h) in objects:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    return img

def obj_to_poly(obj):
    x, y, w, h = obj
    return Polygon([(x, y), (x+w, y), (x+w, y+h), (x, y+h)])

def objects_touch(faces, hands):
    if len(faces)>0 and len(hands)>0:
        face_poly = obj_to_poly(faces[0])
        for hand in hands:
            hand_poly = obj_to_poly(hand)
            if face_poly.intersects(hand_poly):
                return True
    return False

def find_intersection(faces,hands):
    ret = []
    if len(faces)>0 and len(hands)>0:
        face_poly = obj_to_poly(faces[0])
        for hand in hands:
            hand_poly = obj_to_poly(hand)
            inter = face_poly.intersection(hand_poly)
            if inter:
                ret.append(inter)
    return ret
             