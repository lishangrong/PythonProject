"""
封装：将数据(属性)和操作数据的方法绑定在一起，形成一个独立的单元(类)，保护数据不被外部访问，通过访问修饰符实现封装。
1. 私有属性：在属性明前加双下划线__
2. 私有方法：在方法名前加双下划线__
注意事项：Python中是没有真正的私有化机制的，都是约定
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

if __name__ == "__main__":
    car = Car("蓝色", "BMW", "X5", "张三")
    # print(car.brand)
    # print(car.model)
    # print(car.color)
    # print(car.__owner)

    # python中无真正的私有化机制
    print(car._Car__owner)
    car._Car__control_fuel()

    # car.start()
    # car.run()
    # car.stop()
    # car.__control_fuel()
    # print(car.get_owner())