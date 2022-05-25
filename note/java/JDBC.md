### JDBC

Jar包安装和依赖关系调整

Maven 是基于jdk的 我们需要下载maven包,然后安装配置环境变量

mvn install:install-file -Dfile=D:\javafile\commons-dbcp-1.4.jar -DgroupId=com.javaworld -DartifactId=dbcp_gary -Dversion=1.0.0 -Dpackaging=jar

或者直接在eclipse中选中pom.xml文件，run as -》maven build

在命令行输入以上代码 注意文件地址等配置信息;

结果会显示build success;

最简单: 在代码文件中创建一个Lib 文件,把jar包拷贝进去,然后在pom文件中添加配置

<dependency>

<groupId>名字</groupId>  

<artifactId>名字</artifactId>  

<version>0.0.1</version>  

<scope>system</scope>  

<systemPath>${project.basedir}/lib/jar包名 

</systemPath>

</dependency>

 

\1. WHAT WHY HOW ?

WHAT: JAVA DATAEBASES CONNECTIVITY.就是java到数据库的桥梁;

JDBC定义了一套标准接口,就是访问数据库的通用API

JDBC接口的实现类称为数据库驱动,由各个数据库厂商提供,使用JDBC必须导入对应数据库的驱动

JDBC接口及数据库厂商实现:

驱动管理:DriverManager 

连接接口:Connection   DatabaseMetaData

语句接口:Statement  PreparedStatement  CallableStatement 

结果集接口:ResultSet  ResultSetMetaData

### JDBC使用步骤:

​	/*

​	 * 1.导入JDBC驱动jar

​	 * 2.注册JDBC驱动 (加载驱动建立连接)

​	 * 3.获得connection对象()

​	 * 4.创建statement(语句)对象(创建语句对象)

​	 * 5.处理SQL执行结果(执行SQL语句)

​	 * 6.关闭数据连接

​	 */

 

 Driver manager :

 

Jar包的导入问题----

package jdbc_L;

 

import java.sql.Connection;

import java.sql.DriverManager;

import java.sql.SQLException;

import java.sql.Statement;

 

public class Jdbc_L {

​	/*

​	 * 1.导入JDBC驱动jar

​	 * 2.注册JDBC驱动(Class.forname())

​	 * 3.获得connection对象

​	 * 4.创建statement(语句)对象

​	 * 5.处理SQL执行结果

​	 * 6.关闭数据连接

​	 */

 

​	public static void main(String[] args) throws ClassNotFoundException, SQLException {

​		Class.forName("oracle.jdbc.OracleDriver");//导入jdbc包然后引导驱动;

​		//连接到数据库:

​		String url="jdbc:oracle:thin:@localhost:1521:xe";

​		String user="system";

​		String password="123456";

​		Connection conn=DriverManager.getConnection(url, user, password);//这个方法是查找并尝试连接数据库

​		System.out.println(conn.getClass());// 输出connection引用对象的实际类型;证明驱动程序提供了connection的实现类;

​		// 结果:class oracle.jdbc.driver.T4CConnection

​		//Statement 接口:execute() executeQuery() executeUpdate();

​		//创建"statement语句"对象;

​		Statement st = conn.createStatement();

​		//执行sql语句;

​		String ddl ="create table robin_demo"+"(id number(6),"+"name varchar2(20))";

​		boolean b=st.execute(ddl);// 返回boolean结果 ,有没有结果集,创建失败抛出异常没有异常就是创建成功,;

​		System.out.println(b); //false

​		conn.close();

​	}

 

}

​		/**

​		 * 插入数据库DML语句

​		 */

​		//注册驱动:class.forname("")

​		Class.**forName**("oracle.jdbc.OracleDriver");

​		//连接数据库:

​		String url="jdbc:oracle:thin:@localhost:1521:xe";

​		String user="system";

​		String password="123456";

​		Connection conn=DriverManager.**getConnection**(url, user, password);

​		//创建Statement对象

​		Statement st=conn.createStatement();

​		//执行dml

​		//String dml="insert into robin_demo(id,name) values(001,'gary')";

​		String dml="update robin_demo set name='Jerry' where id=1"; 

​		//String dml ="delete from robin_demo where id =1";

​		st.executeUpdate(dml);

​		// 关闭连接

​		conn.close();

处理结果集 ResultSet:

 /**

​		 * 插入数据库DQL语句

​		 * 

​		 * 

​		 * 注册驱动 class.forname

​		 * 连接数据库

​		 * 创建Statement

​		 * 执行SQL

​		 * 处理结果

​		 * 关闭连接

​		 */

