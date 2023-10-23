from User import *
from Card import *


class ATM:
    def __init__(self):
        self.allUsers = {}

    # 开户
    def createUser(self):
        # 目标：向用户字典中添加一对键值对（卡号、用户）
        name = input('请输入您的姓名：')
        idCard = input('请输入您的身份证号码：')
        phone = input('请输入您的电话号码：')

        prestoreMoney = int(input('请输入预存款金额：'))
        if prestoreMoney < 0:
            print("预存款输入有误！开户失败......")

    # 查询
    def searchUserInfo(self):
        pass

    # 取款
    def getMoney(self):
        pass

    # 存款
    def saveMoney(self):
        pass

    # 转账
    def transferMoney(self):
        pass

    # 改密
    def changePasswd(self):
        pass

    # 锁定
    def lockUser(self):
        pass

    # 解锁
    def unlockUser(self):
        pass

    # 补卡
    def newCard(self):
        pass

    # 销户
    def killUser(self):
        pass
