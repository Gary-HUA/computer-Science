### 第一讲： 图像视频的基本操作

~~~python
import cv2 as cv
# 定义一个方法 用于获取图片的格式等基本信息

def image_info(img):
    print(type(img))  # <class 'numpy.ndarray'>
    print(img.shape)  # (256, 256, 3)  大小和通道（opencv 通道为	BGR）
    print(img.size)  # 196608
    print(img.dtype)  # uint8

src = cv.imread("E:/python_OpenCV lib/lena.jpg")  # 加载一张图片,第二个参数定义色彩(cv.IMREAD_COLOR) CV.IMREAD_GRAYSCALE
cv.imwrite("E:/python_OpenCV lib/lena_gray.jpg", src)  # 保存图像信息,第一个参数是位置,第二个参数是源文件
cv.imshow("image", src)  # 显示一张图片
image_info(src)
cv.waitKey(0)  # 等待窗口,任意键关闭
cv.destroyAllWindows()  # 销毁窗口

~~~

#### 图像的读入,显示,调整窗口大小，图像写入。

~~~python
import numpy as np
import cv2 as cv
# load  an color image in grayscale;
img = cv.imread("E:/python_OpenCV lib/lena.jpg", 0)  # 图像的读入 
cv.nameWindow("image",cv.WINDOW_NORMAL/AUTOSIZE)
cv.imshow("image", img)  # 图像的显示
k = cv.waitKey(0)  # 键盘绑定函数，等待是否有键盘输入
# 对退出条件进行判断 如果是S 就是保存当前图像
if k == 27:  # 27 is  exit 
    cv.destroyAllWindows()  # 删除我们创建任意的窗口
elif k == ord("s"):  # wait for S to save and exit;
    cv.imwrite("E:/python_OpenCV lib/ord_s.jpg", img)
    cv.destroyAllWindows()
~~~

#### 使用 Matplotlib 

~~~python
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("E:/python_OpenCV lib/lena.jpg",0)   # 读入图像
plt.imshow(img, cmap="gray", interpolation="bicubic") # 显示图像，
plt.xticks([]), plt.yticks([])  
plt.show()
~~~



#### 使用opencv 画几何图像

~~~python
# Drawing Functions in OpenCV
#  You will learn these functions : cv2.line(), cv2.circle() , cv2.rectangle(), cv2.ellipse(), cv2.putText() etc.
import cv2 as cv
import numpy as np
# draw a plant in zero
img = np.zeros((512, 512, 3), np.uint8)
# draw line
img = cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)  # origin img, star_pos, end_pos, line_pixel
# draw rectangle
img = cv.rectangle(img, (0, 0), (200, 200), (0, 255, 0), 5)
# draw circle
img = cv.circle(img, (200, 200), 50, (0, 0, 255), 5)
 # draw ellipse
img = cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 200, -1)
# draw polygon(多边形)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv.polylines(img, [pts], True, (0, 255, 255))
cv.imshow("res", img)
cv.waitKey(0)
cv.destroyAllWindows()
~~~

#### 添加文本到图像

~~~python
# 画上文字
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = np.zeros((512, 512, 3), np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "gary_H", (0, int(512/2)), font, 4, (0, 0, 255), 2, cv.LINE_AA)
cv.imshow("res", img)
cv.waitKey(0)
cv.destroyWindow("res")

~~~

#### mouse event 

~~~ python
# 鼠标事件作为画笔 双击鼠标出现一个圆
import cv2 as cv
import numpy as np


def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x,y), 100, (0, 255, 0), -1)


# create a black image
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow("image")
cv.setMouseCallback("image", draw_circle)
while (1):
    cv.imshow("image", img)
    if cv.waitKey(20) & 0xff == 27:
        break
cv.destroyAllWindows()


~~~

#### color palette

~~~python
# create color  palette
import cv2 as cv
import numpy as np


def nothing(x):
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("image")
# create trackbars for color palette
cv.createTrackbar("R", "image", 0, 255, nothing)
cv.createTrackbar("G", "image", 0, 255, nothing)
cv.createTrackbar("B", "image", 0, 255, nothing)
# create switch for ON/OFF functionality
switch = "0:OFF\n1:ON"

cv.createTrackbar(switch, "image", 0, 1, nothing)


while(1):
    cv.imshow("image", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

# get current positions of four trackbars
r = cv.getTrackbarPos("R", "image")
g = cv.getTrackbarPos("G", "image")
b = cv.getTrackbarPos("B", "image")
s = cv.getTrackbarPos(switch, "image")
if s == 0:
    img[:] = 0
else:
    img[:] = [b, g, r]
cv.destroyAllWindows()

~~~

#### pixel  operation

~~~python
# pixel operation
import cv2 as cv
import numpy as np

img = cv.imread("E:/python_OpenCV lib/lena.jpg")
print(img.shape)  # (256, 256, 3)  彩色图像
print(img[100, 100])  # [81 81 81] 3通道色彩bgr
gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(gray_scale.shape)  # (256,256) grayscale
print(gray_scale[100, 100])  # 81 gray value
# print img.size= width*height*channels
print(img.size)  # 196608  256*256*3=196608
print(gray_scale.size)  # 65536 256*256*1=65536
# print array data type img.dtype
print(img.dtype)  # uint8
print(gray_scale.dtype)  # uint8
# ROI
hat = img[100:200, 50:150]  # clip a region of img
res = np.zeros((100, 100), np.uint8)  # a new window
res = hat
# set origin image. from a region image of img
hat = img[50:80, 50:100]  # 截取像素
img[100:130, 100:150] = hat  # 放到原图像指定位置
cv.imshow("result", img)
cv.waitKey(0)
cv.destroyAllWindows()


~~~

calculate time for function 

~~~ python
# count time for code  .
import cv2 as cv
import numpy as np
start = cv.getTickCount()
for i in range(100):
    print(i)
end = cv.getTickCount()
time = (end - start)/cv.getTickFrequency()
print(time)
~~~

### 第二讲 视频读入，显示，保存，视频帧参数修改操作

~~~python
import cv2 as cv
src = cv.VideoCapture(0)  # 获取视频
if src.isOpened():  # 判断是否正常打开
    opened, frame = src.read()  # 读取源  得到两个返回值 bool 和帧数
    frame = cv.flip(frame, 1)  # 颠倒摄像头镜像问题
    # cv.imshow("frame", frame)
else:
    opened = False
while open:
    ret, frame = src.read()
    if frame is None:
        break
    if ret:
        gray = cv.cvtColor(frame, cv.IMREAD_COLOR)
        cv.imshow("result", gray)
        if cv.waitKey(50) & 0xFF == 27:
            break
src.release()
cv.destroyAllWindows()
~~~

### 第三讲 截取部分图像数据

~~~python
import cv2 as cv
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
res = src[20:400, 50:220]  # H W POSITION 把图像按照期望进行切割截取
cv.imshow("result", res)
cv.imwrite("E:/python_OpenCV lib/lena_cutting.jpg", res)
cv.waitKey(0)
cv.destroyAllWindows()
~~~

### 第四讲 颜色通道提取

~~~python
import cv2
src = cv2.imread("E:/python_OpenCV lib/lena.jpg")  # 源图像
b, g, r = cv2.split(src)  # 对图像进行通道划分
r[50:100, 50:100] = 0  # 操作通道值 把红色通道制定区域设置为0
g[50:100, 50:100] = 0  # 双通道操作
image_new = cv2.merge((b, g, r))  # 合成操作后的通道
cv2.imshow("new_image", image_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
~~~

#### changing color space  and object tracking

~~~python
# object tracking

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
if cap.isOpened():
    opened, frame = cap.read()
    frame = cv.flip(frame, 1)
else:
    opened = False
while (opened):
    ret, frame = cap.read()  # get frame from video
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    low_blue = np.array([100, 50, 50])
    upper_blue = np.array([150, 255, 255])
    # threshold  the hsv image to get only blue colors
    mask = cv.inRange(hsv, low_blue, upper_blue)
    # bitwise_and mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    k = cv.waitKey(27) & 0xff
    if k == 27:
        break
cv.destroyAllWindows()
~~~



### 第五讲 边界填充

~~~python
# 边界填充copyMakeBorder  边界需要画出来 使用了matplotlib
# replicate 复制方法
# reflect 反射
# reflect_101
# wrap
# constant
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("E:/python_OpenCV lib/lena.jpg")
top_size, bottom_size, left_size, right_size = (20, 20, 20, 20)  # 制定扩充边界的大小
img_replace = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv.BORDER_REPLICATE)
plt.subplot(231), plt.imshow(img, "gray"), plt.title("original")
plt.subplot(232), plt.imshow(img_replace, "gray"), plt.title("replace")
plt.savefig("E:/python_OpenCV lib/lena.jpg")
plt.show()


# import cv2
# import matplotlib.pyplot as plt
# img = cv2.imread("E:/python_OpenCV lib/lena.jpg")
# top_size,bottom_size,left_size,right_size = (50,50,50,50)
# 边界填充方法
# img_replace = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REPLICATE)
# img_reflect = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT)
# img_reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
# img_wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
# img_constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_CONSTANT, value=0)
# # cv_show('img_wrap',img_wrap) 显示图
# plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(img_replace,'gray'),plt.title('Replace')
# plt.subplot(233), plt.imshow(img_reflect, 'gray'), plt.title('REFLECT')
# plt.subplot(234), plt.imshow(img_reflect101, 'gray'), plt.title('REFLECT_101')
# plt.subplot(235), plt.imshow(img_wrap, 'gray'), plt.title('WRAP')
# plt.subplot(236), plt.imshow(img_constant, 'gray'), plt.title('CONSTANT')
# plt.savefig('cat_fill.jpg')
# plt.show()

~~~

### 第六讲 数值计算

~~~python
import cv2 as cv
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
src = src+20  # 图像加一个值 就是每个像素每个通道都加
cv.imshow("ori", src)
cv.waitKey(0)
cv.destroyAllWindows()
~~~

### 第七讲 图像融合

~~~ pythoN
# 图像融合  首先图像shape相等 或者cv.resize(src,(a,b)) 图像的等比例缩放 cv.resize(src,(0,0),fx=a,fx=b)
# import cv2 as cv
# src = cv.imread("E:/python_OpenCV lib/lena.jpg")
# result = cv.resize(src, (0, 0), fx=2, fy=2)  # fx=2 方法倍数  (0,0) 是指定像素大小
# cv.imshow("result", result)
# cv.waitKey()
# cv.destroyAllWindows()
import cv2 as cv


def details(image):
    print(type(image))
    print(image.size)
    print(image.shape)
    print(image.dtype)


# 图像大小进行一致化
src1 = cv.imread("E:/python_OpenCV lib/img_addation1.jpg")
src2 = cv.imread("E:/python_OpenCV lib/img_addation2.jpg")
details(src1)
print("------")
details(src2)
changed = cv.resize(src1, (295, 171))
details(changed)
# 融合   这里的融合会有背景混乱 图像噪声过大的结果
# fashion = src2+changed
# cv.imshow("fashion img", fashion)
# 使用cv.addWeighted  分别以两张图片的权重进行融合 a*x1+b*x2+c a=0.4 b=0.6
re_fashion = cv.addWeighted(src2, 0.3, changed, 0.7, 0)
cv.imshow("re_fashion", re_fashion)
cv.waitKey()
cv.destroyAllWindows()

~~~

### 第八讲 图像处理（图像阙值）

~~~python
import cv2
import matplotlib.pyplot as plt
# 多个图像的集中显示和对比
img = cv2.imread("E:/python_OpenCV lib/lena.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,img_bi = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
ret_1,img_bi_inv = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
ret_2,img_tr = cv2.threshold(img_gray,127,255,cv2.THRESH_TRUNC)
re_3,img_zero = cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO)
re_4,img_zero_inv = cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO_INV)

