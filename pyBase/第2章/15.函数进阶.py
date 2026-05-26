# 全局变量
from itertools import count

num= 10

def circle_area(radius):
    # 局部变量：仅能在函数内部使用
    pi = 3.14
    area = pi * radius * radius
    # # 局部变量 num
    # num = 1000
    # 修改全局变量 --- 先声明(global 关键字)，后使用
    global num
    num = 10000
    print("num=", num)
    return area

print(f"全局变量：{num}" )
# print("pi=", pi)
# print("area=", area)
c_area = circle_area(20)
print(c_area)

"""
函数传参方式:
1. 位置参数，调用函数时根据函数定义时的位置来传递参数
2. 关键字参数：调用函数时，以函数定义时形参名称作为关键字，以 “键=值” 的形式来传递参数（不要求顺序）

参数默认值：也称为缺省参数，用于定义函数时，为参数提供默认值，调用函数时，可以不传递有默认值的参数
注意：默认参数必须放在没有默认值的参数列表的后面，一个函数在定义时是可以设置多个默认参数的。
注意：寒素调用时，如果为默认参数传递了值，则会修改默认的参数值，如果没有传递该参数，则直接使用默认值

不定长参数：也叫可变参数，用于函数定义及调用时参数个数不确定(0个或多个)的场景。  类型： 位置传递 、 关键字传递
位置传递方式(*args)
关键字传递方式(**kwargs)
def 函数名(*args):
注意：传递的所有匹配的位置参数都会被args 变量收集，这些参数会合并封装为一个元祖， args 是元祖类型(注意并不会封装关键字参数)
注意：args只是约定俗成的变量名，并不是关键字，这里可以使用任何合法的变量名(如 *data)
注意：参数是以"键=值"形式传递的关键字参数，这些 “键=值” 参数都会被kwargs 接受，并合并封装为一个字典类型



"""
#------------------- 函数 传参方式 -----------------------------------
"""
# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功，姓名{name},年龄: {age}, 性别: {gender}, 城市: {city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数 - 传参方式：位置参数
stu = reg_stu("赵四", 18, "男", "北京")
print(stu)
# 调用函数-传参方式：关键字参数
stu1 = reg_stu(name="张三", age= 20, gender="男", city="上海")
print(stu1)
stu2 = reg_stu(gender="女", name="丽丽", city="南京", age=18)
print(stu2)
# 调用函数- 传参方式：位置参数 + 关键字参数 ---> 位置参数在前，关键字参数在后
stu3 = reg_stu("李牧晚", 20, gender="女", city="深圳")
print(stu3)
"""
# -------------------函数 默认参数-----------------------------

def reg_stu(name, age, gender="男", city="北京"):
    print(f"注册成功，姓名{name},年龄: {age}, 性别: {gender}, 城市: {city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
stu = reg_stu("王林", 22)
print(stu)

stu1 = reg_stu("李木木", 24, "女")
print(stu1)

stu2 = reg_stu("韩力", 22, city="上海")
print(stu2)

print("----------------------------------------------------------------------")

#---------------------- 函数 不定长参数(位置参数 *args ---> 元祖) ---------------------------
# 需求，定义函数，根据传入的数据，计算这批数据中的最小值、最大值、平均值。
# 注意：传递的所有匹配的位置参数都会被args 变量收集，这些参数会合并封装为一个元祖， args 是元祖类型(注意并不会封装关键字参数)

# def calc_data(*args):
#     max_data = max(args)
#     min_data = min(args)
#     avg_data = sum(args) / len(args)
#     return max_data, min_data, round(avg_data, 1)
#
# print(calc_data(2, 7, 8, 10, 11))
# print(calc_data(2, 7, 8, 10, 11, 93, 102, 777, 222))

# ----------------------------函数 不定长参数（关键字传递 **kwargs ---> 字典类型）
def calc_data(*args, **kwargs):
    """

    :param args:  不定长位置参数，需要计算这批数据
    :param kwargs: 不定长关键字参数
        round：保留的小数位个数
        print： 是否打印输出
    :return: 最大值、最小值、平均值
    """
    max_data = max(args)
    min_data = min(args)
    avg_data = sum(args) / len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))
    if kwargs.get("print"):
        print(f"最大值：{max_data}，最小值：{min_data}, 平均值：{avg_data}")

    return max_data, min_data, avg_data

print(calc_data(2, 7, 8, 10, 11, round = 3, print = True))
print(calc_data(34, 67, 89, 44, 32, 11))
print(calc_data(2, 7, 8, 10, 11, 93, 102, 777, 222, round=4))


print('--------------------------------------')
# 函数的参数参数类型：
# 普通参数：数字，布尔，字符串，列表，元祖，集合，字典等
# 特殊参数：函数

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y


def calc(x, y, oper):
    return oper(x, y)

print(calc(1, 2, add))
print(calc(1, 2, subtract))
print(calc(1, 2, multiply))
print(calc(1, 2, divide))

