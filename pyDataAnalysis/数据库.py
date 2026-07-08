"""
数据库的 CURD
数据表的 CURD
表字段的 CURD
表数据的 CURD
窗口函数

数据库类型（按存储数据形式分类）：
关系型数据库(SQL数据库) ---> RDBMS
    MySQL，Oracle，SQLServer，DB2，SQLite
非关系型数据库(NoSQL数据库)
    Redis，HBASE，MongoDB

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
3. 注释写法： /* 多行注释的文本 */
            # 单行注释
            -- 单行注释



MySQL数据库：
 是C/S软件： Client【客户端】和Server【服务端】
 使用标准的SQL数据语言形式(增删改查)
 免费开源（mySQL5以上企业版收费）
    连接：
    命令行方式：mysql -h[IP地址] -P[端口号] -u[用户名] -p[密码]
    连接本机：mysql -u[用户名] -p[密码]
"""