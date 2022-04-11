# Задание 3
from asyncore import write
import os

def file_add_write(file_name_src:str, content:str, file_name_result:str, file_num:int):
    if file_num == 1:
        option_write = 'w'
    else:
        option_write = 'a'
    with open(file_name_result, option_write) as file_result:
        file_result.write(f"{file_name_src}\n")
        file_result.write(f"{len(content)}\n")
    # with open(file_name_result, 'a') as file_result:
        file_result.writelines(content)
        file_result.write("\n")

def file_read_content(file_name:str):
    with open(file_name, 'rt') as file:
        return file.readlines()

BASE_PATH = os.getcwd()
FILE_DIR_1 = 'netology_python'
FILE_DIR_2 = 'files_txt'
FILE_NAME_RESULT = 'unite_result.txt'
DIR_PATH = os.path.join(BASE_PATH, FILE_DIR_1, FILE_DIR_2)
files = os.listdir(DIR_PATH)
files_txt_name = list(filter(lambda x: x.endswith('.txt'), files))
# print(files_txt_name)

dict_files = dict()
for file_name in files_txt_name:
    with open(os.path.join(DIR_PATH, file_name), 'rt') as file:
        content = file.readlines()
        dict_files[file_name] = len(content)
        # dict_files[file_name]["count_str"] = len(content)
        # dict_files[file_name]["content"] = content
dict_files_sorted = sorted(dict_files.items(), key=lambda x: x[1])
dict(dict_files_sorted)

print(dict_files_sorted)

file_num = 1
for file_name in dict_files_sorted:
    content = file_read_content(os.path.join(DIR_PATH, file_name[0]))
    file_add_write(file_name[0], content, os.path.join(BASE_PATH, FILE_DIR_1, FILE_NAME_RESULT), file_num)
    file_num += 1

