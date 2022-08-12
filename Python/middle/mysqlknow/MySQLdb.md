import MySQLdb
# 连接数据库
conn = MySQLdb.connect(host="localhost",user="root",passwd="123123",db="qiwsirtest",charset="utf8")
host:等号的后面应该填写mysql数据库的地址，因为就数据库就在本机上（也称作本地），所以使用localhost，注意引号。如果在其它的服务器上，这里应该填写ip地址。一般中小型的网站，数据库和程序都是在同一台服务器（计算机）上，就使用localhost了。
user:登录数据库的用户名，这里一般填写"root",还是要注意引号。当然，如果读者命名了别的用户名，数据库管理者提供了专有用户名，就更改为相应用户。但是，不同用户的权限可能不同，所以，在程序中，如果要操作数据库，还要注意所拥有的权限。在这里用root，就放心了，什么权限都有啦。不过，这样做，在大型系统中是应该避免的。
passwd:上述user账户对应的登录mysql的密码。我在上面的例子中用的密码是"123123"。不要忘记引号。
db:就是刚刚通create命令建立的数据库，我建立的数据库名字是"qiwsirtest"，还是要注意引号。看官如果建立的数据库名字不是这个，就写自己所建数据库名字。
port:一般情况，mysql的默认端口是3306，当mysql被安装到服务器之后，为了能够允许网络访问，服务器（计算机）要提供一个访问端口给它。
charset:这个设置，在很多教程中都不写，结果在真正进行数据存储的时候，发现有乱码。这里我将qiwsirtest这个数据库的编码设置为utf-8格式，这样就允许存入汉字而无乱码了。注意，在mysql设置中，utf-8写成utf8,没有中间的横线。但是在python文件开头和其它地方设置编码格式的时候，要写成utf-8。切记！


Python建立了与数据的连接，其实是建立了一个MySQLdb.connect()的实例对象，或者泛泛地称之为连接对象，python就是通过连接对象和数据库对话。这个对象常用的方法有：
commit()：如果数据库表进行了修改，提交保存当前的数据。当然，如果此用户没有权限就作罢了，什么也不会发生。
rollback()：如果有权限，就取消当前的操作，否则报错。
cursor([cursorclass])：返回连接的游标对象。通过游标执行SQL查询并检查结果。游标比连接支持更多的方法，而且可能在程序中更好用。
close()：关闭连接。此后，连接对象和游标都不再可用了。

cur = conn.cursor()
此后，就可以利用游标对象的方法对数据库进行操作。那么还得了解游标对象的常用方法：

名称	描述
close()	关闭游标。之后游标不可用
execute(query[,args])	执行一条SQL语句，可以带参数
executemany(query, pseq)	对序列pseq中的每个参数执行sql语句
fetchone()	返回一条查询结果
fetchall()	返回所有查询结果
fetchmany([size])	返回size条结果
nextset()	移动到下一个结果
scroll(value,mode='relative')	移动游标到指定行，如果mode='relative',则表示从当前所在行移动value条,如果mode='absolute',则表示从结果集的第一行移动value条.