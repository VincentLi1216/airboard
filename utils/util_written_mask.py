import cv2
import numpy as np
from utils.util_compare_img import compare_images

def create_written_mask(img,blur_radius=41):
    blur_img = cv2.medianBlur(img,blur_radius)
    result = compare_images(img, blur_img)
    return result