titles = ["Original","Binary",'Binary_INV','TRUNC','ZERO','ZERO_INV']
images = [img,img_bi,img_bi_inv,img_tr,img_zero,img_zero_inv]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray'),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])   # 不显示坐标轴
plt.show()
-------------------------------
# 图像的阈值操作
# ret dst = cv2.threshold(src, thresh, maxval, type) thresh一般是127 maxval =255 type(二值化操作类型)有五种类型
import cv2 as cv
import matplotlib.pyplot as plt
src = cv.imread("E:/python_OpenCV lib/lena_gray.jpg")  # 输入原图(因为阈值的特性我们使用二值图像)
# 1.THRESH_BINARY
# ret, img_bi = cv.threshold(src, 127, 255, cv.THRESH_BINARY)  # 大于阈值的像素值赋值为255,
# cv.imshow("test", img_bi)
# 2.THRESH_BINARY_INV
# ret, img_bi_inv = cv.threshold(src, 127, 255, cv.THRESH_BINARY_INV)  # 二值得反转,
# cv.imshow("test", img_bi_inv)
# 3.cv.THRESH_TRUNC  大于阈值部分取值阈值
# ret, img_bi_trunc = cv.threshold(src, 127, 255, cv.THRESH_TRUNC)  # 大于阈值的像素值取阈值127,
# cv.imshow("test", img_bi_trunc)
# 4.THRESH_TOZONE   大于阈值不变,小于阈值的为0
# ret, img_bi_tozone = cv.threshold(src, 127, 255, cv.THRESH_TOZERO)  # 大于阈值的像素值不变,小于阈值的取0,
# cv.imshow("test", img_bi_tozone)
# 5 THRESH_TOZONE_INV
# ret, img_bi_tozone_inv = cv.threshold(src, 127, 255, cv.THRESH_TOZERO_INV)  # 大于阈值的像素值不变,小于阈值的取0,
# cv.imshow("test", img_bi_tozone_inv)
cv.waitKey(0)
cv.destroyAllWindows()

~~~

#### adaptive threshold

~~~python
# simple threshold , adaptive threshold
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("E:/python_OpenCV lib/lena.jpg", 0)
img = cv.medianBlur(img, 5)
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  # 固定阈值二值化 global threshold
# dst = cv2.adaptiveThreshold(src, maxval, thresh_type, type, Block Size, C) 自适应
th2 = cv.adaptiveThreshold(img,255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
titles = ["original image", "global thresholding", "adaptive mean thresholding", "adaptive Gussian threshold"]
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()



~~~

#### **Otsu’s Binarization**

~~~python
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("E:/python_OpenCV lib/lena.jpg", 0)
# global thresholding 全局阈值 ， 固定阈值二值化
ret1, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)', 'Original Noisy Image','Histogram',"Otsu's Thresholding", 'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()


~~~

#### 图像色彩空间

~~~ python
通过颜色进行对象提取 
现在我们知道如何将BGR图像转换为HSV，我们可以使用HSV色彩空间来提取彩色对象。在HSV中表示颜色比在BGR颜色空间中更容易。在我们的程序中，我们将尝试提取视频画面中的蓝色对象。下面是方法程序执行步骤：
获取视频中的每一帧
从BGR转换为HSV颜色空间
我们为HSV图像设定一系列的蓝色阈值
单独提取蓝色对象并显示，之后我们便可以对我们想要的图像做任何事情
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # transform rgb to hsv
    # define color range
    low_blue = np.array([110,50,50])
    hight_blue = np.array([130,255,255])
    # mask range of color
    mask = cv.inRange(hsv,low_blue,hight_blue)
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow("frame", frame)
    cv.imshow("result", res)
    k = cv.waitKey(5) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

~~~



### 给图像加椒盐噪声代码

~~~python
import cv2 as cv
import random as r
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
print(src.shape)
cv.imshow("1", src)
t1 = cv.getTickCount()
for i in range(src.shape[0]*src.shape[1]//10):
    r1 = r.randint(0, src.shape[0]-1)
    c1 = r.randint(0, 1)*255
    r2 = r.randint(0, src.shape[1]-1)
    c2 = r.randint(0, 1)*255
    src[r1, r2] = (c1, c1, c1)
t2 = cv.getTickCount()
t = (t2-t1)/cv.getTickFrequency()
print(t)
cv.imshow("2", src)
cv.imwrite("E:/python_OpenCV lib/lena_nosing.jpg", src)
cv.waitKey(0)
~~~

### 给图像添加高斯噪声代码

~~~  python 
import cv2 as cv
import random as r
import numpy as np
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
print(src.shape)
t1 = cv.getTickCount()
for i in range(src.shape[0]):
    for j in range(src.shape[1]):
        g = r.gauss(0, 10)
        r1 = np.where((g+src[i, j]) > 255, 255, (g+src[i, j]))
        r2 = np.where(r1 < 0, 0, r1)
        src[i, j] = np.round(r2)
t2 = cv.getTickCount()
print((t2-t1)/cv.getTickFrequency())
cv.imshow("result",src)
cv.imwrite("E:/python_OpenCV lib/lena_GaussNoise.jpg", src)
cv.waitKey(0)
~~~

### 第九讲 图像滤波去噪 

~~~ python
# 图像滤波 (remove nosing)  filter average , box_filter, gaussian_blur ,median_blur
import cv2 as cv
from matplotlib import pyplot as plt
src = cv.imread("E:/python_OpenCV lib/lena_nosing.jpg")  # 椒盐噪声源图像
cv.imshow("original", src)  # 显示原图
blur = cv.blur(src, (3, 3))  # 均值滤波(模糊化比较严重,噪声没有太大的减少)
# cv.imshow("result", blur)
box_filter = cv.boxFilter(src, -1, (3, 3), normalize=True)  # 方框滤波  当值为ture 和均值滤波一样,
# cv.imshow("result", box_filter)
Gussian_Blur = cv.GaussianBlur(src, (3, 3), 1)  # 更重视中间值 上下左右的比重增加,而对角数值比重进行减轻
# cv.imshow("result", Gussian_Blur)
median_blur = cv.medianBlur(src, 5) # 中值滤波 基本没有噪声 但是平滑较严重 图像有模糊现象
# 下边是图像结果的显示
titles = ["src", "blur", "box_filter", "gussian_blur", "median_blur"]
results = [src, blur, box_filter, Gussian_Blur, median_blur]
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(results[i], "gray"), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])   # 不显示坐标轴
plt.show()
~~~

