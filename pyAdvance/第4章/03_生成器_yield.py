"""
生成器：
    概述：
        根据程序员制定的规则循环生成数据，当条件不成立时则生成数据结束。
        数据不是一次性全部生成出来，而是使用一个，再生成一个，可以节约大量内存

    创建生成器的方式：
        1.生成器推导式
        2.yield 关键字
"""
# 需求： 通过yield方式，获取生成器之 1 ~ 10 之间的整数
# 回顾： 推导式写法
my_gt = (i for i in range(1, 11))

# yield方式如下
# 1. 定义函数，存储到生成器中，并返回
def my_fun():
    # yield 在这里做了三件事：1.创建生成器对象，2.把值存储到生成器中， 3.返回生成器
    for i in range(1, 11):
        yield i

# 测试
my_gt2 = my_fun()
print(type(my_gt2))

print(next(my_gt2))
print(next(my_gt2))

print('-' * 23)
for i in my_gt2:
    print(i)