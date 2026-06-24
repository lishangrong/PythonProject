"""
选择排序：
    工作原理：
        从 待排序的数据元素 中选出最小(或最大)的一个元素，存放在 序列的起始位置，
    要点：
        1.比较的总轮数：列表长度-1
        2.每轮比较的总次数： i+ 1, 列表长度
        3.谁和谁比较(交换)： i 和 min_index 位置的元素  a,b = b,a
    流程：假设共5个元素
        第几轮(索引)    公式(具体的谁和谁比较)   该轮比较的总次数
        第1轮(索引：0)， 0 和 1，2，3，4 比较   共4次
        第2轮(索引：1)， 1和2，3，4比较,        共3次
        第3轮(索引：2)， 2和3，4比较,           共2次
        第4轮(索引：3)， 3和4比较,              共1次
"""
def select_sort(alist):
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
            print("第%d轮：%d和%d比较"%(i+1, i, min_index))
            alist[i], alist[min_index] = alist[min_index], alist[i]


if __name__ == '__main__':
    my_list = [54,26,93,17,77,31,44,55,20]
    select_sort(my_list)
    print(my_list)