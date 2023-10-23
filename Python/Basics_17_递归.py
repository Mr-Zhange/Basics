# 循环递归
i = 1
result = 1
while i <= 4:
    result *= i
    i += 1

print(result)


# 方法递归
def getNums(num):
    if num > 1:
        return num * getNums(num - 1)
    else:
        return num


print(getNums(4))

# 递归遍历目录

import os


def getAllDir(path):
    # 得到当前目录下所有文件
    filesList = os.listdir(path)

    print(filesList)

    # 处理每一个文件
    for fileName in filesList:

        # 判断是否是文件夹或者文件(要用绝对路径)
        fileAbsPath = os.path.join(path, fileName)

        if os.path.isdir(fileAbsPath):

            print("目录：", fileName)

            getAllDir(fileAbsPath)

        else:
            print("普通文件：", fileName)


getAllDir(r"D:\Cache")
