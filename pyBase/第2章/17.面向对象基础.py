"""
类： 定义类时，类名的命名规范-->大驼峰命名法 如 UserInfo、 UserAccount
 __init__ 初始化方法（名称不能改），对象创建时自动调用，可以在该方法中为对象设置对应的属性,
 self: 是第一个参数，表示当前所创建出来的实例对象

 魔法方法： 指python中提供的以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，比如 __init__
 魔法方法是不需要我们手动调用的，Python会在合适的时机自动调用。
 1. __init__  初始化方法
 2. __str__  字符串表示的方法
 3. __eq__   比较两个对象是否相等（equal）
 4.__lt__, __le__, __gt__, __ge__  支持比较两个对象的大小(
                                     小于(less than)，
                                     小于等于(less than or equal),
                                     大于(greater than)
                                     大于等于(greater than or equal),
                                     )
属性：
实例属性：属于每个具体对象的属性，每个对象都是独立的（各个对象特有的数据）
类属性：是属于类本身的属性，所有实例共享的(所有对象共享的数据或配置)
"""

# 定义类
# class Car:
#     pass
#
# # 创建对象
# c1 = Car()
# # 动态的为对象添加属性
# c1.color = 'red'
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 500000
#
# print(c1)
# print(c1.brand)
# print(c1.__dict__)

# 定义类
# __init__ 初始化方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性；名称不能改,
# self: 是第一个参数，表示当前所创建出来的实例对象

class Car:
    # 类属性
    wheel = 4  # 轮胎数量
    tax_rate = 0.1 # 购置税
    def __init__(self, c_color, c_brand, c_name, c_price):
        # 实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")
    # 创建实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶...")
    def total_cost(self, discount, rate=0.1):
        """
        计算提车的总费用，包含2部分：车的价格，税费
        :param discount: 折扣
        :param rate: 税率
        :return: 总价
        """
        return self.price * discount + self.price * rate
    # 魔法方法
    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"

    def __eq__(self, other):
        return self.price == other.price and self.brand == other.brand and self.name == other.name

    def __lt__(self, other):
        return self.price < other.price

"""
# 创建对象
c1 = Car('red', 'BMW', 'X5', 300000)
print(c1.__dict__)
print(c1.wheel)
c1.running()
print("汽车总价：", c1.total_cost(0.9, 0.1))

c2 = Car('白色', '奔驰', 'E300', 400000)

print(c2.__dict__)
print("奔驰E300总价：", c2.total_cost(0.8))
print(c1 == c2)
print(c1 < c2)
"""
