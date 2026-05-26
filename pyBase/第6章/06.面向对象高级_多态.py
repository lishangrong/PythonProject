"""
多态：是指同一个方法，具有不同的形态、行为、表现。

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
        print(f"{self.brand} {self.model} 正在充电...")

# 补充燃料函数
def handle_charge(car:Car): # 函数参数类型声明 --- 指定的是父类型
    car.charge()


# 测试代码
if __name__ == "__main__":
    handle_charge(FuelCar("蓝色", "BMW", "X5", "张三"))
    handle_charge(ElectricCar("白色", "比亚迪", "X5", "张三"))
