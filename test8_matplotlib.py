import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import cv2

from util_find_files_in_dir import find_files_in_dir


dir_path = "./example_dir/subtrack_back_with_mask"
img_paths = find_files_in_dir(dir_path, [".png"])

pixel_list = np.array([])
x = np.arange(len(img_paths))

for img_path in tqdm(img_paths):
    img = cv2.imread(img_path)
    totol_count = np.sum(img)
    pixel_list = np.append(pixel_list, totol_count)

# print(pixel_list)
window_size = 3
smooth = np.convolve(pixel_list, np.ones(window_size)/window_size, mode='valid')
diff = np.diff(smooth)
plt.plot(x, pixel_list, "r-")
plt.plot(np.arange(len(smooth)), smooth, "b-")
plt.plot(diff, "g-")
plt.show()
