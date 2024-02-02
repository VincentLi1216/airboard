import cv2
import numpy as np

def color_map(img):

    (width, height, _) = img.shape
    print(width, height)
    # 創建一個對應的數值矩陣，範圍在 0 到 1 之間
    overlay_values = np.random.random((width, height))

    # 將數值矩陣轉換為灰度圖像
    gray_values = (overlay_values * 255).astype(np.uint8)
    gray_values = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 使用 OpenCV 的 applyColorMap 函數將灰度圖像轉換為彩色圖像
    colored_overlay = cv2.applyColorMap(gray_values, cv2.COLORMAP_JET)

    # 疊加原圖和彩色覆蓋層
    alpha = 0.5
    overlayed_image = cv2.addWeighted(img, 1 - alpha, colored_overlay, alpha, 0)

    return overlayed_image

if __name__ == "__main__":

    img=cv2.imread("./ex_moon.jpg")

    result = color_map(img)
    cv2.imshow("result", result)
    cv2.waitKey(0)
    cv2.DestoryAllWindows()
