"""
小名同学当前体重是100kg，每当他跑步一次时，则会减少0.5kg,每当他大吃大喝一次时，则会增加2kg，
请试着采用面向对象方式完成案例

分析：
类名: Student
对象名: xm
属性(名词): 当前体重， current_weight
行为(动词): 跑步，吃饭
"""

class Student:
    def __init__(self, weight):
        self.current_weight = weight

    def run(self):
        self.current_weight -= 0.5

    def eat(self):
        self.current_weight += 2
    def __str__(self):
        return f"当前体重是{self.current_weight}kg"



#测试
if __name__ == '__main__':
    xm = Student(100)
    print(xm)
    xm.run()
    print(xm)
    xm.eat()
    print(xm)