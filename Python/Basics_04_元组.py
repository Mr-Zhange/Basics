'''
元组
'''

# 定义一个元组
dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])
print("*" * 30)

# dimensions[0]=250
'''
此处报错。
Python将不能修改的值称为比可变，而不可变的列表称为元组
元组里的值，定义之后将不可修改
Traceback (most recent call last):
  File "E:/Python/Basics/Basics_03_元组.py", line 11, in <module>
    dimensions[0]=250
TypeError: 'tuple' object does not support item assignment
'''

# 遍历元组中所有的值
for dimension in dimensions:
    print(dimension)
print("*" * 30)

# 这是个坑
# 修改元组变量
# 虽然元组的值不可修改，但是可重新定义...
dimensions = (400, 400)
print(dimensions)
