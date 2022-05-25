

# **网页设计:**

## 第一章:WEB概述:

web三要素: 

1.向服务器发送请求,下载服务器中的网页,然后执行HTML显示出内容;

2.服务器:接受浏览器的请求,发送相应的页面到浏览器;

3.HTTP协议,浏览器和服务器的通讯协议;

### HTML 用来勾勒网页的结构和内容

什么是HTML(hyperText MarkUp Language)超文本标记语言,纯文本类型的语言;

用来设计网页的标记语言,用该语言编写文件,以.html or .htm为后缀,有浏览器就是执行,HTML页面上,可以嵌套脚本语言编写的程序段;

XML和HTML和联系:

XML:可扩展标签语言,标签,属性,标签的嵌套关系都是可扩展(自定义)的;用来存储或者传输数据;

HTML: 超文本标签语言,语法固定的,主要用来显示数据,有一些特定的版本严格遵守XML规范;可以将HTML理解为标签固定的XML;

单标签 <student/>(无内容的双标签),双标签<student></student>;

创建web项目注意点: 在eclipse中 在install new software 中给软件安装插件,切换到javaee 创建文件,然后报错右击deployment 生成;

~~~html
<!-- HTML唯一的根元素,只能出现一次;元素是标签属性内容的统称 -->
<!doctype html>  <!-- 版本声明 一下所有的都是HTML5的 -->
<HTML>
	<!-- 只有一对head and body;head是对网页的基本的配置 body是网页的具体的内容 -->
	<head>
		<!-- title,meta,link,http-equiv,charset -->
		<meta charset="utf-8">  <!-- 声明网页的编码 -->
		<title>http:www.baidu.com/test_L</title><!-- 声明网页的标题 -->>
	</head>
	<body>
		HTML is running!,很高兴认识你;<!-- 内容 -->
		<h1>  <!-- 文章标题元素 <h1...h6>-->
		第一章:一级标题.
		</h1>   
		<h2>
		第二章:二级标题
		</h2>
		这里是没有段落的内容,让我们显示下内容有什么不同;
			<p>
				这是段落的内容
			</p><!-- 这是段落,独立的一行 -->
			<p>
				这是第二段段落的内容
			</p>
		<!-- 列表(有序和无序)可以嵌套 -->
			<!-- 有序列表 排序 -->
		<ol>
			<li>这是有序列表1</li>
			<li>这是有序列表2</li>
		</ol>
		<!-- 无序列表 前边加. -->
		<ul>
			<li>这是无序列表1</li>
			<li>这是无序列表2</li>
			<li>这是无序列表3</li>
		</ul>
		<!-- 有序套无序的嵌套 -->
			<ol>
				<li>
					河南省
					<ul><li>周口市</li></ul> 
					<ul><li>驻马店市</li></ul>
				</li>
			</ol>	
	</body>
</HTML>
~~~

### 分区div 

分区,可以对不同的内容进行特定的修饰,从而不影响其他的区域 

~~~html
<!-- HTML唯一的根元素,只能出现一次;元素是标签属性内容的统称 -->
<!doctype html>  <!-- 版本声明 一下所有的都是HTML5的 -->
<HTML>
	<!-- 只有一对head and body;head是对网页的基本的配置 body是网页的具体的内容 -->
<head>
	<!-- title,meta,link,http-equiv,charset -->
	<meta charset="utf-8">  <!-- 声明网页的编码 -->
	<title>http:www.baidu.com/test_L</title><!-- 声明网页的标题 -->
</head>
	<body>
	<!-- 分区,可以对不同的内容进行特定的修饰从而不影响其他的区域 -->
	<!-- logo area -->
		<div>
			<p>这是第一个区域的内容,logo区域</p>
		</div>
	<!-- content area -->
		<div style="color:red;">
		<h1>
		 	这是内容区.宫保鸡丁的制作方法;
		 </h1>
		 <h2>
		 	<p>步骤1: 洗锅烧油</p>
		 	<p>步骤2:开始做</p>
		 	<p>步骤3:结束</p>
		 </h2>
		</div>
	<!-- version area -->
		<div>
		<p>版权所有,违者必究</p>
		</div>
	</body>
</HTML>
~~~

 ### 行内元素

~~~html
<!-- HTML唯一的根元素,只能出现一次;元素是标签属性内容的统称 -->
<!doctype html>  <!-- 版本声明 一下所有的都是HTML5的 -->
<HTML>
	<!-- 只有一对head and body;head是对网页的基本的配置 body是网页的具体的内容 -->
<head>
	<!-- title,meta,link,http-equiv,charset -->
	<meta charset="utf-8">  <!-- 声明网页的编码 -->
	<title>http:www.baidu.com/test_L</title><!-- 声明网页的标题 -->
</head>
	<body>
	<!-- 元素显示方式 span(style),i(倾斜),em(倾斜),b(加粗),strong(加粗),u(下划线),del(删除线)-->
	<!-- 行内元素,不会独立成行<span style="color:red"> 从一段内容选择一部分进行修饰 -->
	<p>
	这里展示span,地址:
		<span style="color:green;"> 河南省周口市</span>
	</p>
	<p>
	这里展示i,地址:
		<i>河南省周口市</i>
	</p>
	<p>
	这里展示b,地址:
		<b>河南省周口市</b>
	</p>
	<p>
	这里展示u,地址:
		<u>河南省周口市</u>
	</p>
	<!-- 空格折叠  默认多个空格,制表符,换行当成一个.br(换行),&nbsp(空格),&lt(小于号)-->
	大家好,   我一个人,<br>这里有多个		制表符,我需要&nbsp;&nbsp;&nbsp;&nbsp;多个空格展示;
	
	
	</body>
</HTML>
~~~

### 图像和超链接

~~~html
<!-- HTML唯一的根元素,只能出现一次;元素是标签属性内容的统称 -->
<!doctype html>  <!-- 版本声明 一下所有的都是HTML5的 -->
<HTML>
	<!-- 只有一对head and body;head是对网页的基本的配置 body是网页的具体的内容 -->
<head>
	<!-- title,meta,link,http-equiv,charset -->
	<meta charset="utf-8">  <!-- 声明网页的编码 -->
	<title>http:www.baidu.com/test_L</title><!-- 声明网页的标题 -->
</head>
	<body>
	<!-- 图像元素<img>(行内元素,左右排列) -->
	<p>
		平级(同一文件夹下的图片相对路径的演示)绝对路径不建议,路径更改会有错误
		<img src="food.jpg"/>
		下级(子文件夹下的图片)
		<img src="image\food.jpg"/>
		<!-- 图片在网页的上级 -->
		<img src="..\images\food.jpg">
		<!-- 工作中一般情况:使用images类似的文件夹 -->
		<img src ="..\images\food.jpg">
	</p>
	</body>
</HTML>


<!--超链接 -->
<!-- HTML唯一的根元素,只能出现一次;元素是标签属性内容的统称 -->
<!doctype html>  <!-- 版本声明 一下所有的都是HTML5的 -->
<HTML>
	<!-- 只有一对head and body;head是对网页的基本的配置 body是网页的具体的内容 --><!-- HTML唯一的根元素,只能出现一次;元素是标签属性内容的统称 -->
<!doctype html>  <!-- 版本声明 一下所有的都是HTML5的 -->
<HTML>
	<!-- 只有一对head and body;head是对网页的基本的配置 body是网页的具体的内容 -->
<head>
	<!-- title,meta,link,http-equiv,charset -->
	<meta charset="utf-8">  <!-- 声明网页的编码 -->
	<title>http:www.baidu.com/test_L</title><!-- 声明网页的标题 -->
</head>
	<body>
	<!--  超链接<a>行内元素(就是不分段落,在同一行编写) -->
	<!--  <a href="" target="">文本</a>  -->
	<p>
	href属性:链接 URL
	target属性:目标打开方式,可取值为_blank(开新窗口),_self(当前窗口)等
		<a href="https://baike.baidu.com/" target="_blank">百度百科
		
		</a>
		<!-- 超链接的特殊用法:(链接到当前网页的某个位置(锚点))
		必须提前声明这个锚点
		 -->
		 <p>
		 锚点的<a name="mao">属性</a>:
		 <a href ="#mao">这里是回来锚点的属性</a>
		 顶部默认就是锚点,没有名字;
		 <a href="#">这是默认的顶部锚点</a>
		 </p>
	</p>
	</body>
</HTML>

~~~

### 表格和表单:

 表格样式：可以使用box模型；
表格的边框合并：border-collapse:collapse 合并相邻的边框；

~~~ html
<body>
	<!--  表格 (块结构)
	需要<table><tr><td>这三对标签来定义表格,创建行,创建列;
	表格 的基本结构,colspan/rowspan(单元格合并) 就是跨行跨列
	跨行,
	跨列
	行分组
	-->
		<table border="1" cellspacing="0" width="30%">
			<tr>
				<td>两行两列</td>
				<td>两行两列</td>
			</tr>
			<tr>
				<td>两行两列</td>
				<td>两行两列</td>
			</tr>
		</table>
	
			<!-- 跨行跨列的演示 -->
			
				<table border="1" cellspacing="0" width="30%">
			<tr>
				<td colspan ="2">两行两列</td>
				<!-- 跨行需要释放掉的内容 <td>两行两列</td>-->
			</tr>
			<tr>
				<td>两行两列</td>
				<td>两行两列</td>
			</tr>
		</table>
			
		<table border="1" cellspacing="0" width="30%">
			<tr>
				<td rowspan="2">两行两列</td>
				<td>两行两列</td>
			</tr> 
			<tr>
				<!-- 跨行需要释放掉 <td>两行两列</td>-->
				<td>两行两列</td>
			</tr>
	
		</table>
		
		<!--  行分组  将行分为不同的组,以助于我们进行修饰
		表格可以划分为三个部分,{表头,表主体,表尾 } +(行分组<thead><tbody><tfoot>)
		 -->
		 <table border="1" width="30% ">
		 <thead>
		 		<tr>
		 			<td>编号</td>
		 			<td>产品名</td>
		 			<td>金额</td>
		 		</tr>
		 </thead>

		 <tbody style ="color:blue">
		 	<tr>
		 		<td>1</td>
		 		<td>电脑</td>
		 		<td>5000</td>
		 	</tr>
		 	<tr>
		 		<td>2</td>
		 		<td>显示器</td>
		 		<td>2000</td>
		 	</tr>
		 
		 </tbody>
		 	
		 	
		 <tfoot>
		 	<tr>
		 		<td colspan = "2">合计</td>
		 		<td>7000</td>
		 	</tr>
		 </tfoot>
		 </table>
	</body>

<!--表单: -->
<!-- HTML唯一的根元素,只能出现一次;元素是标签属性内容的统称 -->
<!doctype html>  <!-- 版本声明 一下所有的都是HTML5的 -->
<HTML>
	<!-- 只有一对head and body;head是对网页的基本的配置 body是网页的具体的内容 -->
<head>
	<!-- title,meta,link,http-equiv,charset -->
	<meta charset="utf-8">  <!-- 声明网页的编码 -->
	<title>http:www.baidu.com/test_L</title><!-- 声明网页的标题 -->
