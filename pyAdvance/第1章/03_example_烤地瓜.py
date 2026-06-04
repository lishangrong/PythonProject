"""
地瓜被烤地瓜    对应的地瓜生熟状态
0-3分钟        生的
3-7分钟       半生不熟
7-12分钟      熟了
超过12分钟     已烤焦，糊了

添加的调料： 用户可以按自己的意愿添加调料


分析：
类名: SweetPotato
对象名: xm
属性(名词): 被烤时间 cook_time, 被烤状态 cook_state, 调料 condiments
行为(动词): 烘烤 cook(), 添加调料 add_condiment()
魔法属性： init() ---> 初始化属性, str() ---> 打印地瓜信息
规则：
烘烤时间   地瓜状态
[0, 3)    生的    包左不包右
[3, 7)    半生不熟
[7, 12)   熟了
[12, ∞]   糊了
"""

class SweetPotato:
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiments = []

    def cook(self, time):
        if self.cook_time < 0:
            print('无效值，你是火星来的吧！')
        else:
            self.cook_time += time
            if 0 <= self.cook_time < 3:
                self.cook_state = '生的'
            elif 3 <= self.cook_time < 7:
                self.cook_state = '半生不熟'
            elif  7 <= self.cook_time < 12:
                self.cook_state = '熟了'

    def add_condiment(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'烘烤时间：{self.cook_time}，地瓜状态：{self.cook_state}，调料：{self.condiments}'

#测试
if __name__ == '__main__':
    # 创建地瓜对象
    dg = SweetPotato()
    # 具体的烘烤动作
    dg.cook(5)
    dg.cook(3)
    # 添加调料
    dg.add_condiment('辣椒')
    dg.add_condiment('芥末')
    dg.add_condiment('鱼腥草')
    dg.add_condiment('折耳根')
    # 打印地瓜状态
    print(dg)