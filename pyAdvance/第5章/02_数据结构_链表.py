"""
数据结构分类：
    线性结构：
        顺序表：栈、队列
            一站式存储：数据区，信息区
            分离式存储
        链表：自定义代码模拟 链表
    非线形结构：
        树，图

线性结构之链表：
    概述： 它属于数据结构之 线性结构的一种，每个节点都只能有1个前驱和一个后继节点
    作用：用于优化顺序标的弊端(如果没有足够的连续的内存空间，会导致扩容失败)
    组成：由 节点 组成，其中 节点由 元素域（数值域）和 链接域（地址域）组成。
    分类：根据节点类型不同，链表主要分为：
        单向链表：节点由 1个数值域 和 1个地址域组成，前边节点的地质域存储的是后续节点的地址，最后1个节点的地址域为None
        单向循环链表：
        双向链表： 地质域，数值域，地址域
        双向循环链表：

元素域item用来存放具体的数据
链接域next用来存放下一个节点的位置
变量head指向链表的头结点(首节点)的位置，从head触发能找到表中的任意节点。
"""

# 自定义代码模拟链表，思路分析：
# 1. 自定义SingleNode类，表示 节点类
#     属性：item(数值域), next(地址域)
# 2.自定义SingleLInkedList 类，表示 链表
#     属性：head(头结点)， 指向第1个节点
#       行为：
#             is_empty(self)  判断链表是否为空
#             length(self)  获取链表长度的
#             travel(self)  遍历链表
#             add(self, item)  在链表头部添加元素
#             append(self, item)  在链表尾部添加元素
#             insert(self, pos, item)  在指定位置添加元素
#             remove(self, item) 删除节点
#             search(self, item)  查找节点是否存在


class SingleNode:
    """单链表的节点"""
    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None

class SingleLinkedList:
    """单链表"""
    def __init__(self, node=None):
        # head是链表的头，初始时没有节点
        self.head = node
    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None
    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.head
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            # 移动到下一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur is not None:
            print(f'数值域: {cur.item}')
            cur = cur.next

    def add(self, item):
        """在链表头部添加元素"""
        new_node = SingleNode(item)
        # 设置新节点的地质域指向头结点
        new_node.next = self.head
        # 设置头结点为新节点
        self.head = new_node

    def append(self, item):
        """在链表尾部添加元素"""
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    def insert(self, pos, item):
        """在指定位置添加元素"""
        # 判断索引是否越界，如果<=0 则添加到链表头部
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            cur = self.head
            count = 0
            # 循环查找，找到指定位置的前一个节点
            while count < pos - 1:
                count += 1
                cur = cur.next
            # 插入节点
            new_node = SingleNode(item)
            new_node.next = cur.next
            cur.next = new_node
        pass

    def remove(self, item):
        """删除节点"""
        # 创建游标
        cur = self.head
        # 记录要删除的节点的 前驱节点
        pre = None
        while cur is not None:
            # 找到待删除节点的前一个节点
            if cur.item == item:
                # 删除节点是否是头结点
                if cur == self.head:
                    self.head = cur.next
                else:
                    # 直接设置 前驱节点的地址域 指向 当前节点的地质域
                    pre.next = cur.next
                    cur.next = None  # 删除节点，断开链接
                return
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    # node1 = SingleNode(10)
    # print(f'元素域(数值域)：{node1.item}')   # 10
    # print(f'链接域(地址域)：{node1.next}')  # None
    # print(f'node1对象：{node1}')         # 地址域，可以重写 str 魔法方法
    # print(f'node1对象类型：{type(node1)}')
    #
    # # my_linkedlist = SingleLinkedList()
    # my_linkedlist = SingleLinkedList(node1)
    # print(f'头结点为：{my_linkedlist.head}')
    # print(f'头结点的元素域(数值域)为：{my_linkedlist.head.item}')  # 10
    # print(f'头结点的链接域(地址域)为：{my_linkedlist.head.next}') # None


    my_linkedlist = SingleLinkedList(SingleNode('乔峰'))
    my_linkedlist.add('虚竹')
    my_linkedlist.add('段誉')

    my_linkedlist.append('王语嫣')
    my_linkedlist.append('木婉清')

    my_linkedlist.insert(3, '小昭')
    my_linkedlist.insert(10, '尹志平')
    my_linkedlist.insert(2, '阿朱')

    # 删除元素
    my_linkedlist.remove('段誉')
    my_linkedlist.remove('尹志平')
    my_linkedlist.remove('阿朱')

    print(f'链表是否包含小昭：{my_linkedlist.search("小昭")}')

    print(f'链表长度为：{my_linkedlist.length()}')

    my_linkedlist.travel()

