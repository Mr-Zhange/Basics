'''
if 语句
'''

cars = ['bmw', 'audi', 'toyota', 'subaru']

'''
if 用来完成判断

if 条件:
    条件成立的时候，做的事情

    比较运算符
    >=  大于等于
    <=  小于等于
    ==  等于
    !=  不等于

    逻辑运算符
    or      或者
    and     和
    not     取反
'''

'''
判断
    如果汽车名是‘audi'，应以全大写的方式打印
    其他汽车名，以首字母大写方式打印
'''
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())

age = 19

if age >= 18:
    print("可以去网吧嗨皮了")
else:
    print("回家睡大觉吧")

"""
功能升级版

if 条件:
    条件成立的时候，做的事情
else:
    条件不成立的时候，做的事情
"""

# int(input("请输入你的年龄：")) 数据类型转换 Str -> Int
age = int(input("请输入你的年龄："))

if age >= 18:
    print("你可以去网吧嗨皮了！")
else:
    print("你还是回家睡大觉吧！")

# 练习：输出打印星期，输入1：打印星期一 ... 输入7：打印星期天

while True:  # 升级版，如果用户输入错误，则重新输入，输入正确为止

    number = int(input("请输入数字(1 - 7):"))

    if number == 1:
        print("星期一")
        break
    elif number == 2:
        print("星期二")
        break
    elif number == 3:
        print("星期三")
        break
    elif number == 4:
        print("星期四")
        break
    elif number == 5:
        print("星期五")
        break
    elif number == 6:
        print("星期六")
        break
    elif number == 7:
        print("星期天")
        break
    else:
        print("输入错误。请重新输入！")
