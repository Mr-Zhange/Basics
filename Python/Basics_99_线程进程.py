'''
现代操作系统（Windows、Mac OS、Linux、Unix）都支持“多任务”

什么叫多任务？
操作系统同时可以运行多任务

并发：看上去一起执行，任务数多于CPU核心数
并行：真正一起执行，任务数小于等于CPU核心数

实现多任务方式：
1、多进程模式
2、多线程模式
3、协程模式
4、多进程+多线程模式
'''

'''
对于操作系统而言，一个任务就是一个进程

进程是系统中程序执行和资源分配的基本单位，每个进程都有自己的数据段、代码段、堆栈段
'''

from time import sleep

# 单任务现象
'''
def run():
    while True:
        print("Sunck is a nice man")
        sleep(1.2)

if __name__ == "__main__":
    while True:
        print("Sunck is a good man")
        sleep(1)

    # 不会被执行到，只有上面的while循环结束才会执行到run()
    run()
'''

'''
multiprocessing 库

跨平台版本的多进程模块

Process类来代表一个进程对象
'''

import os

from multiprocessing import Process

# 多进程
'''
def run(str):
    print("启动子进程")

    while True:
        # os.getpid() 获取当前进程的ID号
        # os.getppid() 获取当前进程的父进程ID号
        print("Sunck is a %s man %s - %s" % (str, os.getpid(), os.getppid()))
        sleep(1.2)


if __name__ == "__main__":

    print("主（父）进程启动")

    # 创建子进程
    # target 说明进程执行的任务
    # args 进程数据传递
    p = Process(target=run, args=("nice",))
    # 启动子进程
    p.start()

    while True:
        print("Sunck is a good man %s - %s" % (os.getpid(), os.getppid()))
        sleep(1)
'''

# 父子进程的先后顺序
'''
def run():
    print("启动子进程")

    sleep(3)

    print("子进程结束")


if __name__ == "__main__":
    print("主（父）进程启动")

    p = Process(target=run)
    p.start()
    # 父进程的结束不能影响子进程，让父进程等待子进程结束，再执行父进程
    # join() 等待，子进程结束之后，父进程再结束
    p.join()

    print("父进程结束")
'''

# 全局变量再多进程中不能共享
'''
# 定义全局变量
number = 100


def run():
    print("子进程开始")
    # global 表示调用全局变量
    global number
    number += 1
    print("子进程结束 - %s" % number)


if __name__ == "__main__":
    print("父进程启动")

    p = Process(target=run)
    p.start()
    p.join()

    # 在子进程中修改全局变量对父进程中的全局变量没有影响
    # 每个进程都有自己的数据段、代码段、堆栈段，数据不共享
    # 在创建子进程时对全局变量做了一个备份，父进程中的与子进程中的number是完全不一样的两个变量
    print("父进程结束 - %d" % number)
'''

# 启动多线程

import random
import time
from multiprocessing import Pool

'''
def run(name):
    print("子进程%d启动 - %s" % (name, os.getpid()))

    start = time.time()
    time.sleep(random.choice([4, 5, 6]))
    end = time.time()

    print("子进程%d结束 - %s,耗时：%d" % (name, os.getpid(), (end - start)))


if __name__ == "__main__":
    print("父进程启动")

    # 创建多个进程
    # Pool进程池
    # 表示可以同时执行的进程数量
    # Pool默认大小是CPU核心数
    pp = Pool()

    for i in range(16):
        # 创建进程，放入进程池，统一管理
        pp.apply_async(run, args=(i,))

    # 在调用join之前必须先调用close，并且调用close之后，不能再继续添加新的进程了
    pp.close()
    # 进程池对象调用join，会等待进程池中所有的子进程结束完毕之后再去执行父进程
    pp.join()

    print("父进程结束")
'''

