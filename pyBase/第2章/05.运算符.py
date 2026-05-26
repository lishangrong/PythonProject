# print('10 + 4 = ', 10 + 4)
# print('10 - 4 = ', 10 - 4)
# print('10 * 4 = ', 10 * 4)
# print('10 / 4 = ', 10 / 4)
# print('10 // 4 = ', 10 // 4)
# print('10 % 4 = ', 10 % 4)
# print('10 ** 4 = ', 10 ** 4)
#
# # 算术运算符的优先级： ** ----> * / // % ---> + -
# print('0.1 + 10 / 4**2 = ', 0.1 + 10 / 4**2)
#
# x = float(input("输入第一个数值:"))
# y = float(input("输入第二个数值:"))
# print('x + y = ', x + y)
# print('x - y = ', x - y)

# --------赋值运算符 ---------
# num = 85
# num += 10
# print('num +=10后， num=', num)
# num -= 10
# print('num -=10后， num=', num)
# num *= 10
# print('num *=10后， num=', num)
# num /= 10
# print('num /=10后， num=', num)
# num //= 10
# print('num //=10后， num=', num)
# num %= 3
# print('num %=3后， num=', num)
# num **= 3
# print('num **=3后， num=', num)

# ---------比较运算符 ----------
# print("100 == 100吗：", 100 == 100) # True
# print("'100' == '100'吗：", '100' == '100') # True
# print("'100' == 100吗：", 100 == '100') # False
# print("100 != 100吗：", 100 != 100) # False
#
# print("100 < 100吗：", 100 < 100) #False
# print("100 <= 100吗：", 100 <= 100) #True
#
# print("100 > 100吗：", 100 > 100) #False
# print("100 >= 100吗：", 100 >= 100) # True

# --------逻辑运算符（and-逻辑与，or-逻辑或， not-逻辑非） ----------

# n= int(input("请输入一个整数："))
# print(f"{n} 在10-20之间：", n >=10 and n <=20)
# print(f"{n} 在10-20之间：", 10 <= n <= 20)

n= int(input("请输入一个整数："))
print(f"{n} 小于10或者大于20：", n <10 or n > 20)