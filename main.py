import cv2
import numpy as np

import util_compare_img
import util_color_map

def min_max_normalize_to_255(arr):
    normalized = (arr - arr.min()) / (arr.max() - arr.min())  # 正規化到 0-1
    scaled = np.round(normalized * 255)  # 縮放到 0-255 並四捨五入
    return scaled.astype(np.uint8)  # 轉換為無符號整數類型


file_path = "./example_dir/cropped/100.png"
img=cv2.imread(file_path)

blur_img = cv2.medianBlur(img,41)

result = util_compare_img.compare_images(img, blur_img)

cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

vertical_sum = result.sum(axis=0)
vertical_sum = min_max_normalize_to_255(vertical_sum)

mask = np.tile(vertical_sum, (img.shape[0],1))

mask = cv2.GaussianBlur(mask, (51, 5), 0)
img_with_mask = util_color_map.apply_colored_mask_on_image(img, mask)

cv2.imshow("result", img_with_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()




