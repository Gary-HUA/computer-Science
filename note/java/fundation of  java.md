### Basic Concept  of  java  :

1-1：

什么是java？ Java 有什么优点？

An: java is a computer language  . 

Java 具有一次编译 到处运行的特性。

1-2：

Java 编译期的运行过程： 

程序员编写的java源文件 经过编译生成.Class 字节码文件。 然后在JVM 运行 。 JVM通过不同的版本针对不同的操作系统，使.class 文件可以在不同的系统运行。

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps1.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps2.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps3.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps4.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps5.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps6.png) 

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps7.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps8.png) 

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps9.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps10.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps11.png)  

编译期  

1-3 ：

### Java的开发环境  以及JVM JDK JRE 的关系：

JDK: java development kit   （java开发工具）

JRE: java run-time environment  (java 运行环境)

JVM:  java virtual machines(java 虚拟机)  

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps12.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps13.png)一个java程序最小的运行环境是JRE ，一个java程序最小的开发 环境是JDK  

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps14.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps15.png)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps16.png) 

JAVA 的布局安装...

Eclipse的安装（一个集成（IDE）开发环境） 

Java的语法：

2-1:

### JAVA 变量 ：

2-1-1： 什么是变量？

变量就是指代在内存中开辟的存储空间，存放运算过程中使用的数据

2-2-2： 变量的声明和使用：

变量的声明： 变量在使用之前需要声明，未经生命的变量不能使用。一条语句可以声明多条变量。  

变量的声明包括两方面：

\1. 变量类型

\2. 变量名

Int  a=2 ;// 定义一个整形变量 a,赋值为2.

Int  b;// declare a variable of integrated b.

Int d,e=5;

Int  c=a+b;// 把a+b的值赋值给整形变量C

 

2-2-3：变量的命名规则和初始化 

 可以有字母，数字 “-”和 $ 组成。

变量不可以数字开头

Java区分大小写

不能使用java中的保留字 （int,long,for ,if, 等）

建议：Java在命名中需要做到见名知意  驼峰命名法，

初始化： 在第一次使用之前需要对变量进行初始化赋值； 

Int a=0; // 声明一个整形变量a, 并初始化赋值为0；

2-3-4：变量的访问 

我们把对变量的访问理解为  变量名是一个代词， 其实对变量的访问就是对内存中的数据的访问和操作。  

变量的操作必须与类型匹配；

 

### java的基本类型：

   ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps17.jpg)

Byte , short , int ,long ,float , double, char , boolean.

 

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps18.jpg) 

1-1：

int 类型 最常见的整数类型；

-2^31~2^31-1;

Long 类型： -2^63~2^63-1  是为了补充int类型不足；

计算时间： 从1970年一月一日0时到此时此刻的时间毫秒数；

long  time = System.currentTimeMillis();

System.out.println(time);

Double  类型：

双精度浮点型， 因为双精度浮点型的精度误差问题 所以我们在需要精确计算结果的时候可以使用 Big Decimal 类来实现；

Char 类型  就是一个字符类型  ；他是用来存储一个字符，用‘’包含；

Boolean; 布尔类型 ：  有两个值，true, false; 

 

1-2：

### 转义符：

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps19.jpg) 

1-3：

基本类型的转换：

1）：自动类型转换；以小转大 就是把小的数据类型赋值给大的数据类型；

Double a =10;// 10 是整形 赋值给了double型。

2）：强制类型转换；

Int a =10.1;// 报错，10.1 是double  类型， 大转小  那么需要我们强制类型转换

Int a =(int)10.1;  

强制类型转换很可能会造成精度的丢失和数据的溢出；

例如： 

2-1：long a=1024*1024*1024*1024;// 1,099,511,627,776

 因为赋值数据是整形，现在把它赋值给长整形， 那么 在计算过程中就会出现数据的溢出问题 ，怎么处理？

Long a = 1024L *1024*1024*1024;// 提前在第一个数字后加上L  意思就是数字转换为长整形。那么这个数据的结果就是长整形了。

 

 

### 运算符和表达式：

 

1-1：

关系运算符：

\> ,<, >=, <=, ==, !=  一共六个；

关系运算符的结果是Boolean型的 所以他的结果就是true 或false ；

​		***\*int\**** num1=100;

​		***\*int\**** num2=10;

​		***\*boolean\**** a = num1<10;//false 

​		***\*boolean\**** b=num2>5;// true

​		System.***\**out\**\***.println(a+","+b);

结果是：

false,true

1-2： 

逻辑运算符；

&&  ||  ！  这三个符号就是逻辑运算符的  与  或  非 

与  就是and  和的意思。

或  就是 或者的意思。

