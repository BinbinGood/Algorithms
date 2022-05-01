# 二叉树每个结点都有一个int型权值，给定一棵二叉树，要求计算出从根结点到
# 叶结点的所有路径中，权值和最大的值为多少。
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def Maxvalue1(head):
    if head is None:
        return 0
    return process(head)


def process(node):
    if node.left and node.right:
        return node.value + max(process(node.left), process(node.right))
    elif node.left:
        return node.value + process(node.left)
    elif node.right:
        return node.value + process(node.right)
    else:
        return node.value


def Maxvalue2(head):
    if head is None:
        return 0



if __name__ == "__main__":
    headnode = Node(1)
    headnode.left = Node(2)
    headnode.left.left = Node(4)
    headnode.left.right = Node(7)
    headnode.left.left.left = Node(9)
    headnode.left.right.right = Node(1)
    headnode.right = Node(5)
    headnode.right.left = Node(3)
    headnode.right.right = Node(8)
    headnode.right.left.left = Node(2)
    headnode.right.right.right = Node(7)
    print(Maxvalue1(headnode))
