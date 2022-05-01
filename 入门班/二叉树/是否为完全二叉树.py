class Node():
    def __init__(self, value,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self):
        self.head = None

# 判断是否为完全二叉树使用宽度优先遍历
# 情况一：任意节点有又无左，返回False
# 情况二，在无违反情况一的条件下，如果遇到了第一个左右子不全（有左子无右子），则后续节点都是叶节点
def IsCBT(head):
    if head is None:
        return True
    queue = [head]
    leaf = False  # 标志变量，提示是否发现第一个左右子不全的节点
    while queue:
        head = queue.pop(0)
        # 如果lesf为True时，后续节点不是叶节点则返回False。或者有右子无左子返回False
        if (leaf and (head.left or head.left)) or ((head.left is None) and head.right):
            return False
        if head.left:
            queue.append(head.left)
        if head.right:
            queue.append(head.right)
        else:
            leaf = True
    return True



if __name__ == "__main__":
    bt1 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n6 = Node(6)
    n3 = Node(3, n6)
    bt1.head = Node(1, n2, n3)
    print("----是否为完全二叉树-----")
    print(IsCBT(bt1.head))
    bt2 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n7 = Node(7)
    n3 = Node(3, None, n7)
    bt2.head = Node(1, n2, n3)
    print(IsCBT(bt2.head))
