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


def main(video_path):
    v_basename = os.path.basename(video_path)
    v_basename, _ = os.path.splitext(v_basename)
    dir_path = os.path.join("./cache", v_basename)
    print(f'Working dir: "{dir_path}"')
    os.makedirs(dir_path, exist_ok=True)

if __name__ == "__main__":
    main("./mp4_videos/example1.mp4")