非  就是否定 不是的意思。

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps20.jpg) 

 

​		***\*int\**** num1=100;

​		***\*int\**** num2=10;

​		***\*boolean\**** a = num1<150&&num1>10;//true 两个条件同时满足

​		***\*boolean\**** b = num2<5|| num2==10;// true 两个条件满足其中之一

​		System.***\**out\**\***.println(a+","+b);

结果是：

true,true

 

***\*int\**** num1=100;

​		***\*boolean\**** a = num1!=150;//true num1的值不等于150 非 取反的意思

​		System.***\**out\**\***.println(a);

结果是：

true

短路逻辑的问题 ：

Java中的逻辑运算遵循短路逻辑的原则 ；

什么意思呢？

当Boolean型 判断的结果为false的时候  那么它就不会执行，只有为真的时候才会执行判断的执行体

***\*int\**** a=5;

​		***\*int\**** b=4;

​		***\*if\****(a>b) {//短路逻辑的问题 如果a>b为真 那么没有短路 执行，反之则调到else；

​			 a=a+b;

​		}***\*else\**** {

​			 a=a-b;

​		}

​		System.***\**out\**\***.println(a);

结果是：

9

 

课后作业1；

使用java数据的基本类型和逻辑运算（短路逻辑）来判断一个叫小明的同学他懂得年龄是19岁，他的年龄是否是成年；（成年的条件是年龄大于等于18）。

***\*int\**** age =19;

​		***\*boolean\**** a=age>=18;//成年为true  未成年 为false

​		System.***\**out\**\***.println(a);

结果是：

true

课后作业2：

对于上一题 我现在不想把他的年龄确定为19岁，我想在控制台输入， 那么 我该怎么做？  提示：scanner 的应用

运算符和表达式

1-1：

算术运算符 ：+ - * / ++ -- % 

重点是 ++  -- 运算符 ：他们的作用是让自身自增 自减1

但是 符号放在前后是有差别的；

如果写在这个变量前就是表示这个变量在使用之前增或者减1；

写在变量之后就是表示这个变量时候之后增或者减1

***\*int\**** a=0;

​		***\*int\**** b=1;

​		/*	a++; 这时候的单纯的自增 没有参与运算 那么 结果都是一样的 在自身增减1

​			++b;

​		 * 

​		 */

​		

​		***\*int\**** c=a++;//参与运算  那么 就有先后顺序 ++ 在a后  那么就是 先赋值 再自增；

​		***\*int\**** d=++b;//就有先后顺序 ++ 在b前  那么就是 先自增  再赋值；

​		System.***\**out\**\***.println(c+","+d);// guess c=0 a=1;  d=2,b=2  因此 结果是0,2

 

 

赋值运算符 ‘=’

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps21.jpg) 

int a=5;// 这里的‘=’号就是赋值运算符；

1-2：

字符串拼接运算符‘+’

System.out.println(“welcome”+”欢迎”+a)；//welcome欢迎5就是结果

1-3：

三目运算符

Boolean表达式？表达式1：表达式2

表达式是判断条件 如果为true 那么执行表达式1 

false则执行表达式2

***\*int\**** age =19;

​		String a= age>18? "成年了":"未成年";//三目表达式；

​		System.***\**out\**\***.println(a);

结果是：

成年了

三目运算符的嵌套：

***\*int\**** age =0;

​	  String a= age>18?"成年了":(age==0?"婴儿":"未成年");//三目表达式嵌套；

​		System.***\**out\**\***.println(a);

结果是：

婴儿

 

### 分支结构：

程序在运行的过程中 根据不同的条件运行不同的语句；

If  语句 ：

 If （逻辑表达式）{// 逻辑表达式是一个boolean 型的结果 真或假

语句；//为真 执行语句 假就不会进入if 语句；

}

​       ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps22.jpg)

 If - else 语句 ：

​       ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps23.jpg)

 

If else 语句的嵌套；

输入一个分数，判断分数的等级

  ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps24.jpg)

 

Scanner scanner=new Scanner (System.in);

​		System.out.print("enter score:");

​		int score = scanner.nextInt();

// 成绩区间的判断

​		if (score >=0&&score<=100) {

​			if (score >90) {

​				System.out.println("great");

​			}else if (score>80) {

​				System.out.println("good");

​			}else if (score>60) {

​				System.out.println("common");

​			}else {

​				System.out.println("fail");

​			}

​		}else {

​			System.out.println("error enter again!");

​		}

 

Switch case 语句 ：

Switch case 语句是一个特殊的分支结构，根据整数的表达式选取不同的执行结构一般和break 联合使用；

Scanner scan =new Scanner (System.in);

​	System.out.println("enter the command num:");

​	int num =scan.nextInt();