</head>
	<!--  表单  表单元素,表单控件:
	表单元素: 圈定一个范围,在这个范围的可以发送给服务器,数据提交的范围;
	表单控件:就是设定一个区域给用户用于输入数据; 
	
	-->
	<body>
	<!--  表单元素:<form> attribute: action 声明数据提交的目标,method/enctype : -->
	<form action = "http:www.baidu.com">
		<!-- 表单控件   12个 有两类:
		input元素 9个,他们之间用type属性区分:
		三个其他元素,标签名不同;
		
		-->
		<!-- 文本框: value maxlength readonly 三种属性在文本和密码属性通用;-->
		<p>
		账号:<input type="text" value="请输入账号" maxlength="20"  readonly/>
		</p>
		<!-- 密码框: -->
		<p>
		密码:<input type="password" value="请输入密码"maxlength="20">
		</p>
		<!-- 单选框(type=radio/),复选框(type="checkbox"/) -->
		<p>
		性别:
		<input type ="radio"  name="sex" checked/>男  <!--  name 是分组名,同组"radio"互斥 checked 默认选中 -->
		<input type ="radio" name="sex"/>女
		
		</p>
		<!-- 复选框: checked:设置默认选中 -->
		<p>
		爱好:
		<input type="checkbox" checked/>音乐
		<input type="checkbox"/>读书
		<input type="checkbox"/>书法
		<input type="checkbox"/>舞蹈
		
		</p>
		<!--  隐藏框, 文件框 -->
		<p>
		需要上传的文件:<input type="file"/>
		
		</p>
		<p>
		<!--  在表单中包含用户不需要看到的数据 input type="hidden" -->
		这是隐藏框:<input type="hidden" value="abc"/>
		</p>
		<!--   按钮:submit(提交) , reset button(需要通过js我们自己设置功能) -->
		 <input type="submit" value="注册"/>
		 <input type="reset" value="重置"/>
		 <input type="button" value ="普通按钮" />
		<!--  其他三个 label(用来管理表单中的文本和控件绑定一起.单选多选增加受力面积 ) 
		select (多个单选数量太多,平常我们需要缩起,使用的时候展开 selected 默认; value属性  )
		textarea(文本域,适合使用长的信息 cols,rows readonly 设置可写的行列文字和权限)
		  -->
		<p>
		<!--  id 是元素的唯一标识.任何元素都可以设定id,程序员有义务保障元素的id不重复 -->
		<input type ="checkbox" id="lab"/>
		<label for="lab">我已阅读并自愿遵守此协议</label>
		</p>
		<p>
		城市:
		<select>
			<option>请选择:</option>
			<option>上海</option>
			<option>深圳</option>
			<option>广州</option>
			<option selected>香港</option>
			<option>澳门</option>
		</select>
		</p>
		<p>
		留言板:
		<textarea cols="30" rows="3">这是文本域的默认值
		</textarea>
		</p>
	</form>

	</body>
</HTML>
~~~



## 第二章:CSS 用来美化网页

~~~ html

<!doctype html>  
<HTML>
<head>
	<meta charset="utf-8">
	<title>http:www.baidu.com/test_L</title>
	<style>
		/* 这是css的注释方式   这里演示的是内部样式 写在head的style中*/
		h3{
		color:blue;
		}
		/*外部样式的引用 写在head中*/
	</style>
		<link rel ="stylesheet" href="demo.css"/>  <!--  引用外部样式一个叫demo.css 的文件 -->
</head>
	<!-- CSS 层叠样式表(cascading style sheets)
	样式定义如何显示html元素
	样式通常储存在样式表中
	如何使用:
	内联样式:样式定义在单个的html 元素中
	内部样式:定义在HTML的头元素中
	外部样式:定义在外部的css文件中(.css文件 由HTML页面引用样式文件)
	-->
	<body>
	<h1 style ="color:red;">css</h1>  <!--  内联样式,在单个的HTML元素中 -->
	<h3>css的三种用法:</h3>   <!--  内部样式在head中写,在整个网页使用 -->
		<p>内联样式</p> 
		<p>内部样式</p>
		<p>外部样式</p>
	</body>
</HTML>
<!-- 这里是一个css的文件的引用的文件-->
/* 这是css的注释方式   这里演示的是外部样式*/
p{
	color:brown;
}
~~~

### css的特性和选择器

~~~ html
<!-- CSS 层叠样式表(cascading style sheets)
	我们学习css就是选择器和声明; p{font="23" color:"red"}
	css 的规则特性:
	继承性:父元素的css声明可以被子元素继承 如字体,颜色等;
	层叠性:同一个元素如果存在多个css规则,对于不冲突的声明可以叠加.
	优先级:同一个元素的css规则,如果存在冲突,那么就一优先级高的为准;
	-->
	<!--  css 选择器: 
	就是用来选择页面的元素的:可以选择多个或一个.
	1.通过元素名p,body,等作为目标.
	2.类选择器,根据元素的class属性来选择 .className {color:red;}
	3,id选择器, # id{}
	4.选择器组:选择器声明以逗号隔开的选择器列表 ,将一些相同规则作用于多个元素
	5.派生选择器: 后代选择器,子元素选择器;
	-->
<!doctype html>
<HTML>	
<head>	
	<meta charset="utf-8">  
	<title>http:www.baidu.com/test_L</title>
	<style>
	/* css的继承性: */
	body{
		font-family:"微软雅黑","文泉驿正黑","黑体"
	}
	/*层叠性: */
	h1{
	color:red;/*.......*/font-size:50px;
	}
	/*优先级: 同一个声明,效果以后者为准,就近原则 */
	h2{
	color: green;/*.....*/color:brown;
	}
	/* 类选择器: */
	.important{
	 color:pink;
	}
	.noneit{
	 color: green;
	}
	/* id 只可以选择唯一的不能有重复 */
	#p4 {
	color:red;
	}
	/* 选择器组:选择一组选择器,选中每个选择器所对应的目标的并集.  */
	.important,#p4,#p5{
	 font-weight:bold;
	}
	/* 派生选择器: 选择某元素的子孙,选择某元素的儿子 */
	#p6 b{
	color:red;
	}
	#p7>u,b {
	color :purple;
	}
	</style>	
</head>
	
	<body>
	<h1>继承性</h1>
	<h2>层叠性</h2>
	<!--  类选择器的声明 -->
		<p class = "important"> 类选择器,根据元素的class属性来选择 .className {color:red;} </p>
		<p class = "noneit"> 类选择器,根据元 .className {color:red;} </p>
		<p class = "important"> 类选择器,根据元素的class属性来选择 .d;} </p>
		<p id="p4"> id选择器</p>
		<p id="p5"> id选择器 </p>
		<p id ="p6"><!-- 选择孙子-->
		<u>vishwamanava <b>international</b> hostel<u> <b>570009</b>
		</p>
		<p id="p7"><!-- 选择儿子-->
		<u>vishwamanava <p>international</p> hostel</u> <b>570009</b>
		</p>
	</body>
</HTML>
~~~

### 伪类选择器

~~~ html
<!--  伪类选择器:设置同一个元素在不同状态下的样式;
link:向未被访问的超链接添加样式;
visited:向已经访问过的超链接添加样式;
active:向被激活的元素添加样式;例如按钮的点击
hover:当鼠标悬停在元素上方时候,向该元素添加样式;
focus:当元素获取焦点时,向该元素添加样式;光标在这个位置闪烁就是焦点
 -->
<HTML>	
<head>	
	<meta charset="utf-8">  
	<title>http:www.baidu.com/test_L</title>
	<style>
	/* link,visited */
	a:link{
		color:black;
	}
	a:visited{
		color:red;
	}
	/*激活态的按钮 */
	#i1:active {
		background-color:red; 
	}
	/* 焦点框 */ 
	#i2:focus{
	 background-color: silver;
	}
	/* 鼠标悬停态的 */
	img:hover{
	 width:250px;
	 height:250ps;
	}
	</style>	
</head>
	<body>
	<!--  伪类选择器 -->
	<a href="http:www.baidu.com">百度网址</a>
	<a href="http:www.google.com">google</a>
	<a href="http:www.catfood.com">cat</a>
	<a href="http:www.zhihu.com">zhihu</a>
	<p>
		<input type="button" value="提交" id="i1"/>
	<p>
		<input type="text" id="i2"/>
	</p>
	<p>
		<img src="..\images\food.jpg"/>
	</p>
	</body>
</HTML>
~~~

### css 声明: border

~~~ html
<!doctype html>
<HTML>	
<head>	
	<meta charset="utf-8">  
	<title>http:www.baidu.com/test_L</title>
	<style>
	/* 四个边框同时设置: */
	p{
	border:1px dashed red
	}
	/* 单边设置:left right top buttom */
	h1{
	border-left: 5px solid blue
	}
	/* 溢出的处理 visible(出了边框 可以看到), hidden(超出隐藏),scroll(滚动,没有超出一样滚动),auto(自动在溢出的时候滚动)*/
	h2{
	border:1px dashed red;
	width:300px;
	height:60px;
	overflow:scroll;
	}
	</style>
		
</head>
<!-- css 声明:
	border(边框) ,box(box模型) ,背景 (背景色,背景图片)
	border: 设置元素的边框;(单边设置(border-left:width style color)和四边设置(:width style color))
	样式单位:百分比% ,英寸in  厘米cm 毫米mm  磅pt 像素px 一个字大小em (缩进2em 间距 等);
	颜色:0-255  十进制 rgb(10,10,10)/(10%,20%,30%) 十六进制:表达256只需2位(0-9 a-f) #8fc567 相邻两位相同可以缩写一个;
	overflow 字体溢出框怎么处理(固定了宽高之后会有溢出现象,块元素一般默认是100% 会随着内容的增加扩展)
	
 -->
	
	<body>
	<h1> css 声明: </h1>
	<p>border: 设置元素的边框;(单边设置(border-left:width style color)和四边设置(:width style color))
	border: 设置元素的边框;(单边设置(border-left:width style color)和四边设置(:width style color))
	border: 设置元素的边框;(单边设置(border-left:width style color)和四边设置(:width style color))
	border: 设置元素的边框;(单边设置(border-left:width style color)和四边设置(:width style color))
	</p>
	<h2>
	<!--  这里出现了溢出的情况;  -->
	border: 设置元素的边框;(单边设置(border-left:width style color)和四边设置(:width style color))
	border: 设置元素的边框;(单边设置(border-left:width style color)和四边设置(:width style color))
	border: 设置元素的边框;(单边设置(border-left:width style color)和四边设置(:width style color))
	border: 设置元素的边框;(单边设置(border-left:width style color)和四边设置(:width style color))
	</h2>

	</body>

</HTML>
~~~

### css声明:box

~~~ html
<!doctype html>
<HTML>	
<head>	
	<meta charset="utf-8">  
	<title>http:www.baidu.com/test_L</title>
	<style>
	
	div{
	border:1px solid red;
	 width: 100px;
	 height:100px
	}
	
	 /* 设置四边相同的边距 padding 内边距 margin 外边距*/
	 #d1{
	 	padding:20px;
	 	margin:30px;
	 }
	/* 2.设置不同的边距*/
	#d2{
	padding:20px 30px 40px 50px;
	margin:20px 30px 40px 50px;
	}
	/*单边设置边距*/
	#d3{
	padding-left:50px;
	margin-left:50px;
	}
	/* 对边设置相同的边距 上下,左右*/
	#d4{
	padding:20px 40px;
	margin:20px 40px;
	}
	/*对边设置边距的特例:在设置外边距时,若左右外边距值为auto,则该元素水平居中*/
	#d5{
	margin:20px auto;
	}
	</style>
		
</head>
<!-- css 声明:
	box(box模型) 
	/* 设置边距有五种:
	1.四边设置相同的边距
	2.四边设置不同的边距(top,right,button,left)
	3.单个边设置边距
	4.对边设置相同的边距 
	5.对边设置边距的特例
	 */
 -->
	
	<body>
	<div id="d0">d0</div>
	<div id ="d1">d1</div>
	<div id="d2">d2</div>
	<div id="d3">d3</div>
	<div id="d4">d4</div>
	<div id="d5">d5</div>
	
	</body>

</HTML>
~~~

### css背景：

~~~ html
<!doctype html>
<HTML>	
<head>	
	<meta charset="utf-8">  
	<title>http:www.gary_H.com/project_L</title>
	<style>
		/*如何设置背景图*/
		body{
		background-image:
			url(food.jpg);
			/*平铺类型：repeat-y repeat-x*/
			/* background-repeat:repeat-y; 垂直平铺*/
			background-repeat: repeat-y; /* 水平平铺*/
			background-position:center; /* 位置 */
			background-attachment:fixed; /* 背景图不动，只有div的飞机在动，类似于水印*/
		}
		/* 一起设置背景色和背景图，可以采用简化的方式
		默认情况下，背景图会随着页面的滚动而移动，可以通过background-attachment属性改变此特征。可以取值为fixed
		 */
		.enemy{
			border: 1px solid red;
			width:50px;
			height:50px;
			margin:20px auto;
			background:url(ene.jpg) no-repeat center;
		}
		.hero{
			border: 1px solid red;
			width:200px;
			height:160px;
			margin:20px auto;
			background:url(icon.jpg) no-repeat center;
		}
		
	</style>
		
