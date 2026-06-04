"""
进程的特点：
    1.进程之间数据是相互隔离的
        因为子进程相当于父进程的"副本"，会将父进程的"main外资源"拷贝一份，即：各是各的
    2.默认情况下，主进程会等待子进程执行借书在结束
        如果要设置主进程结束，子进程同步结束，方式如下：
            思路1：设置子进程为 守护进程
            思路2： 强制关闭子进程。 可能会导致子进程变成僵尸，交由Python 计时器自动回收(底层有 init初始化进程来管理维护)
"""
import multiprocessing
import time

def work():
    for i in range(10):
        print("正在努力工作中...")
        time.sleep(0.2)



if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work)
    # 思路1：设置为守护进程
    # p1.daemon = True  # 设置p1为：守护进程
    p1.start()
    # 主进程休眠1秒
    time.sleep(1)
    # 思路2 强制关闭子进程
    p1.terminate()
    print("main进程结束！")