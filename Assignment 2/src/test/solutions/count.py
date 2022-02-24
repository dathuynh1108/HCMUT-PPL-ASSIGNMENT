import os
folder = r'D:\Workspace\PPL\Assignment\Assignment 2\src\test\solutions'
#folder = r'D:\Workspace\PPL\Assignment\Assignment 1\src\test\solutions'
file_list = []
for base, dirs, files in os.walk(folder):
    for file in files:
        list = file.split('.')
        file_name, tail = list[0], list[1]
        if (tail != 'txt'): continue
        if (int(file_name) >= 300 and int(file_name) <= 399 and file_name not in file_list): 
            file_list.append(file_name)
print(len(file_list))
