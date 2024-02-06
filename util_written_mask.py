import cv2
import numpy as np

def create_written_mask(img):
    blur_img = cv2.medianBlur(img,41)
    result = util_compare_img(img, blur_img)
    return result