print("-------------------匿名函数--------------------")
"""
匿名函数：指没有名称的函数， 需要通过lambda表达式来声明函数，可以简化简单函数的编写(单行表达式)
注意：函数逻辑比较简单（单行表达式）且只在一个地方使用时，可以考虑使用匿名函数，简化书写(通常作为高阶函数的参数使用)
注意： 匿名函数仲可以返回结果，也可以不返回结果。返回结果时，不需要写return， 表达式的运行结果就是要返回的结果
"""
lambda x, y: x + y
lambda: print('----------')

# 调用函数需要将匿名函数赋值给一个变量
out_line = lambda: print('----------')
out_line()
add = lambda x, y: x + y
print(add(1, 2))

print('-----------------------------------------------------------')
# 需求：完成如下列表的排序操作，按照每一个元素的字符个数， 从小到大排序；
data_list = ["C++", "C", "Python", "Jack", "PHP","Java", "Go", "JavaScript", "Rust"]

# print(data_list)
# data_list.sort()
# print(data_list)

# sort方法中的参数说明，key控制如何排序， 是一个函数
# sort(*, key=None, reverse=False)
data_list.sort(key=lambda item: len(item))
print(data_list)

print("-----------------------------------------------")
# 定义一个函数，根据传入的数字，计算该数字阶乘的结果 N *(N-1)*(N-2)....*2 *1

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(10))
print(factorial(1), factorial(2), factorial(3), factorial(4))

print("--------------------------------------------")

"""
电商订单计算器
定义一个函数，用于根据传入的一批商品信息(商品名，价格，数量)，优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
具体规则如下：
1.优惠券需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价
2. 积分抵扣需要商品总金额满5000 才可以使用，100积分抵扣1元(切抵扣金额不能超过商品总价，积分智能整百抵扣)
"""

def calc_order_cost(*args:tuple[str, float, int], coupon:int = 0, score:int = 0, express:float= 0) -> float:
    """
    根据传入的一批商品信息(商品名，价格，数量)，优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
    :param args: 一批商品信息 ---->("键盘", 188, 2) ("鼠标", 99, 3)
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单总金额
    """

    # 订单总金额 = 商品总额 - 优惠券 - 积分抵扣 + 运费
    # 1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    # 2. 扣减优惠券
    if total_cost >= 5000 and total_cost >= coupon:
        total_cost -= coupon
    # 3. 扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
    # 4. 添加运费
    total_cost += express
    # 返回总订单金额
    return total_cost

# 不满5000时
total = calc_order_cost(("键盘", 188, 2), ("鼠标", 99, 3), ("手机", 3999, 1), coupon=10, score=4000, express=9.9)
print(total)

# 满5000
total = calc_order_cost(("键盘", 188, 20), ("鼠标", 99, 30), ("手机", 3999, 1), coupon=22, score=6000, express=9.9)
print(total)

# 无优惠券，无积分
total = calc_order_cost(("键盘", 188, 10), ("鼠标", 99, 10), ("手机", 3999, 1), express=9.9)
print(total)
# 无优惠券，无积分，无运费
total = calc_order_cost(("键盘", 188, 10), ("鼠标", 99, 10), ("手机", 3999, 1))
print(total)

# 参数类型不正确时
total = calc_order_cost(("键盘", "188", 10), ("鼠标", 99, 10), ("手机", 3999, 1))
print(total)


print("----------------------------------------------------")

# 类型注解：是python中的一种语法特性，用于明确标识变量、函数参数和返回值的数据类型，从而使代码更清新，更安全、更易维护。
# 类型推断：是指python解释器自动推断出变量，表达式或幻术返回值的数据类型的能力，而无需开发者显示声明。
# 如果对变量直接赋值、变量运算等场景，Python会自动进行类型推断。
# Python 是动态类型语言，添加的类型注解只是提示，并不是强制约束！！！

a = 3
score = 66.5
hobby = "python, java"
flag = False
pic = None
names = ["A", "B", "C", "D", "E", "F"]
phones = {"13581764567", "18876567890"}
options= {"count": 10, "total": 20}
goods = ("手机", 3999, 1)
names.append("X")
names.append(1000)


a:int = 3
score:float = 66.5
hobby:str = "python, java"
flag:bool = False
pic:None = None
names:list[str | int] = ["A", "B", "C", "D", "E", "F"]
phones:set[str] = {"13581764567", "18876567890"}
options:dict[str, int] = {"count": 10, "total": 20}
goods:tuple[str, int, int] = ("手机", 3999, 1)

names.append("X")
names.append(1000)

# 函数的类型注解
def calc(scores:list[int]) -> float:
    return sum(scores) / len(scores)

def calc_data(scores:list[int]) -> tuple[int, int, float]:
    max_v = max(scores)
    min_v = min(scores)
    avg_v = sum(scores) / len(scores)
    return max_v, min_v, avg_v
