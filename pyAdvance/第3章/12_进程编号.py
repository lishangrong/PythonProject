"""
进程的编号解释：
    概述：
        在设备中，每个程序(进程)都有自己的唯一进程Id，当程序释放的时候，该进程Id也会释放。即：进程Id是可以重复使用的。
    目的：
        1.查看子进程和父进程的关系，方便管理
        2. 例如：杀死指定进程，创建子进程....
    格式：
    查看当前进程的pid：
        os模块(operating，系统模块) 的 getpid()   get Process id
        multiprocessing#current_process() 的pid 属性
    查看当前进程的ppid  parent process id(父进程id)
        os#getppid()
细节：
    main 中创建的进程，如果灭有特殊指定，ta的父进程都是main进程，
    而main进程的父进程是 Pycharm的pid
进程编号的作用
    进程编号 唯一标识一个进程，方便管理进程。
    在一个操作系统中，一个进程拥有的进程号是唯一的，进程号可以反复使用。
获取进程编号的目的是验证主进程和子进程的关系，可以得知 子进程是有哪个主进程创建出来的

获取进程编号的两种操作：
1.获取当前进程编号
2.获取当前父进程编号
"""


import os
import multiprocessing
import time

# 定义函数 表示编写代码
def coding(name, num):
    for i in range(1,num + 1):
        time.sleep(0.1) # 可以模拟耗时操作，更好的查看多任务的执行效果
        print(f"{name}正在敲 第{i} 遍代码...")
    print(f'p1进程的Id：{os.getpid()}, {multiprocessing.current_process().pid},父进程Id：{os.getppid()}')

# 定义函数，表示听音乐
def music(name, count):
    for i in range(1,count + 1):
        time.sleep(0.1)
        print(f"{name}正在听 第{i} 遍音乐...")
    print(f'p2进程的Id：{os.getpid()}, {multiprocessing.current_process().pid},父进程Id：{os.getppid()}')

# 创建2个进程对象，分别关联上述的两个 目标函数
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding, args=("虚竹", 10))
    p2 = multiprocessing.Process(target=music, kwargs={"name": "刘备", "count": 20})

    p1.start()
    p2.start()

    # 查看主进程的信息
    print(f'main进程的Id：{os.getpid()}, {multiprocessing.current_process().pid},父进程Id：{os.getppid()}')