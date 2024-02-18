import cv2
import numpy as np
import os
from tqdm import tqdm
import matplotlib.pyplot as plt

import util_compare_img
import util_color_map
from util_find_files_in_dir import find_files_in_dir
from util_color_mask import color_mask
from util_written_mask import create_written_mask
from util_conv_array import conv_array, diff_array, filter_np_array

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
        
def substract_img_from_the_back(dir_path):
    pixel_list = np.array([])


    file_paths = find_files_in_dir(dir_path, [".png"])

    x=np.arange(len(file_paths)-1)

    base_img = cv2.imread(file_paths[-1])
    base_mask = color_mask(base_img)
    base_img = create_written_mask(base_img)
    base_img = cv2.bitwise_and(base_img, base_mask)
    for i,file_path in enumerate(tqdm(file_paths)):
        if i == len(file_paths)-1:break
        img = cv2.imread(file_path)
        img_mask = color_mask(img)
        img = create_written_mask(img)
        img = cv2.bitwise_and(img, img_mask)
        result = cv2.subtract(img, base_img)

        mask_count = np.sum(img_mask)
        result_count = np.sum(result)
        pixel_list = np.append(pixel_list, result_count/mask_count)

        # cv2.imwrite(f"./example_dir/subtrack_back_with_mask/{i}.png", result)

        # cv2.imshow(f"{i}.png", result)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
    window_size = 10
    smooth = conv_array(pixel_list, window_size)
    # smooth = smooth[-len(pixel_list):]
    # print(smooth.shape)
    diff = diff_array(smooth)
    diff = conv_array(diff, window_size)
    diff[diff>0] = 0 
    diff = filter_np_array(diff)
    
    # diff = conv_array(diff, 14)
    diff2 = diff_array(diff)
    # diff2 = conv_array(diff2, window_size)
    diff2 = filter_np_array(diff2)
    diff3 = diff_array(diff2)

    range_list = []
    in_range = False
    start_index = None
    for index, i in enumerate(diff):
        if i < 0 and not in_range:
            in_range = True
            start_index = index

        if i == 0 and in_range:
            in_range = False
            range_list.append([start_index, index])
    print(range_list)
    
    # 存儲每個範圍最小值索引的列表
    min_indices = []

    for r in range_list:
        start, end = r
        # 尋找每個範圍內的最小值的索引
        min_index = np.argmin(diff[start:end]) + start
        min_indices.append(min_index)

    print(min_indices)


        

    # print(diff2)
    plt.plot(x, pixel_list, "r-o", label="original")
    plt.plot(smooth, "b-o", label="conv_array")

    plt.plot(diff*3 , "g-", label="diff1")
    # plt.plot(diff2, "y-", label="diff2")
    # plt.plot(diff3, "c-", label="diff3")
    plt.plot(np.zeros(len(x)), "m-")
    plt.legend()
    plt.show()


# test_add("./example_dir/written_mask_with_vmask") 
# main("./example_dir/cropped")
# substract_img("./example_dir/written_mask_with_vmask", start_index=40)

substract_img_from_the_back("./example_dir/cropped")
