# 栈：先进后出

# 模拟栈结构
stack = []

# 压栈（向栈存数据）
stack.append("A")
print(stack)

stack.append("B")
print(stack)

stack.append("C")
print(stack)

# 出栈（在栈取数据）
res = stack.pop()
print(res)
print(stack)

res2 = stack.pop()
print(res2)
print(stack)

# 队列：先进先出
import collections

# 创建一个队列
queue = collections.deque()
print(queue)

# 进队（存数据）
queue.append("A")
print(queue)

queue.append("B")
print(queue)

queue.append("C")
print(queue)

# 出队（取数据）
res4 = queue.popleft()
print(res4)
print(queue)

res5 = queue.popleft()
print(res5)
print(queue)

# 栈模拟递归遍历目录（深度遍历）
import os


def getAllDirDE(path):
    # 第一个栈
    stack = []

    # 压栈
    stack.append(path)

    # 处理栈，当栈为空时停止循环
    while len(stack) != 0:
        # 取出栈数据
        dirPath = stack.pop()
        print(dirPath)

        # 目录下所有文件
        filesList = os.listdir(dirPath)
        print(filesList)
        # 判断是否是文件夹或者文件，文件夹压栈，普通文件打印输出
        for fileNmae in filesList:

            fileAbsPath = os.path.join(dirPath, fileNmae)

            if os.path.isdir(fileAbsPath):

                # 如果是文件夹，就压栈。否则就打印普通文件
                print("目录：", fileNmae)
                stack.append(fileAbsPath)
            else:
                print("普通文件：", fileNmae)


getAllDirDE(r"D:\Cache")

# 队列模拟递归遍历目录（广度遍历）

import collections


def getAllDirQU(path):
    queue = collections.deque()

    # 进队
    queue.append(path)

    while len(queue) != 0:
        # 出队
        dirPath = queue.popleft()

        # 找出所有的文件
        filesList = os.listdir(dirPath)

        for fileName in filesList:

            fileAbsPath = os.path.join(dirPath, fileName)

            # 如果是文件夹，就进队。否则就打印普通文件
            if os.path.isdir(fileAbsPath):
                print("目录：", fileName)

                # 进队
                queue.append(fileAbsPath)
            else:
                print("普通文件：", fileName)


getAllDirQU(r"D:\Cache")
