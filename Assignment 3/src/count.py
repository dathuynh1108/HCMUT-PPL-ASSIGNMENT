from cProfile import run
import importlib
import inspect
import os, subprocess
from functools import reduce
import ast
class CountFunc(ast.NodeVisitor):
    func_count = 0
    def visit_FunctionDef(self, node):
        self.func_count += 1


p = ast.parse(open("./test/CheckerSuite.py").read())
f = CountFunc()
f.visit(p)
print(f.func_count)


folder_list = [
    r'./test/testcases',
    r'./test/solution'
]

subprocess.run(["rm", "-i", "./test/testcases/*.txt"])
subprocess.run(["rm", "-i", "./test/solutions/*.txt"])
subprocess.run(["python3", "run.py","test", "CheckerSuite"])

def check(file_name, file_list):
    return int(file_name) >= 400 and int(file_name) <= 499 and file_name not in file_list



print("Testcase and solution: ", end="")
for folder in folder_list:
    for base, dirs, files in os.walk(folder):
        for file in files:
            list = file.split('.')
            file_name, tail = list[0], list[1]
            if (tail != 'txt'): continue
        file_list = reduce(lambda file_list, current_file: file_list + [current_file] if check(file_name, file_list) else file_list, files, [])
    print(len(file_list), end = " ")
