# 使用Matplotlib显示图片
# OpenCV 加载的彩色图像处于BGR模式,但是但是Matplotlib以RGB模式显示。
# 因此，如果使用OpenCV读取彩色图像，则Matplotlib中将无法正确显示彩色图像。

import cv2
from matplotlib import pyplot

small = cv2.imread("./img/2021-01-17_23-44-13.mkv_20210118_000643.209.jpg", 0)
pyplot.imshow(small, cmap='gray', interpolation='bicubic')

# 隐藏 x 轴和 y 轴上的刻度值
pyplot.xticks([]), pyplot.yticks([])

pyplot.show()
