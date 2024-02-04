import cv2, copy
import numpy as np

import util_find_files_in_dir



def color_mask(input_img, lower_bound, upper_bound, blur_radius=0, show_result=False, erosion_ksize=0):
    img = copy.deepcopy(input_img)
    if blur_radius > 1:  # 確保 blur_radius 是奇數且大於1
        img = cv2.medianBlur(img, blur_radius)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    if erosion_ksize > 0:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (erosion_ksize, erosion_ksize))
        mask = cv2.dilate(mask, kernel)
        mask = cv2.erode(mask, kernel)
        print(mask.shape)
        mask[int(mask.shape[0]-mask.shape[0]*0.05):,:] = 255

    res = cv2.bitwise_and(input_img, input_img, mask=mask) if show_result else mask
    return res



if __name__ == "__main__":
    dir_path = "./example_dir/cropped"

    file_paths = util_find_files_in_dir.find_files_in_dir(dir_path, [".jpg", ".png"])
    for file_path in file_paths:
        print(file_path)
        img = cv2.imread(file_path)
        lower_bound = np.array([47, 14, 82])
        upper_bound = np.array([120, 130, 190])
        res = color_mask(img, lower_bound, upper_bound, blur_radius=41, show_result=True, erosion_ksize=15)
        cv2.imshow('Input', img)
        cv2.imshow('Result', res)
        cv2.waitKey(0)