### 第十讲 图像形态学处理,梯度处理Sobel,Scharr, Laplacian算子

~~~python
"""
图像分割将图像划分为均匀有意义的区域集合, 根据特征或者属性(对比度, 灰度级, 光谱值, 纹理特征)进行处理 得到我们想要的背景前景 提取对象  在图像分割中主要是边缘, 线, 点的检测
腐蚀与膨胀属于形态学操作，所谓的形态学，就是改变物体的形状，形象理解一些：腐蚀=变瘦 膨胀=变胖
	腐蚀：是一种消除边界点，使边界向内部收缩的过程
	膨胀：是将与物体接触的所有背景点合并到该物体中，使边界向外部扩张的过程，可以用来填补物体中的空洞
	先腐蚀后膨胀的过程称为 开运算。用来消除小物体、在纤细点处分离物体、平滑较大物体的边界的同时并不明显改变其面积
	先膨胀后腐蚀的过程称为 闭运算。用来填充物体内细小空洞、连接邻近物体、平滑其边界的同时并不明显改变其面积.
	膨胀 - 腐蚀的过程称为 梯度运算。用来计算轮廓
	顶帽：原始输入 - 开运算结果 
	黑帽：闭运算 - 原始输入
""" 
# 主要使用cv2.erode()和cv2.dilate() 以及膨胀腐蚀的开闭运算
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("E:/python_OpenCV lib/NAME.JPG", cv.IMREAD_GRAYSCALE)
kernel = np.ones((3, 3), np.uint8)
erosion = cv.erode(img, kernel, iterations=2)  # 膨胀 结果1 是迭代次数
dilate = cv.dilate(img, kernel, iterations=3)  # 腐蚀
res = np.hstack((img, erosion, dilate))
cv.imshow("image and result", res)
cv.waitKey(0)
cv.destroyAllWindows()
~~~

#### gamma 矫正 

~~~python
通过gamma 矫正对输入图像进行颜色空间的标准化（归一化）目的是调整图像的对比度，降低图像局部的阴影和光照变化影响，同时抑制噪声。
import numpy as np
import cv2 as cv
img = cv.imread("E:/python_OpenCV lib/face.jpg", 0)
print(img.shape)
# gamma  矫正 值越大 contrast越大
img1 = np.power(img/float(np.max(img)), 1/1.5)
img2 = np.power(img/float(np.max(img)), 1.5)
cv.imshow("ori", img)
cv.imshow("gamma=1/1.5", img1)
cv.imshow("gamma=1.5", img2)
cv.waitKey(0)
cv.destroyAllWindows()
~~~



#### 开闭运算

~~~python
# 开运算 先腐蚀再膨胀
import cv2 as cv
import numpy as np
img = cv.imread("E:/python_OpenCV lib/NAME.JPG", cv.IMREAD_GRAYSCALE)
kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)  # 开 腐蚀 去掉边角的毛刺
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)  # 闭 膨胀 剩余膨胀轮廓
result = np.hstack((img, opening, closing))
cv.imshow("open and close", result)
cv.waitKey(0)
cv.destroyAllWindows()
~~~

#### 梯度运算 (膨胀-腐蚀)

~~~python
# 梯度运算= 膨胀-腐蚀  膨胀一个轮廓 然后再对原图像进行腐蚀 得出一个轮廓
import cv2 as cv
import numpy as np
img = cv.imread("E:/python_OpenCV lib/gradient_demo.jpg")
kernel = np.ones((3, 3), np.uint8)
dilate = cv.dilate(img, kernel, iterations=5)
erosion = cv.erode(img, kernel, iterations=5)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
res = np.hstack((dilate, erosion, gradient))
cv.imshow("result", res)
cv.waitKey(0)
cv.destroyAllWindows()
~~~

#### 礼帽 (原始图像-开运算结果)

黑帽(闭运算-原始输入=膨胀的边缘部分)

~~~python
import numpy as np
import cv2 as cv
img = cv.imread("E:/python_OpenCV lib/gradient_demo.jpg")
kernel = np.ones((3, 3), np.uint8)
top_hat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)  # 礼帽 得出边缘毛刺
black_hat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)  # 黑帽 图像边缘轮廓
res = np.hstack((img, top_hat, black_hat))
cv.imshow("result", res)
cv.waitKey(0)
cv.destroyAllWindows()

~~~

#### Robert算子

~~~python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import Model
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
img_RGB = cv.cvtColor(src, cv.COLOR_BGR2RGB) #转成RGB 方便后面显示
gray_img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 图像转为灰度图
# Robert 算子
# template
kernel_x = np.array([[1, 0], [0, -1]], dtype=int)
kernel_y = np.array([[0, 1], [-1, 0]], dtype=int)
x = cv.filter2D(gray_img, cv.CV_16S, kernel_x)
y = cv.filter2D(gray_img, cv.CV_16S, kernel_y)
# 转UNIT8
absx = cv.convertScaleAbs(x)
abxy = cv.convertScaleAbs(y)
Roberts = cv.addWeighted(absx, 0.5, abxy, 0.5, 0)
# 显示正常中文标签
# plt.rcParams["font.sans-serif"] = ["SimHei"]

# 显示图形
# titles = [u'原始图像', u'Roberts算子']
# images = [img_RGB, Roberts]
# for i in range(2):
#     plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()
# 显示结果图像
plt.subplot(121), plt.imshow(img_RGB), plt.title("original"), plt.axis("off")
plt.subplot(122), plt.imshow(Roberts), plt.title("robert algorithm"), plt.axis("off")
plt.show()

~~~



#### Prewitt 算子

~~~python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
gray_img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 图像转为灰度图
img_RGB = cv.cvtColor(src, cv.COLOR_BGR2RGB)  # 为了显示原图
# Prewitt 算子 基于Robert算子的进阶版 3*3的模板 直观视觉是轮廓对比Robert 更加粗
# 模板
kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
x = cv.filter2D(gray_img, cv.CV_16S, kernel_x)
y = cv.filter2D(gray_img, cv.CV_16S, kernel_y)

absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Prewitt = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# 显示结果图像
plt.subplot(121), plt.imshow(img_RGB), plt.title("origin image"), plt.axis('off')  # 坐标轴关闭
plt.subplot(122), plt.imshow(Prewitt), plt.title("Prewitt"), plt.axis('off')
plt.show()

~~~



#### 图像梯度 Sobel算子



#### canny边缘检测

- 1 使用高斯滤波器，以平滑图像，滤除噪声。
- 2 计算图像中每个像素点的梯度强度和方向。
- 3 应用非极大值（Non-Maximum Suppression, NMS）抑制，以消除边缘检测带来的杂散响应。
- 4 应用双阈值（Double-Threshold）检测来确定真实的和潜在的边缘。
- 5 通过抑制孤立的弱边缘最终完成边缘检测。

~~~ python
import numpy as np
import cv2 as cv
# canny 轮廓获取 根据两个参数进行制定双阈值的范围
img = cv.imread("E:/python_OpenCV lib/lena.jpg", cv.IMREAD_GRAYSCALE)  # 灰度图
res_1 = cv.Canny(img, 300, 400)  # canny 方法 双阈值参数根据图像进行调整 大于阈值是边界 , 在阈值之间连续的值是边界 小于阈值的舍弃
res_2 = cv.Canny(img, 100, 200)
res = np.hstack((img, res_1, res_2))
cv.imshow("result", res)
cv.waitKey(0)
cv.destroyAllWindows()

~~~

#### Prewitt 算子

~~~python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
gray_img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 图像转为灰度图
img_RGB = cv.cvtColor(src, cv.COLOR_BGR2RGB)  # 为了显示原图
# Prewitt 算子 基于Robert算子的进阶版 3*3的模板 直观视觉是轮廓对比Robert 更加粗
# 模板
kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
x = cv.filter2D(gray_img, cv.CV_16S, kernel_x)
y = cv.filter2D(gray_img, cv.CV_16S, kernel_y)

absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Prewitt = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# 显示结果图像
plt.subplot(121), plt.imshow(img_RGB), plt.title("origin image"), plt.axis('off')  # 坐标轴关闭
plt.subplot(122), plt.imshow(Prewitt), plt.title("Prewitt"), plt.axis('off')
plt.show()

~~~

####  Laplacian 算子