</head>
<!--背景色: 
 background-color:red;
 背景图:background-image:url\(address)

 -->
	
	<body>
	<div class="enemy"></div>
	<div class="enemy"></div>
	<div class="enemy"></div>
	<div class="enemy"></div>
	<div class="hero"></div>
	<div class="hero"></div>
	<div class="hero"></div>
	<div class="hero"></div>
	<div class="hero"></div>
	<div class="hero"></div>
	<div class="hero"></div>
	<div class="hero"></div>
	<div class="hero"></div>
	<div class="hero"></div>
	</body>

</HTML>
~~~

### css 文本格式化

~~~ html
<!doctype html>
<HTML>	
<head>	
	<meta charset="utf-8">  
	<title>http:www.gary_H.com/project_L</title>
	<style>
		/* 文本格式设置演示： */
		h1{
		text-align:center; 
		/* 字体在行高范围内垂直居中，元素的高等于行高的时候，文字会垂直居中*/
		line-height:100px;
		}
		
		p{
		
		text-decoration:underline;
		line-height:3em;
		text-indent:2em
}	
	</style>
		
</head>
<!--
文本格式化：
1.控制文本：font-family:value1,value2;(指定字体)font-size:value;(字体大小)font-weight:normal/hold;(字体加粗)
color：value（文本颜色）；text-align:left/right/center （文本排列）；text-decoration:none/underline;(文字修饰)
line-height:value(1.6em);(行高)，text-indent:value(2em)(首行文本缩进)
 -->
	<body>
	<h1>精彩人生</h1>
	<p>  
汤姆·汉克斯是一位美国演员和制片人。汉克斯在电影、电视和舞台上都积累了丰富的作品，
	</p>
	<p>1993年，汉克斯凭借在《费城故事》中的表现赢得了第一个奥斯卡最佳男主角奖。
此后，他又出演了浪漫喜剧《阿甘正传》，并凭借该片连续第2年获得奥斯卡最佳男主角奖，
	</p>
	</body>
</HTML>
~~~

### css声明：定位

~~~html
<!--定位：解决元素的摆放问题；
1.定位的分类5种：
默认的定位：块元素垂直排列，行内元素左右排列  （流定位）
特殊：
1.浮动定位：可以让块元素左右排列 左/右浮动
浮动规律：浮动的目标脱离队伍，到达指定位置。后者填充，浏览器渲染规则：父元素高度自适应，以内部流中的元素高度为准；
浏览器认为文字很重要无论如何都会文字显示完整；
左浮动可以让块按照正序左右排列；
  消除浮动影响:只消除对叔叔元素的边框的影响.在被影响的元素使用clear:left;
  消除对父类的影响,父元素的边框要显示;在父元素内加空的块 高度为0,对空块加clear,空块会出现在浮动元素下方,空块还在流内,
  从而拉伸了父元素的高度
浮动定位中左右浮动的影响问题,就是因为块的出流对块的高度产生了影响,
然后使得下面的内容产生了改变,为了消除改变我们在块流最后放一个透明块d4,同时消除上面有色块的影响d4{clear},
得到无色块在流的最后.无形中拉伸了父类块的搞度,解决了影响下级文字的影响;
2.相对定位(见project_01web)：元素以自己为目标产生微小的偏移 ,元素不会脱离流,位置不会释放;只有相对定位不能释放位置;
position:relative声明
3.绝对定位(见project_01web,position_absolute)：可以让元素以父类目标产生很大的偏移;以带有position属性的父类为目标;
若所有父类都有就近原则,都没有则以body为目标;
绝对定位目标脱离流,释放位置. position 
4.固定定位(见project_01web,position_fixed)：可以让元素以窗口为目标产生巨大的偏移;以浏览器窗口为目标;固定定位也脱离流,位置会释放;
position:fixed;(广告,回顶链接)
后三位都是以某元素为目标产生偏移,可以以四条边为目标声明偏移;
left/top/right/bottom:20px;(向目标的中心偏移就是正数,反之为负)

 --><!doctype html>
<HTML>	
<head>	
	<meta charset="utf-8">  
	<title>http:www.gary_H.com/project_L</title>
	<style>
		/* */
		#d0 ,p {
		border:1px solid red;
		width:400px;
		 clear:right; 
		}
	   	#d1,#d2,#d3{
	   	width:100px;
	   	height:100px;
	   	margin:10px;
	   	}
	   	#d1{
	    	background-color:#f00;
	   
	   	}
	   	#d2{
	   		background-color:#0f0;
	   	}
	   	#d3{
	   		background-color:#00f;
	   	}
	   	/*浮动*/
	   	#d1,#d2,#d3{
	   		float:right;
	   	}
	   	#d4{
	   		clear:right;
	   	}
	</style>
		
</head>
	<body>
	<div id="d0">
		<div id="d1"></div>
		<div id ="d2"></div>
		<div id ="d3"></div>
		<div id ="d4"></div> <!-- 加的空块为了解决浮动的影响,对空块加了clear之后无视了有色块的影响,进入到了流的最后变 就是d0的最后位置 -->
	</div>
	<p> 浮动规律：浮动的目标脱离队伍，到达指定位置。流中后者填充，浏览器渲染规则：父元素高度自适应，以内部流中的元素高度为准；
浏览器认为文字很重要无论如何都会文字显示完整； </p>
	

	</body>

</HTML>
~~~



项目练习

~~~ html
<!--对浮动定位,相对定位和list ul.等的使用形成一个类似照片墙的效果; -->
<!doctype html>
<HTML>	
<head>	
	<meta charset="utf-8">  
	<title>http:www.gary_H.com/project_L</title>
	<style>
		body{
		background-color:#066;
		}
		ul{
		/* border: 1px solid red; */
		width:780px;
		margin:20px auto;
		list-style-type:none;/* 去掉图片前的符号*/
		}
		li{
		background-color:#fff;
		border:1px solid #ccc;
		padding :10px;
		margin:10px;
		float:left;
		}
		p{
		text-align:center;
		font-family:"微软雅黑","文泉驿正黑","黑体";
		}
		/*鼠标悬停时,li向右上方偏移两个像素,从而实现抖动的效果.使用相对定位进行实现*/
		li:hover{
			position:relative; /*使用之前的声明;*/
			left:2px;
			top:-2px;
		}
	</style>
		
</head>

	<body>
	<ul>
		<li>
			<img src="web_01.jpg"/>
		<p>秋衣盎然</p>
		</li>
		<li>
			<img src="web_01.jpg"/>
		<p>绿叶依旧</p>
		</li>
		<li>
			<img src="web_01.jpg"/>
		<p>未来的你</p>
		</li>
		<li>
			<img src="web_01.jpg"/>
		<p>又在何方</p>
		</li>
		<li>
			<img src="web_01.jpg"/>
		<p>北风来临</p>
		</li>
		<li>
			<img src="web_01.jpg"/>
		<p>东风不远</p>
		</li>
	</ul>
	</body>
</HTML>
~~~

### 堆叠顺序

~~~ html
<!doctype html>
<HTML>	
<head>	
	<meta charset="utf-8">  
	<title>http:www.gary_H.com/project_L</title>
	<style>
		/* */
		div{
		background-color:#066;
		width:800px;
		height:500px;
		margin:20px auto;
		position:relative;
		}
		#i1,#i2,#i3{
			position:absolute;
		}
		#i1{
			left:170px;
			top:100px;
		}
		#i2{
			left:200px;
			top:100px;
		}
		#i3{
			left:250px;
			top:150px;
		}
		/*堆叠顺序，数字越大越靠上，反之在下*/
		img:hover{
			z-index:999;
		}
	</style>
</head>
<!--堆叠顺序：元素之间互相重叠
 -->
	<body>
		<div>
			<img src="ene.jpg" id="i1"/>
			<img src="icon.jpg" id="i2"/>
			<img src="food.jpg" id="i3"/>
		</div>
	</body>
</HTML>
~~~

### 列表样式和显示方式：

~~~ html
<!doctype html>
<HTML>	
<head>	
	<meta charset="utf-8">  
	<title>http:www.gary_H.com/project_L</title>
	<style>
		/*让有序出现大写罗马数字 */
		ol {
			list-style-type:upper-roman;
		}
		ul{
			list-style-type:square;
		}
		p { /*把块p改为行内元素 没有宽高 （auto）*/
		 display:inline;
		}
		span{/*span行内改为块元素；*/
			display:block;
		}
		div{  /*隐藏相应的元素*/
		 display:none;
		}
	
	</style>
</head>
<!--列表样式：list-style-type 属性用于控制列表中列表标志的样式（有序无需列表）
无序列表取值：none(无) disc（实行圆默认） circle（空心圆） square（实心方块）;
有序列表取值:none(无) decimal(数字) lower-raman(小写罗马) upper-roman(大写罗马)
list-style-image:url();指定图像作为有序或者无序的标志;
 -->
 <!-- 元素的显示方式
 1.块元素: 从上至下排列,可以设置宽高 如 h p ol/ul/li div table form 等
 2.行内元素:从左到右排列,不能设置宽高,如 span/i/em/b/strong/u/del a label   等
 3.行内块元素:从左至右排列,可以设置宽高,如 img input select textarea 等;
 总结: h p ol/ul/li div span/i/em/b/strong/u/del img a table form input label select textarea
 如何修改显示方式; 一般很少改 隐藏经常用;
 display:block;改为块
 inline;行内
 inline-block;行内块
 none;隐藏
  -->
	<body>
	<ol>
		<li>河北</li>
		<li>河南</li>
		<li>山东</li>
		<li>安徽</li>
		<li>福建</li>
	</ol>
	<ul>
		<li>山西</li>
		<li>陕西</li>
		<li>四川</li>
		<li>广州</li>
		<li>广西</li>
	</ul>
	
	<!--显示方式的演示;-->
	<div>  <!--块-->
		<p>hello </p>
		<p>world</p>
		<p>happy</p>
	</div>
	<div>	<!--行内-->
		<span>hi</span>
		<span>who are you </span>
		<span>and you </span>
	</div>
	</body>
</HTML>
~~~

### 鼠标形状：

<!--鼠标形状；默认情况下 ，光标会随着用户的操作发生改变。
cursor:default（默认箭头）/pointer（手）/crosshair（可移动的加号）/text（编辑I光标）/wait（转圈）/help（？）等；
 -->

## 第三章:JAVASCRIPT 让网页呈现动态的数据和效果

js直接使用,没有封装成函数，在网页上加载时直接调用；就是说网页上使用js,如果没有放在函数中,那么在加载网页时候,js表达式是在页面内容之前被加载的.

js的使用有三种封装形式：
1.事件定义式：在元素上直接写；
2.嵌入式:在script标签中写js,标签可以放在任意位置,但是一般放在head中;
3.文件调用式：在.js文件中写函数 在head中script中引入；在标签中调用；

~~~ html 
<!--js 是嵌入在浏览器中的基于对象和事件驱动的解释性脚本语言，具有与Java和c类似的语法，一种网页编程技术。向html页面添加交互行为，直接嵌入HTML页面，由浏览器解释执行代码，不进行预编译；-->
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<script>
	function f1() {
		alert('hello world');//跳出窗口进行输出;
	}
</script> 
<!--/* 第三种方式的调用 创建一个js_test.js的文件，里边是function f2{alert("welcome tom")}，该标签必须是双标签 即使是没有内容；该标签不能即引入js又写js */  -->
<script src="js_test.js"></script>

</head>
<body>

