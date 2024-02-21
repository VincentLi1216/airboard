import cv2
import numpy as np
import os
from tqdm import tqdm
import matplotlib.pyplot as plt

import utils.util_compare_img
import utils.util_color_map
from utils.util_find_files_in_dir import find_files_in_dir
from utils.util_color_mask import color_mask
from utils.util_written_mask import create_written_mask
from utils.util_conv_array import conv_array, diff_array, filter_np_array


def find_critical_indices(dir_path, save_path = None, to_show=False, show_plot=False):
    pixel_list = np.array([])
    file_paths = find_files_in_dir(dir_path, [".png"])
    
    # base_img is the last img
    base_img = cv2.imread(file_paths[-1])
    base_mask = color_mask(base_img)
    base_img = create_written_mask(base_img)
    base_img = cv2.bitwise_and(base_img, base_mask)

    # subtract img from the back
    for i in tqdm(range(len(file_paths)-1)):
        file_path = file_paths[i]
        img = cv2.imread(file_path)
        img_mask = color_mask(img)
        img = create_written_mask(img)
        img = cv2.bitwise_and(img, img_mask)
        result = cv2.subtract(img, base_img)

        mask_count = np.sum(img_mask)
        result_count = np.sum(result)
        pixel_list = np.append(pixel_list, result_count/mask_count)

        if save_path != None:
            cv2.imwrite(f"./example_dir/subtrack_back_with_mask/{i}.png", result)

        if to_show:
            cv2.imshow(f"{i}.png", result)
            cv2.waitKey()
            cv2.destroyAllWindows()
    
    # data processing
    window_size = 10
    smooth = conv_array(pixel_list, window_size)
    diff = diff_array(smooth)
    diff = conv_array(diff, window_size)
    diff[diff>0] = 0 
    diff = filter_np_array(diff)
    
    
    # find out negative ranges
    range_list = []
    in_range = False
    start_index = None
    for index, i in enumerate(diff):
        if i < 0 and not in_range:
            in_range = True
            start_index = index

        if i == 0 and in_range:
            in_range = False
            range_list.append([int(start_index), int(index)])
    # print(range_list)
    
    # 存儲每個範圍最小值索引的列表
    min_indices = []

    for r in range_list:
        start, end = r
        # 尋找每個範圍內的最小值的索引
        min_index = np.argmin(diff[start:end]) + start
        min_indices.append(int(min_index))

    # print(min_indices)

    if show_plot:
        print(min_indices, pixel_list[min_indices])
        plt.plot(pixel_list, "r-", label="original")
        plt.plot(smooth, "b", label="conv_array")
        plt.scatter(np.array(min_indices), pixel_list[min_indices], color="c", marker="v")

        plt.plot(diff*3 , "g-", label="diff1")
        plt.plot(np.zeros(len(pixel_list)), "m-")
        plt.legend()
        plt.show()

    return list(min_indices), list(range_list)

if __name__ == "__main__":
    
    find_critical_indices("./example_dir/cropped", show_plot=True)
