"""
案例：演示对象属性 和 类属性
属性介绍：
    概述：
        它是1个名词，用来描述事物的外在特征的
    分类：
        对象属性：属于每个对象的，即：每个对象的属性值可能都不同，修改A对象的属性，不影响对象B
        类属性：属于类的，即：能被该类下的所有对象所共享，A对象修改类属性，B对象访问的是修改后的

对象属性：
    定义到init 魔法方法中的属性，每个对象都有自己的内容
    只能通过 对象名. 的方式调用
类属性：
    定义到类中，函数外的属性(变量)，能被该类下所有的对象所共享
    既能通过 类名. 还能通过 对象名. 的方式来调用，推荐使用 类名. 的方式

"""

# 需求：演示 对象属性 和类属性相关
# 1. 定义1个 Student 类，每个学生都有自己的 姓名、年龄
class Student:
    teacher_name = "水镜先生"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}"

if __name__ == '__main__':
    # 场景1：对象属性
    s1 = Student("曹操", 38)
    s2 = Student("曹操", 40)
    # 修改s1 的属性
    s1.name = '许褚'
    s1.age = 40
    print(f's1: {s1}')
    print(f's2: {s2}')
    print('-' * 34)

    # 场景2：类属性
    print(s1.teacher_name)
    print(s2.teacher_name)
    print(Student.teacher_name)
    print('*' * 34)
    # 尝试用 对象名. 修改类属性
    # s1.teacher_name = "东子" # 只能给s1对象赋值，不能给类属性赋值
    # 如果要修改类属性的值，只能 通过 类名. 的方式
    Student.teacher_name = "东子"
    print(s1.teacher_name)
    print(s2.teacher_name)
    print(Student.teacher_name)