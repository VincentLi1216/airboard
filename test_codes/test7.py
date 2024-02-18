from tqdm import tqdm
import cv2, os

from util_find_files_in_dir import find_files_in_dir
from util_compare_img import compare_images

dir_path = "./example_dir/written_mask"
file_paths = find_files_in_dir(dir_path, ["png"])

# img1 = cv2.imread("./example_dir/written_mask/40.png")
# img2 = cv2.imread("./example_dir/written_mask/100.png")

# img = cv2.subtract(img2, img1)
# cv2.imshow("img",img)
# cv2.waitKey()


for i in tqdm(range(0,len(file_paths)-1)):
    img1 = cv2.imread(file_paths[0])
    img2 = cv2.imread(file_paths[i+1])
    # img = compare_images(cv2.imread(file_paths[i]), cv2.imread(file_paths[i+1]))

    img = cv2.subtract(img1,img2)
    # img = cv2.medianBlur(img, 5)
    saved_file_name = f"./example_dir/substarct_img1-2/{os.path.basename(file_paths[i])}"
    cv2.imwrite(saved_file_name, img)
    # cv2.imshow("good", img)
    # cv2.waitKey(0)