~~~python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("E:/python_OpenCV lib/lena.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# 拉普拉斯算法  对噪声点效果很差
dst = cv.Laplacian(gray_img, cv.CV_16S, ksize=3)
Laplacian = cv.convertScaleAbs(dst)
plt.subplot(121), plt.imshow(RGB_img), plt.title("origin_img"), plt.axis("off")
plt.subplot(122), plt.imshow(Laplacian, cmap=plt.cm.gray), plt.title("Laplacian"), plt.axis("off")
plt.show()
~~~

#### Kirsh 算子

~~~python

~~~



### 十一讲 图像金字塔   

高斯金字塔(向下采样), 拉普拉斯金字塔(向上采样) 两种经典金字塔

~~~ python
# 生成高斯金字塔的具体操作 向下采样: 从大到小  1. 对图像进行高斯卷积, 2. 删除所有的偶数行和偶数列
# 拉普拉斯金字塔 向上采样 从小到达: 1. 将维数扩大两位, 2. 扩大位的值设置为0, 3. 对新图像进行高斯卷积, 4.用新层次的高斯金字塔减去3中形成的图像
#  pyramid of image
import cv2 as cv
import numpy as np
img = cv.imread("E:/python_OpenCV lib/lena_pyramid.jpg")
up_samp = cv.pyrUp(img)  # 高斯金字塔就是向下采样 图像变小,高斯卷积然后删除了偶数行列,
down_sampling = cv.pyrDown(img)  # 拉普拉斯金字塔 向上采样,图像变大, 扩大位置填充0
cv.imshow("original", img)
cv.imshow("up_sampling", up_samp)
cv.imshow("down_sampling", down_sampling)
cv.waitKey(0)
cv.destroyAllWindows()


~~~

### 十二讲 图像轮廓   轮廓特征 轮廓近似

- cv2.findContours(img,mode,method)
  **img: 二值图像**
  **mode: 轮廓检索模式**

- RETR_EXTERNAL ：只检索最外面的轮廓；

- RETR_LIST：检索所有的轮廓，并将其保存到一条链表当中；

- RETR_CCOMP：检索所有的轮廓，并将他们组织为两层：顶层是各部分的外部边界，第二层是空洞的边界;

- **RETR_TREE**：检索所有的轮廓，并重构嵌套轮廓的整个层次; （通常选这个）

- **method:轮廓逼近方法**

  - CHAIN_APPROX_NONE：以Freeman链码的方式输出轮廓，所有其他方法输出多边形（顶点的序列）。
  - CHAIN_APPROX_SIMPLE:压缩水平的、垂直的和斜的部分，也就是，函数只保留他们的终点部分。

  **返回值**

  - contours 是一个list，list中每个元素都是图像中的一个轮廓，用numpy中的ndarray表示
  
  - hierarchy 是一个ndarray，其中的元素个数和轮廓个数相同，每个轮廓contours[i]对应4个hierarchy元素hierarchy[i][0] ~hierarchy[i][3]，分别表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，则该值为负数
  
  - ## 5. 凸包
  
    凸包看起来类似于轮廓近似，但它不是（两者在某些情况下可能提供相同的结果）。这里，`cv.convexHull()`函数检查曲线的凸性缺陷并进行修正。一般而言，凸曲线是总是凸出或至少平坦的曲线。如果它在内部膨胀，则称为凸性缺陷。例如，检查下面的手形图像。红线表示手的凸包。双面箭头标记显示凸起缺陷，即船体与轮廓的局部最大偏差。

~~~ python
import cv2 as cv
import numpy as np
img = cv.imread("E:/python_OpenCV lib/contours.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   # 彩色图以灰度图的形式显示
ret, thresh = cv.threshold(gray_img, 50, 255, cv.THRESH_BINARY)  # 使用阈值函数对灰度图进行二值化
# cv.imwrite("E:/python_OpenCV lib/contours_binary.jpg", thresh)
# cv.imshow("thresh", thresh)
# cv.waitKey(0)
# cv.destroyAllWindows()
# 计算轮廓  cv2.findContours(img,mode,method)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# 绘制轮廓 先进行copy 避免在原图作画
draw_img1 = img.copy()
draw_img2 = img.copy()
draw_img3 = img.copy()
# 参数如下：传入绘制图像，轮廓，轮廓索引，颜色模式，线条厚度
all_contours = cv.drawContours(draw_img1, contours, -1, (0, 255, 0), 2)	 # -1是指所有的轮廓
contours_0 = cv.drawContours(draw_img2, contours, 0, (0, 0, 255), 2)		# 检测到的第1个轮廓
contours_1 = cv.drawContours(draw_img3, contours, 1, (255, 0, 0), 2)		# 检测到的第2个轮廓
# 图像轮廓特征
cnt = contours[3]  #
# res = cv.contourArea(cnt)  # 轮廓特征的面积
res = cv.arcLength(cnt, True)  # 周长 True 表示闭合
print(cnt)
print(res)
#  图像轮廓近似
epsilon1 = 0.01*cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon1, True)
draw_approx = cv.drawContours(draw_img1, [approx], -1, (0, 0, 255), 2)

cv.imshow('res', np.hstack((all_contours, contours_0, contours_1,)))
cv.waitKey(0)

# 轮廓特征
cnt = contours[0]
#面积
cv2.contourArea(cnt)

#周长，True表示闭合的
cv2.arcLength(cnt,True)
#外接边界矩形  直边矩形，
"旋转矩形"这里，以最小面积绘制边界矩形，因此它也考虑旋转。使用的函数是cv.minAreaRect()。它返回一个Box2D结构，其中包含以下detals - (center(x，y)，(width，height)，rotation of rotation)。但要画这个矩形，我们需要矩形的4个角。它是由函数cv.boxPoints()获得的
#  轮廓近似
cv2.approxPolyDP(contour,epsilon,True) 把一条平滑的曲线曲折化
参数
epsilon：表示的是精度，越小精度越高，因为表示的意思是是原始曲线与近似曲线之间的最大距离
closed：表示输出的多边形是否封闭；true表示封闭，false表示不封闭。

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
src = cv.imread("E:/python_OpenCV lib/gradient_self.jpg")  # binary_image
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# cv.imshow("result", thresh)
# cv.waitKey(0)
# cv.destroyAllWindows()
# 绘制轮廓
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
draw_src = src.copy()  # 如果没有用copy 相当于在原图作画
res = cv.drawContours(draw_src, contours, -1, (0, 255, 0), 2)
cv.imshow("res", res)
cnt = contours[-1]  # 拿出某一个轮廓进行计算
res1 = cv.arcLength(cnt, True)  # 计算周长
print(res1)
# 外接矩形轮廓
x, y, w, h = cv.boundingRect(cnt)
img = cv.rectangle(src, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv.imshow("res", img)
cv.waitKey(0)
cv.destroyAllWindows()
# 旋转矩形
import cv2 as cv
import numpy as np
img = cv.imread("E:/python_OpenCV lib/shape.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, bin_img = cv.threshold(img_gray,127,255,cv.THRESH_BINARY)
contours,hierarchy = cv.findContours(bin_img,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnt = contours[1]
# 一般外接矩形
# x, y, w, h = cv.boundingRect(cnt)
# img = cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# 最小旋转矩形
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img,[box],0,(0,255,0),2)
cv.imshow("res",img)
cv.waitKey(0)
cv.destroyAllWindows()
~~~

###  十三讲 模板匹配

模板匹配和卷积原理很像,模板在原图像上从原点开始滑动,计算模板与(图像被模板覆盖的地方)的差别程度,这个差别程度的计算方法在opencv里有6种,然后把每次计算的結果放入一个矩阵里,作为結果输出.假如原图形是AxB大小,而模板是axb大小,则输出结果的矩阵是(A-a+1)x(B-b+1)  简单来说: 模板匹配就是在整个图像区域发现与给定子图像匹配的小块区域

- **cv2.matchTemplate**(image, templ, method, result=None, mask=None)
  image：待匹配图像
  templ：模板图像
  method：计算匹配程度的方法
  返回参数res：是一个结果矩阵，假设待匹配图像为 I，宽高为(W,H)，模板图像为 T，宽高为(w,h)。那么result的大小就为(W-w+1, H-h+1)
- 其中method：
  TM-SQDIFF:计算平方不同,计算出来的值越小,越相关
  TM_CCORR:计算相关性,计算出来的值越大,越相关
  TM_CCOEFF:计算相关系数,计算出来的值越大,越相关
  TM SQDIFF-NORMED: 计算归一化平方不同,计算出来的值越接近0,越相关
  TM_CCORR-NORMED: 计t算归一化相关性,计算出来的值越接近1,越相关
  TM-CCOEFF-NORMED:计算归一化相关系数,计算出来的值越接近1,越相关

~~~ python
import cv2
import numpy as np
from matplotlib import pyplot as plt
# %matplotlib inline
img = cv2.imread("E:/python_OpenCV lib/lena.jpg", 0)
img2 = img.copy()
template = cv2.imread("E:/python_OpenCV lib/template.jpg", 0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)	# method这不要写成字符串的形式，别加上引号, cv2.xx就行
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

   
    								#  匹配对个对象
import cv2
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv2.imread("E:/python_OpenCV lib/lena.jpg")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread("E:/python_OpenCV lib/template.jpg", 0)
h, w = template.shape[:2]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
# 取匹配程度大于%90的坐标
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # *号表示可选参数
    bottom_right = (pt[0] + w, pt[1] + h)
    cv2.rectangle(img_rgb, pt, bottom_right, (0, 0, 255), 2)

cv2.imshow('img_rgb', img_rgb)
cv2.waitKey(0)

~~~

### 十四讲 直方图 histogram

直方图是灰度级的函数,描述的是图像中每个灰度级的个数(频数) 反映图像中每个灰度级出现的频率.

- cv2.calcHist(images,channels,mask,histSize,ranges)
  images: 原图像图像格式为 uint8 或 ﬂoat32。当传入函数时应 **用中括号 []** 括来例如[img]
  channels: 同样用中括号括来它会告函数我们统幅图 像的直方图。如果入图像是灰度图它的值就是 [0]如果是彩色图像 的传入的参数可以是 [0][1][2] 它们分别对应着 BGR。
  mask: 掩模图像。统整幅图像的直方图就把它为 None。但是如 果你想统图像某一分的直方图的你就制作一个掩模图像并 使用它。
  histSize:BIN 的数目。也应用中括号括来
  ranges: 像素值范围常为 [0-256]

~~~ python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("E:/python_OpenCV lib/lena.jpg", 1)


def cv_show(img, name):
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# 参数 图像, channels(灰度图0,彩色123对应着BGR) mask(掩模图像要整个图像的直方图就是NONE)
hist = cv.calcHist([img], [0], None, [256], [0, 256])  # 直方图的计算
plt.hist(img.ravel(), 256)
plt.show()

~~~

~~~ python
# 三个颜色通道的直方图
import cv2 as cv  # bgr
import numpy as np
import matplotlib.pyplot as plt  # rgb
img = cv.imread("E:/python_OpenCV lib/lena.jpg", 1)
color = ("b", "g", "r")  # 使用cv2色彩模式
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0,256])  # 计算直方图
    plt.plot(histr, color=col)
    plt.xlim([0, 256])  # 显示台控制 就是X轴的取值
    plt.show()  # 展示直方图结果
~~~

#### 掩模操作

~~~python
# mask operator
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import Model as Mo
img = cv.imread("E:/python_OpenCV lib/lena_gray.jpg", 0)
# 创建mask
mask = np.zeros(img.shape[0:2], np.uint8)  # 画出一个窗口
mask[50:200, 50:200] = 255  # mask的大小范围

# 对图像进行掩模
masked_img = cv.bitwise_and(img, img, mask=mask)  # &操作  图像和掩模进行重合计算
hist_full = cv.calcHist([img], [0], None, [256], [0, 256])  # 计算直方图
hist_mask = cv.calcHist([img], [0], mask, [256], [0, 256])
# 展示结果  这里221 "gray" 都是固定参数 不要改变
plt.subplot(221), plt.imshow(img, "gray")  # 显示的原图像
plt.subplot(222), plt.imshow(mask, "gray")  # 掩模
plt.subplot(223), plt.imshow(masked_img, "gray")  # 掩模后的图像
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)  # 这里画出了直方图
plt.xlim([0, 256])
plt.show()
~~~

