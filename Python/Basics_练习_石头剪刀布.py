#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2019/5/13 12:19
# @Author     : 张正
# @Email       : zhangzheng@email.com
# @Site         :
# @File          : Basics_04_运算符与表达式.py
# @Software  : PyCharm


import random


def rock_paper_scissors():
    """
    石头剪刀布游戏
    """

    while True:

        ran = random.randint(0, 2)

        number = int(input("请输入：剪刀(0)  石头(1)  布(2)："))

        if number not in range(0, 3):
            print(ran)
            print("输入错误，请重新输入！")

        elif (number == 0 and ran == 2) or (number == 1 and ran == 0) or (number == 2 and ran == 1):
            print(ran)
            print("恭喜你！取得胜利！！！")

        elif ran == number:
            print(ran)
            print("平手平手，我们继续！")

        else:
            print(ran)
            print("输了，洗洗手，我们继续")


rock_paper_scissors()
