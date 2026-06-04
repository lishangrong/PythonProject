"""
案例：演示多线程共享全局变量，可能出现的问题。

多线程共享全局变量，出现问题的问题：
    累加次数不够

产生原因：
    线程1还没有来得及执行完(一个完整的动作)前，被线程2抢走了资源，就可能出问题

解决方案：
    加锁思想，即：互斥锁
    线程同步(加锁)：保证同一时刻 只能 有一个线程去操作全局变量、
    线程同步的方式：锁

细节：
    使用互斥锁的时候，要在合适的实际释放锁，否则可能出现 死锁(忘记释放) 或者 锁不住的情况(使用2把锁)

互斥锁：对共享数据进行锁定，保证同一时刻只有一个线程去操作
注意：互斥锁是多个线程一起抢，抢到锁的线程先执行，没抢到锁的线程进行等待，等锁使用完释放后，其他等待的线程再去抢这个锁。

互斥锁使用流程:
1. 互斥锁的创建
mutex = threading.Lock()
2. 上锁
mutex.acquire()
3. 释放锁
mutex.release()

死锁：一直等待对方释放锁的情景
死锁的原因：使用互斥锁的时候需要注意思索的问题，未在合适的地方注意释放锁
死锁的结果：会造成应用程序的停止响应，应用程序无法继续往下执行了

进程和线程的区别：
    1.线程依赖进程
    2.进程更消耗资源，不能共享全局变量，相对稳定
    3.线程更轻量级，可以共享全局变量，相对更灵活

"""
# 需求：定义两个函数，分别对全局变量累加100w次，创建2个线程，关联这两个函数，执行看效果

import threading
# 1. 定义全局变量
global_num = 0

# 创建线程锁
mutex_lock = threading.Lock()

# 2. 定义目标函数1，对全局变量累加100w次
def target_fun1():
    mutex_lock.acquire() # 加锁
    # 2.1 声明全局变量
    global global_num
    # 2.2 循环累加
    for i in range(1000000):
        global_num += 1
    print(f'target_fun1 函数结果：{global_num}')
    mutex_lock.release() # 释放锁

# 3. 创建目标函数2，对全局变量累加100w次
def target_fun2():
    mutex_lock.acquire() # 加锁
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'target_fun2 函数结果：{global_num}')
    mutex_lock.release() # 释放锁

# 测试
if __name__ == '__main__':
    # 1. 创建进程对象
    p1 = threading.Thread(target=target_fun1)
    p2 = threading.Thread(target=target_fun2)
    # 2. 启动进程
    p1.start()
    p2.start()
