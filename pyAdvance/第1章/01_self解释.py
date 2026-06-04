"""
self 关键字介绍
概述：
    它是Python内置的关键字，用于标识本类当前对象的引用。
作用：
    1个类是可以有多个对象的，这多个对象都可以通过 对象名. 的方式访问类中的行为(函数)
     函数默认有self属性，函数通过self来区分到底是哪个对象调用的该函数。
     大白话：谁调用函数，self就代表哪个对象
"""

class Car:
    def run(self):
        print("汽车会跑")
        print(f"我是run函数，self的值是:{self}")

# 创建汽车类的对象
c1 = Car()
print(f'c1对象：{c1}')
c1.run()
print('-' * 34)

c2 = Car()
print(f'c2对象：{c2}')
c2.run()