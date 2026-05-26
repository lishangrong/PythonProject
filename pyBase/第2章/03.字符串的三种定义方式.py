# 字符串的3种定义方式
# s1 = "hello"
# s2 = 'world'
#
# # 可换行
# s3 = """
# 白日依山尽，
# 黄河入海流，
# 欲穷千里目，
# 更上一层楼
# """
from token import STRING

# print(s1)
# print(s2)
# print(s3)
# print(type(s3))

# 转义字符 \', \", \n ---换行, \t --制表符
# msg = 'It\'s very easy!'
# print(msg)
# msg2 = "It's very easy!"
# print(msg2)
# msg3= "Hello 的意思就是\"你好\""
# print(msg3)
# print("\t欢迎大家进入Python课程的学习\n\t大家记得一键三连哦~")

# 字符串拼接
# slogan = '黑马程序员' '成就IT黑马'
# print(slogan)
# slogen = '盒马生鲜' + ' 下单2小时达'
# print(slogen)
# s1='人生苦短'
# s2='我用Python'
# print('龟叔说：', s1 + ',' + s2)

# 案例
# name='涛哥'
# age = 18
# pro='软件工程'
# hobby='Python、Java'
# print('大家好，我是' + name + ', 今年' + str(age) + '岁，学习的专业是' + pro + ', 爱好是' + hobby)

# 字符串格式化 ---> 方式一：通过 %s 占位符
# name='涛哥'
# age = 18
# pro='软件工程'
# hobby='Python、Java'
# print('大家好，我是%s,今年%s岁，学习的专业是%s, 爱好是%s' %(name,age,pro,hobby))

# 字符串格式化 ---> 方式二：f"...{变量名/表达式}..."
name='涛哥'
age = 18
pro='软件工程'
hobby='Python、Java'
print(f'大家好，我是{name},今年{age}岁，学习的专业是{pro}, 爱好是{hobby}' )