class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.head = None

# 先序遍历保存
def serialByPre(head):
    if head is None:
        return "#_"
    curstr = str(head.value) + "_"
    curstr += serialByPre(head.left)
    curstr += serialByPre(head.right)
    return curstr


def reconByPreString(str):
    if len(str)==0:
        return
    str1 = str.split("_")
    queue=[]
    for i in str1:
        if i != '':
            queue.append(i)
    return reconPreOrder(queue)


def reconPreOrder(queue):
    value = queue.pop(0)
    if value == "#":
        return None
    head = Node(value)
    head.left = reconPreOrder(queue)
    head.right = reconPreOrder(queue)

    return head


if __name__ == "__main__":
    bt1 = BinaryTree()
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n6 = Node(6)
    n7 = Node(7)
    n3 = Node(3, n6, n7)
    bt1.head = Node(1, n2, n3)
    print("-----序列化-----")
    str1 = serialByPre(bt1.head)
    print(str1)
    print("-----反序列化------")
    head = reconByPreString(str1)
    print(head.value)


