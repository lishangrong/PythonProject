"""
多继承
需求：
故事2：小明是个爱学习的好孩子，想学习更多的摊煎饼果子技术，于是，在百度搜索到黑马程序员学校，报班来培训学习摊煎饼果子技术。

扩展： MRO机制
    解释：
        Python中有MRO机制，可以查看某个对象，在调用函数时的顺序，即，先找哪个类，后找哪个类
    格式:
        类名.mro()
        类名.__mro__
"""

class Master:
    def __init__(self):
        self.kongfu = '[古法配方]'

    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼果子")

class School:
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼果子")

# 定义子类，
class Prentice(School,Master): #从左到右，就近原则
    pass

xm = Prentice()
xm.make_cake()
print('-' * 23)
# 查看mro机制的结果
print(Prentice.mro()) # Prentice -> School -> Master -> object
print(Prentice.__mro__) # Prentice -> School -> Master -> object
