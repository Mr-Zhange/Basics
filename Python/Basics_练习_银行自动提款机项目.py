'''
人
类名：Person
属性：姓名、身份证ID、电话号码、卡
行为：开户、查询、取款、存储、转账、改密、锁定、解锁、补卡、销户

卡
类名：Card
属性：卡号、密码、余额

提款机
类名：ATM
属性：
行为：开户、查询、取款、存储、转账、改密、锁定、解锁、补卡、销户

界面
类型：View
属性：
行为：管理员界面、管理员登录、系统功能界面
'''

import time
from View import View
from ATM import ATM


def main():

    # 管理员开机界面
    if View.printAdminView(View) == 0:

        # 死循环，等待用户操作
        while True:
            View.printFunctionView(View)

            option = input("请输入您的操作：")

            if option == '1':
                # 开户
                ATM.createUser(ATM)

            elif  option == '2':
                # 查询
                pass

            elif option == '3':
                # 取款
                pass

            elif option == '4':
                # 存款
                pass

            elif option == '5':
                # 转账
                pass

            elif option == '6':
                # 改密
                pass

            elif option == '7':
                # 锁定
                pass

            elif option == '8':
                # 解锁
                pass

            elif option == '9':
                # 补卡
                pass

            elif option == '0':
                # 销户
                pass

            elif option == 'q':
                # 退出程序
                View.quit(View)
                break

            else:
                View.errorQuit(View)



            time.sleep(1)


if __name__ == "__main__":
    main()
