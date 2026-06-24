"""
快速排序： 通过多次比较和交换来实现排序
流程：
1.首先设定一个 分界值，通过该分界值将数组分成 左右两部分
2.将大于或等于分界值的数据集中到数组右边，小于分界值的数据集中到数组的左边
3.然后，左边和右边的数据可以独立排序。
对于左侧的数据又可以取一个分界值，将该部分数据分成左右两部分，同样在左边放置较小值，右边放置较大值。右侧的数组数据也做类似处理
4.重复上述过程，可以看出，这是一个递归定义。通过递归将左侧部分排好序后，再递归排好右侧部分的顺序。
当左、右两个部分各个数据排序完成后，整个数组的排序也就完成了。

大白话解释：
第1轮：1个分界值， 假设第1个元素为分界值，次数：比该分界值小的都放在左边，比该分界值大于或者等于 放右边。   小  分界 大
第2轮：2个分界值，上一轮分界值左边数据 找个分界值。 上一轮分界值右边数据 找个分界值
第3轮：4个分界值 ......以此类推

递归思想：每次需要传入：列表、起始位置、结束位置
最优收件复杂度: O(nlog n)

"""
from pip._internal.resolution import legacy


# 1. 定义函数 quick_sort, 实现：对列表元素 升序排序
def quick_sort(alist, start, end):
    """
    快速排序思路：实现对列表元素排序
    :param alist: 要操作的列表
    :param start: 操作的数据，起始索引
    :param end: 操作的数据，结束索引
    :return:
    """
    # 核心细节： start >= end 递归结束，说明排好序了
    if start >= end:
        return
    # 1.1 定义变量 left 和 right，分别表示：分界值左、右的索引
    left = start
    right = end
    # 1.2 定义变量mid, 表示：分界值，假设列表的起始值为分界值
    mid = alist[start]
    # 1.3 具体的查找过程，只要 left 比 right 小，就继续查找
    while left < right:
        # 1.4 把分界值右边的数据，依次和分界值进行比较，如果比分界值小，放分界值左侧
        # 1.4.1 循环操作，只要分界值右侧的数据比分界值大，，right 就 -1， 直至循环结束
        while alist[right] >= mid and left < right:
            right -= 1
        # 1.4.2 alist[right] < mid, 放左侧
        alist[left] = alist[right]
        # 1.5  把分界值左边，比分界值大的数据，放分界值右边
        # 1.5.1 循环操作，只要分界值侧左侧的数据比比分界值小，left 就 +1， 直至循环结束
        while alist[left] < mid and left < right:
            left += 1
        # 1.5.2 alist[left] > mid, 放右侧
        alist[right] = alist[left]
    # 1.6 循环结束，即：分界值的位置已经找到，赋值即可。left 和 right 相等，此时，left 和 right 指向的元素，就是分界值
    alist[left] = mid

    # 1.7 递归方式，处理分界值左侧的数据，找个分界值，继续操作
    quick_sort(alist, start, left-1)
    # 1.8 递归方式，处理分界值右侧的数据，找个分界值，继续操作
    quick_sort(alist, right+1, end)

if __name__ == '__main__':
    my_list = [54,26,93,17,77,31,44,55,20]
    quick_sort(my_list, 0, len(my_list)-1)
    print(f'排序后: {my_list}')