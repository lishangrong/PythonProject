"""
数据容器-字典(dict):存储键值对(key:value)类型的数据，可以根据键(key)找到对应的值(value)
key不能重复，可修改
常用操作:
添加/修改：字典名称[key] = value   dict1[key] = value
删除： 字典名.pop(key) / del 字典名[key]   dict1.pop(key) / del dict1[key]
查询：字典名称[key]/ 字典名称.get(key)  dict1["王林"] / dict1.get("王林")
     字典名称.keys()  获取所有的key dict1.keys()
     字典名称.values() 获取所有的value  dict1.values()
     字典名称.items()  获取所有的key-value键值对  dict1.items()
"""
"""
# 定义字典
dict1 = {"王林": 675, "李慧": 688, "徐立国": 580, "韩丽": 732}
# key 必须是不可变类型(str, int, float, tuple)
dict4 = {0: 760, 1.5: 608, (1, 2): 580, "A": 708}
# 访问
print(dict1["李慧"])
# 修改
dict1["李慧"] = 645
print(dict1)
# 空字典
dict2 = {}
dict3 = dict()
print(type(dict1), type(dict2), type(dict3))
"""

# -----------------------字典常见操作-----------------
"""
dict1 = {"王林": 675, "李慧": 688, "徐立国": 580, "韩丽": 732, "涛哥": 550}
# 添加
print(dict1)

# 修改
dict1["涛哥"] = 620
print(dict1)

# 查询
print(dict1["涛哥"])
print(dict1.get("涛哥"))

print(dict1.keys())
print(dict1.values())
print(dict1.items())

# 删除
score = dict1.pop("涛哥")
print(score)
print(dict1)

del dict1["韩丽"]
print(dict1)

# 字典遍历
# 方式1：
for k in dict1.keys():
    print(f"{k}: {dict1[k]}")
print("----------------------------")
# 方式2
for k, v in dict1.items():
    print(f"{k}: {v}")
"""
# ---------------案例--------------------
"""
需求：开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1. 添加购物车：用户根据提示录入商品名称、以及商品的价格，数量，保存该商品信息到购物车
2. 修改购物车：要求用户输入要修改的购物车商品名称，然后在提示输入盖商品的价格、数量、输入完成后修改该商品信息。
3. 删除购物车：要求用户输入要删除的商品名称，根据名称删除购物车中的商品。
4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx, 商品价格： xxx, 商品数量：xxx"
5. 退出购物车
数据结构：shopping_cat = {商品名称:{price: 10, count: 1}, 商品名称2: {price: 11, count: 2}}}}
"""
# 初始化购物车
shopping_cat = {}
# 1.制作菜单
print("欢迎使用购物车管理系统 ~")
menu = """
################ 购物车系统 ################
#             1. 添加购物车                #
#             2. 修改购物车                #
#             3. 删除购物车                #
#             4. 查询购物车                #
#             5. 退出购物车                #
##########################################
"""
# 2. 执行具体操作
while True:
    print(menu)
    choice = input("请选择要执行的操作(1-5): ")
    match choice:
        case "1":  # 添加购物车
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_count = int(input("请输入商品数量："))
            if goods_name in shopping_cat:
                print("该商品已存在，请重新选择~")
            else:
                shopping_cat[goods_name] = {"price": goods_price, "count": goods_count}
                print("商品添加完毕~")

        case "2":  # 修改购物车
            goods_name = input("请输入要修改的商品名称：")
            if goods_name not in shopping_cat:
                print("该商品不存在，请重新选择~")
                continue
            goods_price = float(input("请输入商品最新的价格："))
            goods_count = int(input("请输入商品最新的数量："))
            shopping_cat[goods_name] = {"price": goods_price, "count": goods_count}
            print("商品修改完毕~")
        case "3":  # 删除购物车
            goods_name = input("请输入要删除的商品名称：")
            if goods_name in shopping_cat:
                del shopping_cat[goods_name]
                print("商品删除完毕~")
            else:
                print("该商品不存在，请重新选择~")

        case "4":  # 查询购物车
            for goods_name in shopping_cat.keys():
                goods_info = shopping_cat[goods_name]
                print(f"商品名称: {goods_name}, 商品价格: {goods_info["price"]}, 商品数量: {goods_info["count"]}")
        case "5":  # 退出购物车
            break
        case _:
            print("不支持此操作！！！")
