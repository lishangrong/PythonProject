"""
继承-重写：是指子类继承父类后，如果父类中的方法不满足需求，可以在子类中重新定义弗雷中已有的方法(方法名相同)，
从而用子类的视线替换父类的实现。
注意：如果子类在重写父类的方法时，需要调用父类的方法，可以通过
父类名.方法名(self) / super().方法名() 方式来调用
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
        self.__control_fuel()
    def stop(self):
        print(f"{self.brand} {self.model} 停止行驶...")
    # 私有方法
    def __control_fuel(self):
        print(f"{self.brand} {self.model} 正在控制油门...")

    def get_owner(self):
        return self.__owner[0:1] + "**"
    def charge(self):
        print(f"{self.brand} {self.model} 正在补充燃料...")

# 燃油车
class FuelCar(Car):
    def charge(self):
        print(f"{self.brand} {self.model} 正在加油...")

# 电车
class ElectricCar(Car):
    def charge(self):
        # 调用父类的charge方法
        # super().charge()  # 方式1
        Car.charge(self) # 方式2
        print(f"{self.brand} {self.model} 正在充电...")

if __name__ == "__main__":
    c1 = FuelCar("蓝色", "BMW", "X5", "张三")
    c1.charge()

    c2 = ElectricCar("红色", "比亚迪", "X5", "李四")
    c2.charge()