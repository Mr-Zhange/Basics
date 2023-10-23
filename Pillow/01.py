from PIL import Image

# 从文件加载图像
img = Image.open("./img/2021-01-17_23-44-13.mkv_20210118_000643.709.jpg")

# 此函数将返回 Image 对象。
print(img.format, img.size, img.mode)
'''
format  图片格式
size    图片宽高,以像素为单位
mode    图片模式,通常有:
        常用模式有灰度图像的“L”（亮度）、真彩色图像的“RGB”和预压图像的“CMYK”
'''

# 打开图片,调用电脑的程序打开
img.show()
