"""
元祖（tuple）：是不可变的序列，一旦定义完成，不可修改
特点： 可以存储不同类型的元素，元素可以重复、有序、不可修改(支持索引访问，切片)

元祖方法：
count() 统计某个元素在元祖中出现的次数
index() 查找某个元素在元祖中的索引位置（第一次出现的位置）
元祖-组包与解包
组包（packing）：将多个值合并到一个容器(元祖、列表)中
解包（unpacking）：将容器（元祖、列表）解成独立的元素，分别赋值给多个变量。
"""
"""
t1 = (2, "hello", 89, 96, 50, 76, 80, 20, 50)
print(t1)
print(type(t1))
# 索引访问
print(t1[0])
print(t1[-1])
# 不支持修改
# t1[1] = 10

# 切片
print(t1[0:5:1])
# count()
print(t1.count(50))
# index()
print(t1.index(96))
print("-----------------------------------")
# 注意点：
t2 = () # 空白元祖
# 定义单元素的元祖，单元素后需要加, 与运算符() 区分开
t3 = (100,)
t4 = (200)
print(type(t3))
print(type(t4))

print("----------------------------------------")

# 元祖定义
t5 = (5, 7, 9, 1) # 推荐
t6 = 5, 7, 9, 11
print(t6)
# 基础解包
a, b, c, d = t5

print(a, b, c, d)

# (*)扩展解包
x, *y, z = t5  # x=5, y = [7, 9], z =1
print(x, y, z)
s, *o = t5 # s= 5, o = [7, 9,1]
print(s, o)
*o, e = t5  # o= [5, 7,9] e = 1
print(o, e)

print("---------------------------------------")
# 案例： 现有2个变量，分别为a = 10, b= 20, 现需要将这两个变量值交换，然后输出到控制台
a = 10
b = 20
# 1.组包
# tt = a, b
# # 2.解包
# b,a = tt
# 步骤1和步骤2 合并
a,b = b, a
print(a, b)

# 案例2， 现有三个变量， a = 100, b= 200, c = 300 ，现需要将这三个变量进行交换，将a, b, c 的值分别赋值给, c, a,b
aa = 100
bb = 200
cc = 300
cc, aa, bb = aa, bb, cc
print(aa, bb, cc)
"""

"""
需求：根据提供的学生成绩，完成如下需求：
1.计算每个学生的总分，平均分，然后一并输出出来
2. 统计各科成绩的最低分、最高分、平均分、并输出
3. 查找成绩优秀(平均分大于90)的学生，并输出
学号： 姓名： 语文： 数学： 英语
S001 王林    85    92   78
S002 李牧晚  92    88    95
S003 十三   78    85    82
S004 管牛   88    79    91
S005 周毅   95    96    89
S006 王卓   76    82    77
S007 红蝶   89    91    94
S008 徐立国 75    69     82
S009 许木   86    89    98
S010 段天   66    59    72

"""
print('-----------------------------------------------')
students = (
("S001", "王林", 85, 92, 78),
("S002", "李牧晚", 92, 88, 95),
("S003", "十三", 78, 85, 82),
("S004", "管牛", 88, 79, 91),
("S005", "周毅", 95, 96, 89),
("S006","王卓", 76, 82, 77),
("S007", "红蝶", 89, 91, 94),
("S008", "徐立国", 75, 69, 82),
("S009", "许木", 86, 89, 98),
("S010", "段天", 66, 59, 72)
)
# 1. 计算每个学生的总分，各科平均分，然后一并数出来 ---->{avg:.1f} ---> 保留1位小数
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
# 方式1：
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t { avg:.1f}")
# 方式2 元祖解包
for id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t { avg:.1f}")

print()
# 2.统计各科成绩的最低分、最高分、平均分、并输出
# 2.1 获取各科的成绩
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
# 2.2统计各科成绩的最低分，最高分，平均分
print(f"语文最低分:{min(chinese_scores)}, 最高分：{max(chinese_scores)}, 平均分: {sum(chinese_scores) / len(chinese_scores)}")
print(f"数学最低分:{min(math_scores)}, 最高分：{max(math_scores)}, 平均分: {sum(math_scores) / len(math_scores)}")
print(f"英语最低分:{min(english_scores)}, 最高分：{max(english_scores)}, 平均分: {sum(english_scores) / len(english_scores)}")
print()

# 3. 查找成绩优秀(平均分大于90)的学生，并输出
print("优秀学生名（平均分 > 90）单如下:")
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     if avg > 90:
#         print(f"学号：{s[0]}，姓名：{s[1]} 平均分： {avg: .1f}")

# 解包方式
for id, name, chinese, math, english  in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90 :
        print(f"学号：{id}，姓名：{name} 平均分： {avg: .1f}")