from multiprocessing import Process
import os
import time


# 进程二次封装
class SunckProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print("子进程启动 - %s - %s" % (self.name, os.getpid()))

        # 子进程的功能
        time.sleep(3)

        print("子进程结束 - %s - %s" % (self.name, os.getpid()))


if __name__ == "__main__":
    print("父进程启动")

    # 创建子进程
    p = SunckProcess("text")
    # 自动调用p进程对象的run方法
    p.start()

    p.join()

    print("父进程结束")
