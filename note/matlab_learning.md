## matlab  learning:

### 矩阵和数组的创建: 

~~~ matlab 

a = [1 2 3 4]  % 逗号或者空格 隔开
b = [1234;5678;9021] % 二维矩阵 3*4
z = zeros/ones/rand/randn/(m*n) % 由0 1 或者均匀随机元素/正态分布随机元素成的M*N的矩阵
% 矩阵的运算 +- 是每一个元素进行运算 * 是 (a*b)(c*d) 前提条件是b=c列元素和行元素一致,然后进行行列的内积得出a*d的矩阵 diag/sum(matrix)得出主对角线和
a' % 转置矩阵 行元素变成列元素
a.^3 % 计算矩阵各个元素的次方
A = [a,a] % 串联 连接多个数组 构成更大的数组.逗号是水平串联,分号是垂直串联 前提是行/列数相同
% 复数

~~~

### 索引

~~~ matlab


~~~

### 工作区变量:

~~~ matlab

存储的是当前计算或数据文件中导入的变量 who  可以查看工作区内容,在程序退出后,工作区的变量不会保留, 可以使用save myfile.mat 进行保存, 
clear 清除工作区变量, 
使用load 进行加载mat文件中的变量到工作区 load myfile.mat
~~~

### 文本和字符串

~~~matlab

t='hello,world'
t="hello,""W""orld" % 他们数据类型是String, 
% 使用+进行字符串的拼接
A=["a","bb","ccc"] % 数据类型是数组 使用strlength(A)求数据中每个字符串的长度 ans=1 2 3
seq='abcdefg' % 字符数据
seq(4) % 'd'
seq2 = [seq, 'abcdefg'] % 字符数据的串联
~~~

### 调用函数

~~~matlab
A = [1 3 5]
max(A) % 求A中的最大值
~~~

### 二维/三维图

~~~matlab

x = 0:pi/100:2*pi
y = sin(x)
plot(x,y) % 正弦函数线图, 第三个参数可以添加颜色和类型 'r--'
% 标记轴和标题
xlabel('x')
ylabel('y')
title('plot')
% hold on  往当前图添加绘图.知道 hold off 
%
% 
[x,y]=meshgrid(-2:.2:2) % 网格
z = x.*exp(-x.^2-y.^2) 
surf(x,y,z)
subplot(2,2,1):mesh(x);title('x')  % 子图 在同一窗口绘制多个图m*n 第i个
~~~

### 编程和脚本:

~~~matlab
edit mysphere % 创建脚本
edit newfile.mlx # 创建实时脚本
% 循环 for/while 
N = 100;
f(1) = 1;
f(2) = 1;

for n = 3:N
    f(n) = f(n-1) + f(n-2);
end
f(1:10)
% 判断if/switch
num = randi(100)
if num < 34
   sz = 'low'
elseif num < 67
   sz = 'medium'
else
   sz = 'high'
end
~~~

### 帮助和文档

~~~ matlab
doc mean % 在单独的窗口中打开函数文档
mean( % 函数提示
help mean % 帮助
% MATLAB 使用传统的十进制记数法以及可选的小数点和前导加号或减号来表示数字。科学记数法使用字母 e 来指定 10 次方的缩放因子。虚数使用 i 或 j 作为后缀
+加法
-减法
.*逐元素乘法
./逐元素除法
.\逐元素左除
.^逐元素幂
.' 非共轭数组转置
pi 3.14159265...

i 虚数单位 G -1^2
j与 i 相同

eps 浮点相对精度 ε=2^−52

realmin最小浮点数 2^−1022

realmax最大浮点数 (2−ε)2^1023
Inf无穷大
NaN非数字
~~~

### 输入命令:

~~~matlab
% format 函数控制所显示的值的数值格式。此函数仅影响数字显示方式，而不会影响 MATLAB® 软件如何计算或保存数字
x = [4/3 1.2345e-6]
format short       1.3333  0.0000
format long        1.33333333333333 0.00000123450000
format e/g/bank/rat/hex/long e/ long g/
% 如果您在仅键入语句后按 Return 或 Enter，MATLAB 会在屏幕上自动显示结果。但是，如果使用分号结束行，MATLAB 会执行计算，但不会显示任何输出
% 如果语句无法容纳在一行中，请使用省略号（三个句点）...，后跟 Return 或 Enter 以指示该语句在下一行继续
% 删除行和列
a(:,2) = [] %删除矩阵的第二列
~~~

### 索引

~~~matlab
~~~

### GMM ,grayscale, binarize, class_translate,

~~~matlab
videoSource = VideoReader('E:\dataset\myself_video\new4.mp4');
%GMM
detector = vision.ForegroundDetector(...
       'NumTrainingFrames', 5, ...
       'InitialVariance', 30*30);
blob = vision.BlobAnalysis(...
       'CentroidOutputPort', false, 'AreaOutputPort', false, ...
       'BoundingBoxOutputPort', true, ...
       'MinimumBlobAreaSource', 'Property', 'MinimumBlobArea', 800,'MaximumCount',1);
shapeInserter = vision.ShapeInserter('BorderColor','Custom');
while hasFrame(videoSource)
     frame  = readFrame(videoSource);
     frameGray = rgb2gray(frame);% garyscale
     % binary image
     binaryimg = imbinarize(frameGray,'adaptive','ForegroundPolarity','dark','Sensitivity',0.2);% bright/dark as foreground
     binaryimg = cast(binaryimg,'double');% translate class 
     fgMask = detector(frame);
     bbox   = blob(fgMask);
     out = insertShape(frame,'Rectangle',bbox,'color','green');
     % out    = shapeInserter(frame,bbox);
     subplot(2,2,1),imshow(frame),title('rgb_frame');
     subplot(2,2,2),imshow(out),title('shape');
     subplot(2,2,3),imshow(binaryimg),title('frameGray');
     %subplot(2,2,4),imshow(),title('');
     % videoPlayer(out);
     pause(0.1);
end
~~~







