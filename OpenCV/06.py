# 图像基本操作

import numpy
import cv2

img = cv2.imread("./img/2021-01-17_23-44-13.mkv_20210118_000643.209.jpg")

# 访问和修改像素值

# 可以通过行和列坐标来访问像素值。对于 BGR 图像，它返回一个由蓝色、绿色和红色值组成的数组。
# 对于灰度图像，只返回相应的灰度。
px = img[100, 100]
print(px)

# 仅访问蓝色像素
blue = img[100, 100, 0]
print(blue)

# 修改像素值
img[100, 100] = [255, 255, 255]
print(img[100, 100])

# Numpy是用于快速数组计算的优化库。因此，简单地访问每个像素值并对其进行修改将非常缓慢，因此不建议使用。

# 访问RED值
print(img.item(10, 10, 2))

# 修改RED值
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

# 访问图像属性

# 图像属性包括行数，列数和通道数，图像数据类型，像素数等。
# 图像的形状可通过 img.shape 访问。它返回行，列和通道数的元组（如果图像是彩色的）
# 如果图像是灰度的，则返回的元组仅包含行数和列数，因此这是检查加载的图像是灰度还是彩色的好方法。
print(img.shape)

# 像素总数
print(img.size)

# 图像数据类型
print(img.dtype)

# 复制区域
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# cv2.imshow("img", img)
# cv2.waitKey(0)

# 拆分和合并图像通道

# 有时需要分别处理图像的B，G，R通道。在这种情况下，你需要将BGR图像拆分为单个通道。
# 在其他情况下，你可能需要将这些单独的频道加入BGR图片。
b = img[:, :, 0]
# cv2.imshow("img", b)

# 将所有红色像素都设置为零，则无需先拆分通道。numpy索引更快
img[:, :, 2] = 0
# cv2.imshow("img2", img)
# cv2.waitKey(0)
