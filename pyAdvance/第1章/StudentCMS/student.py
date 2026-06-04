"""
该文件用于记录学生类， 学生属性信息为：姓名，性别，年龄，手机号，描述信息
"""

# 1. 定义学生类
class Student:
    # 2. 定义魔法方法，初始化属性信息
    def __init__(self, name, sex, age, phone, desc):
        """
        该魔法方法，用于初始化 属性信息
        :param name: 学生姓名
        :param sex: 学生性别
        :param age: 学生年龄
        :param phone: 学生手机号
        :param desc: 学生描述
        """
        self.name = name
        self.sex = sex
        self.age = age
        self.phone = phone
        self.desc = desc
    # 3. 定义魔法方法，打印学生信息
    def __str__(self):
        return f"姓名：{self.name}，性别：{self.sex}，年龄：{self.age}，手机号：{self.phone}，描述信息：{self.desc}"


# 测试
if __name__ == '__main__':
    xm = Student("小明", "男", 18, "13888888888", "小明是一个爱学习，爱敲代码的小伙伴")
    print(xm)

