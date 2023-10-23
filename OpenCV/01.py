# 图片的加载,修改,保存

import cv2

# imread 读入图片

# 指定了我们想要的图像的方式
# IMREAD_COLOR 加载彩色图像.任何图像的透明度都会被忽视.默认项
# IMREAD_GRAYSCALE 以灰度模式加载图片
# IMREAD_UNCHANGED 加载图像,包括alpha通道
# 还可以简单的传递整数1, 0 或 -1.

# 即使图像路径错误,也不会报错,但是print 会给出None
small = cv2.imread("./img/2021-01-17_23-44-13.mkv_20210118_000643.209.jpg", cv2.IMREAD_UNCHANGED)

# 以窗口的形式显示图片,参数1:窗口标题,参数2:要显示的图片
# 窗口自动适应图像尺寸
cv2.imshow("image", small)

# 保存图片,参数1:保存图片路径及名称,参数2:要保存的图片
cv2.imwrite("./img/1.jpg", small)

# 等待用户按下一个键（否则程序会结束太快）
cv2.waitKey(0)