<!-- 
js直接封装成函数 可以让标签直接调用;
function是关键字,用来声明函数,f2是函数名,小括号可以声明参数,大括号是函数体;js中函数都是共有的不需要修饰符;
js不区分单双引号; 
js的使用有三种形式：
1.事件定义式：在元素上直接写；
2.嵌入式:在script标签中写js,标签可以放在任意位置,但是一般放在head中;
3.文件调用式：在.js文件中写函数 在head中script中引入；在标签中调用；
-->
<!-- 直接在元素标签加 onclick="alert();" 在点击之后出现一个对话框返回alert内容 -->
	<input type="button" value="button_1" onclick="alert('welcome on my website');" />
	<input type="button" value="button_2" onclick= "f1();" />
	<input type="button" value="button_3" onclick= "f2();" />
</body>
</html>

~~~

### js基本语法：

 （语法规范，标识符和变量 ，数据类型，运算符）很多地方和Java一样；部分有区别

~~~js
/**
js的基本语法：基本和Java类似
var,typeof,function,undefined是Java没有的
var关键字，声明变量 变量是没有类型的，统一使用关键字var声明。
js中没有赋值 默认值不再是null 而是undefined;
typeof关键字:查询当前数据类型,返回string/number/boolean/object/function/undefined
isNaN(is not a number?)判断被检测表达式经过转换后是否不是一个数,返回结果是true/false

数据类型(变量所引用的数据类型):
1.特殊类型: null(空), undefined(未定义)
2.内置对象(基本类型):Number(数字),String(字符串),Boolean(布尔),Function(函数),Array(数组)
3.外部对象:window(浏览器对象),document(文档对象)
4.自定义对象:object(自定义对象)

数据类型的转换函数:(字符串不能强制转换为数字)
	toString(所有的数据类型转换为string类型) ,
	parseInt 强制转换为整数,如果不能转换返回结果是NaN(not a number),
	parseFloat强制转换为浮点数,如果不能转换返回结果是NaN(not a number).
**/
<script>
// 直接加载调用的演示：执行时机甚至比body还早
		//alert(1);
	console.log("控制台打印") // 在浏览器的检查console查看
		//声明变量
	var x;
	console.log(x);
	x=3;
	console.log(x);
	var y="hello "
	console.log(y);
// 数据类型的问题;
		//隐式转换:字符串最大 和任何相加都是字符串 ,boolean是T1F0
	//var s="hello";
	//var n=8;
	//var b=true;
	//console.log(s+n);
	//console.log(n+b);
	//console.log(s+b); // hellotrue
//数据类型的转换函数:(字符串不能强制转换为数字)
	 var s="hello";
	 var n=10.5;
	 var b=true;
	 console.log((n.toString())+1);//10.51
	 console.log(parseInt(n)+1);//11
	 console.log(parseFloat(n));//10
	 console.log(parseInt(s));//NaN

	console.log(typeof(n));//查看数据类型number
	console.log(isNaN(56)); // 判断语句 false  重点 :判断是不是数字 然后进行操作
	console.log(isNaN("abc"));//true 
</script>
~~~

基本语法的小案例 _1

~~~ js
/* 使用js实现一个文本框内输入一个数字 然后一个按钮执行平方运算 得到的结果输入到一个span框内*/
<!DOCTYPE HTML>
<html>
<head>
<meta charset="UFT-8">
<title>java_script_L</title>
<script>
/* 计算square 函数*/
 function square (){
	var input_num=document.getElementById("num");//获得文本框的值;
	//console.log(input_num);
	var n =input_num.value;// 提取文本框中的值
	//console.log(n);//5
	// 因为判断中的结果是span 里的 所以我们提前取span
	var span = document.getElementById("result");
	//judge the num 
	if (isNaN(n)){
		// 不是数字 给与提示:
		span.innerHTML="请输入数字:";
	}else{
	//是数字,计算平方
		span.innerHTML=n*n;
	}
	
}
</script>
</head>
<body>
/*
案例:
1.如何获取一个网页上的一个元素;
document.getElementById("id")
2.如何读取一个文本框的值:
input.value(读)
input.value="abc";(写)
3.如何读写span的内容:
span.innerHTML(read)
span.innerHTML="abc";(write)
*/
<input type="text" id ="num"/>
<input type="button" value="square" onclick="square();"/>
= <span id="result"></span>
</body>
</html>

~~~

案例_2 猜数字

~~~js
<!DOCTYPE HTML>
<html>
<head>
<meta charset="UFT-8">
<title>java_script_L</title>
<script>
// 网页加载时候直接生成随机数；
var ran=parseInt(Math.random()*10);
console.log(ran);
//判断函数guess()
 function guess(){
	var num_input=document.getElementById("num")
	var n =num_input.value;
	var span = document.getElementById("result");
	if (isNaN(n)){
		span.innerHTML="enter a number in 0-10";
	}else{
		if (ran>n){
			span.innerHTML="smaller";
		}else if(ran<n){
			span.innerHTML="bigger";
		}else{
			span.innerHTML="success";
		}
	}
}

</script>
</head>
<body>
/*用js做一个案例猜数字*/
<p>请随机输入一个10以内的数字：</p>
<input type="text" id="num"/>
<input type="button" value="guess" onclick="guess();"/>
<span id="result"></span>
</body>
</html>
~~~

### 控制语句:

~~~ js
<!DOCTYPE HTML>
<html>
<head>
<meta charset="UFT-8">
<title>java_script_L</title>
<script>
var a=0;//a得值是除了那五种控制类型中的任意一种都可以执行方法体；
if (a){
	console.log("pass");
}
</script>
</head>
<body>
/* 流程控制语句：
控制语句：包括判断，分支，循环。基本和Java语法一致 if ，switch-case ,for ,while,do-while;
java中条件表达式必须返回Boolean值，JS中的表达式可以是任意表达式。可以返回任何类型值；
就是说一切非空的值都是true 。 包括0,null,"",undefined,NaN，这五种是空值 返回值是false.
使用举例：if（a）{ pass}如果a是这五个之中的任意一个类型，那么就不会执行方法体。
-----
阶乘：n!=1*2*3...*n ; 0!=1;负数没有阶乘;
*/
</body>
</html>
~~~



### JS对象:JS内置对象,外部对象,自定义对象;

~~~js
<!DOCTYPE HTML>
<html>
<head>
<meta charset="UFT-8">
<title>java_script_L</title>
<script>
//Number:
var num = 500.3652;
//alert(num.toFixed(2));// 结果是500.37 有四舍五入
console.log(num.toFixed(2));//控制台显示,结果一样,不一样的显示方式;
//Array:
var arr=["gary",200,"tom"]
console.log(arr[1]);//200

//创建空数组然后追加;
var arr1 = new Array();
arr1.push("addition");
console.log(arr1) // [addition]
//数组倒转:
 var arr2=["gary","tom"];
alert(arr2.reverse());
//数组排序(*):
var arr3=[5,3,6,3,123,67];
console.log(arr3.sort());// [123, 3, 3, 5, 6, 67]js 的sort 并不是按照数字排序.默认按照字符串比较的是unicode码;
//数字化使用sort排序(替换比较方法改变排序结果,对象作为参数,该方法不用复用,写成匿名函数):
var arr4=[4,90,55,6,2,756];
//这里使用了js的匿名函数 function(para1,para2){return mathod_body}
console.log(arr4.sort(function(a,b){return a-b})) //[2, 4, 6, 55, 90, 756] 数组按数字的排序从小到大(b-a大到小) 
// Math:
console.log(Math.PI);//3.141592653589793
console.log(Math.round(Math.PI));//3
//Date:
var now=new Date();
console.log(now);//Sun Aug 16 2020 20:21:07 GMT+0530 (印度时间) 浏览器时间
var d=new Date("2020/08/01 20:23:20");//Sat Aug 01 2020 20:23:20 GMT+0530 (印度时间)
console.log(d);
//时间格式转换成指定的格式(转换为本地时间或日期的字符串):
console.log(now.toLocaleDateString());//2020/8/16
console.log(now.toLocaleTimeString());//下午8:27:59
//我们自己得到对象的时间,读写时间分量;get set 方法
var y =now.getFullYear();
var m=(now.getMonth())+1;//月份从0开始
var d=now.getDate();
console.log(y+"年"+m+"月"+d+"日");//2020年8月16日
//正则表达式:
var name="garyasksjdfkljaldkjggkgk";
var reg=/a/g;// 默认不写模式 和i都可以，模式设置为g没有得到预期结果(多次执行才能全局出多个结果)
console.log(reg.exec(name));//["a", index: 1, input: "garyasksjdfkljaldkjggkgk", groups: undefined]
console.log(reg.test(name));//true
console.log(reg.exec(name));//second times ["a", index: 14, input: "garyasksjdfkljaldkjggkgk", groups: undefined]
console.log(reg.exec(name));//third times  null (如果后边还有 输出下标,没有就是null)
// String和正则表达式:
console.log(name.replace(reg,"x"));// 将name中的正则结果替换为x gxryxsksjdfkljxldkjggkgk
console.log(name.match(reg));// ["a", "a", "a"]
console.log(name.search(reg)); 1
//function对象:
//使用new 出函数对象:
var divide=new Function("a","b","return (a/b);");
var result=divide(5,2);//result=2.5
alert(result);

//
function sum(){
 	var s=0;
	if (arguments.length>0){
		for (var i=0;i<arguments.length;i++){
			s+=arguments[i];
		}
	}	
	return s;
}
// 多个参数传入到arguments 数组中,供函数调用;
console.log(sum(1,23,45));//69
function minus(a,b){
	return a-b;
}
console.log(minus(5));//NaN
console.log(minus(5,1));//4
console.log(minus(57,14,23));//43 这里虽然是多个参数 但是函数只从数组中取了需要的两个.另一个是undefined
// eval demo:
var str="4+5"; //String class;
alert(str);// 4+5 
alert(eval(str));9
</script>
</head>
<body>
/*对象：
什么是js对象:对象是js中最重要的API,包含内置,外部,自定义对象.
js中常用的内置对象:String,<*Number>,Boolean,<*Array>,Math,Date,<*RegExp>,<*Function>等对象.
创建String对象的两种方式:
var str="hello world";
var str = new String ("hello world"); 
Number对象的常用方法:toFixed(num):转换为字符串,并保留小数点后一定位数.
Array对象创建: 
var a=[100,200,"gary"];//java中类型有要求,尽量一致,但是js中没有数据类型的要求.都是object数组;
var a=new Array();
数组的倒转和排序:
x.reverse();//数组中的数据完全倒转.
s.sort();//不是按数字进行排序,按照字符串进行排序;
//那么如何按照数字进行排序呢?我们把对象当做参数传进方法.就是匿名函数的用法.
//Math对象:
Math.PI,Math.round(取整)
//Date对象(js和java不一样 java得到的是服务器的时间,js得到的是浏览器的时间.我们一般选择数据库或则服务器的时间):
get ,set 方法,装换为字符串:toString(),toLocaleString(),toLocaleDateString();
//regExp 正则表达式:
var reg1=/pattern/flags; /正则表达式/模式(I/G); 
var reg2=new RegExp("pattern",["flags"]); flag标识:g(global):设定当前匹配模式为全局模式.i(ignore):忽略匹配中的大小写.
reg.exec(str):检索字符串中指定的值,返回值是找到的结果(全局模式(匹配结果全部显示)和普通模式(找出第一个匹配结果))
reg.test(str):检索字符串中指定的值,返回值是boolean;(不区分全局普通,只进行判断)
String 对象和正则表达式:
x.replace(regexp,tostr) // regexp (正则表达式或字符串)replace(返回替代后的结果)
x.match(regexp) // 返回匹配字符串的数组
x.search(regexp)//返回匹配字符串的首字符位置索引;
// function函数 
默认返回undefined 可以使用return返回具体的值
js没有重载,调用时候只要函数名一样,无论传入多少个参数,调用的都是同一个参数.
(其实可以任意参数,只是不是参数的类型是undefined类型.参数封装到arguments数组中供函数调用)
虽然没有重载,但是和重载有了类似的功能;
创建函数对象可以new :
var sum=new Function("x","y","return(x+y);")
匿名函数:
//这里使用了js的匿名函数 function(para1,para2){return mathod_body}
console.log(arr4.sort(function(a,b){return a-b})) //[2, 4, 6, 55, 90, 756] 数组按数字的排序从小到大(b-a大到小) 
//全局函数:
常用的全局函数有:parseInt/parseFloat , isNaN ,eval(可以把字符串当成表达式具有运算的能力)  可以在做计算器中使用 把输入的字符串当做表达式
*/
</body>
</html>
~~~

