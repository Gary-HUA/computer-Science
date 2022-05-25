import pytesseract as pyt
import cv2 as cv
from PIL import Image
"""
1: 判断文本朝向 进行图像预处理 做角度矫正和去噪
出现预处理很重要 图像可能是翻转, 有倾斜角的  需要正放.
"""
# OCR - tesseract - test
# import pytesseract as pyt
# import cv2 as cv
# from PIL import Image
img = cv.imread("E:/python_OpenCV lib/OCR_R.jpg")
test = pyt.image_to_string(Image.fromarray(img))
print(test)


