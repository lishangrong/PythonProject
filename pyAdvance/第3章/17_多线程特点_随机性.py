"""
多线程特点：
    1. 线程之间执行时无序的,线程执行具有随机性，原因是因为CPU在作者高效的切换
    2. 默认情况下，主线程会等待所有子线程执行结束再结束
    3. (同一个进程)线程之间共享全局变量
    4. 多线程操作之间共享数据，可能会出现出现安全问题，可以用 互斥锁解决

CPU调度资源的策略
    1.
    2.
"""

#需求： 创建多个线程，多次运行，观察结果
import threading
import time

# 1. 定义对线程的目标函数
def print_info():
    # 1.1 休眠
    time.sleep(0.2)
    #1.2 获取当前线程对象
    current_thread = threading.current_thread()
    # 1.3 打印当前线程的名字
    print(current_thread.name)

# 2. 测试
if __name__ == '__main__':
    # 2.1 创建10个线程，观察其运行结果
    for i in range(10):
        t = threading.Thread(target=print_info)
        t.start()