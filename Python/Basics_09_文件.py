'''
文件
'''

"""
Python 中通过open() 函数打开文件

语法
open(name[, mode[, buffering]])

name        文件名，唯一强制参数
mode        模式， 参数的输入
buffering   缓冲

open() 函数能打开文件，文件不存在，也可以创建文件。如需要写入文件，需要添加参数

'r'     读模式
'w'     写模式,如果文件已存在则覆盖。如果文件不存在，创建新文件
'a'     追加模式,如果文件已存在则覆盖。如果文件不存在，创建新文件
'b'     二进制模式（可添加到其他模式中使用）
'+'     读/写模式（可添加到其他模式中使用）

write() 写入
read()  读取
close() 关闭

readline()  按行读取，读一行，返回字符串
readlines() 按行读取，返回列表

文件写入，可加入转义字符

文件定位读写
seek(offset, from)

offset:偏移量
from:方向
    0:表示文件开头
    1:表示当前位置
    2:表示文件末尾
"""

# 文件读取

# 关键字with在不再需要访问文件后将其关闭。在这个程序中，注意到我们调用了open()，但没有调用close()；
# 你也可以调用open()和close()来打开和关闭文件，但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭
# open()，如果省略了读写模式，open默认为读模式
with open('pi_digitx.txt') as file_object:
    contents = file_object.read()
    # print(contents)
    # 删除字符串末尾的空白
    # ???好像结尾的空白行没删除掉
    # print(contents.rstrip())

# 逐行读取

filename = 'pi_digitx.txt'
with open(filename) as file_object:
    for line in file_object.readlines():
        # print(line)
        print(line.rstrip())

print('-' * 30)

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print('π = ' + pi_string[:52] + '...')
print('π长度为：' + str(len(pi_string)))

print('-' * 30)

# 获得用户输入的出生年月日
# birthday = input('请输入出生年月日(900101):')
birthday = '900722'

# 判断年月日是否出现在pi出现
if birthday in pi_string:
    print('Yes')
else:
    print('No')

print('-' * 30)

# 文件写入
# Python只能将字符串写入到文本文件，要将数值数据存储到文本文件中，必须先使用函数str()将去转换为字符串格式

filename = 'programming.txt'

# 打开文件，写入模式，如果文件不存在，则创建一个
# w 写入模式，如果原文件存在内容，则覆盖原内容
with open(filename, 'w') as file_object:
    # 写入默认是不换行的，如需换行，需要添加换行符
    # file_object.write('I Love programming')
    file_object.write('I Love programming\n')
    file_object.write('I Love creating new games.\n')

# a 追加模式，不会覆盖文件内容，数据添加在原内容的末尾
with open(filename, 'a') as file_object:
    file_object.write('这是附加行1.\n')
    file_object.write('这是附加行2.\n')

# 练习题，制作文件备份

# 输入文件路径及文件名称
old_file_name = input("请输入文件名：")

# 创建备份文件
# fileNameBak = fileName + ".bak"  # 创建名称不符合规范
number = old_file_name.rfind(".")
new_file_name = old_file_name[0: number] + "[复件]" + old_file_name[number:]

# print(fileNameBak)

# 打开源文件
f_read = open(old_file_name, "r")

# 创建打开备份文件
f_write = open(new_file_name, "w")

"""
# 源文件写入备份文件
有漏洞的代码，如果遇到超大型文件，内存不够用，就会造成数据溢出，代码保存
wr.write(re.read())
"""

# 源文件写入备份文件（升级版）
while True:
    content = f_read.read(1024)  # 一次只读取1024字节

    print(content)

    if len(content) == 0:
        break

    f_write.write(content)

# 关闭备份文件
f_write.close()

# 关闭源文件
f_read.close()

"""
文件(夹)操作

导入包文件
import os

重命名
os.rename("原文件名","新文件名")

删除文件
os.remove("文件名")

创建文件夹
os.mkdir("文件夹名称")

获取当前目录
os.getcwd()

改变默认目录
os.chdir("../")

获取目录列表
os.listdie("./")

删除文件夹
os.rmdir("文件夹名称")
"""
