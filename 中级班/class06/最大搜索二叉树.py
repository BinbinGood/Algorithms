# 找到一棵二叉树中，最大的搜索二叉子树，返回最大搜索二叉子树的节点个数。

class ReturnType:
    def __init__(self, maxBSThead, isBST, minvalue, maxvalue, BSTsize):
        self.maxBSThead = maxBSThead
        self.isBST = isBST
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.maxBSTsize = BSTsize


def f(x):
    if x is None:
        return None
    leftinfo = f(x.left)
    rightinfo = f(x.right)

    minvalue = x.value
    maxvalue = x.value
    if leftinfo is not None:
        minvalue = min(minvalue, leftinfo.minvalue)
        maxvalue = max(maxvalue, leftinfo.maxvalue)
    if rightinfo is not None:
        minvalue = min(minvalue, rightinfo.minvalue)
        maxvalue = max(maxvalue, rightinfo.maxvalue)

    maxBSTsize = 0
    maxBSThead = None
    if leftinfo is not None:
        maxBSTsize = leftinfo.maxBSTsize
        maxBSThead = leftinfo.maxBSThead
    if rightinfo is not None:
        if rightinfo.maxBSTsize > maxBSTsize:
            maxBSTsize = rightinfo.maxBSTsize
            maxBSThead = rightinfo.maxBSThead

    isBST = False
    if ((leftinfo is None) or leftinfo.isBST) and ((rightinfo is None) or rightinfo.isBST):
        if ((leftinfo is None) or leftinfo.maxvalue < x.value) and (
                (rightinfo is None) or rightinfo.minvalue > x.value):
            isBST = True
            maxBSThead = x
            leftsize = 0 if (leftinfo is None) else leftinfo.maxBSTsize
            rightsize = 0 if (rightinfo is None) else rightinfo.maxBSTsize
            maxBSTsize = leftsize + rightsize + 1
    return ReturnType(maxBSThead, isBST, minvalue, maxvalue, maxBSTsize)


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


if __name__ == "__main__":
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
    print("----------中序遍历最大搜索二叉树----------")
    maxBSThead = f(head).maxBSThead
    # print(maxBSThead)
    inorderprint(maxBSThead)
    print()
    print('----------------------测试二-------------------')
    head = Node(3)
    head.left = Node(5)
    head.right = Node(7)
    head.left.left = Node(1)
    head.left.right = Node(6)
    head.left.left.right = Node(2)
    head.right.left = Node(4)
    head.right.right = Node(8)
    head.right.left.left = Node(2)
    head.right.left.right = Node(10)
    head.right.left.left.left = Node(1)
    head.right.right.right = Node(9)
    print("----------中序遍历二叉树----------")
    inorderprint(head)
    print()
    print("----------中序遍历最大搜索二叉树----------")
    maxBSThead = f(head).maxBSThead
    # print(maxBSThead)
    inorderprint(maxBSThead)