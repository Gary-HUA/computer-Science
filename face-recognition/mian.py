# face recognition in video
"""face model ,
gray scale,
detecting face ,
mark face"""
# def video_mirror_output(video):
#     new_img = np.zeros_like(video)
#     h, w = video.shape[0], video.shape[1]
#     for row in range(h):
#         for i in range(w):
#             new_img[row, i] = video[row, w-i-1]
#     return new_img

# modify intensity of image
# rows, cols, channels = frame.shape
# dst = frame.copy()
# a = 0.5
# b = 80
# for i in range(rows):
#     for j in range(cols):
#         for c in range(3):
#             color = frame[i, j][c] * a + b
#             if color > 255:
#                 dst[i, j][c] = 255
#             elif color < 0:
#                 dst[i, j][c] = 0
import cv2 as cv
import numpy as np


def Contrast_and_Brightness(alpha, beta, img):
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + (1-alpha) * blank + beta
    dst = cv.addWeighted(img, alpha, blank, 1-alpha, beta)
    return dst


img = cv.imread("E:/python_OpenCV lib/face.jpg")
# face model
face = cv.CascadeClassifier("D:/python lib/haarcascade_frontalface_alt.xml")
# video capture
capture = cv.VideoCapture(0)
if capture.isOpened():  # 判断是否正常打开
    opened, frame = capture.read()  # 读取源  得到两个返回值 bool 和帧数
    frame = cv.flip(frame, 1)  # 颠倒摄像头镜像问题
else:
    opened = False
while open:
    ret, frame = capture.read()
    if frame is None:
        break
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # gray scale 灰度图 提高检测效率
        frame = Contrast_and_Brightness(1.8, 1.3, frame)
        faces = face.detectMultiScale(gray)  # detecting face
        # make mark on face
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # show result
        cv.imshow("result", frame)
        if cv.waitKey(50) & 0xFF == 27:
            break
capture.release()
cv.destroyAllWindows()


