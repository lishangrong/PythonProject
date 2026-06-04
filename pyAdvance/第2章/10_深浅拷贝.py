"""
深浅拷贝
1. 所谓的深浅拷贝分别指的是：
    浅拷贝：copy模块的copy()
    深拷贝：copy模块的deepcopy() 函数
2. 深浅拷贝主要是针对于可变类型来讲的，深拷贝拷贝所有层(可变)，浅拷贝只拷贝第1层(可变)
    如果针对于不可变类型，则用法 和普通赋值一样，并无区别
"""

import copy

# 普通赋值
def demo_01():
    a = 10
    b = a
    print('id(a)-->', id(a))  # 0x01
    print('id(b)-->', id(b))  # 0x01
    print('id(10)-->', id(10))  # 0x01

    a = [1, 2,3]
    b = [11, 22, 33]
    c = [a, b]
    d = c
    print('id(c)-->', id(c))  # 0x02
    print('id(d)-->', id(d)) # 0x02

# 浅拷贝可变类型
def demo_02():
    a = [1, 2,3]      # 0x01
    b = [11, 22, 33]  # 0x02
    c = [6, 7, a, b]  # 0x03

    d = copy.copy(c)  # 浅拷贝

    print('id(c)-->', id(c))  # 0x03
    print('id(d)-->', id(d)) # 0x04

    # 测试2
    print(id(c[2]))  # 0x01
    print(id(a))    #0x01

    # 修改
    a[2] = 22
    print('c-->', c)
    print('d-->', d)

# 浅拷贝不可变类型
def demo_03():
    # 不可变类型 a，b, c
    a = (1, 2, 3)    #0x01
    b = (11, 22, 33) #0x02
    c = (6, 7, a, b) #0x03

    # 针对不可变类型，以下三种写法 结果一样
    d = copy.copy(c) # 浅拷贝 相当于普通赋值
    # d = c
    # d = copy.deepcopy(c)

    print('id(c)-->', id(c))  # 0x03
    print('id(d)-->', id(d))  # 0x03


# 深拷贝可变类型
def demo_04():
    a = [1, 2,3]      # 0x01
    b = [11, 22, 33]  # 0x02
    c = [6, 7, a, b]  # 0x03

    d = copy.deepcopy(c)  # 深拷贝

    print('id(c)-->', id(c))  # 0x03
    print('id(d)-->', id(d)) # 0x04

    # 测试2
    print(id(c[2]))  # 0x01
    print(id(a))    #0x01

    # 修改
    a[1] = 100
    b[1] = 800
    print('c-->', c) # [6, 7, [1, 100, 3], [11, 800, 33]]
    print('d-->', d) # [6, 7, [1, 2, 3], [11, 22, 33]]
    print(id(d[2]))  # 0x05
    print(id(d[3]))  # 0x06


# 深拷贝不可变类型
def demo_05():
    # 不可变类型 a，b, c
    a = (1, 2, 3)    #0x01
    b = (11, 22, 33) #0x02
    c = (6, 7, a, b) #0x03

    # 针对不可变类型，深拷贝
    d = copy.deepcopy(c)

    print('id(c)-->', id(c))  # 0x03
    print('id(d)-->', id(d))  # 0x03

if __name__ == '__main__':
    # demo_01()
    # demo_02()  # 多看看（面试知识点）
    # demo_03()
    # demo_04() # 多看看（面试知识点）
    demo_05()