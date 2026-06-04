"""
多进程目的：
    它属于多任务的一种实现方式，目的是充分利用CPU资源，提高程序执行效率

实现方式：
    1. 导包
    2. 创建进程对象，关联目标函数
    3. 启动进程
"""

from multiprocessing import Process
import time

# 定义函数 表示编写代码
def coding():
    for i in range(1,11):
        time.sleep(0.1) # 可以模拟耗时操作，更好的查看多任务的执行效果
        print(f"正在敲 第{i} 遍代码...")

# 定义函数，表示听音乐
def music():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在听 第{i} 遍音乐...")

# 创建2个进程对象，分别关联上述的两个 目标函数
if __name__ == '__main__':

    # 单任务
    # coding()
    # music()

    p1 = Process(target=coding)
    p2 = Process(target=music)

    p1.start()
    p2.start()
