"""
集合（set）：无序的、不可重复的，可修改的数据容器
注意：空集合的定义不可以使用{}, {} 表示的是空字典；由于集合是无序的，因此是不支持下标索引访问的。
集合的常见方法：
add(...) 添加元素到集合中 s1.add('t')
remove(...) 移除集合中指定元素（z指定元素不存在报错） s1.remove('t')
pop() 随机删除集合中的元素并返回 w = s1.pop()
clear() 清空集合  s1.clear()
difference() 求取两个集合的差集（包含在第一个结合但不包含在第二个集合的元素）s1.difference(s2)
union() 求取两个集合的并集  s1.union(s2)
intersection() 求取两个集合的交集 s1.intersection(s2)
交集符号 &: s1 & s2
差集符号 -： s1 - s2
并集符号 |: s1 | s2
集合推导式 --->快速构建集合， 语法： {要往集合中添加的元素 for s in set1 if 条件}
"""
# 定义
# s1 = {"A", "B", "C","B", 5, 0, 5}
# print(s1)
# print(type(s1))
#
# # 定义空集合
# s2 = set()
# print(s2)

# 常见方法
s1 = {100, 200, 300, 400, 500}
s1.add(600)
print(s1)
s1.remove(300)
print(s1)
e = s1.pop()
print(e)
print(s1)
s1.clear()
print(s1)

s2 = {"A", "B", "C", "D", "E"}
s3 = {"C", "D", "E","F", "G"}
print(s2.difference(s3))
print(s2.union(s3))
print(s2.intersection(s3))

print("-------------------------------------------------")

"""
需求：根据提供的班级学生的选课情况，完成以下需求：
1.找出同时选修了法语和艺术的学生
2.找出同时选修了所有四门课程的学生
3.找出选修了足球，但是没有选修篮球的学生
4.统计每一个学生选修的课程数量
"""
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "段天", "天运子", "韩丽", "李飞宇", "武丑", "紫菱"}
# 选修篮球学生名单
basketball_set = {"张贴", "墨居仁", "王林", "姜老刀", "曾牛", "王婵", "韩丽", "天运子", "李华元", "李飞宇", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎跑", "姜老刀", "天运子", "红蝶", "李飞宇", "韩丽", "曾牛"}
# 选修艺术学生名单
art_set = {"段天", "天运子", "韩丽", "虎跑", "姜老刀", "紫菱"}

# 1.找出同时选修了法语和艺术的学生
print(f"同时选修了法语和艺术的学生：{french_set.intersection(art_set)}")
# &---->交集
print(f"同时选修了法语和艺术的学生：{french_set & art_set}")
#2.找出同时选修了所有四门课程的学生
print(f"选修4门课的学生：{football_set.intersection(basketball_set).intersection(french_set).intersection(art_set)}")
print(f"选修4门课的学生：{football_set & basketball_set & french_set & art_set}")

# 3.找出选修了足球，但是没有选修篮球的学生
print(f"选修足球，没有选修篮球的学生：{football_set.difference(basketball_set)}")
# -：差集
print(f"选修足球，没有选修篮球的学生：{football_set - basketball_set}")
#  集合推导式 --->快速构建集合， 语法： {要往集合中添加的元素 for s in set if 条件}
fb_set = {s for s in football_set if s not in basketball_set}
print(f"选修足球，没有选修篮球的学生：{fb_set}")
# 4.统计每一个学生选修的课程数量
# 4.1 获取所有学生：
# students_set = football_set.union(art_set).union(basketball_set).union(french_set)
# |： 并集
students_set = football_set | basketball_set | french_set | art_set
# 4.2 获取每个学生选修的课程列表
all_list = [*football_set, *basketball_set, *french_set, *art_set]
print(all_list)

for student in students_set:
    print(f"学生 {student} 选修 {all_list.count(student)} 门课")