#### 直方图均衡化 

直方图均衡化 + 自适应均衡

~~~python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import Model as Mo
img = cv.imread("E:/python_OpenCV lib/lena_gray.jpg", 0)
res = cv.equalizeHist(img)  # 直方图均衡化 使得图像的灰度色彩对比度增大
# 自适应直方图均衡化
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(3, 3))  #
res1 = clahe.apply(img)
# result = np.hstack((img, res, res1))
hist1 = cv.calcHist([img], [0], None, [256], [0, 256])
hist2 = cv.calcHist([res], [0], None, [256], [0, 256])
hist3 = cv.calcHist([res1], [0], None, [256], [0, 256])
plt.subplot(221), plt.imshow(img, "gray")  # 显示的原图像
plt.subplot(222), plt.imshow(res, "gray")
plt.subplot(223), plt.imshow(res1, "gray")
plt.subplot(224),plt.plot(img), plt.plot(hist1), plt.plot(hist2), plt.plot(hist3)  # 这里画出了直方图
plt.xlim(0, 256)
plt.show()

~~~

### 第十五讲 傅里叶变换 

时域和空间域的不同角度问题

傅里叶变换的作用
高频：**变化剧烈**的灰度分量，例如边界
低频：**变化缓慢**的灰度分量，例如一片大海
在原图中做低频/高频的变换较难，因此转换到频域中处理较方便   在一张图像中我们可以根据频率变化划分不同的对象

滤波
低通滤波器：只保留低频，会使得图像模糊  (图像中异常点会消失 平滑,例如噪声)
高通滤波器：只保留高频，会使得图像细节增强  (图像锐化)

opencv中主要就是 **cv2.dft()** 和 **cv2.idft()** ，输入图像需要**先转换成np.float32 格式**。
得到的结果中频率为0的部分会在左上角，通常要转换到中心位置，可以通过shift变换来实现。
cv2.dft()返回的结果是双通道的（实部，虚部），通常还需要转换成图像格式才能展示（0,255）, 用逆变换cv2.idft()。

~~~python
# 傅里叶变换  时域和空间域的不同角度问题
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("E:/python_OpenCV lib/lena_gray.jpg", 0)
# 格式转换为np.float32
img_float32 = np.float32(img)
# 傅里叶变换 dft
dft = cv.dft(img_float32, flags=cv.DFT_COMPLEX_OUTPUT)
# np的 fftshift得到低频在中心的位置的频谱图
dft_shift = np.fft.fftshift(dft)
# 转换为灰度图的表示形式
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0], dft_shift[:, :, 1]))  # 0 and 1 两个通道
plt.subplot(121), plt.imshow(img, cmap="gray")
plt.title("input image"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("magnitude spectrum"), plt.xticks([]), plt.yticks([])
plt.show()
~~~

~~~ python
# 低通滤波
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("E:/python_OpenCV lib/lena_gray.jpg", 0)
# 1.转换成np.float32 格式
img_float32 = np.float32(img)
# 2.傅里叶变换 dft
dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
# 3.np的fftshift得到低频在中心位置的频谱图
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)     # 中心位置

# 4.低通滤波
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1  # 所以计算图像长宽是为制作mask,中心(30+30)x(30x30)区域为1

# 5.IDFT
fshift = dft_shift*mask					# 仅保留了中心区域
f_ishift = np.fft.ifftshift(fshift)		# 把中心位置的东西放回原位	ifftshift
img_back = cv2.idft(f_ishift)			# 从频谱图转换回来 idft
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])	# 转换一下 得到灰度图能表示的形式

plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap='gray')
plt.title('Result'), plt.xticks([]), plt.yticks([])

plt.show()

~~~

~~~python
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("E:/python_OpenCV lib/lena_gray.jpg", 0)
img_float32 = np.float32(img)

dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = int(rows/2) , int(cols/2)     # 中心位置

