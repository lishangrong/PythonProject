#-------------------------------------案例1: 多表建表之 一对多 --------------------------------------------------------------
# 需求：新建部门表(dept,department) 和员工表(emp)，他们之间是一对多的关系，请用外键约束，完成限定

# 1. 切库，查表
use day02;
show tables;

# 2. 创建主表 ---部门表
create table dept(
    id int primary key auto_increment,
    name varchar(10)
);

# 3. 创建 外表 ---员工表
create table emp(
    id int primary key auto_increment, # 员工id
    name varchar(10),                  # 员工姓名
    salary double,                     # 员工工资
    dept_id int                        # 员工所属部门id
    # 设置外键约束的方式1：建表时添加 外键约束，注意：写到外表中.
    ,constraint fk_dept_emp foreign key(dept_id) references dept(id)
);

# 4. 给部门添加数据
insert into dept values(null, '人事部'),(null,'财务部'),(null, '研发部'),(null,'行政部');

# 5. 给员工添加数据
insert into emp values(null, '胡歌', 33333, 1);
insert into emp values(null, '刘亦菲', 22222, 2);
insert into emp values(null, '迪丽热巴', 11111, 2);
insert into emp values(null, '水冷哥', 12111, 3);
insert into emp values(null, '坤坤', 12111, 10); # 报错，外表的外键列不能出现主表的主键列没有的数据。

# 6. 查看表数据
select * from dept;
SELECT * from emp;

# 7. 删除外键约束
# 格式： alter table 外表名 drop foreign key 外键约束名
alter table emp drop foreign key fk_dept_emp;

# 8. 建表后，添加外键约束，前提：表数据之间必须是合法的。
# 格式： alter table 数据表名 add [constraint 外键约束名] foreign key(外键列名) references 主表名(主键列名)
alter table emp add foreign key(dept_id) references dept(id);

#-------------------------------------案例2: 多表查询，准备数据 --------------------------------------------------------------
# 1. 创建hero表
create table hero(
    hid int primary key auto_increment,
    hname varchar(255),
    kongfu_id int
);
# 2. 创建kongfu表
create table kongfu(
    kid int primary key auto_increment,
    kname varchar(255)
);

# 3. 添加数据
insert into hero values(1, '鸠摩智', 9),(3, '乔峰', 1),(4, '虚竹', 4),(5, '段誉', 12);
insert into kongfu values(1,'降龙十八掌'),(2, '乾坤大挪移'),(3,'猴子偷桃'),(4, '天山折梅手');

# 4. 查看表数据
select * from hero;
select * from kongfu;

#-------------------------------------案例3: 多表查询，交叉连接 --------------------------------------------------------------
# 格式1：select * from 表名1，表名2；
# 格式2：select * from 表名1 join 表名2；
# 查询结果 = 两张表的笛卡尔积，即：表A的总条数 * 表B的总条数， 会差生大量的脏数据，实际开发一般不用。
select * from hero, kongfu;
select * from hero join kongfu;

#-------------------------------------案例4: 多表查询，内连接(inner join) --------------------------------------------------------------
# 隐式内连接
# 格式1：select * from 表名1, 表名2 where 关联条件；
select  * from hero as h, kongfu as kf where h.kongfu_id = kf.kid;  # 标准写法
select * from hero, kongfu where kongfu_id = kid;

# 显示内连接（推荐使用，效率高）
# 格式2：select * from 表名1 inner join 表名2 on 关联条件；  # 细节：inner可以省略
select * from hero as h inner join kongfu as kf on h.kongfu_id = kf.kid;
select * from hero as h join kongfu as kf on h.kongfu_id = kf.kid;

#-------------------------------------案例5: 多表查询，外连接(outer join) --------------------------------------------------------------
# 场景1：左外连接，查询结果 = 左表的全集 + 交集
# 格式： select * from 表1 left outer join 表2 on 关联条件  # outer 可以省略不写
select * from hero h left outer join kongfu kf on h.kongfu_id = kf.kid;
select * from hero h left join kongfu kf on h.kongfu_id = kf.kid;  # 效果同上，outer可以省略不写

# 场景2，右外连接，查询结果 = 右表的全集 + 交集
# 格式: select * from 表1 right outer join 表2 on 关联条件 # outer 可省略不写
select * from hero h right outer join kongfu kf on h.kongfu_id = kf.kid;
select * from hero h right join kongfu kf on h.kongfu_id = kf.kid;


# 场景3：满外连接(全连接)， 查询结果 = 左外连接 + 右外连接的结果
# 格式： select * from 表1 full outer join 表2 on 关联条件  # outer 可以省略不写， 格式如此，但是MySql不支持 full outer join 写法
# select * from hero h full outer join kongfu kf on h.kongfu_id = kf.kid;

# 可以使用 union 关键字 把 左外连接 和 右外连接的结果 合并到一起，形成满外连接的效果
select * from hero h left join kongfu kf on h.kongfu_id = kf.kid  # 左外连接
# union distinct   # 合并，并去重。细节：distinct 可以不写
# union
union all  # 合并，不去重
select * from hero h right join kongfu kf on h.kongfu_id = kf.kid;  # 右外连接



#-------------------------------------案例5: 多表查询，子查询 --------------------------------------------------------------
/*
概述：
    一个SQL语句的查询条件，需要依赖另1个SQL语句的查询结果，这种写法就叫：子查询.
    外表的查询叫：父查询(只查询)，里边的查询叫：子查询.
写法：
    select * from 表名 where 字段 = (select 字段 from 表名 where ...)
*/

# 需求：查询价格最高的商品信息，只要商品名，价格，分类id即可.
select pname, price, category_id from product where price = (select max(price) from product);

# 实际开发写法， 连接查询
SELECT *
FROM product p
JOIN (SELECT MAX(price) price FROM product) t1 ON p.price = t1.price;

# case when语句
# 需求：c001 ->电脑， c002 -> 服装, c003 ->化妆品 c004 ->零食， c005 -> 饮料， null -> 未知类别
/*
格式1：通用写法
    case
        when 条件1 then 结果1
        when 条件2 then 结果2
        ...
        else 结果n
    end [as 别名]

格式2： 针对于格式1的语法糖，要满足两点：-->1.都是操作同1个字段，2. 都是等于的判断
    case 字段名
        when 值1 then 结果1
        when 值2 then 结果2
        ...
        else 结果n
    end [as 别名]

*/

 select
     *,
     case
        when category_id = 'c001' then '电脑'
        when category_id = 'c002' then '服装'
        when category_id = 'c003' then '化妆品'
        when category_id = 'c004' then '零食'
        when category_id = 'c005' then '饮料'
        else '未知类别'
    end as category_name
 from
     product;

 # 上述格式可以简化为：
 select
     *,
     case category_id
        when 'c001' then '电脑'
        when 'c002' then '服装'
        when 'c003' then '化妆品'
        when 'c004' then '零食'
        when 'c005' then '饮料'
        else '未知类别'
    end as category_name
 from
     product;
