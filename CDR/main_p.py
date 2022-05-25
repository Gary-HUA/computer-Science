import cv2 as cv
import numpy as np
from imutils import contours
import myutils
import argparse


# 图像信息显示
def cv_show(name, image):
    cv.imshow(name, image)
    cv.waitKey(0)
    cv.destroyAllWindows() 


# 图像 和 模板的读入
img = cv.imread("E:/python_OpenCV lib/card.jpg")
template = cv.imread("E:/python_OpenCV lib/temp.jpg")

# 模板处理
gray_tem = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
ret, bi_tem = cv.threshold(gray_tem, 127, 255, cv.THRESH_BINARY)
# cv_show("res", bi_tem)  # 展示模板的二值图像
# 轮廓检测(outside)
bt = bi_tem.copy()
contours, hierarchy = cv.findContours(bt, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# draw contours
contours_res = cv.drawContours(template, contours, -1, (0, 255, 0), 3)  # 在二值图上得到, 需要画在原图上,
# cv_show("contours_res", contours_res)
print(np.array(contours).shape)

# 对轮廓进行了排序从左到右

contours = myutils.sort_contours(contours, method="left-to-right")[0]
digits = {}  # 存模板的数字
print(digits)

# 遍历轮廓, 外接矩形

for (i, c) in enumerate(contours):  # c 是每个轮廓的终点坐标 讲一个可遍历的数据对象组合成一个索引序列
    (x, y, w, h) = cv.boundingRect(c)  # 计算外接矩形, resize 成合适大小
    # 扣模板
    roi = gray_tem[y:y+h, x:x+w]  # 每个roi对应一个数字
    roi = cv.resize(roi, (57, 85))  # 模板拆分数字
    digits[i] = roi  # 每个数字对应一个模板

# image of detecting
# 初始化卷积核
rectKernel = cv.getStructuringElement(cv.MORPH_RECT, (9, 3))  #
sqKernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  #
# read image
# cv_show("ori_img", img)
# pre-processing image
img = myutils.resize(img, width=300)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv_show("gray_img", gray_img)
# top_hat operation  把轮廓高亮处显示出来 文字等作为毛刺突出
top_hat = cv.morphologyEx(gray_img, cv.MORPH_TOPHAT, rectKernel)
# cv_show("top_hat", top_hat)
# sobel 算子 进行轮廓计算
gradX = cv.Sobel(top_hat, ddepth=cv.CV_32F, dx=1, dy=0, ksize=-1)  # ksize=-1 相当于用3*3的模板
# 对X方向进行归一化  只对x方向进行轮廓计算是因为 从X方向获得我们要的文字信息
gradX = np.absolute(gradX)  # calculate |gradx|
(minVal, maxVal) = (np.min(gradX), np.max(gradX))
gradX = (255*((gradX-minVal)/(maxVal-minVal)))
gradX = gradX.astype("uint8")
print(np.array(gradX).shape)
# cv_show("input_sobel_gradx", gradX)
# 通过闭操作对数字进行处理 四个数字为一组进行膨胀 其他的腐蚀掉
gradX = cv.morphologyEx(gradX, cv.MORPH_CLOSE, rectKernel)

# cv_show("input_close_gradx", gradX)
# 阈值操作, THRESH_OTSU 会自动找到合适的阈值, 通过阈值处理把没用的信息进行过滤.只留下明显的文字图像信息
thresh = cv.threshold(gradX, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
# cv_show("input_thresh", thresh)
# 再来一个闭操作
thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, sqKernel)  # 填补空洞
# cv_show("input_thresh_close_again", thresh)
# 计算轮廓
thresh_contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
tc = thresh_contours
ic = img.copy()
cv.drawContours(ic, tc, -1, (0, 255, 0), 3)
# cv_show("input_contours", ic)
locs = []
# 遍历轮廓
for (i, c) in enumerate(tc):
    # calculate sqrec
    (x, y, w, h) = cv.boundingRect(c)
    ar = w/float(h)
    # 选择符合的区域进行选择
    if ar > 2.5 and ar < 4.0:
        if (w > 40 and w <55) and (h>10 and h < 20):
            locs.append((x, y, w, h))

# 讲符合的轮廓进行左到右的排序
locs = sorted(locs, key=lambda x:x[0])
output = []
# 遍历每一个轮廓中的数字
for (i, (gx, gy, gw, gh)) in enumerate(locs):
    groupOutput = []

    # 根据坐标提取每一组
    group = gray_img[gy-5:gy+gh+5, gx-5:gx+gw+5]
    # cv_show("group", group)
    # 预处理
    group = cv.threshold(group, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    # cv_show("group_pro", group)
    # 计算每一组的轮廓
    digitCnts, hierarchy = cv.findContours(group.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    digitCnts = myutils.sort_contours(digitCnts, method="left-to-right")[0]

    for c in digitCnts:
        z = 0
        (x, y, w, h) = cv.boundingRect(c)
        roi = group[y:y+h, x:x+w]
        roi = cv.resize(roi, (57, 85))
        # cv_show("roi", roi)
        # 计算匹配得分
        score = []
        for (digit, digitROI) in digits.items():
            res = cv.matchTemplate(roi, digitROI, cv.TM_CCOEFF)
            max_score = cv.minMaxLoc(res)[1]
            score.append(max_score)
        print("score", score)
        groupOutput.append(str(np.argmax(score)))
        z = z+1
    # 画
    cv.rectangle(img, (gx-5, gy-5), (gx+gw+5, gy+gh+5), (0, 255, 0), 2)
    cv.putText(img, "".join(groupOutput), (gx, gy-15), cv.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)
    # 得到结果
    output.extend(groupOutput)
    print("groupOutput:", groupOutput)
    # cv_show("res", img)
