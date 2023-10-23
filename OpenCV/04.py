# 读取视频文件

import cv2

cap = cv2.VideoCapture("D:/Cache/OBS/2021-01-17_23-49-03.mkv")

while cap.isOpened():
    ret, frame = cap.read()

    #  如果正确读取帧，ret为True
    if not ret:
        print("视频播放结束")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video", gray)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
