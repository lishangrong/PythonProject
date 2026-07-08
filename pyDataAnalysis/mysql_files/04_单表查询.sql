/*
单表查询语句：
select
    [distinct] 列名 as 别名,列名2...
from
    数据表名
where
    组前筛选
group by
    分组字段
having
    组后筛选
order by
    排序字段 [asc | desc]
limit
    起始索引,数据条数

 */

#-------------------------------------准备动作: 准备数据 --------------------------------------------------------------

#准备数据
use day02;
# 1. 创建商品表
create table product
(
    pid int primary key auto_increment,
    pname varchar(20),
    price double,
    category_id varchar(32)
);

# 2.添加表数据
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'联想',5000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'海尔',3000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'雷神',5000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'杰克琼斯',800,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'真维斯',200, null);
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'花花公子',440,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'劲霸',2000,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'香奈儿',800,'c003');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'相宜本草',200, null);
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'面霸',5,'c003');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'好想你枣',56,'c004');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'香飘飘奶茶',1,'c005');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'海澜之家',1,'c002');

#-------------------------------------案例1: 简单查询 --------------------------------------------------------------
# 查询表中的所有数据
select pid, pname, price, category_id from product;
select * from product;

# 别名
select pname as 商品名, price as 价格 from product as p;
select pname 商品名, price 价格 from product p;

# 修改某列值
select pname, price + 10 as price from product;
select pname, price + 10  price from product;


#-------------------------------------案例2: 条件查询 --------------------------------------------------------------

/*
select * from 数据表名 where 条件;
条件可以是：
    1. 比较运算符: >, >=, <, <=, != <>, =
    2.逻辑运算符: and, or not
    3. like 模糊查询
        _ 代表任意的1个字符
        % 代表任意的多个字符，至少0个，至多无所谓。
    4. 范围查询
        between 值1 and 值2  包左包右，适用于 连续值的判断
        in(值1, 值2, 值3) 满足任意切割值即可，适用于 非连续的值的判断
    5.空值判断：is null 或者 is not null

*/

# 1. 查询所有数据
select * from product;

# 2. 查找单价在500元以上的商品信息
select * from product where price > 500;
# 3. 查找不是 c001类别的商品信息
select * from product where category_id != 'c001';
select * from product where category_id <> 'c001';

# 4. 查找单价在 800 ~ 3000元的商品信息，只要商品名，价格
select pname, price from product where price BETWEEN 800 and 3000;
select pname, price from product where price >= 800 and price <= 3000;

# 5. 查找 第二个字是 霸的 商品信息，商品名共计2个字
select * from product where pname like '_霸';
# 6. 商品名包含 斯
select * from product where pname like '%斯%';

# 7. 查询单价 是， 200， 800 或者 5000的商品信息
select * from product where price in (200, 800, 5000);
select * from product where price=200 or price=800 or price=5000;

# 8.  查询单价不是， 200， 800 或者 5000的商品信息
select * from product where price not in (200, 800, 5000);
select * from product where price!=200 and price!=800 and price!=5000;


# 9. 查询 没有分类id 的商品信息
select * from product WHERE category_id is null;



#-------------------------------------案例3: 排序查询 --------------------------------------------------------------

/*
格式：
    select * from 数据表名 order by 排序的列1 [asc/desc], 排序的列2 [asc/desc]...;
细节：
    1. 如果不写asc|desc， 默认是 asc(升序),它 可以省略不写
    2. 武林SQL简单还是复杂，order by 都要写到语句的最后， 严格意义上讲，它应该写到limit 的前边。
*/
# 1. 查看表数据
select * from product;

# 2. 按照价格升序排列
select * from product ORDER BY price;
select * from product ORDER BY price asc;  # ascending 升序，默认的，可以不写
# 按照价格降序
select * from product ORDER BY price desc;  # descending 降序

# 按照价格降序排列，如果价格一致，按照分类id降序排列
select * from  product order by price desc, category_id desc;

