"""
案例：演示类方法和静态方法
类方法：
    属于类方法，可用通过 类名. 还可以通过 对象名. 的方式来调用。
    定义类方法的时候，必须使用装饰器 @classmethod，且第一个参数必须表示 类对象

静态方法：
    属于该类下所有对象所共享的方法，可以通过 类名. 还可以通过 对象名. 的方式来调用
    定义静态方法时，必须使用装饰器@staticmethod, 且参数传不传都可以

区别：
    1. 类方法的第一个参数必须是 类对象，静态方法无参数的特殊要求
    2. 你可以理解为：如果函数中要用 类对象，就定义成类方法，否则 定义成 静态方法，除此外，并无任何区别。
"""

# 定义学生类
class Student:
    # 定义类属性
    school = '黑马程序员'
    # 定义类方法
    @classmethod
    def show1(cls):
        print(f"cls: {cls}") #  <class '__main__.Student'>
        print(cls.school)
        print('我是类方法')
    # 定义静态方法
    @staticmethod
    def show2():
        print(Student.school)
        print('我是静态方法')

# 测试
if __name__ == '__main__':
    s1 = Student()
    s1.show1()
    print('-' * 23)
    s1.show2()