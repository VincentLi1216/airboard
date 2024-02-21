import cv2
import numpy as np
from sklearn.cluster import KMeans

def find_dominant_colors(image_path, k=3):
    # 读取图像
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 转换为一维像素数组
    pixels = img_rgb.reshape((-1, 3))

    # 使用 K-means 算法找出主要颜色
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)

    # 获取颜色聚类的中心
    colors = kmeans.cluster_centers_

    return colors

def define_hsv_range(bgr_color, delta=10):
    # 将 RGB 颜色转换为 HSV
    hsv_color = cv2.cvtColor(np.uint8([[bgr_color]]), cv2.COLOR_BGR2HSV)[0][0]
    
    # 定义 HSV 范围
    lower_bound = np.array([hsv_color[0] - delta, max(hsv_color[1] - delta, 0), max(hsv_color[2] - delta, 0)])
    upper_bound = np.array([hsv_color[0] + delta, min(hsv_color[1] + delta, 255), min(hsv_color[2] + delta, 255)])

    return lower_bound, upper_bound

# 使用示例
dominant_colors = find_dominant_colors('./bur_example.png', k=1)

for color in dominant_colors:
    # 将浮点数颜色转换为整数
    color = np.uint8(color)
    color = np.flip(color)

    lower_bound, upper_bound = define_hsv_range(color, delta=50)
    print(f"Color: {color}, Lower HSV: {lower_bound}, Upper HSV: {upper_bound}")
    # lower_color = cv2.cvtColor(lower_bound, cv2.COLOR_HSV2RGB)
    # lower_color = cv2.cvtColor(lower_bound, cv2.COLOR_HSV2BGR)
    # print(lower_color[0][0])

    # 创建一个高度为 300、宽度为 900 的白色图像
    height = 300
    width = 900
    img = np.full((height, width, 3), 255, dtype=np.uint8)

    # 填充左侧 300x300 区域为 K-means 算法返回的颜色
    img[:300, :300] = color

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



