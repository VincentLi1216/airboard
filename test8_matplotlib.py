import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import cv2

from util_find_files_in_dir import find_files_in_dir


dir_path = "./example_dir/substarct_img2-1"
img_paths = find_files_in_dir(dir_path, [".png"])

pixel_list = np.array([])
x = np.arange(135)

for img_path in tqdm(img_paths):
    img = cv2.imread(img_path)
    totol_count = np.sum(img)
    pixel_list = np.append(pixel_list, totol_count)

print(pixel_list)

plt.plot(x, pixel_list, "r-")
plt.show()