# 高通滤波
mask = np.ones((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 0

# IDFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Result'), plt.xticks([]), plt.yticks([])
plt.show()

~~~

### 十六讲 颜色插值算法

~~~python
# 图像插值是因为图像在几何变化中 源图像的像素值可能不能整值进行表达 我们需要进行插值计算 获得变化图像的像素值
import cv2 as cv
# cv. resize(src, dsize[, dst[, fx[, fy[ , interpolation])
# 通常, 缩小图像使用区域插值, 放大使用三次样条插值和双线性插值,
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
print(src.shape)  # (225, 225, 3)
print(src.size)
width = int(src.shape[0]*0.3)  # x
height = int(src.shape[1]*0.3)  # y
dsize = (width, height)  # 重置大小
resized = cv.resize(src, dsize, interpolation=cv.INTER_LINEAR)   # 双线性插值法
# 图像变换数据
fx = 1.5
fy = 1.5
resized1 = cv.resize(src, dsize=None, fx=fx, fy=fy, interpolation=cv.INTER_NEAREST)  # 最近邻插值法
resized2 = cv.resize(src, dsize=None, fx=fx, fy=fy, interpolation=cv.INTER_LINEAR)  # 双线性插值法
resized3 =cv.resize(src, dsize=None, fx=fx, fy=fy, interpolation=cv.INTER_CUBIC)  # 基于4*4的三次插值法
resized4 = cv.resize(src, dsize=None, fx=fx, fy=fy, interpolation=cv.INTER_AREA)  # 区域插值,块匹配算法
print("resized shape", resized.shape)  # int(225*0.3, 225*0.3, 3)
print("nearest interpolation", resized1.shape)  #
cv.imshow("ori", src)
cv.imshow("res", resized)
cv.imshow("nearest interpolation", resized1)
cv.imshow("bilinear interpolation", resized2)
cv.imshow("three linear interpolation", resized3)
cv.imshow("block interpolation", resized4)
cv.waitKey(0)
cv.destroyAllWindows()
~~~

### 图像分割

图像分割将图像划分为均匀有意义的区域集合, 根据特征或者属性(对比度, 灰度级, 光谱值, 纹理特征)进行处理 得到我们想要的背景前景 提取对象  在图像分割中主要是边缘, 线, 点的检测  主要是Robert(2*2)对噪声敏感,  Sobel(3*3) , Prewitt(4*4 四方向), Kirsch(3*3 八方向),Canny(dual-threshold)抗噪 轮廓边缘检测算子

~~~ python 
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread("E:/python_OpenCV lib/lena.jpg")
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转成RGB 方便后面显示

# 灰度化处理图像
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯滤波
gaussianBlur = cv2.GaussianBlur(grayImage, (3, 3), 0)

# 阈值处理
ret, binary = cv2.threshold(gaussianBlur, 127, 255, cv2.THRESH_BINARY)

# Roberts算子
kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
kernely = np.array([[0, -1], [1, 0]], dtype=int)
x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# Prewitt算子
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Prewitt = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# Sobel算子
x = cv2.Sobel(grayImage, cv2.CV_16S, 1, 0)
y = cv2.Sobel(grayImage, cv2.CV_16S, 0, 1)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# Laplacian算子
dst = cv2.Laplacian(grayImage, cv2.CV_16S, ksize=3)
Laplacian = cv2.convertScaleAbs(dst)

# #效果图
# titles = ['Source Image', 'Binary Image', 'Roberts Image',
#           'Prewitt Image','Sobel Image', 'Laplacian Image']
# images = [lenna_img, binary, Roberts, Prewitt, Sobel, Laplacian]
# for i in np.arange(6):
#    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
# plt.show()

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# # 显示图形
plt.subplot(231), plt.imshow(img_RGB), plt.title('原始图像'), plt.axis('off')  # 坐标轴关闭
plt.subplot(232), plt.imshow(binary, cmap=plt.cm.gray), plt.title('二值图'), plt.axis('off')
plt.subplot(233), plt.imshow(Roberts, cmap=plt.cm.gray), plt.title('Roberts算子'), plt.axis('off')
plt.subplot(234), plt.imshow(Prewitt, cmap=plt.cm.gray), plt.title('Prewitt算子'), plt.axis('off')
plt.subplot(235), plt.imshow(Sobel, cmap=plt.cm.gray), plt.title('Sobel算子'), plt.axis('off')
plt.subplot(236), plt.imshow(Laplacian, cmap=plt.cm.gray), plt.title('Laplacian算子'), plt.axis('off')
plt.show()
~~~

### OCR

~~~python
import pytesseract as pyt
import cv2 as cv
from PIL import Image
"""
1: 判断文本朝向 进行图像预处理 做角度矫正和去噪
出现预处理很重要 图像可能是翻转, 有倾斜角的  需要正放.
"""
img = cv.imread("E:/python_OpenCV lib/OCR_R.jpg")
test = pyt.image_to_string(Image.fromarray(img))
print(test)
~~~

###  第十七讲 图像特征 Harris, Sift角点

~~~python
# 图像中一般存在 平面, 边界, 角点等三大类形状 我们通过Harris检测出图像中X,Y方向变化比较大的角点区域
import cv2 as cv
import numpy as np
# cv2.cornerHarris(img, blockSize, k)  img为float32类型图像, blocksize 指定区域大小可能是个高斯函数, ksize求导窗口大小.K 0.04/0.06
img = cv.imread("E:/python_OpenCV lib/corner_Harris.jpg")  # 输入图像
# print(type(img))  # <class 'numpy.ndarray'>  这里需要图像的类型转换
# print(img.shape)  # (225, 224, 3)
# print(img.size)  # 151200
# 图像的预处理
# 结果得出图像有点小 magnification processing
img = cv.resize(img, dsize=None, fx=2, fy=2)
print(img.shape)
gary_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 灰度图转换
print(type(gary_img))  # <class 'numpy.ndarray'>
gray_type = np.float32(gary_img)  # 图像的格式转换
res = cv.cornerHarris(gray_type, 2, 3, 0.04)
print("result_shape:", res.shape)  # result_shape: (225, 224)
# 角点判定
img[res > 0.05*res.max()] = [0, 0, 255]  # 就是我们的判断结果 为 True 那么就是角点 进行绿色标注 我们通过对0.01的更改获得更加精准的值
# 画出结果图像
cv.imshow("result", img)
cv.waitKey(0)
cv.destroyAllWindows()
~~~

#### sift角点检测   copyright  

~~~python

~~~

### 图像的变换 平移 旋转  

~~~ python
import cv2 as cv
import numpy as np

img = cv.imread("E:/python_OpenCV lib/lena.jpg")
# 图像的变换  仿射变换(Affine transformation / Affine map) 是二维坐标(x, y)到二维线性的变换(u,v)
# u=a1x+b1y+c v= a2x+b2y+c
# 图像的平移 cv.warpAffine(img,M,img_size)
h = np.float32([[1, 0, 10], [0, 1, 20]])  # M 变换矩阵 10 20 是平移量
rows, cols = img.shape[:2]  # 图像的长宽赋值给row col
res = cv.warpAffine(img, h, (rows, cols))
# 图像的扩大缩小(比例缩放) resized  这里还涉及到插值问题    前文16讲有介绍 不再演示
# 图像的旋转  cv.getRotationMatrix2D()  para: 旋转中心, 旋转角度, 旋转后缩放比例
M = cv.getRotationMatrix2D((rows/2, cols/2), 180, 1)  # M 矩阵  按照中心点 旋转 180 得到倒图像
res1 = cv.warpAffine(img, M, (rows, cols))
# cv.imshow("img", img)
# cv.imshow("res", res)
cv.imshow("res1", res1)
cv.waitKey(0)
cv.destroyAllWindows()
透视变换
对于透视变换，需要一个3x3变换矩阵。即使在转换之后，直线仍是直线。要找到此变换矩阵，需要在输入图像上找4个点，以及它们在输出图像中的对应位置。在这4个点中，其中任意3个不共线。然后可以通过函数cv.getPerspectiveTransform找到变换矩阵，将cv.warpPerspective应用于此3x3变换矩阵

~~~

#### **Geometric Transformations of Images**

~~~ python

~~~





#### 图像的仿射变换

图像的旋转加上拉升就是图像仿射变换，仿射变化也是需要一个M矩阵就可以，但是由于仿射变换比较复杂，一般直接找很难找到这个矩阵，opencv提供了根据变换前后三个点的对应关系来自动求解M。这个函数是
M=cv2.getAffineTransform(pos1,pos2),其中两个位置就是变换前后的对应位置关系。输 出的就是仿射矩阵M。然后在使用函数cv2.warpAffine()。形象化的图如下

~~~python
import cv2 as cv
import numpy as np
"""图像的旋转加上拉升就是图像仿射变换，仿射变化也是需要一个M矩阵就可以，但是由于仿射变换比较复杂，一般直接找很难找到这个矩阵，
opencv提供了根据变换前后三个点的对应关系来自动求解M。这个函数是
M=cv2.getAffineTransform(pos1,pos2),
其中两个位置就是变换前后的对应位置关系。
输出的就是仿射矩阵M。然后在使用函数cv2.warpAffine() 进行变换。
"""
img = cv.imread("E:/python_OpenCV lib/lena.jpg")
rows, cols = img.shape[:2]
print(img.shape)
# pst的值和图像的变换三个点有密切关系 运行代码查看各自代表值
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv.getAffineTransform(pts1, pts2)
res = cv.warpAffine(img, M, (rows, cols))
# 图像的透射
"""透视需要的是一个3*3的矩阵，同理opencv在构造这个矩阵的时候还是采用一种点对应的关系来通过函数自己寻找的，因为我们自己很难计算出来。
这个函数是M = cv2.getPerspectiveTransform(pts1,pts2)，
其中pts需要变换前后的4个点对应位置。得到M后在通过函数cv2.warpPerspective(img,M,(200,200))进行"""
pst3 = np.float32([[50, 60], [100., 52], [28, 200], [200, 220]])  # 四点
pst4 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
M1 = cv.getPerspectiveTransform(pst3, pst4)  # notice
res1 = cv.warpPerspective(img, M1, (110, 110))  # notice
cv.imshow("ori", img)
cv.imshow("res", res)
cv.imshow("res1", res1)
cv.waitKey(0)
cv.destroyAllWindows()
~~~

### 第十八讲 背景建模

1. 帧差法: 目标影像在不同图像中帧的位置不同, 进行差分运算. 不同帧对应的像素进行相减, 判断灰度差的绝对值, 当绝对值超过一定阈值, 判断为运动目标 (但是会引入噪音和空洞问题 )
2. 混合高斯模型 前景检测之前, 首先对背景进行训练, 对图像中的每一个背景采取混合高斯模型进行模拟, 在测试阶段, 对新来的像素进行GMM匹配, 如果该像素的值是一个高斯 就认为是一个背景, 否则认为是前景.

~~~ python
import numpy as np
import cv2 as cv
# 创建一个kernel
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
# 创建混合高斯背景建模
fgbg = cv.createBackgroundSubtractorMOG2()
cap = cv.VideoCapture(0)
while (True):
    ret, frame = cap.read()  # 获取每一帧
    frame = cv.flip(frame, 1)  # 镜像颠倒问题
    fgmask = fgbg.apply(frame)
    # 形态学进行开运算 去除噪声点
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
    # 寻找视频中的轮廓
    contours, hierarchy = cv.findContours(fgmask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # 计算轮廓周长(circumference)
        perimeter = cv.arcLength(c, True)
        if perimeter > 100:
            x, y, w, h = cv.boundingRect(c)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow("frame", frame)
    cv.imshow("fgmask", fgmask)
    k = cv.waitKey(150) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
~~~

### 第十九讲 optical flow estimation 

光流是空间运动物体在观测成像平面上的像素运动的瞬时速度, 根据各个像素点的速度矢量特征, 对图像进行动态分析, 

亮度恒定: 同一点(像素块)随着时间的变化, 他的亮度不会产生明显的变化

小运动: 对象的运动随着时间的变化不会引起位置的剧烈变化, 只有小运动情况下才能用前后帧之间的单位位置变化引起的灰度变化去近似灰度对位置的偏导 

空间一致:一个场景中临近点投影到图像上也是临近点. 并且临近点的速度一致, 因为光流法基本方程约束只有一个, 要求x,y方向的速度, 有两个位置变量, 所以需要联立N多个方程求解.

~~~ pythoN
"""光流计算和跟踪
cv.calcOpticalFlowPyrLK() : para:previmg, nextimg, prevpts(待跟踪的特征点向量), winsize, maxLevel(最大金字塔层数)
返回: nextPts 输出追踪特征点向量. status: 特征点是否找到的状态(1 Y, 0 N)
cv.goodFeaturesToTrack: 跟踪好的特征: feature_params , qualityLevel 品质因子越大,得到的角点越少. maxLevel 在这个范围 哪个品质因子最强

"""
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)  # 获取视频图像 0 是该设备的0号传感器
# 角点检测需要的参数
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7)
# lucas kanade 方法参数
lk_params = dict(winSize=(15, 15), maxLevel=2)
color = np.random.randint(0, 255, (100, 3))  # 对不同对象产生不同的颜色追踪路径
# 获取第一帧图像 进行灰度转换
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
# 检测第一帧的角点:
p0 = cv.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
# 创建一个MASK
mask = np.zeros_like(old_frame)  # 返回和给定数组具有相同形状和类型的零数组
while(True):
    ret, frame = cap.read()
    # 视频修正:
    frame = cv.flip(frame, 1)
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 光流计算, 前一帧图像和当前图像的角点 st(status)
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # 第一帧第二帧都找到角点
    good_new = p1[st == 1]
    good_old = p0[st == 1]
    # 绘制轨迹
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv.line(mask, (a, b), (c, d), color[i].tolist(), 2)
        frame = cv.circle(frame, (a, b), 5, color[i].tolist(), -1)
    img = cv.add(frame, mask)
    cv.imshow("frame", img)
    k = cv.waitKey(150) & 0xff
    if k == 27:
        break
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)
cap.release()
cv.destroyAllWindows()
~~~

