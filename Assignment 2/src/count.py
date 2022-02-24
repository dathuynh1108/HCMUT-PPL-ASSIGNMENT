import os, subprocess
from functools import reduce

folder_list = [
    r'./test/testcases',
    r'./test/solution'
]

subprocess.run(["powershell", "del", "./test/testcases/*.txt"], shell=True)
subprocess.run(["powershell", "del", "./test/solutions/*.txt"], shell=True)
subprocess.run(["powershell", "python", "run.py","test", "ASTGenSuite"], shell=True)

def check(file_name, file_list):
    return int(file_name) >= 300 and int(file_name) <= 399 and file_name not in file_list

for folder in folder_list:
    for base, dirs, files in os.walk(folder):
        for file in files:
            list = file.split('.')
            file_name, tail = list[0], list[1]
            if (tail != 'txt'): continue
        file_list = reduce(lambda file_list, current_file: file_list + [current_file] if check(file_name, file_list) else file_list, files, [])
    print(len(file_list))

