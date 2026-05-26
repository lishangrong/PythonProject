"""
多继承：指的是一个子类，同时继承了多个父类的情况(会将多个父类中的非私有属性和方法都继承下来)
语法：
class 子类名(父类名1, 父类名2, 父类名3, ...):

注意：当一个类继承了多个父类时，默认有限使用第一个父类中的同名属性或方法，可以使用
类名.__mro__属性 或 类名.mro() 方法查看调用顺序
"""


class Car:
    def __init__(self, color, brand, model, owner):
        self.color = color # 颜色
        self.brand = brand # 品牌
        self.model = model # 型号

        self.__owner = owner # 所有者(私有属性)

    def start(self):
        print(f"{self.brand} {self.model} 正在启动...")

    def run(self):
        print(f" {self.__owner} {self.brand} {self.model} 启动成功，正在行驶...")

    def stop(self):
        print(f"{self.brand} {self.model} 停止行驶...")

    def get_owner(self):
        return self.__owner[0:1] + "**"

    def charge(self):
        print(f"{self.brand} {self.model} 正在补充燃料...")

# 华为智驾
class HuaweiAiDriving:
    def __init__(self,version="V1.0"):
        self.version = version
    def run(self):
        print(f"使用华为AI智能驾驶系统{self.version}正在行驶...")



# 问界汽车
class WenJieCar(Car, HuaweiAiDriving):
    # 需要使用多个父类属相时，可自定义init方法
    def __init__(self, color, brand, model, owner, version):
        # super().__init__(color, brand, model, owner)
        Car.__init__(self, color, brand, model, owner)
        HuaweiAiDriving.__init__(self, version)

    # run方法，需要执行每个父类中的run方法时
    def run(self):
        Car.run(self)
        HuaweiAiDriving.run(self)

# MRO原则：Method Resolution Order ----> 方法解析顺序
if __name__ == "__main__":
    # c1 = WenJieCar("蓝色", "BMW", "X5", "张三")
    # 查看调用顺序
    # print(WenJieCar.__mro__)
    # print(WenJieCar.mro())
    c = WenJieCar("蓝色", "BMW", "X5", "张三", "V1.0")
    print(c.__dict__)
    c.run()