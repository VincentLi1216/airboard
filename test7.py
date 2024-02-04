import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

# 假設 file_list 是包含檔案名稱的列表
file_list = ["20.png", "1.png", "100.png", "0.png"]

# 使用自然排序
file_list.sort(key=natural_sort_key)

print(file_list)

