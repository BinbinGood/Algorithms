class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.head = None


# 宽度优先遍历
def WidthTraversal(head):
    if head:
        queue = [head]
        while queue:
            head = queue.pop(0)  # pop(0)表示先进先出
            print(head.value)
            if head.left:
                queue.append(head.left)
            if head.right:
                queue.append(head.right)


# 求二叉树最大宽度，使用哈希表的方法
def MaxWidth(head):
    if head:
        queue = [head]
        hashmap = {head: 1}
        curlevel = 1
        curlevelnodes = 0
        maxnodes = -1
        while queue:
            head = queue.pop(0)  # pop(0)表示先进先出
            curnodelevel = hashmap[head]
            if curnodelevel == curlevel:
                curlevelnodes += 1
            else:
                curlevel += 1
                curlevelnodes = 1
            maxnodes = max(maxnodes, curlevelnodes)
            if head.left:
                hashmap[head.left] = curlevel + 1
                queue.append(head.left)
            if head.right:
                hashmap[head.right] = curlevel + 1
                queue.append(head.right)
        print(maxnodes)


if __name__ == "__main__":
    bt1 = BinaryTree()
    n5 = Node(5)
    n8 = Node(8)
    n4 = Node(4, n8, n5)
    n9 = Node(9)
    n6 = Node(6, None, n9)
    n2 = Node(2, n4, n6)
    n10 = Node(10)
    n7 = Node(7, None, n10)
    n3 = Node(3, n7, None)
    bt1.head = Node(1, n2, n3)
    print("--------宽度优先遍历---------")
    WidthTraversal(bt1.head)
    print("--------求二叉树最大宽度---------")
    MaxWidth(bt1.head)
