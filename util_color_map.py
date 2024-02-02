import cv2
import numpy as np

def color_map(img):
    is_BGR = None

    if len(img.shape) == 3:
        # Width and height are the second and third elements
        (height, width, _) = img.shape
        is_BGR = True
    elif len(img.shape) == 2:
        # Width and height for grayscale image
        (height, width) = img.shape
        is_BGR = False

    # Convert the values matrix to a grayscale image
    gray_values = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if is_BGR else img

    # Convert grayscale image to a color map
    colored_overlay = cv2.applyColorMap(gray_values, cv2.COLORMAP_JET)

    if not is_BGR:
        # If the original image is grayscale, convert it to BGR
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # Overlay original image with color map
    alpha = 0.5
    overlayed_image = cv2.addWeighted(img, 1 - alpha, colored_overlay, alpha, 0)

    return overlayed_image

if __name__ == "__main__":
    img = cv2.imread("./ex_moon.jpg")

    result = color_map(img)
    cv2.imshow("result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


