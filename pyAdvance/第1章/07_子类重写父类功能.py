"""
重写解释：
概述： 重写也叫覆盖，即：子类出现和父类重名的属性或者行为，称之为：重写
调用层次： 遵循 就近原则，子类有就用，没有就去就近的父类找，依次查找其所有的父类，有就用，没有就报错
"""
# 故事3：小明掌握了老师傅和黑马的技术后，自己潜心钻研出一套自己的独门配方的全新摊煎饼果子技术。

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

if __name__ == '__main__':
    td = Prentice()
    print(td.kongfu)
    td.make_cake()