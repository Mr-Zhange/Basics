import os
import time

import win32con

'''
由于版本原因，win32gui目前只支持到python3.7
目前安装pypiwin32,支持导入win32gui
'''
import win32gui

# 获取窗口句柄句,参数（窗体类名,窗口标题）
微信 = win32gui.FindWindow("TrayNotifyWnd", "微信")

print(微信)

# 隐藏窗口
win32gui.ShowWindow(微信, win32con.SW_HIDE)

# 延时任务，秒
time.sleep(2)

# 显示窗体
win32gui.ShowWindow(微信, win32con.SW_SHOW)