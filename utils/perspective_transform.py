import cv2
import numpy as np

import sys

sys.path.append('.')
from utils import select_corners


def distance_between_points(p1, p2):
    """Calculate the distance between two points"""
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def perspective_transform(img, points):
    """Apply perspective transform to the given image"""

    # Ensure that exactly four points are provided
    if len(points) != 4:
        raise ValueError("Exactly four points are required")

    pts_src = np.array(points, dtype=np.float32)

    # Calculate the width and height of the target image
    width = distance_between_points(pts_src[0], pts_src[1])
    height = distance_between_points(pts_src[0], pts_src[3])

    # Specify the coordinates of the four corners of the transformed image
    # Order: Right Top, Left Top, Left Bottom, Right Bottom
    pts_dst = np.array([[width-1, 0], [0, 0], [0, height-1],
                       [width-1, height-1]], dtype=np.float32)

    # Calculate the perspective transform matrix
    M = cv2.getPerspectiveTransform(pts_src, pts_dst)

    # Apply the perspective transformation
    transformed_img = cv2.warpPerspective(img, M, (int(width), int(height)))

    return transformed_img


if __name__ == "__main__":
    # Usage example
    file_path = "./example_dir/captured_img/0.png"
    img = cv2.imread(file_path)
    corners = select_corners.select_corner(img)
    print(type(corners))
    print(corners)
    transformed_image = perspective_transform(img, corners)
    cv2.imshow('Transformed Image', transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
