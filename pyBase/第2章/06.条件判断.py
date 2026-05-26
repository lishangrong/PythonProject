# if 条件判断
# score = 600
# if score > 680:
#     print('欢迎你来清华读书')
#     print('也恭喜你即将踏入精彩的大学生活')
#
# print('------------')

# 案例 账号密码判断
# ok_account = '18888888888'
# ok_pwd = '666888'
# account = input("请输入B站账号:")
# pwd = input("请输入B站密码:")
# if account == ok_account and pwd == ok_pwd:
#     print("登录成功，进入B站首页")
# # if account != ok_account or pwd != ok_pwd:
# #     print("登录失败~，账号或密码错误")
# else:
#     print('登录失败~，账号或密码错误')

# 案例， 判断输入年份是否是闰年， 非整百年-被4整除， 整百年-被400整除
# year = int(input('请输入要判断的年份：'))
#
# if (year % 100 !=0 and year % 4 ==0) or year %400 == 0:
#     print(f'{year}是闰年~')
# else:
#     print(f'{year}是平年~')

# 案例， 判断输入的数字 ，是正数？  负数？ 0？
# num = int(input('请输入一个数字:'))
# if num > 0:
#     print(f'{num} 是正数')
# elif num < 0:
#     print(f'{num} 是负数')
# else:
#     print('是0')

# 案例 根据输入用户名和密码进行登录 -----admin/666888  root/547527  zhangsan/123456
# username = input('请输入用户名：')
# password = input('请输入密码：')
# if username == 'admin' and password == '666888':
#     print('登陆成功1~')
# elif username == 'root' and password == '547527':
#     print('登陆成功2~')
# elif username == 'zhangsan' and password == '123456':
#     print('登陆成功3~')
# else:
#     print('登录失败，用户名或者密码错误')

# 练习1  考试成绩  >85 优秀， 60-85 及格 其他 不及格
# score = float(input('输入考试成绩：'))
# if score >= 85:
#     print('成绩优秀')
# elif 60 <= score< 85:
#     print('成绩合格')
# else:
#     print('成绩不合格')

# 练习2 购物折扣计算，输出实际应付金额
# 金额 > 500: 8折， 300<= 金额 < 500: 九折， 100<= 金额 < 300 : 95折, 金额< 100： 无折扣
# 多行注释 """
"""
amount = float(input('输入商品总额：'))
if amount > 500:
    print(f'实付金额：{amount * 0.8}')
elif 300 <= amount < 500:
    print(f'实付金额：{amount * 0.9}')
elif 100 <= amount < 300:
    print(f'实付金额：{amount * 0.95}')
else:
    print(f'实付金额：{amount}')
"""

# 案例：三角形类型判断：根据输入的三个边的边长(正整数)，判断是等边三角形，等腰三角形，普通三角形，还是不能构成三角形
a = int(input("输入第一个边的边长："))
b = int(input("输入第二个边的边长："))
c = int(input("输入第三个边的边长："))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print(f'{a} {b} {c} 这三个边构成等边三角形')
    elif a == b or b == c or c == a :
        print(f'{a} {b} {c} 这三个边构成等腰三角形')
    else:
        print(f'{a} {b} {c} 这三个边构成普通三角形')
else:
    print(f'{a} {b} {c} 这三个边不能构成三角形')