​		Class.**forName**("oracle.jdbc.OracleDriver");

​		//Class.forName(driver);

​		String url="jdbc:oracle:thin:@localhost:1521:xe";

​		String user="system";

​		String password="123456";

​		Connection conn =DriverManager.**getConnection**(url, user, password);

​		Statement st=conn.createStatement();

​		String sql="select id,name from robin_demo";

​		//返回值; 结果集 java发送SQL语句到数据库 拿到数据 返回给java一个映射的结果集,结果集有一个游标在第一行上边 使用while语句next()方法进行遍历出所有数据

​		ResultSet rs=st.executeQuery(sql);

​		//处理结果:

​		***\*while\**** (rs.next()) {

​			***\*int\**** id=rs.getInt("id");

​			String name=rs.getString("name");

​			System.***\**out\**\***.println(id+","+name);  // 遍历打印输出数据库的id和name 

​		}

​		//关闭连接:

​		conn.close();

​	通过封装连接来简化连接过程,

封装类:

***\*package\**** jdbc_L;

***\*import\**** java.io.InputStream;

***\*import\**** java.sql.Connection;

***\*import\**** java.sql.DriverManager;

***\*import\**** java.sql.SQLException;

***\*import\**** java.util.Properties;

/**

 \* 封装的连接数据库注册连接,简化连接;

 \* ***\*@author\**** Administrator

 *

 */

***\*public\**** ***\*class\**** Dbutils {

​	//静态变量 只要一分就可以了;优化这里在文件中进行读取;创建一个文件 db.properties

​	/**

​	 * properties 就是为了读取 *.properties文件而设计的api 其底层就是文件的io 本身实现map接口 内部是散列表,限定了key和value都是String类型;

​	 * load(流) 将文件读取为散列表,String getproperties(key) 查询value  

​	 * 使用步骤:

​	 * 创建properties对象:

​	 * Properties ppt=new Properties();

​	 * 利用load方法读取文件

​	 * InputStream in=Dbutils.Class.getClassLoader().getResourceAsStream("db.properties");

​	 * ppt.load(in);

​	 * 查找文件内容 就是读取文件内容;

​	 * String s = ppt.getProperty("jdbc.driver"); // 这里是Key

​	 * 

​	 * 

​	 */

​	***\*static\**** String **Driver** ;

​	***\*static\**** String **url**;

​	***\*static\**** String **user**;

​	***\*static\**** String **password**;

​	//静态代码块 初始化静态属性;

​	***\*static\**** {

​		//使用properties 读取配置文件

​		***\*try\**** {

​		Properties ppt=***\*new\**** Properties();

​		InputStream in = Dbutils.***\*class\****.getClassLoader().getResourceAsStream("db.properties");

​		ppt.load(in);

​		//System.out.println(ppt);//打桩

​		//初始化 连接参数;

​		**Driver**=ppt.getProperty("jdbc.driver");

​		**url**=ppt.getProperty("jdbc.url");

​		**user**=ppt.getProperty("jdbc.user");

​		**password**=ppt.getProperty("jdbc.password");

​		}***\*catch\****(Exception e){

​			e.printStackTrace();

​			***\*throw\**** ***\*new\**** RuntimeException(e);

​		}

​	}

​	

​	***\*public\**** ***\*static\**** Connection getConnection() {

​		***\*try\**** {

​		Class.**forName**(**Driver**);

​		Connection conn=DriverManager.**getConnection**(**url**,**user**,**password**);

​		***\*return\**** conn;

​		}***\*catch\****(Exception e) {

​			e.printStackTrace();

​			***\*throw\**** ***\*new\**** RuntimeException(e);// 这一句是为了处理return问题.

​		}

​	}

​	// 关闭数据库连接封装:

​	***\*public\**** ***\*static\**** ***\*void\**** close(Connection conn) {

​		***\*if\**** (conn!=***\*null\****) {

​			***\*try\**** {

​				conn.close();

​			}***\*catch\**** (Exception e) {

​				e.printStackTrace();

​			}

​		}

​	}	

}

 

主方法:

/**

 \* 连接管理:数据库的连接 注册,连接等封装起来作为一个类,使我们使用起来更加便利;

 */

***\*public\**** ***\*class\**** Jdbc_L {

​	***\*public\**** ***\*static\**** ***\*void\**** main(String[] args) ***\*throws\**** SQLException {

​		Connection conn=Dbutils.**getConnection**();

​		Statement st=conn.createStatement();

​		String sql="select * from robin_demo";

​		ResultSet rs=st.executeQuery(sql);

​		***\*while\****(rs.next()) {

​			***\*int\**** id=rs.getInt("id");

​			String name =rs.getString("name");

​			System.***\**out\**\***.println(id+","+name);

​		}

conn.close();}}