Lucas-Kanade 法是计算稀疏特征集的光流（上面的例子使用Shi-Tomasi 算法检测角点）。OpenCV 还提供了一种计算稠密光流的方法，它会计算图像中的所有点的光流。这是基于 Gunner_Farneback 的算法，2003年Gunner Farneback在“Two-Frame Motion Estimation Based on Polynomial Expansion”中对该算法进行了解释。 下面的例子就是使用上面的算法计算稠密光流。结果是一个带有光流向量（u，v）的双通道数组。通过计算我们能得到光流的大小和方向。我们使用颜色对结果进行编码以便于更好的观察。方向对应于 H（Hue）通道，大小对应于 V（Value）通道

~~~ python
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

ret, frame1 = cap.read()
prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255

while(1):
    ret, frame2 = cap.read()
    next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)

    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
    bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)

    cv.imshow('frame2',bgr)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

~~~



### 第二十讲 DNN模块

~~~ Python

~~~

### 第二十一讲  face-recognition

~~~python
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



~~~

### 二十二讲 背景差分算法

~~~python
1."BackgroundSubtractorMOG"
这是一个以混合高斯模型为基础的前景/背景分割算法。2001年，P. KadewTraKuPong 和 R. Bowden在论文"An improved adaptive background mixture model for real-time tracking with shadow detection" 中进行了介绍。它使用 K（K=3 或 5）个高斯分布混合对背景像素进行建模。混合的权重表示这些颜色停留在场景中的时间比例，背景颜色是那些保持更长时间和更静态的颜色
import numpy as np
import cv2 as cv
# BackgroundSubtractorMOG
cap = cv.VideoCapture(0)
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()  # 混合高斯模型背景分割算法
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('frame',frame)
    cv.imshow("fgmask",fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

2. "BackgroundSubtractorMOG2"
这个也是以高斯混合模型为基础的背景/前景分割算法。它是以 2004 年和 2006 年 Z.Zivkovic 的两篇文章为基础的，分别是"Improved adaptive Gaussian mixture model for background subtraction" 和 "Efficient Adaptive Density Estimation per Image Pixel for the Task of Background Subtraction" 。这个算法的一个特点是它为每一个像素选择一个合适数目的高斯分布。（上一个方法中我们使用是 K 高斯分布）。它能更好地适应光照不同等各种场景。 和前面一样我们需要创建一个背景对象。但在这里我们我们可以选择是否检测阴影。如果 detectShadows = True（默认值），它就会检测并将影子标记出来，但是这样做会降低处理速度。影子会被标记为灰色。
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

fgbg = cv.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('frame',fgmask)
    cv.imshow("result", frame)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()

3."BackgroundSubtractorGMG"
此算法结合了静态背景图像估计和每个像素的贝叶斯分割。这是 2012 年Andrew_B.Godbehere，Akihiro_Matsukawa 和 Ken_Goldberg 在文章"Visual Tracking of Human Visitors under Variable-Lighting Conditions for a Responsive Audio Art Installation"中提出的。 它使用前面很少的图像（默认为前 120 帧）进行背景建模。它采用概率前景分割算法，使用贝叶斯推断识别可能的前景对象。这是一种自适应的估计，新观察到的对象比旧的对象具有更高的权重，从而对光照变化产生适应。一些形态学操作如开运算闭运算等被用来除去不需要的噪音。在开始的前几帧图像中你会看到一个黑色窗口。
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
fgbg = cv.bgsegm.createBackgroundSubtractorGMG()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
    cv.imshow('frame',fgmask)
    cv.imshow("result",frame)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
~~~

#### 帧差分算法 temporal different method

该算法是背景差集算法 的一个子方法，对时间上连续的2/3帧图像进行差分运算，不同帧对应的像素点相减，判断灰度差的绝对值。

~~~python

~~~



### HAR SYSTEM  background subtraction method

~~~python
import cv2 as cv
import numpy as np

def pre_process(image):  # pre-processing
    blur = cv.medianBlur(image, 5)
    # opening operation for nosing
    kernel = np.ones((3,3),np.uint8)
    opening = cv.morphologyEx(blur,cv.MORPH_OPEN,kernel)
    return opening

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
fgbg = cv.bgsegm.createBackgroundSubtractorGMG()  # shadow be detected
src = cv.VideoCapture("../HAR/KTH_walking.avi")  # acquire KTH video information
while True:
    ret, frame = src.read()
    frame = cv.flip(frame, 1)  # mirror
    pre_process(frame)
    fgmask = fgbg.apply(frame)  # background model
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)  # contous model
    fgmask = pre_process(fgmask)
    contous, hierarchy = cv.findContours(fgmask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # contous detecting
    for c in contous:
        perimeter = cv.arcLength(c, True)
        if perimeter > 30:  # set-up parameter to decrease noise
            x,y,w,h = cv.boundingRect(c)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow("frame", frame)
    cv.imshow("fgmask", fgmask)
    if cv.waitKey(50) & 0xff == 27:
        break
src.release()
cv.destroyAllWindows()
~~~

### meanshift and Camshift 在图像中寻找和追踪物体

OpenCV 中的 Meanshift :要在 OpenCV 中使用 Meanshift 算法，首先我们需要设置目标，找到它的直方图，这样我们就可以在每一帧上对目标进行反向投影来计算平均位移。另外我们还需要提供窗口的起始位置。对于直方图，我们仅考虑Hue（色调）值，此外，为了避免因光线不足而产生错误值，使用`cv.inRange ( )`函数将这些值忽略掉.

当物体运动时，运动明显地反映在直方图的反向投影图像中。因此，meanshift算法将窗口移动到具有最大密度的新位置。

~~~python
import numpy as np
import cv2 as cv
# 主要用于移动对象的追踪
cap = cv.VideoCapture(0)
# get first frame .
ret,frame = cap.read()

# setup initial location of window 追踪的窗口
r,h,c,w = 250,90,400,125  # simply hardcoded the values
track_window = (c,r,w,h)

# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
    ret, frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)

        # Draw it on image
        x,y,w,h = track_window
        img2 = cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
        cv.imshow('img2',img2)

        k = cv.waitKey(60) & 0xff
        if k == 27:
            break

    else:
        break

