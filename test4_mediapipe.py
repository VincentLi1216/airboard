import os
import cv2
import mediapipe as mp

# 初始化 MediaPipe Pose 模組
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def detect_pose_and_draw(image_path):
    # 讀取圖片
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 檢測姿勢
    results = pose.process(img_rgb)

    # 繪製關節點和連接線
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    return img

if __name__ == "__main__":
    dir_path = "./example"

    for folder, subfolders, filenames in os.walk(dir_path):
        print(f'目前資料夾路徑為：{folder}')
        
        for filename in filenames:
            # print(f'{folder}內含檔案為：{filename}')
            file_path =os.path.join(folder, filename) 
            print(file_path)

            # 使用範例
            img_with_pose = detect_pose_and_draw(file_path)
            cv2.imshow('Pose Detection', img_with_pose)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

