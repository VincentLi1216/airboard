import cv2
import numpy as np
import os
from tqdm import tqdm

from util_capture_frame import capture_frames
from util_crop4dir import crop4dir
from util_find_critical_indices import find_critical_indices

def print_step(step_name):
    print("\n","-"*5, step_name, "-"*5)

def main(video_path, skip_steps=[]):
    # init_workspace
    print_step("Initializing Workspace")
    if "init_workspace" not in skip_steps:
        v_basename = os.path.basename(video_path)
        v_basename, _ = os.path.splitext(v_basename)
        dir_path = os.path.join("./cache", v_basename)
        capture_path = os.path.join(dir_path, "captured")
        cropped_path = os.path.join(dir_path, "cropped")
        print(f'Working dir: "{dir_path}"')
        for dir in [dir_path, capture_path, cropped_path]:
            os.makedirs(dir, exist_ok=True)
            print(f'mkdir: "{dir}"')
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
        find_critical_indices(cropped_path)
    else:
        print("Skipped")
    
    

if __name__ == "__main__":
    main("./mp4_videos/example_EM.mp4", skip_steps=["capture_frames", "crop_img"])
