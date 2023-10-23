import os
import time
from multiprocessing import Pool

# 需要文件量相当大，否则，单进程比多进程还快

# 单进程操作
'''
# 实现文件的拷贝
def copyFile(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")

    context = fr.read()
    fw.write(context)

    fr.close()
    fw.close()


Path = r"D:\_Code\Text"

toPath = r"D:\_Code\ToText"

# 读取Path下的所有文件
filesList = os.listdir(Path)

# 启动for循环处理每一个文件
start = time.time()

for fileName in filesList:
    copyFile(os.path.join(Path, fileName), os.path.join(toPath, fileName))

end = time.time()

print(end - start)
'''


# 多进程实现

# 实现文件的拷贝
def copyFile(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")

    context = fr.read()
    fw.write(context)

    fr.close()
    fw.close()


# 原文件地址
Path = r"D:\_Code\Text"

# 文件拷贝地址
toPath = r"D:\_Code\ToText"

if __name__ == "__main__":

    start = time.time()

    # 读取Path下的所有文件
    filesList = os.listdir(Path)

    pp = Pool(4)

    for fileName in filesList:
        pp.apply_async(copyFile, args=(os.path.join(Path, fileName), os.path.join(toPath, fileName)))

    pp.close()
    pp.join()

    end = time.time()

    print(end - start)
