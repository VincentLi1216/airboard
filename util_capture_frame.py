import os
from moviepy.editor import VideoFileClip
from PIL import Image
import numpy as np

def capture_frames(video_path, interval, max_duration=None):
    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Video file does not exist: {video_path}")
        return

    # Get the video file name (excluding the extension)
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Create a folder with the video name to store screenshots
    output_folder = os.path.join(os.path.dirname(video_path), video_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video
    clip = VideoFileClip(video_path)

    # Calculate the number of screenshots
    total_frames = int(clip.duration // interval)

    # Capture and save images
    for i in range(total_frames):
        frame_time = i * interval
        frame = clip.get_frame(frame_time)
        frame_image = Image.fromarray(frame)
        frame_path = os.path.join(output_folder, f"{i}.png")
        frame_image.save(frame_path)
        print(f"{i}.png completed")
        
        if max_duration is not None:
            if i*interval >= max_duration:
                break

    print(f"Screenshots completed, saved in the folder {output_folder}.")



if __name__ == "__main__":
    # Example usage
    video_file_path = "./example_dir/mp4/example.mp4"  # Set your video path
    interval = 20  # Set the screenshot interval in seconds
    capture_frames(video_file_path, interval)



