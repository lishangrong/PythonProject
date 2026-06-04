"""
闭包解释：
    概述：内部函数 使用了外部函数的变量，这种写法就称之为闭包
    格式：
    def 外部函数名(形参列表):
        外部函数的(局部)变量

        def 内部函数名(形参列表):
            使用外部函数的变量

        return 内部函数名

闭包形成条件：
    有嵌套、有引用、有返回

global: 声明全局变量
nonlocal: 声明能够让内部函数去修改外部函数的变量

"""
# 需求：定义函数保存变量10，调用函数返回值，并重复累加数值，观察结果
#1. 定义函数，保存变量10

def func():
    num = 10
    # 2. 返回函数
    return num

num = func()
print(num + 1)  # 想要的结果：11
print(num + 1)  # 想要结果：12
print(num + 1) # 想要结果：13

# 闭包1
# def fun_outer(num1):
#     def fun_inner(num2):
#         sum_count =  num1 + num2
#         print(f"求和结果：{sum_count}")
#     return fun_inner
#
# fun_inner = fun_outer(10)
# fun_inner(20)
# print('-' * 23)
# fun_outer(100)(200)

# 闭包2
def fn_outer():
    a = 100
    def fn_inner():
        # nonlocal 让内部函数能修改外部函数的变量
        nonlocal  a
        a = a + 1
        print(f'a: {a}')
    return fn_inner

fn_inner = fn_outer()
fn_inner()
fn_inner()
fn_inner()