'''
变量和简单数据类型

'''

# 导入,数学相关库
import math
# 随机数库
import random

print("Hello Word")
print("你好！世界！")

print("-" * 30)

'''
    占位符     转换
    %c        字符
    %s        通过str()字符串转换来格式化
    %i        有符号十进制整数
    %d        有符号十进制整数
    %u        无符号十进制整数
    %o        八进制整数
    %x        十六进制整数(小写字母)
    %X        十六进制整数(大写整数)
    %e        索引符号(小写‘e’)
    %E        索引符号(大写‘E’)
    %f        浮点实数
    %g        %f和%e的简写
    %G        %f和%E的简写
'''

# 变量

'''
    变量名 命名规则
        1、变量名只能包含字母、数字、下划线。变量名可以字母或下划线大头，但不能以数字打头
        2、变量名不能包含空格，但可以使用下划线来分割其中的单词
        3、不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词
            查看Python关键字
            import keyword
            print(keyword.kwlist)
        4、变量名应既简短又具有描述性
        5、慎用小写字母I和大写字母O，因为它们可能被人看错成数字1和0
'''

print("变量：")

# type() 输出变量的数据类型

_number = 100
print("_number = %d" % _number)
print(type(_number))
print("*" * 30)

_message = "Hello Word"
print("_message = %s" % _message)
print(type(_message))
print("*" * 30)

_bool = True
print("_bool = %s" % _bool)
print(type(_bool))
print("*" * 30)

_list = [1, 2, 3, 4, 5]
print("_list = %s" % _list)
print(type(_list))
print("*" * 30)

_tup = (1, 2, 3, 4, 5)
print("_tup = ", _tup)
print(type(_tup))
print("*" * 30)

_dict = {"Name": "ZhangSan",
         "Age": 18}
print("_dict = %s" % _dict)
print(type(_dict))
print("-" * 30)

# 返回数字的绝对值 abs
Number = 10
print(abs(Number))
print("*" * 30)

# 返回给定参数的最大值 max
print(max(9, 3, 46, 1884, 35, 32843, 321564, 3212))
print("*" * 30)

# 返回给定参数的最小值 min
print(min(9, 3, 46, 1884, 35, 32843, 321564, 3212))
print("*" * 30)

# 求X的Y次方 pow
print(pow(2, 5))
print("*" * 30)

# 四舍五入,或取小数位 round
print(round(3.456))
print(round(3.556))
print(round(3.456, 1))
print(round(3.456, 2))
print("*" * 30)

# 向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))
print("*" * 30)

# 向下取整
print(math.floor(18.1))
print(math.floor(18.9))
print("*" * 30)

# 返回整数部分与小数部分
print(math.modf(22.3))
print("*" * 30)

# 开方
print(math.sqrt(16))
print("*" * 30)

# 随机数

# 随机输出列表中的数值
print(random.choice([1, 2, 3, 9, 5, 4, 6, 7, 4, 4, 5, 6, 7]))
print("*" * 30)

# 产生一个1-100之间的随机数
rand = random.choice(range(100)) + 1
print(rand)
print("-" * 30)

# 字符串
# 字符串就是一系列字符。在Python中，用引号括起来的都是字符串，其中的引号可以是单引号，也可以是双引号。
'This is a string'
"This is also a string"

# format() 字符串格式化符，通过预留的 {} 占位符，向占位符添加字符串。类似填空题
_name = "{} San".format("Zhang")
print("format()方法：", end="")
print(_name)
print("*" * 30)

myStr = "    Hello \n Worle    "

# .find()   根据字符，找到返回下标，找不到返回-1
# .rfind()  从左边开始查找
print(myStr.find("H"))
print("*" * 30)

# .index()  根据字符，找到返回下标，找不到就报错
# .rindex() 从左边开始查找
print(myStr.index("e"))
print("*" * 30)

# .count()  查找字符出现的次数
print(myStr.count("o"))
print("*" * 30)

# .replace() 替换
# .replace("原字符", "替换的字符", 替换的次数(可选))
print(myStr.replace("Worle", "Word"))
print("*" * 30)

# .split()  切割，返回列表
print(myStr.split(" "))
print("*" * 30)

# .splitlines() 根据换行符切割
print(myStr.splitlines())
print("*" * 30)

# .partition()  分割，返回元祖
# .rpartition() 从右边开始查找
print(myStr.partition("o"))
print("*" * 30)

# .capitalize() 字符串首字母大写
print(myStr.capitalize())
print("*" * 30)

# .title()  字符串每个单词的首字母大写
print(myStr.title())
print("*" * 30)

# .lower()  全部小写
print(myStr.lower())
print("*" * 30)

# .upper()  全部大写
print(myStr.upper())
print("*" * 30)

# .startswith() 判断以什么开头
print(myStr.startswith("W"))
print("*" * 30)

# .endswith()   判断以什么结尾
print(myStr.endswith("e"))
print("*" * 30)

'''
# .rjust()  右对齐
print(myStr.rjust())

# .ljust()  左对其
print(myStr)

# .center() 剧中
print(myStr.center())
'''

# .rstrip() 去右空格
print(myStr.rstrip())
print("*" * 30)

# .lstrip() 去左空格
print(myStr.lstrip())
print("*" * 30)

# .strip()  去左右空格
print(myStr.strip())
print("*" * 30)

# .isalnum()    判断字符串是不是纯字母
print(myStr.isalnum())
print("*" * 30)

# .isdigit()    判断字符串是不是纯数字
print(myStr.isdigit())
print("*" * 30)

# .isalnum()    判断字符串是不是字符与数字的组合
print(myStr.isalnum())
print("*" * 30)

names = ["张三", "李四", "王五"]

a = "——"

# .join() 通过一个字符把列表组合成成字符串
print(a.join(names))

# 查找替换，讲语句中的1，替换成2
myStr.replace('1', '2')


'''
作用域：变量可以使用的范围

程序的变量并不是在所有位置都能使用的，访问的权限决定于变量的在哪里赋值的

作用域：
    局部作用据
    全局作用域
    内建作用据
'''

# 定义一个全局变量
wendu = 33


def get_wendu():
    # 定义的局部变量
    # wendu = 30

    """
    如果：全局变量与局部变量重名，在方法中调用时，默认调用局部变量
    """

    # 使用global用来声明一个变量，那么就是对全局变量来进行修改
    global wendu

    wendu = 40

    print(wendu)


get_wendu()