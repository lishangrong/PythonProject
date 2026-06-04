"""
案例：子类重写父类功能后，继续访问父类功能
思路：
    1. 父类名.父类函数名(self)  # 精准访问，想找哪个父类，就调用哪个父类
    2.super().父类函数名()  # 只能访问最近的父类，有就用，没有就报错
"""
# 故事4：很多顾客都希望能吃到徒弟做出的有自己独立品牌的煎饼果子，也有黑马配方技术的煎饼果子味道。

# 师傅类
class Master:
    def __init__(self):
        self.kongfu = '[古法配方]'

    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼果子")

# 学校类
class School:
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼果子")

# 定义子类，
class Prentice(School, Master): #从左到右，就近原则
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'
    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼果子")
    # 3.3 调用父类的功能
    def make_master_cake(self):
        # Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

if __name__ == '__main__':
    td = Prentice()
    print(td.kongfu)
    td.make_cake()
    td.make_master_cake()
    td.make_cake()