​		switch (num){

​			 case 1:

​				 System.out.println("show the log sheet ");

​				 break;

​			 case 2 :

​		System.out.println("show the login sheet ");

​				 break;

​			 default :

 System.out.println("ERROR ! ENTER THE NUM AGAIN PLEASE.");

}

 

分支结构课后练习 ：

\1. 定义三个int 数，输入最大值；

2.成绩判断程序 ；(if else 的嵌套)

3.输入一个月份 判断有多少天；（switch case ）

 

 

### 循环结构

 

1. 什么是循环 ？

循环就是反复地执行某一个语句 （循环体  循环条件） 

2. While 语句  ：

While （Boolean 表达式）{

语句；

}

***\*int\**** a=10;

​		***\*while\****(a>=10&&a<20) {

​			System.***\**out\**\***.println("while 循环");

​			a++;//没有这句什么情况？

​		}

Break 的使用；

***\*int\**** a=10;

​		***\*while\****(a>=10&&a<20) {

​			***\*if\**** (a==15) {

​				***\*break\****;// 当满足if语句的判断时 跳出当前循环

​			}

​			System.***\**out\**\***.println("while 循环");

​			a++;

​		}

​	

Do - while 语句 ：先执行语句块 再判断 ；

 Do {

执行语句；

}while （Boolean 表达式）；

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml6704\wps25.jpg) 

***\*int\**** a =0;

​		***\*do\**** {

​			a++;// 不管条件是否满足 ，我们都会先执行

​			System.***\**out\**\***.println(a);

​		}***\*while\**** (a<=5);

​		// 结果是123456  ？为什么有6  因为我们先执行 后判断，

​		//那么 当a=5的时候 我们依然执行一次+1=6 同时输出 判断不再满足条件

使用do while 和 while  do 比较

Scanner scan=***\*new\**** Scanner(System.***\**in\**\***);

​		***\*int\**** pwd;

​		***\*do\**** {

​			System.***\**out\**\***.println("enter password:");

​			pwd=scan.nextInt();

​		}***\*while\**** (123456!=pwd);

 

Scanner scan=***\*new\**** Scanner(System.***\**in\**\***);

​		***\*int\**** pwd;

​			System.***\**out\**\***.println("enter password:");

​			pwd=scan.nextInt();

​			***\*boolean\**** flag=***\*true\****;// 开关

​		***\*while\**** (123456!=pwd) {

​			System.***\**out\**\***.println("error");

​			flag=***\*false\****;

​			***\*break\****;

​			

​		}

​		***\*if\**** (flag) {

​			System.***\**out\**\***.println("welcome");

​		}

​		

For 语句：

用于实现固定次数循环；例如 累加 阶乘等

 For  (表达式1；表达式2；表达式3){

语句；

}

​	***\*int\**** num=10;

​		***\*for\**** (***\*int\**** i=0;i<num;i++) {

​			System.***\**out\**\***.println("for structure loop");

​		}

 

循环中的 break 和 continue;

Break 在循环语句中 跳出当前循环 执行循环外边的语句 ；

Continue 跳出循环中剩余的语句 执行下一次循环

***\*int\**** num=10;

​		***\*for\**** (***\*int\**** i=0;i<num;i++) {

System.***\**out\**\***.println("i=5");			

***\*if\**** (i==5) {//当i的值是5时，不执行循环体 再次回到循环判断

​				***\*continue\****;

​			}

​			System.***\**out\**\***.println("for structure loop");

​		}

所以 原本结果应该是10次输出 结果是

for structure loop

for structure loop

for structure loop

for structure loop

for structure loop

i=5

for structure loop

for structure loop

for structure loop

for structure loop

 

 

课后练习：

1.获取一个十以内的数字 三次机会进行猜数字游戏  系统提示数字大了 小了 正确 ；

\2. 加法 运算器  

出十道加法运算题 控制台输入结果 系统判断结果是否正确，并统计得分情况  一共100 分 

 

 

### 数组

什么是数组？

相同数据类型的元素组成的集合。

这些元素按照线性顺序排列， 线性顺序就是除了第一个元素 ，其他的元素都有唯一的前驱元素。除了最后一个元素 每一个元素都有后继元素；

可以通过下标的方式遍历访问数组中的每一个数组元素；

数组的创建：

Int [] arr =new  int []  数组类型 数组类型引用 数组长度；

数组的初始化：

数组声明的同时初始化；

Int [] arr={10,20,30};

数组的赋值：

Int [] arr;

......

Arr=new int []{10,20,30};// 元素的个数就是数组的长度

 

数组的访问:

调用数组的length 属性可以获取数组的长度；

Int  len=arr.length;

数组的下标以0为开始 ，那么我们就可以通过下标进行访问数组中的每一个元素；下标的范围是0~(n-1).

 