cv.destroyAllWindows()
cap.release()
~~~

Camshift

这里面有一个问题，我们的窗口的大小是固定的，而汽车由远及近（在视觉上）是一个逐渐变大的过程，固定窗口是不合适的。所以我们需要根据目标的大小和角度来对窗口进行调整。1988年，OpenCVLabs 提出了一个解决方案：CAMshift （Continuously Adaptive Meanshift）算法，由Gary Bradsky发表在他的论文“Computer Vision Face Tracking for Use in a Perceptual User Interface”中。

Camshift算法首先应用meanshift。一旦meanshift收敛，它就会更新窗口的大小，$$ s = 2 \times \sqrt{\frac{M_{00}}{256}} $$。它还计算最佳拟合椭圆的方向。同样，它将新的缩放搜索窗口和先前的窗口位置应用于meanshift。继续该过程直到满足所需的准确度。

~~~ python
import numpy as np
import cv2 as cv

cap = cv.VideoCapture('slow.flv')

# take first frame of the video
ret,frame = cap.read()

# setup initial location of window
r,h,c,w = 250,90,400,125  # simply hardcoded the values
track_window = (c,r,w,h)

# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply meanshift to get the new location
        ret, track_window = cv.CamShift(dst, track_window, term_crit)

        # Draw it on image
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv.polylines(frame,[pts],True, 255,2)
        cv.imshow('img2',img2)
        k = cv.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv.imwrite(chr(k)+".jpg",img2)
    else:
        break

cv.destroyAllWindows()
cap.release()
~~~

### HOG 特征提取

~~~ python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, exposure
np.set_printoptions(threshold=np.inf)  # 长显示数组矩阵
img = cv.imread("E:/python_OpenCV lib/lena.jpg", 0)
img = np.float32(img)/255  # 归一化
fd, hog_image = hog(img,orientations=8, pixels_per_cell=(16,16),cells_per_block=(1, 1), visualize=True,multichannel=False) # HOG vector
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6), sharex=True, sharey=True)
print(hog_image)
ax1.axis('off')
ax1.imshow(img, cmap=plt.cm.gray)
ax1.set_title('Input image')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()

# cv.imshow("img", img)
# cv.waitKey(0)
# cv.destroyAllWindows()
~~~

### binary_shape based object detecting

1. 灰度图， 二值图像的转换，滤波处理噪声，对象划分，寻找二值轮廓，进行标注

   ~~~ python 
   import cv2
   import numpy as np
   src = cv2.VideoCapture("D:/python lib/datasets/KTH_boxing.avi")
   fourcc = cv2.VideoWriter_fourcc(*"DIVX")
   out = cv2.VideoWriter("thresh_out.avi", fourcc, 20.0, (160, 120))
   
   
   def cap_camera(name="video", dir = src):  # 视频获取
       if dir.isOpened():
           opened, frame = dir.read()
       else:
           opened = False
   
   
       while True:
           cap, frame = dir.read()
           # 图像处理  1.基于轮廓的对象检测
           frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
           ret, thresh = cv2.threshold(frame_gray, 150, 255, cv2.THRESH_BINARY)
           # noise processing 1. dilate -> erosion
           kernel = np.ones((3,3), np.uint8)
           median_blur = cv2.medianBlur(thresh, 3)  # median blur
           dilate = cv2.dilate(thresh, kernel, iterations=1)
           erosion = cv2.erode(dilate, kernel, iterations=2)
           contous, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
           for c in contous:
               perimeter = cv2.arcLength(c, True)
               if perimeter > 150 and perimeter < 200:  # set-up parameter to decrease noise
                   x, y, w, h = cv2.boundingRect(c)
                   cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
           cv2.imshow("name", frame)
           cv2.imshow("thresh", erosion)
           out.write(frame)
   
           if cv2.waitKey(50) & 0xff == 27:
               break
       dir.release()
       cv2.destroyAllWindows()
   if __name__ == "__main__":
       cap_camera()  # 获取视频, 处理图像
   ~~~

   ### HAR_SVM （silhouette，shape, hog, svm）

   ~~~python
   import cv2
   import numpy as np
   from skimage.feature import hog
   from skimage import data, exposure
   
   src = cv2.VideoCapture("D:/python lib/datasets/KTH_running.avi")
   fourcc = cv2.VideoWriter_fourcc(*"DIVX")
   out = cv2.VideoWriter("thresh_out.avi", fourcc, 20.0, (160, 120))
   
   
   # silhouette detecting and circumscribe
   def sil_de(frames, frame):
       contous, hierarchy = cv2.findContours(frames, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
       for c in contous:
           perimeter = cv2.arcLength(c, True)
           if 150 < perimeter < 200:  # set-up parameter to decrease noise
               x, y, w, h = cv2.boundingRect(c)
               bound = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
               # print(bound)
               return bound
   
   
   def hog_pro(frame_local):
       if frame_local is None:
           print("not get detecting area...")
       else:
           frame_local = cv2.cvtColor(frame_local, cv2.COLOR_BGR2GRAY)
           np.set_printoptions(threshold=np.inf)
           # frame = np.float(bound_array)/255.0  # contrast-normalized
           fd, hog_feature = hog(frame_local, orientations=8, pixels_per_cell=(16, 16),
                             cells_per_block=(1, 1), visualize=True, multichannel=False)
           print(hog_feature)
           return hog_feature
   
   
   # capture video, pre-processing, silhouette detecting ,bounding,
   def cap_camera(name="video", dir = src):
       if dir.isOpened():
           opened, frame = dir.read()
       else:
           opened = False
       while True:
           cap, frame = dir.read()
           frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
           ret, thresh = cv2.threshold(frame_gray, 150, 255, cv2.THRESH_BINARY)
           # noise processing 1. median_blur dilate -> erosion
           kernel = np.ones((3, 3), np.uint8)
           median_blur = cv2.medianBlur(thresh, 3)  # median blur
           dilate = cv2.dilate(median_blur, kernel, iterations=1)
           pre_done = cv2.erode(dilate, kernel, iterations=2)
           frame_local = sil_de(pre_done, frame)  # def detecting and circumscribe
           vector_fea = hog_pro(frame_local)
           #write_fea(vector_fea)
           cv2.imshow("name", frame)
           # out.write(frame)  # output
   
           if cv2.waitKey(50) & 0xff == 27:
               break
       dir.release()
       cv2.destroyAllWindows()
   
   
   def write_fea(fea):
       f = open("D:/python lib/datasets/feature.txt", mode="w", encoding="gbk")
       if len(fea) is None:
           print("no feature to write..")
       else:
           for i in range(len(fea)):
               for j in range(len(fea[i])):
                   f.write(str(fea[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
                   f.write("\t")  # 相当于Tab一下，换一个单元格
               f.write("\n")  # 写完一行立马换行
           f.close()
   if __name__ == "__main__":
       cap_camera()
   ~~~
   
   ### batch processing images in a file 
   
   ~~~python
   import os
   import numpy as np
   import cv2 as cv
   """ 
   batch to process images in a file 
   """
   cat = []
   
   
   def outPut_img(img):
       cv.imshow("image", img)
       k = cv.waitKey(0)
       if k == 27:
           cv.destroyAllWindows()
   
   def ReFileName(dirPath):
       for file in os.listdir(dirPath):
           if os.path.isfile(os.path.join(dirPath, file)) == True:
               c = os.path.basename(file)
               name = dirPath + "\\" + c
               img = cv.imread(name)
               img = cv.resize(img, (100,100))
               outPut_img(img)
   
               cat.append(img)
   
   
   dirPath = r"F:\dataset\myvideo"
   ReFileName(dirPath)
   cat = np.array(cat)
   print("输入x.shape:", cat.shape)
   label = [1 for i in range(len(cat))]
   label = np.array(label)
   print("输入y.shape:", label.shape)
   
   
   
   ~~~
   
   
   
   