主方法优化:

 

***\*import\**** java.sql.Connection;

***\*import\**** java.sql.DriverManager;

***\*import\**** java.sql.ResultSet;

***\*import\**** java.sql.SQLException;

***\*import\**** java.sql.Statement;

/**

 \* 连接管理:数据库的连接 注册,连接等封装起来作为一个类,使我们使用起来更加便利;

 \* 

 \* ***\*@author\**** Administrator

 *

 */

***\*public\**** ***\*class\**** Jdbc_L {

​	***\*public\**** ***\*static\**** ***\*void\**** main(String[] args) ***\*throws\**** SQLException {

​			Connection conn=***\*null\****;

​		***\*try\**** {

​			conn=Dbutils.**getConnection**();

​			Statement st=conn.createStatement();

​			String sql="select * from robin_demo";

​			ResultSet rs=st.executeQuery(sql);

​			

​			***\*while\****(rs.next()) {

​				***\*int\**** id=rs.getInt("id");

​				String name =rs.getString("name");

​				System.***\**out\**\***.println(id+","+name);

​				//如果重复使用结果集和语句对象 我们可以使用close()关闭它;

​				}

​			rs.close();

​			st.close();

​		// 关闭不可靠 出现异常所以出现在finally里,但是写这里比较繁琐;我们封装到Dbutils里

​	}***\*catch\****(Exception e) {

​		e.printStackTrace();

​	}***\*finally\****{

​		conn.close();

​	}

​	}

}

 

JDBC主要用于数据库和java的通信操作管理问题 在java中是属于固定套路的代码

\1. 创建连接,conn ; 

\2. Trycatch处理异常;

\3. 创建语句 statement;

\4. 创建sql语句

\5. 执行sql语句 st.execute**()

\6. 返回结果集的处理

\7. 关闭连接;

连接池技术![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml1644\wps1.jpg)

 

 

 

DBCP(DataBase connection pool)

连接池管理工具类;使用与并发场合;只需要前期创建一个连接池就可以;

通过连接池对并发线程进行管理,使得用户在使用的时候从连接池拿去连接,用完之后进行归还;

 

JDBC的核心;

preparedStatement预处理机制:执行计划,完全相同的sql语句使用同一个实行计划;可以有效提高数据库的效率  sql语句将使用带参数的语句,然后在创建执行计划之后赋值参数 再由执行计划执行;参数需要注意注入攻击;

 \* preparedStatement原理和使用:执行计划,带参数的sql语句;

 \* ***\*@author\**** Administrator

 *preparedStatement pstmt=con.prepareStatement("update emp set job=? where empno=?");创建语句;

 *pstmt.setLong(1,"Manager");  赋值参数

 *pstmt.setInt(2,1001);

 *pstmt.executeUpdate();  执行语句;

 

 

​	***\*public\**** ***\*static\**** ***\*void\**** main(String[] args) {

​		Connection conn=***\*null\****;

​		***\*try\**** {

​			conn=Dbcp_utils.**getConnection**();

​			//创建带参数的sql语句;

​			String sql="insert into robin_demo (id,name) values (?,?)";

​			// 将sql发送到数据库,创建执行计划;

​			PreparedStatement ps= conn.prepareStatement(sql);

​			//替换执行计划中的参数,按照顺序

​			ps.setInt(1,9);// 替换的执行计划

​			ps.setString(2, "goi");

​			***\*int\**** n=ps.executeUpdate();// 执行语句;返回值是1 o是拒绝

​			//我们可以再次调用ps然后执行;

​			ps.setInt(1, 10);

​			ps.setString(2, "Andy");

​			ps.executeUpdate();

​			System.***\**out\**\***.println(n);

​			

​		} ***\*catch\**** (Exception e) {

​		e.printStackTrace();

​		

​		}***\*finally\**** {

​			Dbcp_utils.**close**(conn);

​		}

 

​	}

 

事务管理:

 原子性(Atomicity),一致性(Consistency),隔离性(Isolation),持久性(Durability)

 \* atomicity:事务必须是原子工作单元,对于数据修改,要么全部执行,要么全部不执行.

 \* consistency:事务完成时候,必须使所有的数据都保持一直状态;

 \* isolation:由并发事务所作的修改必须与任何其他并发事务所做的修改隔离;

 \* durability: 事务完成之后,对系统的影响必须是永久性的;

 

 

 

