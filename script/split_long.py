import re
def split(filename):
    new_line=[]
    with open(filename,"r") as f:
        lines=f.readlines()
        for line in lines:
            if len(line)>100:
                n=re.sub(r'(\d+)',r'\n\1',line)
                #print(n)
                new_line.append(n)
            else:
                new_line.append(line)
    return ''.join(new_line)
def remove_line(filename):
    with open(filename,"r") as f:
        content=f.read()

def save(filename,content):
    with open(filename,"w") as f:
        f.write(content)
#filename="bible/GEN01.md"

#a=split(filename)
#save(filename,a)
#print(a)

import os
import glob

# 定义目录路径
directory = 'bible'

# 使用 glob 模块获取指定目录下的所有 .md 文件路径
md_files = glob.glob(os.path.join(directory, '*.md'))

# 遍历输出每个 .md 文件的路径名
for file_path in md_files:
    print(file_path)
    a=split(file_path)
    save(file_path,a)


