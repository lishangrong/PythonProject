"""

class A(B):
    pass
叫法：
    A：子类，派生类
    B：父类，基类，超类
好处：
    提高代码的复用性
弊端：
    耦合性增强了，父类不好的内容，子类想没有都不行
扩展：开发原则
    高内聚，低耦合
    内聚：指的是类自己独立处理问题的能力
    耦合：指的是类与类之间的关系
    大白话解释：自己能搞定的事儿，就不要麻烦别人

"""
# 需求，定义父类(男，散步)，定义子类，继承父类
class Father:
    def __init__(self):
        self.gender = "男"
    def walk(self):
        print("饭后走一走，活到九十九")
    def smoking(self):
        print("抽烟有害，健康")

# 定义子类
class Son(Father):
    pass

son = Son()
print(f'性别: {son.gender}')
son.walk()