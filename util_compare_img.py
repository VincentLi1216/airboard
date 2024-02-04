import cv2
import numpy as np

import util_color_map

def compare_images(img1, img2):
    # Step 2: Resize images if they are different sizes
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Step 3: Compute the absolute difference
    difference = cv2.absdiff(img1, img2)
    
    # Convert the difference to grayscale
    gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

    # Step 4: Normalize the differences to enhance visibility
    normalized_difference = cv2.normalize(gray_difference, None, 0, 255, cv2.NORM_MINMAX)

    return normalized_difference


if __name__ == "__main__":
    img1 = cv2.imread("./example_dir/cropped/100.png")
    img2 = cv2.imread("./example_dir/cropped/12.png")
    diff_img = compare_images(img1, img2)

    # 標準化圖像
    diff_img= cv2.normalize(diff_img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

    print(diff_img.shape)
    color_map_img = util_color_map.color_map(diff_img)
    
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('diff_img', diff_img)
    cv2.imshow("color map", color_map_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

