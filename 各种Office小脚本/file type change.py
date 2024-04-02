import os

# 列出当前目录下所有的文件
files = os.listdir('.')  # 如果path为None，则使用path = '.' 

for filename in files:
    portion = os.path.splitext(filename)  # 分离文件名与扩展名
    if (portion[1] == '.cpp'):
        newname = portion[0] + '.c'
        os.rename(filename, newname)
