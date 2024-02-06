import cv2
import numpy as np
import os
from tqdm import tqdm

import util_compare_img
import util_color_map
from util_find_files_in_dir import find_files_in_dir
from util_color_mask import color_mask
from util_written_mask import create_written_mask

def min_max_normalize_to_255(arr):
    normalized = (arr - arr.min()) / (arr.max() - arr.min())  # 正規化到 0-1
    scaled = np.round(normalized * 255)  # 縮放到 0-255 並四捨五入
    return scaled.astype(np.uint8)  # 轉換為無符號整數類型

def main(dir_path):
    file_paths = find_files_in_dir(dir_path, [".png"])
    for file_path in tqdm(file_paths):
        img=cv2.imread(file_path)

        result = create_written_mask(img)
        # cv2.imshow("result", result)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        vertical_sum = result.sum(axis=0)
        vertical_sum = min_max_normalize_to_255(vertical_sum)

        mask = np.tile(vertical_sum, (img.shape[0],1))

        mask = cv2.GaussianBlur(mask, (51, 5), 0)
        
        block_mask = color_mask(img, vertical_mask=True)
        mask = cv2.bitwise_and(mask, block_mask)
        result = cv2.bitwise_and(result, block_mask)
        # cv2.imwrite(f"./example_dir/written_mask_with_vmask/{os.path.basename(file_path)}", result)
        
        

        img_with_mask = util_color_map.apply_colored_mask_on_image(img, mask)

        cv2.imshow("img", result)
        cv2.imshow("result", img_with_mask)
        cv2.waitKey(0)
        # cv2.destroyAllWindows()

def test_add(dir_path):
    file_paths = find_files_in_dir(dir_path, [".png"])
    base_img = cv2.imread(file_paths[0])
    for i in tqdm(range(1,len(file_paths))):
        img = cv2.imread(file_paths[i])
        base_img = cv2.add(base_img, img)
        cv2.imshow(f"{i}.png", base_img)
        cv2.waitKey()
        cv2.destroyAllWindows()

def substract_img(dir_path, start_index=0):
    file_paths = find_files_in_dir(dir_path, [".png"])
    base_img = cv2.imread(file_paths[start_index])
    for i in tqdm(range(start_index+1,len(file_paths))):
        img = cv2.imread(file_paths[i])
        result = cv2.subtract(base_img, img)
        cv2.imshow(f"{i}.png", result)
        cv2.waitKey()
        cv2.destroyAllWindows()
        







# test_add("./example_dir/written_mask_with_vmask") 
# main("./example_dir/cropped")
substract_img("./example_dir/written_mask_with_vmask", start_index=40)

