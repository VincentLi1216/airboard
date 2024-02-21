import cv2
import mediapipe as mp
import numpy as np

# 初始化 MediaPipe 自拍分割模塊
mp_selfie_segmentation = mp.solutions.selfie_segmentation

def create_human_mask(img):
    # 讀取圖像並調整尺寸
    # img = cv2.resize(img, (520, 300))

    # 將 BGR 圖像轉換為 RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 使用 MediaPipe 自拍分割
    with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_segmentation:
        results = selfie_segmentation.process(img_rgb)

    # 創建二值化遮罩
    mask = (results.segmentation_mask > 0.01).astype(np.uint8) * 255

    return mask



if __name__ == "__main__":
    # 使用範例
    img = cv2.imread("./example_frame_9.png")
    mask = create_human_mask(img)
    cv2.imshow("img", img)
    cv2.imshow('Human Mask', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

