## algorithms(趣味算法_陈小玉& 算法导论)

 ### 算法入门

~~~python\
**算法** 就是定义良好的计算过程，我们也可以把算法看做一个工具，用来解决具有良好规格说明的计算问题。它取一个或者一组值作为输入， 并且产生出一个或者多个值作为输出。 算法就是一系列计算的步骤， 用来将输入数据转换成输出结果。
**数据结构**是存储和组织数据数据的一种方式。 以便于对数据进行访问和修改。 了解数据结构的长处和局限性相当重要。
~~~

### 插入排序(insertion-sort)

~~~c++
插入排序是对少量元素进行排序的有效算法,插入排序使用的是增量方法，算法的运行取决于数组排序程度。
for (i = 0; i<n ; i++)
{
    insert >> x;
    for (j=i-1;j>=0;j--)
    {
        if (a[j]>=x)
        {
            a[j+1] = a[j];
        }else {
            break;
        }
    }
}
a[j+1]= x;

~~~

### 合并排序

~~~python
~~~



思维引导： 

​	-1 1 -1 1  ..... n  

~~~python
1.
sum = 0 
n = 10
for i in range(n):
    sum += (-1)**i
    i += 1
print(sum)

2.sum = 0 
n = 10
if (n%2 == 0):
    sum = 0
else: 
    sum = -1
print(sum)
~~~



### Greedy algorithm

#### bubbling sort

~~~ python 
# to understand greedy_algorithm . bubble sort
lis = [10, 15, 5, 2, 8, 7, 35, 6, 4, 9, 1]  # data
tem = 0  # support space
#  start
if len(lis) > 0:  # judge list is null ?
    for i in range(len(lis)):
        for j in range(len(lis)-1-i):  # -i for  not match passed num
            if lis[j] > lis[j+1]:
                tem = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = tem
            j += 1
        i += 1
# end
print(lis)
~~~

#### 加勒比海盗船_最优装载问题

~~~python

~~~