​		***\*int\**** [] arr = ***\*new\**** ***\*int\**** [5];

​		***\*for\**** (***\*int\**** i=0;i<arr.length;i++) {

​			arr[i]=i;

​			System.***\**out\**\***.println(arr[i]);

​		}

​	}

 

:01234 

 

​		***\*int\**** [] arr = ***\*new\**** ***\*int\**** [5];//1.

​		***\*int\**** [] arr1;//2.

​		arr1=***\*new\**** ***\*int\****[] {10,20,30};

​		***\*int\**** [] arr2= {10,25,30};//3.

​		//  下面三种显示的都是arr引用的地址，不是具体的参数值；数组需要遍历才能看到每一个值；

​		System.***\**out\**\***.println(arr);

​		System.***\**out\**\***.println(arr1);

​		System.***\**out\**\***.println(arr2);

​		// 遍历输出；traverse arrays.outprint;

​		***\*for\**** (***\*int\**** i=0;i<arr2.length;i++) {

​			System.***\**out\**\***.println(arr2[i]);

​		}

}

[I@34c45dca

[I@52cc8049

[I@5b6f7412

10

25

30

数组的复制扩展：两种：

数组的长度在创建之后不能改变，所谓的扩展就是创建一个更大的数组将原来的数组元素复制给新数组；

 

​		String [] arr=***\*new\**** String [] {"gary","hua","liu","zhang","mei"};//1.

​		String [] arr1;//2.

​		arr1=***\*new\**** String []{"mei","hau","zhang","wang","ben"};

​		String [] arr2= {"mei","hau","zhang","wang","ben"};//3.

​		System.***\**out\**\***.println(arr2.length);

​		// 扩展数组1；

​		String [] arr4=***\*new\**** String [6];

​		System.**arraycopy**(arr, 0, arr4, 0, 2);// 参数：从arr 中的第0个元素开始复制到arr4中 第0个元素开始，一共两个元素

​		***\*for\**** (***\*int\**** i=0;i<arr4.length;i++){

​			System.***\**out\**\***.println(arr4[i]);

​			

​		}

​		// 扩展数组2：arrays.copyOf方法；自我扩容

​		arr2=Arrays.**copyOf**(arr2, arr2.length+1);

​		System.***\**out\**\***.println(arr2.length);

​		arr2[arr.length]="ggg";

​		***\*for\**** (***\*int\**** i=0;i<arr2.length;i++) {

​			System.***\**out\**\***.println(arr2[i]);

​		}

### Java方法（method）

什么是方法？

Java中的方法function 就是行为和动作；

\1. 方法的声明：

方法用于封装一段特定的逻辑功能，方法的主要要素有：

方法名，参数列表，返回值

方法是由修饰符，返回值类型(void，基本类型，引用类型)，方法名，参数列表 返回值组成；

如果在void 中使用return 作用是结束方法的调用；

参数列表：方法的参数是在调用时传递给方法的，被方法处理的数据；

 

Public int  number (int  x，int  y){

//方法体;

Int sum;

Sum=x+y;

Return sum;
}

 

​		Cla c=***\*new\**** Cla();// 创建一个Cla类型的引用对象，c direct to Cla();

​		c.name="gary";//assignment  gary to name ;

​		System.***\**out\**\***.println(c.name);//

​		***\*int\**** sum=c.sum(5, 6);// sum方法的调用 ，我们把值返回给sum 

​		System.***\**out\**\***.println(sum);

​	}

}

//创建一个Cla 类 ， 类中有属性和方法；

 ***\*class\**** Cla{

​	String name;

​	***\*int\**** age;

// sum 方法， 求两个参数x y 的和；

​	***\*public\**** ***\*int\**** sum(***\*int\**** x,***\*int\**** y) {

​	***\*return\**** x+y;	

}

}

总结：

\1. java的基本类型；

java8种基本类型byte,short ,int ,long float,double,char,boolean，转换，基本类型的使用

\2. 转义字符 \ ‘\n’ ‘\t’’\\’’\”’

\3. Java的算术运算符；+-*/%  ++-- 

\4. Java的关系运算符：> < >= <= != ==

\5. Java的逻辑运算符：&& || ！ 逻辑运算的嵌套， 

\6. Java的赋值运算符 = 

\7. Java的三目运算符：String  age=10>18?””:”未成年”； 

\8. Java的分支结构：

4-1：if  If else  if else if嵌套  

4-2：switch case ;

\9. Java 的循环结构:

5-1:while 循环 当循环；

5-2:do  while 循环 直到型循环

5-3:for 循环 

\10. 数组： 数组的引用声明，赋值，遍历，扩展（扩容）

\11. 方法：方法的定义，方法的调用和实现，

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 