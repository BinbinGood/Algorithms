class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


class BinaryTree(object):
    def __init__(self):
        self.head = None


# 先序递归遍历
def preOrderRecur(head):
    if head is None:
        return
    print(head.value)
    preOrderRecur(head.left)
    preOrderRecur(head.right)


# 中序递归遍历
def inOrderRecur(head):
    if head is None:
        return
    inOrderRecur(head.left)
    print(head.value)
    inOrderRecur(head.right)


# 后序递归遍历
def posOrderRecur(head):
    if head is None:
        return
    posOrderRecur(head.left)
    posOrderRecur(head.right)
    print(head.value)


# 先序非递归遍历
def preOrderUnRecur(head):
    if head:
        stack = [head]
        while stack:
            head = stack.pop()
            print(head.value)
            if head.right:
                stack.append(head.right)
            if head.left:
                stack.append(head.left)


# 中序非递归遍历
def inOrderUnRecur(head):
    if head:
        stack = []
        while stack or head:
            if head:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                print(head.value)
                head = head.right


# 后序非递归遍历
def posOrderUnRecur(head):
    if head:
        stack = [head]
        stack1 = []
        while stack:
            head = stack.pop()
            stack1.append(head)
            if head.left:
                stack.append(head.left)
            if head.right:
                stack.append(head.right)
        while stack1:
            print(stack1.pop().value)


if __name__ == "__main__":
    bt1 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n6 = Node(6)
    n7 = Node(7)
    n3 = Node(3, n6, n7)
    bt1.head = Node(1, n2, n3)

    print("------先序递归遍历-------")
    preOrderRecur(bt1.head)
    print("------中序递归遍历-------")
    inOrderRecur(bt1.head)
    print("------后序递归遍历-------")
    posOrderRecur(bt1.head)
    print("------先序非递归遍历-------")
    preOrderUnRecur(bt1.head)
    print("------中序非递归遍历-------")
    inOrderUnRecur(bt1.head)
    print("------后序非递归遍历-------")
    posOrderUnRecur(bt1.head)
