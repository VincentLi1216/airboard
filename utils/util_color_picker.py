import cv2
import numpy as np


def show_color(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        bgr = image[y, x]
        rgb = bgr[::-1]
        hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]

        color_info = f"RGB: {rgb}, BGR: {bgr}, HSV: {hsv}"
        print(color_info)


# 讀取圖像
image = cv2.imread('./example_dir/cropped/117.png')  # 替換成你的圖像路徑
if image is None:
    print("Error: Unable to load image. Check file path.")
    exit()

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', show_color)

# 顯示圖像
while True:
    cv2.imshow('Image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
