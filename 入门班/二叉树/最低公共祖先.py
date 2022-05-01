class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.head = None


# 使用哈希表，将二叉树哦所有节点和他的父节点保存
# 将nod1往上回溯的链保存，然后利用nod2进行回溯，然后再set1链里查找
def lowestAncestor(head, nod1, nod2):
    hashfathermap = {head: head}
    process(head, hashfathermap)
    set1 = []
    cur = nod1
    while cur != hashfathermap[cur]:  # 一直回溯到头节点
        set1.append(cur)
        cur = hashfathermap[cur]
    set1.append(head)
    cur = nod2
    while cur != hashfathermap[cur]:
        if cur in set1:
            return cur
        cur = hashfathermap[cur]
    return head

# 情况一nod1和nod2互为公共祖先
# 情况二nod1和nod2不互为公共祖先，回溯才能找到
def lowestAncestor2(head, nod1, nod2):
    if (head is None) or (head == nod1) or (head == nod2):
        return head
    left = lowestAncestor2(head.left, nod1, nod2)
    right = lowestAncestor2(head.right, nod1, nod2)
    if left and right:
        return head
    # 左右两边并不都为空则谁不为空返回谁
    if left:
        return left
    else:
        return right


def process(head, hashfathermap):
    if head is None:
        return
    hashfathermap[head.left] = head
    hashfathermap[head.right] = head
    process(head.left, hashfathermap)
    process(head.right, hashfathermap)


if __name__ == "__main__":
    bt1 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n7 = Node(7)
    n6 = Node(6)
    n3 = Node(3, n6, n7)
    bt1.head = Node(1, n2, n3)
    print("----方法一-----")
    comnode = lowestAncestor(bt1.head, n4, n6)
    print(comnode.value)
    print("----方法二-----")
    print(lowestAncestor2(bt1.head, n4, n6).value)
    bt2 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n7 = Node(7)
    n3 = Node(3, None, n7)
    bt2.head = Node(1, n2, n3)
