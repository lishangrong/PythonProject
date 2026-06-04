"""
装饰器的使用分类：
    细节：
        装饰器的内部函数格式，要和 被装饰的原函数 保持一致，
        即：原函数是无参无返回的， 则 装饰器的内部函数也必须是 无参无返回值的
            原函数时有参有返回的，则 装饰器的内部函数也必须是 有伞又返回的

1.无参无返回值的函数
2.有参无返回值的函数
3.无参有返回值的函数
4.有参有返回值的函数

"""



# 需求：定义有1个可以计算多个数据和字典values值和的函数，并给出友好提示：
# 1. 定义装饰器
def my_decorator(fu_name):
    #1.1 定义内部函数
    def fun_inner(*args, **kwargs):
        # 1.2 添加提示信息【额外功能】
        print("正在努力计算中...")
        # 1.3 调用原函数【原功能】
        return fu_name(*args, **kwargs)

    # 1.4 返回内部函数
    return fun_inner

# 2. 定义被装饰的函数
@my_decorator
def get_sum(*args, **kwargs):
    """
    该函数用于计算 数字元祖 和字典value值 之和
    :param args: 数字元祖 *args --> 接收所有的位置参数，封装到元祖
    :param kwargs: 字典，键是字符串，值是数字，**kwargs ---> 接收所有的关键字参数，封装到 字典
    :return: 结果之和
    """
    # _sum = 0
    # # 遍历元祖，获取每个元素，求和
    # for i in args:
    #     _sum += i
    # # 遍历字典，获取每个元素值，求和
    # for v in kwargs.values():
    #     _sum += v
    #
    # return _sum

    return sum(args) + sum(kwargs.values())

# 3.测试
# 3.1 传统方式
# get_sum = my_decorator(get_sum)
# result = get_sum(11, 88, a=10, b=2 )
# print(result)

# 3.2 语法糖
res = get_sum(999, 11, a=10, b=2)
print(res)
