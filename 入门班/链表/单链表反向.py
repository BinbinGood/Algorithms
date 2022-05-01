class Node(object):
    # 节点
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkList(object):
    # 单向链表
    def __init__(self):
        self.head = None


def ReverseList(head):
    # 反转链表
    pre, cur = None, head
    while cur:
        temp = cur.next  # 临时变量保存后续节点
        cur.next = pre  # 将当前节点和前节点连接
        pre = cur  # 指向前节点的指针后移
        cur = temp  # 指向当前节点的指针也后移
    return pre


def PrintList(head):
    # 打印链表
    cur = head
    while cur:
        print(cur.value)
        cur = cur.next


if __name__ == "__main__":
    # 创建链表
    linklist = LinkList()
    linklist.head = Node(1)
    linklist.head.next = Node(2)
    linklist.head.next.next = Node(3)
    linklist.head.next.next.next = Node(4)
    linklist.head.next.next.next.next = Node(5)
    node = linklist.head
    # 遍历打印链表
    PrintList(node)
    node = ReverseList(node)
    PrintList(node)
