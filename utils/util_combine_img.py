import cv2
import numpy as np
import os

from utils.util_color_mask import color_mask


def combine(path, index, extension=".png", to_show=False):
    i = index
    img_path = os.path.join(path, f"{i}{extension}")
    img = cv2.imread(img_path)
    img_mask = color_mask(img, vertical_mask=True)
    img = cv2.bitwise_and(img, img, mask=img_mask)
    if to_show:
        cv2.imshow("img", img)
        cv2.waitKey()
        cv2.destroyAllWindows()
    while np.any(img_mask == 0):
        i -= 1
        new_img_path = os.path.join(path, f"{i}{extension}")
        new_img = cv2.imread(new_img_path)
        new_img_mask = color_mask(new_img, vertical_mask=True)
        combine_mask = cv2.subtract(new_img_mask, img_mask)
        new_img = cv2.bitwise_and(new_img, new_img, mask=combine_mask)
        img = cv2.add(img, new_img)
        img_mask = cv2.add(img_mask, combine_mask)
        if to_show:
            cv2.imshow("img", img)
            cv2.waitKey()
            cv2.destroyAllWindows()

    return img


if __name__ == "__main__":
    combine("./cache/example_EM/cropped", 91, to_show=True)
