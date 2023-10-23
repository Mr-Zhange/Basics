# 一个.py文件就是一个模块

'''
__name__ 属性
模块就是一个可执行的.py文件，一个模块被另一个程序引用。
我们不想让模块中的某些代码执行，可以用 __name__ 属性来使程序仅调用模块中的一部分

每一个模块都有一个 __name__ 属性，当其值等于 __main__时，表示该模块自身在执行.否则表示被引入到了其他文件
'''

# 当前文件如果为程序的入口文件，则__name__属性的值为"__main__"
if __name__ == "__main__":

    print(__name__)

    print("这是Text/sunck.py文件")

else:

    print(__name__)

    def sayGood():
        print("sunck is a very Good man!")


    def sayNice():
        print("sunck is a very Nice man!")


import time

print(time.process_time())

