import cv2

src = cv2.imread("D:\\CC\\image\\scale_match.bmp", 1)
print(src.shape)
Img = 255 - src
print(Img.shape)
cv2.imshow("Img", Img)
cv2.imshow("src", src)
cv2.waitKey(0)
cv2.imwrite("D:\\CC\\image\\scale_match.bmp", Img)
