class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# morris 遍历
def Morris(head):
    if head is None:
        return
    cur = head
    mostRight = None
    while cur is not None:
        mostRight = cur.left
        if mostRight:  # 左孩子存在
            while mostRight.right is not None and mostRight.right != cur:  # 得到左孩子树上的最右节点
                mostRight = mostRight.right
            if mostRight.right is None:  # 如果最右节点为空
                mostRight.right = cur
                print(cur.value, end=' ')
                cur = cur.left
                continue  # 跳过下面的语句继续执行while循环
            else:  # 最右节点不为空
                mostRight.right = None
        print(cur.value, end=' ')
        cur = cur.right  # 此语句情况一和情况二的b情况共用


# morris 先序遍历
def Morrispre(head):
    if head is None:
        return
    cur = head
    mostRight = None
    while cur is not None:
        mostRight = cur.left
        if mostRight:  # 左孩子存在
            while mostRight.right is not None and mostRight.right != cur:  # 得到左孩子树上的最右节点
                mostRight = mostRight.right
            if mostRight.right is None:  # 如果最右节点为空,第一次到达
                mostRight.right = cur
                print(cur.value, end=' ')
                cur = cur.left
                continue  # 跳过下面的语句继续执行while循环
            else:  # 最右节点不为空,第二次到达
                mostRight.right = None
        else:
            print(cur.value, end=' ')
        cur = cur.right  # 此语句情况一和情况二的b情况共用


# morris中序遍历
def Morrisin(head):
    if head is None:
        return
    cur = head
    mostRight = None
    while cur is not None:
        mostRight = cur.left
        if mostRight:  # 左孩子存在
            while mostRight.right is not None and mostRight.right != cur:  # 得到左孩子树上的最右节点
                mostRight = mostRight.right
            if mostRight.right is None:  # 如果最右节点为空
                mostRight.right = cur
                cur = cur.left
                continue  # 跳过下面的语句继续执行while循环
            else:  # 最右节点不为空
                mostRight.right = None
        print(cur.value, end=' ')
        cur = cur.right  # 此语句情况一和情况二的b情况共用


# morris后序遍历
def Morrispos(head):
    if head is None:
        return
    cur = head
    mostRight = None
    while cur is not None:
        mostRight = cur.left
        if mostRight:  # 左孩子存在
            while mostRight.right is not None and mostRight.right != cur:  # 得到左孩子树上的最右节点
                mostRight = mostRight.right
            if mostRight.right is None:  # 如果最右节点为空，第一次到达
                mostRight.right = cur
                cur = cur.left
                continue  # 跳过下面的语句继续执行while循环
            else:  # 最右节点不为空，第二次到达
                mostRight.right = None
                printRightEdge(cur.left)  # 第二次到达的节点，逆序打印左树的右边界
        cur = cur.right  # 此语句情况一（左孩子不存在）和情况二的b情况（左孩子存在第二次到达的节点）共用
    printRightEdge(head)  # 结束后逆序打印整棵树的右边界


def printRightEdge(node):
    tail = reverseRightEdge(node)
    cur = tail
    while cur:
        print(cur.value, end=' ')
        cur = cur.right
    reverseRightEdge(tail)


def reverseRightEdge(node):
    if node is None:
        return None
    cur = node
    pre = None
    while cur:
        temp = cur.right
        cur.right = pre
        pre = cur
        cur = temp
    return pre


if __name__ == "__main__":
    headnode = Node(1)
    headnode.left = Node(2)
    headnode.left.left = Node(4)
    headnode.left.right = Node(5)
    headnode.right = Node(3)
    headnode.right.left = Node(6)
    headnode.right.right = Node(7)
    print("------Morris遍历--------")
    Morris(headnode)
    print("\n------Morris先序遍历--------")
    Morrispre(headnode)
    print("\n------Morris中序遍历--------")
    Morrisin(headnode)
    print("\n------Morris后序遍历--------")
    Morrispos(headnode)