案例3:regular_demo

~~~js
<!DOCTYPE HTML>
<html>
<head>
<meta charset="UFT-8">
<title>java_script_L</title>
<style>
.ok{
	color:green;
}
.error{
	color:red;
}

</style>
<script>
// onblur 焦点移除事件  onfocus 光标切入事件
//验证账号的格式;
function checkAccount (){
	//alert("焦点移除")
	//获取账号:
	var account_v=document.getElementById("account").value;
	//regular 判断格式是否正确
	var reg=/^\w{5,10}$/; // 从开头(^)到结尾($)是否是5-10位的
	//获取span
	var span=document.getElementById("acc_msg");
	
	if (reg.test(account_v)){
		//格式一致 绿色
		span.className="ok";
		return true;
	}else {
		// 格式错误 红色
		span.className="error";
		return false;
	}
}
function checkpwd(){
	var pwd_v=document.getElementById("pwd").value;
	var reg=/^\w{10,20}$/;
	var span=document.getElementById("pwd_msg");
		// judge REGULAR
	if(reg.test(pwd_v)){
		span.className="ok";
		return true;
	}else{
		span.className="error";
		return false;
	}
}
// 我们还需要登录校验:否则提交按钮不管你是否正确都会提交 这里的校验直接在form中校验 <这里是重点>
</script>
</head>
<body>
<!-- 对象和正则表达式的demo -->
	<form action="https://google.com" onsubmit="return checkAccount()+checkpwd()==2"> <!-- 给服务器通信 表单有onsubmit事件,触发时提交数据,"return false(0,undefined等不能代替false)"就可以取消事件.隐式相加是数字 -->
		<p>
			账号：<input type="text" id="account" onblur="checkAccount();"/> 
			<span>5-10位字母，数字，下划线<span id="acc_msg">(incorrect/correct)</span></span>
		</p>
		<p>
			密码：<input type="password" id="pwd" onblur="checkpwd();"/>
			<span id="pwd_msg">10-20位字母,数字,下划线</span>
		</p>
		<P>
			<input type="submit" value="log_in"/>
		</P>
	</form>
</body>
</html>
~~~

### 全局函数 eval 的案例_4 :  

eval(string)  一个表示 JavaScript 表达式、语句或一系列语句的字符串。表达式可以包含变量与已存在对象的属性。

`eval()` 的参数是一个字符串。如果字符串表示的是表达式，`eval()` 会对表达式进行求值。如果参数表示一个或多个 JavaScript 语句，那么`eval()` 就会执行这些语句。



~~~js
<!DOCTYPE HTML>
<html>
<head>
<meta charset="UFT-8">
<title>java_script_L</title>
<style>

</style>
<script>
	function calculate(){
		var input=document.getElementById("num");
		var num=input.value;
		try{
            // eval 的运算 这里加括号就是为了避免是字符串
		var value=eval("("+num+")");
		input.value=value;
		}catch(e){
		input.value="error";
		}
	}
</script>
</head>
<body>
<!-- 计算器的案例-->
	<input type ="text" id="num"/>
	<input type="button" value="=" onclick="calculate()"/>
</body>
</html>
~~~

### 外部对象: 

浏览器就是一个软件 里边有很多对象供我们使用window(location history document screen navigator等),外部对象就是浏览器的API

BOM:browser object  model 浏览器对象模型.用来访问和操作浏览器窗口,使得JavaScript可以和浏览器对话,通过BOM可以移动窗口,更改状态栏文本,执行其他不和页面内容直接相关的操作.没有相关的标准但是广泛支持.BOM包含了DOM

DOM: document object model:文档对象模型,用来操作文档.定义了访问和操作HTML文档的标准方法,应用程序通过对DOM树的操作,实现对HTML文档数据的操作.

### BOM(brower object model):

~~~js
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>test_javascript</title>
<script>
//第一类: 弹出框:弹出框,确认框,输入框. 这是window的对象方法 可以省略window. 
// alert(),confirm(),setTimeout(),clearTimeout(),setInterval(),clearInterval(),是window的对象方法 弹出框和定时器的api
function f1(){
	window.alert("hello");
}
// 确认框
function f2(){
	var re=confirm("do you have lunch?");
	console.log(re);// 返回结果是ture or false
}
//输入框
function f3(){
	var re=prompt("what do you had?");
	console.log(re);//返回值就是输入框的结果.
}
//第二类:定时器  类似Java中的timer .周期性定时器(每隔n毫秒执行一次函数,直到结束条件).一次性定时器(隔n毫秒开始执行).可以手动停止
//周期性定时器
function f4(){
	//启动定时器 就相当于启动一个支线程,f4是主线程.并发执行不互相等待
	//id 用来停止计时器
	var num=5;
	var id=window.setInterval(function(){
		console.log(num--);
		if (!num){
			clearInterval(id);//停止制定ID的定时器;
			console.log("fire");//没有时间间隔直接执行
		}
	},1000);// 方法(匿名函数)和时间间隔
	console.log("点火");// 这是主线程的console立刻输出 和计时器同时执行了.结果是 (点火,5,4,3,2,1,fire)
}
//一次性定时器
var id;//全局ID 在两个函数中使用
function f5(){
	//启动一次性定时器 setTimeout(),如果想在没有执行之前停止,使用ID进行手动停止
	id=setTimeout(function(){
		console.log("di di di...");//执行一次后自动结束
	},3000);
}
// cancle 给一次性定时器(执行之前)手动取消
function f6(){
	clearTimeout(id);
}
</script>
</head>

<body>
<!-- 弹出框演示 -->
	<input type="button" value="按钮1" onclick="f1();"/>
	<input type="button" value="按钮2" onclick="f2()"/>
	<input type="button" value="按钮3" onclick="f3()"/>
	<input type="button" value="按钮4" onclick="f4()"/>
	<input type="button" value="按钮5" onclick="f5()"/>
	<input type="button" value="cancle" onclick="f6()"/>
</body>
</html>
~~~

定时器小案例:

~~~js
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>test_javascript</title>
<script>
//开始函数
var id;//这里ID为undefined 还没有启动 如果启动了就不能再次启动
function f1(){
	if(id){
		return;
	}
	 id =setInterval(function(){
		//创建当前客户端的时间
		var date=new Date();
		//获取本地时间格式
		var now=date.toLocaleTimeString();
		//将时间写入clock 获取文本框
		var p=document.getElementById("clock");
		p.innerHTML=now;// 只有表单里的框使用p.value
	},1000);
}
//停止时间 需要使用f1的ID 如果给ID限制了 那么再次启动就不为空 不能重启 需要给ID清空
function f2(){
	if(id){
		clearInterval(id);
		id=null;//id清空 才能再次启动
	}
}
</script>
<style>
#clock{
	border:1px solid green;
	width:200px;
	text-align:center;
	font-size:20px;
	height:30px;
	line-height:30px;
	
}
</style>
</head>

<body>
<!-- 定时器案例  动态时钟的启动和停止 -->
	<input type="button" value="start" onclick="f1();"/>
	<input type="button" value="stop" onclick="f2();"/>
	<p>本地时间: </p>
 	<p id="clock"/>
	
	
</html>
~~~

### 外部对象 window 分支:

~~~js
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>test_javascript</title>
<script>
//这些对象都是window的子对象,可以写window.reload/screen等;
//location 对象:
	function f1(){
	//我们可以使用它进行跳转之前的判断,相对于链接来说变得更加灵活,可选择性.
	confirm("你确定离开页面吗?");//根据boolean值进行判断
	location.href="http://www.baidu.com";//这是属性
}
//刷新reload()
function f2(){
	location.reload();//这是方法
}
//screen对象
function f3(){
	console.log(screen.height);
	console.log(screen.width);
	console.log(screen.availWidth);//可用的宽高
	console.log(screen.availHeight);
}
//history对象
function f4(){
	window.alert(history.length);//当前网页历史记录
}
function f5(){
	history.back();//后退到上一页浏览记录(相当于后退按钮)
}
function f6(){
	history.forward();//前进到下一业浏览记录(相当于单击前进按钮)
}
function f7(){
	history.go(-1)//前进后退n步
}
//
function f8(){
	console.log(navigator.userAgent);//帮助按钮 navigator
}

</script>
<style>

</style>
</head>

<body>
<!--window 对象具有五个分支 location,history,document,screen,navigator,我们把document单独拉出来进行讲解
1.location:对象包含有关当前URL的信息,常用语获取和改变浏览的网址,href属性,reload()重新载入当前网址,相当于刷新按钮.
2.history:对象包含用户(在浏览器窗口中)访问过的URL length属性(浏览历史的数量),back(),forward(),go(n)方法.n是前进后退n步
3.screen:对象包含了有关客户端显示屏幕的信息,常用语获取屏幕分辨率和色彩 常用属性:width/height availWidth/availHeight
4.navigator:对象包含了有关浏览器的信息.常用于客户端浏览器和操作系统的信息navigarot.userAgent.
  -->
	<input type="button" value="网址" onclick="f1();"/>
	<input type="button" value="刷新" onclick="f2();"/>
	<input type="button" value="屏幕" onclick="f3();"/>
	<input type="button" value="历史记录" onclick="f4()"/>
	<input type="button" value="后退"  onclick="f5()"/>
	<input type="button" value="前进 " onclick="f6()"/>
	<input type="button" value="go(n)" onclick="f7()"/>
	<input type="button" value="帮助" onclick="f8();"/>
	
</html>
~~~

### DOM(document object model):

~~~js
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>test_javascript</title>
<script>
//var p =document.getElementById("read");// P 的结果是null 不能获得文本信息.优先执行原因.
//onload 是页面加载事件,在页面加载完成后自动触发.相当于定义了一个加载函数.
window.onload=function(){
	//读写节点的内容
	var p =document.getElementById("read");//这句话没有在函数中就会优先执行 获取不到P 因为优先执行
	//读取节点的名称(only-read)/类型
	console.log(p.nodeName);//P
	console.log(p.nodeType);//1
	//读取节点的内容(双标签之间的内容)innerHTML,innerText(忽略子标签)
	console.log(p.innerHTML); //<b>1.读写操作</b>
	console.log(p.innerText); //1.读写操作
	//读取节点的值/修改(表单控件input,select,textarea中的数据叫值,)
	var rw=document.getElementById("rw");//获取表单控件
	console.log(rw.value);//读取表单控件的值:acquiescent
	rw.value="按钮";//修改表单控件的值 
	console.log(rw.value);// 按钮
	//读写节点的属性 通过方法读写属性(*)x.getAttribute/setAttribute("src")
	var img=document.getElementById("nodeattribute");
	console.log(img.getAttribute("src"));//../img/test_rw_nodeattribute.png
	//update
	img.setAttribute("src","../img/test_update.png")//替换掉原来的图片
	//remove arrtibute
	img.removeAttribute("src");// 删除图片
	//2.通过标准属性名进行操作 更加简单易用, className,id,style等 通常使用的是className
	//通过id进行style的属性读写
	var p=document.getElementById("p");
	console.log(p.style.color);// red
	p.style.color="blue";//字体style颜色变成蓝色
	//3.通过不标准的属性名读写属性 不推荐使用.(a.href,img.src等)
	
}
</script>
 

</head>

<body>
	<!--DOM概述
	文档对象模型,当网页被加载时,浏览器会创建页面的文档对象模型,通过可编程的对象模型,JavaScript获得了足够的能力来创建动态的HTML
	js能够改变页面中所有的HTML元素,HTML属性,css样式,事件的反应
	一个网页(HTML)从服务器被dom4j加载之后当做一个document对象(DOM树)进行解析,浏览器在更改信息的时候肯定不是更改服务器的
	我们可以更改HTML或document对象.对象是更容易更方便的.DOM树具有不同的节点,
	(document文档节点,body/p等元素节点,注释节点,文本节点,属性节点)不同的节点具有不同的API
	归纳:浏览器获得HTML网页后解析为对象,这套对象具有树状结构成为DOM树,不同的节点具有不同的分类 学习DOM就是学习结构和节点的API
