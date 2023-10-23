'''
函数
'''


# 无参函数
def greet_user():
    # 显示简单问候语
    print('Hello Python')


greet_user()


# 带参函数
# 在函数greet_user()的定义中，变量username是一个形参 -- 函数完成其工作所需的一项信息。
# 在代码greet_user('zhangzheng')中，值‘zhangzheng’是一个实参。实参是调用函数时传递给函数的信息
def greet_user(username):
    print('Hello, ' + username.title())


greet_user('zhangzheng')


def describe_pet(animal_type, pet_name):
    # 显示宠物的信息
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')


# a未赋值，b赋值，表明为缺省参数，调动方法时，如为b赋值，就使用缺省参数。10
def text(a, b=10):
    sums = a + b
    print("sum = %d" % sums)


# 调用缺省参数
text(10)

# 不使用缺省参数
text(11, 22)


# 返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name


musician = get_formatted_name('jimi', 'hendrix')
print(musician.title())


# 返回字典
def build_person(first_name, last_name):
    # 返回一个字典，其中包含一个人的信息
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# 传递列表
def greet_users(names):
    for name in names:
        print(name.title())


username = ['hannah', 'ty', 'margot']
greet_users(username)


# 不定长参数,*args,代表一个元祖。如果方法有多个参数，元祖需要放在最后一个参数
def number(a, b, *args):
    print(a)
    print(b)
    print(args)

    sum = a + b

    for num in args:
        sum += num

    print(sum)


number(1, 2, 3, 4, 5, 6, 7, 8, 9)

# 导入模块。
# 正常情况下，模块导入是在代码的最上面
import Pizza

Pizza.make_pizza(16, 'pepperoni')
Pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as给模块指定别名
import Pizza as p

p.make_pizza(16, 'pepperoni')

# 导入指定的函数
# 导入模块中指定函数
from Pizza import make_pizza

make_pizza(16, 'pepperoni')

# 使用as给函数指定别名
from Pizza import make_pizza as mp

mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入模块中的所有函数
from Pizza import *

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 通用装饰器
def outer(func):
    def inner(*args,**kwargs):
        # 添加修改功能
        pass

    return inner()
