"""
案例：多层继承
多层继承解释：
    类A继承类B，类B继承C，这就是多层继承
目前题设中的继承体系
Object <- Master、School  <- Prentice <- TuSun
"""
# 故事5：N年后，小明老了，想要把“有自己的独立品牌，也有黑马配方技术的煎饼果子味道”的所有技术传授给自己的徒弟。

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
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

class TuSun(Prentice):
    pass

if __name__ == '__main__':
    # 创建徒孙对象
    ts = TuSun()
    ts.make_cake()  # Prentice类的
    ts.make_master_cake() # Master类的
    ts.make_school_cake() # School类的 