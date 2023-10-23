'''
1、使用标准库模块

标准库模块：time datetime os ......
'''

'''
2、使用自定义模块
使用imoprt导入一个自写的模块
'''
# 引入一个自定义模块
import sunck

sunck.sayNice()
sunck.sayGood()

# 从一个模块中导入一个指定的部分内容
# 格式：from 模块名 import 指定内容名称 as 自定义名称
from sunck import sayNice as sn

sn()

# 把一个模块中的所有内容全部导入
# 格式：from 模块名 import *
from sunck import *

sayNice()
sayGood()

'''

包

为了解决模块命名的冲突，引入了按目录来组织的模块的方法，称为“包”

引入了包以后，只要顶层的包不予其他人发生冲突，那么模块都不会与别人的发生冲突

目录只有包含了一个“__init__.py”的文件，才会被认作是包

一个包目录下可以有多个文件
'''

import Text.sunck as ts

ts.sayGood()
ts.sayNice()

'''
3、第三方模块
    Pillow  非常强大的处理图像的工具库
'''

# 引入了三方库
from PIL import Image

# 打开图片
im = Image.open("./Image/夜空下4k壁纸_彼岸图网.jpg")

# 查看图片信息
print(im.format, im.size, im.mode)

# 设置图片大小
im.thumbnail((150, 100))

# 保存成新的图片
im.save("./Image/temp.jpg","JPEG")

