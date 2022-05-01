class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.head = None


class ReturnType():
    def __init__(self, isF, hei, nod):
        self.isFBT = isF
        self.height = hei
        self.nodes = nod


def IsFBT(head):
    if head is None:
        return ReturnType(True, 0, 0)
    left = IsFBT(head.left)
    right = IsFBT(head.right)
    curheight = left.height + 1
    curnodes = left.nodes + right.nodes + 1
    curisFBT = True
    if (left.isFBT is False) or (right is False) or (left.height != right.height):
        curisFBT = False
    if curnodes != (1 << curheight) - 1:
        curisFBT = False
    return ReturnType(curisFBT, curheight, curnodes)


if __name__ == "__main__":
    bt1 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n7 = Node(7)
    n6 = Node(6)
    n3 = Node(3, n6, n7)
    bt1.head = Node(1, n2, n3)
    print("----树1是否为满二叉树-----")
    print(IsFBT(bt1.head).isFBT)
    bt2 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n7 = Node(7)
    n3 = Node(3, None, n7)
    bt2.head = Node(1, n2, n3)
    print("----树2是否为满二叉树-----")
    print(IsFBT(bt2.head).isFBT)
