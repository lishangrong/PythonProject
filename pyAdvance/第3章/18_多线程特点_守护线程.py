"""
案例：演示多线程特点之 守护线程
多线程特点：
    1. 线程之间执行时无序的,线程执行具有随机性，原因是因为CPU在作者高效的切换
    2. 默认情况下，主线程会等待所有子线程执行结束再结束  --->(可以使用守护线程来解决)
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
def work():
    for i in range(10):
        time.sleep(0.2)
        print(f"正在执行第{i}个线程")

# 2. 测试
if __name__ == '__main__':
    # 2.1 创建子线程对象
    # t = threading.Thread(target=work)
    # (守护线程)写法1， daemon=True
    # t = threading.Thread(target=work, daemon=True)

    # (守护线程)写法2， setDaemon()函数，已过时(新版中暂时还支持，以后的版本中可能会被移除掉)
    # t = threading.Thread(target=work)
    # t.setDaemon(True)

    # (守护线程)写法3， daemon 属性
    t = threading.Thread(target=work)
    t.daemon = True
    # 2.2 启动线程
    t.start()
    # 2.3 设置主线程休眠时间1秒
    time.sleep(1)
    print("主程序结束！！")
