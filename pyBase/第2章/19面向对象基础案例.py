"""
需求：采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
系统使用自定义对象存储存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1. 添加购物车：用户根据提示录入商品名称、以及商品的价格，数量，保存该商品信息到购物车
2. 修改购物车：要求用户输入要修改的购物车商品名称，然后在提示输入盖商品的价格、数量、输入完成后修改该商品信息。
3. 删除购物车：要求用户输入要删除的商品名称，根据名称删除购物车中的商品。
4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx, 商品价格： xxx, 商品数量：xxx"
5. 退出购物车
"""

# 商品信息
class Goods:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称: {self.name}, 商品价格：{self.price}, 商品数量：{self.num}"

    def update_goods(self, price, num):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num


class ShoppingCat:
    def __init__(self):
        self.goods_list = []
    # 添加商品
    def add_goods(self):
        g_name = input("请输入商品名称:")
        for goods in self.goods_list:
            if goods.name == g_name:
                print("该商品已存在，不能添加")
                return
        g_price = float(input("请输入商品价格："))
        g_num = int(input("请输入商品数量："))
        self.goods_list.append(Goods(g_name, g_price, g_num))
        print("商品添加完毕~")
    # 修改商品
    def update_goods(self):
        g_name = input("请输入要修改的商品名称:")
        for goods in self.goods_list:
            if goods.name == g_name:
                g_price = float(input("请输入要修改的商品价格："))
                g_num = int(input("请输入要修改的商品数量："))
                goods.update_goods(g_price, g_num)
                print("商品修改成功~")
                return
        print("该商品不存在，无法修改~")
    # 删除商品
    def delete_goods(self):
        g_name = input("请输入要删除的商品名称:")
        for goods in self.goods_list:
            if goods.name == g_name:
                self.goods_list.remove(goods)
                print("商品删除成功~")
                return
        print("该商品不存在，无法删除~")
    # 展示商品信息
    def show_goods(self):
        for goods in self.goods_list:
            print(goods)

    # 执行
    def run(self):
        print("欢迎使用购物车系统~")
        menu = """
        ################ 购物车系统 ################
        # 1. 添加购物车    2. 修改购物车             #
        # 3. 删除购物车    4. 查询购物车             #
        # 5. 退出购物车                            #
        ##########################################
        """
        while True:
            print()
            print(menu)
            choice = int(input("请选择要执行的操作，输入 1-5："))
            match choice:
                case 1:
                    self.add_goods()
                case 2:
                    self.update_goods()
                case 3:
                    self.delete_goods()
                case 4:
                    self.show_goods()
                case 5:
                    print("Bye Bye")
                    break
                case _:
                    print("输入错误，请输入1-5之间的操作")

# 测试
if __name__ == "__main__":
    cat = ShoppingCat()
    cat.run()
