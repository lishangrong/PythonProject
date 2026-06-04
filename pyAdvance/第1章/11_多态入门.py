"""
案例：演示多态入门
多态概述：
    专业版：同一个函数，接收不同的参数，有不同的效果
    大白话：同一个事物在不同时刻表现出来的不同状态，形态

    前提条件：
    1. 要有继承(定义父类、定义子类、子类继承父类)
    2. 要有方法重写，不然多态无意义 （子类重写父类的函数）
    3. 要有父类引用指向子类对象 （子类对象传给父类对象调用者）
    案例： 动物类案例

封装：
    好处： 安全性、复用性
    弊端： 代码量增量
继承：
    好处：复用性、子承父业
    弊端：耦合性增强了
多态：
    好处： 应用解耦，同函数、不同效果
    弊端：无法精准限定类型

python 中：抽象类 = 接口

"""
from pyclbr import Class


# 1. 定义动物类
class Animal:  # 抽象类(也叫：接口)
    def speak(self):  # 抽象方法
        pass

# 2. 定义子类 狗类
class Dog(Animal):
    def speak(self):
        print("狗叫：汪汪汪")

# 3. 定义子类，猫类
class Cat(Animal):
    def speak(self):
        print("猫叫：喵喵喵")

class Car:
    def speak(self):
        print("车叫：滴滴滴")
# 定义函数，接收不同的动物对象，调用speak方法
def make_noise(an:Animal): # an:Animal = Dog() 父类引用指向子类对象
    an.speak()

if __name__ == '__main__':
    # 创建对象, 猫类，狗类
    an: Animal = Dog()  # 父类引用指向子类对象
    d:Dog = Dog() # 创建狗类对象
    d1 = Dog()
    c1 = Cat()
    # 调用函数
    make_noise(d1)
    make_noise(c1)
    print('-' * 23)
    # 创建对象，汽车类
    c = Car()
    make_noise(c)