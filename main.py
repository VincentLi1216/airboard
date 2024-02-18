import cv2
import numpy as np
import os
from tqdm import tqdm
import json

from util_capture_frame import capture_frames
from util_crop4dir import crop4dir
from util_find_critical_indices import find_critical_indices
from util_combine_img import combine

def print_step(step_name):
    print("\n","-"*5, step_name, "-"*5)

def main(video_path, skip_steps=[]):
    # init_workspace
    print_step("Initializing Workspace")
    if "init_workspace" not in skip_steps:
        # mkdir cache
        os.makedirs("./cache", exist_ok=True)
        v_basename = os.path.basename(video_path)
        v_basename, _ = os.path.splitext(v_basename)
        dir_path = os.path.join("./cache", v_basename)
        capture_path = os.path.join(dir_path, "captured")
        cropped_path = os.path.join(dir_path, "cropped")
        result_path = os.path.join(dir_path, "final_result")
        print(f'Working dir: "{dir_path}"')
        dirs = [dir_path, capture_path, cropped_path, result_path]
        for dir in dirs:
            print(f'mkdir: "{dir}"')

        json_path = os.path.join(dir_path, "info.json")
        if not os.path.exists(json_path):
            print(f'touch: "{json_path}"')
            os.system(f"touch {json_path}")

        for dir in tqdm(dirs):
            os.makedirs(dir, exist_ok=True)

    else:
        print("Skipped")
    
    # capture_frames
    print_step("Capturing Frames")
    if "capture_frames" not in skip_steps:
        print(f'From: "{video_path}"\nTo: "{capture_path}"')
        capture_frames(video_path, capture_path, interval=20)
    else:
        print("Skipped")

    # crop_img
    print_step("Cropping Images")
    if "crop_img" not in skip_steps:
        crop4dir(capture_path, cropped_path)
    else:
        print("Skipped")

    # find_critical_indices
    print_step("Find Critical Indices")
    if "find_critical_indices" not in skip_steps:
        critical_indices, critical_ranges = find_critical_indices(cropped_path)
        # add the last img to the list
        critical_indices.append(len(os.listdir(cropped_path))-2)
        data = {"critical_indices":critical_indices, "critical_ranges":critical_ranges}
        with open(json_path, "w") as f:
            json.dump(data, f)
    else:
        with open(json_path, "r") as f:
            data = json.load(f)
        critical_indices = data["critical_indices"]
        print("Skipped")

    # combine_img
    print_step("Combining Images")
    print(critical_indices)
    if "combine_img" not in skip_steps:
        for index, i in enumerate(tqdm(critical_indices)):
            if index == len(critical_indices)-1: 
                img_index = i
                print("hi")
            else:
                offset = -2
                img_index = i+offset
            save_path = os.path.join(result_path, f"{img_index}.png")
            res = combine(cropped_path, i)
            cv2.imwrite(save_path, res)
    else:
        print("Skipped")
    

if __name__ == "__main__":
    main("./mp4_videos/example_EM.mp4", skip_steps=["capture_frames", "crop_img"])
