import cv2
import os
from tqdm import tqdm

import utils.find_files_in_dir
import utils.select_corners
import utils.perspective_transform


def crop4dir(input_dir_path, output_dir_path=None, to_show=False):
    ok_formats = [".png", ".jpg"]
    file_paths = utils.find_files_in_dir.find_files_in_dir(
        input_dir_path, ok_formats)

    corners = utils.select_corners.select_corner(
        cv2.imread(file_paths[0]))
    for file_path in tqdm(file_paths):
        file_name = os.path.basename(file_path)
        img = cv2.imread(file_path)
        img = utils.perspective_transform.perspective_transform(
            img, corners)

        if to_show:
            cv2.imshow("output", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if output_dir_path != None:
            cv2.imwrite(os.path.join(output_dir_path, file_name), img)


if __name__ == "__main__":
    crop4dir("./example_dir/example", "./example_dir/cropped", False)
