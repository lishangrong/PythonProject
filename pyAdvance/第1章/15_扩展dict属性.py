"""
案例： 演示 python内置的dict属性
__dict__ 属性介绍：
    它是python 内置的属性，可以把对象转成字典形式

"""
from StudentCMS.student import Student
# 需求1：把学生对象 ---> 字典形式，属性名做键，属性值做值
s1 = Student('小明', '男', 18, '13888888888', '小明是一个爱学习，爱敲代码的小伙伴')
print(s1)
## 知识点 __dict__
my_dict = s1.__dict__
print(my_dict)
print(type(my_dict))
print('-' * 23)

# 需求2：把[学生对象, 学生对象] ---> [字典，字典]
s1 = Student('明明', '男', 18, '13888885555', '小明是爱敲代码的小伙伴')
s2 = Student('小王', '男', 20, '13888886666', '小王是一个爱学习的小伙伴')
s3 = Student('张可', '男', 22, '13888888888', '小张是一个爱美的小伙伴')

stu_list = [s1, s2, s3]
list_dict = [stu.__dict__ for stu in stu_list]
print(list_dict)
print('-' * 23)

# 需求3：把[字典，字典] ---> [学生对象，学生对象]
my_dict = {'name': '明明', 'sex': '男', 'age': 18, 'phone': '13888885555', 'desc': '小明是爱敲代码的小伙伴'}
## 知识点 **
s4 = Student(**my_dict)
print(s4)
print(type(s4))
print('-' * 23)