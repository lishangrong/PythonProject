"""
函数：组织好的、可以重复使用的、用来实现特定功能的代码片段。
    通过锁紧来描述归属关系
函数定义与调用:
# 定义函数
def 函数名(参数列表):
    函数体
    ....
    return 返回值
# 调用函数（先定义后调用）
函数名(参数)
"""
import math


# # 定义函数
# def out_line():
#     print("________________")
#     print('定义函数')
#
# # 调用函数
# out_line()

# 函数1：计算圆的面积 -- 半径
# def circle_area(radius):
#     area = 3.14 * radius ** 2
#     return area
#
# area = circle_area(10)
# print(area)

# 函数2：长方形的面积 --- 长、宽
# def rectangle_area(l, w):
#     area = l * w
#     return area
#
# print(rectangle_area(10, 5))

# 函数3：计算圆的面积与周长 --->如果返回值有多个，多个返回值之间逗号分割 ----> 多个返回值会封装到元祖之中
# def circle_area_len(r):
#     return round(3.14 * r**2, 1), round(3.14 * r *2, 1)
#
# area, len = circle_area_len(10)
# print(area, len)

"""
函数的说明文档(Docstring) 是写在函数开头，用三个引号包裹字符串，用于解释函数的功能、参数、返回值等信息，
方便调用者清楚函数的具体作用及细节。
"""
# 定义一个函数，根据半径，计算圆的周长、面积
def circle_area_len(r):
    """
    该函数用于根据圆的半径，计算圆的面积和圆的周长
    :param r: 圆的半径
    :return: 圆的面积，圆的周长
    """
    return round(3.14*r**2, 1), round(3.14*r*2)

# 函数嵌套调用：指的是在一个函数中，有调用了另外一个函数，
# 函数调用遵循栈结构，最后被调用的函数最先返回LIFO（Last In First Out， 先进后出）

"""
def function_a():
    print("a.....before")
    function_b()
    print("a.....after")

def function_b():
    print("b.....before")
    function_c()
    print("b.....after")

def function_c():
    print("c.....")

function_a()

"""
"""
案例：
1.定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）
2. 定义一个函数：计算传入的字符串种元音字母的个数(元音字母为 aeiouAEIOU)
3. 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分，最低分，平均分(保留一位小数)并返回
"""

"""
def triangle_area(d, h):
    return d * h / 2

print(f"底长为30， 高度为20的三角形面积: {triangle_area(30, 20)}")

def vowel_count(s):
    num = 0
    for c in s:
        if c in "aeiouAEIOU":
            num += 1
    return num
print(f"元音字符的个数:{vowel_count("Hello Python Hello World OK")}")

def calc_score(score_list):
    max_score = max(score_list)
    min_score = min(score_list)
    average_score = round(sum(score_list) / len(score_list), 1)
    return max_score, min_score, average_score

max_s, min_s, average_s = calc_score([66, 90, 89, 99, 78, 95, 93, 95])
print(f"班级最高分:{max_s}, 最低分：{min_s}, 平均分：{average_s}")
"""
"""
需求：
1. 定义一个函数，根据传入的分数，计算对应的分数登记并返回。
    分数 >=90:A, 分数 >=75:B, 分数>=60:C, 分数<60:D
2. 定义一个函数，用于判断一个字符串是否是回文，返回bool值
    把字符串反转，如果和原字符串相同，就是回文串
3. 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒
4. 定义一个函数：根据传入的三角形三个边的边长，判断三角形的类型(等边，等腰，普通，或者不能构成三角形)
"""

def calc_score_level(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

def is_palindrome(s):
    return s == s.reverse()

def format_time(time):
    h =  int(time / 3600)
    m = int(time % 3600 / 60)
    s = int(time % 3600 % 60)
    return f"{h}小时{m}:、分钟{s}秒"
print(format_time(76000))