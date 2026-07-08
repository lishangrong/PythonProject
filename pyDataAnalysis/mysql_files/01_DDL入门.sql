/*

DDL：数据定义语言,主要怕是操作 数据库，数据表，字段，进行：增删改查(CURD)
    涉及到的关键字：create，drop，alter，show
    create database if not exists 数据库名 charset 'utf8'
    show databases;  # 显示已有的数据库
    use 数据库名  # 使用指定数据库
    create table 表名(
        字段名1 数据类型 [约束],
        字段名2 数据类型 [约束],
        字段名3 数据类型 [约束],
    );
    show tables; # 展示所有表
    desc 表名    # 展示表信息
    rename table 旧表名 to  新表名  # 重命名
    drop table 表名  # 删除表

DML：数据操作语言，主要是操作 表数据，进行：增删改(CUD)
    涉及到的关键字：insert，delete，update
DQL：数据查询语言，主要是操作 表数据，进行：查询操作(R)
    涉及到的关键字： select，from，where
DCL：数据控制语言，主要是 创建用户，设置权限，隔离级别等
适用语法：
1. SQL语句可以写一行，也可以写多行，最后用 分号 结尾。
2. SQL语句不区分大小写，为了阅读方便，建议关键字大写，其他小写。
3. 注释写法： /星 多行注释的文本 星/
            # 单行注释
            -- 单行注释


数据类型：
    概述：用来限定某列值的范围的，必须是：整数，小数，字符串，日期等...
    常用的数据类型：
        整型：int
        浮点数：double, float, decimal
        日期型：datetime
        字符串型：varchar(长度)
约束：
    概述：在数据类型限定的基础上，进一步对该列值做 限定
    常见约束：
      单表约束：
        primary key：主键约束，唯一标识表中的一行记录。特点：非空，唯一，一般结合 auto_increment(自动增长，自增) 一起使用。
        not null：   非空约束， 此字段不允许填写空值。 NULL 表示空
        unique:      唯一约束， 此字段不允许重复
        default:     默认约束
    多表约束：
        foreign key: 外键约束，对关系字段进行约束

添加修改删除表字段：
# 添加表字段
    alter table 表名 add 列名 类型(长度) [约束]
# 修改表字段：
    alter table 表名 change 旧列名 新列名 类型(长度) [约束]
# 删除表字段
    alter table 表名 drop 列名

    */




# ------------------------案例1 DDL语句(数据定义语言) 操作 数据库(database)------------------------
# 1.查看(已创建的)所有数据库
show databases;

# 2.创建数据库
create database day01; # 以默认码表(utf8)
create database day02 character set 'gbk'; # 以GBK码表，创建数据表
create database day01; # 报错，因为数据库存在
create database if not exists day01;
# 完整建库格式
create database if not exists day03 charset 'utf8';

# 3.修改数据库 -->码表
alter database day02 charset 'utf8';

# 4.删除数据库
drop database day01;
drop database day02;
drop database day03;

# 5.查看当前用的哪个数据库
select database();

# 6.切换数据库
use day01;

# 7. 查看某个指定数据库的数据库码表
show create  database day01; # 默认 utf-8码表
show create  database day02; # gbk码表

# ------------------------案例2 DDL语句(数据定义语言) 操作 数据表(table)----------------------
# 1. 切库
use day01;
# 2. 查看（当前数据库中）所有数据表
show tables;
# 3. 创建数据表 学生表： student, 字段为sid, name，age
create table if not exists student (
    sid int,             # 学生学号
    name varchar(20),    # 学生姓名
    age int              # 学生年龄
);

# 4. 修改数据表名 student --> stu
rename table student to stu;

# 5. 删除数据表
drop table if exists stu;

# 6 查看表结构
# show create table stu;
desc student;

# ------------------------案例3 DDL语句(数据定义语言) 操作 字段(Field)----------------------
use day01;
show tables;
desc student;
# 给student表添加字段 address varchar(20)
alter table student add address varchar(20) not null;
# 修改字段
# 场景1：只修改数据类型 和 约束
# 格式： alter table 表名 modify 新列名 数据类型 [约束]
alter table student modify address int;

# 场景2  即修改数据类型 和 约束，还修改字段 address --> add varchar(10)
# 格式 alter table 表名 change 旧列名 新列名 新的数据类型 [新的约束]
alter table student change address  addr varchar(10) not null;

# 删除字段
# 格式： alter table 表名 drop 字段名
alter table student drop addr;
