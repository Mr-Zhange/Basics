# 读取视频，显示视频
# cv.VideoCapture()，cv.VideoWriter()

import cv2

# 创建一个VideoCapture对象,它的蚕食可以是设备索引或者视频文件的名称
# 视频索引就是指向哪个摄像头的数字
cap = cv2.VideoCapture(0)

'''
有时,cap可能尚未初始化捕获.在这种情况下,此代码显示错误.
可以通过cap.isOpened()方法检查是否已经初始化.如果是True.
否则使用cap.open()打开它

还可以使用 cap.get(propId) 方法访问该视频的某些功能，其中propId是0到18之间的一个数字。
每个数字表示视频的属性（如果适用于该视频），并且可以显示完整的详细信息在这里看到：cv::VideoCapture::get()。
其中一些值可以使用 cap.set(propId，value) 进行修改。 value是你想要的新值。

例如，我可以通过 cap.get(cv.CAP_PROP_FRAME_WIDTH) 和 cap.get(cv.CAP_PROP_FRAME_HEIGHT)
检查框架的宽度和高度。默认情况下，它的分辨率为640x480。但我想将其修改为320x240。
只需使用和即可。 ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320) and ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240) .

'''
if not cap.isOpened():
    print("没有发现摄像头!")
    exit()

while True:
    # 逐帧捕获
    # 返回布尔值,如果正确读取了帧,它将为True.因此,可以通过检车次返回值来检查视频的结尾
    ret, frame = cap.read()

    # 如果正确读取帧,ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # 读取视频帧
    gray = cv2.cvtColor(frame, cv2.IMREAD_COLOR)

    # 显示视频帧
    cv2.imshow("Video", gray)

    # 手动死循环,获取视频帧,直到用户按下q
    if cv2.waitKey(1) == ord('q'):
        break

# 完成所有操作后,释放捕获器
cap.release()
cv2.destroyAllWindows()
