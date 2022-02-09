import os
folder = r'D:\Workspace\PPL\Assignment\Assignment 1\src\test\testcases'
#folder = r'D:\Workspace\PPL\Assignment\Assignment 1\src\test\solutions'
lexer_list = []
parser_list = []
for base, dirs, files in os.walk(folder):
    for file in files:
        list = file.split('.')
        file_name, tail = list[0], list[1]
        if (tail != 'txt'): continue
        if (int(file_name) >= 100 and int(file_name) <= 199 and file_name not in lexer_list): 
            lexer_list.append(file_name)
        elif (int(file_name) >= 200 and int(file_name) <= 299 and file_name not in parser_list):
            parser_list.append(file_name)

print(len(lexer_list))
print(len(parser_list))