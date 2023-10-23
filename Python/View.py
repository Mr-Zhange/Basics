'''
界面
类型：View
属性：
行为：管理员界面、管理员登录、系统功能界面
'''

import time


class View(object):
    admin = "1"
    passwd = "1"

    # 管理员界面
    def printAdminView(self):
        print("****************************************************************")
        print("*                                                              *")
        print("*                     欢迎登录XX银行系统                        *")
        print("*                                                              *")
        print("****************************************************************")

        inputAdmin = input("请输入管理员帐号：")

        # 判断账户正确
        if self.admin != inputAdmin:
            print("帐号输入有误，请重启程序！")
            return -1

        inputPasswd = input("请输入密码：")

        # 判断密码正确
        if self.passwd != inputPasswd:
            print("密码错误，请重启程序")
            return -1

        print("登录成功！请稍等......")

        time.sleep(2)

        return 0

    # 功能界面
    def printFunctionView(self):
        print("****************************************************************")
        print("*                                                              *")
        print("*                     欢迎登录XX银行系统                        *")
        print("*                                                              *")
        print("*       开户(1)       查询(2)       取款(3)       存款(4)       *")
        print("*       转账(5)       改密(6)       锁定(7)       解锁(8)       *")
        print("*       补卡(9)       销户(0)                     退出(q)       *")
        print("*                                                              *")
        print("****************************************************************")

    # 退出提示
    def errorQuit(self):
        print("输入错误，请重新输入。")

    def quit(self):
        print("程序退出。")