DOM操作: 查找节点,读取节点信息,修改节点信息,创建新节点,删除节点
	1.读取节点操作:
	nodeName:节点名称:元素节点以及属性节点返回标签或者属性名称,文本节点是 #text,文档节点是#document.
	nodeType:节点类型:返回值1(元素节点),2(属性节点),3(文本节点),8(注释节点),9(文档节点)
	读取节点的内容:innerHTML,innerText.
	读取节点的值:针对表单控件中的数据值, x.value
	读写节点的属性:1.通过方法读写属性,2.通过标准的属性名读写属性,3,通过不标准属性名读写属性(只有高标准的浏览器才支持)
	案例:轮播
	 -->
	 <p>
	 	DOM的操作:
	  </p>
	 			<p id="read"><b>1.读写操作</b></p>
	 			<p id="search"><b>2.查询操作</b></p>
	 			<p id="add-delete"><b>3.增删节点操作</b><p>
 				<p>
 					<input type="button" value="acquiescent" id="rw"/>
 				</p>
 				<p>
 					<img src="../img/test_rw_nodeattribute.png" id="nodeattribute">
 				</p>
 				<p style="color:red;" id="p">
 					标准的属性名进行操作
 				</p>
	
</html>
~~~

节点读取的案例_图片轮播

~~~js
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>test_javascript</title>
<style>
	div{
		border:1px solid red;
		width:604px;
		height:193px;
		margin:50px auto;
	}
	.show{
		display:inline-block;
	}
	.hide{
		display:none;
	}
	
</style>
<script>
//轮播方法 在加载页面后启动定时器进行轮播
window.onload=function(){//页面加载函数
	roll_p();	//轮播函数调用
}
var id;
function roll_p(){//轮播函数
 var n=0;//轮播次数  放到全局可以避免轮播鼠标离开充值(为了继续之前的轮播):本代码不需要(why?)
	 id=setInterval(function(){
		n++;//通过N求模,得出每次循环哪个图片显示
		var imgs=document.getElementsByTagName("img");//标签名获得元素
		//将所有的图片隐藏
		for(var i=0;i<imgs.length;i++){//循环一轮 其中一张图片一直显示,另外两张隐藏
			imgs[i].className="hide";
			var index=n%imgs.length;//显示的图片下标
			imgs[index].className="show";
		}
	},1000);	
}
function stop(){//stop timer 定时器停止
	clearInterval(id);
}
</script>
</head>

<body>  
	<!--案例 图片的轮播 
	display:inline-block;
	display:none;
	1.在块中设置三个轮播图片
	2.给图片添加样式(style)在块中其他两张图片被挤出,只有一张在块中.
	3.预制样式:.show{} .hide{}
	4.在显示上设置class="hide"
	5.开始轮播 获取所有图片 给图片设置显示/隐藏 定义定时器进行轮播,循环确定循环中哪一个图片是显示
	6.鼠标事件 ,鼠标放在图片希望暂停轮播.离开图片继续  onmouseover, onmouseout
	
	-->
	<div onmouseover="stop()" onmouseout="roll_p()"> <!-- 鼠标事件 悬停和离开-->
		<img src="../img/pic_roll_01.png" class= "hide"/>
		<img src="../img/pic_roll_02.png" class="hide"/>
		<img src="../img/pic_roll_03.png" class="hide"/>
		
	
	</div>
</body>

~~~

### 节点的查询:

~~~js
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>test_javascript</title>
<style>

</style>
<script>
// 节点查询:
window.onload=function(){
	//1.根据id查询
	var q=document.getElementById("gz");
	console.log(q);
	//2.根据标签名称查询内容
	var na=document.getElementsByTagName("li");
	console.log(na);
	//3.通过层次(节点关系查询)1.查询父亲2.查询孩子3.兄弟查询(标准中没有)
	var gz=document.getElementById("gz");
	var ul=gz.parentNode;
	//console.log(ul);
	console.log(gz.parentNode);//<ul>...<ul>
	console.log(ul.childNodes);//显示ul下的所有的子节点,空格,回车等都包括
	console.log(ul.getElementsByTagName("li"));//只包含元素的子节点查询 更常用
	//兄弟节点查询 某节点.父亲.孩子[i]
	var five_brother=((gz.parentNode).childNodes);//etc...
	console.log(five_brother);
	//4. 通过name属性:一般用于查询一组单选或者多选
	var radio=document.getElementsByName("sex");
	console.log(radio);//得出带有name属性的查询  NodeList(2) [input, input]	
}
</script>
</head>
<body>  
	<!-- DOM操作 查询节点
	查询节点的方式: 
	通过id查询 document.getElementById("id_name");
	通过层次(节点关系查询) 
	通过标签名称查询 document.getElementByTagName("element_name");
	通过name属性查询 
	 -->
	 <ul>
	 	<li>北京</li>
	 	<li>上海</li>
	 	<li id= "gz">广州</li>
	 	<li >深圳</li>
	 	<li>郑州</li>
	 	<li>周口</li>
	 </ul>
	 <p>
	 <!-- 带有name属性的查询 -->
	 <input type="radio" name="sex" checked/>男
	 <input type="radio" name="sex" />女
	 </p>
</body>
</html>
~~~

### 节点的增加删除:

~~~js
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>test_javascript</title>
<style>
</style>
<script>
//追加函数
function add(){
	//创建新的li,给li设置内容,再追加到ul之下
	var li=document.createElement("li");
	//console.log(li);
	li.innerText="安徽";//innerHTML都随意使用
	//挂到DOM树上去
	var ul=document.getElementById("city");//获得ul
	ul.appendChild(li);//追加到新的li到ul中最后位置
}
//插入节点:父节点之下 子节点之前.
function insert(){
	//创建新节点
	var li=document.createElement("li");
	li.innerHTML="山东";
	//挂上 获取父亲和弟弟的节点
	var ul=document.getElementById("city");
	var gz=document.getElementById("gz");
	//插入到指定的位置：
	ul.insertBefore(li,gz);
}
	// 删除函数
function remove(){
	// 必须通过父亲删除孩子,子节点如果还有子节点 那么一起删除了
	//获取删除元素的父亲,获取要删除的元素,通过父节点删除子节点
	var ul=document.getElementById("city");
	var gz=document.getElementById("gz");
	ul.removeChild(gz);
}
</script>
</head>
<body>  
<!-- 节点的增加删除 
增加: 创建节点:createElement();
插入:按照指定位置插入节点
删除：fathernode.removeChild(childnode)
-->
<p>
<input type="button" value="addation" id="add" onclick="add()"/>
<input type="button" value="insert" id="in" onclick="insert()"/>
<input type="button" value="remove" id="re" onclick="remove()"/>
</p>
	 <ul id="city">
	 	<li>北京</li>
	 	<li>上海</li>
	 	<li id= "gz">广州</li>
	 	<li >深圳</li>
	 	<li>郑州</li>
	 	<li>周口</li>
	 </ul>
</body>
</html>
~~~

省市联动菜单案例:

~~~js
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>test_javascript</title>
<style>
</style>
<script>
var cities;
window.onload=function(){
	//模拟查询所有的城市
	 cities=[
		["石家庄","保定","廊坊"],
		["郑州","洛阳","开封"],
		["合肥","阜阳","马鞍山"]
	];
}
//值改变方法
function change(){
	//alert("hello");// 点击选择其他省份的时候触发	
	var resu_1=document.getElementById("province");
	//alert(resu_1.value);
	//获取选中省份的序号
	var n=resu_1.value;
	//获取该省份对应的城市
	var p_cities=cities[n];
	//先删除之前的城市名(倒序) 增加新选择的省份的城市
	var select_2=document.getElementById("city");//获得父元素
    //不用获得子元素然后依次删除 直接重置省份下的option innerHTML可以保留结构.然后追加就可以了.
	select_2.innerHTML="<option>请选择</option>";//可以替代下边删除代码 利用了innerHTML的结构保留特性.直接把除了结构之外的内容重置.
	//var options=select_2.getElementsByTagName("option");//所有的子元素
	//删除旧城市名 所有的子元素
	//for (var i=options.length-1;i>0;i--){
		//select_2.removeChild(options[i]);
	//}
	// 追加新城市
	if (p_cities){
		for (var i=0;i<p_cities.length;i++){
			//创建一个新的option 
			var option=document.createElement("option");
			//把城市名赋值给option
			option.innerHTML=p_cities[i];
			//追加option
			select_2.appendChild(option);
		}
	}
}
</script>
</head>
<body>  
<!-- 省市联动:
创建省市下拉选,当改变省份的时候 更新市;
在省份上使用onchange值改变事件,在值发生改变的时候 结果随着改变.
-->
省:
	<select onchange="change();" id="province">
		<option value="-1">请选择:</option>
		<option value="0">河北省</option>
		<option value="1">河南省</option>
		<option value="2">安徽省</option>
	</select>
市:
	<select id="city">
		<option>请选择:</option>
	</select>
</body>
</html>

~~~

### 自定义对象  (直接创建对象(也叫JSON对象),使用函数构造器创建对象)

~~~js
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>test_javascript</title>
<style>

</style>
<script>
// 直接创建对象
function f1(){
	var student={"name":"zs","age":"20","work":function(){alert("java leaning")}};//创建学生对象
	alert(student.name);
	alert(student.age);
	student.work();
}
//采用内置构造器创建对象
function f2(){
	var teacher =new Object();
	teacher.name="gary";
	teacher.age="26";
	teacher.sex="male";
	teacher.work=function (){alert("hello world")};
	
	console.log(teacher.name);
	teacher.work();
}
//自定义构造器  声明一个函数,首字母大写,(供别人new) 声明参数(让调用者清楚要传的参数),让对象记住这些参数

function Coder(name,age,work){
	//记录参数
	this.name=name;
	this.age=age;
	this.job=work;
}
function f3(){
	var programmer=new Coder("gary",25,function(){alert("hello world")});
	alert(programmer.name);
	alert(programmer.age);
	programmer.job();
}
</script>
</head>
<body>  
<!-- 自定义对象
概述:自定义对象是一种特殊的数据类型,由属性和方法封装成.
对象名.属性名
对象名.方法名()
创建对象: 
直接创建对象,(直接量) var student = {"name":"za","age":"20"};就是按照dic的方式进行保存键值对.采用直接量创建的对象也叫JSON对象(轻量级对象)
使用构造器(new的函数,首字母大写就是用来new的,规范)创建对象,(内置构造器,自定义构造器)
	特殊构造器:Array ,Date,RegExp,Function
	通用:Object 
使用JSON创建对象 ,其实就是直接量创建对象.
总结:无论用那种方式创建对象 其实都是Object,如果是为了让大家引用,那么使用构造器自定义创建,
-->
<input type="button" value="按钮1" onclick="f1();"/>
<input type="button" value="按钮2" onclick="f2();"/>
<input type="button"value="按钮3" onclick="f3();"/>
</body>
</html>
~~~

### 事件: 

事件就是用户的操作,在页面元素状态改变,用户在操作鼠标键盘等时,触发的动作 (鼠标事件,键盘事件,状态改变事件), (event对象, 事件触发后将会产生一个event对象)

鼠标事件: onclick(单击),ondblclick,onmousedown,onmouseup,onmouseover(鼠标移到),onmouseout(鼠标移出).

键盘事件: onkeydown ,onkeyup

状态事件: onload ,onchange,onfocus,onblur,onsubmit.

~~~js
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>test_javascript</title>
<style>

</style>
<script>
//直接定义事件
function f1(){
	alert("hello world");
	
}
//后绑定事件 加载页面之后
window.onload=function(){
	var tie=document.getElementById("tie_after");
	tie.onclick=function(){alert("hello world")};//使用元素的属性.事件
};
//取消事件
function removeData(){
	//var result=confirm("are you sure to remove the result?")
	//return result;//这个结果有true 和false
	var result=confirm("are you sure?");
	result.preventDefault();
}
</script>
</head>

