#  **python ：**

# 第一章：  环境搭建 

## 辅助笔记软件typore使用：

（一级标题使用# 和空格 然后输入标题）

（二级标题使用##加一个空格 然后输入二级标题 然后依次加#号 #<=6）

Ctrl+？ 可以切换源码格式；

有序序号和无序序号

减号加上空格/tab键可以出表示点；

- 减号+空格

  - 在上一步减号+空格的基础上+TAB
    - 在上一步的基础上+TAB 

  代码块  三个~符号+语言名字 然后回车

  ~~~python
  print("hello world")
  ~~~

  - `` 双波浪键 可以把内容用背景标注出来

  `你好`

  - 两个星号包括是加粗   一对星号包括是斜体

  **加粗**

  *斜体*

  - 抹除线 一对双~号包括

  ~~抹除~~

  - 表格格式

  | 姓名 | 性别 | 年龄 |
  | :--: | :--: | :--: |
  |      |      |      |
  |      |      |      |

  - 链接插入：

    [链接名]（网址域名）Ctrl 键+鼠标左键进入链接    [百度](http://www.baidu.com/)
  
    


## 软件下载和安装

1. Python安装和环境搭建

   [python官网](http://www.python.org) 进行python解释器的下载软件 last version 3.8.3和python2.7 共存使用；

   python3.8安装和环境配置之后，对python文件夹中的EXE执行文件复制一个叫python2.exe的快捷路径；然后配置path 在cmd中验证；

   安装之后的环境变量配置；

   在系统环境变量中设置中选择path 指向python3和python2的路径；

   

2. pycharm安装和环境搭建

   下载地址:[pycharm官网地址;](http://www.jetbrains.com)

## 第一个python程序：


~~~python
# -*- coding: UTF-8 -*-    --头文件 文件脚本必须带上头文件
print("hello world")
~~~

然后在终端 管理员模式下输入 python空格+py代码文件路径;

Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>python C:\Users\Administrator\Desktop\python-coding.py
hello world

C:\Users\Administrator>python2 C:\Users\Administrator\Desktop\python-coding.py
hello world

C:\Users\Administrator>python C:\Users\Administrator\Desktop\python-coding.py
hello world! 世界你好!

- **--python2 不支持中文**

C:\Users\Administrator>python2 C:\Users\Administrator\Desktop\python-coding.py
hello world! 涓栫晫浣犲ソ!   

C:\Users\Administrator>

##  python 简介：

在1989年圣诞节期间，吉多范罗苏姆为了打发圣诞节 而开始编写的一个语言。Python崇尚优美，清晰，简单，是一个优秀并被广泛使用的语言。

### Python是什么编程语言：

编程语言主要从以下几个角度分类：编译型和解释型语言，静态语言和动态语言，强类型定义语言和弱类型定义语言。

Python是解释型语言。

编译型：

​		优点:编译器一般会有预编译的过程对代码进行优化，因为编译只做一次，运行时不需要编译，所以编译型语言的程序执行效率比较高，可以脱离语言环境独立运行。

​		缺点：编译之后如果需要修改就需要整个模块重新编译。编译的时候根据对应的运行环境生成机器码，不同的操作系统之间移植会有问题，

解释型：

​		优点：有良好的平台兼容性，在任何环境中都可以运行，前提是安装了解释器（虚拟机），灵活，修改代码可以直接修改，可以快速部署，不用停机维护；

​		缺点：每次运行都需要解释一遍，性能上不如编译型语言。

动态类型语言：

​		动态类型语言是指在运行期间才去做数据类型检查的语言，也就是说，

在用动态类型的语言编程时，永远也不用给任何变量指定数据类型，该语言会在你第一次赋值给变量时，

在内部将数据类型记录下来。Python和Ruby就是一种典型的动态类型语言，其他的各种脚本语言如

VBScript也多少属于动态类型语言。

静态类型语言：

​		静态类型语言与动态类型语言刚好相反，它的数据类型是在编译其间检查的，

也就是说在写程序时要声明所有变量的数据类型，C/C++是静态类型语言的典型代表，

其他的静态类型语言还有C#、JAVA等。



强类型定义语言：

​	强制数据类型定义的语言。也就是说，一旦一个变量被指定了某个数据类型，如果不经过强制转换，那么它就永远是这个数据类型了。

举个例子：如果你定义了一个整型变量a,那么程序根本不可能将a当作字符串类型处理。

强类型定义语言是类型安全的语言。

弱类型定义语言：

​	数据类型可以被忽略的语言。它与强类型定义语言相反, 一个变量可以赋不同数据类型的值。强类型定义语言在速度上可能略逊色于弱类型定义语言，但是强类型定义语言带来的严谨性能够有效的避 免许多错误。另外,“这门语言是不是动态语言”与“这门语言是否类型安全”之间是完全没有联系的！

例如：Python是动态语言，是强类型定义语言（类型安全的语言）; VBScript是动态语言，是弱类型定义语言（类型不安全的语言）; JAVA是静态语言，是强类型定义语言（类型安全的语言）。

由上对于语言的不同类型定义我们得出一个结论：

​			Python是一门动态解释性的弱类型定义语言。

python 主要用于：网络开发，软件开发，数学，系统脚本等；

# 第二章：python基础语法

## 注释  python 中注释是#空格+注释内容；

单行注释  # 

多行注释 ”“”/'''开头结尾 支持换行；

选中集体注释 Ctrl+？

2. 变量：将程序中运行的一些临时数据存储下来；

2. 常量：配置文件中使用；

   ~~~python
   # 注释  输出
   print("hello world")
   ~~~

   python 2和python3的版本问题；

   ~~~python
   python2：print()跟不跟括号可以判断使用的python2还是3；
   # python2：使用ASCII编码 不能对中文进行识别
   print("你好世界")
   --SyntaxError: Non-ASCII character 
   对编码进行declare 可以进行中文输出
   # coding:utf-8
   print 123
   print 'abc'
   print '你好'
   print ("你好nn")
   --
   123
   abc
   你好
   你好nn
   # python3: 使用UTF-8 支持中文 可以直接进行中文的输出；
   print(123)
   print("abc")
   print("你好世界！")
   --
   123
   abc
   你好世界
   ~~~

   ~~~python
   # 变量：sum=2+8  sum是变量名，= 赋值运算符 2+8变量值；
   print(2+8)
   sum=2+8
   print(sum)
   print("sum=",sum)
   ~~~

   ## 命名规则：

   数字，字母，下划线 组成；

   不能以数字开

   不能使用关键字

   不建议使用中文和拼音

   变量名区分大小写

   变量名具有意义 见名知意 驼峰体/字母之间下划线；

   变量名全部大写就是常量；

## 程序交互：input 输入，获取用户信息。

~~~python 
user_name=input("enter user_name:")  # 输入账户名
password=input("enter user_pw")  # 输入密码
print(user_name)  # 输出账户名
print(password)  # 输出密码
~~~

## 数据类型：

文字类型：str

数值类型：int ,float ,complex

序列类型：list,tuple,range

映射类型：dict

集合类型：set frozenset

布尔类型：bool

二进制类型：bytes，bytearray, memoryview

1. 字符串 : str   在python中，只要是引号（双单）引起来的就是字符串，字符串就是不可变数据类型（就是在内存中不可原地修改，修改会重新指向空间）；

   字符串 表示Unicode字符的字节数组，方括号可以用于访问字符串的元素（就是下标）

   ~~~python
   a="hello"
   b="world"
   print(a+b)  # str 的拼接
   print(a*4)  # str的倍输出
   --
   helloworld
   hellohellohellohello
   ~~~

   

2. 整型： int 

   Python2中数据量比较大的话>64**5就有long 类型，Python3中所有的整数都是int类型， Python3中不存在long数据类型。

3. 布尔值： bool

   真假  True 1  ; False 0 ;

4. 数据转换：

   ~~~python
   # 字符串转化成数字
   a =int("123")
   b =str(123)
   print(a)
   print(b)
   print(a+4)  # 这里把字符串转换成了数字 进行运算得到127
   print(b+"4")  # 这里b是字符串 不能进行算术运算。
   --
   123
   123
   127
   1234
   # 转换数据类型
   num=input("请输入数字：")
   print(int(num)+10)
   --
   请输入数字：10
   20
   ~~~

   

5. 查看数据类型

   ~~~python
   # 查看数据类型
   num=10
   print(type(num))
   --
   <class 'int'>
   ~~~

   在python3中input获取的数据类型是str型

   ~~~python
   num=input("输入数字:")
   print(num)
   print(type(num))
   --
   输入数字5
   5
   <class 'str'>
   #解决方法：类型转换；
   num=input("输入数字")
   print(int(num)+10)
   ~~~

   Python的数据类型2：

   1. 列表： 类似于java之中的数组。可以存放不同的数据类型，列表相比较于字符串，可以存储更多数据类型，还可以存储大量数据，列表是有序的，有索引值，可切片，方便取值。
   
      ~~~python
      #  列表  类似于java等语言的数组 ；
      lis = ["gary", 123456, 'true', "%^$*#*"]
      print(lis)  # ['gary', 123456, 'true', '%^$*#*']
      print(lis[0])
      print(lis[1])
      # 修改列表：
      lis[2] = "false"
      print(lis)
      # 列表的切片：
      print(lis[0:3])  # ['gary', 123456, 'false']
      # 列表的增删改查：
      # 列表的追加
      print(lis)
      lis.append("gary_hua")  # 列表的结尾追加；
      print(lis)
      # 列表的插入
      lis.insert(2, "harry")  # 指定位置插入 ['gary', 123456, 'harry', 'false', '%^$*#*', 'gary_hua']
      print(lis)
      # 迭代添加：
      lis.extend(["tom", "jerry", "happy"])  # 迭代添加是往列表中添加多个元素，用逗号分隔开的；简单说就是两个列表的并集
      print(lis)
      # 列表的删除：pop 通过下标删除元素；
      lis.pop(4)  # 删除了下标是4的元素；pop以下标作为参数进行删除,remove以列表元素作为参数
      print(lis)
      # 通过元素内容删除：
      lis.remove("tom")  # 元素是tom的被删除；
      # clear 清空：
      lis.clear()  # 清空列表中的所有元素 []
      print(lis)
      # 列表的修改,索引切片修改；
      lis = ["gary", "tom", "jerry"]
      lis[1] = "happy"  # 下标指向，重新指向新内存
      print(lis)  # ['gary', 'happy', 'jerry']
      # 查询：列表是一个迭代对象，可以进行for循环
      for i in lis:
          print(i)  # 以字符串的形式把每一个元素打出；
      #  列表的嵌套：
      print((lis[2][4]))  # y
      ~~~
   
      元组 tuple：对于容器类型的list 无论谁都可以进行修改，重要的数据放在其中是不安全的，所以我们需要一个只能查看而不能修改的数据类型 就是元祖。
   
      就是将一些非常重要的不可让人改动的数据放在元祖中，配置文件中的不想让人修改的单个变量使用常量,如果是多个不想让人修改的就是用元组来存储
   
      俗称不可变列表，只读列表，基本数据类型之一；
   
      ~~~python
      tu = ("gary", "tom", "12345%")
      print(tu)
      print(tu[1])
      # traverse
      for i in tu:
          print(i)
      print(tu[0:2])
      #  尝试更改：
      # tu[1] = "jack"  #  TypeError: 'tuple' object does not support item assignment
      # 元组嵌套：
      tupp = ("gary", "tom", ("tom", "and",  "jerry"))
      print(tupp[2][1])   # and
      tup = ("gary",)  # 仅仅只有一个元素的元组，需要加逗号 否则就是一个字符串了
      print(tup)
      ~~~
   
      Rang: 包围，成环形；
   
      ~~~python
      rang(0,6,2) # 参数分别是 范围的起始位置，结束位置，步长
      print(list(range(0, 5)))  # [0, 1, 2, 3, 4]
      print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
      ~~~
   
      字典：列表可以存储大量的数据类型，但是只能按照顺序存储，数据之间的关联性不强。所以我们需要引入一种容器型的数据类型，”dict字典“
   
      字典是Python中唯一的一个映射类型，以{}括起来的键值对。key是惟一的，在保存的时候根据key通过hash算法计算出内存地址，然后将key_value保存在这个地址中。key值必须是可以hash的就是意味着不可变，value可以存储任意数据类型。
   
      语法：{"key1":1,"key2":2} 
   
      ~~~python
       #  list , dict , set 是可变的 不能作为key
       dic = {123: 123, "name": "name", "&^*": "dfdj*&", }  # 可以作为key的数据类型 int, str, tuple, bool
       print(dic[123], dic["name"], dic["&^*"])  # 123 name dfdj*& dict保存的数据不是按照顺序保存的，暗战hash表 不是连续的，所以不能进行切片，只能通过key来获取dic的数据
       # 字典的增删改查
       # 增：
       dic = {}
       dic["name"] = "gary"
       dic["age"] = 20
       print(dic)  # {'name': 'gary', 'age': 20}
       dic["name"] = "tom"  # 测试key值是不是要唯一要求；可以使用，但是内容被替换
       print(dic)
       # 设置默认值：
       de = dic.setdefault("gary", "student")
       print(de)  # 默认设置显示的是内容； student
       print(dic)  # dic 是字典的键值对， {'name': 'tom', 'age': 20, 'gary': 'student'}
       #  删除：
       print(dic.pop("gary"))  # 以key来删除，返回值是删除的值； student
       print(dic.popitem())  # 随机删除 ，python 3.6 以后删除最后一个，返回结果是删除项 ('age', 20)
       dic.clear()  # 清空；
       print(dic)  # {}
       # 改：
      dic = {"你好": "gar", 21: "海鸟"}
      dic[21] = "海鸥"  # 如果要修改的key是字典中的 那么就是修改内容，没有就是添加；
      dic[22] = "海燕"
      print(dic)  # {'你好': 'gar', 21: '海鸥'，22: '海燕'}
      dic.update({21: "苍鹰"})  # 字典中没有键值对就是添加，有事修改内容；
      print(dic)
      # 查 ：通过key查到对应的内容；
      print(dic.get(21))  # 苍鹰
      print(dic.get("jjiu"))  # None  查找没有的内容
      # 其他操作
   dic = {"name": "gary", 123: "harry" }
      key_list = dic.keys()  # 获取字典中的key值
   print(key_list)  # dict_keys(['name', 123])
      print(dic.values())  # dict_values(['gary', 'harry']) 获取字典的值
      values_list = dic.items()  # 获取字典中的键值对；
      print(values_list)  # dict_items([('name', 'gary'), (123, 'harry')])
      ~~~
   
   # 循环打印字典的键；
   
   ~~~python 
      for i in dic:
          print(i)  # name  123
      for i in dic.keys():
          print(i)  # name 123
   ~~~
   
      # 循环打印字典中的值；
   
   ~~~python 
   	for i in dic.items():  # 也是循环打印的键值对（元组形式的键值对）
          print(i)   # ('name', 'gary')  (123, 'harry')
      for i in dic.values():
          print(i)    # gary harry
     字典的嵌套;
      dic = {"name": "gary", "child": [{"name": "tom", "age": 5}], "daughters": [{"name": "jerry", "age": 3}], "boy": [{"name": "happy", "age": 12 , "name":"tomi","age":2}]}
      for k, v in dic.items():
          print(k)
          print(v)
      print(dic["daughters"][0])   # daughter [{'name': 'jerry', 'age': 3}]
      print(dic["daughters"][0]["name"])  # jerry
   
   print(dic["boy"])  # {'name': 'tomi', 'age': 2}   键值对的KEY 不能完全一样,一样就是覆盖了;
   ~~~
   
   解构：我们可以通过解构将内容分别赋值到变量之中，快速的将值使用；
   
      ~~~python
      a, b, c = ("gary", "tom", "1234")  # 解构就是一次给多个变量初始化值；
      print(a+b)  # gary tom
      print(b+c)  # tom 1234  这里的1234是字符串
      a, b, c = ("gary", "tom", "1234")  # 解构就是一次给多个变量初始化值；
      print(a+b)  # garytom
      print(b+c)  # tom1234  这里的1234是字符串
      # 循环字典 通过解构分别获取键，值
      dic = {123: "gary", "name": "tom"}
      for k, v in dic.items():
          print("key is:", k)
          print("values is:", v) # key 的值和values的值成对循环遍历出来
      ~~~
   
   集合(set):集合也是我们Python中的一个数据类型,我们一般只用它自身带的特性,其余操作很少使用;
   
   集合以{}的形式展示,集合是一个没有值的字典,集合中的元素是不可变的而且还是唯一的,我们利用他的唯一性
   
   ~~~python
   # 集合:set{}
   lst = [1, 5, 3, 8, 52, 6, 2, 4, 1, 5, 6, 3]
   print(set(lst))  # {1, 2, 3, 4, 5, 6, 8, 52}  列表转成集合,自动去重形成集合的唯一性,
   lst_result = list(set(lst))  # 把集合转换成列表;
   print(lst_result)  # [1, 2, 3, 4, 5, 6, 8, 52]
   # 验证集合的不可变;
   lst = [1, 5, 3, 8, 52, 6, 2, 4, 1, 5, 6, 3]
   result = set(lst)
   print(result)  # {1, 2, 3, 4, 5, 6, 8, 52}
   result[1] = "gary"
   print(result)  # TypeError: 'set' object does not support item assignment
   # 集合的增删改查: 集合增加到了第二位;
   # 集合的添加:
   lst = {"gary", "tom", "jerry"}
   lst.add("harry")
   print(lst)  # {'gary', 'harry', 'jerry', 'tom'}
   lst.add("harry")
   print(lst)  # {'gary', 'harry', 'jerry', 'tom'} 集合的不可重复性,
   lst.update("ti")  # {'tom', 'o', 'i', 't', 'm', 'harry', 'gary', 'jerry'}迭代更新,把指定的字符串无序拆分为了集合的每一个元素;
   lst.update(["dj", "df"])  # 列表会以单个元素为单位进行插入,用以在集合中添加字符串;{'df', 't', 'tom', 'jerry', 'harry', 'gary', 'i', 'dj'}
   print(lst)
   # 集合的删除:
   lst = {"gary", "tom", "jerry"}
   print(lst.pop())  # 随机弹出一个元素;
   # print(lst.remove("tom"))  # None 直接删除,二次执行会报错,没有这个元素;
   print(lst)  # {'tom', 'gary'}
   print(lst.clear())  # 清空set集合,集合如果是空的 显示的是set() 为了和dict  "{}" 区分;
   print(lst)   # set()
   # 集合的修改;set集合中没有索引,没有办法定位元素,所以没有办法直接修改,一般我们采用先删除后添加的方式进行修改;
   lst = {"gary", "tom", "jerry"}
   print(lst.remove("jerry"))
   print(lst.add("jerry_reset"))
   print(lst)  # {'gary', 'tom', 'jerry_reset'}
   # 集合的查询:set是个可迭代对象,所以可以进行for循环;
   for i in lst:
       print(i)
   # 集合的常用操作;集合的交集,并集,差集,反交集,子集,超集;
   lst = {"gary", "tom", "jerry"}
   lst_2 ={"dfj", "dfd", "tom"}
   print(lst & lst_2)  # {'tom'} 交集
   print(lst | lst_2)  # {'gary', 'dfd', 'tom', 'jerry', 'dfj'} 并集
   print(lst - lst_2)  # {'jerry', 'gary'} 差集 从A中删除在B中有的元素
   print(lst ^ lst_2)  # {'dfd', 'gary', 'dfj', 'jerry'} 反交集
   # print(lst.symmetric_difference(lst_2))   # {'dfd', 'gary', 'dfj', 'jerry'} 反交集
   print(lst < lst_2)  # false B是否是A的子集 B中的所有元素是否都在A中存在;子集
   # print(lst.issubset(lst_2))  # false
   print(lst > lst_2)  # false  超集 A 是否是B的子集;
   # -- 集合本身是可以改变的,不可hash的 我们可以使用frozenset来保存数据,frozenset是不可变的,也就是改成了可hash的数据类型;
   lst = frozenset(["gary", "tom", "jerry"])
   dic = {lst: "name"}
   print(dic)  # {frozenset({'jerry', 'gary', 'tom'}): 'name'}
   ~~~
   
## 数据类型的补充和总结:

~~~Python
# 首字母大写:
name = "gary world"
print(name.capitalize())  # Gary world
# 每个单词的首字母大写:
print(name.title())  # Gary World
# 大小写反转:
print(name.swapcase())  # GARY WORLD
# 统计:
print(name.count("r"))  # 2  必须有参数(查找的字符) at last one
# 查找:
print(name.find("a"))  # 1 查找的数据不存在返回-1
print(name.index("o"))  # 6 查找的是字符在字符串所在位置的下标 没有结果显示substring not found;
# 居中:
print(name.center(20))  #       gary world     字符串位置后缩20
# 填充:
name = "Gary{}, {}, {}"  # 按照顺序填充:
print(name.format("_H", "Jerry", "Tom"))  # Gary_H, Jerry, Tom
name = "Gary{0}, {1}, {2}"  # 按照下标填充:
print(name.format("_H", "Jerry", "Tom"))  # Gary_H, Jerry, Tom
name = "Gary{a}, {b}, {c}"  # 按照关键字填充:
print(name.format(a="_H", b="Tom", c="Jerry"))  # Gary_H, Tom, Jerry
# 拼接:将可迭代容器转换成字符串,字典拼接的是键;可迭代容器中的元素必须是字符串类型;
lst = ["2", "3", "4", "5"]  # 列表
print('*'.join(lst))  # 2*3*4*5

tu = ("2", "3", "4", "5")  # tuple
print('*'.join(tu))  # key1*key2

dic = {"key1": 2, "key2": 4}  # 字典;
print('*'.join(dic))  # key1*key2

se = {"1", "3", "34"}  # 集合
print('*'.join(se))  # 1*34*3
# 字符 +
name1 = "tom"
name2 = "gary"
print(name1+name2)  # tomgary
print(id(name1)+id(name2))  # 82633824
# 字符 *  字符+ 和字符*都是开辟新空间
print(id(name1))  # 41705584
print(id(name1)*2)  # 83411168
#   list:
# 反转:
lst = [1, 2, 3, 4, 5]
lst.reverse()  # none 没有返回值 在lst元数据上进行了反转
print(lst)
# 排序:
lst = [1, 6, 8, 4, 5]
lst.sort()
print(lst)  # [1, 4, 5, 6, 8] 升序 有小到大
lst.sort(reverse=True)  # 降序
print(lst)  # [8, 6, 5, 4, 1]
# 查找:
lst = [1, 3, 5, 2, 8, 6, 9]
print(lst.index(1))  # 存在就返回索引下标,不存在就报错
# 统计:
lst = (1, 25, 65, 8, 9)
print(lst.count(65))  # 1
# # list +
# lst = [1,8,3,5,9]
# print(id(lst))  # 41403776
# lst1 = [2,8,5,9,7]
# print(id(lst1))  # 41271808
# print(id(lst) + id(lst1))  # 82806592
# print(id(lst + lst1))  # 41237312
# # list *
# print(lst * 2)  # [1, 8, 3, 5, 9, 1, 8, 3, 5, 9]
# print(id(lst * 2))  # 41302784  -- 和lst貌似没有关系;
# # 列表在进行乘法的时候元素都是共用的
# lst = [[]]
# new_lst = lst*2  # 开辟空间的时候*2就是开辟了一个新的有两个列表的列表
# new_lst[0].append(1)
# print(new_lst)  # [[1], [1]]
# print(new_lst.index([1]))  # 0 复制的下标一样
# print(id(lst))  # 41403200
# print(id(new_lst))  # 41404032
# tuple: +
# tu = (1)
# tu1 = (1,2)
# tu2 = (1,)
# print(tu)  # 1
# print(tu1)  # (1, 2)
# print(tu2)  # (1,)
# tu3 = tu1+tu2
# print(tu3)  # (1, 2, 1)
# print(id(tu2))
# # 列表在进行乘法的时候元素都是共用的
# print(tu1*2)  # (1, 2, 1, 2)
tu = ([],)
tu1 = tu * 5
tu1[0].append(9)
print(tu1)  # ([9], [9], [9], [9], [9])
# dict:字典定义方式:
dict(key=0,key1=1,key2=2)
# 随机删除:
dic = {"key1":"values", "key2":"values2"}
dic.popitem()  # 随机删除 最后一个删除
print(dic)  # {'key1': 'values'}
# 批量创建字典:formkeys这个是个坑,坑点就在于值是可变数据类型的时候,当第一个键对应的值进行修改了以后,其余的键对应的值也都跟着进行改变了. 如何避免坑,就是批量创建字典的时候值不能使用可变的数据类型.
dic={}
dic1=dic.fromkeys("a",[1,2])
print(dic1)
# 集合定义:
print(set("123456"))  # {'2', '4', '1', '3', '6', '5'}
# 数据类型
# # 有序:
# 数字
# 字符串
# 列表
# 元组
# # 无序:
# 字典
# 集合
# # 可变数据类型:
# 列表
# 字典
# 集合
# # 不可变数据类型:
# 字符串
# 数字
# 元组
# # 取值顺序:
# 直接取值 — 数字,布尔值,集合
# 顺序取值(索引) — 列表,元组,字符串
# 通过键取值 — 字典

# 类型转换:
list(tuple)  # 元组到列表;
tuple(list)  # 列表-元组
str.split()  # 字符串-列表
str.join(list)  #列表-字符串

~~~

- **列表**是有序且可更改的集合。允许重复的成员。
- **元组**是有序**且不可更改**的集合。允许重复的成员。
- **Set**是无序和未索引的集合。没有重复的成员。
- **字典**是无序，可变和索引的集合。没有重复的成员。

 


   ## python 2和python3的input之间的区别；

   ~~~python
   #python2:input获取的对应输入的数据类型；
   #python3:input的获取的数据类型是str；
   在python2中的raw_input 和python3的input数据类型是等价的 都是str类型；
   ~~~

## 流程控制语句if-else：

if 条件语句：

   ~~~python
num = 3
print(num)
if num > 5:  # 语法有严格位置要求，if顶位，print table之后
    print("true打桩")
print("false不打桩")
--
3
false不打桩
# if完整条件分支结构代码；
num = 3
print(num)
if num > 5:  
    print("true 打桩")
else:
    print("false 打桩")
   ~~~

~~~python
# 验证账号是否正确：
user_name = "gary_H"
if input("enter user_name:") == user_name:
    print("账号正确！")
else:
    print("账号错误！")
~~~

~~~python
# if  elif  elif ...多路分支
age = 20
input_age = int(input("enter age:"))
if age == input_age:
    print("恭喜你，猜对了！")
elif age > input_age:
    print("猜小了！")
elif age < input_age:
    print("猜大了！")
print("游戏结束！")
~~~

~~~python
# 模拟手机功能业务：
msg = """
1.查询剩余本地主动呼叫分钟
2.查询本地流量余额
3.查询全国流量余额
4.查询短信剩余条数
5.查询当前套餐
6.变更套餐
7.查询话费余额
8.查询缴费记录
请选择您要操作的功能：
"""
choose = input(msg)
if choose == "1":  # 直接和msg进行匹配 如果有一样的就是匹配到了
    print("查询剩余本地主动呼叫分钟")
elif choose == "2":
    print("查询本地流量余额")
elif choose == "3":
    print("查询全国流量余额")
elif choose == "4":
    print("查询短信剩余条数")
elif choose == "5":
    print("查询当前套餐")
elif choose == "6":
    print("变更套餐")
elif choose == "7":
    print("查询话费余额")
elif choose == "8":
    print("查询缴费记录")
else:
    print("输入有误，请重新输入：")
    --
1.查询剩余本地主动呼叫分钟
2.查询本地流量余额
3.查询全国流量余额
4.查询短信剩余条数
5.查询当前套餐
6.变更套餐
7.查询话费余额
8.查询缴费记录
请选择您要操作的功能：
12
输入有误，请重新输入：
~~~

if 嵌套：

~~~python
#  if 的嵌套：  本代码具有安全bug 有用账号可以扫描出来 密码可以试出来；
user_name = "gary"
pass_word = "123456"
if user_name == input("enter user_name"):
    if pass_word == input("enter pass_word"):
        print("登录成功！")
    else:
        print("密码不正确！请重新输入：")
else:
    print("账号不正确，请重新输入：")
 #安全bug的解决：
user_name = "gary"
pass_word = "123456"
if user_name == input("enter user_name") and pass_word == input("enter password:"):
    print("登录成功！")
else:
    print("账号或密码不正确，请重新输入：")
~~~

## while 循环：

~~~python
count = 1
while count < 11:
    print("the number is :"+str(count))  # python 的 print 和 input 都是str数据类型；
    count += 1
print("计数结束")
--
the number is :1
the number is :2
the number is :3
the number is :4
the number is :5
the number is :6
the number is :7
the number is :8
the number is :9
the number is :10
计数结束
~~~

~~~python 
# python 代码问题？？？ 怎样在while 循环中 一次判断账号和密码 然后得出success or error
user_name = "gary"
pass_word = "123456"
while user_name != input("enter the user_name:") and pass_word != input("enter the pass_word:"):
    print("error")
if pass_word == input("enter the pass_word"):
    print("success!")
else:
    print("error enter again")
-- 第二段 改进后：
user_name = "gary"
pass_word = "123456"
# flag = True
while True:
    inp_name = input("enter user_name:")
    inp_pass_w = input("enter pass_word:")
    if inp_name == user_name and inp_pass_w == pass_word:
        print("success")
        break   
        # 这里可以是 flag = False(使用开关)  or  break
    else:
        print("error")
~~~

### while 循环进阶：

​		break 终止当前循环

~~~python
num = 1
while True:
    print("the num is :" + str(num))
    num += 1
    if num > 100:
        break
----第二段
num = 1
flag = True
while flag:
    print("the num is:" + str(num))
    num += 1
    if num > 100:
        flag = False
~~~



​		continue 跳出当前循环 进行下一次循环；

~~~python 
while True:
    print("loop") # 一直执行当前行，遇到continue 意思就是到达了代码的最后一行 重新开始循环
    continue
print("end")
~~~

while else :

~~~python
num = 1
while num < 10:
    print("the num is:" + str(num))
    num += 1
else:
    print("end")
 ------第二段
count = 1
while count <= 3:
    username = input("enter user_name:")
    pwd = input("enter pass_word:")
    count += 1
    if username == "gary" and pwd == "123456":
        print("success")
        break
    else:
        print("error")
else:
    print("the user was lacked")

~~~

while 嵌套：

~~~python
info = """
1.注册
2.登录
3.退出
"""
user = "gary"
pwd = "123456"
while True:
    print(info)
    choose = input("enter choose:")
    if choose == "1":
        z_name = input("user_name:")
        z_pwd = input("pass_word")
        z_phone = input("phone_number:")
        print(f"success register {z_name}  welcome")

    if choose == "2":
        while True:
            in_name = input("enter user_name:")
            in_pwd = input("enter pass_word:")
            if in_name == user and in_pwd == pwd:
                print("success")
                break
            else:
                print("error")
                continue
    if choose == "3":
        print(f"{in_name} welcome again")
        break
~~~

## 格式化：

~~~python
name = input("enter name:")
phone = input ("enter phone num:")
job = input("enter job:")
email = input("enter email:")
address = input("enter address:")
msg = """
姓名：%s
电话：%s
职位：%s
邮箱：%s
公司地址：%s
""" % (name, phone, job, email, address)
# python 3.6以上才可以使用：
print(msg)
mesg = f"""
姓名：{name}
电话：{phone}
职位：{job}
邮箱：{email}
地址：{address}
"""
print(mesg)
~~~

## 运算符：

1. 算术运算符：+-*/ %   （a//b 整除） （a**b  求幂 次方）

   ~~~python
   print(10//5)  # 2
   print(10//4)  # 2
   print(10**2)  # 100
   print(10/3)  # 3.3333333333333335
   print(10/3)  # 3  puthon2 version /除法结果取整数；
   ~~~

2. 比较运算符：> < == >= <= != 

3. 赋值运算符：=  +=  -=   *=  /=  %= **=

4. 逻辑运算符：and or not 与或非 （优先级：() not >and>or）

5. 在数字中 非零的都是True ,零是False ；

   字符串中非空的都是True,空的就是False;

    当and都为真 那么结果选择右边的true 当and都为假的时候 选择左边的False;  

   当Or两边只有一个为真的时候选择前边的内容

   当or运算都是真的时候选择or后边的内容 

6. 成员运算符：in  在  not in 不在

   ~~~python
   user_name = "gary"
   pass_word = "123456"
   num = 0
   blacklist = "meet li  liu  tom"
   while num < 3:
       name = input("enter user_name:")
       pwd = input("enter pass_word:")
       num += 1
       if name in blacklist:
           print(f"user:{name},sorry you are black_list")
           break
       if name == user_name and pwd == pass_word:
           print("success")
           break
       else:
           print("user_name or  pass_word is an error")
   else:
       print("over 3 times it was locked")
   ~~~

## 编码和进制转换：

1. ASCII(1字节 八位)     GBK  UTF-8（变长编码）

2. 进制转换：

   十进制转二进制 对2 求模 倒写出来；

  ## 字符串：

1. 索引：

   ~~~python
   # python 字符串下标定位；
   st = "gary" #[0-3] 负数就是从右往左排序查找
   print(st[2])
   ~~~

   字符串的加和乘  加是拼接，乘是倍输入输出；

   2. 切片：

   ~~~python
   st = "今天是个好日子，明天放假啦"
   print(st[0:8])  # garyh  顾头不顾腚0-a切片（0，a+1） # 今天是个好日子，
   print(st[-8:-1])   # 日子，明天放假
   st1 = "garyhua hello"
   print(st1[-5:-1])  #  hell
   ~~~

   2. 2 步长 ：默认是1左到右 参数为正 右左是负数；

      ~~~python
      st = "gary_hua"
      print(st[0:6:1])  # 第三个参数是步长 默认是 1  gary_h
      print(st[0:6:2])  # gr_
      ~~~

## 字符串的方法：

1.修改：upper() 全大写；lower() 全部小写；replace()替换；format()字符串格式化；capitalize()首字母大写；title()每个单词首字母大写；swapcase 大小写反转；

2.操作：split 分隔；strip去头尾内容；count统计元素出现次数；center 居中；

3.判断：startswith 判断什么开头；endswith判断什么结尾；isdecimal判断是否是十进制；isalnum 判断是否是数字，字母，中文；isalpha判断是否是字母和汉字；

4.查找：find查找某个元素是否存在，如果存在就返回这个元素的下标，没有返回-1 ；  index ；

1. 修改：

   ~~~python
   name = "hello wOrld"
   print(name.upper())  # HELLO WORLD
   name_up = name.upper()  # 大小写转换：
   print(name_up)  # HELLO WORLD 字符串是不可变数据类型
   print(name.lower())  # hello world
   # 验证码不区分大小写：
   msg = input("enter verification code:")
   if msg.upper() == "HELLO":
       print("verification code success!")
   else:
       print("error!")
   #  替换 游戏脏话屏蔽：
   name = "hello wOrld"
   print(name.replace("O", "o"))  # 大写o替换成小写
   # format 字符串格式化：还可以使用该方法将数字和字符串拼接一起 占位符{}，通过format方法将age给了{0}
   age = 36
   txt = "My name is John, and I am {}"
   print(txt.format(age))
   
   print(name.format())  # hello wOrld
   # capitalize()首字母大写：
   print(name.capitalize())  # Hello world
   # title() 每个单词首字母大写：
   print(name.title())  # Hello World
   # swapcase() 大小写反转：
   print(name.swapcase())  # HELLO WoRLD
   ~~~
 2. 操作：

~~~python
### spit 分隔：
name = "hello wOrldhe"
print(name.split(" "))   # ['hello', 'wOrldhe']
# strip 去头头尾：
print(name.strip("he"))  # llo wOrld
# count()统计元素出现次数；
print(name.count("l"))  # 3
# center 居中
print(name.center())  # -----
~~~

3.判断：

~~~python
# startswith()  endswith()
name = "hello wOrldhe"
print(name.startswith("w"))
-- False # startwith 就是判断字符串是不是以指定的字母开头；结果是boolean类型
name = "hello wOrldhe"
print(name.endswith("e"))
--True #判断结尾是不是指定的字母，
~~~

~~~python

# 判断是否是0-&的数字 isdecimal()
name = "dfkdjfdj"
print(name.isdecimal())  # false
name1 = "123456"
print(name1.isdecimal())  # true
name2 = "010101"
print(name2.isdecimal())  # true
name3 = "3.125"
print(name3.isdecimal())  # false
name4 = "-10"
print(name4.isdecimal())  # false
~~~

~~~python 
# 判断是不是数字，字母以及中文：isalnum
name = "dfkdjfdj"
print(name.isalnum())  # True
name = "1234"
print(name.isalnum())  # true
name = "dfkdj456dfd"
print(name.isalnum())  # True
name = "墨迹阿婆"
print(name.isalnum())  # True
name = "d^f?k_dj——f"
print(name.isalnum())  # False
~~~

~~~python
# 判断是不是字母或汉字
name = "dfkdjfdj"
print(name.isalpha())  # true
name = "dfk123456fdj"
print(name.isalpha())  # false
name = "dfk——_j?fdj"
print(name.isalpha())  # false

~~~

~~~python
# 查找find（） 查找"元素"的下标
name = "dfkdjfdj"
print(name.find("k"))  # 查找到的是第一个找到的下标
name = "你好呀很高兴认识你"
print(name.find("高"))  # 4 中文可以查找
name = "123456"
print(name.find("5"))  # 4 数字可以
~~~

获取字符串的长度：

~~~python
# 获取字符串长度：
name = "djdjfklasdfa"
print(len(name))  # 12 字符串长度是1开始的数字 下标是比长度小1的数字
#使用while循环打印出每个元素
# 使用while循环遍历字符串
name = "djdjfklasdfa"
count = 0
while count < (len(name)):
    print(name[count])
    count += 1
~~~

   ## for 循环：

~~~python
### for 循环 i是一个变量 暂时把i理解为一个变量，从第一个循环走向最后一个；
name = "Meet"
for i in name: # i 就是一个指针放到字符串中，for循环遍历每一个
    print(i)

for i in "meet":   
    print(i)
name = "anything"
i = 1
for i in name:
    print(i)
~~~

~~~Python
# 使用for循环索引/遍历出所有的列表/元组：
lis = ["gary", "tom", "jerry"]
tu = ("gary", "tom", "jerry")
for i in lis:
    print(i)
for i in tu:
    print(i)

~~~

   ## 小数据池: ==  id  is

~~~python
# 我们在定义变量的时候,内存那种开辟一个空间如果变量的值是一样的 那么就是变量名指向了同一个值;
# python 中我们经常开辟和销毁变量空间,在底层就自己维护了一个小数据池,它规定了一个区间能使用的是同一个内存地址,比如小数据池的数字区间是-5~256
#
a = 10
b = 10
print(a == b)  # True
print(id(a))  # 8790875903936
print(id(b))  # 8790875903936 a and b is the same address in disk;
# is 判断变量的地址是否相同;
print(a is b)  # True
c = 1025
d = 1025
print(id(c))  # 6322608  这里我们超出了小数据池的区间 ,那么为什么还是一样的地址呢? 在终端中就不一样了终端中一行代码就是一个代码块.
# 这里有代码块机制,代码块机制防止我们频繁的开辟空间降低效率,我们开辟了空间之后 他会检测我们的定义值有没有开辟没有再开辟,有了就使用同一个;
print(id(d))  # 6322608
# 代码块支持：
# 字符串：
# 定义字符串的时候内容，长度任意内存地址相同。
# 字符串进行乘法的时候总长度 <=20 内存地址相同。
# 中文，特舒符号 乘法的时候只能乘以1或 0
# 数字：
# 相同的数字内存地址相同
# 布尔值：
# 相同的内存地址相同
# 当代码块和小数据池两个在一起,就先执行代码块
# 小数据支持：
# 字符串：
# 纯字母和数字的时候长度任意，内存地址相同。
# 纯字母和数字乘法总长度 <= 20 内存地址相同。
# 中文和特殊符号乘法的时候只能乘以 0 内存地址相同
# 数字：
# -5 ～ 256
# 布尔值：
# True
# False
# 小数据池和代码块都是Python内置的,咱们开发的时候不使用,他们统称为驻留机制,有了小数据池和代码块能够提升Python的效率
~~~

## 深浅拷贝:

~~~PYTHON
# 浅拷贝: 就是把原列表中的记录的内存地址的内存地址拿到一个新开辟的列表中;
lst = [1, 2, 3, [4, 5, 6]]
result = lst.copy()  # 复制列表给result 虽然也是地址 但是原列表的更改会在result列表中体现;
print(result)  # [1, 2, 3, [4, 5, 6]]
lst1 = lst[:]  # 浅拷贝
print(lst1)  # [1, 2, 3, [4, 5, 6]]
lst[0] = 0
print(lst, lst1)  # [0, 2, 3, [4, 5, 6]] [1, 2, 3, [4, 5, 6]] 浅拷贝原数据进行改变,新开辟的列表不进行变动,新列表拷贝了原的地址.指向的还是原数据;
lst.append(9)  # 浅拷贝的添加; 开辟一个空间 装了9 然后把地址给lst指向9;
print(lst)  # [1, 2, 3, [4, 5, 6], 9]
print(result)  # [1, 2, 3, [4, 5, 6]]
# 深拷贝: 是把内层元素的每个元素地址拷贝到新空间中 指向了内层的元素;
import copy
lst = [1, 2, 3, [5, 6]]
lst2 = copy.deepcopy(lst)
print(lst2)   # [1, 2, 3, [5, 6]]
lst[3] = "gary"
print(lst)  # [1, 2, 3, 'gary']
print(lst2)  # [1, 2, 3, [5, 6]]  深拷贝不论是否修改原数据, 新列表不会进行改变
# 总结:列表中 赋值: 两个或多个变量名指向同一个内存地址时,有任何一个操作对指向的地址进行了更改,那么其余变量名指向了新的更改值.
lst1 = lst
print(lst, lst1)  # [1, 2, 3, 'gary'] [1, 2, 3, 'gary']
lst[0] = 2
print(lst, lst1)   # [2, 2, 3, 'gary'] [2, 2, 3, 'gary']
# 浅拷贝:只拷贝列表中第一层的内存地址,原列表修改了不可变数据类型,新开辟的列表不进行变动,因为只是在原列表中将内存地址进行修改了,新开辟的列表中的内存地址还是用的之前的内存地址
# 浅拷贝:原列表对可变数据类型进行了添加,新开辟的列表中存放就是可变数据类型的地址,在去查看的时候就发现进行更改了--

# 深拷贝:不管你修改原数据的不可变类型还是可变类型,新开辟的空间中都不会进行改变,因为可变数据类型新开辟了一个空间

~~~

## python_file基础,文件操作:

使用Python来读写文件是非常简单的操作,我们使用open()来打开一个文件,获取到文件句柄,然后通过文件句柄就可以进行各种各样的操作了

模式：只读，只写，追加，写读，读写....根据打开方式的不同能够执行的操作会有相应的差异.

打开文件的方式:

　　r,w,a

　　r+,w+,a+

　　rb,wb,ab

　　r+b,w+b,a+b

~~~python
# r 模式下的只读 操作:
c = open("fileText.txt",mode="r",encoding="gbk")  # ("文件名","模式","编码格式") c是文件句柄,文件操作符,文件操作对象,
content = c.read(5)  # 读方法,读取文件中指定的文件 也可以指定我们想要读取的内容数量,在方法里加参数(字符串的长度)
print(content)
c.close()
# rb模式: 只读字节模式 在读取非文本文件的时候,mp3,图像,视频等信息 字节模式用于传输和存储
f = open("fileText.txt", mode="rb")  # 读字节模式不用写编码格式;
content =f.read()
print(content)  # b'\xbc\xc6\xe3  等信息 是byte类型,在RB模式下,不能coding字符集;
f.close()
# 文件路径: 相对路径和绝对路径:相对路径就是相对于当前工作地址.绝对路径就是以根目录作为参照物去寻找文件地址;比喻:一栋十层楼 相对 我知道你在第几层挨个房间找 绝对:我从一楼开始每个房间找
"""
Python在使用绝对路径的时候因为系统原因造成\意义不同:
解决方法一:
open('C:\\Users\\Meet')  # 这样就成功的将\进行转义   两个\\代表一个\
 解决方法二:
open(r'C:\Users\Meet') #这样相比上边的还要省事,在字符串的前面加个小r也是转义的意思
"""
# 绝对路径测试:
f = open(R"C:\Users\Administrator\Desktop\新建文本文档.txt",mode="r",encoding="GBK")
content = f.read()
print(content)
f.close()
# 读取操作中,read()方法,如果文件中数据量很大的话,那么全部读取放在内存中会到最后内存的崩溃
# 读取行操作 readline() 每次只读取一行,最后有一个\n
f = open("fileText.txt",mode="r",encoding="gbk")
content = f.readline()
f.close()
print(content)  # 读取一行最后有换行符
~~~

~~~python
# 写操作:  在写文件的时候我们要养成一个写完文件就刷新的习惯. 刷新flush()
# 覆盖写: 如果文件不存在,那么W模式下会创建文件.
c = open("fileText.txt",mode="w",encoding="gbk")  # mode="w"当我选择使用w模式的时候,在打开文件的时候就就会把文件中的所有内容都清空,然后再操作
c1 = open("fileText.txt",mode="r",encoding="gbk")
content = c.write("这是最后的结果,来自Python")
c.flush()
content1 = c1.read()
c.close()
print(content1)   # 这是最后的结果,来自Python  文档中的内容已经被覆盖
c2 = open("fileText.txt",mode="wb")  # wb写入bytes数据模式下 不可以对文件进行编码指定,需要在字符串下指定编码,然后写入
content2 = "你好".encode("gbk")
c2.write(content2)
c2.flush()
mes = c1.read()
c2.close()
print(mes)  # 你好
#  追加: mode 是a 或者是a+ 都是在文件末尾写入 不考虑光标的位置; a模式如果文件不存在 会创建一个指定文件名的文件;
c3 = open("fileText.txt",mode="a",encoding="gbk")
c3.write("这是Python的追加写入")
c3.flush()
c3.close()
mes = c1.read()
c1.close()
print(mes)  # 你好这是Python的追加写入

~~~

~~~python
# 读写模式 R+,先读后写,因为开始我们的光标在开头,读完光标走到末尾之后我们再进行追加写;常用使用
# f = open("fileText.txt",mode="r+",encoding="gbk")
# content = f.read()  # 先读,光标走到文件末尾
# f.write("读写模式r+")  # 写入数据
# f.flush()
# f.close()
# print(content)  # 第一次运行看不到写入内容
# 在r+模式下. 如果读取了内容. 不论读取内容多少. 光标显示的是多少. 再写入 或者操作文件的时候都是在结尾进行的操作.
# 先写后读 错误的写法 光标在文件头之前 写入在文档中看不到;
# f = open("fileText.txt",mode="r+",encoding="gbk")
# f.write("我先写了")
# f.flush()
# content = f.read()
# f.close()
# print(content)  # 这样的写法看不到写入的内容;没有写进去
# 写读模式 W+ 先将所有的内容清空,然后写入,最后读取, 但是读出内容为空
f = open("fileText.txt",mode="w+",encoding="gbk")  # w+和w模式写一样,先清空,再写入,我们读取不到内容的;
f.write("大家好,我是写读W+模式")
f.flush()
mes = f.read()
f.close()
print(mes)  # 读出内容为空,
# a+模式下,不论是先读还是后读,都是读不到数据的
~~~

其他相关操作

~~~python
# seek() :移动光标位置到N位置.移动单位是byte通常我们移动到开头或者结尾  # tell() 可以获取当前光标位置
f = open("fileText.txt",mode="r+",encoding="gbk")
f.seek(0, 0)  # 光标移动到开头 (0,1)移动到当前位置(0,2)移动到末尾(3)移动光标按照字节进行移动
content = f.read()  # 读取从开开头到结尾
f.seek(0)  # 移动到开头
f.seek(0,2)  # 移动到末尾
content1 =f.read()
print(content1)  # 什么也没有读到
f.seek(0)
f.write("华光辉")
f.flush()
print(f.tell())  # 6 (012)2*3
f.seek(0)
print(f.tell())  # 获取当前光标位置 0
content2 = f.read()
f.close()
print(content2)  # 华光辉,我是写读W+模式
# 修改文件:只能将文件中的内容读取到内存中, 将信息修改完毕, 然后将源文件删除, 将新文件的名字改成老文件的名字.(弊端:数据量大内存溢出,采取行读取的方式)
import os
with open("fileText.txt",mode="r", encoding="gbk") as f,open("新建文本文档.txt",mode="w", encoding="gbk") as f1:
    content = f.read()
    print(content)
    new_content = content.replace("dajiha","hello")  # 指定的第一个参数替换成第二个参数的值
    f1.write(new_content)
    print(new_content)
os.remove("fileText.txt")  # 删除源文件
os.rename("新建文本文档.txt","fileText.txt")  # 把存入数据的文件重命名为原文件名 文件中必须先创建文件新文档用于存数据
f = open("fileText.txt",mode="r",encoding="gbk")
content = f.read()
print(content)
f.close()
# 防止数据溢出优化代码:行读取更改
import os
with open("fileText.txt",mode="r",encoding="gbk") as f, open("新建文本文档.txt",mode="w",encoding="gbk")as f1:
    for line in f:  # 在文件中行遍历
        new_line = line.replace("hello","gary")  # 遇到hello 更改为gary
        f1.write(new_line)   # 写入新建文本文档的 new_line
os.remove("fileText.txt")  # 删除源文件
os.rename("新建文本文档.txt","fileText.txt")  # 给文件更名为源文件

~~~

## 函数 function:

def 是Python中用来定义函数的关键字; 位置参数,关键字参数,混合参数(混合参数必须在关键字参数前面);

~~~python
# 函数 关键字是def 空间中开辟一个空间存放了函数的代码 在需要的时候调用这段代码
def len():
    a = "hello world"
    count = 0
    for i in a:
        count += 1
        print(count)  # 0-11
result = len()
print(result)  # none 没有返回值
# 函数的返回值;
def happy():
    print("gary")
    print("jerry")
    print("tom")
    return "friends"
    print("tomi")  # return 后的代码不再执行,遇到return 代码结束;
result = happy()
print(result)  # friends return 给了返回值
# 函数的返回值可以有多个结果;
def test():
    a=3
    if a>0:
        print("success")
    else:
        print("error")
    return "你猜对不对","我才不猜"
result = test()
print(result)
print(type(result))  # <class 'tuple'> 当返回值是多个结果的时候,就是一个元组 我们可以通过解构获取多个变量;
# 函数的参数: 我们通过对函数参数进行定义
def name(na):  # na 是形参
    print("我的名字是:"+na)
    print("他的名字是gary")
    print("那个人没有名字")
    return na
get_name = name("tom") # 实参 这个过程叫传参
print(get_name)  # tom
# 参数:
# 1.形参:写在函数声明位置的变量叫形参,形式上的完整 说明这个函数需要参数;
# 2.实参:在函数调用的时候传递给函数的值, if 实际上传递给形参的结果:
# 3.传参:在调用函数的过程中,把实参传递给形参的过程称作传参;
# 参数的分类:多个参数
def name(na,na1,na2):  # na 是形参 也可以给某个参数赋值,作为默认参数
    print("我的名字是:"+na)
    print("他的名字是"+na1)
    print("那个人没有名字"+na2)
    return na,na1,na2
get_name = name("tom","gary","none") # 实参 这个过程叫传参
print(get_name)  # ('tom', 'gary', 'none')
# 关键字参数: 就是在参数比较多的情况下 比较复杂需要记忆,关键字参数我们只要记住参数名字就可以了;直接在形参处赋值
def name(na="gary",na1="tom",na2="none"):  # na 是形参
    print("我的名字是:"+na)
    print("他的名字是"+na1)
    print("那个人没有名字"+na2)
    return na,na1,na2
# get_name = name("tom","gary","none") # 实参 这个过程叫传参
get_name = name()  # 这里不需要传参,因为直接放在了形参处;
print(get_name)  # ('tom', 'gary', 'none')
~~~

函数的动态参数:给一个函数传了很多参数,我们就要写很多,很麻烦怎么办呢,我们可以考虑使用动态参数,动态参数必须放在位置参数的后边,否则会覆盖~~~

~~~python
# 动态参数:动态接收位置参数;动态参数必须在位置参数的后边;默认参数写在动态参数前边没有生效 形参的顺序: 位置参数 , 动态参数 , 默认参数
def eat(*args):  # *表示接受任意参数.
    print("我要吃",args)  # 这里用,号连接,args是元组,不能进行字符串拼接
eat("黄焖鸡","烧烤")  # 参数是元组
# 动态参数是一个元组,必须在位置参数的后边,否则数据混乱;
def eat(a,b,*args):
    print("大家好!","我会",a,"我会",b,"还有",args)
eat("唱歌","跳舞","吃","喝","嫖","赌")
# 默认参数写在动态参数前边没有生效 动态参数会把默认参数覆盖,形参的顺序:位置参数,动态参数,默认参数;
def eat(a,b="毒",*args):
    print("大家好!","我会",a,"我会",b,"还有",args)
eat("吃","喝","嫖","赌")  # 大家好! 我会 吃 我会 喝 还有 ('嫖', '赌')
# 在python中可以动态位置参数,但是不能动态关键字参数,动态关键字参数是dict;
def fuc(*args):
    print("print reault:",args)
fuc("gary","tom","jerry")  # print reault: ('gary', 'tom', 'jerry')
# 动态关键字参数结果是dict演示;
def fuc(**args):
    print("print result:",args)
fuc(a=1,b=2,c=3)  # print result: {'a': 1, 'b': 2, 'c': 3}
位置参数 > args(动态位置参数) > 默认值参数 > *kwargs(动态默认参数)
# 动态位置和动态关键字结合可以接受所有的参数;
def func(*args,**kwargs):
    print(args,kwargs)  # (1, 23, 5) {'a': 1, 'b': 6}
func(1,23,5,a=1,b=6)
# 动态参数传列表元素;
lst = [1,3,5]
def fuc(*args):
    print(args)  # (1, 3, 5)
fuc(lst[0],lst[1],lst[2])
fuc(*lst)  # (1, 3, 5) 实参位置上是用*将lst按照顺序打散;在形参的位置上用*把收到的参数组合成一个元组;
# 字典动态参数;
dic = {'a':1,'b':2}  # 字典
def func(**kwargs):
    print(kwargs)  # {'a': 1, 'b': 2}
func(**dic)
~~~

名称空间:在python解释器开始执行, 就会在内存中开辟一个空间, 每当遇到一个变量的时候, 就把变量名和值之间的关系记录下来, 但是当遇到函数定义的时候, 解释器只是把函数名读入内存, 表示这个函数存在了, 至于函数内部的变量和逻辑, 解释器是不关心的. 也就是说一开始的时候函数只是加载进来, 仅此而已, 只有当函数被调用和访问的时候, 解释器才会根据函数内部声明的变量来进行开辟变量的内部空间. 随着函数执行完毕, 这些函数内部变量占用的空间也会随着函数执行完毕而被清空.

~~~ python
def fun():  # 在解释器遇到函数定义的时候,解释器仅仅把函数名读入内存,表示这个函数的存在,不关心内部的变量值和逻辑关系,只有在函数调用的时候才会根据函数内部的声明进行开辟变量空间 函数执行完毕,空间清空
    a = 10
    print(a)
fun()
print(a)  # 超出作用域
我们给存放名字和值的关系的空间起一个名字叫: 命名空间. 我们的变量在存储的时候就是存储在这片空间中的.
# 命名空间分为 全局命名空间, 局部命名空间,内置命名空间(存放关键字):加载顺序:内置,全局,局部(函数被执行的时候);取值顺序:局部,全局,内置
# 我们可以通过global()函数查看全局作用域(全局+内置)中的内容,通过locals()函数查看局部作用域中的变量和函数信息;
a = 10
def fun():
    a = 15
    b = 20
    print(a, b)
    print(globals())
    print(locals())
fun()
~~~

函数的嵌套:

~~~ python
def fun():
    print(111)
def fun1():
    print(222)
fun()
print("over")  # 函数调用哪个执行哪一个
# 函数的嵌套:
def fun():
    print("111")
    def fun1():
        print("222")
    fun1()
    print("333")
print("over")
fun()
print("end")
~~~

global and nonlocal

~~~ python

# global、nonlocal :
# global在函数内部修改全局的变量,如果全局中不存在就创建一个变量
a = 100  # 如果没有这个全局a 报错a is not defined
def func():
    global a    # 加了个global表示不再局部创建这个变量了. 而是直接使用全局的a
    a = 28
print(a)  # 100
func()  # 进行了声明和更改
print(a)  # 28
# nonlocal 我称他为半全局变量,只在函数内部起作用.只修改上一层变量,如果上一层中没有变量就往函数再上找一层,只会找到函数的最外层,不会找到全局进行修改
a = 10
def func():
    a = 15
    print(a)
    def func1():
        nonlocal a
        a = 23
        print(a)
    func1()
    print(a)
print(a)
func()
# 10 15 23 23
# 代码理解nonlocal
a = 1
def fun_1():
    a = 2
    def fun_2():
        nonlocal a
        a = 3
        def fun_3():
            a = 4
            print(a)
        print(a)
        fun_3()
        print(a)
    print(a)
    fun_2()
    print(a)
print(a)
fun_1()
print(a)
~~~

## 函数名的使用和f-string使用:

函数名的运用:函数名是一个变量,是一个特殊的变量,和括号配合可以执行函数的变量;

~~~ python
# 函数名的内存地址: 同时函数名可以赋值给变量,可以当做容器类的元素:
def func():
    print("hello")
print(func)  #  输出函数名,得到函数的内存地址;  <function func at 0x00000000005D5280>
# a = func
# a()  # hello 函数名给了a 就替换了func,相当于给函数func换了一个名字;
def func1():
    print("world")
def func():
    print("hello")
def func1():
    print("world")
lst = [func,func1]  # 本事是遍历名字替换成I 然后调用I的函数
for i in lst:
    i()
# 函数名可以当做函数的参数:
def func():
    print("吃了么")
def func2(fn):  # func2(func())
    print("我是func2")
    fn()    # 执行传递过来的fn  执行 fn()的时候就是func()
    print("我是func2")
func2(func)     # 把函数func当成参数传递给func2的参数fn.fn()函数就代表了func()
# 函数名可以作为函数的返回值:
def func_1():
    print("这里是函数1")
    def func_2():
        print("这里是函数2")
    print("这里是函数1")
    return func_2
fn = func_1()
# 执行函数1.  函数1返回的是函数2, 这时fn指向的就是上面函数2
fn()    # 执行func_2函数
# 这里是函数1 这里是函数1 这里是函数2
~~~

f-string字符串格式化:

~~~ python
# f-strings 字符串格式化:python 3.6开始加入标准库输出先写法:这个格式化输出比之前的%s format效率高,更加简化,非常好用.
name = "gary"
age = 18
sex = "男"
mes = f"姓名:{name}\n性别:{sex}\n年龄:{age}"  # 其实就是模版和变量的使用; {}中是变量,可以使用变量给任意值,
print(mes)
# f-strings 任意表达式:
print(f"年龄:{3*7}")  # 不管是任何类型的表达式,都需要是string类型的  年龄:21
print(f"全部大写:{name.upper()}")  # 全部大写:GARY
teacher = {"name":"tom","age":"18"}  # 字典的格式化表达:
print(f"teacher name:{teacher['name']} age {teacher['age']}")  # teacher name:tom,age 18
# 列表的格式化表达:
lst = ["gary","tom","jerry"]
print(f"姓名:{lst[0]} 姓名:{lst[1]}")  # 姓名:gary 姓名:tom
# 也可以插入表达式,格式化显示返回值到字符串相应的位置;
def sum(a,b):
    return a+b
a = 2
b = 3
print(f"a+b={sum(a,b)}")  # a+b=5
# 多行f格式化:
print(f"hello{name}")
speaker = (f"hello,{name}"),(f"hello,{teacher['name']}"),(f"hello,{lst[2]}")
print(speaker)  # ('hello,gary', 'hello,tom', 'hello,jerry')
# 其他细节: ! , : { } 这些标点不能出现在{}里边.使用lambda 表达式会有问题 我么通过lambda嵌套在圆括号里解决问题;
print(f"hello,{name}")  # 测试不允许标点:{name}外层加多层{}结果不一样,不成格式化了;
x = 5
print(f"{(lambda x: x*2) (x)}")  # 10

~~~

## ==迭代器==:iterator 

 可迭代对象:更新迭代的: 是一个重复(但是不是单纯的循环一样的重复,每次重复基于上次的结果)取值的对象;在python中凡是内部含有iter方法的对象都是可迭代对象;可迭代对象就是内部含有'--iter--'方法的对象,就是可迭代对象;

可迭代对象的优点: 可以直观的查看里面的数据

可迭代对象的缺点: 1.占用内存。 2.可迭代对象不能迭代取值（除去索引，key以外）。

~~~ python 
# 在python 中使用dir()方法查看对象是不是可迭代对象;返回一个列表 这个列表含有该对象以字符串的形式的所有方法名.
name = "gary"
a = 100
print(dir(name))  # 可以查看所有的该对象可以使用的方法;
print("__iter__" in dir(name))  # true
print("__iter__" in dir(a))  # false
for i in dir(name):
    if i in "__iter__":
        print("true")
    else:
        print("-")   # 结果中有true
~~~

迭代器: it is a tools which in Python is simply an [object](https://www.programiz.com/python-programming/class) that can be iterated upon. An object which will return data, one element at a time.迭代器是这样的对象：实现了无参数的--next--方法，返回序列中的下一个元素，如果没有元素了，那么抛出StopIteration异常.python中的迭代器还实现了__iter__方法，因此迭代器也可以迭代.简单说:内部含有--iter--方法 并且含有--next-- 方法的对象就是迭代器

迭代器的优点：

 节省内存。 迭代器在内存中相当于只占一个数据的空间：因为每次取值都上一条数据会在内存释放，加载当前的此条数据。

 惰性机制。 next一次，取一个值，绝不过多取值。

 有一个迭代器模式可以很好的解释上面这两条：迭代是数据处理的基石。扫描内存中放不下的数据集时，我们要找到一种惰性获取数据项的方式，即按需一次获        	取一个数据项。这就是迭代器模式。

 迭代器的缺点：

 不能直观的查看里面的数据。

 取值时不走回头路，只能一直向下取值。

对比:

**可迭代对象：**

 是一个私有的方法比较多，操作灵活（比如列表，字典的增删改查，字符串的常用操作方法等）,比较直观，但是占用内存，而且不能直接通过循环迭代取值的这么一个数据集。

 **应用**：当你侧重于对于数据可以灵活处理，并且内存空间足够，将数据集设置为可迭代对象是明确的选择。

 **迭代器：**

 是一个非常节省内存，可以记录取值位置，可以直接通过循环+next方法取值，但是不直观，操作方法比较单一的数据集。

 **应用**：当你的数据量过大，大到足以撑爆你的内存或者你以节省内存为首选因素时，将数据集设置为迭代器是一个不错的选择。（可参考为什么python把文件句柄设置成迭代器）。

~~~ python
# 如果判断对象是都是迭代器或迭代对象;str list tuple dict set range 文件句柄 哪个是迭代器，哪个是可迭代对象
name = "gary_hua"
lst = [1,2,3]
tup = (1,2,3)
dic = {"name":"gary","age":18}
set = {1,2,"gary"}
f = open("fileText.txt",mode="r+",encoding="gbk")
# 可迭代对象;
print(dir(name))  # 查看对象的全部方法.可以判断是否包含iter可迭代
print("__iter__" in dir(name))  # true  注意__符号不要写成--
print("__iter__" in dir(lst))  # true
print("__iter__" in dir(tup))  # true
print("__iter__" in dir(dic))  # true
print("__iter__" in dir(set))  # true
print("__iter__" in dir(f))  # true
# 判断迭代器:
print("__next__" in dir(name))  # false
print("__next__" in dir(lst))  # false
print("__next__" in dir(tup))  # false
print("__next__" in dir(dic))  # false
print("__next__" in dir(set))  # false
print("__next__" in dir(f))  # true
# 以上结果可得:所有的对象都是迭代对象,只有文件句柄是迭代器;
# 可迭代对象转成迭代器;
name = "gary"
set = {1,2,5}
print("__iter__" in dir(name))  # true 可迭代对象;
print("__next__" in dir(name))  # false 不是迭代器
ite = name.__iter__()  # 或者:iter(name)
print(ite)  # <str_iterator object at 0x00000000026A59D0>
ite1 = iter(set)
print(ite1)  # <set_iterator object at 0x000000000247EA80>
print("__iter__"in dir(ite1))  # true
# 迭代器取值;可迭代对象是不可以一直迭代取值的,(除去索引,切片,key) 但是转换成迭代器就可以了;迭代器是利用__next__进行取值;
name = "hello world gary is a lucky boy always"
obj = iter(name)  # 转换成迭代器
job1 = obj.__next__()
print(job1)  # h
job2 = obj.__next__()
print(job2)  # e...... 依次遍历出hello world gary is a lucky boy always
for i in name:
    print(i)  # 循环遍历(循环迭代)
# for循环的循环对象一定要是可迭代对象，但是这不意味着可迭代对象就可以取值 for循环内部机制是:将可迭代对象转换成迭代器，然后利用next进行取值，最后利用异常处理处理StopIteration抛出的异常。
# 我们使用while 语句模拟for循环的迭代器机制
name = "gary hello"
obj = iter(name)
while 1:  # 1 为真,其他数字为假
    try:  # python的异常处理模式:
        print(next(obj))  # 使用迭代器的next()打印输出迭代器遍历内容
    except StopIteration:
        break

~~~

## 生成器 

 生成器和迭代器也有不同，唯一的不同就是：迭代器都是Python给你提供的已经写好的工具或者通过数据转化得来的，（比如文件句柄，iter([1,2,3])。生成器是需要我们自己用python代码构建的工具。

在python中有三种方式来创建生成器：

1. 通过"生成器函数"
2. 通过生成器推导式
3. python内置函数或者模块提供（其实1,3两种本质上差不多，都是通过函数的形式生成，只不过1是自己写的生成器函数，3是python提供的生成器函数而已）

~~~ python
# 生成器函数构建生成器 yield 关键字:(替换return)
def func():
    print(111)
    return 222  # 单纯调用函数没有返回值 这里我们把return 替换成 yield
print(func())
# 当我们把返回值替换成yield的时候,func 就不再是函数 而是一个生成器.
def func():
    print(111)
    yield 333
func()  # 没有运行;
print(func())  # <generator object func at 0x00000000027543C0>
# 那么我们接下来就要按照迭代器的的形式去取值;
generator = func()  # 这个时候的函数只是生成器,没有函数功能了
result = generator.__next__()  # 调用迭代器的next方法
print(result)  # 111  333  直接使用迭代器名(函数名)调用或者重新命名;
print(func().__next__())  # 111  333
# 生成器函数中写多个yield.
def func():
    print("111")
    yield 222
    print("333")
    yield 444
    print("555")
    yield 666
    print("pause1")  # 这个语句没有执行出结果 这一句没有yield去迭代结果,所以不执行;
print("over the program")
result = func()
print(result)  # <generator object func at 0x00000000027643C0>
re1 = result.__next__()  # 大概是第一个next的意思包含了 整个生成器迭代走一遍 只返回一次yield值 下次next返回下一个yield值
re2 = result.__next__()  # 二次yield 再返回下一个yield的值
re3 = result.__next__()  # 三次返回yield的值
print(re1)  # 111 333 555 222
print(re2)   # 444
print(re3)  # 666
# yield 和 return区别 return一般在函数中只设置一个，他的作用是终止函数，并且给函数的执行者返回值。yield在生成器函数中可设置多个，他并不会终止函数，next会获取对应yield生成的元素。
def eat():
    lst = []  # declare a list type lst no element;
    for i in range(1,101):  # 不包含第二个参数;
        lst.append('包子'+str(i))  # 生成1-99的空间,里边设置成"包子"+i;
    return lst   # 执行完之后一次 return返回结果
e = eat()  # 执行函数 得到的生成的包子空间
print(e)  # 输出包子列表 得到的返回值 lst
def eat():
    for i in range(1,101):
        print("新包子做好了")
        yield '包子'+str(i)  # 使用生成器,得到一个值 就返给生成器e(单纯的返回,自己决定是否输出)
        print("老板再来一个")
e = eat()
for i in range(50):  # 这个是主程序;先执行这里;
    print(e.__next__())  # 这句语句也是是yield以及以上的语句执行;然后这句话输出了yield返回值
    # next(e)  # 这句话单纯调用生成器 没有调用返回值 就是不报第几个包子
    print("吃包子")
# 新包子做好了 吃包子 老板再来一个  这句话执行50次 如果使用print(e.__next__()) 就显示 新包子做好了 包子1 吃包子 老板再来一个
# 象比较第一种return返回方式,yield节省内存,同时保留上次的位置;
def eat():
    for i in range(1,10000):
        yield '包子'+str(i)  # 这句话输出了500次
e = eat()
for i in range(200):   #这两个循环并且关系 200 执行完 执行下一个300 同时生成器记得位置,一共执行500
    print(e.__next__())
for i in range(300):
   print(e.__next__())
# 扩展: send()方法;
# send和next()区别:
# ​ 相同点：
# ​ send 和 next()都可以让生成器对应的yield向下执行一次。
# ​ 都可以获取到yield生成的值。
# ​ 不同点：
# ​ 第一次获取yield值只能用next不能用send（可以用send(None)）。
# ​ send可以给上一个yield置传递值。
def gen(name):
    print(f'{name} ready to eat')
    while 1:
        food = yield 111  # 这个值不能被传递
        print(f'{name} start to eat {food}')  # 这是yield之后的
dog = gen('alex')
next(dog)  # alex ready to eat 在没有输出的情况下 第一次next遇到yield就出循环 找下一个next 然后执行yield之后的
next(dog)  # alex start to eat None
next(dog)  # alex start to eat None
def gen(name):
    print(f'{name} ready to eat')
    while 1:
        food = yield
        print(f'{name} start to eat {food}')

dog = gen('alex')
next(dog)  # alex ready to eat
dog.send('骨头')  # alex start to eat 骨头
dog.send('狗粮')  # alex start to eat 狗粮
dog.send('香肠')  # alex start to eat 香肠
# yield from
def func():
    lst = ['卫龙','老冰棍','北冰洋','牛羊配']
    yield lst
g = func()
print(g)  # 这个不用多讲了吧,生成器对象地址
print(next(g))  # 只是返回一个列表 ['卫龙', '老冰棍', '北冰洋', '牛羊配']
print(g.__next__())  # StopIteration 停止迭代
def func():
    lst = ['卫龙','老冰棍','北冰洋','牛羊配']
    yield from lst  # 迭代list元素
g = func()
print(g)
# 他会将这个可迭代对象(列表)的每个元素当成迭代器的每个结果进行返回。
print(next(g))  # 卫龙
print(next(g))  # 老冰棍
print(next(g))  # 北冰洋
print(g.__next__())  # 牛羊配
# yield from 细节;
def func():
    lst1 = ['卫龙', '老冰棍', '北冰洋', '牛羊配']  # 先迭代这个列表;全部结束走列表2
    lst2 = ['馒头', '花卷', '豆包', '大饼']
    yield from lst1
    yield from lst2
g = func()
for i in g:
    print(i)  # 卫龙 老冰棍 北冰洋 牛羊配 馒头 花卷 豆包 大饼
~~~

## 推导式:

本节我们讲列表推导式,"生成器表达式"以及"其他推导式"我认为推导式就是构建比较有规律的列表,生成器，字典等一种简便的方式

~~~ python
# 列表推导式;
# 一般形式:
lst = []  # 空列表
for i in range(1,11):  # range(10) 就是迭代生成1-10
    lst.append(i)
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 列表推导式生成:  循环模式[变量(处理的变量) for 变量 in iterable];筛选模式:[变量 for 变量 in iterable if 条件] 还有多层循环;
lst = [i for i in range(10)]  # 在列表中for循环生成10个数 值是i,然后把i 放到列表中;
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = [i*i for i in range(10) if i != 5]  # i*i 处理的变量
print(lst)  # [0, 1, 4, 9, 16, 36, 49, 64, 81]
# 100 以内的所有的偶数;
lst = [i for i in range(2,101,2)] # 以2开始到101 步长是2
print(lst)  # [2,4,6,8,10,12...,100]
lst = [f"python{i}" for i in range(1,5)]  # 这里就是加工处理过的变量 我们想要的理想数据
print(lst)  # ['python1', 'python2', 'python3', 'python4']
# 生成器表达式:生成器表达式和列表推导式的语法上一模一样,只是把[]换成()就行了
gen = (i*2 for i in range(10))
print(gen)  # <generator object <genexpr> at 0x00000000027743C0>
for i in gen:
    print(i)  # 0 2 4 6 8 10 12 14 16 18
# 生成器表达式的筛选:
gen = (i for i in range(5) if i < 3)
for i in gen:
    print(i)  # 0 1 2
~~~

**生成器表达式和列表推导式的区别:**

1. 列表推导式比较耗内存,所有数据一次性加载到内存。而生成器表达式遵循迭代器协议，逐个产生元素。
2. 得到的值不一样,列表推导式得到的是一个列表.生成器表达式获取的是一个生成器
3. 列表推导式一目了然，生成器表达式只是一个内存地址。

 无论是生成器表达式，还是列表推导式，他只是Python给你提供了一个相对简单的构造方式，因为使用推导式非常简单，所以大多数都会为之着迷，这个一定要慎重，推导式只能构建相对复杂的并且有规律的对象，对于没有什么规律，而且嵌套层数比较多（for循环超过三层）这样就不建议大家用推导式构建。

生成器的惰性机制: 生成器只有在访问的时候才取值,说白了.你找他要才给你值.不找他要.他是不会执行的.

其他相关的推导式;

~~~ python
# 字典推导式:
lst1 = ['jay','jj','gary']
lst2 = ['周杰伦','林俊杰','华光辉']
dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
print(dic)  # {'jay': '周杰伦', 'jj': '林俊杰', 'gary': '华光辉'}
# 集合推导式;
lst = [1,2,3,4,5,6]
s ={i for i in lst}  # {1, 2, 3, 4, 5, 6}
print(s)
for i in s:
    print(i)
~~~

## 内置函数 inner_func:

函数就是功能,一个函数封装一个功能,python将一些常用的功能函数封装起来给我们使用,提高效率,避免代码的重复.这些函数就是内置函数;我们自己定义的函数

~~~ python
这是我们不常用的函数:
all() any() bytes() callable() chr() complex() divmod() eval() exec() frozenset() globals() hash() help() id()
input() int() iter() locals() next() oct() ord() pow() repr() round()\

常用函数:abs() format()enumerate() filter() map() max() min() open() range() print() len() list() dict() str() float()
reversed() set() sorted() sum() tuple() type() zip() dir()

classmethod() delattr() getattr() hasattr() issubclass() isinstance() object() property() setattr() staticmethod() super()
# test all(),any()
lst = [1<2]  # 测试参数:[0][0,1] [1,2][""][1>2][1<2]  结果:false false;ft:ft:tt;ff;ff;tt
print(all(lst))   # 所有元素为0,为空"",表达式为false 那么返回就是false;namely :所有为真就是真 所有为假就是假;
print(any(lst))  # 如果任意元素为0,false或者为空,那么返回false; 所有为真才是真,任意为假就是假;
# bytes() 测试bytes(s,encode("utf-8")) bytes函数就是把字符串指定为编码格式,或者还原更改为其他的编码方式;
s = '你好'
bs = s.encode('utf-8')
print(bs)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
s1 = bs.decode('utf-8')
print(s1)  # 你好
bs = bytes(s,encoding='utf-8')
print(bs)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
re = bs.decode("utf-8")
print(re)  # 你好
b = '你好'.encode('gbk')
print(b)  # b'\xc4\xe3\xba\xc3'
b1 = b.decode('gbk')
print(b1)  # 你好
print(b1.encode('utf-8'))  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
rs = b1.encode("utf-8")
print(rs)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
rs = rs.decode("utf-8")
print(rs)  # 你好
# 上边的内置函数准备在使用中统计,专门记录不便于理解;
# print(b)  # b'\xc4\xe3\xba\xc3'
# b1 = b.decode('gbk')
# print(b1)  # 你好
# print(b1.encode('utf-8'))  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
# rs = b1.encode("utf-8")
# print(rs)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
# rs = rs.decode("utf-8")
# print(rs)  # 你好
# 上边的内置函数准备在使用中统计,专门记录不便于理解;
~~~

## 匿名函数none_name（lambda）:

匿名函数，顾名思义就是没有名字的函数，那么什么函数没有名字呢？这个就是我们以后面试或者工作中经常用匿名函数 lambda，也叫一句话函数。

   ~~~ Python
# 匿名函数 函数名 = lambda 参数:返回值
# 正常我们使用一个函数
name = "gary"
def func(name):
    print(name+"handsome")
rs=func(name)
# 使用匿名函数:
func = lambda name:name+"handsome" # lambda parameters:expression
print(func("gary"))  # garyhandsome
# 匿名函数小题:
 
   ~~~

## 闭包

定义:闭包是嵌套在函数中的函数;闭包必须是被内函数对外层函数的变量(非全局变量) 的引用;

闭包的作用：保存局部信息不被销毁，保证数据的安全性。

~~~ Python
# 闭包;
# 先完成一个三个值求平均值的例子;
# 从上面的例子可以看出，基本上完成了我们的要求，但是这个代码相对来说是不安全的，因为你的这个series列表是一个全局变量，只要是全局作用域的任何地方，都可能对这个列表进行改变。
values =[]
def func(new_values):
    values.append(new_values)
    total = sum(values)
    return total/len(values)
print(func(200))  # 200.0
print(func(300))  # 250.0
# 对数据进行改变;
values.append(15000)  # 那么最后结果就变成了4000.0
print(func(500))  # 333.333333
# 怎么进行优化呢? 我们猜想把全局变量放进函数里 变成局部变量;
def make_averager(value):
    series = []  # 这里不会保存上次得到的数据随着函数的结束而消失,会临时开辟新空间存放, 把本地得到的value值放进列表, 所以每次的print结果就是value
    series.append(value)
    total = sum(series)
    return total / len(series)
print(make_averager(100))
print(make_averager(200))
print(make_averager(500))
# 那么 我们现在使用闭包的理念去试试吧.闭包是嵌套在函数中的函数。闭包必须是内层函数对外层函数的变量（非全局变量）的引用。
# 闭包的作用：保存局部信息不被销毁，保证数据的安全性。
# 闭包的应用：
# 可以保存一些非全局变量但是不易被销毁、改变的数据。
# 装饰器。
def func():
    values = []
    def make_avg(value):
        values.append(value)
        total = sum(values)
        return total/len(values)
    print(make_avg(100))  # 100
    print(make_avg(200))  # 150
    print(make_avg(1500))   # 600.0
func()

~~~

## python 装饰器:

修饰器:在不改变原被装饰的函数的源代码以及调用方式下，为其添加额外的功能。

开放封闭原则: 对扩展开放,对修改是封闭的 怎么理解: 假如我们开发一个软件,后期我们肯定是要进行扩展的,那么我们原来的代码就需要封闭,不能轻易更改,要不然程序就不能按照既定的功能使用,但是我们又要扩展新功能 所以我们可以调用写好的函数 为我们的新扩展服务,这就是开放封闭原则.对扩展开放,对源码封闭;

~~~ python
import time

# 这个包导入全局有效;下边代码省略# # 装饰器;
# # 我们通过一个例子去理解装饰器


def func():
    print(range(100))
    time.sleep(1)


def func1():
    print(range(200))
    time.sleep(2)


def func2():
    print(range(300))
    time.sleep(3)
# # 接下来我们对这个函数进行性能测试,就是看运行着个函数耗费了多少时间;
print(time.time())  # 获取的时间戳 1594992298.7047856 格林尼治时间
start_time=time.time()
func()  # 这个地方如果我们需要测试不同的代码n个 那么我们写n次这个测试代码吗?
end_time =time.time()
print("耗时:",end_time-start_time,"秒")
# # 优化: 这里在写函数调用的时候依然有问题, 有一百次调用我们就写一百次吗?
#
#
def test(func_name):   # func_name 就是需要测试的函数名字;
    start_time = time.time()
    func_name()  # 这个地方如果我们需要测试不同的代码n个 那么我们写n次这个测试代码吗?
    end_time = time.time()
    return ("耗时:",end_time - start_time, "秒")


rs = test(func1)  # 这里就成了动态传参; 测试一千次 调用一千次???
print(rs)
# # 深度最终优化:  装饰器;借助于内层函数inner(),将func() 的返回值返回给了函数的调用者,也就是index()自身,index()调用 返回给index()
#
#
def index():  # 测试代码
    time.sleep(2)  # 模拟一下网络延迟以及代码的效率
    print('欢迎访问博客园主页')
    return '访问成功'


def timer(func):  # func = index
    def inner():
        start_time = time.time()  # 开始时间
        func()  # 函数调用 index() 实际返回了这里
        end_time = time.time()  #
        print(f'此函数的执行效率为{end_time-start_time}')
    return inner
def timer(func):  # func = index
    def inner():
        start_time = time.time()
        ret = func()  # 这里我们让index函数的返回值赋值给ret ,执行完之后返回值给ret 实际就是给了index() 就是不管你的代码
        end_time = time.time()
        print(f'此函数的执行效率为{end_time-start_time}')
        return ret
    return inner


# # 如果inner有返回值, 那么timer()函数的结果就会改变; 这里的timer就是装饰.实际上他是inner()
index = timer(index)  # 这里先执行timer函数 参数是index 那么就是timer(index).返回inner,所以index=inner 然后输入index函数,那么我们就进入inner函数执行,遇到func()参数是index我们执行index()
print(index())  # None ?? 根据上句的index返回值是inner 所以我们这一句index()其实是inner()
# # 装饰函数参数问题:

def index():
    time.sleep(2)  # 模拟一下网络延迟以及代码的效率
    print('欢迎访问博客园主页')
    return '访问成功'


def home(name):
    time.sleep(3)  # 模拟一下网络延迟以及代码的效率
    print(f'欢迎访问{name}主页')


def timer(func):  # func = index
    def inner(name):  # 这里函数有参数 我们就能进行参数传递了
        start_time = time.time()
        func(name)  # 这里进行参数声明,那么太白就传给了home(name)函数,
        end_time = time.time()
        print(f'此函数的执行效率为{end_time-start_time}')
    return inner
# 
# # 要想timer装饰home函数怎么做？
home = timer(home)
home('太白')    # home也就是inner()是无参的,我们这里给了一个参数,因此报错了
~~~

标准版修饰器:

~~~python
import time


def home(name,age):  # 被测试函数;
    time.sleep(3)
    print(f"欢迎你{name}")


def timer(func):  # 测试耗时函数 func = home
    def inner(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)  # func就是home函数; 这里func(home)到这参数去了被测试函数;
        end_time=time.time()
        print(f"耗时:,{end_time-start_time}")
    return inner


home = timer(home)  # timer(home) is inner()
home("gary",18)  # 对home(inner)进行传参;


def timer(func):  # func = home
    def inner(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print(f'此函数的执行效率为{end_time-start_time}')
    return inner


@timer  # home = timer(home)  # 简化说明修饰器
def home(name,age):
    time.sleep(3)  # 模拟一下网络延迟以及代码的效率
    print(name,age)
    print(f'欢迎访问{name}主页')


home('太白',18)

# 利用装饰器做一个需求;简单模拟登陆要求:
login_status = {   # 初始化
    'username': None,
    'status': False,
}


def auth(func):
    def inner(*args,**kwargs):
        if login_status['status']:
            ret = func()
            return ret
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        if username == "gary" and password == '123456':
            login_status['status'] = True
            ret = func()
            return ret
    return inner

@auth 
def diary():
    print('欢迎访问日记页面')

@auth
def comment():
    print('欢迎访问评论页面')

@auth
def home():
    print('欢迎访问主页')


diary()
comment()
home()


import time


def method(name,age): # 被调用函数;
    time.sleep(2)
    print("欢迎您",name)


def test(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs);
        end_time = time.time()
        print("耗时:",(end_time-start_time))
    return inner


rs = test(method)
rs("hello",20)  # 两个参数传到inner里边,然后传给func()调用,最后到达method()方法中.
# 带参数的装饰器(/装饰器装饰多个函数 ); 其实就是装饰器的嵌套,用装饰器去修饰一个可以作为形参参数的装饰器;
def wrapper1(func):
    def inner1(*args,**kwargs):
        print("这是装饰器一开始")
        func(*args,**kwargs)
        print("这是装饰器一结束")
    return inner1

def wrapper2(func):
    def inner2(*args,**kwargs):
        print("这是装饰器二开始")
        func(*args,**kwargs)
        print("这是装饰器二结束")
    return inner2


@wrapper1  # 两个装饰器装饰func函数;Python规定多个装饰器装饰一个函数的时候先执行离被装饰的函数最近的装饰器
@wrapper2
def func():  # 相当于 func =wrapper1(func)
    print("这是被装饰的函数")
func()
# 结果是:这是装饰器一开始 这是装饰器二开始 这是被装饰的函数 这是装饰器二结束 这是装饰器一结束

~~~

## 递归recursion:

~~~python
# 斐波那契数列  recursion 的使用
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return func(n-1)+func(n-2)


result = func(7)
print(result)
print("------")
# 我想看到每个数列的值
for i in range(1, 8):
    print(func(i))
~~~

~~~ python
# 递归(recursion):递归就是不断地去调用自身;
def func():
    print("it is recursion")
    func()


# func()  # 这是一个循环 不断调用自身;
# 不断的调用自己本身
# 有明确的终止条件


def age(n):
    if n == 1:  # 4
        return 18  # 5
    else:
        return age(n-1)  # or 5


result = age(3)  # 2
print(result)  # 6

li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]

def func(lst):
    for i in lst:
        if type(i) == list:
            func(i)  # recursion
        else:
            print(i)
func(li)

# func(5)是函数的调用  下边是调用过程:
# 1.n=5  if ==false return 5*func(5-1)
# 2.现在不在关注外部的第一个func 而是把焦点放在5*func(5-1) 这个函数中
# 3.func(4) if == false  else return 4*func(4-1)
# 4.func(3) if == false else return 3*func(3-1)
# ....
# func(1) if == true  return 1 ;
# 当调用结束 会依次得出返回值 返回给函数.也是递归形式 5*(4*(3*(2*1)))=120
def func(n):
    if n == 1:
        return 1
    else:
        return n*func(n-1)


result = func(5)
print(result)
~~~

## 模块 modula:

1. 从文件级别组织程序，更方便管理, 随着程序的发展，功能越来越多，为了方便管理，我们通常将程序分成一个个的文件，这样做程序的结构更清晰，这时我们不仅仅可以把这些文件当做脚本去执行，还可以把他们当做模块来导入到其他的模块中，实现了功能的重复利用
2. 拿来主义，提升开发效率 同样的原理，我们也可以下载别人写好的模块然后导入到自己的项目中使用，这种拿来主义，可以极大地提升我们的开发效率，避免重复造轮子.
3. 内置模块(标准库) 第三方模块,自定义模块.

~~~ python
# 模块的定义和调用; 每个模块都是一个独立的名称空间，定义在这个模块中的函数，把这个模块的名称空间当做全局名称空间，这样我们在编写自己的模块时，
# 就不用担心我们定义在自己模块中全局变量会在被导入时，与使用者的全局变量冲突。
# import 使用;
import meet  # 导入模块,那么就是把里边的代码加载进命名空间,随时准备调用,如果是直接的输出语句,那么会输出
# 这里我把下面代码都注释掉 依然执行了 print("这是我的模块")


def func():
    print("这是自己定义的函数;")


t = meet.func()  # 这里已经调用了模块 输出了模块中的内容;
# func()  # 本代码的定义函数,虽然可模块中的重名,但模块的引用方式是模块名+.函数名
print(t)  # none 这个返回值是none
t = type(t)
print(t)  # <class 'NoneType'>
# # 为模块起别名 方便使用,有利于代码的扩展和优化.
import meet

# # 导入多个模块 推荐写法是每个模块占一行,这样易于阅读,易于编译,搜索和维护
# from ... import ... 使用 同时支持别名;
from meet import func  # 仅仅调用了函数 而不是像import一样把代码加载到内存空间 print 直接输出;
print(func())  # 仅仅输出空间名,func()是调用函数+函数返回值none
# from..import.. 和 import 区别: import是相当于全局变量或者函数声明,模块名+.函数名进行调用,from import是直接加载进当前名称空间 可以直接使用函数名进行调用;
# 优点是方便好用; 缺点是容易和当前执行文件中的名字冲突
# 当执行文件中的变量或者函数名和模块同名,会有覆盖效果;
meet = "gary"  # 覆盖操作.
print(meet)  # gary
# # meet.func()  # 这里找不到对应的函数,因为meet被string类型的字符串覆盖了
from meet import *
func()
func1()
func2()
# 模块循环导入问题;模块导入一次之后,就不会重新导入,只会在第一次导入时执行模块代码,在我们的项目中应该尽量避免出现循环/嵌套导入，如果出现多个模块都需要共享的数据，可以将共享的数据集中存放到某一个地方
~~~

py文件的两种功能;1.是脚本,一个文件就是整个程序,用来被执行,2.模块,文件中存放的是一些功能函数,用来被导入调用.

python为我们内置了全局变量--name--， 当文件被当做脚本执行时：--name-- 等于'--main--' 当文件被当做模块导入时：--name--等于模块名作用：用来控制.py文件在不同的应用场景下执行不同的逻辑

 Python中引用模块是按照一定的规则以及顺序去寻找的，这个查询顺序为：先从内存中已经加载的模块进行寻找找不到再从内置模块中寻找，内置模块如果也没有，最后去sys.path中路径包含的模块中寻找。它只会按照这个顺序从这些指定的地方去寻找，如果最终都没有找到，那么就会报错。

 内存中已经加载的模块->内置模块->sys.path路径中包含的模块

  ~~~ python
# 常用模块:time ,datetime,random,
# time  时间戳,格式化字符串时间. fromat String:"19940407"
import time
from datetime import datetime

# 时间戳
tp = type(time.time())  # float 类型
tm=time.time()
print(tm)  # 1595393395.8905227

# 时间字符串:
t = time.strftime("%y-%m-%d %X")  # X 大写是时间,小写是重复输出日期格式;
print(t)  # 20-07-22 07/22/20  20-07-22 10:12:31
# 时间元组:localtime将一个时间戳转换成当前时区的struct_time
t = time.localtime()
print(t)
# 时间格式转换;时间戳-->结构化时间-->时间戳(-->字符串时间-->结构化时
print(time.time())  # 格林尼时间  时间戳
print(time.localtime())  # 当地时间  结构化

# 结构化时间-->时间戳
time_tuple = time.localtime()
t = time.mktime(time_tuple)
print(t)  # 1595393873.0
# 结构化--->字符串时间
print(time.strftime("%y-%m-%d"))  # 20-07-22
t=time.strftime("%y-%m-%d",time.localtime())  # 通过更改格林尼时间秒数输出字符串时间;
print(t)  # 20-07-22
# datetime模块:
print(datetime.now())  # 2020-07-22 10:41:36.779929
print(datetime(2018,5,28,13,13,13))  # 获取指定时间;2018-05-28 13:13:13
# datetime 和时间戳替换:
t = datetime.now()
print(t.timestamp())  # 1595395058.786634
# str 和 datetime的转换 一般用户输入str 我们处理时间如期转成datetime 通过datetime.strptime()
t=datetime.strptime("2020-7-22","%Y-%m-%d")
print(t)  # 2020-07-22 00:00:00
# random 模块;
num = (random.random()*100)  # random.random() 0-1之间的随机数
print(num)
num1=random.randint(1,100)  # 100 以内整数随机;
print(num1)
num2=random.randrange(1,100,2)  # 奇数(第三个参数不能被整除的数)
print(num2)
num3=random.choice([1,58,6,3,4,"12"])  # 随机选择返回一个
print(num3)
# 打乱列表顺序;
lis =[1,2,85,6,4,85,9,66,5,7]
random.shuffle(lis)  # 随机打乱次序,还在lis列表里;
print(lis)
# 练习 随机生成验证码;
import random
def v_code():
    code = ""  # str 空字符串;
    for i in range(5):  # 遍历循环出五个数据
        num=random.randint(0,9)  # 随机生成0-9的数字
        alf=chr(random.randint(65,90))  # 从编码表随机生成一个65-90的数字对应的码表;
        add=random.choice([num,alf])  # 随机选择数字或者码表生成字母 放在列表中;
        code="".join([code,str(add)])  # str(add)方法选择一个结果,赋值给code,然后以""的方式连接成一个新的字符串;
        # str(add)是对add执行的结果进行数据类型转换; ([]) code就是前一位,str(add)是新生字符,然后使用""进行拼接;
    return code
print(v_code())
  ~~~

## 序列化模块serialization_modula:

 序列化的本质就是将一种数据结构（如字典、列表)等转换成一个__特殊__的序列（字符串或者bytes）的过程就叫做序列化

序列化模块就是将一个常见的数据结构转化成一个特殊的序列，并且这个特殊的序列还可以反解回去。它的主要用途：文件读写数据，网络传输数据

 json模块 :（**重点**）

 用于网络传输：dumps、loads

 用于文件写读：dump、load

1. 不同语言都遵循的一种数据转化格式，即不同语言都使用的特殊字符串。（比如Python的一个列表[1, 2, 3]利用json转化成特殊的字符串，然后在编码成bytes发送给php的开发者，php的开发者就可以解码成特殊的字符串，然后在反解成原数组(列表): [1, 2, 3]）
2. json序列化只支持部分Python数据结构：dict,list, tuple,str,int, float,True,False,None

 pickle模块：

1. 只能是Python语言遵循的一种数据转化格式，只能在python语言中使用。
2. 支持Python所有的数据类型包括实例化对象。

 shelve模块：类似于字典的操作方式去操作特殊的字符串（不讲，可以课下了解）。   

   ~~~ python
# 序列化模块 json
import json
dic ={"gary":18,"tom":20,"jerry":6}  # 字典
str_dic = json.dumps(dic)  # json 转化成特殊字符串序列
print(type(str_dic),str_dic)  # <class 'str'> {"gary": 18, "tom": 20, "jerry": 6}
# 反解回去;
st = json.loads(str_dic)
print(type(st),st)  # <class 'dict'> {'gary': 18, 'tom': 20, 'jerry': 6}

# dump load 将对象转换成字符串然后写入文件中;针对文件操作;
f = open("json_file","w")
json.dump(str_dic,f)  # 直接写入文件 ,没有返回值
f.close()
# 反解:
f = open("json_file","r+")
st = json.load(f)
f.close
print(st)  # {"gary": 18, "tom": 20, "jerry": 6}

   ~~~

json序列化存储多个数据到同一个文件中,存储多个数据到一个文件中是有问题的,默认的json文件只能存储一个json数据,但是可以解决;

~~~python
# # 多个数据存储到同一个文件中;可以是不同的数据类型;
import json
dic = {"tom":12,"gary":15,"jerry":6}
str = "gary"
dic_1 ={"tom":10,"gary":1,"jerry":2}
f = open('序列化',encoding='utf-8',mode='w+')
r_1 = json.dumps(dic)  # 字典序列化为字符串,然后行写入.
f.write(r_1 + "\n")  # 写一个数据,换一行;
r_2 = json.dumps(dic_1)
f.write(r_2 + "\n")
r_3 = json.dumps(str+"\n")
f.write(r_3)
f.close()
# # 反解出来: 这里反解就出问题了;我们使用写入换行,写出读行来解决;
f = open('序列化',encoding="utf-8",mode="r+")
# # r1=json.load(sts,f)
# # r2=json.load(dic,f)
# print(r)  # json.decoder.JSONDecodeError: Extra data:
for line in f:
    print(json.loads(line))

import json
# 重复执行也是实际上只写入一次  
dic ={"gary":18,"tom":17,"jerry":20}
str_name = "hello world"
lst = [45,55,12,3,3,6,5]
f = open("te_json_file",encoding="utf-8",mode="w+")
str_1= json.dumps(dic)
f.write(str_1+"\n")

f.write(str_name+"\n")
str_2 = json.dumps(lst)
f.write(str_2+"\n")
f.close()
# 反解:
f = open("te_json_file",encoding="utf-8",mode="r+")
print(json.loads(str_1))
print(str_name)  # 本身没有序列化 直接就是str类型的,所以在反序列化就有问题了;
print(json.loads(str_2))


~~~

pickle 模块: 将数据结构转换成bytes类型,然后可以反序列化回去;只能用于python语言识别.json是通用语言,而pickle是python专用.

~~~ Python
 # pickle 序列化:
import pickle
dic = {"gary":18,"jerry":20}
bina = pickle.dumps(dic)
print(bina)
# b'\x80\x04\x95\x18\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04gary\x94K\x12\x8c\x05jerry\x94K\x14u.'
# 反序列化
bin_op=pickle.loads(bina)
print(bin_op)  # {'gary': 18, 'jerry': 20}


# 多个数据到一个文件中的序列化: 和json略有不同,编码问题
dic = {"gary":"fifteen","tom":"twenty","jerry":"six"}
dic_1 = {"time":"ten","min":"seven"}
f = open("pickle_test",mode="wb")  # 转换成binary 不需要指定编码格式
pickle.dump(dic,f)
pickle.dump(dic_1,f)
f.close()
# 反序列化:
f = open("pickle_test",mode="rb")  # 使用rb读取字节操作
while True:
    try:
        print(pickle.load(f))
    except EOFError:
        break
f.close()
~~~

~~~ python
# os 模块 特是一个和操作系统交互的一个接口,它提供的功能多与工作目录，路径，文件等相关
import os
# 工作目录相关
print(os.getcwd())  # 获取当前工作目录  D:\python\python_code
os.chdir("dirname"))  # 改变当前工作目录  相当于cd:
os.curdir  # 返回当前目录
os.pardir  # 获取当前目录的父目录名;


# 文件夹相关的
os.makedirs('dirname1/dirname2')     # 可生成多层递归目录  ***
os.removedirs('dirname1')  # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推 ***
os.mkdir('dirname')    # 生成单级目录；相当于shell中mkdir dirname ***
os.rmdir('dirname')    # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname ***
li = os.listdir('dirname1')    # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印 列表显示


# 文件相关
os.remove("file_name")  # 删除一个文件  ***
os.rename("old_name","new_name")  # 重命名文件/目录  ***
os.stat("path/filename")  # 获取文件/目录信息 **

# 路径相关
os.path.abspath("path")  # 返回path规范化的绝对路径  ***
os.path.split("path")  # 将path分割成目录和文件名二元组返回 ***
os.path.dirname("path")  # 返回path的目录。其实就是os.path.split(path)的第一个元素  **
os.path.basename("path")  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值，即os.path.split(path)的第二个元素。 **
os.path.exists("path")   # 如果path存在，返回True；如果path不存在，返回False  ***
os.path.isabs("path")   # 如果path是绝对路径，返回True  **
os.path.isfile("path")   # 如果path是一个存在的文件，返回True。否则返回False  ***
os.path.isdir("path")   # 如果path是一个存在的目录，则返回True。否则返回False  ***
os.path.join(path1[, path2[, ...]])   # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略 ***
os.path.getatime("path")   # 返回path所指向的文件或者目录的最后访问时间  **
os.path.getmtime("path")   # 返回path所指向的文件或者目录的最后修改时间  **
os.path.getsize("path")  # 返回path的大小 ***

# 操作系统相关
os.sep   # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/" *
os.linesep     # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep     # 输出用于分割文件路径的字符串 win下为;,Linux下为: *
os.name     # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix' *
# 和执行系统命令相关
os.system("bash command")   # 运行shell命令，直接显示  **
os.popen("bash command).read()")  # 运行shell命令，获取执行结果  **
os.environ   # 获取系统环境变量  **


# os.stat('path/filename') 获取文件/目录信息 的结构说明(了解)
stat 结构:
st_mode: inode 保护模式
st_ino: inode 节点号。
st_dev: inode 驻留的设备。
st_nlink: inode 的链接数。
st_uid: 所有者的用户ID。
st_gid: 所有者的组ID。
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
st_atime: 上次访问的时间。
st_mtime: 最后一次修改的时间。
st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。


# sys 模块
sys.argv           # 命令行参数List，第一个元素是程序本身路径
sys.exit(n)        # 退出程序，正常退出时exit(0),错误退出sys.exit(1)
sys.version        # 获取Python解释程序的版本信息
sys.path           # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值  ***
sys.platform       # 返回操作系统平台名称


# hashlib模块 此模块有人称为摘要算法，也叫做加密算法，或者是哈希算法，散列算法等等
# 它的工作原理给大家简单描述一下：它通过一个函数，把任意长度的数据按照一定规则转换为一个固定长度的数据串（通常用16进制的字符串表示）。
# hashlib的特征以及使用要点：
# bytes类型数据 ---> 通过hashlib算法 ---> 固定长度的字符串
# 不同的bytes类型数据转化成的结果一定不同。
# 相同的bytes类型数据转化成的结果一定相同。
# 此转化过程不可逆。
# 那么刚才我们也说了，hashlib的主要用途有两个：
# ​ 密码的加密。
# ​ 文件一致性校验。
import hashlib
md5 = hashlib.md5()
md5.update("123456".encode("gbk"))
print(md5.hexdigest())  # e10adc3949ba59abbe56e057f20f883e
# 加盐加密  固定盐 ,动态盐
ret = hashlib.md5('xx教育'.encode('utf-8'))  # xx教育就是固定的盐
ret.update('a'.encode('utf-8'))  # 对a这个字符进行加盐
print(ret.hexdigest())
# 动态盐
username = '宝元666'
ret = hashlib.md5(username[::2].encode('utf-8'))  # 针对于每个账户，每个账户的盐都不一样
ret.update('a'.encode('utf-8'))
print(ret.hexdigest())
collections模块
在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。

# 1.namedtuple: 生成可以使用名字来访问元素内容的tuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)  # Point(x=1, y=2)

# 2.deque: 双端队列，可以快速的从另外一侧追加和推出对象
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q
deque(['y', 'a', 'b', 'c', 'x'])
#
# 3.Counter: 计数器，主要用来计数
from collections import Counter

c = Counter('abcdeabcdabcaba')
print(c)  # Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})

# 4.OrderedDict: 有序字典 对key插入的顺序排序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)]) # 另一种定义字典的方式
print(d)
# 结果:{'a': 1, 'c': 3, 'b': 2}

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
# 结果: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# 5.defaultdict: 带有默认值的字典
li = [11,22,33,44,55,77,88,99,90]
result = {}
for row in li:
    if row > 66:
        if 'key1' not in result:
            result['key1'] = []
        result['key1'].append(row)
    else:
        if 'key2' not in result:
            result['key2'] = []
        result['key2'].append(row)
print(result)  # {'key2': [11, 22, 33, 44, 55], 'key1': [77, 88, 99, 90]}

from collections import defaultdict
values = [11, 22, 33,44,55,66,77,88,99,90]
my_dict = defaultdict(list)

for value in  values:
    if value>66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)
print(my_dict)  # defaultdict(<class 'list'>, {'k2': [11, 22, 33, 44, 55, 66], 'k1': [77, 88, 99, 90]})
~~~

## 软件开发规范:

~~~python 
# 开发分层分级对代码进行规划,做到清晰,代码分类,函数,方法等独立
~~~

## re 正则表达式 Regular representation

~~~python
　#正则就是用一些具有特殊含义的符号组合到一起（称为正则表达式）来描述字符或者字符串的方法。或者说：正则就是用来描述一类事物的规则。（在Python中）它内嵌在Python中，并通过 re 模块实现。正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。
\w	匹配字母（包含中文）或数字或下划线
\W	匹配非字母（包含中文）或数字或下划线
\s	匹配任意的空白符
\S	匹配任意非空白符
\d	匹配数字
\D	匹配非数字
\A	从字符串开头匹配
\z	匹配字符串的结束，如果是换行，只匹配到换行前的结果
\n	匹配一个换行符
\t	匹配一个制表符
^	匹配字符串的开始
$	匹配字符串的结尾
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	匹配字符组中的字符
...	匹配除了字符组中的字符的所有字符
*	匹配0个或者多个左边的字符。
+	匹配一个或者多个左边的字符。
？	匹配0个或者1个左边的字符，非贪婪方式。
{n}	精准匹配n个前面的表达式。
{n,m}	匹配n到m次由前面的正则表达式定义的片段，贪婪方式
ab	匹配a或者b
()	匹配括号内的表达式，也表示一个组
~~~

## 模块和包 modula and package

~~~ python
# 只要文件夹下含有__init__.py文件就是一个包
# 为了能够充分的将某个功能进行重用 我们使用了模块,但是慢慢的模块就会越来越多.我们想提高程序的结构性可维护性,就使用包将模块进行统一管理
# 使用import 和from xx import xx 进行包的使用;
~~~

## loging_modula

~~~ python
# 这个模块的功能是记录我们软件的各种状态
# 开发人员可以通过错误日志中的内容对他的程序进行修改
# 简单配置函数
import logging
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
# 默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，这说明默认的日志级别设置为WARNING
# （日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）
# 默认的日志格式为 日志级别：Logger名称：用户输出消息

# asicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有：
# filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
# filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
# format：指定handler使用的日志显示格式。
# datefmt：指定日期时间格式。
# level：设置记录日志的级别
# stream：用指定的stream创建StreamHandler。可以指定输出到
# sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。
# format参数中可能用到的格式化串：
#
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息
# logging库提供了多个组件：Logger、Handler、Filter、Formatter。Logger对象提供应用程序可直接使用的接口，Handler发送日志到适当的目的地，
# Filter提供了过滤日志信息的方法，Formatter指定日志显示格式。另外，可以通过：logger.setLevel(logging.Debug)设置级别,当然，也可以通过
# fh.setLevel(logging.Debug)单对文件流设置某个级别。
~~~

## 面向对象oop(object-oriented programming):

~~~ python
# 面向函数,就是面向对象,我们不再面向过程编程,而是把问题看待成一个对象进行处理;  减少代码的重复,增强代码的可读性
#面向对象的程序设计的核心是对象（上帝式思维），要理解对象为何物，必须把自己当成上帝，上帝眼里世间存在的万物皆为对象，不存在的也可以创造出来。
# 对象：就是类的具体表现形式
# 类：就是具有相同属性和功能的一类事物
# 面向过程:
s1 = "fjdsklafsjda"
count = 0
for i in s1:
    count += 1
print(count)
# 面向函数:


def func(s):
    count = 0
    for i in s:
        count += 1
    return count


rs_1 =func("fdsafdsa")
rs_2 =func([1,2,3,4])
print(rs_1,rs_2)  # 8 4


# 类的结构:
class Human:
    """
    此类主要是构建人类
    """
    mind = '有思想'  # 第一部分：静态属性 属性 静态变量 静态字段
    dic = {}
    l1 = []
    def work(self): # 第二部分：方法 函数 动态属性
        print('人类会工作')
class 是关键字与def用法相同，定义一个类。
Human是此类的类名，类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头。
类的结构从大方向来说就分为两部分：
静态变量。
动态方法。
#  类的结构
class TestClass:  # 描述人的类
    name = "gary"
    age = 18
    sex = "男"
    print(name)  # 这里会在控制台进行输出,

    def eat(self):  # 对象操作类方法的时候,对象将本身当做参数隐形传参
        print("吃饭")

    def work(self):
        print("工作")

    def walk(self):
        print("散步")


p = TestClass()  # 类的实例化:独立开辟一个空间指向了类.

print(TestClass.name)
print(p.name)
TestClass.eat(1)  # 用类名调用方法就需要带形参
p.eat()


class Person():
    def __init__(self,name):  # 魔法方法(初始化函数); 给对象空间封装属性;def _init_()函数为对象属性或者创建对象的时候必须执行的其他操作分配值；
        # 每次使用这个类创建对象的时候都会引用_init_()给属性赋值。就是初始化；
        self.name = name
        print("1111")


p = Person("jerry")
print(p.name)
# 类的公有成员,类的私有成员;


class Person():
    nationality = "中国"  # 公有成员变量
    __a = 10  # 这里声明的是类私有成员变量,只能在类中使用;

    def __init__(self,name):  # 魔法方法(初始化函数); 给对象空间封装属性;
        self.name = name
        print("1111")


p = Person("jerry")
p_1 = Person("tom")
print(p.name)
print(p.nationality)
print(p_1.nationality)


# 查看类中的所有内容：类名.__dict__方式。
class Human:
    """
    此类主要是构建人类
    """
    mind = '有思想'  # 第一部分：静态属性 属性 静态变量 静态字段
    dic = {}
    l1 = []
    def work(self): # 第二部分：方法 函数 动态属性
        # print(self)
        print('人类会工作')

print(Human.__dict__)
以下了解:
print(Human.__dict__['mind'])
Human.__dict__['mind'] = '无脑'  # 错误
#通过这种方式只能查询，不能增删改.
print(Human.__dict__)

# 万能的点  # # 通过万能的点 可以增删改查类中的单个属性
class Human:
    """
    此类主要是构建人类
    """
    mind = '有思想'  # 第一部分：静态属性 属性 静态变量 静态字段
    dic = {}
    l1 = []
    def work(self): # 第二部分：方法 函数 动态属性
        # print(self)
        print('人类会工作')
print(Human.mind)  # 查
Human.mind = '无脑'  # 改
print(Human.mind)
del Human.mind  # 删
Human.walk = '直立行走'
print(Human.walk)


# 类名操作动态方法  除了两个特殊方法：属性，类方法之外，一般不会通过类名操作一个类中的方法。
class Human:
    """
    此类主要是构建人类
    """
    mind = '有思想'  # 第一部分：静态属性 属性 静态变量 静态字段
    dic = {}
    l1 = []
    def work(self): # 第二部分：方法 函数 动态属性
        # print(self)
        print('人类会工作')
    def tools(self):
        print('人类会使用工具')

Human.work(111)
Human.tools(111)
下面可以做，但不用。
Human.__dict__['work'](111)

# 对象是从类中出来的，只要是类名加上（），这就是一个实例化过程，这个就会实例化一个对象。一个类可以实例化多个对象
class Human:
    mind = '有思想'

    def work(self):
        print('人类会工作')

    def tools(self):
        print('人类会使用工具')
obj = Human() # 实例化对象
print(obj)  # <__main__.Human object at 0x00000191508AA828>
实例化过程中;
在内存中开辟了一个对象空间。

自动执行类中的__init__方法，并将这个对象空间（内存地址）传给了__init__方法的第一个位置参数self。

在__init__ 方法中通过self给对象空间添加属性。
#  

~~~

~~~python
# 类
class Student:
    native_place = "Henan"  # 类属性

    def __init__(self ,name ,age):   # 初始化方法 对方法内的属性进行赋值
        self.name = name
        self.age = age

    def eat(self):  # 实例方法 带有self参数
        print("正在吃饭")

# 静态方法 没有参数 提前@声明staticmethod
    @staticmethod
    def drink():
        print("正在喝水")
# 类方法
    @classmethod
    def cm(cls):
        print("这里是类方法,")
~~~

## 面向对象的三大特征

:封装,继承,多态

~~~ python
class Animal(Person):  # 括号里就是继承
    def dog(self):
        self.name = "harry"
        print(self.name)
        self.eat()


d = Animal()
d.dog()


# 类的封装: 就是在类内定义的方法被定义在类中,数据私有化,
# 类的继承:


class Person():
    name="gary"
    age= 20
    sex = "男"

    def eat(self):
        print(self.name,"吃饭")

    def drink(self):
        print(self.name,"喝")

    def sleep(self):
        print(self.name,"睡觉")


# p = Person()
# print(p.name)
# p.eat()
# p.sleep()


class Animal(Person):  # 括号里就是继承

    # pass   # 相当于空的类体

    def __init__(self,name,age,sex):  # 这里相当于重构
        self.name = name
        self.age = age
        self.sex = sex

    def dog(self):
        print(self.name)
        self.eat()


d = Animal("tom",10,"男")
d.dog()
~~~



## python中反射和双下方法:

反射的概念是由Smith在1982年首次提出的，主要是指程序可以访问、检测和修改它本身状态或行为的一种能力（自省）。这一概念的提出很快引发了计算机科学领域关于应用反射性的研究。它首先被程序语言的设计领域所采用,并在Lisp和面向对象方面取得了成绩。

python面向对象中的反射：通过字符串的形式操作对象相关的属性。python中的一切事物都是对象（都可以使用反射）

~~~ python
# 对象的反射
class Foo:
    f = '类的静态变量'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hi(self):
        print('hi,%s'%self.name)

obj=Foo('egon',73)

#检测是否含有某属性
print(hasattr(obj,'name'))
print(hasattr(obj,'say_hi'))

#获取属性
n=getattr(obj,'name')
print(n)
func=getattr(obj,'say_hi')
func()

print(getattr(obj,'aaaaaaaa','不存在啊')) #报错

#设置属性
setattr(obj,'sb',True)
setattr(obj,'show_name',lambda self:self.name+'sb')
print(obj.__dict__)
print(obj.show_name(obj))

#删除属性
delattr(obj,'age')
delattr(obj,'show_name')
delattr(obj,'show_name111')#不存在,则报错

print(obj.__dict__)


# 类的反射:
class Foo(object):

    staticField = "old boy"

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'

    @staticmethod
    def bar():
        return 'bar'


print(getattr(Foo, 'staticField'))
print(getattr(Foo, 'func'))
print(getattr(Foo, 'bar'))
~~~

## 异常捕获:

~~~ Python
# 异常捕获 和结构; python 为每一种异常定制了一个类型,然后提供了一种特定的语法结构进行异常处理;

# try:
#     pass  # 被检测的代码
# except 异常类型:
#     pass   # 出现异常执行的逻辑
# else:
#    pass
# finally

f = open("pickle_test","rb")
while True:
    try:
        print(next(f))
    except StopIteration:
        f.close()
        break
~~~

~~~ python

~~~

## python小项目练习

~~~ python
import turtle
import copy
from random import randrange
import pygame
"""
贪吃蛇游戏分析:
1.我们写一个square 方法在面板上画出一个方块,让方块来代替我们蛇的身体的一部分 使用turtle 画笔
2.我们定义一个蛇的变量 snake 由三个坐标组成,我们通过snake的坐标调用square函数生成三个方块当做蛇的身体
3.然后我们让蛇的身体动起来,我们制定移动目标,aim(默认移动方向) ,移动的路径move_dir(需要键盘监控) 我们通过蛇头的重新定义成新坐标来表示移动,尾巴
随着蛇头前进,尾巴去掉;然后刷新面板
4.上一步我们可以正常移动了,那么这里我们使用square生成方块,随机生成坐标当做食物,这里有一个判断,如果食物(坐标)和蛇头(坐标)一样.我们就当做把食物吃掉了 当次不再
删除尾巴,我们吃了一个方块食物长大了;
5.游戏终止控制: 蛇头出了边界和吃到了自己的身体(in snake or not inside)表示游戏结束;
"""


snake = [[0,0],[0,10],[0,20]]  # 定义一个蛇,他的属性 由三个块组成,坐标分别是
aim = [0,10]  # 默认移动方向
food = [0,10]  # 给食物初始化


def inside(head):  # 设置蛇的活动边界
    return -260 < head[0] < 240 and -250 < head[1] < 250


def move_dir(x,y):  # 蛇的移动方向
    aim[0] = x
    aim[1] = y


def square(x,y,size,color):  # 定义方法画出方块  引用模块海龟画图
    turtle.penup()
    turtle.goto(x,y)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def snake_move():  # 头上加一个方块,尾巴减去一个,朝着一个方向(定义方向)走就可以了
    head = copy.deepcopy(snake[-1])  # 取出头的位置,重新赋值,按照我们指定的方向 然后重新画蛇的身体
    head = [head[0]+aim[0],head[1]+aim[1]]
    if head in snake or not inside(head):
        print("game over")
        return
    if food == head:
        food[0] = randrange(-20,20)*10
        food[1] = randrange(-20,20)*10
    else:
        snake.pop(0)  # 蛇数据的0号位置删除(如果没有吃到食物就正常移动的删除尾巴,迟到了就不删除)
    snake.append(head)
    turtle.clear()
    # 画食物:
    square(food[0],food[1],10,"green")
    for body in snake:  # 使用方块函数画出蛇的身体
        square(body[0], body[1], 10, "black")  #
        turtle.update()
    turtle.ontimer(snake_move, 200)


turtle.setup(500,500)
turtle.tracer(False)  # 把画的过程改为False 不再展示画图过程
turtle.hideturtle()  # 隐藏画笔
# 监听键盘
turtle.listen()
turtle.onkey(lambda: move_dir(0,10),"Up")
turtle.onkey(lambda: move_dir(0,-10),"Down")
turtle.onkey(lambda: move_dir(-10,0),"Left")
turtle.onkey(lambda: move_dir(10,0),"Right")

snake_move()
turtle.done()




##  hit flight games
# -*- utf-8 -*-
"""
在打飞机的游戏中,我们考虑的思路和问题
1.画出面板,设置大小,名字,logo,背景色 然后 blit on screen;
2.画飞机:开辟一个变量空间接收飞机图片的路径,然后 blit on screen;
3.让飞机移动: 监听事件 for event in pygame.event.get() 然后让飞机左右(上下)移动;
4. 仿照2中的画飞机画出敌机(enemy) 让敌机移动,创建列表设定飞机个数,循环出现飞机的移动 设定边界问题出界返回下降1;
5.参照飞机的位置画出子弹,让子弹y-进行向上移动;子弹如果出边界删除,子弹如果和敌机的相撞,敌机和子弹一起删除;
6.给游戏添加背景音乐和碰撞音效
7.画游戏面板的分数和游戏结束画面
在学习中的优秀思路:
 1. 在敌机移动的过程中 撞边界返回 只需要把移动的步长*-1 就是向相反的方向移动;
 2.飞机碰撞检测中,使用毕达哥拉斯定义(勾股定理) 进行判断
 def distance(b_x,b_y,e_x,e_y):
    a = b_x - e_x
    b = b_y - e_y
    return math.sqrt((a*a)+(b*b))
 如果 a 和 b 的坐标小于某一个值 就说明他们碰撞饿了; 
attention: 游戏的更新和判断方法的严谨性;

"""
import pygame,random,math

pygame.init()  # function  initialize

screen = pygame.display.set_mode((500,500))  # set up parameter of board; argument is a tuple

pygame.display.set_caption("flight_games")  # set up title of board

icon = pygame.image.load(r"images\icon.jpg")   #
pygame.display.set_icon(icon)  # introduce an address of pic_logo

bgImg = pygame.image.load(r"images\background_flight_shoot.jpg")  # introduce bg

flight = pygame.image.load(r"images\plr.jpg")  # hero flight attribute
flight_x = 220
flight_y = 450
flight_step = 0

enemy_number = 5  # numbers of enemy
bullets = []  # save the bullets.
# add music
# pygame.mixer.music.load("")  # load music
# pygame.mixer.music.play(-1)  # play music as loop
# add boom music
# bobmusic = pygame.mixer.Sound("")
# add score
score = 0
# create word-font
font = pygame.font.Font("freesansbold.ttf",32)
is_over = False  # judge game status;


def show_over():
    if is_over:
        text = f"game over"
        over_render = font.render(text,True,(255,0,0))
        screen.blit(over_render,(200,200))


def show_score():
    text = f"score:{score}"
    score_render = font.render(text,True,(255,255,255))  # 渲染
    screen.blit(score_render,(10,10))


class Bullet():
    def __init__(self):
        self.img = pygame.image.load(r"images\bullet.jpg")
        self.x = flight_x+20
        self.y = flight_y+5
        self.step = -2

    def hit(self):
        global score
        for e in enemys:
            if distance(self.x, self.y, e.x, e.y) < 30:  # the bullet got enemy
                # bobmusic.play()
                bullets.remove(self)
                e.reset()
                score += 10


def show_bullet():
    for b in bullets:
        screen.blit(b.img,(b.x,b.y))
        b.hit()
        b.y += b.step
        if b.y < 0 and b not in bullets:
            bullets.remove(b)
            print("remove_bullet")


def distance(b_x,b_y,e_x,e_y):
    a = b_x - e_x
    b = b_y - e_y
    return math.sqrt((a*a)+(b*b))


def move_flight():
    global flight_x,flight_y,flight_step,running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # listing keyboard
            if event.key == pygame.K_RIGHT:
                flight_step += 1
            elif event.key == pygame.K_LEFT:
                flight_step -= 1
            elif event.key == pygame.K_SPACE:  # bullet shoot
                bullets.append(Bullet())

        if event.type == pygame.KEYUP:
            flight_step = 0
    flight_x += flight_step


class Enemy():
    def __init__(self):
        self.img = pygame.image.load(r"images\ene.jpg")
        self.x = random.randrange(0,450)
        self.y = random.randrange(0,100)
        self.step = 1

    def reset(self):
        self.x = random.randrange(0,450)
        self.y = random.randrange(0,100)


def enemy_dir():  # produce enemy
    global is_over
    for e in enemys:
        screen.blit(e.img,(e.x, e.y))  # draw enemy_flight(random(x,y)
        e.x += e.step
        if e.x > 450 or e.x < 0:
            e.step *= -1
            e.y += 20
        if e.y > 450:  # game over
            is_over = True
            print("game over")
            enemys.clear()
def flight_out():  # over flow of coordinate
    global flight_x
    if flight_x > 450:
        flight_x = 450
    if flight_x < 0:
        flight_x = 0
# loop structure  update the board;（main structure）
enemys = []  # a list to enemys
for i in range(enemy_number):  # produce the enemy
    enemys.append(Enemy())
running = True
while running:
    screen.blit(bgImg, (0, 0))  # background on board ## <display.update>
    screen.blit(flight, (flight_x, flight_y))  # draw flight at (225,450)
    show_score()  # show score
    flight_out()  # judge flight outer
    move_flight()  # move flight
    enemy_dir()
    show_bullet()
    show_over()
    pygame.display.update()
~~~

## 安装辅助控件 软件常见问题 收集:

~~~python
安装pip和导入包出现问题
解决方法如下：
1.解决办法升级设置工具（可能pip没有升级，使用升级就会自动升到系统的最高级了）
pip install --upgrade setuptools

2.升级pip安装工具
python -m pip install --upgrade --force pip

pip3:

pip3 install --upgrade pip （pip3的安装）

3.有人说是版本的问题
pip install setuptools==33.1.1 可以试着去做升级

自己遇到的是这样，在第二步的时候就解决问题了，也有可能在下载的过程中中断的问题，有可能是网络不稳定的问题，可以尝试多试几次或者隔天安装。
直接在pycharm 上setting , project interpreter 点击+ 号然后搜索框搜索需要下载的包,下载即可
~~~

学习过程中的问题和解决方案

~~~ python
1. 画笔画图工具  turtle  
import turtle   # 导入模块
turtle.setup(size(x),size(y))  # 设置面板大小
turtle.tracer(False)  # 不显示画的轨迹
turtle.hideturtle()  # 隐藏画笔
turtle.listen() # 监听
turtle.onkey(lambda:object_method,"Up") # 监听键盘
turtle.done()  # 让面板保留
turtle.penup()  # 抬笔
turtle.goto(x,y)  # 指向指定的位置
turtle.color(color) # 设置画笔颜色
turtle.pendown()  # 落笔
turtle.begin_fill()  # 开始画图形
	pass
	turtle.forward(size)  #画笔的前进距离
    turtle.left(90) # 画笔向左旋转90度
turtle.end_fill()  # 画结束
turtle.update  # 更新画笔
turtle.ontime(object,time)  # 画笔的等待操作


2.游戏界面设置模块 pygame
import pygame
pygame.init()  # 初始化
pygame.display.set_mode((sizex,sizey))  # 设置面板大小
pygame.display.set_caption("面板名")  # 设置面板名字
pygame.display.set_icon(pygame.image.load("图片路径"))  #设置面板logo
pygame.image.load("图片路径")  # 引入图片(例如背景bg 然后画出在screen.blit(bg,(x,y))上)
pygame.mixer.music.load("路径")  # 加载音频
pygame.mixer.music.play(-1)  # 循环播放
pygame.mixer.Sound("路径")  # 加载音频
pygame.font.Font("字体",size)  # 在面板鞋子 设置字体
screen.blit(object,(x,y))  # 把object画在面板上
for event in pygame.event.get():  # 监听事件(affair)
    if event.type == pygame.QUIT:
        pass
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            pass  
pygame.display.uopdate()  # 界面的更新

        

~~~

## 二分查找算法

~~~PythoN
# 二分法 判断一个数组是否有自己需要的数字
lis = [2,4,5,7,11,22,57,68,89,98]
item = 98


def binary_search(lis, item):
    if len(lis) == 0:
        return False
    else:
        midpoint = int(len(lis)/2)  # 获得列表的长度
        if lis[midpoint] == item:
            return True
        else:
            if item < lis[midpoint]:
                return binary_search(lis[:midpoint], item)
            else:
                return binary_search(lis[midpoint:], item)


result = binary_search(lis,item)
print(result)
~~~
