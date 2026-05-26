# 模式匹配 match...case(3.10版本中的新语法) 工作日程安排
"""
day = input("请输入星期几（1-7）：")
match day:
    case "1":
        print("周一：工作会议日")
    case "2":
        print("周二：学习培训日")
    case "3":
        print("周三：项目开发日")
    case "4":
        print("周四：代码审查日")
    case "5":
        print("周五：总结规划日")
    case "6" | "7":
        print("周末：休息放松日")
    case _: # 匹配其他所有的情况的
        print("输入有误！")

"""

# 案例 基于match-case 实现一个简易的计算器，可以实现 + - * / 运算，用户输入需要运算的两个数和运算符之后，就可以进行计算
# num1 = float(input("请输入第一个数："))
# num2 = float(input("请输入第二个数："))
# oper = input("请输入运算符(+ - * /):")
# match oper:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "/" if num2 != 0: # if 条件成立，才匹配这个case
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("操作不支持")

# 练习 编写游戏校色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行相应的动作(输出控制台)
# 玩家输入 上/w/W - 角色上移， 下/s/S - 角色下移, 左/a/A - 角色左移, 右/d/D - 角色右移,
# 跳/" "(空格) - 角色跳跃， 攻击/j/J - 角色发动攻击，退出/esc/ESC - 角色退出游戏
promise = input("请输入游戏指令：")
match promise:
    case "上" | "w" | "W":
        print("角色向上移动")
    case "下" | "s" | "S":
        print("角色向下移动")
    case "左" | "a" | "A":
        print("角色向左移动")
    case "右" | "d" | "D":
        print("角色向右移动")
    case "跳" | " ":
        print("角色跳跃")
    case "攻击" | "j" | "J":
        print("角色发动攻击")
    case "退出" | "esc" | "ESC":
        print("角色退出游戏")
    case _:
        print("操作不支持")