​	***\*public\**** ***\*static\**** ***\*void\**** main(String[] args) {

​	**pay**(1,3,500); // 方法调用;

​	System.***\**out\**\***.println("程序完成");

​		

 

​	}

​	//汇款方法;

​	***\*public\**** ***\*static\**** ***\*void\**** pay(***\*int\**** from ,***\*int\**** to,***\*double\**** money) {

​		// 两个sql语句;

​		String sql_1="update r_account set balance=balance+? where id=?";

​		String sql_2="select balance from r_account where id=?";

​		Connection conn=***\*null\****;

​		***\*try\**** {

​			conn=Dbcp_utils.**getConnection**(); // 创建连接从配置文件DBCP_utils;

​			conn.setAutoCommit(***\*false\****);// 取消自动提交,后期手动提交

​			//sql 语句...从原账户减去钱数;

​			PreparedStatement ps=conn.prepareStatement(sql_1);//创建执行计划;

​			ps.setDouble(1,-money); //设置第一个参数;

​			ps.setInt(2,from);//设置第二个参数;

​			***\*int\**** n=ps.executeUpdate();// 执行计划和返回值;

​			***\*if\**** (n!=1) {

​				***\*throw\**** ***\*new\**** Exception("扣款不正确,请检查账户");

​			}

​			ps.setDouble(1, money);//传参

​			ps.setInt(2,to);

​			n=ps.executeUpdate();

​			***\*if\****(n!=1) {

​				***\*throw\**** ***\*new\**** Exception("钱到账问题,请到附近银行查询");

​			}

​			ps.close();

​			ps=conn.prepareStatement(sql_2);//执行计划的重新赋值 反复重用;

​			ps.setInt(1, from);

​			ResultSet rs=ps.executeQuery();

​			System.***\**out\**\***.println("success");

​			***\*while\****(rs.next()) {

​				***\*double\**** bal=rs.getDouble(1);

​				***\*if\**** (bal<0) {

​					***\*throw\**** ***\*new\**** Exception("余额透支");

​				}

​			}

​			

​			//中间异常抛出(余额不足;)

​			//

​			conn.commit();

​			

​		} ***\*catch\**** (Exception e) {

​			e.printStackTrace();

​			Dbcp_utils.**rollback**(); // 异常 回滚;

​			

​		}***\*finally\**** {

​			Dbcp_utils.**close**(conn);

​		}

​	}

 

批量处理:

Batch 是指大量处理数据库,主要是查询DQL语句等;

 addBatch(string sql)

 addBatch()

 executeBatch()

 clearBatch()

 

 

​	***\*public\**** ***\*static\**** ***\*void\**** main(String[] args) {

​		//批sql ddl 一般主要用于dml DQL批处理修改数据,

//		String sql_1="create table log_01 (id number(8), msg varchar2(100))";

//		String sql_2="create table log_02 (id number(8), msg varchar2(100))";

//		String sql_3="create table log_03 (id number(8), msg varchar2(100))";

//		String sql_4="create table log_04 (id number(8), msg varchar2(100))";

//		String sql_5="create table log_05 (id number(8), msg varchar2(100))";

​		String sql_1="insert into log_01(id,msg) values(1,'hello')";

​		String sql_2="insert into log_02(id,msg) values(1,'hello')";

​		Connection conn=***\*null\****;

​		***\*try\**** {

​			conn=Dbcp_utils.**getConnection**();//创建连接;

​			Statement st= conn.createStatement();//创建语句

​			//没有执行 只是缓存

​			st.addBatch(sql_1);//批量数据;

​			st.addBatch(sql_2);

//			st.addBatch(sql_3);

//			st.addBatch(sql_4);

//			st.addBatch(sql_5);

​			//执行

​			***\*int\**** [] ary=st.executeBatch();//批量执行

​			System.***\**out\**\***.println("执行完毕");

​		} ***\*catch\**** (Exception e) {

​			e.printStackTrace();

​			

​		}***\*finally\**** {

​			Dbcp_utils.**close**(conn);

​		}

}

批量参数处理;既然可以批量处理sql 那么我们做好执行计划是否可以批量进行传参处理呢?

 

 