<body>  
<!-- 事件
事件就是用户的操作,在页面元素状态改变,用户在操作鼠标键盘时,触发的动作
 (鼠标事件,键盘事件,状态改变事件), 
(event对象, 事件触发后将会产生一个event对象)
事件的定义:
1.直接定义事件:在元素上通过事件属性直接定义(onclick) 直接但是耦合度(关系紧密程度)比较高
2.后绑定事件:在页面加载后使用js获取元素并绑定事件 ,耦合度低但是不直观.
取消事件: 在事件函数内 return false 分为 w3school的 preventDefault() ,和 return falsea两种方式
原本选择了删除按钮 就是不在询问直接删除，我们使用了取消事件 就会发生询问，是否取消 结果有true/false(可以参考正则表达式的密码验证)
-->
<input type="button" value="按钮1" onclick="f1();"/>
<input type="button" value="按钮2" id="tie_after"/>
<input type="button" value="cancle" id="cancle" onclick="return removeData();">
</body>
</html>
~~~

### 事件对象

~~~js
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>

</style>
<script>
function f1(e){//e 就是事件对象  包含了事件发生时候的一切信息
	//MouseEvent {isTrusted: true, screenX: 1571, screenY: -95, clientX: 35, clientY: 18, …}
	alert("hello world");
	console.log(e);
}
window.onload=function(){
	var btn=document.getElementById("btn");
	btn.onclick=function(e){// 不需要在写触发事件的时候传入event 浏览器自动传入 我们只需要在写函数的时候传入参数接受就可以了.
		console.log("hello world!");
		console.log(e);
	}
	
}
</script>
</head>
<body>
<!-- 事件对象
只要是用户触发了事件,有一些信息可以被确定下来,开发时候可能需要这些信息.浏览器方便开发者,将这些信息封装到一个对象里 event.
如何获取事件对象: 
直接定义事件:在调用函数时候直接传入event ,在写这个函数的时候
后绑定事件:触发事件时,浏览器会自动给函数传入event;在写函数的时候加参数来接收就可以了;
  -->
<input type="button" value="按钮1" onclick="f1(event);"/>
<input type="button" value="按钮2"  id="btn"/>
</body>
</html>
~~~

### 事件处理机制(冒泡机制/取消事件的冒泡机制) 以及事件源

~~~js
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>
div{
width:500px;
border:1px solid red;
padding:30px;
}
p{
border:1px solid red;
padding:30px;
}
</style>
<script>
function f1(e){
	alert("button");
	//不同的浏览器不同的结构 我们需要进行判断有哪个事件.
	//停止冒泡:
		//event={"stopPropagation":function(){}}
		//event={"cancelBubble":false}
	if (e.stopPropagation){//事件属性存在 不为空 判断对象有没有这个属性.
		e.stopPropagation();//如果存在就调用stopPropagation方法
	}else{
		e.cancelBubble=true;
	}
}
function f2(e){
	//通过事件对象获得事件源 仍然考虑浏览器的兼容问题e.srcElement  e.target;
	var obj=e.srcElement || e.target;
	console.log(obj);// 鼠标点击哪里 获取相对应元素的详细信息	
}
</script>
</head>
<body>
<!-- 事件处理机制:
冒泡机制:
事件从内到外传播 称为冒泡机制. 
可以取消事件的冒泡机制: event.stopPropagation()  event.cancelBubble=true;
冒泡机制的作用: 可以简化事件的定义. 可以在父元素上定义一个事件,接收众多子元素的事件.需要了解事件源.(事件发生的具体位置)
事件源通过事件对象获取事件源. 
  -->
  <!-- 在下边代码中,事件具有传递性,从内向外进行触发. 
  如: 我们点击了按钮 会一次显示 button , P , div.  
  如: 直接点击了p/div的区域 (p的会一次显示p,div),div元素区域只显示div.
  我们想要点按钮只触发按钮的事件,父标签的事件不再触发: 叫做取消事件的冒泡机制.
   -->
<div onclick="alert('div');">
	<p onclick="alert('p');">
		<input type="button" value="按钮1"  onclick="alert('button')"/>
		<input type="button" value="停止冒泡" onclick="f1(event);">
	</p>	 
</div>
<!-- 事件源的演示 -->
<div onclick="f2(event);">
<a href="#">百度</a>
<img src="../img/pic_roll_01.png">
<span>Gary</span>
</div>
</body>
</html>
~~~

使用事件源做计算器案例:

~~~js
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>
</style>
<script>
window.onload=function(){
	//后绑定事件 获取div 然后在div中进行数据计算
	var div=document.getElementById("jsq");
	div.onclick=function(e){
		//获取事件源  input /p/div
		var obj=e.srcElement||e.target;
		//判断之前获取P 
		var p =document.getElementById("screen");
		//只处理input
		if(obj.nodeName=="INPUT"){
			if(obj.value=="C"){
				//清空
				p.innerHTML="";
			} else if (obj.value=="="){
				//计算
				try{
					var result=eval("("+p.innerHTML+")");
					p.innerHTML=result;
				}catch(ex){
					p.innerHTML="error";
				}
			}else{
				//累加
				p.innerHTML+=obj.value;
			}
		}
	}
}
</script>
</head>
<body>
<!--事件源案例_计算器:
在父元素创建一个事件对象 接收所有的子元素的事件.简化事件定义,达到我们的目的
js 逻辑
-- 页面自己查找设计(assignment)
-->
</html>
~~~

## 第四章:JQuery 提高JavaScript的开发效率

jQuery 是JavaScript的一个框架,提高JS 的开发效率.极大的简化了js编程,.它封装了js,css,DOM,提供了一致的,简介的API.兼容CSS3 以及各种浏览器.使得用户更加方便地处理HTML,Event  实现动画效果,并且方便为网站提供AJAX交互. 可以为用户提供HTML页面"保持代码"和HTML"内容代码"的分离 它是一个轻量级的js库

jquery 利用选择器 选择一个DOM数组。然后封装成一个jQuery对象（包含了DOM数组和API）通过对象对API进行操作 这样就相对js一次操作一个document简化了许多。这个对象只能调用JQuery方法。我们可以把DOM封装成jQuery对象使用jQuery API. $(DOM)   jQuery 本质上就是DOM数组

~~~js
<!DOCTYPE HTML>  
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>

</style>
<script src="../HTML_T/JS/jquery-3.5.1.js">  //引入jQuery </script>  
<script>

function bigger(){
	//$("p");//选择器选中一组DOM数组。 选中页面上所有的p 相当于 document.getElementTagName "p:first" /last/其他(eq(下标))
	//取p的原始字号
	var size =$("p").css("font-size");//默认取第一个
	//alert(size); 假设16px
	//去掉单位(替换px 为空值) 便于增加字号
	size=size.replace("px","");
	//将字号+1再设置给段落
	$("p").css("font-size",++size+"px");
}
</script>
</head>
<body>
<!-- JQuery 
本质上是Js,他的文件是.js文件
使用:1.引入JQery的js文件,2.使用jQuery先选择器定位要操作的节点3.调用jQuery的API方法进行操作.

demo :
页面上增加一个+按钮 点击该按钮可以将页面的段落字体放大
 -->
 <p>
 页面上增加一个+按钮 点击该按钮可以将页面的段落字体放大
 </p>
 <input type="button" value="+" onclick="bigger()"/>
</body>

</html>
~~~

~~~js
<!DOCTYPE HTML>  
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>
</style>
<script src="../HTML_T/JS/jquery-3.5.1.js">  //引入jQuery </script>  
<script>
function print(){
	//使用选择器获取jquery对象
	var $ps=$("p");//一般我们在jquery对象名字前加$加以区分
	console.log($ps);
	for(var i =0;i<$ps.length;i++){
		//从jquery获得的值是DOM.
		var p=$ps[i];//这里是DOM对象
		console.log(p.innerHTML);
	}
}
//调用时传入了this 指代点击的图爱 
function change_1(img){
	console.log($(img).width());//转成jquery对象 获得宽高
	console.log($(img).height());
	//通过点击图片 使得图片变大变小;
	if ($(img).width()==823){
		$(img).width(1000).height(1000);//jquery对象方法返回的还是对象 所以我们可以直接再次调用
	}else{
		$(img).width(823).height(474);
	}	
}
</script>
</head>
<body>
<!-- jquery 的本质就是DOM数组 jquery对象才能调用jquery方法.DOM 对象调用DOM方法.
什么时候得到DOM 然后需要把它转化为Jquery对象.

 -->
 <input type="button" value="print" onclick="print();">
 <p>
 jquery 的本质就是DOM数组 jquery对象才能调用jquery方法.DOM 对象调用DOM方法.
 </p>
 <p>jquery 的本质就是DOM数组 jquery对象才能调用jquery方法.DOM 对象调用DOM方法.</p>
 <!-- 案例2  图片的变大变小 
 多张图片必须使用 this. 点击哪一张图片 指代的就是哪一张图片
 -->
 <div>
 <img src="../HTML_T/img/test_1.png" onclick="change_1(this);"/>
 </div>
</body>
</html>
~~~

### jQuery 选择器

jquery选择器包含了:
 基本选择器,层次选择器,过滤选择器(基本过滤,内容过滤,可见性过滤,属性过滤,状态过滤),表单选择器

~~~js
<!DOCTYPE HTML>  
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>
.demo,#id{
color:pink;
font-size:20px;
}
</style>
<script src="../HTML_T/JS/jquery-3.5.1.js">  //引入jQuery </script>  
<script>
//元素选择器
function f1(){
	alert("hello world");
	var p=$("p");
	console.log(p.css("font-size"));
}
//类选择器
function f2(){
	var cla=$("p.demo");
	console.log(cla.css("font-size"));
}
//组选择器
function f3(){
	alert("hello world");
	var group=$(".demo,#id");
	console.log(group.css("font-size"));
}
</script>
</head>
<body>
<!-- 基本选择器:
1.元素选择器 $("tag_name")
2.类选择器 $(".class_name")
3.id选择器  $("#id")
4.选择器组   $("#id,.importent");
----- ///实例见CSS 选择器
jQuery 使用 CSS 选择器来选取 HTML 元素。
$("p") 选取 <p> 元素。
$("p.intro") 选取所有 class="intro" 的 <p> 元素。
$("p#demo") 选取所有 id="demo" 的 <p> 元素。
 -->
 <input type="button" value="base_choicer" onclick="f3();"/>
<p>基本选择器</p>
<p class="demo">基本选择器</p>
<p id="id">基本选择器</p>
</body>
</html>
~~~

选择器demo

