"""
字符串：是字符的容器，可以存放任意数量的字符。
特点：不可变性（无法修改）、有序性、可迭代性
字符串中的每个字符元素都有其对应的下标(索引)，通过元素对应的索引，可以获取到对应的元素
字符长操作常用方法：
find() 在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1 s.finde("Python")
count() 统计子串在字符串中出现的次数, s.count("H")
upper() 将字符串中的所有字母转为大写 s.upper()
lower() 将字符串中的所有字母转为小写 s.lower()
split() 将字符串按指定分隔符分割成列表 s.split(" ")
strip() 去除字符创两端的空白字符创或者指定字符 s.strip() 、s.strip("*")
replace() 将字符串中指定的子串替换为新的子串 s.replace("H", "C")
startswith() 检查字符串是否以指定子串开头，返回布尔值 s.startswith("Hello")
endswith() 检查字符串是否以指定子串结尾，返回布尔值 s.endswith("Python")
"""


# s = "Hello-Python"
# 有序性
# print(s[4]) # 正向索引
# print(s[-8]) # 反向索引
# 不可变性
# s[4] = "X" # 不可修改 报错：'str' object does not support item assignment
# print(s)
# 可迭代性
# for c in s:
#     print(c)

# 切片
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])

# print("--------------------")
# print(s[6:12:1])
# print(s[6::1])
# print(s[6:])
#
# print("------------------------------------")
# 步长 ---> 正数：从前往后截取；负数：从后往前截取
# print(s[0:5:2])
# print(s[-1:-7:-1])
print('-----------------------------------')
"""
s = "  Hello-Python-Hello-World   "
# find()
index = s.find("-")
print("find-:", index)
# count()
c = s.count("o")
print("count:", c)
# upper()
su = s.upper()
print("upper:", su)
# lower()
sl = s.lower()
print("lower:", sl)
# split()
slit = s.split("-")
print("strip:", slit)
# strip()
ss = s.strip()
print("strip:", ss)
# replace()
sr = s.replace("-", "_")
print("replace:", sr)
# startswith
print("startswith:", ss.startswith("Hello"))
print("endswith:", ss.endswith("Python"))
"""

"""
# 案例 邮箱格式校验（包含一个@,至少有一个.）
email = input('请输入邮箱：')
# 方式1
# if email.count("@") == 1 and email.count(".") >=1:
# 方式2
if email.count("@") == 1 and "." in email:
    print("邮箱格式正确~！")
else:
    print("邮箱格式错误！")
print("---------------------------------")
"""
"""
完成以下需求：
1. 输入一个字符串，判断改字符串是否是回文（两边对称）
黄山落叶松叶落山黄
上海自来水来自海上
2. 将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来
"""
# 判断是否是回文
