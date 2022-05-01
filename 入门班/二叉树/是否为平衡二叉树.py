class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.head = None


class ReturnType():
    def __init__(self, isB, hei):
        self.balenced = isB
        self.height = hei


def IsBBT(head):
    if head is None:
        return ReturnType(True, 0)
    left = IsBBT(head.left)
    right = IsBBT(head.right)
    if left.balenced and right.balenced and (abs(left.height - right.height) < 2):
        return ReturnType(True, max(left.height, right.height)+1)
    else:
        return ReturnType(False, max(left.height, right.height)+1)


if __name__ == "__main__":
    bt1 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n7 = Node(7)
    n6 = Node(6, n7)
    n3 = Node(3, n6)
    bt1.head = Node(1, n2, n3)
    print("----树1是否为平衡二叉树-----")
    print(IsBBT(bt1.head).balenced)
    bt2 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n7 = Node(7)
    n3 = Node(3, None, n7)
    bt2.head = Node(1, n2, n3)
    print("----树2是否为平衡二叉树-----")
    print(IsBBT(bt2.head).balenced)
