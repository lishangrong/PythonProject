/*
DML语句详解：
    概述：
        它叫数据操作语言，主要是 操作 表结构， 进行 增删改操作的。
        实际开发中，增删改统称为 --> 更新语句。
    细节：
        进行删除，修改前，一定一定一定要备份，一个过来人的含泪忠告。
    添加数据：
      格式：
        insert into 数据表名(列名1,列名2,列名3...) values(值1,值2,值3...)
        insert into 数据表名 values(值1,值2,值3...)
        insert into 数据表名 values(值1,值2...), (值1,值2...)...
     细节：
        1. 要添加的值的个数，必须 和 列名及其类型对应.
        2. 如果不写列名，默认是：全列名.
    修改数据：
      格式：
        update 数据表名 set 字段名=值,字段名=值...where 条件;
    删除数据：
      格式：
        delete from 数据表名 where 条件;
        truncate table 数据表名;   相当于把表摧毁了，然后在创建一张一模一样的表，即：会重置主键id


*/

#------------------------案例1 DML语句(数据操作语言) 操作 表数据(data) 增----------------------
#1. 切库，查表
use day01;
show tables;

# 2. 创建分类表，分类id，分类名，描述信息
create table category(
    cid int,
    cname varchar(20),
    info varchar(100)
);

# 3. 往表中添加数据
insert into category(cid, cname) values(1, '电脑');
# insert into category(cid, cname) values(1, '电脑', 3); # 报错，列的个数 和 值的个数 不匹配

insert into category values(2, '手机', '华为手机666');
# insert into category values(3, '拉杆箱'); # 报错，列的个数 和 值的个数 不匹配

insert into category values(3, '汽车', '小米'),(4, '平板', '华为');

# 4. 查看表数据
select * from category;

#------------------------案例2 DML语句(数据操作语言) 操作 表数据(data) 改----------------------

# 1. 查看表数据
select * from category;

# 2. 修改 cname='空调',info='格力', cid=3
update category set cname='空调', info="格力" where cid=3;

#------------------------案例3 DML语句(数据操作语言) 操作 表数据(data) 删----------------------
delete from category where cid=4;
delete from category;  # 一次性删除所有，不会重置主键id

# 演示 truncate table
truncate table category;


#------------------------案例4 扩展_如何备份数据表           ----------------------
# 查看数据表
show tables;
# 1. 原表
select * from category;

# 2. 场景1：备份表不存在
# 格式: create table 备份表名 select * from 原表明 where ...
create table category_tmp select * from category;

# 3. 场景2:备份表存在
# 格式：insert into 备份表名 select * from 原表明 where ...
insert into category_tmp select * from category where cid<=3;

# 4. 查看备份表数据
SELECT * from category_tmp;

# 5. 清空备份表
delete from category_tmp;