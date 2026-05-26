"""
# while 循环
while 条件表达式:
    循环体语句1
    循环体语句2
else: # 可选部分
    条件为False，循环正常结束时执行

for 循环： 本质是一种轮询遍历机制，对一批内容进行逐个处理
for 元素 in 待处理数据集:
    循环体代码(对元素进行处理)
else: # 可选
    循环结束时，执行的代码
"""
# i = 0
# while i < 10:
#     print("人生苦短，我用Python")
#     i += 1
# else:
#     print("循环正常结束")

# 计算 1-100之间，所有偶数之和
# total = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         total += i
#     i += 1
#
# print(f"1-100之间的偶数的累加之和：{total}")
# msg = "hello-Python"
# for char in msg:
#     print(char)
# else:
#     print("循环结束")



# 练习 基于for 循环完成如下需求
# 1. 计算 1- 100 之间所有奇数之和。
# 2. 计算100-500之间所有3的倍数的数字之和
# 如何获取到1-100的数据集  ---> range
"""
range 语句
作用：生成制定规则的数字序列
range(end) --> 获取一个从0开始， 到end 结束的数字序列(不含end本身)
range(5) -> 0, 1, 2, 3, 4, 
range(start, end)  --> 获取一个从start开始，到end结束的数字序列(不包含end本身)
range(2, 6) --> 2, 3, 4, 5
range(start, end, step) ---> 获取一个从start开始，到end结束的熟悉序列，step步长(不包含end本身)
range(2, 10, 2) --> 2, 4, 6, 8
"""


total = 0
# for num in range(1, 101):
#     if num % 2 == 1:
#         total += num
# print(f"1-100之间奇数之和：{total}")
# 优化
"""
for i in range(1, 101, 2):
    total += i
print(f"1-100之间奇数之和：{total}")


sum1 = 0
for num in range(100, 501):
    if num % 3 == 0:
        sum1 += num
print(f"100-500之间所有3的倍数的数字之和：{sum1}")
"""

"""

# 循环嵌套：根据输入的长方形的长度m, 宽度n, 打印一个长方形
m = int(input("请输入长方形的长度："))
n = int(input("请输入长方形的宽度："))
for j in range(n): # 控制行
    for i in range(m): # 控制列
        print('*', end=' ')
    print() # 为了换行
"""
"""
# 案例：打印99乘法表
for i in range(1, 10): # 控制行
    for j in range(1, i + 1): # 控制列
        print(f"{j} x {i} = {j * i}", end='\t')
    print()
"""
"""
需求 根据输入用户名和密码进行登录 -----
    1.正确的用户名和密码为：admin/666888  root/547527  zhangsan/123456
    2.输入用户名和密码，知道登陆成功，程序结束运行，如果登录失败，则继续输入用户名和密码进行登录
    3.输入的用户名和密码不能为空
    4.登陆成功，输出“登录成功，进入B站首页~”
    5.登录失败：输出 “用户或者密码错误， 请重新输入！”
关键字： 
    break， 只能够出现在循环中，表示结束，跳出循环的含义（break 跳出循环时，while后边的else中的代码将不会执行）
    continue:只能出现在循环中，表示中断本次循环，直接进入下一次循环
"""
"""
while True:
    # 1.输入用户名和密码
    account = input("请输入用户名：")
    password = input("请输入密码：")
    # 2.校验：输入的用户名和密码不能为空
    if account == '' or password == '':
        print('输入的用户名或者密码不能为空')
        continue # 结束本次循环，进入下次循环
    # 3.判断用户名和密码的正确性，执行登录操作
    if account == 'admin' and password == '666888':
        print('登录成功，进入B站首页~')
        break # 跳出(结束)循环
    elif account == 'root' and password == '547527':
        print('登录成功，进入B站首页~')
        break
    elif account == 'zhangsan' and password == '123456':
        print('登录成功，进入B站首页~')
        break
    else:
        print('用户或者密码错误， 请重新输入！')
"""

"""
作业： 用户名密码登录，正确的用户名和密码为 admin/666888  root/888888  zhangsan/123456，
5次登录机会，输入错误五次，不允许在操作了
"""
"""

i = 0
while i < 5:
    username = input("请输入用户名：")
    pwd = input("请输入密码：")
    if username == '' or pwd == '':
        print('输入的用户名或者密码不能为空')
        i += 1
        continue # 结束本次循环，进入下次循环
    if username == 'admin' and pwd == '666888':
        print('登录成功，进入B站首页~')
        break # 跳出(结束)循环
    elif username == 'root' and pwd == '888888':
        print('登录成功，进入B站首页~')
        break
    elif username == 'zhangsan' and pwd == '123456':
        print('登录成功，进入B站首页~')
        break
    else:
        i += 1
        print('用户或者密码错误， 请重新输入！')
else:
    print('5次机会已用完，不允许再操作了！！！')
"""

"""
猜数字游戏
1.系统随机生成一个随机数 random
2.用户根据提示猜数字，并将所猜的数字输入系统
3.如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
4.如果猜对，系统自动退出，游戏结束
"""

import random
# 生成随机整数
random_num = random.randint(1,100)

while True:
    num = int(input("请输入一个数字:"))
    if num > random_num:
        print("你输入的数字太大了！")
    elif num < random_num:
        print("你输入的数字太小了！")
    else:
        print("恭喜你，猜对了， 666")
        print(f"随机数是 {random_num}")
        break


