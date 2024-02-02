import os

def find_files_in_dir(path, file_format_list):
    return_list = []
    # 获取指定路径下的所有文件和目录名
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        # 检查是否为文件且符合指定的格式
        if os.path.isfile(full_path) and any(item.endswith(format) for format in file_format_list):
            return_list.append(full_path)
    return return_list


if __name__ == "__main__":
    path = "./example_dir/mp4"
    print(find_files_in_dir(path, [".mp4", ".py"]))

