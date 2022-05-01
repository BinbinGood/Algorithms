class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.head = None


# 判断是否为搜索二叉树
def IsBST(head):
    if head is None:
        return True
    list1 = []
    process(head, list1)
    pre = -1
    for i in list1:
        if pre > i.value:
            return False
        pre = i.value
    return True


# 中序遍历生成一个列表
def process(head, inorderlist):
    if head is None:
        return
    process(head.left, inorderlist)
    inorderlist.append(head)
    process(head.right, inorderlist)


def IsBST3(head):
    if head:
        stack = []
        prevalue = -1
        while stack or head:
            if head:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                if head.value < prevalue:
                    return False
                else:
                    prevalue = head.value
                head = head.right
    return True


def CheckBST(head):
    global prevalue3
    if head is None:
        return True
    if CheckBST(head.left) is False:
        return False
    if head.value < prevalue3:
        return False
    else:
        prevalue3 = head.value
    return CheckBST(head.right)


# 使用树型DP问题解决此问题
class ReturnType():
    def __init__(self, isS, max, min):
        self.isSbt = isS
        self.max = max
        self.min = min


def IsSBT4(head):
    if head is None:
        return None
    left = IsSBT4(head.left)
    right = IsSBT4(head.right)
    min1, max1 = head.value, head.value
    if left is not None:
        min1 = min(min1, left.min)
        max1 = max(max1, left.max)
    if right is not None:
        min1 = min(min1, right.min)
        max1 = max(max1, right.max)
    curSBT = True
    if (left is not None) and ((left.isSbt is False) or (left.max >= head.value)):
        curSBT = False
    if (right is not None) and ((right.isSbt is False) or (right.min <= head.value)):
        curSBT = False
    return ReturnType(curSBT, min1, max1)


if __name__ == "__main__":
    bt1 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n6 = Node(6)
    n7 = Node(7)
    n3 = Node(3, n6, n7)
    bt1.head = Node(1, n2, n3)
    print("------第一棵树不是搜索二叉树-------")
    print("------递归中序遍历判断是否为搜索二叉树-----")
    print(IsBST(bt1.head))
    print("------非递归中序遍历判断是否为搜索二叉树-----")
    print(IsBST3(bt1.head))
    print("------递归方法二-----")
    prevalue3 = -1
    print(CheckBST(bt1.head))
    print("------树型DP方法-----")
    print(IsSBT4(bt1.head).isSbt)

    bt2 = BinaryTree()
    n1 = Node(1)
    n2 = Node(2, n1)
    n4 = Node(4)
    n3 = Node(3, n2, n4)
    n6 = Node(6)
    n7 = Node(7, n6)
    bt2.head = Node(5, n3, n7)
    print("------第二棵树是搜索二叉树-------")
    print("------递归中序遍历判断是否为搜索二叉树-----")
    print(IsBST(bt2.head))
    print("------非递归中序遍历判断是否为搜索二叉树-----")
    print(IsBST3(bt2.head))
    print("------递归方法二-----")
    prevalue3 = -1
    print(CheckBST(bt2.head))
    print("------树型DP方法-----")
    print(IsSBT4(bt2.head).isSbt)
