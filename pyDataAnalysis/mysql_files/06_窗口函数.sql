#-------------------------------------案例1: 窗口函数(MySQL8.x 新特性) --------------------------------------------------------------

/*
窗口函数解释：
    概述：它是MySQL8.x的新特性，主要用于 给表新增 1列，至于新增的内容是什么，取决于你用什么 窗口函数。
    格式：窗口函数 over([partition by 分组字段 order by 排序字段 asc|desc])
    常用窗口函数：
        row_number(),rank(),dense_rank() 这3个函数都是用于返回结果集的分组内每行的排名。
        row_number():  做行号标记的，不管排名是否有相同，都按照顺序1，2，3...n
        rank()：       做稀疏排名的，排名相同的名次一样，同一排名有几个，后面排名就会跳过几次
        dense_rank()： 做密集排名的， 排名相同的名次一样，且后面名次不跳跃。

    举例说明：
        假设数据集是 100，90，90，60，则三个函数的排名结果分别是：
            row_number(): 1, 2, 3, 4
            rank():       1, 2, 2, 4
            dense_rank(): 1, 2, 2, 3

    细节：
        1. 窗口函数 = 给表新增1列，至于新增的内容是什么，取决于和什么函数一起用。
        2. 如果不写 partition by， 则统计的是全表数据，如果写了，则统计的是组内的数据。
        3. 如果不写 order by，则统计的是组内所有的数据，如果写了，则统计的是组内从第一行，截止到当前行的数据。
        4. 如果你感兴趣，你可以尝试玩以下其他的窗口函数结合 over() 一起用。
            例如：count(),max(),min(),sum(),avg(),ntile(n),lag(),lead(), first_value(), last_value()...
    总结：关于窗口函数，希望大家掌握两点：
        1.分组排名
        2. 分组排名求TopN

*/

# 准备数据 --> 建库，切库，查表
drop database day03;
create database day03;
use day03;
show tables;

# 准备数据 --> 建表，添加数据

# 2. 创建数据表.
create table employee (
    id int,                 # 员工id
    ename varchar(20),      # 员工名
    deptid int,             # 部门id
    salary decimal(10,2)    # 工资
);
# 3. 添加表数据.
insert into employee values(1,'刘备',10,5500.00);
insert into employee values(2,'赵云',10,4500.00);
insert into employee values(2,'张飞',10,3500.00);
insert into employee values(2,'关羽',10,4500.00);

insert into employee values(3,'曹操',20,1900.00);
insert into employee values(4,'许褚',20,4800.00);
insert into employee values(5,'张辽',20,6500.00);
insert into employee values(6,'徐晃',20,14500.00);

insert into employee values(7,'孙权',30,44500.00);
insert into employee values(8,'周瑜',30,6500.00);
insert into employee values(9,'陆逊',30,7500.00);

# 查看数据
select * from employee;

# 案例1：分组排名，需求：按照部门id分组，按照工资降序排名
# 场景1：如何给表新增1列
select *, '航哥' from employee;
select *, 10 / 3  from employee;
select *, deptid + 100  from employee;

# 场景2： 引入窗口函数。
select
    *,
#     row_number() over(partition by deptid order by salary desc) as rn
#     sum(salary) over() as total_sum                                          # 没写 partition by 统计全表
#     sum(salary) over(partition by deptid) as total_sum                       # 写了 partition by， 统计全组
    sum(salary) over(partition by deptid order by salary desc) as total_sum    # 写了 order by， 统计全组
from
    employee;

# 场景3：分组排名
SELECT
    *,
    row_number() OVER (PARTITION BY deptid ORDER BY salary DESC ) as rn,
    rank() OVER (PARTITION BY deptid ORDER BY salary DESC ) as rk,
    dense_rank() OVER (PARTITION BY deptid ORDER BY salary DESC ) dr
FROM
    employee;

# 场景4：分组排名求TopN， 需求：找出每组工资最高的2人的信息(考虑并列)
# 如下代码，思路没有问题，但是语法格式有问题，因为where后边的字段必须是表中已有的

SELECT
    *,
    rank() OVER (PARTITION BY deptid ORDER BY salary DESC ) as rk
FROM
    employee
WHERE
    rk <=2;

# 解决方案如下:
# 思路1：使用子查询解决
SELECT  * from (
    SELECT
        *,
        rank() OVER (PARTITION BY deptid ORDER BY salary DESC ) as rk
    FROM employee
    ) t1
where rk <=2;

# 思路2：用CTE 公共表表达式, 可以把常用的数据集封装成新表，方便操作
/*
    with 表名1 as (select...),
         表名2 as (select...),
         表名3 as (select...)
    select * from t1 ...; # 这里正常写SQL，使用上述的 表名即可

*/
with t1 as (SELECT  *,  rank() OVER (PARTITION BY deptid ORDER BY salary DESC ) as rk FROM employee)
SELECT  * from t1 WHERE  t1.rk <=2;

# 扩展： 1个休表示 CTE 表达式的强大之处
with t1 as (select * from employee),
     t2 as (select * from employee where deptid=10),
     t3 as (select * from employee where deptid=20),
     t4 as (select * from employee where deptid=30),
     t5 as (select *, sum(salary) over() as total_salary from employee)
select * from t5;


#-------------------------------------案例2: 自关联(自连接)查询--------------------------------------------------------------
/*
解释:
    表自己和自己 做 关联查询 --> 自关联，自连接查询。
应用场景：
    省市区(行政区域表) 信息查询。
如果不考虑 自连接查询，让你设计 行政区域表，要求有行政区域的id和行政区域名，例如：410000 --> 河南省，你如何设计？
    大概率你会设计成3张表，分别对应 省，市，区 的信息，但这样做太繁琐了，我们可以考虑把省市区合并到一张表，然后做 自关联查询即可。
    合并之后，表中有三个字段，分别是：
    区域自身id       区域名    区域的父级id
    410000          河南省      0

    410100          郑州市      410000
    410200          开封市      410000

    410101          三七区      410100
    410102          金水区      410100
    .......

 */

# 查表
show tables;
# 查看表数据
select * from areas;

# 查看河南省的数据
select * from areas where title = '河南省';
# 查看河南省所有的市
SELECT * from areas WHERE  pid = '410000';
# 查看新乡市所有的县区
select * from areas where pid = '410700';

# 省：province  市：city  县区：county

# 查看所有省，所有市，所有县区的信息
select
    province.id, province.title,  # 省级 id， 名字
    city.id, city.title,          # 市级 id， 名称
    county.id, county.title       # 县区级 id 名称
from
    areas as county  # 县区表
join
        areas as city on county.pid = city.id   # 市级表
join
        areas as province on city.pid = province.id  # 省级表
;


# 精准查找信息
select
    province.id, province.title,  # 省级 id， 名字
    city.id, city.title,          # 市级 id， 名称
    county.id, county.title       # 县区级 id 名称
from
    areas as county  # 县区表
join
        areas as city on county.pid = city.id   # 市级表
join
        areas as province on city.pid = province.id  # 省级表
where
    county.id = '371327'
;