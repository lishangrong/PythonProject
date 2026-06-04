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

多个装饰器装饰一个函数：
    多个装饰器装饰1个原函数，是按照 由内向外 的顺序来装饰的，
    但如果你要是用 装饰的写法来做，看到的效果是：从上往下执行的
    离函数最近的装饰器先装饰，然后外面的装饰器在进行装饰，是 由内到外 的装饰过程

"""

# 需求：发表评论，需要先登录，再验证验证码，请用所学，模拟该功能
# 1. 定义装饰器
def check_login(fu_name):
    #1.1 定义内部函数
    def fun_inner():
        # 1.2 添加提示信息【额外功能】
        print("校验登录，登录成功")
        # 1.3 调用原函数【原功能】
        fu_name()

    # 1.4 返回内部函数
    return fun_inner

# 2. 定义装饰器，表示:验证验证码
def check_code(fu_name):
    #1.1 定义内部函数
    def fun_inner():
        # 1.2 添加提示信息【额外功能】
        print("校验验证码，验证成功")
        # 1.3 调用原函数【原功能】
        fu_name()
    return fun_inner

# 2. 定义被装饰的函数
# @check_login
# @check_code
def comment():
    print("发表评论")

# 3.测试
# 3.1 传统方式
# check_code = check_code(comment)
# comment = check_login(check_code)
comment = check_code(comment)
comment = check_login(comment)
comment()





# 3.2 语法糖
# comment()

