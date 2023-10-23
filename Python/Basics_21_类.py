'''
创建类
类：一种数据类型，本身并不占内存空间，跟所学过的number,string,boolean等类似。
用类创建实例化对象都（变量），对象占内存空间

格式：
class 类名(父类列表):
    属性
    行为（方法）
'''


# 定义一个类
class Dog():
    '''一次模拟小狗的简单尝试'''

    # self 谁调用这个类，self就表示谁

    # 初始化属性
    # 属性可以给定默认值
    def __init__(self, name='gg', age=3):
        self.name = name
        self.age = age

    # 释放对象时，执行的函数
    # 自动执行
    def __del__(self):
        print("我是析构函数")

    def __str__(self):
        print(self.name,self.age)

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title() + ' rolled over!')


# 根据类，创建示例
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 无参创建类
my_dog = Dog()
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()


# 创建一个汽车类
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # self.odometer_reading = mileage
        # 判断：新值是否比原值大，条件成立才写入
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        print("50")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改类属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 通过方法修改属性的值
my_new_car.update_odometer(24)
my_new_car.read_odometer()


class A:
    def __init__(self):
        self.num1 = 100
        # 访问权限，如果要让内部属性不被外部直接访问，就在变量名前加两个下划线
        self.__num2 = 200

    def text1(self):
        print("=====test1=====")

    # 私有方法，不让外部调用
    def __test2(self):
        print("=====test2=====")

    def test3(self):
        self.__test2()
        print(self.__num2)

    # 通过@property实现有访问权限的属性
    @property
    def num2(self):
        return self.__num2
    # 通过.setter 修改有访问权限的属性
    @num2.setter
    def num2(self,num2):
        if num2 < 0:
            num2 = 0
        self.__num2 = num2


class B(A):
    pass


b = B()
print(b.num1)
b.text1()
b.test3()


b.num2 = 10000
print(b.num2)



# 手动释放对象，后面将不能再调用
# del b
# b.text1()

"""
如果调用的是继承的父类中的共有方法
可以在这个共有方法中访问父类中的私有属性和私有方法
但是，如果在子类中实现了一个共有方法，那么
这个方法是不能够调用继承的父类中的私有方法和私有属性
"""