#-------------------------------------案例4: 聚合查询 --------------------------------------------------------------
/*
聚合函数：
    概述：它是以列为单位进行操作的，例如，计算某列值的个数，最小值，最大值，求和，平均值等。
    涉及到的函数：
    count() 总数
    sum()   求和
    max()   最大值
    min()   最小值
    avg()   平均值
*/

# 1. 查看表数据
select * from product;

# 统计数据条数
/*
    面试题:
        count(*), count(1), count(列) 的区别 是什么？
    答案：
        1. 是否统计null值.
            count(列)不统计, count(*),count(1) 统计
        2. 效率问题，效率从高到低分别是：
            count(主键列) > count(1) > count(列) > count(*)
            主键列的底层是：主键索引。
*/

select count(*) from product;               # 13
select count(1) from product;               # 13
select count(pid) from product;             # 13
select count(category_id) from product;     # 11， count() 统计列的时候，会忽略该列的 null 值

# 3. 查看商品价格的 求和， 最大值， 最小值， 平均值
select
    sum(price) as s_price,
    max(price) as max_price,
    min(price) as min_price,
    round(avg(price), 2) as avg_price  # 四舍五入，保留2位小数
from product;


#-------------------------------------案例5: 分组查询 --------------------------------------------------------------
/*
格式：
    select
        *
    from
        数据表名
    where
        组前筛选
    group by
        分组的列1， 列2 ...
    having
        组后筛选;
细节：
    1.根据谁分组，就根据谁查询，即：分组查询的查询列，只能出现 分组字段 和聚合函数。
    2. 组前筛选用where，组后筛选用having。
    3. 面试题： where 和 having 的区别是什么？
        1）作用不同。
            where用于 组前筛选，having用于 组后筛选
        2）后边是否可以跟聚合函数。
            where 后边不可以， having后边可以。

*/

# 1. 查看表数据
select * from product;
# 2. 需求：统计每个类别的商品数量
SELECT category_id, COUNT(*) AS total_cnt
FROM product
GROUP BY category_id;

# 3 需求： 统计每个类别的商品数量，只显示 商品树龄 在 2 以上的分类
SELECT category_id, COUNT(*) AS total_cnt
FROM product
GROUP BY category_id
having total_cnt >=2;


#-------------------------------------案例6: 去重查询 --------------------------------------------------------------
/*
去重解释：
    概述：把相同的数据，给移除掉，只保留一份
    方式：
        思路1：distinct 关键字实现
        思路2: 分组实现.
*/
# 1. 查看表数据
select * from product;

# 2。 查看(去重后)所有分类
select distinct category_id from product;

# 3. 按照分类id，价格进行去重。  是把category_id 和 price 当做整体 去重的
select distinct category_id, price from product;

# 4. 去重思路2，分组去重
select category_id from product group by category_id;
select category_id,price from product group by category_id, price;

#-------------------------------------案例7: 分页查询 --------------------------------------------------------------

/*
分页查询的好处：
    1. 提高用户体验
    2. 降低服务器端压力
    3. 降低浏览器端压力

语法：
    select * from 数据表名 limit 起始索引, 数据条数
细节：
    1. 在sql中，每条数据都是有索引的，且索引从0 开始
    2. 关于分页，有4个参数的计算规则，需要大家掌握：
        总页数： (数据总条数 + 每页的数据条数 - 1) // 每页的数据条数
        每页的数据条数：产品经理/项目经理 决定
        每页的起始索引：(当前页数 -1) * 每页的数据条数
        数据总条数：count(主键列)

*/

# 1. 查看表数据
select * from product;

# 2. 场景1 3条/页
select * from product limit 0, 3;
select * from product limit 3;  # 起始索引是0的情况下，可以省略不写
select * from product limit 3, 3;
select * from product limit 6, 3;
select * from product limit 9, 3;
select * from product limit 12, 3;

# 3. 场景2 5条/ 页
select * from product limit 0, 5;
select * from product limit 5, 5;
select * from product limit 10, 5;

# 4. 场景3 4条/页,求第二页
select * from product limit 4, 4;