一、数据库(database)层面
(1)查看所有数据库。
show databases;
(2)添加数据库,并设置对应的编码。
create databases database_name character set utf8;（utf8中间不能有“-”）
或
CREATE DATABASE IF NOT EXISTS database_name DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
**COLLATE utf8_general_ci的理解：**
作用：设置数据库校对规则。
ci是case insensitive的缩写，意思是大小写不敏感；
相对的是cs，即case sensitive，大小写敏感；
还有一种是utf8_bin，是将字符串中的每一个字符用二进制数据存储，区分大小写。
如果建表的时候选择的是区别大小写的规则而查询的时候又暂时不想区别，可以用类似 WHERE column_name COLLATE utf8_general_ci = 'xxx' 的写法改变查询使用的校对规则
(3)删除数据库。
drop database database_name;
(4)切换数据库。
use database_name

二、表(table)层面
(1)查看所有的表。
show tables;
(2)创建表。
create table table_name (
    id Integer primary key auto_increment,
    age int,
    name varvhar(32),
)
(3)查看表(能够显示字段名称、大小、是否为空、是否外键、默认值、额外设置)。
describe table_name; //查看表名为table_name 的表
(4)查看表的详细sql构建语句。
show create table table_name;
(5)删除表。
drop table table_name; 
(6)修改表名。
alter table old_table_name rename [to] new_table_name;
(7)在表中增加字段。
alter table table_name add 属性名 属性类型； //在表的最后一个位置增加字段。
alter table table_name add 属性名 属性类型 first; //在表的第一个位置增加字段
alter table table_name add 属性名 属性类型 after 已有的属性名； //在关键字所指的属性后边增加字段
(8)删除字段。
alter table table_name drop 属性名；
(9)修改字段。
修改字段的数据类型：
alter table table_name modify 属性名 数据类型；
修改字段的名称
alter table table_name change 旧属性名 新属性名 旧数据类型；
同时修改字段的名称和数据类型
alter table table_name change 旧属性名 新属性名 新数据类型；
(10)修改字段的顺序：
alter table table_name modify 属性名1 数据类型 first/after 属性名2；
属性名1 代表要修改的字段，”first“代表把属性1放到表的第一个位置，“after 属性名2 ”代表把属性1调整到属性2后边。

三、字段/列(column)
