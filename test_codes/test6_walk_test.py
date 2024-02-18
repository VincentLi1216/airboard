import os

dir_path = "./example"
for folder, subfolders, filenames in os.walk(dir_path):
    print(f'目前資料夾路徑為：{folder}')
    
    for subfolder in subfolders:
        print(f'{folder}的子資料夾為：{subfolder}')

    for filename in filenames:
        print(f'{folder}內含檔案為：{filename}')
        print(os.path.join(folder, filename))

