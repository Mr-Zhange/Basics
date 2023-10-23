'''
UTC(世界协调时间)：格林尼治天文时间，世界标准时间，在中国来说就是UTC+8

DST(夏令时)：是一种节约能源而认为规定时间制度，在夏季调快1小时

时间的表示形式
1、时间戳
    以整型或浮点型表示时间的一个以秒为单位的时间间隔。这个时间间隔的基准值是从1970年1月1日开始算起
2、元组
    一种Python的数据结构表示，这个元组有9个整型内容
    year    年
    month   月
    day     日
    hours   时
    minutes 分
    seconds 秒
    weekday
    Julia day
    flag （1 或 -1 或 0）
3、格式化字符串
'''

import time

# 返回当前时间的时间戳，浮点数，不需要参数
c = time.time()
print(c)

# 将时间戳转为：格林尼治天文时间，元组
t = time.gmtime(c)
print(t)

# 将时间戳转为：本地时间，元组
b = time.localtime(c)
print(b)

# 将本地时间转为：时间戳
m = time.mktime(b)
print(m)

# 将本地时间元组转为：字符串
s = time.asctime(b)
print(s)

# 将时间戳转为：字符串
p = time.ctime(c)
print(p)

# 将时间元组转为：按照自定义格式。时间元组可不写，那就是获得当前时间
q = time.strftime("%Y-%m-%d %H:%m:%S", b)
print(q)

# 延迟时间,单位：秒
time.sleep(1)

'''
###
Python 3.8版本开始已经启用该函数

# 返回当前程序的CPU执行时间
# Linux始终返回全部的运行时间
# windows从第二次开始，都是以第一个调用的时间戳作为基数
# time.clock()

y = time.clock()
print(y)

time.sleep(1)

y2 = time.clock()

print(y2)

'''

# 类似上方的函数，不过不需要再执行两次
y = time.process_time()

print(y)

time.sleep(1)

y2 = time.process_time()
print(y2)

'''
datetime:time 升级版
基于time封装
datetime    同时有时间和日期
timedelta   主要用于计算时间的跨度
tzinfo      时区相关
time        只关注时间
date        只关注日期
'''

import datetime

# 获取当前时间
d1 = datetime.datetime.now()
print(d1)

# 获取指定时间
d2 = datetime.datetime(1990, 9, 10, 12, 12, 12, 123456)
print(d2)

# 讲时间转为字符串
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)

# 将格式化转为datetime对象
# 注意：转换的格式要与字符串一致
d4 = datetime.datetime.strptime(d3, "%Y-%m-%d %X")
print(d4)

# 时间间隔
d5 = datetime.datetime(1990, 9, 10, 12, 12, 12, 123456)
d6 = datetime.datetime.now()

d7 = d6 - d5
print(d7)
print(d7.days)
print(d7.seconds)

'''
日历模块
'''
import calendar

# 获得月历表
print(calendar.month(2217, 7))

# 获得某年的日历
print(calendar.calendar(2217))

# 判断闰年
print(calendar.isleap(2008))

# 获得某年某月的第一天和有多少天
print(calendar.monthrange(2217, 7))

# 返回某月以，每周为元素的列表
print(calendar.monthcalendar(2217, 7))
