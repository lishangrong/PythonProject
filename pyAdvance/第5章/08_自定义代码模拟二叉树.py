"""
抽取方法的快捷键：ctrl + alt + M  / command + option + M
"""
class Node:
    def __init__(self, item):
        self.item = item # 元素域
        self.lchild = None # 左子节点
        self.rchild = None # 右子节点

class BinaryTree:
    def __init__(self, node = None):
        self.root = node
    # 添加节点
    def add(self, item):
        # 1.把item封装成节点
        new_node = Node(item)
        # 2. 判断根节点是否为空，如果为空，设置当前节点为根节点
        if self.root is None:
            self.root = new_node
            return
        # 3. 创建队列，添加根节点到队列中
        queue = []
        queue.append(self.root)
        # 4. 通过 while True 死循环，找到空缺的节点位置
        while True:
            # 5. 获取队列的第一个元素
            node = queue.pop(0)
            # 6. 判断当前节点的左子节点是否为空，如果为空，则把当前节点的左子节点设置为当前节点
            if node.lchild is None:
                # 6.1 设置当前节点的左子节点为当前节点
                node.lchild = new_node
                return
            else:
                # 6.2. 若左子树不为空，添加 当前节点的左子节点 到队列中
                queue.append(node.lchild)
            # 7. 判断当前节点的右子节点是否为空，如果为空，则把当前节点的右子节点设置为当前节点
            if node.rchild is None:
                # 7.1 添加当前节点的右子节点
                node.rchild = new_node
                return
            else:
                # 7.2. 若右子树不为空，添加 当前节点的右子节点 到队列中
                queue.append(node.rchild)
    # 定义函数 breafth(),表示：广度优先遍历(逐层遍历，一层一层遍历)
    def breadth_travel(self):
        # 1.判断根节点是否为空
        if self.root is None:
            return
        # 2. 创建队列,添加 根节点 到队列中
        queue = []
        queue.append(self.root)
        # 3. 遍历队列，取出节点，并打印
        while len(queue) != 0:
            # 4. 获取队列的第一个元素
            node = queue.pop(0)
            # 5. 打印节点的元素域
            print(node.item, end=' ')
            # 6.判断当前节点的左子树是否存在，存在就添加到队列中
            if node.lchild is not None:
                queue.append(node.lchild)
            # 7.判断当前节点的右子树是否存在，存在就添加到队列中
            if node.rchild is not None:
                queue.append(node.rchild)
    # 定义函数 preorder(),表示：深度优先之先序遍历(根左右)
    def preorder(self, root):
        # 1. 判断根节点是否为空
        if root is not None:
            # 2. 打印根节点的元素域
            print(root.item, end=' ')
            # 3. 递归遍历左子树
            self.preorder(root.lchild)
            # 8. 递归遍历右子树
            self.preorder(root.rchild)

     # 定义函数 inorder(),表示：深度优先之中序遍历(左根右)
    def inorder(self, root):
        # 1. 判断根节点是否不为空
        if root is not None:
            # 2. 递归遍历左子树
            self.inorder(root.lchild)
            # 3. 打印根节点的元素域
            print(root.item, end=' ')
            # 4. 递归遍历右子树
            self.inorder(root.rchild)
    # 定义函数 postorder(),表示：深度优先之后序遍历(左右根)
    def postorder(self, root):
        # 1. 判断根节点是否不为空
        if root is not None:
            # 2. 递归遍历左子树
            self.postorder(root.lchild)
            # 3. 递归遍历右子树
            self.postorder(root.rchild)
            # 4. 打印根节点的元素域
            print(root.item, end=' ')

def dm01_test():
    # 1.创建节点
    node1 = Node('A')
    # 2.打印节点的元素域，左子树，右子树
    print(node1.item)  # A
    print(node1.lchild) # None
    print(node1.rchild) # None
    print('-' * 23)
    # 3. 测试二叉树
    # bt = BinaryTree() # 空
    # print(bt.root)   #None

    bt = BinaryTree(node1)
    print(bt.root)  # 根节点(的地址)
    print(bt.root.item) # 根节点的元素域


def dm02_queue():
    # 1.创建队列，特点：先进先出
    queue = []
    # 模拟往队列中添加元素
    queue.append('A')
    queue.append('B')
    queue.append('C')
    # 3. 模拟从队列中取出元素
    print(queue.pop(0))  # A 删除索引为0的元素，并返回元素，即模拟从 队列中获取 元素
    print(queue.pop(0))  # B
    print(queue.pop(0))  # C
    print(queue)


def dm03_广度优先遍历():
    bt = BinaryTree()
    bt.add('A')
    bt.add('B')
    bt.add('C')
    bt.add('D')
    bt.add('E')
    bt.add('F')
    bt.add('G')
    bt.add('H')
    bt.add('I')
    bt.add('J')
    bt.breadth_travel()


def dm04_深度优先遍历测试():
    # 1. 创建二叉树对象
    bt = BinaryTree()
    # 2. 添加节点
    bt.add(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)
    # 3.深度优先遍历
    print(f'先序(根左右):', end=' ')
    bt.preorder(bt.root)

    print(f'\n中序(左根右):', end=' ')
    bt.inorder(bt.root)

    print(f'\n后序(左右根):', end=' ')
    bt.postorder(bt.root)


if __name__ == '__main__':
    # dm01_test()
    # dm02_queue()
    # dm03_广度优先遍历()
    dm04_深度优先遍历测试()
