# 求完全二叉树的节点个数

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def mostLeftnode(node, level):
    while node:
        level += 1
        node = node.left
    return level - 1


def treeNodeSums(head):
    if head is None:
        return 0
    return process(head, 1, mostLeftnode(head, 1))


def process(node, curlevel, sumlevel):
    if curlevel == sumlevel:
        return 1
    if mostLeftnode(node.right, curlevel + 1) == sumlevel:
        return (1 << (sumlevel - curlevel)) + process(node.right, curlevel + 1, sumlevel)
    else:
        return (1 << (sumlevel - curlevel - 1)) + process(node.left, curlevel + 1, sumlevel)


if __name__ == "__main__":
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.left.left.left = Node(8)
    head.left.left.right = Node(9)
    head.left.right.left = Node(10)
    head.left.right.right = Node(11)
    head.right.left = Node(6)
    head.right.right = Node(7)
    head.right.left.left = Node(12)
    head.right.left.right = Node(13)
    print(treeNodeSums(head))