~~~js
<!DOCTYPE HTML>  
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>
#gz{
color:pink;
}
</style>
<script src="../HTML_T/JS/jquery-3.5.1.js">  //引入jQuery </script>  
<script>
// 层次选择器
window.onload=function(){
	//1.选择子孙
	console.log($("ul li"));//选择器选中满足2的所有元素 /$("ul>li")
	//2.选择兄弟
	console.log($("#gz+li"));// 选择id的下一个兄弟+li  ~ 是所有兄弟
	//基本过滤选择器
	console.log($("li:first"));// li元素的第一个li
	console.log($("li:even"));// li的偶数行元素 0 2 
	console.log($("li:eq(1)"));//下标等于1的li
	console.log($("li:not(empty)"));// li中下标不为空的
	console.log($("li:not(#gz)"));//li中id不为gz的元素
	//内容选择过滤器
	console.log($("li:contains(海)"));// 有海字的元素
	console.log($("li:empty")); //所有不包含子元素/文本元素的空元素
	//可见性过滤
	console.log($("li:hidden"));//不可见元素选择器
	console.log($("li:visible"))//可见元素选择
	//属性过滤
	console.log($("li[style]"));//选择具有style属性的li 
	//状态过滤
	console.log($("input:enabled"));//选择可用元素 密码 男 女
	console.log($("input:checked"));//选中 已经选中的radio
	//表单选择器:
	console.log($("input:radio"));//可以使用属性过滤 表单更简单
	console.log($(":password"));//可以直接冒号+名
}
</script>
</head>
<body>
<!-- 层次选择器:
选择子孙
 -->
 <!-- 过滤选择器
 1.基本过滤选择器(*) 常用于表格和列表
 :first 第一个元素, :last 最后一个元素,:not(selector) selector排除在外 ,:even 挑选偶数行 ,:add 挑选奇数行,
 :eq(index) 下标等于index的元素 ,:gt(index)下标大于index的元素 ,:lt(index) 下标小于index的元素,
 2.内容过滤选择器
 :contains(text) 匹配包含给定文本的元素
 :empty 匹配所有不包含子元素或文本的空元素
 3.可见性过滤选择器
 :hidden  匹配所有不可见元素 或者type为hidden的元素
 :visible 匹配所有可见元素
 4.属性过滤选择器
 [attribute] 匹配具有attribute属性的元素
 [attribute=value] 属性等于value的元素
 [attribute!=value] 属性不等于value的元素
 5.状态过滤选择器
 :enabled  匹配可用的元素
 :disabled 匹配不可用的元素
 :checked 匹配选中的CheckBox(radio)
 :selected 匹配选中的option(下拉选)
 6.表单选择器
 :text  匹配文本框
 :password  匹配密码框
 :radio  匹配单选框
 :checkbox 匹配多选框
 :submit 匹配提交按钮
 :reset 匹配重置按钮
 :button 匹配普通按钮
 :file 匹配文件框
 :hidden 匹配隐藏框
  -->
<ul>
<li>北京</li>
<li>上海</li>
<li id="gz">广州</li>
<li>深圳</li>
<li style="display:none;">郑州</li>
</ul>
<!--  状态过滤demo
disabled不可用  readonly只读,数据有效 可以提交服务器 但是disabled 数据无效,不能提交给服务器.
 -->
<p>
账号:
<input type="text" disabled />
密码:
<input type="password"/>
</p>
<p>
<input type="radio" name="sex" checked/>男
<input type="radio" name="sex"/>女
</p>
</body>
</html>
~~~

### jquery操作DOM

~~~js
<!DOCTYPE HTML>  
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>
</style>
<script src="../HTML_T/JS/jquery-3.5.1.js">  //引入jQuery </script>  
<script>
//jquery 等价于 window.onload=function(){} 
$(function(){
	//1.读写节点操作 读写内容(双标签才有内容),读写值(表单控件有值),读写属性() ,给我们两个方法 html()==innerHTML,text()==innerText.
	console.log($("p:eq(0)").html());//带有标签格式的内容,相当于 innerHTML
	//有了参数就是赋值 写内容
	console.log($("p:eq(0)").html("jquery对DOM操作提供了API支持 简化<u>DOM</u>的增删查(查就是选择器)"));//在网页中生效
	console.log($("p:eq(0)").text());//用法同上
	//读写值 val()==value
	console.log($(":button:first").val());
	//修改值
	console.log($(":button:first").val("button"));
	//读写属性attr()
	console.log($("img:first").attr("src"));
	console.log($("img:first").attr("src","../HTML_T/img/test_1.png"))
	//创建节点 $("节点内容") 创建之后需要挂到DOM树上
	var $ins= $("<li>南京</li>");
	var $ins2=$("<li>郑州</li>")
	console.log($ins);
	$("ul").append($ins);//挂载 ,插入到li的最后一个节点
	$("#gz").before($ins2);
	//删除节点 
	$("li:last").remove();
	//遍历  通过某个方法得到了广州
	var $gz=$("#gz");
	console.log($gz.parent());
	console.log($gz.next());
	var $ul=$("ul");
	console.log($ul.find("li:eq(0)"));	
});
</script>
</head>
<body>
<!-- JQuery 操作DOM (*)
读写节点
增删节点(创建DOM节点,插入DOM节点,删除DOM节点)
样式操作
遍历节点
插入DOM节点 
"parent".append(obj)作为最后一个子节点插入进来
"parent".prepend(obj) 作为第一个子节点添加进来
"brother".after(obj) 作为下一个兄弟节点添加进来
"brother".before(obj)作为上一个兄弟节点添加进来
删除DOM节点
obj.remove() 删除节点
obj.remove(selector) 只删除满足selector的节点
obj.empty() 清空节点
遍历节点 查找某个节点的relations.  我们调用别人的方法对一个节点进行操作,如果我们需要相关节点 我们不能直接得到选择器 ,那么我们就遍历节点.
.parent() 父节点
.children()/children(selector) 直接子节点
.next()/next(selector) 下一个兄弟节点
.prev()/prev(selector) 上一个兄弟节点
.siblings()/siblings(selector) 所有兄弟节点
.find(selector) 查找满足选择器的所有后代

 -->
 <p>
 	jquery对DOM操作提供了API支持 简化<b>DOM</b>的增删查(查就是选择器)
 </p>
 <p>
 	<input type="button" value="按钮"/>
 </p>
 <p>
 	<img src="../HTML_T/img/test_1.png"/>
 </p>
 <ul>
 	<li>北京</li>
 	<li>上海</li>
 	<li id=gz>广州</li>
 	<li>深圳</li>
 </ul>
</body>
</html>
~~~

### jquery样式操作

~~~js
<!DOCTYPE HTML>  
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>
.big{font-size:30px;}
.important{color:red;}
</style>
<script src="../HTML_T/JS/jquery-3.5.1.js">  //引入jQuery </script>  
<script>
//追加样式 <p class="big important">样式的操作</p> 可以两个类样式一起出现
$(function(){
	$("p:first").addClass("big").addClass("important");//给第一个P加class 样式
	//删除样式
	$("P:first").removeClass("big").removeClass("important");//返回的是jquery对象 所以可以直接继续调用
	$("p:first").removeClass();//删除所有样式
	//判断是否有某个样式
	var $result=$("p:eq(1)").hasClass("big");
	console.log($result);//false
	//切换样式  如果原元素有这个属性(相同) 就删除原来的 更换成新的样式 没有的话添加上这个样式
	//----
})
//切换样式 
function big(){
	$("p:eq(2)").toggleClass("big");
}
</script>
</head>
<body>
<!-- 样式操作:
addClass("") 追加样式
removeClass("") 移出制定样式
removeClass() 移除所有样式
toggleClass("") 切换样式
hasClass("") 判断是否有某个样式
css("") 读取css的值
css("","") 设置多个样式
 -->
 <p>
 <!-- 字体在不变和变大中切换 -->
 <input type="button" value="style" onclick="big();"/>
 </p>
 <p>样式的操作</p>
<p class="important">
切换为新的样式
</p>
</body>
</html>
~~~

### jquery 事件处理

~~~js
<!DOCTYPE HTML>  
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>

</style>
<script src="../HTML_T/JS/jquery-3.5.1.js">  //引入jQuery </script>  
<script>
$(function(){
	//用jquery后绑定事件, 给按钮绑定单击事件
	$(":button:eq(0)").click(function(e){
		alert("hello world");
		console.log(e);//此事件对象被jquery做了封装
	})
})
$(function(){
	//合成事件的demo jquery中的后绑定hover事件
	$("img").hover(
			
	function(){
		console.log("hello");
		$(this).width(1000).height(1000);
		// $(this).css("width","1000px").css("height","1000px");
	}, //悬停		
	function(){
		console.log("world");
		$(this).width(823).height(474);
	} //绑定
	);
})	
//toggle()demo
$(function(){
	$(":button:eq(1)").click(function(){
	//让图片在显示和隐藏之间切换
	$("img").toggle(); //点击按钮 图片隐藏 再次点击 图片显示
	})
});
//模拟事件
$(function(){
	$(":button:eq(2)").click(function(){
		//启动定时器 2秒一次
		var n=0;
		var id=setInterval(function(){
			//获取下一个要处理的框
			var $text=$(":text").eq(n);
			//模拟光标切入事件
			$text.trigger("focus");
			//生成随机的分数写入框内
			var score=parseInt(Math.random()*100);
			$text.val(score);
			//停止计时器
			if(n==$(":text").length-1){
				clearInterval(id);
			}
			n++;
		},2000);	
	});
});
</script>
</head>
<body>
<!-- jquery 事件处理 ，动画
语法： $obj.bind(事件类型，事件处理函数) $obj.bind('click',fn);简写:$obj.click(fn);
$obj.click();代表触发了函数
获取事件对象
此事件对象被jquery做了封装为了解决不同浏览器的兼容问题.进行了包装统一(取消事件冒泡,e.stopPropagation() 获取事件源 e.target)
获取事件源 e.target 返回值是DOM对象 获取鼠标点击坐标 e.pageX e.page.Y
jQuery的合成事件种类: 
hover(mouseenter,mouseleave)模拟鼠标悬停事件 parameter:鼠标悬停,鼠标离开
toggle() 在多个事件响应中切换 现在主要在显示和隐藏之间切换
模拟操作: 模拟人进行操作,例如巨幅广告的自动消失
$obj.trigger(事件类型)  $obj.trigger("focus"/click); 简写为 $obj.focus();
 -->
 <p>
 <input type="button" value="按钮"/>
 <input type="button"value="按钮2"/>
 </p>
 <img src="../HTML_T/img/test_1.png"/>
 <!-- 模拟操作
  -->
 <p>
 <input type="button" value="打分"/>
 </p>
 <p>
 谢威:<input type="text"/>
 </p>
 <p>
 振华:<input type="text"/>
 </p>
 <p>
  阿淼:  <input type="text"/>
 </p>
</body>
</html>
~~~

### jquery 动画

1.显示和隐藏的动画效果

2.自定义

~~~js
<!DOCTYPE HTML>  
<html>
<head>
<meta charset="utf-8">
<title>java_script_L</title>
<style>
/*  自定义动画  设置相对/决对/固定定位,然后做出动画效果.动画就是连续改变元素的偏移量*/
img{
position:relative;
}

</style>
<script src="../HTML_T/JS/jquery-3.5.1.js">  //引入jQuery </script>  
<script>
function f1(){
	//选择图片 添加时间之后 会逐渐变大变小（透明度）在规定时间内
	$("img").show();
}
function f2(){
	$("img").hide(2000,function(){//回调函数 在执行完了隐藏之后执行此函数 
		alert("hide finished")
	});
	
}
// 他们和show()效果一样 但是没有透明化缩小
function f3(){
	$("img").slideUp();
}
function f4(){
	$("img").slideDown();
}
//逐渐透明化的显示/隐藏
function f5(){
	$("img").fadeIn(2000);
}
function f6(){
	$("img").fadeOut(2000);
}
//这里是相对定位(想对于初始位置)进行既定路线的运动
function f7(){
	$("img").animate({"left":"300px"},3000).animate({"top":"300px"},3000).animate({"left":"0px"},3000).animate({"top":"0px"},3000);
}
</script>
</head>
<body>
<!-- 动画效果 实现原理就是通过定时器连续改变元素的样式(大小/透明度); 因此在执行完成动画效果(相当于一个线程)再执行其他函数就会出现并发问题
因此我们使用回调函数
显示隐藏效果
show()\hide() 通过同事改变元素的宽度和高度实现实现或者隐藏 $obj.show(执行时间(slow,normal,fast/毫秒数),回调函数(动画执行完毕后要执行的函数))
上下活动式动画实现  通过改变高度实现显示或者隐藏的效果
slideDown()/slideUp()
淡入淡出的动画效果 通过改变不透明度实现显示或者隐藏
fadeIn()/fadeOut()
自定义动画效果
animate(偏移位置,执行时间,回调函数)
 -->
 <input type="button" value="显示" onclick="f1();"/>
 <input type="button" value="隐藏" onclick="f2();"/>
 <input type="button" value="上拉 " onclick="f3();"/>
 <input type="button" value="下拉"  onclick="f4();"/>
 <input type="button" value="淡入"  onclick="f5();"/>
 <input type="button" value="淡出"  onclick="f6();"/>
  <input type="button" value="自定义"  onclick="f7();"/>
 <p>
 <img src="../HTML_T/img/test_1.png"/>
 </p>
</body>
</html>
~~~









