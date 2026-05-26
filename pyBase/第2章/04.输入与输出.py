# # 获取键盘上输入的数据 ----input(...)
# name= input('请输入你的姓名：')
# age = input("请输入你的年龄：")
# print(f"你的姓名是{name}, 年龄是{age}")

# 案例
# 需求：银行卡中有10000元，ATM进行取钱操作，根据输入金额
total = 10000
p = input("输入密码：")
num = input('输入金额：')
print(f"取款后银行卡余额{total - int(num) }")
