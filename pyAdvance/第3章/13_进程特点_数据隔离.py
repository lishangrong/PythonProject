"""
进程的特点：
    1.进程之间数据是相互隔离的
        因为子进程相当于父进程的"副本"，会将父进程的"main外资源"拷贝一份，即：各是各的
    2.默认情况下，主进程会等待子进程执行借书在结束
"""
import multiprocessing
import time

# 需求：定义一个共同的容器my_list = [], 一个进程往里写数据，一个进程从里读数据，看是否读取到

my_list = []
def write_data():
    for i in range(1, 6):
        time.sleep(0.1)
        my_list.append(i)
        print(f"添加数据：{i}")
    print(f'write_data函数：{my_list}')

def read_data():
    time.sleep(0.1)
    print(f'read_data函数：{my_list}')


print('我是main外资源，看我执行了几次')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data)
    p1.start()
    p2.start()
    print('我是main内资源，看我执行了几次')