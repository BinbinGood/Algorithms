# 一棵二叉树原本是搜索二叉树，但是其中有两个节点调换了位置，使得这棵二叉树不再
# 是搜索二叉树，请找到这两个错误节点并返回。
# 已知二叉树中所有节点的值都不一样，给定二叉树的头节点 head，返回一个长度为2的
# 二叉树节点类型的数组errs，errs[0]表示一个错误节点， errs[1]表示另一个错误节
# 点。
# 进阶:
# 如果在原问题中得到了这两个错误节点，我们当然可以通过交换两个节点的节点值的方
# 式让整棵二叉树重新成为搜索二叉树。
# 但现在要求你不能这么做，而是在结构上完全交换两个节点的位置，请实现调整的函数。
class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# 利用非递归的中序遍历，找出降序的节点
def getTwoErrNodes(head):
    errs = [None] * 2
    if head is None:
        return errs
    stack = []
    pre = None
    while stack or head:
        if head:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            if (pre is not None) and (pre.val > head.val):
                errs[0] = pre if (errs[0] is None) else errs[0]
                errs[1] = head
            pre = head
            head = head.right
    return errs


# 获取两个错误节点的父节点并返回
def getTwoErrParents(head, e1, e2):
    parents = [None, None]
    if head is None:
        return parents
    stack = []
    while stack or head:
        if head:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            if head.left == e1 or head.right == e1:
                parents[0] = head
            if head.left == e2 or head.right == e2:
                parents[1] = head
            head = head.right
    return parents


# 恢复搜索二叉树，将乱序的两个节点恢复原来的位置
def recoverTree(head):
    errs = getTwoErrNodes(head)
    parents = getTwoErrParents(head, errs[0], errs[1])
    e1, e2 = errs[0], errs[1]
    e1p, e2p = parents[0], parents[1]
    e1l, e1r = e1.left, e1.right
    e2l, e2r = e2.left, e2.right
    if e1 == head:
        if e1 == e2p:
            e1.left = e2l
            e1.right = e2r
            e2.right = e1
            e2.left = e1l
        elif e2p.left == e2:
            e2p.left = e1
            e2.left = e1l
            e2.right = e1r
            e1.left = e2l
            e1.right = e2r
        else:
            e2p.right = e1
            e2.left = e1l
            e2.right = e1r
            e1.left = e2l
            e1.right = e2r
        head = e2
    elif e2 == head:
        if e2 == e1p:
            e2.left = e1l
            e2.right = e1r
            e1.right = e2
            e1.left = e2l
        elif e1p.left == e1:
            e1p.left = e2
            e1.left = e2l
            e1.right = e2r
            e2.left = e1l
            e2.right = e1r
        else:
            e1p.right = e2
            e1.left = e2l
            e1.right = e2r
            e2.left = e1l
            e2.right = e1r
        head = e1
    else:
        if e1 == e2p:
            if e1p.left == e1:
                e1p.left = e2
                e1.left = e2l
                e1.right = e2r
                e2.left = e1l
                e2.right = e1
            else:
                e1p.right = e2
                e1.left = e2l
                e1.right = e2r
                e2.left = e1l
                e2.right = e1
        elif e2 == e1p:
            if e2p.left == e2:
                e2p.left = e1
                e2.left = e1l
                e2.right = e1r
                e1.left = e2
                e1.right = e2r
            else:
                e2p.right = e1
                e2.left = e1l
                e2.right = e1r
                e1.left = e2
                e1.right = e2r
        else:
            if e1p.left == e1:
                if e2p.left == e2:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.left = e2
                    e2p.left = e1
                else:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.left = e2
                    e2p.right = e1
            else:
                if e2p.left == e2:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.right = e2
                    e2p.left = e1
                else:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.right = e2
                    e2p.right = e1
    return head


head = Node(7)
head.left = Node(3)
head.right = Node(5)
head.left.left = Node(2)
head.left.right = Node(4)
head.right.left = Node(6)
head.right.right = Node(8)
head.left.left.left = Node(1)
errs = getTwoErrNodes(head)
print(f'错误节点：{errs[0].val}，{errs[1].val}')
head = recoverTree(head)
errs = getTwoErrNodes(head)
print(f'错误节点：{errs[0].val if (errs[0] is not None) else None}，{errs[1].val if (errs[1] is not None) else None}')
