import cv2
import copy
import numpy as np
from tqdm import tqdm

from utils.color_mask import color_mask
from utils.find_files_in_dir import find_files_in_dir


def overlay_img(dir_path, start_index=0):
    file_paths = find_files_in_dir(dir_path, [".png"])
    base_img = cv2.imread(file_paths[start_index])
    base_mask = color_mask(base_img, vertical_mask=True)
    base_mask = base_mask[:, :, np.newaxis] * np.ones((1, 1, 3), dtype="uint8")
    base_img = cv2.bitwise_and(base_img, base_mask)
    # print(base_mask.shape)
    result = None
    for i in tqdm(range(1, len(file_paths))):
        if np.all(base_mask == 255):
            break
        img = cv2.imread(file_paths[i])
        mask = color_mask(img, vertical_mask=True)
        mask = mask[:, :, np.newaxis] * np.ones((1, 1, 3), dtype="uint8")
        mask = cv2.subtract(mask, base_mask)
        # print(img.shape, mask.shape)
        img = cv2.bitwise_and(img, mask)
        base_img = cv2.bitwise_or(base_img, img)
        base_mask = cv2.bitwise_or(base_mask, mask)

        cv2.imshow("img", base_img)
        cv2.waitKey()


if __name__ == "__main__":
    overlay_img("./example_dir/cropped", 8)
