"""
二分查找（递归版）：
    概念：属于查找类算法，相对效率较高，时间复杂度: O(log n)
        又叫折半查找，它是一种效率较高的查找方法。
    前提：列表必须是有序的
    原理：将数组分为3部分，依次是 中值前，中值，中值后
         将要 查找的值与中值进行比较，若小于中值则在中值前面找，若大于中值则在中值后面找，等于中值时直接返回
        假设列表是 升序的
        1.比较 要查找的元素 和列表的中值， 如果一样就返回True,程序结束。
        2.如果 查找的元素 比 中值小，去前半段(中值前) 查找。
        3.如果 查找的元素 比 中值大，去后半段(中值后) 查找。
        4.重复上述动作，直至找完。如果都找完了，还找不到，就返回False

"""
# 定义函数 binary_search_recursion(), 表示 二分查找

# 递归版
def binary_search_recursion(alist, target):
    """
    该函数时二分查找的递归版，实现查找指定元素是否在列表中
    :param alist: 待查找的列表
    :param target: 要查找的元素
    :return: True:在,False:不在
    """
    n = len(alist)
    if n == 0:
        return False
    mid = n // 2
    if alist[mid] == target:
        return True
    elif alist[mid] > target:
        return binary_search_recursion(alist[:mid], target)
    else:
        return binary_search_recursion(alist[mid+1:], target)
    # 走到这里，说明列表已经遍历完，没找到
    return False

# 非递归版
def binary_search(alist, target):
    # 定义变量 start，end, 分别表示列表的开始 和结束索引
    start = 0
    end = len(alist) - 1
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == target:
            return True
        elif alist[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search_recursion(my_list, 5))
    print(binary_search_recursion(my_list, 15))
    print('-' * 23)
    print(binary_search(my_list, 5))
    print(binary_search(my_list, 15))