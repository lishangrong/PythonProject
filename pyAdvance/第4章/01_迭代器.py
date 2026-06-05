"""
迭代器（Iterator）是Python中的一种对象，用于在数据集合中逐个访问元素，而不需要暴露数据集合的底层实现。

迭代器是一个实现了 __iter__(), __next__() 方法的对象，使得可以逐步遍历它的元素

# 演示自定义迭代器

迭代器介绍：
    概述：
        自定义的类，只要重写了  __iter__() 和 __next__() 方法，就可以称为 迭代器。
    目的：
        隐藏底层的逻辑，让用户使用更方便
        惰性加载，用的时候才能获取
"""

# 需求，模拟range(1,6)，自定义 迭代器实现同等逻辑
# 场景1：回顾 range() 用法
for i in range(1,6):
    print(i)
print('-' * 23)

# 场景2：自定义迭代器
class MyIterator:
    # 通过init 魔法方法，初始化属性，指定范围
    def __init__(self, start, end, step=1):
        self.end = end
        self.current = start
        self.step = step
    # 重写iterator魔法方法，返回当前对象
    def __iter__(self):
        return self
    # 重写next 魔法方法，返回当前值，并更行当前值
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        # value = self.current
        # self.current += self.step
        # return value
        # 优化
        self.current += self.step
        return self.current - self.step


# 创建迭代器对象，并遍历
for i in MyIterator(1,6):
    print(i)
print('-' * 23)

# next() 函数
my_iter = MyIterator(10,13)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))  # 报错




