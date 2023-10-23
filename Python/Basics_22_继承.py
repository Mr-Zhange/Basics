'''
继承
'''

# 导入Car类
from Basics_21_类 import Car


# 创建子类，继承Car，父类
class ElectricCar(Car):

    def __init__(self, make, model, year):
        # 初始化父类的属性
        super().__init__(make, model, year)
        # 初始化电动车的独有方法
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    # 重写父类方法
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
print(my_tesla.describe_battery())
print(my_tesla.fill_gas_tank())
