### Deep Learning <<深度学习入门, 基于python 的理论和实现>>

#### 第二章:   Numpy 

~~~python 
"""
the numpy lib using
list and matrix calculating.
"""
import numpy as np

x = np.array([1.0, 2.0 ,3.0])
print(x)  # [1. 2. 3.]
print(type(x))  # <class 'numpy.ndarray'>


# numpy operator
y = np.array([5 , 6, 7])
result = x+y
print(result)  # [ 6.  8. 10.]

result_2 = x * y # 对应位置相乘.  element-wise product.
print(result_2)  #　[ 5. 12. 21.]

# 数组和标量的运算, 我们叫他 广播
z = 2.0   # sigle value is called 标量
result_3 = x /z  #
print(result_3)  # [0.5 1.  1.5]


#  multi-dimension array

a = np.array([[1,2,3], [4, 5, 6]])
b = np.array([[2,2],[3,3],[4,4]])
print(a)  # [[1 2 3]  [4 5 6]]
print(b)  # [[2 2] [3 3] [4 4]]
print(a.shape)  # (2, 3)
print(b.shape)  # (3, 2)
print(a.dtype) # int32
# result_4 = a + b  #  not working (shape)
# result_5 = a * b  # not working(shape)
result_6 = a /z  # z = 2
print(result_6)  # [[0.5 1.  1.5] [2.  2.5 3. ]]

c = np.array([[2,2,2]])  # c still as a scalars
print(c.shape)  # (1, 3)
result_7 = a * c
print(result_7)  # [[ 2  4  6] [ 8 10 12]]
"""
so due to the broadcast funtion, the difference of the array can be operated.
"""
# flatten()
result_8 = a.flatten()
print(result_8)  # [1 2 3 4 5 6]



~~~

#### 第二章: Perceptron

~~~ python
"""
The basic of the deep learning "perceptron".
"""

def And(x1, x2):
    w1, w2, theta = 0.5, 0.5 , 0.7
    temp = x1*w1 + x2*w2
    if temp > theta:
        return 1
    elif temp < theta:
        return 0


if __name__ == '__main__':
 result = And(0.1, 0.2)
 print(result)


~~~





