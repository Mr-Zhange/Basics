from types import MethodType


# 创建一个空类
class Person():
    # 限制添加属性,(只有括号里的属性才能动态添加. )
    __slots__ = ("name", "speak")


# 实例化
s = Person()

# 动态添加属性
s.name = "tom"

print(s.name)


# 动态要添加方法
def say(self):
    print("My Name is :", self.name)


# 动态添加方法
s.speak = MethodType(say, s)
