"""
继承：描述的是两个类之间的关系，子类继承父类，就可以获取到父类中的属性和方法（非私有）
语法:
class 子类名(父类名):
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

# 燃油车
class FuelCar(Car):
    pass

# 电车
class ElectricCar(Car):
    pass

if __name__ == "__main__":
    c1 = FuelCar("蓝色", "BMW", "X5", "张三")
    print(c1.model)
    print(c1.brand)
    print(c1.color)

    c1.start()
    c1.run()
    c1.stop()
    c1.get_owner()