# # 字面量的写法
# print(100) #整数（int）
# print(3.14) #浮点数/小数（float）
# print(True) #布尔（bool）
# print(False) #布尔（bool）
# print('Hello Python') #字符串（str）
# print('----------------') #字符串（str）
# print(None) #空值（None Type）
#
# print(True + 1)
# print(False - 1)
from ctypes import pythonapi

# 变量 -----> python 是动态类型语言，一个变量可以存储不同类型的数据的（但是，项目开发中，推荐一个变量只存储一种类型）
# num = 114.1
# print(num)
# num = num + 1
# print(num)
# num = 'OK'
# print(num)

# 案例
# base = 20.7 # 基础播放量
# incr = 50 # 新增播放量
base, incr = 20.7, 50
# 第一个月播放量
print('未来第一个月的播放量：', base + incr)
# 第二个月播放量
print('未来第二个月的播放量：', base + incr * 2)

# 标识符- 是程序员在代码中为变量、函数、类等元素所起的名字
# 标识符命名规则：
# 1.只能包含字母(a-z, A-Z)、数字(0-9)、下划线_
# 2.不能以数字开头
# 3. 不能使用关键字：True， False，None，and， or， if， else， elif，for， while等
# 4.严格区分大小写，比如：age,Age,AGE 是三个变量

# 标识符命名规范
# python 代码风格： https://peps.python.org/pep-0008/
# 1.见名知意
# 多个部分使用下划线链接
# 英文字符全小写
