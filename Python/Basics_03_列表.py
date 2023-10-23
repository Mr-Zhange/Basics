'''
列表
'''

# 定义一个列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素
print(bicycles[2])
print("*" * 30)

# 访问列表元素加首字母大写
print(bicycles[2].title())
print("*" * 30)

# 访问列表最后一个元素
print(bicycles[-1])
print("*" * 30)

# 修改表元素
bicycles[0] = 'ducati'
print(bicycles)
print("*" * 30)

# 列表中添加元素
# 添加在列表的末尾
bicycles.append('New_trek')
print(bicycles)

# 在列表的指定位置添加元素
bicycles.insert(0, 'New')
print(bicycles)
print("*" * 30)

# 删除列表元素
# 根据元素下标删除
del bicycles[0]
print(bicycles)

# 删除(弹出)列表末尾的元素
# 被弹出的元素
# 可被访问
popped = bicycles.pop()
print(bicycles)
print(popped)

# 根据下标删除(弹出)元素
popped = bicycles.pop(2)
print(bicycles)
print(popped)
print("*" * 30)

# 根据值删除元素
# remove()只删除第一个指定的值，如果要删除的值可能在列表中出现多次，就需要循环判断来删除所有指定的值
bicycles.remove('cannondale')
print(bicycles)

# 清空列表
# bicycles.clear()

# 获取元素重复次数
print(bicycles.count('redline'))

print("*" * 30)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# 对列表进行永久性排序
cars.sort()
print(cars)

# 倒序排序
cars.sort(reverse=True)
print(cars)
print("*" * 30)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# 临时排序
print(sorted(cars))
print(cars)

# 确认列表长度
print(len(bicycles))
print("*" * 30)

magicians = ['alice', 'david', 'carolina']

# 遍历列表
for magician in magicians:
    print(magician)
print("*" * 30)

# 创建数值列表
# 使用函数range(1, 5)，创建1 - 5，不包含5的数字
# 使用range()函数时，可指定步长
for value in range(1, 5):
    print(value)

# 使用list()将range()的结果直接转换为列表
number = list(range(1, 6))
print(number)

# 步长
# range(2, 11, 2)，从2开始，然后不断加2，直到达到或超过终值11
number = list(range(2, 11, 2))
print(number)
print("*" * 30)

# 列表解析
# 定义一个列表名，然后指定左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为value**2,它计算的平方值。接下来，
# 编写一个for循环，用于给表达式赋值，再加上一个有方括号。
squares = [value ** 2 for value in range(1, 11)]
print(squares)
print("*" * 30)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)

# 切片
# 指定 0 - 3，不包含3之间的索引
print(players[0:3])

print(players[1:4])

# 如果没有指定第一个所以，Python将从列表开头开始
print(players[:4])

# 要切片到列表末尾，也可以使用类似方法，不指定结束索引
print(players[2:])

# 负索引返回离列表末尾相应距离的元素，倒数几个。-2就是返回末尾的两个元素
print(players[-2:])
print("*" * 30)

# 循环遍历切片
# 设定遍历列表的范围，循环输出
for player in players[:3]:
    print(player)
print("*" * 30)

# 复制列表
# friend_foods = my_foods[:] 不等于 friend_foods = my_foods
# friend_foods = my_foods[:] 在内存里创建了新的堆栈，并复制给了friend_foods
# friend_foods = my_foods 只是把内存地址给了friend_foods，一边变量改变了数据，另一个变量也会改变数据
my_foods = ['pizza', 'falafel', 'carrot', 'cake']
friend_foods = my_foods[:]
