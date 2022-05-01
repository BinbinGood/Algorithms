class Node():
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class BinaryTree():
    def __init__(self):
        self.head = None


# 后继节点是中序遍历当前节点的下一个节点
def getSuccessorNode(nod):
    if nod is None:
        return nod
    if nod.right:
        return getmaxleft(nod.right)  # 右树上的最左节点
    else:  # 无右子树
        parent = nod.parent
        while parent and parent.left != nod:  # 当前节点是你父亲的右孩子  # 此条件兼顾了此节点为整棵树的最优节点
            nod = parent
            parent = nod.parent
        return parent


def getmaxleft(nod):
    if nod is None:
        return nod
    while nod.left:  # 一路往左走，找到右子树的最左节点
        nod = nod.left
    return nod


if __name__ == "__main__":
    bt1 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n7 = Node(7)
    n6 = Node(6)
    n3 = Node(3, n6, n7)
    bt1.head = Node(1, n2, n3)
    n2.parent = bt1.head
    n3.parent = bt1.head
    n4.parent = n5.parent = n2
    n6.parent = n7.parent = n3
    if getSuccessorNode(n7) is None:
        print("None")
    else:
        print(getSuccessorNode(n7).value)
