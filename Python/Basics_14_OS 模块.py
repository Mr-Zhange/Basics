'''
OS 包含了普通的操作系统的功能
'''

import os

# 获取操作系统类型  Nt：Windows  POSIX：Linux、Unix、Mac OS X
print(os.name)

# 获取操作系统详细信息，Windows无法使用
# print(os.uname())

# 获取操作系统中所有的环境变量
print(os.environ)
# 获取系统中指定的环境变量
print(
    os.environ.get("APPDATA")
)

# 获取当前文件路径
print(os.curdir)

# 获取当前工作目录，即当前脚本所在目录
print(os.getcwd())

# 获取指定路径下所有文件名信息
print(
    os.listdir(
        os.getcwd()
    )
)

# 创建文件目录
os.mkdir("mkdir")

# 删除文件目录
os.rmdir("mkdir")

# 获取文件属性
print(
    os.stat("Basics_01_变量和简单数据类型.py")
)

# 重命名
# os.rename("原文件名","新文件名")

# 删除文件
# os.remove("文件名")

# 可运行终端命令
# os.system("notepad")


# 查看当前绝对路径
print(
    os.path.abspath(".")
)

# 拼接路径
p1 = "C:\\"
p2 = "Windows"

print(
    os.path.join(p1, p2)
)

# 拆分路径
p3 = r"C:\Users\ZHANGZHENG\Documents\Code\Basics\__pycache__\Basics_09_类.cpython-37.pyc"

# 拆分，获取文件名,含扩展名
print(
    os.path.split(p3)
)

# 获取文件名
print(
    os.path.basename(p3)
)

# 拆分，获取扩展名，如没有扩展名，则为空
print(
    os.path.splitext(p3)
)

# 获取文件路径
print(
    os.path.dirname(p3)
)


# 判断是否是目录
print(
    os.path.isdir(p3)
)
print(
    os.path.isdir(p1)
)

# 判断文件是否存在
print(
    os.path.isfile(p3)
)

# 判断目录是否存在
print(
    os.path.exists(p1)
)

# 判断文件大小
print(
    os.path.getsize(p3)
)
