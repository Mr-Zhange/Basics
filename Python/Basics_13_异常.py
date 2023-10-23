'''
异常

格式：
    try:
        语句，可能会出现错误的语句
    except 错误码 as e:
        出现错误执行的语句
        ...
    except 错误码 as e:
        出现错误执行的语句
        ...
    else:
        语句，当以上错误码都未捕获到的错误，就执行else里面的语句代码
        ...
'''

# 报错代码
# 没有进行异常操作，代码报错，程序停止运行
# print(5 / 0)

# ZeroDivisionError异常，Python无法按照你的要求做时，就会创建这种对象
try:
    # try代码块内放觉得会有问题的代码
    number = 4 / 2
except ZeroDivisionError:
    # 如果上方的代码出现异常，则运行以下代码，程序继续往下，避免程序崩溃
    print('代码运行错误')
else:
    # 如果try代码快运行成功，无报错。则输出else
    print(number)

print('-' * 30)

filename = 'alice.txt'

# FileNotFoundError异常，这是Python找不到要打开的文件时创建的异常。
try:
    # 让程序读取一个不存在的文件
    # 铁定报错
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print('没有找到' + filename + '文件。')

print('-' * 30)

# 基本常用异常代码这么写
try:
    print(4/0)
except :
    # 写入错误日志
    print("程序出现异常")

print('-' * 30)

# 基本常用异常代码这么写
try:
    print(4/0)
# 一个except捕获多种异常
except(ZeroDivisionError,FileNotFoundError) :
    # 写入错误日志
    print("程序出现异常")

print('-' * 30)

# BaseException 所有错误都继承自BaseException，可以捕获所有的异常错误
try:
    print(4/0)
except BaseException:
    # 写入错误日志
    print("程序出现异常")

print('-' * 30)

'''
异常

格式：
    try:
        语句，可能会出现错误的语句
    except 错误码 as e:
        出现错误执行的语句
        ...
    except 错误码 as e:
        出现错误执行的语句
        ...
    finaiiy:
        不论try语句是否有错误，都会执行finaiiy语句
        ...
'''

try:
    print(1/0)
except ZeroDivisionError:
    print("为0了")
finally:
    print("我会执行")

print('-' * 30)

try:
    print(1/1)
except ZeroDivisionError:
    print("为0了")
finally:
    print("我会执行")

print('-' * 30)

'''
断言
'''

def func(mun,div):
    assert (div != 0),"div不能为0"
    return mun / div


print(func(10,0))