​	***\*public\**** ***\*static\**** ***\*void\**** main(String[] args) {

​		String sql="insert into robin_user (id,name,pwd)values(?,?,?)";//sql

​		Connection conn=***\*null\****;

​		***\*try\**** {

​			conn=Dbcp_utils.**getConnection**();

​			PreparedStatement ps=conn.prepareStatement(sql);//执行计划;

​			//替换参数  循环给表格进行填充数据;

​			***\*for\****(***\*int\**** i=0;i<100;i++) {

​				ps.setInt(1, i);

​				ps.setString(2, "name"+i);

​				ps.setString(3,"123456");

​				//将参数添加到批处理缓冲区;

​				ps.addBatch();

​				//使用判断进行批处理 防止内存溢出(outofmemory);

​				***\*if\****((i+1)%8==0) {

​					***\*int\**** [] ary=ps.executeBatch();

​					ps.clearBatch();

​					System.***\**out\**\***.println(Arrays.**toString**(ary));

​				}

​				//批量执行;

//				int [] ary=ps.executeBatch();

//				System.out.println(Arrays.toString(ary));

//				ps.clearBatch();//清空缓存区;

​			}

​			

​			

​			

​		} ***\*catch\**** (Exception e) {

​			e.printStackTrace();

​		}***\*finally\**** {

​			Dbcp_utils.**close**(conn);

​		}

​	}

 

/**

 \* JDBC返回自动主键api

 \* 两个表之间有关联,例如话题和关键字在不同的表中,但是需要我们关联他们;

 \* get.generatekeys()

 \* 

 \* ***\*@author\**** Administrator

 *

 */

 

***\*public\**** ***\*class\**** Serialization_Id {

 

​	***\*public\**** ***\*static\**** ***\*void\**** main(String[] args) {

​		Connection conn=***\*null\****;

​		

​		***\*try\**** {

​			conn=Dbcp_utils.**getConnection**();

​			//事务保护;

​			conn.setAutoCommit(***\*false\****);

​			String sql_1="insert into r_keywords(id,word) values (k_seq.nextval,?)";

​			

​			//自动生成序号的列名; 先生成话题,

​			String[] cols= {"id"};

​			PreparedStatement ps=conn.prepareStatement(sql_1,cols);

​			ps.setString(1,"雾霾");

​			***\*int\**** n=ps.executeUpdate();

​			***\*if\**** (n!=1) {

​				***\*throw\**** ***\*new\**** Exception("话题生成失败");

​			}

​			//获取自动生成id

​			ResultSet rs=ps.getGeneratedKeys(); 

​			***\*int\**** id=-1;

​			***\*while\****(rs.next()) {

​				id=rs.getInt(1);

​			}

​			rs.close();

​			ps.close();

​			String sql_2="insert into r_post(id,content,k_id)values(p_seq.nextval,?,?)";

​			//

​			ps=conn.prepareStatement(sql_2);

​			ps.setString(1, "今天天气不错,晚上有月亮");

​			ps.setInt(2, id);

​			n=ps.executeUpdate();

​			***\*if\**** (n!=1) {

​				***\*throw\**** ***\*new\**** Exception("天气太糟");

​			}

​			conn.commit();

​			System.***\**out\**\***.println("success");

​		} ***\*catch\**** (Exception e) {

​			e.printStackTrace();

​			Dbcp_utils.**rollback**();

​		}***\*finally\**** {

​			Dbcp_utils.**close**(conn);

​		}

 

​	}

 

}

 

 

/**

 \* ResultSetMetaData 数据结果集的元数据;

 \* 就是查询结果集的相关信息 包含列名,列数量,列数据类型等;

 \* ***\*@author\**** Administrator

 *

 */

***\*public\**** ***\*class\**** ResultSet_MD {

 

​	***\*public\**** ***\*static\**** ***\*void\**** main(String[] args) {

​	Connection conn=***\*null\****;

​		***\*try\**** {

​			conn=Dbcp_utils.**getConnection**();

​			String sql="select * from robin_demo";

​			Statement st=conn.createStatement();

​			ResultSet rs = st.executeQuery(sql);//就行语句,返回结果集数据;

​			// 结果集元数据的处理;

​			ResultSetMetaData meta= rs.getMetaData();

​			***\*int\**** n=meta.getColumnCount();//列的数量

​			String name=meta.getColumnName(1);//列名

​			String name1=meta.getColumnName(2);//列名

​			System.***\**out\**\***.println(n+","+name+","+name1);  //2,ID,NAME

​			

​		} ***\*catch\**** (Exception e) {

​			e.printStackTrace();

​			

​		}***\*finally\**** {

​			Dbcp_utils.**close**(conn);

​		}

 

​	}

 

}

DAO事务封装; 就是封装JDBC的事务处理;

 

 