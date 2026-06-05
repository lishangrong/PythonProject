"""
生成器：
    概述：
        根据程序员制定的规则循环生成数据，当条件不成立时则生成数据结束。
        数据不是一次性全部生成出来，而是使用一个，再生成一个，可以节约大量内存

    创建生成器的方式：
        1.生成器推导式
        2.yield 关键字
"""
import  sys

# 场景1：生成器 推导式写法
# 需求1: 生成 1~10 之间的整数
my_generator = (i for i in range(1, 11))
print(my_generator)
print(type(my_generator)) # <class 'generator'>
print('-' * 23)

# 需求2： 生成1~10之间的偶数
my_gt2 = (i for i in range(1, 11) if i % 2 == 0)
print(my_gt2)
print('-' * 23)

# 需求3：如何从生成器中获取数据。
# 思路1： next()
print(next(my_gt2))
print(next(my_gt2))
print('-' * 23)
for i in my_gt2:
    print(i)  # 6, 8, 10

# 验证 生成器的目的，就是可以减少内容占用
my_list = [i for i in range(10000000)]
my_gt3 = (i for i in range(10000000))
print(type(my_list), type(my_gt3))

# 查看my_list 的内存空间占用
print(f'my_list 占用内存空间为：{sys.getsizeof(my_list)}')  # 89095160
print(f'my_gt3 占用内存空间为：{sys.getsizeof(my_gt3)}')  # 192

