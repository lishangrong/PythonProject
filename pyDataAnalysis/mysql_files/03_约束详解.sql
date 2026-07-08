#------------------------案例1 演示主键约束           ----------------------

# 1. 建库，切库，查表
drop database day02;
create database day02;
use day02;
show tables;

# 场景1：建表时添加主键约束
# 0. 删表
drop table student;
# 1. 创建学生表， 字段 id， name， age

create table student(
    sid int primary key,
    name varchar(10),
    age int
);

# 2. 查看表结构
desc student;
# 3. 给student 表添加数据
insert into student values(1, '张三', 18);
insert into student values(1, '张三', 18); # 报错 id重复
insert into student values(null, '张三', 18); # 报错 id不能为空（细节：如果结合自增，是可以传入null的）

# 4 查询表结构
select * from student;

# 5. 删除主键约束
alter table student drop primary key;

# 6.建表后，添加主键约束，结合自增
alter table student add primary key(sid);
alter table student modify sid int auto_increment; # 增加 自增功能

# 7. 再次尝试往表中添加数据
insert into student values(2, '李四', 20);
insert into student values(2, '李四', 20); # 报错，主键冲突
insert into student values(null, '李四', 20); # 可以，因为有自增，主键会自动 + 1


# 总结，实际开发中，掌握如下代码即可
# 1. 建表
create table student(
    cid int primary key auto_increment,
    name varchar(10),
    age int
);

# 插入数据
insert into student values(null, '王五', 22);

# 查看数据
select * from student;


# 回顾 delete from(不会重置主键id)，truncate table(重置主键id)
delete from student; # 不会重置主键id
truncate student; # 重置主键id,相当于把表摧毁了，然后创建一张和原表一模一样的新表

#------------------------案例2 演示主键约束           ----------------------
# 1. 查表
show tables;

# 2.建表， 员工表(employee),字段(员工id，员工姓名，员工手机号，员工性别，员工住址)
create table employee(
    eid int primary key auto_increment,
    name varchar(10) not null,
    mobile varchar(11) unique,
    address varchar(10) default '北京'
);
# 3. 查看表结构
desc employee;

# 4. 插入数据
insert into employee values(null, '乔峰', '111', '南院');
insert into employee values(null, null, '222', '缥缈峰');  # 报错：姓名不能为空
insert into employee values(null, '乔峰', '111', '缥缈峰');  # 报错：手机号必须唯一
insert into employee values(null, '乔峰', '222', '缥缈峰');  # 正常

insert into employee values(null, '段誉', '333');  # 报错 值得个数和列的个数一致
insert into employee(eid, name, mobile) values(null, '段誉', '333');  # 正常

# 5. 查询表数据
select * from employee;