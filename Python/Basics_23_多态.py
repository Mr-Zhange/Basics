'''

多态：
    一种事物的多种形态

'''


# 动物类
class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + ": 吃")


# 猫类，继承动物类
class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)


# 鼠类，继承动物类
class Mouse(Animal):
    def __init__(self, name):
        super(Mouse, self).__init__(name)


tom = Cat("tom")
tom.eat()

jerry = Mouse("jerry")
jerry.eat()


# 人类
class Person():
    def feedAni(self, ani):
        print("给你食物")
        ani.eat()


p = Person()

p.feedAni(tom)

p.feedAni(jerry)
