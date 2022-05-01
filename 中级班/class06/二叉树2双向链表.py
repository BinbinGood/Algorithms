# 双向链表节点结构和二叉树节点结构是一样的，如果你把last认为是left，
# next认为是right的话。
# 给定一个搜索二叉树的头节点head，请转化成一条有序的双向链表，并返回链
# 表的头节点。

class ReturnType:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end


def convert2(head):
    if head is None:
        return None
    return tree2List(head).start


def tree2List(head):
    if head is None:
        return ReturnType(None, None)
    leftheadend = tree2List(head.left)
    rightheadend = tree2List(head.right)
    if leftheadend.end is not None:
        leftheadend.end.right = head
    head.left = leftheadend.end
    head.right = rightheadend.start
    if rightheadend.start is not None:
        rightheadend.start.left = head
    return ReturnType(leftheadend.start if (leftheadend.start is not None) else head,  # 考虑左右子树其中一个为空的情况
                      rightheadend.end if (rightheadend.end is not None) else head)


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# 中序打印二叉树
def inorderprint(head):
    if head is None:
        return
    inorderprint(head.left)
    print(head.value, end=' ')
    inorderprint(head.right)


def printlist(head):
    if head is None:
        return
    print("--正向打印--")
    pre = None
    while head:
        print(head.value, end=' ')
        pre = head
        head = head.right
    print()
    print('--反向打印--')
    while pre:
        print(pre.value, end=' ')
        pre = pre.left


if __name__ =="__main__":
    head = Node(5)
    head.left = Node(2)
    head.right = Node(9)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.left.right.right = Node(4)
    head.right.left = Node(7)
    head.right.right = Node(10)
    head.right.left.left = Node(6)
    head.right.left.right = Node(8)
    print("----------中序遍历二叉树----------")
    inorderprint(head)
    print()
    print("----------打印双向链表----------")
    head = convert2(head)
    printlist(head)
