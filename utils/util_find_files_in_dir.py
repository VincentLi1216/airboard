import os
import re


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]


def find_files_in_dir(path, file_format_list):
    return_list = []
    # 获取指定路径下的所有文件和目录名
    file_names = os.listdir(path)
    file_names.sort(key=natural_sort_key)  # 修改這裡
    # print(file_names)
    for item in file_names:
        full_path = os.path.join(path, item)
        # 检查是否为文件且符合指定的格式
        if os.path.isfile(full_path) and any(item.endswith(format) for format in file_format_list):
            return_list.append(full_path)
    return return_list


if __name__ == "__main__":
    path = "./example_dir/cropped"
    print(find_files_in_dir(path, [".png", ".jpg"]))
